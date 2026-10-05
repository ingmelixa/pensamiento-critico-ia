# Manual de instalación

Cómo dejar listo `criterio` en tu IA. Si no quieres instalar nada, ve directo a [Cualquier otra IA](#cualquier-otra-ia-solo-los-prompts): con pegar un texto basta, en cualquier IA y desde el celular.

> **Nota sobre los enlaces.** Los enlaces usan `https://github.com/gutiedward/pensamiento-critico-ia`. Si el repositorio cambia de dirección, busca el mismo archivo en la nueva.
>
> **Revisado el 5 de octubre de 2026** con la documentación oficial de cada producto (las URL van en cada sección). Los productos cambian rápido: lo marcado con «⚠️ por confirmar en la prueba» todavía no se ha probado.

---

## Antes de empezar: qué hay para instalar

| Pieza | Qué es | Dónde está |
|---|---|---|
| **Prompts** | Textos para pegar en cualquier chat | `prompts/brief.txt`, `prompts/reporte.txt`, `prompts/coach.txt` |
| **Skills** | Carpetas con un `SKILL.md` que la IA carga sola cuando hacen falta | `skills/brief-4d`, `skills/detector`, `skills/coach`, `skills/revision-de-historial` |
| **Analizador** | Un script de Python que revisa tu historial exportado, en tu computador | `skills/revision-de-historial/scripts/analizar.py` |

### Conseguir los `.zip` de las skills

Algunas IA piden cada skill como un archivo `.zip`. Descárgalos de Releases:

1. Abre https://github.com/gutiedward/pensamiento-critico-ia/releases/latest
2. En «Assets», descarga `brief-4d.zip`, `detector.zip`, `coach.zip` y `revision-de-historial.zip`.
3. **No los descomprimas.** Se suben tal cual. Cada `.zip` trae la carpeta de la skill como raíz.

---

## Claude

### 1. claude.ai (web), app de escritorio y celular

**Qué dice la documentación oficial** ([Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)):
- Las skills están disponibles en los planes **Free, Pro, Max, Team y Enterprise**.
- **Necesitan la ejecución de código activada**, para todas las skills, no solo para `revision-de-historial`.
- Las skills propias se suben como `.zip` en **Customize › Skills** (en la interfaz en español puede aparecer como «Personalizar › Skills»).
- El `.zip` debe tener la carpeta de la skill como raíz. Los de `criterio` ya vienen así.

**Pasos (en el navegador, en claude.ai):**
1. Entra a https://claude.ai con tu cuenta.
2. Ve a **Configuración › Capacidades** (*Settings › Capabilities*).
3. Activa **Ejecución de código y creación de archivos** (*Code execution and file creation*).
   - En planes Team o Enterprise, quien administra la organización debe permitirlo en *Organization settings › Plugins & skills*.
4. Ve a **Personalizar › Skills** (*Customize › Skills*).
5. Toca **+**, luego **Crear skill** (*Create skill*) y luego **Subir una skill** (*Upload a skill*).
6. Elige `brief-4d.zip`.
7. Repite los pasos 5 y 6 con `detector.zip`, `coach.zip` y `revision-de-historial.zip`.
8. Revisa que las cuatro queden con el interruptor **encendido**. Una skill apagada no se usa.

**App de escritorio (Mac y Windows):** usa la misma cuenta. ⚠️ por confirmar en la prueba: que las skills subidas en la web aparezcan solas en la app de escritorio.

**Celular (iOS y Android):** la documentación de skills no dice si funcionan en la app móvil. ⚠️ por confirmar en la prueba. Mientras tanto:
- Sube las skills desde el navegador del computador (pasos de arriba).
- En el celular, si la skill no responde, **pega el prompt** (ver [Cualquier otra IA](#cualquier-otra-ia-solo-los-prompts)). Siempre funciona.

### 2. Claude Code

**Qué dice la documentación oficial** ([Skills en Claude Code](https://code.claude.com/docs/en/skills)):
- Skills personales: `~/.claude/skills/<nombre>/SKILL.md`, para todos tus proyectos.
- Skills de un proyecto: `.claude/skills/<nombre>/SKILL.md`, solo en ese repositorio.
- Claude Code detecta los cambios en esas carpetas sin reiniciar. Si la carpeta `skills/` no existía antes, corre `/reload-skills`.
- `/skills` lista las skills disponibles.

**Pasos:**
1. Descarga el repositorio:
   ```bash
   git clone https://github.com/gutiedward/pensamiento-critico-ia.git
   cd pensamiento-critico-ia
   ```
2. Copia las cuatro skills a tu carpeta personal:
   ```bash
   mkdir -p ~/.claude/skills
   cp -R skills/brief-4d skills/detector skills/coach skills/revision-de-historial ~/.claude/skills/
   ```
   O, para un solo proyecto, cópialas a `.claude/skills/` dentro de ese proyecto.
3. Abre Claude Code. Si ya estaba abierto y la carpeta era nueva, escribe `/reload-skills`.
4. Escribe `/skills` y revisa que aparezcan `brief-4d`, `detector`, `coach` y `revision-de-historial`.

### 3. API de Claude

Aplica solo si programas. La API acepta skills propias con el endpoint `POST /v1/skills`, y cada petición debe incluir la herramienta de ejecución de código. Esas skills **no se comparten con claude.ai**: viven en tu espacio de trabajo de la API y se pagan por uso ([guía de skills en la API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)).

Para el público del taller **no hace falta**. `criterio` no trae código para la API y esa vía no se probó. ⚠️ por confirmar si alguien la necesita.

---

## ChatGPT

**Qué dice la documentación oficial:**
- ChatGPT **sí tiene Skills** (con `SKILL.md`), pero solo para **Business, Enterprise, Healthcare y Edu**. Las cuentas **Free, Plus y Pro no están incluidas** ([Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)). Se suben con **Create › Upload from your computer**, en *Plugins › Skills*.
- Los **GPT personalizados ya no se pueden crear** en cuentas personales (Free, Go, Plus ni Pro) ([Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)).
- Los **Proyectos** sí están en el plan gratuito y aceptan instrucciones propias ([Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)).
- **Codex** (la herramienta para programar de OpenAI) lee skills de `~/.agents/skills` y `.agents/skills` ([Build skills](https://learn.chatgpt.com/docs/build-skills)).

### Si tienes cuenta personal (Free, Plus o Pro): un Proyecto con instrucciones

Así no tienes que pegar el prompt cada vez. Haz un Proyecto por prompt.

1. En https://chatgpt.com, en la barra lateral, crea un **Proyecto nuevo**. Ponle de nombre «criterio · reporte».
2. Abre el menú **•••** del proyecto y entra a **Configuración del proyecto** (*Project settings*).
3. En **Instrucciones**, escribe primero esta línea:
   > Conversa normal conmigo. Solo cuando te escriba «dame mi reporte de criterio», sigue estas instrucciones:

   y debajo pega el texto completo de [`prompts/reporte.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/reporte.txt).
4. Guarda. Los chats que abras **dentro** de ese proyecto tendrán el reporte a mano.
5. Para el brief, crea otro proyecto, «criterio · brief», y pega [`prompts/brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt) sin la línea extra: ahí cada chat nuevo empieza con la entrevista.

⚠️ por confirmar en la prueba: que el proyecto del reporte solo responda con el reporte cuando lo pides. Si no, usa la vía de pegar el prompt al final del chat.

### Si tienes ChatGPT Business, Enterprise o Edu: skills

1. Consigue los `.zip` (ver [arriba](#conseguir-los-zip-de-las-skills)).
2. En la barra lateral, abre **Plugins › Skills**.
3. **Create › Upload from your computer** y sube `brief-4d.zip`. Repite con las demás.
4. ChatGPT revisa cada skill antes de activarla.

⚠️ por confirmar en la prueba: que ChatGPT acepte el `.zip` con esta estructura y que respete el `description` de cada skill. Tu organización puede tener las skills apagadas.

### Codex

Copia las carpetas de `skills/` a `~/.agents/skills/`. ⚠️ por confirmar en la prueba. Si tu herramienta no carga skills, el archivo `AGENTS.md` del repositorio le explica qué hacer.

---

## Gemini

**Qué dice la documentación oficial:**
- La app de Gemini **ya tiene skills** y acepta archivos `SKILL.md` ([Create & manage skills](https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop)):
  - Se suben en **Configuración › Skills › Upload**, como un `SKILL.md`, una carpeta o un `.zip` con el `SKILL.md` en su carpeta principal.
  - Solo se suben **desde gemini.google.com o la app de Mac**. Se usan también en la app del celular.
  - Requisitos: **18 años o más**, **cuenta personal de Google** (no de trabajo ni de colegio) y **la Actividad activada**.
  - Se llaman escribiendo `/` en el chat, o Gemini las usa solo cuando encajan con lo que pides.
  - Los scripts no pueden usar internet.
- Las **Gems** se reemplazan por skills: en cuentas personales, desde **noviembre de 2026** ([About the transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en)). Hoy todavía se pueden crear Gems en gemini.google.com ([Use Gems](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop)).
- La documentación **no dice si las skills están en el plan gratuito**. ⚠️ por confirmar en la prueba.
- **Gemini CLI** (para programadores) lee skills de `~/.gemini/skills/` y `.gemini/skills/` ([Agent Skills en Gemini CLI](https://geminicli.com/docs/cli/skills/)).

### Opción 1 · Skills en la app de Gemini

1. En el computador, entra a https://gemini.google.com.
2. Abre la barra lateral y ve a **Configuración › Skills**.
3. Arriba, haz clic en **Upload** y luego en **Open**.
4. Elige `brief-4d.zip`. Si no lo acepta, descomprímelo y elige la carpeta `brief-4d`.
5. Revisa lo que muestra y haz clic en **Create**.
6. Repite con `detector`, `coach` y `revision-de-historial`.

⚠️ por confirmar en la prueba: que Gemini acepte nuestros `.zip` (el `SKILL.md` está dentro de una carpeta con el nombre de la skill), que lea los archivos de `references/` y que respete la regla de activarse solo cuando lo pides.

### Opción 2 · Una Gem con instrucciones (hasta que desaparezcan las Gems)

1. En https://gemini.google.com, abre la barra lateral y entra a **Gems › Nueva Gem**.
2. Nombre: «criterio · reporte».
3. En **Instrucciones**, escribe la misma línea de ChatGPT («Conversa normal conmigo. Solo cuando te escriba "dame mi reporte de criterio", sigue estas instrucciones:») y debajo pega el texto completo de [`prompts/reporte.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/reporte.txt).
4. **Guardar**. La Gem aparece también en la app del celular.
5. Crea otra Gem, «criterio · brief», con [`prompts/brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt) tal cual.

⚠️ por confirmar en la prueba: igual que en ChatGPT, que la Gem del reporte espere a que se lo pidas.

### Gemini CLI

Copia las carpetas de `skills/` a `~/.gemini/skills/`. ⚠️ por confirmar en la prueba.

---

## Cualquier otra IA: solo los prompts

No se instala nada. Funciona en cualquier IA, en cualquier plan y en el celular.

1. Abre el prompt que necesites y cópialo **completo**:
   - Antes de pedir algo: [`brief.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/brief.txt)
   - Al terminar un chat: [`reporte.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/reporte.txt)
   - Para practicar: [`coach.txt`](https://raw.githubusercontent.com/gutiedward/pensamiento-critico-ia/main/prompts/coach.txt)
2. Guárdalos donde los encuentres rápido: en tus notas del celular o en un documento.
3. Cómo usarlos está en el [manual de uso](uso.md).

---

## Analizador de historial (Python, en tu computador)

Revisa tu historial exportado de ChatGPT, Claude o Gemini. **No usa internet:** solo la biblioteca estándar de Python, sin módulos de red, y hay una prueba automática que lo verifica. El reporte HTML tampoco carga nada de afuera.

**Necesitas:** un computador (no funciona en el celular) y Python 3.9 o superior.

1. Revisa si tienes Python. Abre la **Terminal** (Mac) o **PowerShell** (Windows) y escribe:
   ```bash
   python3 --version
   ```
   En Windows: `py --version`.
   - Si sale `Python 3.9` o un número mayor, listo.
   - Si tu Mac te ofrece instalar las herramientas de desarrollo, acepta.
   - Si no lo tienes, instálalo desde https://www.python.org/downloads/
2. Descarga el repositorio: en GitHub, **Code › Download ZIP**, y descomprímelo. O usa `git clone`.
3. No hay que instalar nada más. Cómo correrlo está en el [manual de uso](uso.md#analizador-de-historial-python-en-tu-computador).

---

## Siguiente paso

- [Manual de uso](uso.md): qué decirle a cada IA.
- [Manual de pruebas](pruebas.md): la lista de chequeo para confirmar que todo funciona.

*Contenido bajo CC BY 4.0.*
