#!/usr/bin/env python3
"""criterio · analizador de historial (v0.1)

Lee exportaciones de ChatGPT, Claude y Gemini, filtra conversaciones,
pre-marca conductas de la rúbrica con señales de texto y escribe:

  - resultados.json : datos crudos
  - reporte.html    : informe para leer en el navegador
  - lotes/*.md      : conversaciones en bloques, por si quieres que un
                      modelo las clasifique con la rúbrica completa

Privacidad: este archivo solo usa la biblioteca estándar de Python y no
abre ninguna conexión de red. Todo se queda en tu equipo.

Uso:
  python3 analizar.py --entrada conversations.json
  python3 analizar.py --entrada export.zip --desde 2026-01-01 --salida mi-reporte
"""

from __future__ import annotations

import argparse
import html
import json
import random
import re
import sys
import unicodedata
import zipfile
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from string import Template

VERSION = "0.1.0"

# ---------------------------------------------------------------------------
# Modelo común
# ---------------------------------------------------------------------------


@dataclass
class Turno:
    rol: str  # "usuario" | "ia"
    texto: str
    fecha: datetime | None = None


@dataclass
class Conversacion:
    id: str
    titulo: str
    fuente: str  # "chatgpt" | "claude" | "gemini"
    creada: datetime | None
    turnos: list[Turno] = field(default_factory=list)

    @property
    def turnos_usuario(self) -> list[Turno]:
        return [t for t in self.turnos if t.rol == "usuario"]


def _fecha(valor) -> datetime | None:
    if valor is None or valor == "":
        return None
    try:
        if isinstance(valor, (int, float)):
            return datetime.fromtimestamp(valor, tz=timezone.utc)
        texto = str(valor).replace("Z", "+00:00")
        f = datetime.fromisoformat(texto)
        return f if f.tzinfo else f.replace(tzinfo=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


# ---------------------------------------------------------------------------
# Lectores por plataforma
# ---------------------------------------------------------------------------


def leer_chatgpt(datos: list) -> list[Conversacion]:
    """conversations.json de ChatGPT: cada conversación es un árbol en `mapping`.
    Seguimos la rama activa desde `current_node` hacia la raíz."""
    salida = []
    for c in datos:
        mapping = c.get("mapping") or {}
        nodo_id = c.get("current_node")
        cadena = []
        vistos = set()
        while nodo_id and nodo_id in mapping and nodo_id not in vistos:
            vistos.add(nodo_id)
            nodo = mapping[nodo_id]
            cadena.append(nodo)
            nodo_id = nodo.get("parent")
        if not cadena:  # sin current_node: orden por fecha
            cadena = sorted(
                mapping.values(),
                key=lambda n: ((n.get("message") or {}).get("create_time") or 0),
                reverse=True,
            )
        turnos = []
        for nodo in reversed(cadena):
            msg = nodo.get("message") or {}
            rol = (msg.get("author") or {}).get("role")
            if rol not in ("user", "assistant"):
                continue
            if (msg.get("metadata") or {}).get("is_visually_hidden_from_conversation"):
                continue
            partes = (msg.get("content") or {}).get("parts") or []
            texto = "\n".join(p for p in partes if isinstance(p, str)).strip()
            if not texto:
                continue
            turnos.append(Turno("usuario" if rol == "user" else "ia", texto, _fecha(msg.get("create_time"))))
        salida.append(
            Conversacion(
                id=str(c.get("id") or c.get("conversation_id") or len(salida)),
                titulo=c.get("title") or "(sin título)",
                fuente="chatgpt",
                creada=_fecha(c.get("create_time")),
                turnos=turnos,
            )
        )
    return salida


def leer_claude(datos: list) -> list[Conversacion]:
    """conversations.json de claude.ai: lista en `chat_messages`. Si la persona
    editó mensajes hay ramas (`parent_message_uuid`); seguimos la rama activa
    desde el mensaje más reciente hacia la raíz."""
    salida = []
    for c in datos:
        mensajes = c.get("chat_messages") or []
        if mensajes and all("parent_message_uuid" in m for m in mensajes):
            por_id = {m.get("uuid"): m for m in mensajes}
            actual = max(mensajes, key=lambda m: m.get("created_at") or "").get("uuid")
            rama = []
            while actual in por_id and por_id[actual] not in rama:
                rama.append(por_id[actual])
                actual = por_id[actual].get("parent_message_uuid")
            mensajes = list(reversed(rama))
        turnos = []
        for m in mensajes:
            rol = m.get("sender")
            if rol not in ("human", "assistant"):
                continue
            bloques = m.get("content") or []
            texto = "\n".join(
                b.get("text", "") for b in bloques if isinstance(b, dict) and b.get("type") == "text"
            ).strip() or (m.get("text") or "").strip()
            if not texto:
                continue
            turnos.append(Turno("usuario" if rol == "human" else "ia", texto, _fecha(m.get("created_at"))))
        salida.append(
            Conversacion(
                id=str(c.get("uuid") or len(salida)),
                titulo=c.get("name") or "(sin título)",
                fuente="claude",
                creada=_fecha(c.get("created_at")),
                turnos=turnos,
            )
        )
    return salida


class _SoloTexto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.partes: list[str] = []

    def handle_data(self, data):
        self.partes.append(data)


def _html_a_texto(fragmento: str) -> str:
    p = _SoloTexto()
    p.feed(fragmento or "")
    return re.sub(r"\s+\n", "\n", "".join(p.partes)).strip()


# EXPERIMENTAL: sin muestra real todavía. Google Takeout guarda cada pregunta
# como una "actividad" suelta, sin agrupar por conversación. Agrupamos por
# cercanía en el tiempo. El prefijo del título cambia según el idioma de la
# cuenta; si ves títulos raros, ajusta este patrón.
_PREFIJO_GEMINI = re.compile(r"^(Prompted|Instrucción dada|Instrucción|Solicitaste|Preguntaste)\s*:?\s*", re.I)
PAUSA_GEMINI = timedelta(minutes=30)


def leer_gemini(datos: list) -> list[Conversacion]:
    actividades = []
    for a in datos:
        cabecera = (a.get("header") or "") + " " + " ".join(a.get("products") or [])
        if "gemini" not in cabecera.lower() and "bard" not in cabecera.lower():
            continue
        pregunta = _PREFIJO_GEMINI.sub("", a.get("title") or "").strip()
        respuesta = " ".join(_html_a_texto(i.get("html", "")) for i in a.get("safeHtmlItem") or [])
        fecha = _fecha(a.get("time"))
        if pregunta:
            actividades.append((fecha, pregunta, respuesta))
    actividades.sort(key=lambda x: x[0] or datetime.min.replace(tzinfo=timezone.utc))

    salida: list[Conversacion] = []
    anterior = None
    for fecha, pregunta, respuesta in actividades:
        if not salida or anterior is None or fecha is None or fecha - anterior > PAUSA_GEMINI:
            salida.append(
                Conversacion(
                    id=f"gemini-{len(salida)}",
                    titulo=pregunta[:60],
                    fuente="gemini",
                    creada=fecha,
                )
            )
        salida[-1].turnos.append(Turno("usuario", pregunta, fecha))
        if respuesta:
            salida[-1].turnos.append(Turno("ia", respuesta, fecha))
        anterior = fecha
    return salida


LECTORES = {"chatgpt": leer_chatgpt, "claude": leer_claude, "gemini": leer_gemini}


def detectar_formato(datos) -> str | None:
    if not isinstance(datos, list) or not datos:
        return None
    muestra = next((d for d in datos if isinstance(d, dict)), {})
    if "mapping" in muestra:
        return "chatgpt"
    if "chat_messages" in muestra:
        return "claude"
    if "header" in muestra and "time" in muestra:
        return "gemini"
    return None


# Nombres de archivo con conversaciones. Las exportaciones nuevas de ChatGPT
# parten el historial en conversations-000.json, conversations-001.json, etc.
_ARCHIVO_CONVERSACIONES = re.compile(r"^(conversations(-\d+)?|myactivity|mi actividad)\.json$", re.I)


def _agregar(encontrados: list, texto: str) -> None:
    datos = json.loads(texto)
    fmt = detectar_formato(datos)
    if fmt:
        encontrados.append((fmt, datos))


def cargar(ruta: Path) -> list[tuple[str, list]]:
    """Devuelve [(formato, datos)]. Acepta un .json, el .zip de la exportación
    o la carpeta ya descomprimida."""
    encontrados: list = []
    if ruta.is_dir():
        for archivo in sorted(ruta.rglob("*.json")):
            if _ARCHIVO_CONVERSACIONES.match(archivo.name):
                _agregar(encontrados, archivo.read_text(encoding="utf-8"))
    elif ruta.suffix.lower() == ".zip":
        with zipfile.ZipFile(ruta) as z:
            for nombre in sorted(z.namelist()):
                if _ARCHIVO_CONVERSACIONES.match(nombre.rsplit("/", 1)[-1]):
                    _agregar(encontrados, z.read(nombre).decode("utf-8"))
    else:
        _agregar(encontrados, ruta.read_text(encoding="utf-8"))
    return encontrados


# ---------------------------------------------------------------------------
# Conductas y señales (pre-marcado heurístico)
# ---------------------------------------------------------------------------
# Las señales son pistas, no pruebas. Buscan en los turnos de la persona,
# sobre texto en minúscula y sin tildes. Ver rubrica/conductas.md.

NUCLEO = ["nota-contexto-faltante", "cuestiona-razonamiento", "verifica-datos", "decide-distinto"]


@dataclass(frozen=True)
class Conducta:
    id: str
    nombre: str
    dimension: str
    referencia: float | None  # % en el AI Fluency Index
    senales: tuple[str, ...]
    evidencia: tuple[str, ...] = ()  # qué la sube a "con evidencia"
    tras_respuesta: bool = False  # solo cuenta después de que la IA respondió


_RAZON = r"\b(porque|ya que|dado que|puesto que|debido a|pues el|pues la|because|since)\b"
_FUENTE = r"(https?://|\bsegun (el|la|los|las)\b|\bverifique\b|\brevise\b|\bbusque\b|\bencontre\b|\bconsulte\b|\bdice que\b|\bi checked\b|\baccording to\b)"
_DATO = r"\b\d+([.,]\d+)?\s?(%|por ciento|millones|pesos|usd)\b"

CONDUCTAS: tuple[Conducta, ...] = (
    Conducta(
        "itera", "Itera y afina", "Descripción", 85.7,
        (r"\b(cambia|ajusta|modifica|acorta|alarga|quita|agrega|anade|reescribe|resume mas|otra version|mejoralo|mejorala|hazlo mas|hazla mas)\b",
         r"\b(make it|shorten|rewrite|change the|add a|remove the)\b"),
        (_RAZON,), tras_respuesta=True,
    ),
    Conducta(
        "aclara-objetivo", "Aclara el objetivo antes de pedir", "Delegación", 51.1,
        (r"\b(necesito (esto|esta|este|un|una)\b.{0,60}\bpara (decidir|presentar|convencer|entregar|el trabajo)|el objetivo es|mi objetivo|lo que busco es|quiero lograr|la idea es que|es para (presentar|convencer|decidir|el trabajo))\b",
         r"\b(the goal is|i need this (to|for)|i'm trying to)\b"),
        (r"\b(decidir|aprobar|convencer|presentar a|entregar el|reunion|junta|comite|me importan?|lo que importa)\b",),
    ),
    Conducta(
        "da-ejemplos", "Muestra cómo se ve lo bueno", "Descripción", 41.1,
        (r"\b(como este|como esta|parecido a (este|esta)|algo asi como|toma como (modelo|referencia|ejemplo)|este es el estilo|te doy un ejemplo|por ejemplo:)",
         r"\b(like this one|here's an example|for example:)"),
        (r"\b(fijate en|nota que|lo que me gusta|lo bueno de|copia (el|la))\b",),
    ),
    Conducta(
        "pide-formato", "Dice qué formato y estructura necesita", "Descripción", 30.0,
        (r"\b(en (una )?tabla|en vinetas|en bullets|maximo \d+|menos de \d+|\d+ palabras|\d+ (secciones|parrafos|puntos)|en formato|con (esta|la siguiente) estructura)\b",
         r"\b(as a table|bullet points|in \d+ words|format it)\b"),
        (_RAZON, r"\b(lo voy a (proyectar|imprimir|enviar|leer en))\b"),
    ),
    Conducta(
        "fija-modo", "Define cómo quiere trabajar con la IA", "Descripción", 30.0,
        (r"\b(actua como|hazme preguntas|preguntame|paso a paso|no me des (la|el)|guiame|critica(lo|la|me)?|se (duro|critico|honesto)|abogado del diablo)\b",
         r"\b(act as|ask me questions|step by step|devil's advocate|be critical)\b"),
        (_RAZON, r"\b(para (prepararme|practicar|aprender)|quiero llegar|manana (lo|la) (presento|tengo)|me van a (preguntar|cuestionar))\b"),
    ),
    Conducta(
        "pide-tono", "Dice el tono y el estilo", "Descripción", 22.7,
        (r"\b(tono|mas formal|menos formal|cercano|sin tecnicismos|que suene|estilo (mas|menos)|tutear|de usted)\b",
         r"\b(tone|more formal|less formal|casual)\b"),
        (_RAZON, r"\b(es para (un|una) (cliente|jefe|gerente))\b"),
    ),
    Conducta(
        "nota-contexto-faltante", "Nota que a la IA le falta contexto", "Discernimiento", 20.3,
        (r"\b(en mi caso|para mi caso|no aplica|te falto|no sabes que|estas asumiendo|estas suponiendo|que supuestos|eso es (de|en) (espana|mexico|argentina|estados unidos|europa)|aqui en colombia|en colombia (no|el|la|los|las|se))\b",
         r"\b(doesn't apply|you're assuming|you don't know that|in my case)\b"),
        (_RAZON, r"\b(ley \d+|decreto|norma|resolucion|mi equipo (es|son)|somos \d+|en colombia (el|la|los|las|se)|cambia (el|la|lo)|justo eso|por eso)\b"),
        tras_respuesta=True,
    ),
    Conducta(
        "define-audiencia", "Dice para quién es el resultado", "Descripción", 17.6,
        (r"\b(es para (mis|los|las|un|una|el|la|docentes|estudiantes|gerentes|clientes|padres|ninos|jovenes)|para el publico|lo va(n)? a leer|mi publico|mis estudiantes|mis alumnos|la audiencia|el lector)\b",
         r"\b(the audience|it's for my|will be read by)\b"),
        (r"\b(que no (saben|conocen|leen|usan)|que (solo|ya) (quieren|saben|conocen)|les preocupa|a quienes|explicalo desde)\b",),
    ),
    Conducta(
        "cuestiona-razonamiento", "Cuestiona cuando el razonamiento no cuadra", "Discernimiento", 15.8,
        (r"\b(no cuadra|te contradices|contradice|no se sigue|de donde sale|por que concluyes|no tiene sentido|revisa el (paso|calculo)|eso no es asi|no es lo mismo|tu conclusion|no me convence|estas seguro)\b|\bseguro\?",
         r"\b(that doesn't follow|you contradict|why do you conclude|are you sure)\b"),
        (_RAZON, _DATO, r"\b(dijiste|arriba (dijiste|pusiste)|salta de|sin pasar por|solo (aprobaron|hay|son)|\d+ de \d+)\b"),
        tras_respuesta=True,
    ),
    Conducta(
        "consulta-enfoque", "Consulta el enfoque antes de ejecutar", "Delegación", 10.1,
        (r"\b(antes de (escribir|hacer|empezar)|como lo abordarias|como lo harias|propon(me)? un plan|dame (\w+ )?(opciones|enfoques|alternativas)|primero (el|un) (esquema|plan))\b",
         r"\b(how would you approach|propose a plan|before you (write|start))\b"),
        (r"\b(prefiero|me quedo con|elijo|la opcion \w+ porque)\b",),
    ),
    Conducta(
        "verifica-datos", "Pide fuente o verifica datos que importan", "Discernimiento", 8.7,
        (r"\b(fuente|de donde sale|donde dice|link|enlace|cita exacta|referencia|verifique|voy a verificar|lo voy a revisar|segun (el|la))\b",
         r"\b(source|citation|where does it say|i checked|let me verify)\b"),
        (_FUENTE,),
    ),
    Conducta(
        "decide-distinto", "Decide distinto a la IA, con argumento", "Discernimiento (propia)", None,
        (r"\b(prefiero|mejor (voy a|vamos a|hagamos)|no voy a|decidi|me quedo con|en cambio|no lo voy a hacer asi|hagamoslo (distinto|diferente))\b",
         r"\b(i'd rather|i prefer|i decided|instead i'll)\b"),
        (_RAZON,), tras_respuesta=True,
    ),
)

ESTADOS = ("ausente", "presente", "con_evidencia")


def normalizar(texto: str) -> str:
    sin_tildes = unicodedata.normalize("NFKD", texto)
    sin_tildes = "".join(ch for ch in sin_tildes if not unicodedata.combining(ch))
    return sin_tildes.lower()


def _cita(texto: str, inicio: int, fin: int, ancho: int = 220) -> str:
    a = max(0, inicio - ancho // 2)
    b = min(len(texto), fin + ancho // 2)
    return ("…" if a > 0 else "") + texto[a:b].strip() + ("…" if b < len(texto) else "")


def evaluar(conv: Conversacion) -> dict:
    """Estado por conducta para una conversación, con hasta 2 citas cada una."""
    resultado = {}
    for conducta in CONDUCTAS:
        estado = "ausente"
        citas = []
        ia_ya_respondio = False
        for i, turno in enumerate(conv.turnos):
            if turno.rol == "ia":
                ia_ya_respondio = True
                continue
            if conducta.tras_respuesta and not ia_ya_respondio:
                continue
            # Buscamos sobre el texto normalizado; como NFKD + quitar marcas
            # conserva la longitud en español, los índices sirven para citar.
            norm = normalizar(turno.texto)
            original = turno.texto if len(norm) == len(turno.texto) else norm
            for patron in conducta.senales:
                m = re.search(patron, norm)
                if not m:
                    continue
                con_ev = any(re.search(p, norm) for p in conducta.evidencia)
                nuevo = "con_evidencia" if con_ev else "presente"
                if ESTADOS.index(nuevo) > ESTADOS.index(estado):
                    estado = nuevo
                if len(citas) < 2:
                    citas.append({"turno": i, "estado": nuevo, "texto": _cita(original, m.start(), m.end())})
                break
        resultado[conducta.id] = {"estado": estado, "citas": citas}
    return resultado


# ---------------------------------------------------------------------------
# Filtros, lotes, agregados
# ---------------------------------------------------------------------------


def filtrar(convs, desde=None, hasta=None, min_turnos=2, buscar=None):
    salida = []
    for c in convs:
        if len(c.turnos_usuario) < min_turnos:
            continue
        if desde and c.creada and c.creada < desde:
            continue
        if hasta and c.creada and c.creada > hasta:
            continue
        if buscar:
            aguja = normalizar(buscar)
            if aguja not in normalizar(c.titulo) and not any(aguja in normalizar(t.texto) for t in c.turnos):
                continue
        salida.append(c)
    return salida


ENCABEZADO_LOTE = """# Lote {n} de {total} · criterio

Clasifica cada conversación con la rúbrica de criterio (`references/rubrica.md` de la skill
`revision-de-historial`, o `rubrica/conductas.md` en el repositorio).
Cada conversación empieza con una línea `=== CONVERSACIÓN id … ===` y termina con
`=== FIN DE LA CONVERSACIÓN ===`. Solo mira lo que escribe la Persona. Para cada una de las 12 conductas da el estado
(ausente, presente o con_evidencia) y, si no es ausente, la cita exacta de la persona
y la razón en una frase, hablándole a la persona ("Corregiste un supuesto de la IA
con un dato concreto").

Responde SOLO con un JSON así y guárdalo como `clasificacion_{n:03}.json`
junto a este archivo:

{{"conversaciones": [{{"id": "<id>", "conductas": {{
  "verifica-datos": {{"estado": "con_evidencia", "cita": "<frase exacta>", "razon": "<por qué>"}},
  "itera": {{"estado": "ausente"}}, ... las 12 ...}}}}]}}

Ids de conducta: {ids}

"""


def _recortar(texto: str, limite: int) -> str:
    return texto if len(texto) <= limite else texto[:limite] + f" […recortado, {len(texto) - limite} caracteres más]"


def armar_lotes(convs, max_caracteres=60_000, max_ia=600, max_persona=3_000) -> list[str]:
    """Los mensajes de la persona se recortan a max_persona: cuando pega un
    documento largo, el criterio casi nunca está en el documento pegado."""
    bloques = []
    for c in convs:
        fecha = c.creada.date() if c.creada else "sin fecha"
        lineas = [f"=== CONVERSACIÓN id {c.id} · {c.fuente} · {fecha} · {c.titulo} ===\n"]
        for t in c.turnos:
            texto = _recortar(t.texto, max_persona if t.rol == "usuario" else max_ia)
            lineas.append(f"**{'Persona' if t.rol == 'usuario' else 'IA'}:** {texto}\n")
        bloques.append("\n".join(lineas))
    lotes, actual = [], ""
    for b in bloques:
        if actual and len(actual) + len(b) > max_caracteres:
            lotes.append(actual)
            actual = ""
        actual += b + "\n=== FIN DE LA CONVERSACIÓN ===\n\n"
    if actual:
        lotes.append(actual)
    ids = ", ".join(c.id for c in CONDUCTAS)
    return [ENCABEZADO_LOTE.format(n=i + 1, total=len(lotes), ids=ids) + l for i, l in enumerate(lotes)]


def cargar_clasificacion(rutas: list[Path]) -> dict[str, dict]:
    """Lee los JSON que devuelve el modelo: {id: {conducta: "estado" | {"estado", "cita"}}}."""
    salida = {}
    for ruta in rutas:
        for conv in json.loads(ruta.read_text(encoding="utf-8")).get("conversaciones", []):
            salida[str(conv["id"])] = conv.get("conductas", {})
    return salida


def evaluar_con_modelo(conv: Conversacion, etiquetas: dict) -> dict:
    """Convierte la clasificación del modelo al mismo formato que evaluar()."""
    resultado = {}
    for c in CONDUCTAS:
        valor = etiquetas.get(c.id, "ausente")
        estado = valor if isinstance(valor, str) else valor.get("estado", "ausente")
        estado = estado.replace(" ", "_") if estado.replace(" ", "_") in ESTADOS else "ausente"
        cita = "" if isinstance(valor, str) else (valor.get("cita") or "").strip()
        razon = "" if isinstance(valor, str) else (valor.get("razon") or "").strip()
        citas = []
        if estado != "ausente":
            turno = next((i for i, t in enumerate(conv.turnos) if t.rol == "usuario" and cita and cita[:40] in t.texto), -1)
            citas.append({"turno": turno, "estado": estado, "texto": cita or "(el modelo no dio cita)", "razon": razon})
        resultado[c.id] = {"estado": estado, "citas": citas}
    return resultado


def agregar(convs, evaluaciones) -> dict:
    totales = {c.id: {e: 0 for e in ESTADOS} for c in CONDUCTAS}
    por_mes: dict[str, dict[str, int]] = {}
    for conv, ev in zip(convs, evaluaciones):
        mes = conv.creada.strftime("%Y-%m") if conv.creada else "sin-fecha"
        por_mes.setdefault(mes, {"conversaciones": 0, **{k: 0 for k in NUCLEO}})
        por_mes[mes]["conversaciones"] += 1
        for cid, r in ev.items():
            totales[cid][r["estado"]] += 1
            if cid in NUCLEO and r["estado"] != "ausente":
                por_mes[mes][cid] += 1
    # Fuerza = (con evidencia, presente). Así, a igual evidencia, pesa más la que al menos aparece.
    fuerza = {cid: (totales[cid]["con_evidencia"], totales[cid]["presente"]) for cid in NUCLEO}
    return {
        "totales": totales,
        "por_mes": dict(sorted(por_mes.items())),
        "con_criterio": sum(any(ev[cid]["estado"] == "con_evidencia" for cid in NUCLEO) for ev in evaluaciones),
        "mas_debil": min(NUCLEO, key=fuerza.get) if convs else None,
        "mas_fuerte": max(NUCLEO, key=fuerza.get) if convs else None,
    }


# ---------------------------------------------------------------------------
# Informe HTML
# ---------------------------------------------------------------------------
# La plantilla vive en reporte_plantilla.html. Todo va en línea: abrir el
# reporte no hace ninguna petición a internet.

# Versión corta; el coach tiene la versión larga en skills/coach/ejercicios.md.
EJERCICIOS = {
    "nota-contexto-faltante": "En tu próximo chat de trabajo, antes de aceptar la primera respuesta, pregúntale a la IA: «¿Qué estás suponiendo sobre mi situación?». Revisa la lista y corrige al menos un supuesto que no aplique a tu caso, diciendo por qué.",
    "cuestiona-razonamiento": "Toma una respuesta larga que ya aceptaste. Busca el paso donde la conclusión depende de un dato o un supuesto y pregunta: «¿Por qué de esto se sigue aquello?». Si no cuadra, di exactamente qué parte no cuadra.",
    "verifica-datos": "Elige la cifra o afirmación de la que más depende una decisión tuya en un chat reciente. Búscala en una fuente primaria (entidad, norma, informe) y vuelve al chat a contar qué encontraste.",
    "decide-distinto": "La próxima vez que la IA te recomiende algo, escribe antes de aceptarlo qué harías tú y por qué, en una línea. Si decides distinto, díselo con tu razón.",
}

MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
ETIQUETA_ESTADO = {"ausente": "ausente", "presente": "presente", "con_evidencia": "con evidencia"}
MAX_CITAS_POR_CONDUCTA = 40


def _pct(x: float) -> str:
    return f"{round(x * 100)} %"


def _num(x: float) -> str:
    return f"{x:.1f}".replace(".", ",")


def _resumen(res: dict) -> tuple[str, str]:
    e = html.escape
    n = res["meta"]["conversaciones"]
    tot = res["agregado"]["totales"]
    nombres = {c.id: c.nombre.lower() for c in CONDUCTAS}
    if n == 0:
        return "<p>No quedó ninguna conversación después de los filtros. Prueba con <code>--min-turnos 1</code> o sin filtro de fechas.</p>", ""
    con_alguna = res["agregado"]["con_criterio"]
    if res["meta"]["modo"] == "heuristico":
        vistos = sum(tot[c]["presente"] + tot[c]["con_evidencia"] for c in NUCLEO)
        frases = [
            f"<p>Revisamos <b>{n}</b> conversaciones. El script alcanzó a ver <b>{vistos}</b> momentos de criterio "
            f"(pedir fuente, notar contexto faltante, cuestionar el razonamiento o decidir distinto), "
            f"y en <b>{con_alguna}</b> conversaciones al menos uno venía con evidencia.</p>",
            "<p><b>Esto es un piso, no tu retrato.</b> El script busca frases típicas y se le escapa buena parte de lo que haces: "
            "en nuestras pruebas vio menos de la mitad de estos momentos. Por eso este reporte no te dice cuál es tu conducta más débil.</p>",
        ]
        cifras = "".join(
            f'<div class="cifra tarjeta"><div class="n">{v}</div><div class="l">{e(l)}</div></div>'
            for v, l in [(n, "conversaciones analizadas"), (vistos, "momentos de criterio vistos por el script"),
                         (", ".join(res["meta"]["fuentes"]) or "—", "fuentes")]
        )
        return "".join(frases), cifras
    frases = [
        f"<p>Revisamos <b>{n}</b> conversaciones. En <b>{con_alguna}</b> diste al menos una muestra de criterio con evidencia: "
        f"un argumento, una fuente o un dato que se puede revisar.</p>"
    ]
    fuerte, debil = res["agregado"]["mas_fuerte"], res["agregado"]["mas_debil"]
    if tot[fuerte]["con_evidencia"]:
        frases.append(
            f"<p>Tu conducta de criterio más fuerte es <b>{e(nombres[fuerte])}</b>: "
            f"aparece con evidencia en {tot[fuerte]['con_evidencia']} de {n} conversaciones.</p>"
        )
    else:
        frases.append("<p>Ninguna conducta del núcleo de criterio apareció con evidencia. Eso puede ser real o puede ser que el script no la vio: revisa las citas más abajo.</p>")
    frases.append(
        f"<p>La que más espacio tiene para crecer es <b>{e(nombres[debil])}</b> "
        f"({tot[debil]['con_evidencia']} con evidencia y {tot[debil]['presente']} sin sustento).</p>"
    )
    it = tot["itera"]
    frases.append(
        f"<p>Iteraste en {it['presente'] + it['con_evidencia']} de {n} conversaciones. Iterar es útil, pero no es lo mismo que dudar: "
        f"importa más <i>cómo</i> corriges que cuántas veces.</p>"
    )
    cifras = "".join(
        f'<div class="cifra tarjeta"><div class="n">{v}</div><div class="l">{e(l)}</div></div>'
        for v, l in [
            (n, "conversaciones analizadas"),
            (con_alguna, "con criterio y evidencia"),
            (sum(tot[c]["con_evidencia"] for c in NUCLEO), "momentos de criterio con evidencia"),
            (", ".join(res["meta"]["fuentes"]) or "—", "fuentes"),
        ]
    )
    return "".join(frases), cifras


def _barras(res: dict) -> tuple[str, str]:
    e = html.escape
    n = res["meta"]["conversaciones"] or 1
    tot = res["agregado"]["totales"]
    grupos = [
        ("Núcleo de criterio", [c for c in CONDUCTAS if c.id in NUCLEO]),
        ("Delegación", [c for c in CONDUCTAS if c.dimension == "Delegación"]),
        ("Descripción", [c for c in CONDUCTAS if c.dimension == "Descripción"]),
    ]
    partes, filas_tabla = [], []
    for titulo, conductas in grupos:
        partes.append(f"<h3>{e(titulo)}</h3>")
        for c in sorted(conductas, key=lambda c: -(tot[c.id]["con_evidencia"] + tot[c.id]["presente"])):
            t = tot[c.id]
            segmentos = "".join(
                f'<span class="{cls}" style="flex-grow:{t[k]}"></span>'
                for k, cls in (("con_evidencia", "s-ev"), ("presente", "s-pre"), ("ausente", "s-aus"))
                if t[k]
            )
            ref = f'<i class="ref" style="left:{c.referencia}%"></i>' if c.referencia is not None else ""
            ref_txt = f"Index: {_num(c.referencia)} %" if c.referencia is not None else "Sin referencia (conducta propia)"
            tip = (
                f"<b>{e(c.nombre)}</b>Con evidencia: {t['con_evidencia']} ({_pct(t['con_evidencia'] / n)})<br>"
                f"Presente: {t['presente']} ({_pct(t['presente'] / n)})<br>Ausente: {t['ausente']}<br>"
                f"Aparece en total: {_pct((t['con_evidencia'] + t['presente']) / n)} · {ref_txt}"
            )
            partes.append(
                f'<div class="fila" tabindex="0" data-tip="{e(tip)}" '
                f'aria-label="{e(c.nombre)}: {t["con_evidencia"]} con evidencia, {t["presente"]} presente, {t["ausente"]} ausente">'
                f'<div class="nombre">{e(c.nombre)}</div>'
                f'<div class="barra" aria-hidden="true">{segmentos}{ref}</div>'
                f'<div class="valor">{_pct(t["con_evidencia"] / n)} con evid.<br>{_pct(t["presente"] / n)} presente</div></div>'
            )
            filas_tabla.append(
                f"<tr><td>{e(c.nombre)}</td><td>{e(c.dimension)}</td><td>{t['con_evidencia']}</td>"
                f"<td>{t['presente']}</td><td>{t['ausente']}</td>"
                f"<td>{_num(c.referencia) + ' %' if c.referencia is not None else '—'}</td></tr>"
            )
    tabla = (
        "<table><tr><th>Conducta</th><th>Dimensión</th><th>Con evidencia</th><th>Presente</th>"
        "<th>Ausente</th><th>Referencia Index</th></tr>" + "".join(filas_tabla) + "</table>"
    )
    return "".join(partes), tabla


def _linea(res: dict) -> str:
    e = html.escape
    meses = [(m, v) for m, v in res["agregado"]["por_mes"].items() if m != "sin-fecha"]
    if len(meses) < 2:
        return '<p class="nota tarjeta">Hace falta más de un mes de conversaciones para ver cambios en el tiempo.</p>'
    nombres = {c.id: c.nombre for c in CONDUCTAS}
    colores = {cid: f"var(--s{i + 1})" for i, cid in enumerate(NUCLEO)}
    W, H, L, R, T, B = 660, 250, 36, 175, 12, 30
    ancho, alto = W - L - R, H - T - B
    x = lambda i: L + (ancho * i / (len(meses) - 1))
    y = lambda v: T + alto * (1 - v)
    svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Evolución mensual del núcleo de criterio">']
    for v in (0, 0.25, 0.5, 0.75, 1):
        svg.append(f'<line class="{"base" if v == 0 else "rejilla"}" x1="{L}" x2="{L + ancho}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>')
        svg.append(f'<text x="{L - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{round(v * 100)}%</text>')
    paso = max(1, len(meses) // 8)
    for i, (m, _) in enumerate(meses):
        if i % paso == 0 or i == len(meses) - 1:
            anio, mes = m.split("-")
            svg.append(f'<text x="{x(i):.1f}" y="{H - 10}" text-anchor="middle">{MESES[int(mes) - 1]} {anio[2:]}</text>')
    svg.append(f'<line class="cruz" x1="0" x2="0" y1="{T}" y2="{T + alto}"/>')
    finales = []
    for cid in NUCLEO:
        vals = [v[cid] / v["conversaciones"] if v["conversaciones"] else 0 for _, v in meses]
        pts = " ".join(f"{x(i):.1f},{y(val):.1f}" for i, val in enumerate(vals))
        svg.append(f'<polyline class="serie" style="stroke:{colores[cid]}" points="{pts}"/>')
        svg.append(f'<circle r="4" cx="{x(len(vals) - 1):.1f}" cy="{y(vals[-1]):.1f}" style="fill:{colores[cid]}"/>')
        finales.append([y(vals[-1]), cid])
    # etiquetas directas al final de cada línea, sin que se monten
    finales.sort()
    for i in range(1, len(finales)):
        finales[i][0] = max(finales[i][0], finales[i - 1][0] + 15)
    for yy, cid in finales:
        corto = {"nota-contexto-faltante": "Contexto faltante", "cuestiona-razonamiento": "Cuestiona razonamiento",
                 "verifica-datos": "Verifica datos", "decide-distinto": "Decide distinto"}[cid]
        svg.append(f'<rect x="{L + ancho + 10}" y="{yy - 4:.1f}" width="10" height="8" rx="2" style="fill:{colores[cid]}"/>')
        svg.append(f'<text class="etq" x="{L + ancho + 25}" y="{yy + 4:.1f}">{corto}</text>')
    # zonas de hover por mes
    col = ancho / (len(meses) - 1)
    for i, (m, v) in enumerate(meses):
        anio, mes = m.split("-")
        filas = "".join(
            f"<br>{e(nombres[cid])}: {_pct(v[cid] / v['conversaciones'])}" for cid in NUCLEO
        )
        tip = f"<b>{MESES[int(mes) - 1]} {anio}</b>{v['conversaciones']} conversaciones{filas}"
        x0 = max(L, x(i) - col / 2)
        x1 = min(L + ancho, x(i) + col / 2)
        svg.append(f'<rect class="zona" x="{x0:.1f}" y="{T}" width="{x1 - x0:.1f}" height="{alto}" data-x="{x(i):.1f}" data-tip="{e(tip)}"/>')
    svg.append("</svg>")
    leyenda = "".join(
        f'<span><i class="muestra" style="background:{colores[cid]}"></i>{e(nombres[cid])}</span>' for cid in NUCLEO
    )
    return f'<div class="grafica tarjeta"><div class="leyenda">{leyenda}</div>{"".join(svg)}</div>'


def _verifica(res: dict) -> str:
    e = html.escape
    orden = [c for c in CONDUCTAS if c.id in NUCLEO] + [c for c in CONDUCTAS if c.id not in NUCLEO]
    bloques = []
    for c in orden:
        items = []
        for conv in res["conversaciones"]:
            for cita in conv["conductas"][c.id]["citas"]:
                items.append((conv, cita))
        items.sort(key=lambda it: (it[1]["estado"] != "con_evidencia", it[0]["fecha"] or ""))
        total = len(items)
        lis = []
        for conv, cita in items[:MAX_CITAS_POR_CONDUCTA]:
            clave = f"{conv['id']}|{c.id}|{cita['turno']}"
            lis.append(
                f'<li data-clave="{e(clave)}" data-conv="{e(conv["id"])}" data-conducta="{c.id}" '
                f'data-turno="{cita["turno"]}" data-estado="{cita["estado"]}">'
                f"<blockquote>«{e(cita['texto'])}»</blockquote>"
                + (f'<p class="razon"><b>Por qué:</b> {e(cita["razon"])}</p>' if cita.get("razon") else "")
                + '<div class="meta">'
                f'<span class="etiqueta">{ETIQUETA_ESTADO[cita["estado"]]}</span>'
                f"<span>{e(conv['titulo'])} · {e(conv['fecha'] or 'sin fecha')} · {e(conv['fuente'])}</span>"
                f'<button type="button" class="desacuerdo" aria-pressed="false">No estoy de acuerdo</button></div></li>'
            )
        mas = (
            f'<p class="nota">Y {total - MAX_CITAS_POR_CONDUCTA} más en <code>resultados.json</code>.</p>'
            if total > MAX_CITAS_POR_CONDUCTA else ""
        )
        vacio = ("El script no encontró frases típicas de esta conducta. Eso no quiere decir que no esté."
                 if res["meta"]["modo"] == "heuristico" else "No apareció en las conversaciones clasificadas.")
        cuerpo = f'<ul class="citas">{"".join(lis)}</ul>{mas}' if lis else f'<p class="nota">{vacio}</p>'
        abierta = res["meta"]["modo"] == "modelo" and c.id == res["agregado"]["mas_debil"]
        bloques.append(
            f'<details{" open" if abierta else ""}><summary>{e(c.nombre)} '
            f'<span class="cuenta">· {total} cita{"s" if total != 1 else ""}</span></summary>{cuerpo}</details>'
        )
    return "".join(bloques)


COMO_COMPLETAR = (
    "<p>Para saber de verdad dónde estás fuerte y dónde flojo, pídele a Claude que clasifique tus conversaciones con la rúbrica:</p>"
    "<ol><li>Abre la carpeta <code>lotes/</code>, junto a este reporte.</li>"
    "<li>En Claude (o Claude Code con la skill <code>revision-de-historial</code>), pásale cada lote y pídele que lo clasifique. "
    "Cada lote trae las instrucciones adentro.</li>"
    "<li>Guarda las respuestas como <code>clasificacion_001.json</code>, <code>clasificacion_002.json</code>… y vuelve a correr el script con "
    "<code>--clasificacion lotes/clasificacion_*.json</code>.</li></ol>"
    '<p class="nota">Ojo: en ese paso el texto de tus chats sí pasa por el modelo. El script, por sí solo, no envía nada.</p>'
)


def _paso(res: dict) -> str:
    if res["meta"]["modo"] == "heuristico":
        return COMO_COMPLETAR
    debil = res["agregado"]["mas_debil"]
    if not debil:
        return "<p>Cuando haya conversaciones analizadas, aquí aparece un ejercicio.</p>"
    nombre = next(c.nombre for c in CONDUCTAS if c.id == debil)
    return (
        f"<p><b>Practica: {html.escape(nombre.lower())}.</b></p><p>{html.escape(EJERCICIOS[debil])}</p>"
        '<p class="nota">Si usas la skill <code>coach</code>, pídele «dame un ejercicio» y te propone otro según tu reporte.</p>'
    )


AVISOS = {
    "heuristico": "<b>Pre-marcado automático: ve poco.</b> El script busca frases típicas y se le escapa buena parte de lo que haces. "
                  "Lo que sí marca suele ser cierto; revisa las citas en «Verifica tú mismo». Para el reporte completo, mira el final.",
    "modelo": "<b>Clasificado por un modelo con la rúbrica.</b> Es mejor que el pre-marcado, pero también se equivoca. "
              "Revisa las citas en «Verifica tú mismo» y decide tú si acertó.",
}


def escribir_html(ruta: Path, resultados: dict) -> None:
    plantilla = Template((Path(__file__).with_name("reporte_plantilla.html")).read_text(encoding="utf-8"))
    meta = resultados["meta"]
    resumen, cifras = _resumen(resultados)
    barras, tabla = _barras(resultados)
    fechas = sorted(c["fecha"] for c in resultados["conversaciones"] if c["fecha"])
    rango = f" · del {fechas[0]} al {fechas[-1]}" if fechas else ""
    ruta.write_text(
        plantilla.substitute(
            subtitulo=html.escape(f"{meta['conversaciones']} conversaciones{rango}"),
            resumen=resumen,
            cifras=cifras,
            barras=barras,
            tabla=tabla,
            linea=_linea(resultados),
            verifica=_verifica(resultados),
            paso=_paso(resultados),
            aviso=AVISOS[meta["modo"]],
            titulo_paso="Tu siguiente paso" if meta["modo"] == "modelo" else "Cómo tener el reporte completo",
            version=VERSION,
            generado=meta["generado"][:10],
            id_reporte=html.escape(meta["generado"]),
        ),
        encoding="utf-8",
    )

# ---------------------------------------------------------------------------
# Programa
# ---------------------------------------------------------------------------


def analizar(convs: list[Conversacion], clasificacion: dict | None = None) -> dict:
    if clasificacion is not None:
        convs = [c for c in convs if c.id in clasificacion]
        evaluaciones = [evaluar_con_modelo(c, clasificacion[c.id]) for c in convs]
    else:
        evaluaciones = [evaluar(c) for c in convs]
    return {
        "meta": {
            "version": VERSION,
            "modo": "modelo" if clasificacion is not None else "heuristico",
            "generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "conversaciones": len(convs),
            "fuentes": sorted({c.fuente for c in convs}),
        },
        "agregado": agregar(convs, evaluaciones),
        "conversaciones": [
            {
                "id": c.id,
                "titulo": c.titulo,
                "fuente": c.fuente,
                "fecha": c.creada.date().isoformat() if c.creada else None,
                "turnos_usuario": len(c.turnos_usuario),
                "conductas": ev,
            }
            for c, ev in zip(convs, evaluaciones)
        ],
    }


def _dia(texto: str | None) -> datetime | None:
    return datetime.strptime(texto, "%Y-%m-%d").replace(tzinfo=timezone.utc) if texto else None


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="criterio · analiza tu historial de chats con IA, en tu equipo.")
    p.add_argument("--entrada", required=True, nargs="+", type=Path, help="conversations.json, MyActivity.json, el .zip de la exportación o su carpeta")
    p.add_argument("--salida", type=Path, default=Path("criterio-salida"), help="carpeta de resultados")
    p.add_argument("--desde", help="AAAA-MM-DD")
    p.add_argument("--hasta", help="AAAA-MM-DD")
    p.add_argument("--min-turnos", type=int, default=2, help="mínimo de mensajes tuyos por conversación (2)")
    p.add_argument("--buscar", help="solo conversaciones que contengan esta palabra")
    p.add_argument("--muestra", type=int, help="analizar solo N conversaciones al azar (útil para el reporte completo con un modelo)")
    p.add_argument("--semilla", type=int, default=2026, help="semilla del azar de --muestra, para repetir la misma muestra")
    p.add_argument("--sin-lotes", action="store_true", help="no escribir lotes para clasificar con un modelo")
    p.add_argument("--clasificacion", nargs="+", type=Path, help="JSON que devolvió el modelo al clasificar los lotes (reporte completo)")
    a = p.parse_args(argv)

    convs: list[Conversacion] = []
    for ruta in a.entrada:
        cargados = cargar(ruta)
        if not cargados:
            print(f"No reconocí el formato de {ruta}. Espero la exportación de ChatGPT, Claude o Gemini.", file=sys.stderr)
            return 1
        por_formato: dict[str, int] = {}
        for fmt, datos in cargados:
            leidas = LECTORES[fmt](datos)
            por_formato[fmt] = por_formato.get(fmt, 0) + len(leidas)
            convs.extend(leidas)
        for fmt, n in por_formato.items():
            aviso = " (experimental)" if fmt == "gemini" else ""
            print(f"{ruta.name}: {n} conversaciones de {fmt}{aviso}")

    hasta = _dia(a.hasta) + timedelta(days=1) if a.hasta else None
    convs = filtrar(convs, _dia(a.desde), hasta, a.min_turnos, a.buscar)
    print(f"Después de filtrar quedan {len(convs)} conversaciones.")
    if a.muestra and a.muestra < len(convs):
        convs = sorted(random.Random(a.semilla).sample(convs, a.muestra), key=lambda c: c.creada or datetime.min.replace(tzinfo=timezone.utc))
        print(f"Muestra al azar: {len(convs)} conversaciones (semilla {a.semilla}).")

    clasificacion = cargar_clasificacion(a.clasificacion) if a.clasificacion else None
    if clasificacion is not None:
        faltan = sum(1 for c in convs if c.id not in clasificacion)
        print(f"Clasificación del modelo: {len(clasificacion)} conversaciones." + (f" {faltan} sin clasificar quedan fuera." if faltan else ""))
    resultados = analizar(convs, clasificacion)
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "resultados.json").write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    escribir_html(a.salida / "reporte.html", resultados)
    if not a.sin_lotes and convs:
        carpeta = a.salida / "lotes"
        carpeta.mkdir(exist_ok=True)
        for i, lote in enumerate(armar_lotes(convs), 1):
            (carpeta / f"lote_{i:03}.md").write_text(lote, encoding="utf-8")

    print(f"Listo. Abre {a.salida / 'reporte.html'} en tu navegador.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
