# Job Search Agent Workspace Template

Un workspace reutilizable para convertir una IA con acceso a archivos locales en un asistente de búsqueda laboral persistente: lee tu CV y documentos profesionales, construye un perfil verificable, analiza vacantes, adapta materiales y mantiene seguimiento sin depender del historial de un único chat.

**Diseñado para usuarios no técnicos. No necesitas saber Python, PowerShell, Git ni programación para comenzar.**

[English README](README.md) · [Empieza aquí](EMPIEZA_AQUI.md)

## Inicio en 5 minutos

### 1. Descarga el ZIP

En esta página de GitHub pulsa:

**Code → Download ZIP**

Descomprime la carpeta en tu computador. No necesitas clonar el repositorio.

### 2. Instala una IA de escritorio

Elige una sola. Para una experiencia gráfica recomendamos **ChatGPT Desktop** o **Cursor**.

| IA / agente | Enlace oficial | Cómo se integra |
| --- | --- | --- |
| **ChatGPT Desktop + Work/Codex** | https://chatgpt.com/download/ | Abre la carpeta local; Codex lee `AGENTS.md` |
| **Cursor** | https://cursor.com/download | Abre la carpeta como proyecto; reglas incluidas en `.cursor/rules/` |
| **Claude** | https://claude.com/download | `CLAUDE.md` redirige al contrato central |
| **Gemini CLI** | https://github.com/google-gemini/gemini-cli | `GEMINI.md` redirige al contrato central; pensado para usuarios más técnicos |
| **Ollama** | https://ollama.com/download | Opción local; requiere un cliente/agente que pueda trabajar con carpetas y herramientas |

ChatGPT Desktop permite abrir carpetas locales desde Work o Codex. Documentación oficial: https://help.openai.com/es-419/articles/20001275

### 3. Copia tu CV y documentos

Abre:

```text
profile_sources/
```

y coloca allí tus archivos. Por ejemplo:

```text
profile_sources/
├── CV.pdf
├── CV_academico.docx
├── certificados.pdf
└── publicaciones.md
```

El template admite **PDF, DOCX, TXT y Markdown**. No necesitas convertir un PDF a Word para que el proyecto funcione.

### 4. Abre la carpeta completa en la IA

En ChatGPT Desktop usa **Work o Codex → abrir carpeta local**. En Cursor usa **Open Folder**. Selecciona la carpeta completa que descomprimiste, no solamente el CV.

### 5. Escribe este prompt

```text
Lee AGENTS.md y EMPIEZA_AQUI.md. Inicializa mi perfil usando los documentos de profile_sources. Haz tú todo el procesamiento técnico necesario. No inventes información. Muéstrame los hechos que requieren revisión antes de comenzar a buscar empleos.
```

Eso es todo para comenzar.

La IA debe ocuparse de leer archivos, generar el perfil, crear los documentos internos y, si dispone de herramientas locales y necesita extracción adicional u OCR, ejecutar esos procesos ella misma.

## Después del primer inicio

Revisa lo que el agente coloque en:

```text
profile/FACTS_VERIFIED.md
profile/PROFILE_SUMMARY.md
```

Luego dile qué empleos te interesan. Por ejemplo:

```text
Quiero buscar posiciones de Data Science y Machine Learning en Chile y remoto. No quiero cargos junior. Pregúntame solo por las preferencias imprescindibles que falten y guarda mis criterios.
```

Finalmente:

```text
Inicia mi búsqueda laboral.
```

También puedes entregarle directamente una vacante:

```text
Analiza esta oferta: <URL>
```

## Qué puede hacer

Según las herramientas disponibles en el cliente de IA, el agente puede leer tu información profesional, identificar requisitos esenciales de una vacante, contrastarlos contra evidencia verificable, mantener un registro de ofertas, preparar versiones adaptadas del CV, redactar cartas y respuestas de formulario, y conservar el estado de procesos de selección.

El agente **no debe enviar una postulación final sin autorización explícita del usuario para esa vacante concreta**.

## PDF y Word

El proyecto no presupone que exista un Word editable.

Si entregas un `CV.pdf`, el agente debe leer el PDF original cuando su entorno lo permita. Si entregas un `.docx`, también puede utilizarlo como fuente. Puedes añadir varios documentos y versiones.

El flujo de evidencia es:

```text
PDF / DOCX / TXT / MD
        ↓
lectura por el agente
        ↓
procedencia + hechos verificables
        ↓
FACTS_VERIFIED.md
        ↓
análisis de vacantes y materiales adaptados
```

Si un PDF contiene solamente imágenes, el agente puede usar OCR cuando su entorno lo permita. El repositorio incluye herramientas auxiliares para ello, pero **el usuario normal no necesita ejecutarlas manualmente**.

## Qué se mejoró respecto de la idea original

Este proyecto fue inspirado por [`agent-data/job-search`](https://github.com/agent-data/job-search) (originally shared at `ackyer/job-search-agent-template`), del cual se conserva la idea de un workspace persistente que una IA puede leer y actualizar entre sesiones.

Esta implementación amplía ese patrón con una experiencia no-code para el usuario final, soporte para PDF/DOCX/TXT/MD, lectura directa de documentos por el agente, OCR opcional, trazabilidad de fuentes, un registro de hechos verificados separado de preferencias, privacidad por defecto, compatibilidad con varios agentes, estructura independiente por postulación, control de duplicados y un límite explícito de aprobación humana antes del envío final.

Consulta [ATTRIBUTION.md](ATTRIBUTION.md) y [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) para la atribución y los avisos de licencia del proyecto de origen.

## Privacidad

`profile_sources/` y los principales archivos generados con información personal están ignorados por Git de forma predeterminada. Esto reduce el riesgo de publicar accidentalmente el CV, correo, teléfono, referencias u otros datos privados cuando se usa este proyecto como template.

Nunca guardes contraseñas, cookies, tokens, documentos de identidad ni credenciales dentro del repositorio.

## Archivos que debe conocer el usuario

```text
EMPIEZA_AQUI.md           guía sencilla en español
START_HERE.md             guía sencilla en inglés
AGENTS.md                 reglas centrales del agente
profile_sources/          aquí colocas tu CV y documentos
profile/                  perfil y evidencia que construye la IA
search/                   criterios y vacantes
applications/             materiales por postulación
tracking/                 procesos activos
```

## Para desarrolladores

Los scripts Python, OCR, pruebas y GitHub Actions siguen disponibles, pero forman parte del nivel avanzado. No son requisitos del flujo normal.

Consulta [docs/ADVANCED_SETUP.md](docs/ADVANCED_SETUP.md).

## Licencia

MIT. Consulta [LICENSE](LICENSE).
