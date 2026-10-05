# AGENTS.md · criterio

Instrucciones para agentes de IA (Codex, Cursor, Gemini CLI y otros) que **no** cargan Agent Skills. Si tu herramienta sí las soporta, usa las carpetas de `skills/`.

## Qué es este repositorio

`criterio` le muestra a una persona cuándo puso criterio propio en sus conversaciones con IA. La base es la rúbrica de 12 conductas con tres estados (ausente, presente, con evidencia) que está en `rubrica/conductas.md`.

## Cuando la persona te pida su reporte de criterio

1. Lee `rubrica/conductas.md` completa, incluida la sección «Casos límite».
2. Mira solo los mensajes de la persona. Tus respuestas son contexto, no se califican.
3. Sigue el formato de salida de `prompts/reporte.txt`: resumen, tabla con estado y cita textual, «Para practicar» y «Lo que este reporte no ve».
4. No inventes citas. Una corrección sin razones vale como máximo «presente».

## Cuando quiera preparar una tarea antes de pedirla

Sigue `prompts/brief.txt` (o `skills/brief-4d/`): no hagas la tarea todavía; hazle las preguntas de las 4D en máximo 2 rondas y entrégale el brief y un checklist de revisión. El prompt lo escribe la persona: tú solo le dices qué le falta, sin reescribirlo.

## Cuando te pida un ejercicio

Usa `skills/coach/references/ejercicios.md`. Propón **un** ejercicio de 10 minutos, adaptado a su trabajo, para la conducta más floja del núcleo de criterio.

## Cuando te pida revisar su historial exportado

1. Corre `python3 skills/revision-de-historial/scripts/analizar.py --entrada <exportación> --salida criterio-salida`.
2. Explica que ese primer reporte es un pre-marcado que ve poco.
3. Para el reporte completo, **pide permiso** antes de leer sus conversaciones, porque pasan por tu proveedor. Clasifica los archivos de `criterio-salida/lotes/` según las instrucciones que traen y vuelve a correr el script con `--clasificacion`.

## Reglas

- Nunca copies conversaciones de la persona a archivos del repositorio.
- No tomes posiciones sobre si la IA es buena o mala. El objetivo es dudar a propósito y por un rato, no desconfiar de todo.
