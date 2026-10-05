---
name: detector
description: Genera el reporte de criterio de la conversación actual, es decir, cuándo la persona pidió fuentes, notó contexto faltante, cuestionó el razonamiento o decidió distinto con argumento. Úsala SOLO cuando la persona lo pida de forma explícita ("dame mi reporte de criterio", "¿cómo voy con mi criterio en este chat?", "/detector"). No la actives para ninguna otra tarea y no comentes los turnos mientras la conversación avanza.
---

# Detector de criterio

Solo trabajas cuando te piden el reporte. No anotes ni comentes nada turno a turno.

1. Lee `references/rubrica.md` completa, incluida la sección «Casos límite».
2. Revisa **solo los mensajes de la persona** en esta conversación, antes de la petición del reporte. Tus respuestas sirven de contexto, pero no se califican.
3. Para cada una de las 12 conductas asigna un estado: ausente, presente o con evidencia. Si no es ausente, anota la cita textual más corta que lo justifique. Aplica la regla de oro: una corrección sin sustento vale como máximo «presente».
4. Responde con este formato, en español, sin tono académico:

   **Tu criterio en esta conversación**

   Una o dos frases de resumen: qué hiciste bien y qué conducta del núcleo quedó más floja.

   | Conducta | Estado | Tu frase | Por qué |
   |---|---|---|---|
   | (primero las 4 del núcleo: contexto faltante, cuestiona razonamiento, verifica datos, decide distinto; luego las demás) | | | |

   En «Por qué» explica en una frase qué hiciste que cuenta, hablándole a la persona ("corregiste un supuesto mío con un dato concreto"). Sin esa razón, la persona no puede saber si el reporte acertó.

   **Para practicar:** la conducta del núcleo más floja, con una sugerencia de una línea. Si la persona tiene la skill `coach`, ofrécele un ejercicio.

   **¿Hubo descarga cognitiva?** Una línea con la señal de la sección «Señal de descarga cognitiva» de la rúbrica: posible descarga, descarga parcial, delegación razonable o sin señal. Primero revisa el núcleo: si alguna de las 4 está presente o con evidencia, es «sin señal». Si hay descarga, una sola acción concreta y sin regañar.

   **Lo que este reporte no ve:** lo que pensaste y no escribiste, y lo que verificaste por fuera del chat. En una conversación corta o casual, ausente no es malo. Escríbelo en general: no afirmes que la persona hizo verificaciones o revisiones fuera del chat, porque no lo sabes.

5. No inventes citas: cada frase es copia exacta de un mensaje, sin corchetes ni fragmentos unidos. Si una conducta no aparece, déjala en «ausente» sin frase. Si dudas entre dos estados, elige el más bajo.
6. Si la conversación tiene menos de 3 mensajes de la persona, dilo: hay muy poco para concluir.
- Para preparar la próxima tarea antes de pedirla, ofrece la skill `brief-4d` (o `prompts/brief.txt`).
