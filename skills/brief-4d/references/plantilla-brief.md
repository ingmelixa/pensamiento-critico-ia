# Plantilla de entrega del brief 4D

Entrega estas piezas, en este orden, con listas (no tablas). El prompt no lo entregas tú: lo escribe la persona.

## 1. Tu brief

**Delegación:** cómo se reparte el trabajo y qué se queda contigo (2 a 4 líneas).
**Descripción:** producto, proceso y comportamiento, en pocas líneas.
**Discernimiento:** criterios de aceptación, el dato que se verifica y dónde, tu respuesta primero.
**Diligencia:** qué datos se reemplazaron, quién debe saber que usaste IA, quién firma.

## 2. Checklist para revisar la respuesta

De 3 a 5 casillas:
- [ ] Cada criterio de aceptación.
- [ ] El dato que se verifica, en su fuente.
- [ ] ¿Qué supuso la IA que no aplica a mi caso?
- [ ] Transparencia: a quién le cuento que usé IA y quién firma.

## 3. Tu prompt: lo escribes tú

Pide: «Ahora escribe tú el prompt con tus palabras, a partir del brief. No tiene que quedar perfecto».

Cuando la persona lo pegue, responde solo con:
- Máximo 3 cosas que le faltan frente al brief (por ejemplo: «no dice para quién es», «falta el marcador de la cifra»).
- La sugerencia de terminar con: «Antes de responder, dime qué estás suponiendo sobre mi caso».
- No lo reescribas. Si la persona pide el prompt hecho, dáselo, y pídele que lo lea y cambie al menos una cosa antes de usarlo.

**Por qué así:** si la IA escribe el prompt y la persona solo lo copia, la IA hizo la Descripción por ella. Eso es descarga cognitiva: justo lo que el brief quiere evitar.

Cierra con: «Cuando termines la conversación, pide tu reporte de criterio (skill `detector` o `prompts/reporte.txt`)».

---

## Ejemplo ilustrativo (inventado)

**Tarea:** «Soy coordinadora de una cooperativa pequeña. Quiero un comunicado para los asociados sobre el cambio de horario de atención.»

**Primera ronda:**
- Para qué: sale el lunes; si no se entiende, se llenan las líneas de quejas.
- Lo que solo ella sabe: muchos asociados son mayores y leen por WhatsApp.
- Qué no pegar: la base de asociados.

**Brief:**
- **Delegación:** la IA redacta y tú revisas. El horario exacto y la firma son tuyos.
- **Descripción:** mensaje de WhatsApp de menos de 80 palabras y una versión para cartelera; tono cercano, sin tecnicismos; antes de escribir, que diga qué está suponiendo.
- **Discernimiento:** sirve si se entiende en una sola lectura y si dice el día del cambio. El dato que se verifica: el horario nuevo, contra el acta del consejo. Tu respuesta primero: «Yo lo mandaría el viernes, no el lunes».
- **Diligencia:** no se pega ningún dato de asociados; el comunicado lo firma la gerencia.

**Su prompt, primera versión:**
> Hazme un comunicado para los asociados sobre el cambio de horario, que sea corto.

**Retroalimentación (sin reescribirlo):**
- No dice que lo van a leer personas mayores por WhatsApp.
- Falta el formato: las dos versiones y el límite de 80 palabras.
- Falta la fecha y el horario: usa los marcadores `[FECHA]` y `[HORARIO]`.

**Su prompt, segunda versión:**
> Necesito un comunicado para los asociados de una cooperativa pequeña sobre un cambio de horario de atención que empieza el [FECHA]. El horario nuevo es [HORARIO]. Muchos asociados son personas mayores y lo van a leer por WhatsApp. Quiero dos versiones: un mensaje de WhatsApp de menos de 80 palabras y un texto para cartelera. Tono cercano, sin tecnicismos. Antes de responder, dime qué estás suponiendo sobre mi caso.

**Checklist:**
- [ ] ¿Se entiende en una sola lectura?
- [ ] ¿Dice el día del cambio?
- [ ] ¿El horario coincide con el acta del consejo?
- [ ] ¿Qué supuso la IA que no aplica?

---

*Contenido bajo CC BY 4.0.*
