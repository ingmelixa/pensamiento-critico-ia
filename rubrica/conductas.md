# Rúbrica de criterio · v0.1

Esta rúbrica dice qué buscamos en una conversación con IA para saber si la persona puso criterio propio. Es la base del detector, del analizador de historial y del coach.

**Una idea guía todo el documento:** dudar sirve cuando se hace a propósito y por un rato. No se trata de desconfiar de todo; dudar de todo es tan inútil como no dudar de nada. Por eso aquí no premiamos llevarle la contraria a la IA, sino hacerlo con razones.

---

## Cómo leer cada conducta

Cada conducta tiene:

- **Qué es**: la conducta dicha en palabras simples.
- **Cuenta / no cuenta**: dónde está la línea y qué confusiones son típicas.
- **Tres estados**:
  - **Ausente**: no aparece en la conversación.
  - **Presente**: aparece, pero sin sustento.
  - **Presente con evidencia**: aparece y además trae una razón, una fuente, un dato o un criterio que se puede revisar dentro del chat.
- **Señales**: frases o movimientos que suelen delatarla. Son pistas, no pruebas.
- **Referencia**: el porcentaje de conversaciones en las que apareció en el AI Fluency Index (Anthropic, feb 2026). Es un punto de comparación, no una meta.
- **Ejemplos ilustrativos**: situaciones inventadas para mostrar la diferencia entre estados. No vienen de chats reales de nadie. Muchos no hacen sentido fuera de contexto: fíjate en lo que dice la persona, no en el tema.

## Regla de oro: corregir no es lo mismo que tener criterio

Contar cuántas veces alguien corrige a la IA o cambia de decisión no dice si confió bien o mal. Una persona puede corregir por capricho y otra puede aceptar todo porque ya verificó. Entonces:

- Una corrección, un desacuerdo o un "no me convence" **sin sustento** vale como máximo **presente**.
- Para llegar a **presente con evidencia** tiene que haber algo revisable: un argumento, una fuente, un dato, una prueba que la persona hizo o un criterio explícito.
- Ninguna cifra de este informe se lee sola. Siempre va con la cita del chat que la produjo.

## Sobre las dimensiones

Las conductas vienen del marco 4D de Rick Dakan y Joseph Feller (Delegación, Descripción, Discernimiento y Diligencia), en la versión observable que usó el AI Fluency Index. Las redactamos con nuestras palabras; no copiamos texto del marco (ver `fundamentos.md`).

El Index confirma que **tres** conductas son de Discernimiento. Cómo se reparten las demás entre Delegación y Descripción es **lectura nuestra**, porque el Index no publica ese mapeo. La conducta 12 es un aporte de este proyecto y no está en el Index.

| # | id | Conducta | Dimensión | Referencia Index |
|---|----|----------|-----------|------------------|
| 1 | `itera` | Itera y afina | Descripción* | 85,7 % |
| 2 | `aclara-objetivo` | Aclara el objetivo antes de pedir | Delegación* | 51,1 % |
| 3 | `da-ejemplos` | Muestra cómo se ve lo bueno | Descripción* | 41,1 % |
| 4 | `pide-formato` | Dice qué formato y estructura necesita | Descripción* | 30,0 % |
| 5 | `fija-modo` | Define cómo quiere trabajar con la IA | Descripción* | 30,0 % |
| 6 | `pide-tono` | Dice el tono y el estilo | Descripción* | 22,7 % |
| 7 | `nota-contexto-faltante` | Nota que a la IA le falta contexto | **Discernimiento** | 20,3 % |
| 8 | `define-audiencia` | Dice para quién es el resultado | Descripción* | 17,6 % |
| 9 | `cuestiona-razonamiento` | Cuestiona cuando el razonamiento no cuadra | **Discernimiento** | 15,8 % |
| 10 | `consulta-enfoque` | Consulta el enfoque antes de ejecutar | Delegación* | 10,1 % |
| 11 | `verifica-datos` | Pide fuente o verifica datos que importan | **Discernimiento** | 8,7 % |
| 12 | `decide-distinto` | Decide distinto a la IA, con argumento | Discernimiento (propia) | — |

\* Asignación nuestra. En **negrita**, las confirmadas por el Index.

Las conductas 7, 9, 11 y 12 son el **núcleo de criterio**: las que más tienen que ver con la duda metódica. El informe las muestra primero.

---

## Núcleo de criterio

### 7 · `nota-contexto-faltante` — Nota que a la IA le falta contexto

**Qué es.** La persona se da cuenta de que la respuesta parte de supuestos que no aplican a su caso, o de que a la IA le falta información para responder bien, y lo dice.

**Cuenta:**
- "Eso aplica en España, pero yo estoy en Colombia."
- "Te faltó saber que el equipo es de 3 personas."
- Preguntarle a la IA qué supuestos está haciendo.

**No cuenta:**
- Dar contexto de entrada, antes de que la IA responda. Eso es `aclara-objetivo`.
- Cambiar de tema.

**Estados:**
- **Ausente:** la persona acepta la respuesta aunque se basa en un supuesto equivocado que se ve en el chat.
- **Presente:** dice que algo no aplica, pero no explica qué falta ("eso no sirve para mi caso").
- **Con evidencia:** nombra en concreto el contexto que falta: un hecho, una cifra, una norma o una restricción de su caso ("Aquí la norma es la Ley 1581, no el RGPD", "el presupuesto del colegio es de 5 millones"). No hace falta que explique por qué cambia la respuesta si el dato ya lo deja claro.

**Señales:** "en mi caso", "no aplica", "te faltó", "no sabes que", "estás asumiendo", "¿qué estás suponiendo?"

**Ejemplos (ilustrativos):**
- *Ausente.* IA: «Para contratar a alguien por prestación de servicios, sigue estos pasos del Estatuto de los Trabajadores…» → Persona: «Listo, gracias.»
- *Presente.* Persona: «Eso no sirve para mi caso.»
- *Con evidencia.* Persona: «Eso es de España. En Colombia el contrato de prestación de servicios no genera prestaciones sociales, y justo eso es lo que necesito revisar.»

---

### 9 · `cuestiona-razonamiento` — Cuestiona cuando el razonamiento no cuadra

**Qué es.** La persona detecta un salto lógico, una contradicción o una conclusión que no se sigue, y lo señala.

**Cuenta:**
- "Dijiste A arriba y ahora B."
- "¿Por qué concluyes eso si el dato dice otra cosa?"
- Pedirle a la IA que muestre el paso a paso de una conclusión que no cuadra.

**No cuenta:**
- Decir "no me gusta" sobre un texto por estilo. Eso es `itera` o `pide-tono`.
- Pedir que "revise" sin decir qué falla.

**Estados:**
- **Ausente:** la IA se contradice o salta pasos y la persona sigue sin decir nada.
- **Presente:** muestra duda sin señalar el problema ("¿seguro?", "no creo").
- **Con evidencia:** señala dónde falla el razonamiento y por qué ("El 20 % es de ventas, no de margen; tu cálculo mezcla las dos").

**Señales:** "no cuadra", "te contradices", "¿por qué?", "no se sigue", "¿de dónde sale?", "revisa el paso"

**Ejemplos (ilustrativos):**
- *Ausente.* IA: «Como el curso tuvo 40 inscritos y 38 lo terminaron, fue un éxito de aprendizaje.» → Persona: «Perfecto, ponlo así en el informe.»
- *Presente.* Persona: «¿Seguro? No sé, no me convence.»
- *Con evidencia.* Persona: «Terminar el curso no es lo mismo que aprender. Tu conclusión salta de asistencia a aprendizaje sin pasar por la evaluación final, y ahí solo aprobaron 22 de 38.»

---

### 11 · `verifica-datos` — Pide fuente o verifica datos que importan

**Qué es.** Ante una cifra, una cita, una norma o un hecho del que depende algo, la persona pide la fuente, la contrasta o avisa que la va a verificar.

**Cuenta:**
- "¿De dónde sale ese 34 %?"
- "Busqué la sentencia y el número es otro."
- "Voy a revisar eso en la página del Ministerio." Esto cuenta como presente, porque la verificación en sí pasa fuera del chat.

**No cuenta:**
- Pedir fuentes de relleno para un texto sin que haya un dato en duda.
- Verificar detalles irrelevantes para la decisión.

**Estados:**
- **Ausente:** hay datos que importan y la persona los usa sin preguntar.
- **Presente:** pide la fuente o dice que va a verificar, sin traer resultado.
- **Con evidencia:** trae al chat lo que encontró (fuente, dato corregido, enlace) o contrasta dos fuentes.

**Señales:** "fuente", "¿de dónde sale?", "¿dónde dice?", "link", "verifiqué", "según [entidad]", "cita exacta"

**Ejemplos (ilustrativos):**
- *Ausente.* IA: «El 68 % de las pymes colombianas ya usa IA.» → Persona: «Buenísimo, lo pongo en la diapositiva 2.»
- *Presente.* Persona: «¿De dónde sale ese 68 %? Lo voy a revisar antes de usarlo.»
- *Con evidencia.* Persona: «Busqué ese 68 % y no lo encontré. Según la encuesta que sí encontré del gremio, la cifra es 31 % y habla de empresas medianas, no de pymes. Usemos esa.»

---

### 12 · `decide-distinto` — Decide distinto a la IA, con argumento *(propia)*

**Qué es.** La persona recibe una recomendación y decide otra cosa, o elige entre opciones con un criterio suyo. Es el cierre de la duda metódica: dudar para decidir, no para quedarse dudando.

**Cuenta:**
- "Prefiero la opción B porque el cliente ya conoce ese formato."
- "No voy a hacer lo que sugieres porque el presupuesto no da."

**No cuenta:**
- Rechazar sin decir por qué. Eso es presente, no con evidencia.
- Pedir más opciones sin elegir ninguna.

**Estados:**
- **Ausente:** la IA recomienda y la persona acepta, o el chat termina sin decisión visible. Ojo: aceptar no es malo; solo significa que esta conducta no apareció.
- **Presente:** decide distinto sin dar razón ("no, hagámoslo de otra forma").
- **Con evidencia:** decide distinto y explica el criterio (costo, contexto, riesgo, experiencia propia, dato).

**Señales:** "prefiero", "voy a", "mejor", "no voy a", "decidí", "en cambio", "porque"

**Ejemplos (ilustrativos):**
- *Ausente.* IA: «Te recomiendo enviar el informe completo de 15 páginas a la junta.» → Persona: «Dale, prepáralo.»
- *Presente.* Persona: «No, mejor hagamos otra cosa.»
- *Con evidencia.* Persona: «Prefiero mandar una página con tres cifras y el informe como anexo, porque la junta de este colegio no lee documentos largos antes de la reunión.»

---

## Delegación: qué y cómo se le pide a la IA

### 2 · `aclara-objetivo` — Aclara el objetivo antes de pedir

**Qué es.** Antes o al empezar, la persona dice para qué necesita el resultado, no solo qué quiere.

**Cuenta:** "Necesito esto para convencer a la junta de aprobar el presupuesto."
**No cuenta:** una orden sin propósito ("hazme un resumen").

**Estados:**
- **Ausente:** solo pide la tarea.
- **Presente:** da un objetivo general ("es para el trabajo").
- **Con evidencia:** el objetivo es concreto e incluye qué decisión o resultado depende de él.

**Señales:** "necesito esto para", "el objetivo es", "lo que busco es", "quiero lograr"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Hazme un resumen de este documento.»
- *Presente.* Persona: «Hazme un resumen de este documento, es para el trabajo.»
- *Con evidencia.* Persona: «Necesito un resumen de este documento para decidir el viernes si renovamos el contrato con el proveedor. Me importan sobre todo las penalidades y los plazos.»

---

### 10 · `consulta-enfoque` — Consulta el enfoque antes de ejecutar

**Qué es.** Antes de pedir el producto final, la persona pregunta cómo abordarlo o pide un plan para revisarlo.

**Cuenta:** "Antes de escribirlo, ¿cómo lo estructurarías?", "Dame tres enfoques y yo elijo."
**No cuenta:** pedir el producto directamente y corregirlo después. Eso es `itera`.

**Estados:**
- **Ausente:** va directo al producto.
- **Presente:** pide un plan o enfoques, pero los acepta sin revisarlos.
- **Con evidencia:** pide el enfoque y lo ajusta o elige con un criterio antes de ejecutar.

**Señales:** "antes de", "¿cómo lo abordarías?", "propón un plan", "dame opciones", "primero el esquema"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Escríbeme la propuesta para el cliente.»
- *Presente.* Persona: «Antes de escribirla, dame tres enfoques para la propuesta.» → IA propone tres → Persona: «Listo, el primero.»
- *Con evidencia.* Persona: «Antes de escribirla, dame tres enfoques.» → IA propone tres → Persona: «Me quedo con el segundo, porque este cliente ya rechazó una propuesta centrada en precio; le funciona más ver casos.»

---

## Descripción: cómo se comunica lo que se necesita

### 1 · `itera` — Itera y afina

**Qué es.** La persona no se queda con la primera versión de algo que la IA entregó: le pide cambios **a ese mismo resultado**, sea un texto, una tabla, un cálculo, un documento o un código.

**La prueba:** ¿la persona le está pidiendo a la IA que **modifique el contenido** de algo que ya entregó? Si sí, es itera. Si pide algo nuevo, es otra cosa.

**Cuenta:**
- "Acorta el segundo párrafo".
- "Rehaz la tabla con los datos de marzo".
- "En el documento, cambia el plazo a 8 semanas".
- "Quita la sección de riesgos del informe".

**No cuenta:**
- Hacer una pregunta nueva o de seguimiento ("¿y cuánto costaría?", "¿qué significa X?").
- Pedir que explique mejor ("no entiendo esa parte, explícamela con un ejemplo"). Eso es entender, no afinar el resultado.
- Pedir el mismo contenido en otro formato sin cambiarle nada ("pásalo a Word"). Eso es `pide-formato`.
- Dar un dato nuevo para una pregunta nueva. Eso puede ser `nota-contexto-faltante` o `aclara-objetivo`.
- Repetir la misma petición con otras palabras sin decir qué cambiar.

**Estados:**
- **Ausente:** no hay ningún pedido de cambio sobre algo que la IA entregó, aunque la conversación siga con otras preguntas.
- **Presente:** pide cambios genéricos ("mejóralo", "otra vez").
- **Con evidencia:** dice qué cambiar y por qué ("quita la tabla; el lector va a verlo en el celular").

**Nota:** es la conducta más común (85,7 %). Iterar mucho no equivale a tener criterio; cuenta más **cómo** se itera.

**Señales:** "cambia", "ajusta", "ahora", "mejor así", "quita", "agrega", "otra versión"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona pide un correo, recibe la primera versión y la copia tal cual.
- *Presente.* Persona: «Mejóralo.» → «Otra vez.» → «Hazlo mejor.»
- *Con evidencia.* Persona: «Quita la tabla y déjalo en dos párrafos, porque lo van a leer en el celular entre reuniones.»

---

### 3 · `da-ejemplos` — Muestra cómo se ve lo bueno

**Qué es.** La persona da un ejemplo, una muestra o un modelo de lo que espera.

**Cuenta:** pegar un correo anterior que funcionó, "algo como esto: …".
**No cuenta:** adjuntar material para que la IA lo resuma, lo corrija o lo convierta en otra cosa (por ejemplo, un documento para volverlo plantilla). Eso es insumo, no ejemplo de resultado.

**Estados:**
- **Ausente:** no hay ejemplo.
- **Presente:** da un ejemplo sin decir qué tiene de bueno.
- **Con evidencia:** da el ejemplo y señala qué rasgo copiar ("fíjate en que abre con la cifra").

**Señales:** "como este", "por ejemplo", "algo así", "este es el estilo", "toma como modelo"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Escríbeme un mensaje de bienvenida para los nuevos empleados.»
- *Presente.* Persona: «Escríbelo parecido a este:» (pega un mensaje anterior).
- *Con evidencia.* Persona: «Toma como modelo este mensaje del año pasado. Fíjate en que abre con el nombre de la persona y cierra con un contacto concreto; eso es lo que funcionó.»

---

### 4 · `pide-formato` — Dice qué formato y estructura necesita

**Qué es.** La persona especifica la forma del resultado: extensión, estructura, tabla, viñetas o secciones.

**Cuenta:** "Máximo una página, con tres secciones", "en tabla con estas columnas".
**No cuenta:** aceptar el formato que la IA eligió.

**Estados:**
- **Ausente:** no dice nada de la forma.
- **Presente:** da un formato sin razón.
- **Con evidencia:** el formato responde a un uso concreto ("en viñetas, porque lo voy a proyectar").

**Señales:** "en tabla", "viñetas", "máximo", "palabras", "secciones", "formato", "estructura"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Explícame los cambios de la reforma.»
- *Presente.* Persona: «Explícamelo en una tabla.»
- *Con evidencia.* Persona: «Ponlo en una tabla de tres columnas (antes, ahora, qué hacemos), porque la voy a proyectar en el comité y tiene que caber en una diapositiva.»

---

### 5 · `fija-modo` — Define cómo quiere trabajar con la IA

**Qué es.** La persona le dice a la IA qué papel cumplir o cómo interactuar: que pregunte antes, que critique, que vaya paso a paso, que no dé la respuesta.

**Cuenta:** "Hazme preguntas antes de responder", "Actúa como un revisor exigente", "No me des la solución, guíame".
**No cuenta:** instrucciones sobre el producto. Eso es formato o tono.

**Estados:**
- **Ausente:** no define la interacción.
- **Presente:** define un modo genérico ("actúa como experto").
- **Con evidencia:** define un modo que sirve a su objetivo ("hazme de abogado del diablo, que mañana me van a cuestionar esto").

**Señales:** "actúa como", "hazme preguntas", "paso a paso", "no me des", "critica", "sé duro"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Revisa mi plan de clase.»
- *Presente.* Persona: «Actúa como un experto y revisa mi plan de clase.»
- *Con evidencia.* Persona: «Hazme de abogado del diablo con este plan de clase. Mañana lo presento a coordinación y quiero llegar con las objeciones ya pensadas.»

---

### 6 · `pide-tono` — Dice el tono y el estilo

**Qué es.** La persona especifica cómo debe sonar el resultado.

**Cuenta:** "Cercano pero sin tutear", "sin tecnicismos", "como hablamos en Colombia".
**No cuenta:** corregir errores de contenido.

**Estados:**
- **Ausente:** no dice nada del tono.
- **Presente:** pide un tono genérico ("más profesional").
- **Con evidencia:** el tono responde a la relación o a la situación ("es para un cliente molesto; firme pero sin sonar a disculpa legal").

**Señales:** "tono", "formal", "cercano", "sin tecnicismos", "que suene", "estilo"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Responde este correo del cliente.»
- *Presente.* Persona: «Responde este correo, que suene más profesional.»
- *Con evidencia.* Persona: «El cliente está molesto por la demora. Que suene firme pero cercano, sin frases de disculpa legal, porque llevamos 5 años trabajando juntos.»

---

### 8 · `define-audiencia` — Dice para quién es el resultado

**Qué es.** La persona dice quién va a leer o usar lo que la IA produce.

**Cuenta:** "Es para docentes de primaria", "lo va a leer la gerente financiera".
**No cuenta:** decir para quién es la persona misma ("soy abogado"). Eso es contexto, no audiencia.

**Estados:**
- **Ausente:** no menciona audiencia.
- **Presente:** menciona una audiencia genérica ("para el público").
- **Con evidencia:** describe la audiencia con lo que sabe, necesita o le preocupa ("gerentes que no leen más de un párrafo y solo quieren el riesgo").

**Señales:** "es para", "lo va a leer", "mi público", "mis estudiantes", "el cliente", "la junta"

**Ejemplos (ilustrativos):**
- *Ausente.* Persona: «Explica qué es la inteligencia artificial.»
- *Presente.* Persona: «Explica qué es la IA para el público general.»
- *Con evidencia.* Persona: «Es para docentes de primaria rurales que no usan computador a diario y a quienes les preocupa que los reemplacen. Explícalo desde ahí.»

---

## Casos límite: cómo desempatar

Estas reglas salieron de comparar dos lecturas independientes de conversaciones reales. Cuando dudes, usa estas.

**Unidad de medida.** Cada conversación recibe, por conducta, el estado más alto que aparezca en cualquier mensaje de la persona. Un mismo mensaje puede contar para varias conductas si hace varias cosas.

**¿Dato nuevo a mitad del chat: contexto faltante o solo contexto?**
- Es `nota-contexto-faltante` si el dato **corrige o completa un supuesto** sobre el que la IA ya respondió, y cambia esa respuesta ("eso es para España", "no es para empresas grandes, es para tiendas de barrio").
- Si el dato acompaña una **petición nueva** y la IA no había supuesto nada sobre eso, no es contexto faltante. Si dice para qué es, es `aclara-objetivo`.
- Si la IA **preguntó** y la persona solo responde, no es contexto faltante: la IA ya había notado que le faltaba. Cuenta solo si la persona corrige algo que la IA había dado por hecho.

**¿Pregunta de aclaración o cuestionar el razonamiento?**
- Pedir que explique algo ("¿qué significa margen bruto?", "explícame esta cifra") **no** es cuestionar. Es entender.
- Es `cuestiona-razonamiento` **presente** si la persona muestra duda sobre una conclusión sin decir qué falla ("¿seguro?", "no creo que sea así").
- Es **con evidencia** si trae algo que contradice la conclusión: un error concreto (una suma, una cifra que no cuadra), un documento o dato que dice otra cosa, o un contraargumento propio.

**¿"Muéstrame antes de generar": fijar el modo o consultar el enfoque?**
- "No actualices todavía", "muéstrame primero en el chat" o "hazme preguntas antes" definen **cómo trabajar**. Eso es `fija-modo`.
- Es `consulta-enfoque` si pide **opciones, un plan o una recomendación sobre cómo resolver** la tarea antes de hacerla ("¿qué enfoque sugieres?", "dame tres opciones").
- Pedir opciones **de un contenido** (nombres, títulos, frases, eslóganes) no es consultar el enfoque: es pedir el producto.
- Consulta-enfoque **con evidencia**: la persona elige o ajusta una de las opciones y dice por qué.

**¿Decidir distinto o solo poner requisitos?**
- `decide-distinto` exige que la IA **haya recomendado o propuesto algo** y que la persona escoja otra cosa o modifique la propuesta.
- Si la persona pone condiciones sin que hubiera una recomendación antes, es `aclara-objetivo` o `itera`.

**¿Pedirle a la IA que busque algo cuenta como verificar?**
- Pedirle que confirme o busque un dato ("confirma esa tasa de interés, creo que es otra", "revisa si esa norma sigue vigente") es `verifica-datos` **presente**.
- Es **con evidencia** si la persona trae la fuente o el resultado al chat: un enlace a la fuente primaria, un documento, un pantallazo, o lo que otra herramienta le mostró.
- Decidir consultar a una persona experta o a quien es fuente directa (el equipo del producto, la entidad, un especialista) también es `verifica-datos` **presente**, aunque la IA no haya recomendado nada. No es `decide-distinto`.

**¿Qué cuenta como tono?**
- Tono es **cómo debe sonar un texto**: formal, cercano, directo o sin frases de IA.
- El estilo visual de un diseño ("que se vea moderno", "en blanco y negro") no es tono; es `pide-formato`. También es formato el idioma del resultado ("en inglés", "en español de Colombia"). El estilo de un nombre no cuenta en ninguna de las dos.
- Con evidencia: el tono va ligado a la relación o la situación ("que no suene a reclamo, porque es un cliente que quiero conservar").

**¿Nombrar al destinatario ya es definir la audiencia?**
- Nombrarlo ("es para la rectora", "es para el comité de compras") es `define-audiencia` **presente**.
- Es **con evidencia** si dice algo de lo que esa audiencia sabe, necesita, le preocupa o de cómo va a usar el resultado: "es para el cliente, así que nada de cifras internas", "la junta cree que esto es muy costoso".

**¿Objetivo presente o con evidencia?**
- Decir qué quiere ("quiero un análisis de mercado") no basta. **Presente** es decir para qué ("para presentar al cliente").
- **Con evidencia** es decir qué decisión o resultado concreto depende de eso ("para decidir el viernes si renovamos", "para escoger proveedor antes de fin de mes").

---

## Señal de descarga cognitiva

No es una conducta más: es una lectura de conjunto que el informe agrega al final. **Descarga cognitiva** es dejarle a la herramienta un esfuerzo mental que antes hacías tú. No es mala en sí misma: delegar el formato de una tabla libera la cabeza para lo que importa. El problema es delegar también el juicio.

Se marca así, mirando solo los mensajes de la persona:

- **Posible descarga:** las 4 conductas del núcleo salen ausentes **y** la persona le pidió a la IA una decisión, un análisis o un texto para entregar, **y** lo aceptó sin cambios de fondo ("perfecto, gracias", "listo, lo mando").
- **Descarga parcial:** las 4 del núcleo salen ausentes, pero la persona sí aportó su parte en la Descripción (aclaró el objetivo, dio contexto, iteró). Preparó bien el pedido, pero no revisó la respuesta.
- **Sin señal:** al menos una conducta del núcleo está presente o con evidencia.

Casos límite:
- Si la tarea era mecánica (traducir, dar formato, resumir para uso propio), la posible descarga se reporta como **«delegación razonable»**: no es un problema.
- Si hay menos de 3 mensajes de la persona, no se marca.
- La señal se dice sin regañar, con una sola acción concreta: «Antes de usar esto, escribe en una línea qué habrías decidido tú y compáralo».

*Ilustrativo:* una persona pide «hazme el análisis de estos tres proveedores y dime cuál escojo», recibe la recomendación y responde «listo, gracias, me voy con ese». Núcleo ausente, decisión aceptada sin cambios: **posible descarga**.

---

## Cómo se arma el informe

1. Cada conversación recibe un estado por conducta: ausente, presente o con evidencia.
2. Cada estado distinto de ausente va con la cita que lo justifica.
3. El informe muestra primero el núcleo de criterio (7, 9, 11 y 12) y después el resto.
4. La conducta más débil es la de menor proporción de "con evidencia" dentro del núcleo. Esa es la que toma el coach.
5. Después de la tabla va la señal de descarga cognitiva (ver arriba).
6. Siempre cierra con lo que no mide (ver abajo).

## Lo que esta rúbrica no puede ver

- **Lo que pasa en tu cabeza.** Si dudaste y no lo escribiste, para la rúbrica no existe.
- **Lo que verificas fuera del chat.** Si revisaste el dato en otra pestaña y no lo contaste, aparece como ausente.
- **Si al final la decisión fue buena.** La rúbrica ve el proceso, no el resultado.
- **El contexto de la tarea.** En un chat para pasar el rato, no verificar es razonable. Ausente no siempre es malo.

---

*Contenido bajo CC BY 4.0. Conductas redactadas a partir del marco 4D de Dakan y Feller (CC BY-NC-SA 4.0) y del AI Fluency Index de Anthropic (feb 2026). Ver `fundamentos.md`.*
