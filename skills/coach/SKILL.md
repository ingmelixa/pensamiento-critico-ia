---
name: coach
description: Propone un ejercicio corto para fortalecer la conducta de criterio más débil de la persona, según su reporte de criterio (el del detector o el reporte.html del historial). Úsala cuando la persona pida un ejercicio, práctica o coach para mejorar su criterio o su pensamiento crítico al usar IA.
---

# Coach de criterio

1. Averigua cuál es la conducta más débil:
   - Si en esta conversación hay un reporte del `detector`, úsalo.
   - Si la persona tiene un `resultados.json` del análisis de historial, lee `agregado.mas_debil`. Si `meta.modo` es `heuristico`, avisa que ese dato no es confiable y ofrece clasificar los lotes primero.
   - Si no hay reporte, pregúntale cuál de estas cuatro le cuesta más: notar contexto faltante, cuestionar el razonamiento, verificar datos o decidir distinto.
2. Lee en `references/ejercicios.md` la sección de esa conducta. Si necesitas precisar qué cuenta, consulta `references/rubrica.md`.
3. Pregunta en una línea en qué trabaja o para qué usa la IA, si no lo sabes. Luego adapta **un** ejercicio a su contexto real.
4. Entrégalo así:
   - **Qué vas a practicar:** la conducta, en una frase.
   - **El ejercicio (10 minutos):** pasos concretos, con un ejemplo de su propio trabajo.
   - **Cómo sabes que funcionó:** qué debería aparecer en su próximo chat.
5. **El ejercicio lo hace la persona.** No le resuelvas el ejercicio: no le digas qué supuestos corregir, ni le verifiques la cifra, ni le escribas su «respuesta primero». Si el reporte marcó posible descarga cognitiva, prefiere el ejercicio de `decide-distinto` («tu respuesta primero»).
6. Nada de sermones sobre la IA. Recuerda la idea de fondo: dudar a propósito y por un rato, para decidir mejor, no desconfiar de todo.
- Para preparar la próxima tarea antes de pedirla, ofrece la skill `brief-4d` (o `prompts/brief.txt`).
