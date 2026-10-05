# Reporte esperado del chat de demostración

Es lo que la rúbrica dice que debería salir al pegar `chat-demo.txt`. Sirve como plan B si la demo en vivo falla, y para revisar si una IA aplicó bien la rúbrica. La conversación es inventada: Marta y su panadería no existen.

**Resumen esperado:** Marta corrigió bien el contexto (Manizales, no Bogotá) y decidió con argumentos propios. Lo más flojo fue **verificar datos**: aceptó sin preguntar que «el 60 % de las panaderías cierra antes de dos años», y ese dato pesó en su decisión.

| Conducta | Estado | Frase | Por qué |
|---|---|---|---|
| Nota contexto faltante | **con evidencia** | «Estoy en Manizales, no en Bogotá. Aquí el local que estoy mirando en el barrio cuesta 2,8 millones al mes» | La IA dio por hecho que era Bogotá; Marta la corrigió con la ciudad y cifras concretas. |
| Cuestiona el razonamiento | **presente** | «¿Seguro? No sé.» | Dudó, pero no dijo qué no cuadraba. El cálculo tenía un error: 5,5 millones ÷ 35 % son casi 16 millones, no 8. |
| Verifica datos | **ausente** | — | Nunca preguntó de dónde salía el 60 %, y ese dato le preocupó al decidir. |
| Decide distinto | **con evidencia** | «Prefiero el local del barrio, porque mis clientes fijos viven cerca y en el centro comercial no puedo abrir a las 6 de la mañana» | La IA recomendó dos veces el centro comercial; Marta eligió otra cosa y dio dos razones. |
| Itera | **con evidencia** | «Quita la fila de publicidad, eso lo maneja mi hija aparte.» | Pidió cambiar la tabla que la IA ya había entregado y dijo por qué. |
| Aclara el objetivo | **con evidencia** | «Ayúdame a decidir si vale la pena y dónde.» | Dijo qué decisión dependía de la respuesta. |
| Pide formato | **con evidencia** | «Hazme una tabla comparando las dos opciones, para mostrársela a mi socio el sábado.» | Pidió una tabla y dijo para qué la iba a usar. |
| Define la audiencia | **presente** | «para mostrársela a mi socio el sábado» | Nombró al destinatario, pero no dijo qué sabe o qué le importa. |
| Consulta el enfoque | ausente | — | |
| Fija el modo | ausente | — | |
| Pide tono | ausente | — | |
| Da ejemplos | ausente | — | |

**¿Hubo descarga cognitiva?** Sin señal: Marta tuvo dos conductas del núcleo (contexto faltante y decide distinto), así que no le dejó el juicio a la IA. Si una IA marca «posible descarga» en este chat, está mal.

**Para practicar (verificar datos):** antes de dejar que una cifra pese en una decisión, pregunta «¿de dónde sale ese 60 %?» y busca la fuente.

## Momentos para señalar en la demo

1. **El 60 %.** La IA lo repitió dos veces y Marta lo aceptó. Es el caso típico del Index: la respuesta suena segura y nadie la revisa.
2. **El error del cálculo.** «¿Seguro? No sé.» es duda sin evidencia. Con evidencia habría sido: «5,5 millones dividido 0,35 da casi 16 millones, no 8».
3. **La decisión.** Marta no le llevó la contraria a la IA por llevarla: dio razones que solo ella conoce, sus clientes y su horario. Eso es criterio.

## Qué puede variar entre IA

- **Aclara el objetivo** puede salir «presente» en lugar de «con evidencia». Los dos son defendibles.
- **Define la audiencia** a veces sale «con evidencia». Según la rúbrica es «presente», porque solo nombra al socio.
- Si una IA marca **verifica datos** como «presente» o «con evidencia», está mal: Marta nunca pidió la fuente.
- Los modelos pequeños o gratuitos a veces cuentan la decisión de Marta dos veces: como *decide distinto* y también como *cuestiona el razonamiento* «con evidencia». Está mal: escoger otra opción con razones es decidir distinto; cuestionar es dudar de una conclusión de la IA. Si pasa en vivo, úsalo como ejemplo: detectarlo es cuestionar el razonamiento de la IA.

**Prueba a ciegas (30 de septiembre de 2026):** Claude coincidió 12 de 12 con este reporte. Claude Haiku coincidió 10 de 12; después de ajustar el prompt, acertó las 4 del núcleo.
