# Fundamentos · de dónde sale esta rúbrica

Este documento explica en qué nos apoyamos y hasta dónde llega cada fuente. No hace falta leerlo para usar `criterio`, pero sirve si alguien pregunta "¿y eso por qué?".

---

## 1. La idea: dudar a propósito y por un rato

En el *Discurso del método* (1637) y en las *Meditaciones metafísicas* (1641), René Descartes propone la **duda metódica**: poner en duda lo que uno cree saber para quedarse solo con lo que resiste el examen.

Hay dos detalles que casi siempre se olvidan y que son el corazón de este proyecto:

- **La duda es una herramienta, no una forma de vida.** Descartes duda para llegar a algo firme, no para instalarse en la sospecha.
- **Mientras duda, sigue actuando.** En la tercera parte del *Discurso* se da una "moral provisional": como el viajero perdido en un bosque, conviene escoger una dirección y mantenerla con firmeza en vez de dar vueltas. Dudar no lo paraliza.

Llevado a una conversación con IA, eso significa:

- **No dudar de nada** es aceptar lo que venga. El problema es obvio.
- **Dudar de todo** tampoco sirve: nunca terminas, desconfías de lo que ya está bien y gastas tu atención donde no importa.
- **Dudar con método** es escoger qué merece revisión (la cifra de la que depende la decisión, el supuesto que no aplica a tu caso), revisarlo y **decidir**.

Por eso la rúbrica no premia llevarle la contraria a la IA. Premia dudar donde importa y cerrar la duda con una razón.

## 2. Qué conductas mirar: el marco 4D y el AI Fluency Index

**El marco.** Rick Dakan y Joseph Feller desarrollaron, junto con Anthropic, el **marco 4D de fluidez con IA**. Tiene cuatro competencias: Delegación (qué hacer con la IA y qué no), Descripción (comunicar bien lo que se necesita), Discernimiento (evaluar lo que la IA produce) y Diligencia (hacerse responsable del uso). El marco describe 24 conductas.

**El índice.** En febrero de 2026, Anthropic publicó el **AI Fluency Index**. De las 24 conductas del marco, 11 se pueden observar directamente dentro de una conversación, y esas midieron.

- **Muestra:** 9.830 conversaciones con varios intercambios en claude.ai, entre el 20 y el 26 de enero de 2026.
- **Método:** 11 clasificadores automáticos, uno por conducta, hechos con Claude.
- **Hallazgo clave para nosotros:** las conductas de Discernimiento son de las menos frecuentes. Notar contexto faltante aparece en el 20,3 % de las conversaciones, cuestionar el razonamiento en el 15,8 % y verificar datos en el 8,7 %.
- **Además:** cuando la persona está creando algo (código, documentos, herramientas), las tres **bajan**, aunque se den más instrucciones al principio. Justo cuando el producto se ve terminado, menos se revisa.

**Cómo lo usamos:**
- Tomamos esas 11 conductas como base y las **redactamos con nuestras palabras**.
- Agregamos una propia: **decidir distinto con argumento**.
- Usamos los porcentajes del Index solo como **referencia**, no como meta. Tus conversaciones no son una muestra comparable: son de otra persona, de otras herramientas, de otras tareas.

**Lo que el Index no publica:**
- A qué competencia pertenece cada conducta. Solo confirma que las tres de arriba son de Discernimiento.
- La repartición de las demás en `conductas.md` es nuestra.

**Licencias:**
- El marco 4D está publicado bajo **CC BY-NC-SA 4.0** (© 2025 Rick Dakan, Joseph Feller y Anthropic). Por eso no copiamos su texto: si lo hiciéramos, esta rúbrica heredaría esa licencia y no podría ser CC BY.
- La página del Index es © 2026 Anthropic. De ella citamos cifras con su fuente.

### Del marco al brief: las 4D antes de pedir

La rúbrica mira la conversación **después**. La skill `brief-4d` (y `prompts/brief.txt`) usa las 4D **antes**, como preguntas para preparar la tarea:

- **Delegación:** ¿para qué es, qué le toca a la IA, qué me toca a mí y conviene usarla?
- **Descripción:** el producto que quiero, el proceso que debe seguir y cómo quiero que trabaje conmigo.
- **Discernimiento:** con qué criterios voy a aceptar la respuesta y cuál es el dato que verifico.
- **Diligencia:** qué datos no comparto, a quién le cuento que usé IA y quién firma.

Las preguntas están escritas con nuestras palabras, sin copiar el material del curso.

## 3. Por qué importa: más confianza en la IA, menos pensamiento crítico

Lee y colegas (Microsoft Research y Carnegie Mellon, **CHI 2025**) encuestaron a **319 trabajadores del conocimiento** que contaron **936 ejemplos** reales de uso de IA generativa en su trabajo.

**Lo que encontraron:**
- **Más confianza en la IA** se asocia con **menos pensamiento crítico** aplicado a la tarea.
- **Más confianza en uno mismo** para esa tarea se asocia con **más pensamiento crítico**.

**Por qué nos importa:**
- El riesgo no es usar IA. El riesgo es que, a medida que la IA "sale bien", dejamos de mirar.
- `criterio` quiere hacer visible ese momento.

**Límite de la fuente:**
- Es una encuesta: mide lo que la gente **dice** que hace, no lo que hace.
- Muestra asociación, no causa.
- Nosotros vamos al otro extremo: miramos lo que la gente **hace** en el chat, pero no vemos lo que piensa (ver sección 5).

## 4. Por qué no contamos desacuerdos: confianza apropiada

La literatura sobre automatización lleva décadas diciendo algo incómodo: **la meta no es confiar menos, es confiar bien**.

- **Parasuraman y Riley (1997)** distinguen dos errores:
  - **mal uso**: confiar de más, dejar pasar errores del sistema
  - **desuso**: confiar de menos, ignorar un sistema que tenía razón

  Los dos son fallas.
- **Lee y See (2004)** proponen la idea de **confianza calibrada**: que la confianza vaya de la mano con lo que el sistema realmente sabe hacer.
- **Schemmer y colegas (IUI 2023)** lo llevan a la IA. Una persona confía de manera apropiada cuando **rechaza el consejo equivocado** y **acepta el correcto**. Contar cuántas veces aceptó o rechazó no dice nada si no sabemos si el consejo era bueno.

**Consecuencia para la rúbrica:**
- Un "no estoy de acuerdo" sin razón no es criterio; puede ser capricho.
- Un "listo, así queda" después de verificar sí puede serlo.
- Por eso cada conducta tiene tres estados. El estado alto, **presente con evidencia**, exige algo revisable en el chat: un argumento, una fuente, un dato.
- Y por eso el informe siempre muestra la cita, no solo el número.

**Lo que no podemos hacer:** saber si la IA tenía razón en cada caso. Eso requeriría conocer la respuesta correcta, y no la tenemos. Nos quedamos con lo siguiente mejor: ver si la persona **dio razones**.

## 5. Límites honestos

- **Solo vemos el chat.** Lo que pensaste y no escribiste, o lo que verificaste en otra pestaña, no aparece.
- **Vemos el proceso, no el resultado.** Una conversación llena de "con evidencia" puede terminar en una mala decisión, y al revés.
- **No todo chat necesita criterio.** Pedir una receta o jugar con ideas no exige verificar fuentes. Ausente no siempre es malo.
- **El detector también se equivoca.** El pre-marcado automático del analizador es una pista. Por eso el informe te muestra las citas para que tú decidas si acertó.
- **Es la versión 0.1.** La rúbrica se va a ajustar con el uso.

---

## Referencias

- Descartes, R. (1637). *Discurso del método*. (1641). *Meditaciones metafísicas*. Dominio público.
- Dakan, R., Feller, J. y Anthropic (2025). *AI Fluency Framework*. CC BY-NC-SA 4.0. https://aifluencyframework.org/ · Cursos de Anthropic Academy: *AI Fluency: Framework & Foundations* y *Teaching AI Fluency*.
- Anthropic (2026, febrero). *The AI Fluency Index*. https://academy.claude.com/tutorials/the-ai-fluency-index
- Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R. y Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. *CHI '25*. https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
- Parasuraman, R. y Riley, V. (1997). Humans and Automation: Use, Misuse, Disuse, Abuse. *Human Factors*, 39(2), 230–253.
- Lee, J. D. y See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50–80.
- Schemmer, M., Kühl, N., Benz, C., Bartos, A. y Satzger, G. (2023). Appropriate Reliance on AI Advice: Conceptualization and the Effect of Explanations. *IUI '23*. https://doi.org/10.1145/3581641.3584066

---

*Contenido bajo CC BY 4.0.*
