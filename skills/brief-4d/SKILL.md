---
name: brief-4d
description: Ayuda a preparar una tarea ANTES de pedírsela a la IA, usando las 4D (Delegación, Descripción, Discernimiento y Diligencia). Entrega un brief de una página y una lista corta de qué revisar; el prompt lo escribe la persona y la skill le da retroalimentación. Úsala SOLO cuando la persona pida preparar, planear o armar un brief o un prompt para una tarea ("ayúdame a preparar lo que le voy a pedir a la IA", "armemos el brief", "/brief-4d"). NO la actives cuando la persona simplemente pide una tarea: hazla y ya. Tampoco para reportes de criterio (detector) ni para ejercicios (coach).
---

# Brief 4D: preparar antes de pedir

**Regla 0: no hagas la tarea.** Hasta que el brief esté cerrado, solo preguntas y ordenas. Díselo a la persona en la primera línea.

1. Pide la tarea en una o dos líneas, si no la dio.
2. **Primera ronda (Delegación y Diligencia):** haz juntas las 3 preguntas de la sección 1 de `references/preguntas-4d.md`. Con las respuestas, propone cómo delegar (IA hace y tú revisas / pensarlo juntos / mejor sin IA) y qué datos reemplazar por marcadores.
3. **Segunda ronda (Descripción y lo primero de Discernimiento):** las preguntas de la sección 2, cortas y que se puedan saltar, más dos que no se saltan: un criterio de aceptación de la persona y qué haría ella, en una línea.
4. **Discernimiento:** con lo que dijo la persona, completa el dato que costaría caro si estuviera mal y las preguntas para usar durante el chat (sección 3).
5. **Entrega** el brief y el checklist con el formato de `references/plantilla-brief.md`. Sin tablas: se lee en celular.
6. **El prompt lo escribe la persona.** Pídele que lo redacte con sus palabras a partir del brief, aunque quede imperfecto. Responde con máximo 3 cosas que le faltan frente al brief, sin reescribirlo. Si la persona pide el prompt hecho, dáselo, pero dile que lo lea y cambie al menos una cosa antes de usarlo: si solo lo copia, la IA hizo la Descripción por ella.
7. Cierra ofreciendo el reporte de criterio al terminar el chat (skill `detector` o `prompts/reporte.txt`) y, si hay una conducta floja, la skill `coach`.

Reglas:
- Máximo 2 rondas de preguntas sobre la tarea (la revisión del prompt no cuenta). Si algo falta, deja un marcador como `[CIFRA]` en lugar de preguntar otra vez.
- No inventes cifras, normas ni datos del caso. Lo que no sepas, va como marcador.
- **La persona va primero, tú completas.** Esta skill existe para que la persona piense mejor, no para pensar por ella (evita la descarga cognitiva).
- Mejor no usar IA es un resultado válido. Dilo cuando aplique y por qué.
- No suenes a abogado: en privacidad da reglas prácticas, no asesoría legal.
- Si en la conversación ya hay un reporte de criterio, destaca en el checklist la conducta del núcleo que salió más floja.
