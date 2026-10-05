# Manual de uso

Qué decirle a cada IA para **preparar** una tarea, **conversar** y **medir** tu criterio. Si todavía no instalaste nada, mira el [manual de instalación](instalacion.md) o usa los prompts para pegar: funcionan en cualquier IA.

> **Nota sobre los enlaces.** Los enlaces usan `https://github.com/gutiedward/pensamiento-critico-ia`. Si el repositorio cambia de dirección, busca el mismo archivo en la nueva.
>
> Lo marcado con «⚠️ por confirmar en la prueba» todavía no se ha probado en ese producto.

---

## El ciclo en 3 pasos

1. **Preparar** (brief 4D): antes de pedir algo, la IA te hace preguntas con las 4D (Delegación, Descripción, Discernimiento y Diligencia) y te entrega un brief y un checklist.
2. **Conversar**: haces tu tarea con la IA, en otro chat, usando **tu** prompt y tu checklist.
3. **Medir** (reporte o detector): al final pides tu reporte de criterio.

Si una conducta te sale floja, el **coach** te propone un ejercicio de 10 minutos.

### Dos cosas que hace distinto `criterio`

- **El prompt lo escribes tú.** El brief 4D no te entrega un prompt listo. Te pide primero tu criterio («sirve si…») y qué harías tú. Cuando escribes tu prompt, la IA te dice **máximo 3 cosas** que le faltan, sin reescribirlo. Si le pides el prompt hecho, te lo da, pero te pide cambiar al menos una cosa. ¿Por qué? Si solo copias, la IA pensó por ti. Eso es **descarga cognitiva**: dejar que la IA piense por ti.
- **El reporte te dice si hubo descarga cognitiva.** Además de las 12 conductas, trae la línea **«¿Hubo descarga cognitiva?»** con una de cuatro señales: *sin señal*, *delegación razonable*, *descarga parcial* o *posible descarga*.

### Privacidad, en corto

- **Lo que pegas en un chat sale de tu equipo** y llega al proveedor de esa IA, con sus condiciones. No pegues datos personales ni de clientes: en Colombia están protegidos por la Ley 1581. Usa marcadores como `[CLIENTE]` o `[VALOR]`.
- **El analizador de historial no usa internet.** Todo se queda en tu computador, salvo que tú decidas pasarle los lotes a una IA.

---

## Claude

### 1. claude.ai (web), app de escritorio y celular

**Con las skills instaladas**, basta con pedirlo en palabras normales:

| Para | Escribe | Qué pasa |
|---|---|---|
| Preparar | «Ayúdame a preparar lo que le voy a pedir a la IA: [tu tarea]» | `brief-4d` te entrevista. No hace la tarea. |
| Medir | «Dame mi reporte de criterio» (al final del chat) | `detector` te da la tabla de 12 conductas, tus frases y «¿Hubo descarga cognitiva?» |
| Practicar | «Dame un ejercicio para mejorar mi criterio» | `coach` te propone uno de 10 minutos |
| Historial | «Revisa mi historial» y sube tu exportación | `revision-de-historial` corre el analizador |

Pasos para el ciclo completo:
1. Abre un chat nuevo y escribe: «Ayúdame a preparar lo que le voy a pedir a la IA: [tu tarea en una línea]».
2. Responde las dos rondas de preguntas. En la segunda, escribe tu criterio («sirve si…») y qué harías tú.
3. Lee tu brief y tu checklist.
4. Escribe tu prompt con tus palabras y pégalo. La IA te dice qué le falta. Ajústalo.
5. Abre **otro chat nuevo**, pega tu prompt y conversa con al menos 4 o 5 mensajes tuyos.
6. Al final, en ese mismo chat, escribe: «Dame mi reporte de criterio».
7. Revisa que las frases sean **tuyas, tal cual**, y que el «Por qué» te convenza.

**El detector no comenta mientras conversas.** Solo responde cuando le pides el reporte. Si comenta cada mensaje, algo está mal: anótalo.

**Revisar tu historial desde claude.ai:** sube el `.zip` de tu exportación al chat y escribe «Revisa mi historial». Ojo: al subirlo, **tus chats salen de tu equipo** hacia Anthropic. Si prefieres que no salgan, usa el [analizador en tu computador](#analizador-de-historial-python-en-tu-computador). ⚠️ por confirmar en la prueba: que el script corra bien dentro de claude.ai.

**En el celular:** ⚠️ por confirmar en la prueba que las skills se activen en la app. Si no, usa los prompts (ver [Cualquier otra IA](#cualquier-otra-ia-solo-los-prompts)). Tip: el brief entrega todo en listas, sin tablas, para que se lea bien en la pantalla pequeña.

**Sin skills:** usa los prompts para pegar.

### 2. Claude Code

Las mismas frases funcionan. También puedes llamar cada skill directo:
- `/brief-4d` para preparar.
- `/detector` para el reporte.
- `/coach` para el ejercicio.
- `/revision-de-historial` para el historial. Te pide la ruta de la exportación, corre `analizar.py` en tu equipo y, **antes de leer tus chats para el reporte completo, te pide permiso**, porque en ese paso el texto pasa por el modelo.

### 3. API de Claude

No hay un flujo de `criterio` para la API. Si programas, puedes mandar el texto de `prompts/*.txt` como mensaje. No se ha probado.

---

## ChatGPT

En cuentas personales (Free, Plus, Pro) no hay skills: usa los prompts o un Proyecto (ver [instalación](instalacion.md#chatgpt)). Funciona en la web, la app de escritorio y el celular.

**Preparar:**
1. Abre un chat nuevo (o un chat dentro del proyecto «criterio · brief»).
2. Si no usas proyecto, pega [`brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt) completo.
3. Escribe tu tarea en una línea al final y envía.
4. Responde las preguntas y escribe tu prompt. ChatGPT te dice qué le falta.

**Conversar:** chat nuevo, pega tu prompt, conversa.

**Medir:**
1. Al final del chat, pega [`reporte.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/reporte.txt) completo.
   - Si conversaste dentro del proyecto «criterio · reporte», basta con escribir «dame mi reporte de criterio».
2. Revisa las frases, el «Por qué» y la línea «¿Hubo descarga cognitiva?».

**Practicar:** después del reporte, pega [`coach.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/coach.txt).

**Con ChatGPT Business, Enterprise o Edu y las skills subidas:** usa las mismas frases que en Claude, o llama la skill con `@` (por ejemplo, `@detector`). ⚠️ por confirmar en la prueba.

---

## Gemini

**Con las skills subidas** (cuenta personal, 18 años o más):
1. Escribe `/` en el chat y elige la skill, o usa las mismas frases que en Claude.
2. Funciona también en la app del celular, si ya subiste las skills desde el computador.
3. ⚠️ por confirmar en la prueba: que se activen solas con la frase y que el detector no comente cada mensaje.

**Con una Gem:** abre la Gem «criterio · brief» o «criterio · reporte» en la barra lateral y conversa ahí.

**Con los prompts:** igual que en ChatGPT.

**Ojo con Gemini:** en una prueba anterior calificó más alto de lo que la rúbrica permite y dijo cosas que la persona «hizo» fuera del chat. El prompt ya se ajustó, pero revisa bien las citas y desconfía de un reporte con casi todo «con evidencia».

---

## Cualquier otra IA: solo los prompts

1. **Preparar:** pega [`brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt) en un chat nuevo y escribe tu tarea al final.
2. **Conversar:** en otro chat, pega el prompt que **tú** escribiste.
3. **Medir:** al final de ese chat, pega [`reporte.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/reporte.txt).
4. **Practicar:** pega [`coach.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/coach.txt).

**Desde el celular:** abre el enlace del prompt, mantén presionado el texto, **Seleccionar todo › Copiar**, y pégalo en la app de tu IA.

**¿No tienes una tarea a mano?** Copia [`taller/chat-demo.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/taller/chat-demo.txt), pégalo completo en un chat nuevo (ya trae el pedido del reporte adentro). Compara con [el reporte esperado](../taller/chat-demo-reporte-esperado.md).

---

## Analizador de historial (Python, en tu computador)

Revisa muchas conversaciones a la vez. Corre en tu computador y **no envía nada a internet**.

### 1. Exporta tu historial

- **ChatGPT:** Configuración › Controles de datos › Exportar datos › Confirmar. Te llega un correo con el enlace; puede tardar. Disponible en Free, Go, Plus, Pro y Edu, no en Business ni Enterprise ([fuente](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data)).
- **Claude:** en la web o la app de escritorio, Configuración › Privacidad › Exportar datos. No se puede desde la app del celular. Te llega un enlace por correo que vence en 24 horas ([fuente](https://support.claude.com/en/articles/9450526-export-your-claude-data)).
- **Gemini:** Google Takeout › Mi actividad › Apps de Gemini. *Soporte experimental:* no se ha probado con una exportación real.

### 2. Corre el analizador

Abre la Terminal en la carpeta del repositorio y escribe:

```bash
python3 skills/revision-de-historial/scripts/analizar.py --entrada ~/Downloads/conversations.zip
```

En Windows:

```
py skills\revision-de-historial\scripts\analizar.py --entrada %USERPROFILE%\Downloads\conversations.zip
```

- Puedes pasarle el `.zip`, la carpeta descomprimida, `conversations.json` (ChatGPT o Claude) o `MyActivity.json` (Gemini).
- Puedes pasarle varias exportaciones a la vez: `--entrada chatgpt.zip claude.zip`.

### 3. Abre el reporte

Abre `criterio-salida/reporte.html` en tu navegador. Trae un resumen, el tablero de las 12 conductas, la evolución por mes y **«Verifica tú mismo»**, con tus frases y un botón «No estoy de acuerdo». Tus marcas se guardan solo en tu navegador.

### Opciones útiles

| Opción | Para qué |
|---|---|
| `--salida <carpeta>` | Dónde dejar los resultados (por defecto `criterio-salida`) |
| `--desde 2026-01-01` / `--hasta 2026-06-30` | Filtrar por fechas |
| `--buscar propuesta` | Solo chats que contengan esa palabra |
| `--min-turnos 3` | Solo chats con al menos 3 mensajes tuyos (por defecto 2) |
| `--muestra 60` | Analizar 60 chats al azar |
| `--semilla 2026` | Repetir la misma muestra al azar |
| `--sin-lotes` | No crear los lotes para clasificar con una IA |
| `--clasificacion <archivos>` | Armar el reporte completo con lo que devolvió la IA |

### Dos niveles de reporte

1. **Pre-marcado** (lo que sale al correr el script): busca frases típicas. Lo que marca suele ser cierto, pero **se le escapa la mayoría**. Es un piso, no tu nota.
2. **Reporte completo:** el script deja tus chats en `criterio-salida/lotes/`, con instrucciones adentro. Se los pasas a una IA (en Claude, la skill `revision-de-historial` lo hace por ti), guardas sus respuestas como `clasificacion_001.json`, etc., y corres:
   ```bash
   python3 skills/revision-de-historial/scripts/analizar.py --entrada ~/Downloads/conversations.zip \
       --clasificacion criterio-salida/lotes/clasificacion_*.json
   ```
   **Ojo:** en este paso el texto de tus chats **sí sale de tu equipo** hacia esa IA.

*Contenido bajo CC BY 4.0.*
