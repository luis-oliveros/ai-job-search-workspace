# Clientes de IA compatibles

El template se diseñó para agentes capaces de leer y modificar archivos locales. Las funciones exactas dependen del producto, plan y permisos del usuario.

| Cliente | Tipo | Descarga / instalación | Integración incluida |
| --- | --- | --- | --- |
| ChatGPT Desktop + Codex | Escritorio / agente | https://chatgpt.com/download/ | `AGENTS.md` nativo |
| Claude Desktop / Claude Code | Escritorio / CLI | https://claude.com/download | `CLAUDE.md` -> `AGENTS.md` |
| Gemini CLI | CLI | https://github.com/google-gemini/gemini-cli | `GEMINI.md` -> `AGENTS.md` |
| Cursor | Editor / agente | https://cursor.com/download | `.cursor/rules/` -> `AGENTS.md` |
| Ollama | Runtime local de modelos | https://ollama.com/download | Requiere agente compatible para automatización completa |

## Qué cliente elegir

**Usuario que quiere la ruta más simple:** ChatGPT Desktop + Codex o Cursor.

**Usuario cómodo con terminal:** Codex CLI, Claude Code o Gemini CLI.

**Usuario que prioriza modelos locales:** Ollama combinado con un agente/editor que pueda consumir modelos de Ollama.

## Importante

Instalar un chatbot no garantiza que pueda modificar archivos locales o ejecutar los scripts del repositorio. Para este proyecto conviene utilizar la modalidad de agente o editor que tenga acceso explícito a la carpeta del workspace.
