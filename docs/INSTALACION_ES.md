# Instalación y uso paso a paso

Esta guía está pensada para una persona que quiere usar el template en su computador, incluso si no trabaja habitualmente con Python o Git.

## 1. Qué necesitas

Hay dos componentes distintos:

1. **El workspace**, que es este repositorio y guarda documentos, evidencia, criterios, ofertas y postulaciones.
2. **Un agente de IA**, que abre la carpeta, lee sus instrucciones y trabaja con los archivos.

También necesitas Python para ejecutar los scripts de ingestión de PDF/DOCX y mantenimiento del workspace.

## 2. Instalar Python

Descarga Python desde el sitio oficial:

- https://www.python.org/downloads/

Se recomienda Python 3.11 o posterior.

En Windows, durante la instalación activa la opción que agrega Python al `PATH` si el instalador la ofrece.

Comprueba la instalación desde PowerShell, Terminal o CMD:

```bash
python --version
```

En algunos equipos Windows el comando puede ser:

```powershell
py --version
```

## 3. Elegir e instalar un agente de IA

No necesitas instalar todos. Elige uno.

### Opción A. ChatGPT Desktop + Codex

Es la ruta recomendada si ya utilizas ChatGPT y quieres una interfaz gráfica.

Descarga oficial:

- ChatGPT Desktop: https://chatgpt.com/download/
- Documentación de Codex CLI: https://developers.openai.com/codex/cli

La aplicación actual de ChatGPT integra Chat, Work y Codex en macOS y Windows. Codex puede trabajar con carpetas locales, repositorios y terminal.

**Uso con este template:** abre la carpeta del repositorio en Codex. Codex reconoce `AGENTS.md` como archivo de instrucciones del proyecto.

### Opción B. Claude Desktop / Claude Code

Descarga oficial:

- Claude Desktop: https://claude.com/download
- Instalación de Claude Code: https://code.claude.com/docs/en/setup

En Windows también puede instalarse Claude Code desde PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Después se inicia desde la carpeta del proyecto con:

```bash
claude
```

Este repositorio incluye `CLAUDE.md`, que dirige a Claude hacia `AGENTS.md`.

### Opción C. Gemini CLI

Documentación e instalación oficial:

- https://github.com/google-gemini/gemini-cli

Requiere Node.js 20 o posterior. Node.js puede descargarse desde:

- https://nodejs.org/

Instalación:

```bash
npm install -g @google/gemini-cli
```

Inicio:

```bash
gemini
```

Este repositorio incluye `GEMINI.md`, que dirige a Gemini hacia `AGENTS.md`.

### Opción D. Cursor

Descarga oficial:

- https://cursor.com/download

Cursor ofrece una interfaz gráfica tipo editor con agente integrado. Abre el directorio del repositorio mediante **File > Open Folder**.

El template incluye una regla persistente en `.cursor/rules/` para que Cursor utilice `AGENTS.md` como contrato principal.

### Opción E. Modelos locales con Ollama

Descarga oficial:

- https://ollama.com/download

Ollama ejecuta modelos localmente. Puede integrarse con distintos agentes y editores. Ollama por sí solo actúa principalmente como runtime de modelos, por lo que para automatizar archivos y comandos conviene combinarlo con un agente compatible.

En Windows puede instalarse también desde PowerShell con el comando oficial publicado por Ollama:

```powershell
irm https://ollama.com/install.ps1 | iex
```

Esta opción es útil cuando se prioriza procesamiento local, aunque la calidad y velocidad dependen del modelo y del hardware disponibles.

## 4. Descargar el template

### Forma sencilla: ZIP

En GitHub selecciona:

```text
Code > Download ZIP
```

Descomprime la carpeta donde quieras trabajar.

Ejemplo en Windows:

```text
D:\JobSearchAgent\
```

### Forma recomendada si usas Git

Instala Git desde:

- https://git-scm.com/downloads

Luego:

```bash
git clone <URL-DEL-REPOSITORIO>
cd job-search-agent-workspace-template
```

## 5. Preparar el entorno Python

Desde la carpeta raíz del proyecto:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Después inicializa los archivos locales del usuario:

```bash
python scripts/init_workspace.py
```

## 6. Agregar tu CV y documentos profesionales

Copia tus documentos dentro de:

```text
profile_sources/
```

Ejemplo:

```text
profile_sources/
├── cv.pdf
├── cv_academico.docx
├── certificaciones.pdf
└── publicaciones.md
```

Formatos admitidos:

- `.pdf`
- `.docx`
- `.txt`
- `.md`

Puedes usar más de un documento. El sistema conserva la procedencia de cada fuente y calcula su SHA-256.

## 7. Leer PDF, Word y otras fuentes

Ejecuta:

```bash
python scripts/ingest_profile.py
```

El script crea versiones normalizadas dentro de:

```text
profile/normalized_sources/
```

Además genera:

```text
profile/SOURCE_INDEX.json
profile/PROFILE_EVIDENCE.md
```

El índice permite saber qué archivo se procesó, cómo se extrajo, qué hash tenía y qué archivo normalizado corresponde a la fuente.

## 8. PDF escaneado y OCR

El OCR es opcional. Para activarlo instala las dependencias Python:

```bash
pip install -r requirements-ocr.txt
```

También necesitas Tesseract instalado en el sistema:

- Documentación oficial: https://tesseract-ocr.github.io/tessdoc/Installation.html

Después:

```bash
python scripts/ingest_profile.py --ocr auto
```

`auto` intenta extracción normal primero y aplica OCR cuando una página tiene muy poco texto utilizable.

## 9. Abrir el proyecto en la IA

La idea central es abrir **la carpeta completa**, no subir solamente el CV a un chat aislado.

### ChatGPT / Codex

1. Abre ChatGPT Desktop.
2. Entra a Codex.
3. Abre la carpeta del repositorio.
4. Inicia una tarea con:

```text
Initialize my profile.
```

O:

```text
Inicializa mi perfil.
```

Codex leerá `AGENTS.md` como instrucciones del repositorio.

### Claude

Abre una terminal dentro de la carpeta y ejecuta:

```bash
claude
```

Luego:

```text
Initialize my profile.
```

`CLAUDE.md` indica a Claude que debe leer `AGENTS.md`.

### Gemini CLI

Desde la carpeta:

```bash
gemini
```

Luego:

```text
Initialize my profile.
```

`GEMINI.md` dirige el agente hacia las reglas centrales.

### Cursor

1. Abre Cursor.
2. Selecciona **File > Open Folder**.
3. Selecciona este repositorio.
4. Abre Agent.
5. Escribe `Initialize my profile.`

## 10. Qué hace `Initialize my profile`

El agente debe revisar los documentos ya extraídos, construir `profile/FACTS_VERIFIED.md`, registrar procedencia y señalar contradicciones o datos que requieren revisión.

El objetivo es que las postulaciones posteriores utilicen evidencia verificable y no dependan de recuerdos imprecisos de conversaciones anteriores.

## 11. Configurar qué trabajo buscas

Edita:

```text
search/SEARCH_CRITERIA.md
```

Aquí se registran ubicaciones, modalidades de trabajo, áreas profesionales, restricciones y preferencias.

Una preferencia no debe convertirse en experiencia profesional. Por ejemplo, indicar interés en AWS no autoriza al agente a afirmar que el usuario domina AWS.

## 12. Flujo diario de uso

Puedes trabajar con instrucciones naturales como:

```text
Start my job search.
```

```text
Analyze this job: <URL>
```

```text
Prepare application for job <ID>.
```

```text
Show me the active application processes.
```

Cada oferta se compara requisito por requisito con `FACTS_VERIFIED.md`.

## 13. Qué puede automatizar

Dependiendo del agente utilizado y de sus permisos, puede:

- investigar ofertas públicas;
- leer descripciones de vacantes;
- registrar y deduplicar oportunidades;
- comparar requisitos con evidencia profesional;
- preparar CVs editables a partir de hechos verificados;
- redactar cartas y respuestas de formularios;
- mantener un historial local del proceso;
- trabajar con navegador o conectores cuando el agente los soporte.

La capacidad concreta depende del cliente de IA. El template no simula herramientas que el agente no tenga disponibles.

## 14. Límite antes de enviar una postulación

El agente debe detenerse antes del envío final y mostrar qué información, documentos y respuestas se utilizarán. La autorización corresponde a esa postulación concreta.

CAPTCHA, firma, identidad, declaraciones legales y consentimientos deben permanecer bajo control humano.

## 15. Validar que todo esté correcto

Ejecuta:

```bash
python scripts/validate_workspace.py
```

Para ejecutar también las pruebas del repositorio:

```bash
pip install -r requirements-dev.txt
pytest -q
```

## 16. Mantener tus datos privados

`profile_sources/`, hechos verificados, documentos normalizados y postulaciones generadas están ignorados por Git de forma predeterminada.

Antes de cualquier `git push`, revisa siempre:

```bash
git status
```

El repositorio público debe contener el motor y los templates. Tus CVs y procesos laborales deberían permanecer locales salvo que conscientemente uses un repositorio privado y decidas versionarlos.

## 17. Ruta recomendada para alguien que empieza desde cero

Si quieres la configuración más simple:

1. Instala Python.
2. Instala ChatGPT Desktop o Cursor.
3. Descarga este repositorio como ZIP.
4. Abre una terminal en la carpeta y prepara el entorno Python.
5. Ejecuta `python scripts/init_workspace.py`.
6. Copia el CV PDF o DOCX a `profile_sources/`.
7. Ejecuta `python scripts/ingest_profile.py`.
8. Abre la carpeta completa en el agente.
9. Escribe `Initialize my profile.`.
10. Revisa `FACTS_VERIFIED.md` antes de iniciar la búsqueda.

Con eso el sistema queda operativo.
