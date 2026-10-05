# Manual de pruebas

Lista de chequeo para confirmar que `criterio` funciona en cada IA antes de recomendarlo. Es para el autor y para quien quiera repetir las pruebas.

> **Nota sobre los enlaces.** Los enlaces usan `https://github.com/gutiedward/pensamiento-critico-ia`. Si el repositorio cambia de dirección, busca el mismo archivo en la nueva.
>
> **Privacidad.** Usa solo los textos inventados de este manual y de `taller/`. No pegues conversaciones reales en estas pruebas. Si pruebas el analizador con tu exportación real, déjala fuera del repositorio y no copies resultados aquí.

---

## Cómo usar este manual

1. Haz las pruebas en orden, una IA a la vez.
2. Usa **un chat nuevo** para cada prueba, salvo que diga otra cosa.
3. Marca la casilla solo si se cumple **todo** el resultado esperado.
4. Llena la anotación de cada prueba:
   - **Resultado:** pasó, falló o pasó a medias, y qué viste.
   - **Modelo y plan usado:** por ejemplo, «Claude Sonnet, plan Free» o «ChatGPT, plan Plus».
   - **Fecha.**
5. Al final, actualiza la [tabla de compatibilidad](#tabla-de-compatibilidad): cambia ⚠️ por ✅ o ❌ según lo que encontraste. Copia lo mismo en [instalacion.md](instalacion.md) y [uso.md](uso.md).

---

## Textos de prueba

Todos son inventados. Cópialos tal cual.

**T1 · Tarea para el brief**
```
Ayúdame a preparar lo que le voy a pedir a la IA: un correo para mi jefa pidiendo cambiar la fecha de entrega de un informe.
```
(Si usas el prompt `brief.txt`, pega el prompt y escribe al final solo: `Un correo para mi jefa pidiendo cambiar la fecha de entrega de un informe.`)

**T2 · Respuestas de la segunda ronda** (incluye el criterio y qué haría yo)
```
Es para el viernes. Mi jefa prefiere correos cortos. Sirve si en menos de 6 líneas explica la causa y propone una fecha nueva. Yo pediría una semana más y ofrecería un avance parcial el viernes.
```

**T3 · Mi prompt (a propósito incompleto)**
```
Escribe un correo para mi jefa pidiendo más tiempo para el informe.
```

**T4 · Pedir el prompt hecho**
```
Mejor dame tú el prompt listo.
```

**T5 · Chat normal (para la prueba de activación)**
```
Dame tres ideas para el asunto de un correo que invita a una reunión de equipo.
```

**T6 · Caso de prueba del reporte (pegar el prompt):** el archivo completo [`taller/chat-demo.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/taller/chat-demo.txt). Ya trae el pedido del reporte adentro.

**T7 · Caso de prueba del reporte (con la skill `detector`):** copia de `taller/chat-demo.txt` solo el bloque entre `=== INICIO DE LA CONVERSACIÓN ===` y `=== FIN DE LA CONVERSACIÓN ===`, ambos incluidos. Pégalo y escribe debajo:
```
Dame mi reporte de criterio de la conversación de arriba. Los mensajes de «Persona» son míos; los de «IA» son contexto.
```

### Resultado esperado del reporte (R-reporte)

Compara con [`taller/chat-demo-reporte-esperado.md`](../taller/chat-demo-reporte-esperado.md). Pasa si:
- [ ] Trae las **12 conductas**, primero las 4 del núcleo.
- [ ] **Nota contexto faltante:** con evidencia («Estoy en Manizales, no en Bogotá…»).
- [ ] **Cuestiona el razonamiento:** presente («¿Seguro? No sé.»). Falla si sale «con evidencia».
- [ ] **Verifica datos:** ausente. Falla si sale presente o con evidencia.
- [ ] **Decide distinto:** con evidencia («Prefiero el local del barrio…»).
- [ ] Las frases son **copia exacta** de los mensajes de Marta, sin «…» ni corchetes.
- [ ] **«¿Hubo descarga cognitiva?»: sin señal.** Falla si dice «posible descarga».
- [ ] «Para practicar» apunta a **verificar datos** (el 60 %).
- [ ] «Lo que este reporte no ve» no afirma que Marta verificó algo fuera del chat.

Puede variar sin que falle: *aclara el objetivo* presente en vez de con evidencia; *define la audiencia* con evidencia en vez de presente.

### Resultado esperado del brief (R-brief)

- [ ] La primera respuesta dice que **no va a hacer la tarea todavía**.
- [ ] La primera ronda trae **3 preguntas juntas** (para qué es, qué sabes tú del caso, qué no debes pegar).
- [ ] La segunda ronda pide **tu criterio de aceptación** («sirve si…») y **qué harías tú**, y no las salta.
- [ ] Máximo **2 rondas** de preguntas sobre la tarea.
- [ ] Entrega el **brief** con las 4D y un **checklist** de 3 a 5 casillas, en listas, **sin tablas**.
- [ ] **No entrega un prompt hecho.** Te pide que lo escribas tú.
- [ ] Al pegar T3, responde con **máximo 3 observaciones** y **no reescribe** el prompt.
- [ ] Al pegar T4, te da el prompt **y** te pide cambiar al menos una cosa antes de usarlo.
- [ ] No inventa cifras ni datos del caso: usa marcadores como `[FECHA]`.

### Resultado esperado del coach (R-coach)

Después del reporte de T6 o T7, en el mismo chat:
- [ ] Toma la conducta más floja del núcleo: **verificar datos**.
- [ ] Si no sabe en qué trabajas, lo pregunta **en una sola línea**.
- [ ] Propone **un solo** ejercicio de 10 minutos con tres partes: qué vas a practicar, el ejercicio, cómo sabes que funcionó.
- [ ] **No resuelve el ejercicio:** no busca ni verifica el 60 % por ti.
- [ ] Sin sermones sobre la IA.

---

## Claude

### 1. claude.ai (web), app de escritorio y celular

**Instalación**
1. Configuración › Capacidades: activa la ejecución de código.
2. Personalizar › Skills › + › Crear skill › Subir una skill: sube los 4 `.zip`.
- [ ] Los 4 `.zip` suben sin error.
- [ ] Las 4 skills aparecen con el interruptor encendido.
- [ ] Anota los nombres exactos del menú en español (para corregir [instalacion.md](instalacion.md)).

> Resultado:
> Modelo y plan usado:
> Fecha:

**brief-4d (web)**
1. Chat nuevo. Pega T1.
2. Responde la primera ronda con lo que quieras. En la segunda, pega T2.
3. Cuando te pida el prompt, pega T3.
4. Luego pega T4.
- [ ] Se activó la skill `brief-4d` (Claude lo muestra en la respuesta).
- [ ] Cumple todo R-brief.

> Resultado:
> Modelo y plan usado:
> Fecha:

**detector (web)**
1. Chat nuevo. Pega T7.
- [ ] Se activó la skill `detector`.
- [ ] Cumple todo R-reporte.

> Resultado:
> Modelo y plan usado:
> Fecha:

**Activación del detector (web)**
1. Chat nuevo. Pega T5.
2. Pide dos cambios cualquiera a las ideas («hazlas más cortas», «quita la segunda»).
3. Escribe: `Dame mi reporte de criterio`.
- [ ] En los pasos 1 y 2, el detector **no** se activa y no comenta tus mensajes.
- [ ] En el paso 3, **sí** se activa y entrega la tabla.
- [ ] Las 4 conductas del núcleo salen **ausentes**: en ese chat no hubo criterio que marcar. Anota qué señal de descarga dio.

> Resultado:
> Modelo y plan usado:
> Fecha:

**Activación del brief (web)**
1. Chat nuevo. Escribe: `Escribe un correo corto invitando al equipo a una reunión el jueves.`
- [ ] `brief-4d` **no** se activa: Claude hace la tarea directo.

> Resultado:
> Modelo y plan usado:
> Fecha:

**coach (web)**
1. En el chat del detector, escribe: `Dame un ejercicio para mejorar mi criterio`.
- [ ] Se activó la skill `coach`.
- [ ] Cumple todo R-coach.

> Resultado:
> Modelo y plan usado:
> Fecha:

**revision-de-historial (web)**
1. Chat nuevo. Sube un archivo de prueba de Claude: una exportación **inventada** con 2 conversaciones (los ejemplos sintéticos viven en el repositorio de desarrollo).
2. Escribe: `Revisa mi historial con este archivo`.
- [ ] Se activó la skill y corrió `analizar.py`.
- [ ] Dice que encontró **2 conversaciones**.
- [ ] Aclara que el resultado es un **pre-marcado** que ve poco.
- [ ] **Pide permiso** antes de clasificar los lotes.
- [ ] Ofrece el `reporte.html` para descargar o mostrar. ⚠️ Anota cómo lo entrega.

> Resultado:
> Modelo y plan usado:
> Fecha:

**App de escritorio**
1. Abre la app con la misma cuenta. Repite la prueba del detector (T7).
- [ ] Las skills aparecen sin volver a subirlas.
- [ ] Cumple R-reporte.

> Resultado:
> Modelo y plan usado:
> Fecha:

**Celular (prueba de uso desde el teléfono)**
1. Abre la app de Claude en el celular, con la misma cuenta.
2. Chat nuevo. Pega T1 y sigue el brief hasta el final, todo desde el teléfono.
3. Chat nuevo. Pega T7.
4. Si las skills no se activan, repite con los prompts: abre `brief.txt` y `chat-demo.txt` en el navegador del teléfono, **Seleccionar todo › Copiar** y pega.
- [ ] Las skills se activan en la app móvil (o anota que no).
- [ ] El brief se lee bien en la pantalla: listas, sin tablas.
- [ ] El reporte cumple R-reporte. Anota si la tabla se ve bien o hay que girar el teléfono.
- [ ] Copiar y pegar el prompt completo desde el teléfono funciona sin cortarse.

> Resultado:
> Modelo y plan usado (y teléfono):
> Fecha:

### 2. Claude Code

1. Copia las skills: `cp -R skills/brief-4d skills/detector skills/coach skills/revision-de-historial ~/.claude/skills/`
2. Abre Claude Code en una carpeta cualquiera y escribe `/skills`.
- [ ] Aparecen las 4 skills.

> Resultado:
> Modelo y plan usado:
> Fecha:

**brief-4d:** pega T1, luego T2, T3 y T4.
- [ ] Cumple R-brief.

> Resultado:
> Modelo y plan usado:
> Fecha:

**detector:** sesión nueva, pega T7.
- [ ] Cumple R-reporte.
- [ ] Activación: en otra sesión, pega T5. El detector **no** se activa. Luego `Dame mi reporte de criterio` **sí** lo activa.

> Resultado:
> Modelo y plan usado:
> Fecha:

**coach:** después del detector, `Dame un ejercicio para mejorar mi criterio`.
- [ ] Cumple R-coach.

> Resultado:
> Modelo y plan usado:
> Fecha:

**revision-de-historial:** en la carpeta del repositorio, escribe `/revision-de-historial` y da la ruta de una exportación de prueba de ChatGPT, guardada **fuera** del repositorio.
- [ ] Corre `analizar.py` en tu equipo y crea `criterio-salida/reporte.html`.
- [ ] Explica que es un pre-marcado.
- [ ] **Pide permiso** antes de leer los lotes.
- [ ] Con permiso, crea `clasificacion_001.json` y regenera el reporte con `--clasificacion`.
- [ ] Al terminar, borra `criterio-salida/` del repositorio (no se sube).

> Resultado:
> Modelo y plan usado:
> Fecha:

### 3. API de Claude

No aplica para el taller: `criterio` no trae código para la API. Si alguien la necesita, probar subir una skill con `POST /v1/skills` ([guía](https://platform.claude.com/docs/en/build-with-claude/skills-guide)).
- [ ] No aplica en v0.1 (deja la casilla sin marcar o anota «no se probó»).

---

## ChatGPT

### Prompts para pegar (cualquier plan)

**brief:** chat nuevo, pega [`brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt) con la tarea de T1 al final. Sigue con T2, T3 y T4.
- [ ] Cumple R-brief.

> Resultado:
> Modelo y plan usado:
> Fecha:

**reporte:** chat nuevo, pega T6.
- [ ] Cumple R-reporte.

> Resultado:
> Modelo y plan usado:
> Fecha:

**coach:** en el mismo chat, pega [`coach.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/coach.txt).
- [ ] Cumple R-coach.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Proyecto con instrucciones (plan gratuito)

1. Crea el proyecto «criterio · reporte» como dice [instalacion.md](instalacion.md#chatgpt).
2. Dentro del proyecto, chat nuevo: pega T5. Luego escribe `Dame mi reporte de criterio`.
3. Dentro del proyecto, chat nuevo: pega el bloque de T7.
- [ ] El proyecto se puede crear en el plan gratuito.
- [ ] Con T5 **no** sale el reporte; con «Dame mi reporte de criterio» **sí**.
- [ ] Con T7 cumple R-reporte.
- [ ] El proyecto «criterio · brief» arranca la entrevista en cada chat nuevo y cumple R-brief.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Skills (solo Business, Enterprise o Edu)

Si tienes acceso a una cuenta así:
1. Plugins › Skills › Create › Upload from your computer: sube los 4 `.zip`.
2. Repite las pruebas de brief (T1–T4), detector (T7 y activación con T5) y coach.
- [ ] Acepta los `.zip`.
- [ ] Cumple R-brief, R-reporte y R-coach.
- [ ] El detector no se activa con T5.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Celular

1. En la app de ChatGPT del teléfono, chat nuevo, pega T6 (copiado desde el navegador del teléfono).
- [ ] Cumple R-reporte y se lee bien en la pantalla.

> Resultado:
> Modelo y plan usado (y teléfono):
> Fecha:

---

## Gemini

### Skills en la app de Gemini

1. En gemini.google.com (computador): Configuración › Skills › Upload. Sube `brief-4d.zip`. Si no lo acepta, sube la carpeta `brief-4d`.
2. Repite con los otros tres.
- [ ] Aparece la opción Skills en tu cuenta. Anota si tu cuenta es gratuita o de pago.
- [ ] Acepta nuestros `.zip`. Si no, anota si aceptó la carpeta.
- [ ] Las skills incluyen los archivos de `references/`.

> Resultado:
> Modelo y plan usado:
> Fecha:

**brief-4d:** chat nuevo, pega T1, luego T2, T3 y T4.
- [ ] La skill se activa sola (o con `/brief-4d`). Anota cuál.
- [ ] Cumple R-brief.

> Resultado:
> Modelo y plan usado:
> Fecha:

**detector:** chat nuevo, pega T5. Luego, otro chat nuevo con T7.
- [ ] Con T5 **no** se activa.
- [ ] Con T7 se activa y cumple R-reporte.
- [ ] No infla: revisa que no salga casi todo «con evidencia».

> Resultado:
> Modelo y plan usado:
> Fecha:

**coach:** después del detector, `Dame un ejercicio para mejorar mi criterio`.
- [ ] Cumple R-coach.

> Resultado:
> Modelo y plan usado:
> Fecha:

**revision-de-historial:** chat nuevo, sube una exportación de prueba de Gemini (inventada) y escribe `Revisa mi historial con este archivo`.
- [ ] Corre el script (o anota que no puede).
- [ ] Pide permiso antes de clasificar.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Prompts para pegar

**reporte:** chat nuevo, pega T6.
- [ ] Cumple R-reporte. Ojo especial: que no afirme que Marta verificó cosas fuera del chat.

**brief:** pega `brief.txt` con la tarea de T1, sigue con T2, T3 y T4.
- [ ] Cumple R-brief.

**coach:** después del reporte, pega `coach.txt`.
- [ ] Cumple R-coach.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Gem con instrucciones

1. Crea la Gem «criterio · reporte» como dice [instalacion.md](instalacion.md#gemini).
2. Pega T5 y luego `Dame mi reporte de criterio`.
- [ ] Con T5 no sale el reporte; con la frase sí.
- [ ] La Gem aparece en la app del celular.

> Resultado:
> Modelo y plan usado:
> Fecha:

### Celular

1. En la app de Gemini del teléfono, chat nuevo. Escribe `/` y elige `detector` (o pega T6 si no hay skills).
2. Pega T7.
- [ ] Las skills subidas desde el computador aparecen en el teléfono.
- [ ] Cumple R-reporte.

> Resultado:
> Modelo y plan usado (y teléfono):
> Fecha:

---

## Cualquier otra IA (solo prompts)

Prueba al menos una, por ejemplo Copilot, Meta AI o DeepSeek.

1. Chat nuevo: pega T6.
2. Chat nuevo: pega `brief.txt` con la tarea de T1, sigue con T2, T3 y T4.
3. Después del reporte, pega `coach.txt`.
- [ ] Reporte: cumple R-reporte.
- [ ] Brief: cumple R-brief.
- [ ] Coach: cumple R-coach.

> Resultado:
> IA, modelo y plan usado:
> Fecha:

---

## Analizador de historial (Python)

**Funciona con exportaciones de prueba**
1. En la carpeta del repositorio, corre el script con una o varias exportaciones de prueba (inventadas o tuyas, siempre **fuera** del repositorio):
   ```bash
   python3 skills/revision-de-historial/scripts/analizar.py --entrada <archivo1> <archivo2> --salida /tmp/criterio-prueba
   ```
2. Abre `/tmp/criterio-prueba/reporte.html` en el navegador.
- [ ] Termina sin errores y dice cuántas conversaciones leyó de cada archivo.
- [ ] El reporte tiene resumen, tablero de 12 conductas, evolución por mes y «Verifica tú mismo».
- [ ] El botón «No estoy de acuerdo» funciona y la marca sigue ahí al recargar.

> Resultado:
> Sistema y versión de Python:
> Fecha:

**Funciona con una exportación real** (la tuya, fuera del repositorio)
1. Corre el script con tu `.zip` de ChatGPT, de Claude y, si puedes, de Gemini. Usa `--salida` hacia una carpeta fuera del repositorio.
- [ ] ChatGPT: lee el `.zip` sin descomprimir.
- [ ] Claude: lee el `.zip` sin descomprimir.
- [ ] Gemini (experimental): lee `MyActivity.json`. Anota qué falló, sin copiar contenido.
- [ ] `--muestra 20`, `--desde` y `--buscar` filtran como se espera.

> Resultado:
> Sistema y versión de Python:
> Fecha:

**Windows**
1. Corre el comando con `py` y barras invertidas, como dice [uso.md](uso.md#analizador-de-historial-python-en-tu-computador).
- [ ] Funciona igual que en Mac.

> Resultado:
> Fecha:

### Privacidad: el reporte HTML hace 0 peticiones de red

> Las pruebas automáticas (que el script no importe módulos de red y que el HTML no cargue enlaces externos) viven en el repositorio de desarrollo. Aquí va la revisión manual.

1. Revisa que el script no importe módulos de red:
   ```bash
   grep -nE "^(import|from) (socket|urllib|http|requests)" skills/revision-de-historial/scripts/analizar.py
   ```
2. Busca direcciones de internet en el reporte:
   ```bash
   grep -cE "https?://" /tmp/criterio-prueba/reporte.html
   ```
3. Abre `/tmp/criterio-prueba/reporte.html` en Chrome. Abre las herramientas de desarrollo (`Cmd+Opción+I` en Mac, `F12` en Windows), pestaña **Red** (*Network*). Marca **Desactivar caché** y recarga la página.
4. Apaga el wifi y vuelve a recargar.
- [ ] El primer `grep` no devuelve nada.
- [ ] El `grep` devuelve **0**.
- [ ] En la pestaña Red solo aparece el propio `reporte.html`: **0 peticiones** a otros sitios.
- [ ] Sin wifi, el reporte se ve completo: estilos, gráfica y botones.

> Resultado:
> Navegador y versión:
> Fecha:

**Limpieza**
- [ ] Borra `/tmp/criterio-prueba` y cualquier `criterio-salida/` que haya quedado.
- [ ] `git status` no muestra exportaciones, resultados ni conversaciones.

---

## Tabla de compatibilidad

Estado al 5 de octubre de 2026, antes de las pruebas.

- ✅ verificado en la documentación oficial. Para los prompts y el analizador: ya probado en el repositorio de desarrollo.
- ⚠️ por probar.
- ❌ no se puede.

| LLM | Skills `brief-4d`, `detector`, `coach` | Skill `revision-de-historial` | Prompts para pegar | Proyecto o Gem con instrucciones | Analizador local |
|---|---|---|---|---|---|
| **claude.ai web** (Free y pagos) | ✅ subir `.zip` con ejecución de código · ⚠️ nuestras skills | ⚠️ | ✅ | No hace falta | ✅ en el computador |
| **Claude app de escritorio** | ⚠️ | ⚠️ | ✅ | No hace falta | ✅ en el computador |
| **Claude celular** | ⚠️ | ⚠️ | ⚠️ | No hace falta | ❌ |
| **Claude Code** | ✅ `~/.claude/skills/` y `.claude/skills/` | ✅ corre en tu equipo | ✅ | No aplica | ✅ |
| **API de Claude** | ✅ `POST /v1/skills` · no aplica al taller | ⚠️ | ⚠️ | No aplica | ✅ |
| **ChatGPT Free, Plus, Pro** | ❌ | ❌ | ✅ | ✅ Proyecto · ❌ crear GPT | ✅ en el computador |
| **ChatGPT Business, Enterprise, Edu** | ✅ en la documentación · ⚠️ nuestros `.zip` | ⚠️ | ✅ | ⚠️ | ✅ en el computador |
| **ChatGPT celular** | ❌ en planes personales | ❌ | ⚠️ | ⚠️ | ❌ |
| **Gemini web y Mac** (cuenta personal, 18+) | ✅ en la documentación · ⚠️ plan gratuito y nuestros `.zip` | ⚠️ | ⚠️ | ✅ Gem hasta nov. 2026 | ✅ en el computador |
| **Gemini celular** | ✅ se usan, no se suben · ⚠️ | ⚠️ | ⚠️ | ✅ Gem creada en la web | ❌ |
| **Gemini CLI** | ✅ `~/.gemini/skills/` · ⚠️ | ⚠️ | ⚠️ | No aplica | ✅ |
| **Codex** | ✅ `~/.agents/skills/` · ⚠️ | ⚠️ | ⚠️ | No aplica | ✅ |
| **Cualquier otra IA** | ❌ | ❌ | ⚠️ | ⚠️ según la IA | ✅ en el computador |

### Fuentes oficiales consultadas

- Claude, skills: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Code, skills: https://code.claude.com/docs/en/skills
- API de Claude, skills: https://platform.claude.com/docs/en/build-with-claude/skills-guide
- Claude, exportar datos: https://support.claude.com/en/articles/9450526-export-your-claude-data
- ChatGPT, skills: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- ChatGPT, GPT personalizados: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- ChatGPT, proyectos: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- ChatGPT, exportar datos: https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data
- Codex, skills: https://learn.chatgpt.com/docs/build-skills
- Gemini, skills: https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop
- Gemini, de Gems a skills: https://support.google.com/gemini/answer/18560919?hl=en
- Gemini, Gems: https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop
- Gemini CLI, skills: https://geminicli.com/docs/cli/skills/

*Contenido bajo CC BY 4.0.*
