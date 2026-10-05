# criterio

**Mide y entrena el criterio que pones cuando trabajas con IA.** Le pides algo a la IA, te responde bien escrito y lo aceptas sin revisar. `criterio` te muestra en qué momentos dudaste con método y en cuáles lo dejaste pasar.

> Versión 0.1. Nació para el taller de pensamiento crítico de REDUC@TE 2026 (ACIS): ver la [guía para asistentes](taller/guia-asistentes.md).

---

## Objetivo

La idea de fondo es la **duda metódica**: dudar a propósito y por un rato, para quedarte con lo que resiste el examen y luego decidir.

- **No dudar de nada** es aceptar lo que venga.
- **Dudar de todo** tampoco sirve: nunca terminas y gastas atención donde no importa.
- **Dudar con método** es escoger qué merece revisión, revisarlo y cerrar la duda con una razón.

`criterio` no premia llevarle la contraria a la IA ni mide cuánto la usas. Mide si, en tus conversaciones, pusiste criterio propio donde importaba.

## Cómo funciona

Un ciclo de cuatro pasos:

1. **Preparar** con el brief 4D. Antes de pedir algo, la IA te hace preguntas con las 4D (Delegación, Descripción, Discernimiento y Diligencia) y te entrega un brief y un checklist.
2. **Conversar.** Haces tu tarea en otro chat, con **tu** prompt y tu checklist.
3. **Medir** con el reporte. Al final pides tu reporte de criterio: 12 conductas, cada una con tu frase exacta.
4. **Practicar** con el coach. Te propone un ejercicio de 10 minutos para tu conducta más floja.

Y si quieres ver el panorama completo, el **analizador de historial** revisa tu historial exportado de ChatGPT, Claude o Gemini, en tu computador.

## Las 12 conductas

Cada conducta tiene tres estados: **ausente**, **presente** (aparece sin sustento) o **con evidencia** (aparece con una razón, fuente o dato que se puede revisar en el chat).

| # | id | Conducta | Dimensión |
|---|----|----------|-----------|
| 7 | `nota-contexto-faltante` | **Nota que a la IA le falta contexto** | **Discernimiento** · núcleo |
| 9 | `cuestiona-razonamiento` | **Cuestiona cuando el razonamiento no cuadra** | **Discernimiento** · núcleo |
| 11 | `verifica-datos` | **Pide fuente o verifica datos que importan** | **Discernimiento** · núcleo |
| 12 | `decide-distinto` | **Decide distinto a la IA, con argumento** | **Discernimiento** (propia) · núcleo |
| 1 | `itera` | Itera y afina | Descripción* |
| 2 | `aclara-objetivo` | Aclara el objetivo antes de pedir | Delegación* |
| 3 | `da-ejemplos` | Muestra cómo se ve lo bueno | Descripción* |
| 4 | `pide-formato` | Dice qué formato y estructura necesita | Descripción* |
| 5 | `fija-modo` | Define cómo quiere trabajar con la IA | Descripción* |
| 6 | `pide-tono` | Dice el tono y el estilo | Descripción* |
| 8 | `define-audiencia` | Dice para quién es el resultado | Descripción* |
| 10 | `consulta-enfoque` | Consulta el enfoque antes de ejecutar | Delegación* |

Las cuatro primeras son el **núcleo de criterio**: las que más tienen que ver con la duda metódica. El reporte las muestra primero. \* Asignación propia: el AI Fluency Index no publica ese mapeo.

**Regla de oro:** corregir a la IA sin razones no es criterio, puede ser capricho. Y aceptar su respuesta después de verificar sí puede serlo. Por eso el estado alto exige evidencia y el reporte siempre muestra tu frase.

Rúbrica completa, con ejemplos ilustrativos y casos límite: [`rubrica/conductas.md`](rubrica/conductas.md). Fuentes y porqué: [`rubrica/fundamentos.md`](rubrica/fundamentos.md).

## Empezar en 2 minutos

Sin instalar nada, en cualquier IA (ChatGPT, Claude, Gemini, Copilot u otra), también desde el celular:

1. Al final de una conversación, pega el texto completo de [`prompts/reporte.txt`](prompts/reporte.txt). Te devuelve tu reporte de criterio.
2. Para practicar, pega después [`prompts/coach.txt`](prompts/coach.txt).
3. Antes de tu próxima tarea, pega [`prompts/brief.txt`](prompts/brief.txt) en un chat nuevo y escribe tu tarea al final.

¿No tienes una conversación a mano? Pega [`taller/chat-demo.txt`](taller/chat-demo.txt) (es inventada) y compara con [el reporte esperado](taller/chat-demo-reporte-esperado.md).

## Usarlo con skills

Las skills son carpetas con un `SKILL.md` que la IA carga sola cuando hacen falta. Cada una trae su propia copia de la rúbrica en `references/`, así que funciona sola.

| Skill | Qué hace | Cuándo se activa |
|---|---|---|
| `brief-4d` | Te entrevista con las 4D y te entrega un brief y un checklist | Cuando pides preparar lo que le vas a pedir a la IA |
| `detector` | Reporte de criterio de la conversación actual | Solo cuando lo pides: «dame mi reporte de criterio» |
| `coach` | Un ejercicio de 10 minutos para tu conducta más floja | Cuando pides un ejercicio |
| `revision-de-historial` | Analiza tu historial exportado | Cuando pides revisar tu historial |

**Dónde funcionan:**
- **Claude** (claude.ai, app de escritorio y Claude Code).
- **Gemini** (app web y Gemini CLI).
- **ChatGPT:** las skills solo están en los planes Business, Enterprise y Edu. En los planes personales usa un Proyecto con instrucciones o pega los prompts.

Los `.zip` de las cuatro skills están en la página de [Releases](https://github.com/gutiedward/pensamiento-critico-ia/releases/latest). Se suben tal cual, sin descomprimir.

Paso a paso: [instalación](docs/instalacion.md) · [uso](docs/uso.md) · [pruebas](docs/pruebas.md).

## El analizador de historial

`skills/revision-de-historial/scripts/analizar.py` lee tu exportación de ChatGPT, Claude o Gemini (experimental) y arma un `reporte.html` con resumen, tablero de las 12 conductas, evolución mes a mes y una sección «Verifica tú mismo» con tus frases exactas.

- **Corre en tu computador.** Usa solo la biblioteca estándar de Python 3.9 o superior y **no importa ningún módulo de red**.
- **El reporte HTML no carga nada de internet**: ni fuentes, ni librerías, ni imágenes.

```bash
python3 skills/revision-de-historial/scripts/analizar.py --entrada ~/Downloads/conversations.zip
```

En Windows, usa `py` y barras invertidas:

```
py skills\revision-de-historial\scripts\analizar.py --entrada %USERPROFILE%\Downloads\conversations.zip
```

Hay dos niveles. El **pre-marcado** sale al correr el script: busca frases típicas, acierta cuando marca, pero se le escapa la mayoría. El **reporte completo** sale cuando una IA clasifica los lotes que deja el script y lo vuelves a correr con `--clasificacion`. Detalle y opciones en [docs/uso.md](docs/uso.md#analizador-de-historial-python-en-tu-computador).

## Diseño contra la descarga cognitiva

La **descarga cognitiva** es dejar que la IA piense por ti. `criterio` está hecho para no fomentarla:

- **Tú vas primero, la IA completa.** El brief te pide tu criterio («sirve si…») y qué harías tú antes de sugerir nada.
- **El prompt lo escribes tú.** La IA te dice máximo 3 cosas que le faltan, sin reescribirlo. Si le pides el prompt hecho, te lo da, pero te pide cambiar al menos una cosa.
- **El reporte señala la descarga.** Además de las 12 conductas, trae la línea «¿Hubo descarga cognitiva?» con una de cuatro señales: *sin señal*, *delegación razonable*, *descarga parcial* o *posible descarga*.

## Privacidad

- **Lo que pegas en un chat sale de tu equipo** y llega al proveedor de esa IA, con sus condiciones. No pegues datos personales ni de clientes (en Colombia los protege la Ley 1581). Usa marcadores como `[CLIENTE]`.
- **El analizador no envía nada.** Todo se queda en tu computador.
- **Ojo con el reporte completo:** si le pasas los lotes a una IA para que los clasifique, el texto de tus chats sí sale hacia ese proveedor. El script te lo recuerda.
- Tus marcas de «No estoy de acuerdo» en el reporte HTML se guardan solo en tu navegador.
- Tus exportaciones y resultados nunca deberían ir a un repositorio. El `.gitignore` ya los excluye.

## Qué no mide

- **Lo que pasa en tu cabeza.** Si dudaste y no lo escribiste, para `criterio` no existe.
- **Lo que verificas por fuera del chat.** Si revisaste el dato en otra pestaña y no lo contaste, sale como ausente.
- **Si tus decisiones fueron buenas.** Ve cómo conversaste, no cómo te fue después.
- **Si la IA tenía razón.** Para eso habría que saber la respuesta correcta de cada caso.
- **El contexto de cada tarea.** En un chat casual no hace falta verificar nada. Ausente no siempre es malo.

## Qué tan confiable es (v0.1)

Se probó con 25 conversaciones reales de una sola persona, el autor. Esas conversaciones no están en el repositorio.

| Qué se midió | Resultado |
|---|---|
| **Pre-marcado del script:** de las conductas del núcleo que sí estaban, ¿cuántas vio? | Entre 0 % y 12 % en tres de ellas; 73 % en *verifica datos*. Cuando marca algo, acierta entre el 80 % y el 100 % de las veces. |
| **Clasificación con Claude:** dos lecturas independientes con la rúbrica, ¿coinciden? | 85 % de coincidencia exacta; acuerdo sustancial (κ ≥ 0,6) en 11 de 12 conductas. Después de aclarar la rúbrica, 94 %. Esa segunda cifra es optimista, porque una lectura se revisó conociendo la otra. |
| **Comparación con una persona:** la misma persona etiquetó 5 conversaciones sin ver las etiquetas de Claude | A ciegas coincidió **50 %** con Claude, casi siempre porque marcaba más alto. Al revisar 6 desacuerdos con el texto completo y la razón de Claude, le dio la razón a Claude en los 6. |

Cómo leerlo:
- El pre-marcado sirve para encontrar ejemplos, no para medirte.
- La clasificación con Claude es **consistente**, pero que dos lecturas de Claude coincidan no prueba que acierten.
- Validado con los chats de **una** persona, en español y casi todos de trabajo.
- El soporte de **Gemini** en el analizador es experimental: no se probó con una exportación real. Con una versión anterior del prompt, Gemini calificó más alto de lo que la rúbrica permite; el prompt se ajustó, pero no se volvió a probar allí. Si lo usas, revisa bien las citas.
- Siempre habrá casos grises. Por eso el reporte muestra tu frase y la razón: la última palabra es tuya.

## Estructura del repositorio

```
rubrica/                 la rúbrica de 12 conductas (fuente única) y sus fundamentos
prompts/                 brief.txt, reporte.txt y coach.txt para pegar en cualquier IA
skills/
  brief-4d/              preparar una tarea con las 4D
  detector/              reporte de criterio de la conversación actual
  coach/                 ejercicios para la conducta más floja
  revision-de-historial/
    scripts/             analizar.py y la plantilla del reporte HTML
docs/                    manuales de instalación, uso y pruebas
taller/                  guía para asistentes y conversación de demostración (inventada)
AGENTS.md                instrucciones para agentes que no cargan skills
```

La rúbrica se edita en `rubrica/conductas.md`. Las copias en `skills/*/references/rubrica.md` deben quedar iguales.

## Créditos y licencias

- Código (`skills/revision-de-historial/scripts/`) bajo **MIT** ([`LICENSE`](LICENSE)). Contenido bajo **CC BY 4.0** ([`LICENSE-CONTENIDO.md`](LICENSE-CONTENIDO.md)).
- Las conductas y las preguntas del brief se inspiran en el **marco 4D de fluidez con IA** de **Rick Dakan, Joseph Feller y Anthropic** (CC BY-NC-SA 4.0): cuatro capacidades para trabajar con IA, que aquí se explican y se aplican con palabras propias. No se copió su texto.
- Las conductas observables y los porcentajes de referencia vienen del **AI Fluency Index de Anthropic (2026)**, citado como fuente. Detalle en [`rubrica/fundamentos.md`](rubrica/fundamentos.md).
- Este proyecto **no está afiliado ni respaldado por Anthropic**. Su nombre aparece solo para citar las fuentes.
- Autor: **Andrés Gutiérrez Aponte**.
