---
name: revision-de-historial
description: Analiza la exportación del historial de ChatGPT, Claude o Gemini con un script local y genera un reporte de criterio en HTML. Úsala solo cuando la persona pida revisar su historial, sus exportaciones o "cómo he usado la IA" en muchas conversaciones.
---

# Revisión de historial

1. Pide la ruta de la exportación: el `.zip`, `conversations.json` (ChatGPT o Claude) o `MyActivity.json` de Gemini (Google Takeout; soporte experimental).
2. Corre el script. No envía nada a internet:
   `python3 scripts/analizar.py --entrada <ruta> --salida criterio-salida`
   Filtros opcionales: `--desde AAAA-MM-DD`, `--hasta AAAA-MM-DD`, `--buscar <palabra>`, `--min-turnos N`.
3. Ese primer reporte es solo un **pre-marcado**: lo que marca suele ser cierto, pero ve poco. No saques conclusiones sobre la persona con él.
4. Para el reporte completo, **avisa primero** que en este paso el texto de sus chats pasa por el modelo de esta sesión, y pide permiso. Con su permiso:
   - Lee `references/rubrica.md`.
   - Clasifica cada archivo de `criterio-salida/lotes/` siguiendo las instrucciones que trae arriba.
   - Guarda cada respuesta como `criterio-salida/lotes/clasificacion_NNN.json`.
5. Regenera el reporte con la clasificación:
   `python3 scripts/analizar.py --entrada <ruta> --salida criterio-salida --clasificacion criterio-salida/lotes/clasificacion_*.json`
6. Dile que abra `criterio-salida/reporte.html` y que revise las citas en «Verifica tú mismo».
7. No copies fragmentos de sus conversaciones a ningún otro lugar.
