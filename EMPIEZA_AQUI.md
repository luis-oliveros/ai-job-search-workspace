# Empieza aquí

Este proyecto está diseñado para poder usarse **sin saber Python, PowerShell ni programación**.

## La forma más simple

### 1. Descarga el proyecto

En GitHub:

1. Pulsa el botón verde **Code**.
2. Elige **Download ZIP**.
3. Descomprime el ZIP en una carpeta de tu computador.

No necesitas clonar el repositorio ni usar Git.

### 2. Instala una IA que pueda trabajar con carpetas locales

Elige una sola opción:

- **ChatGPT Desktop**: https://chatgpt.com/download/
- **Cursor**: https://cursor.com/download
- **Claude**: https://claude.com/download

También puedes usar otros agentes compatibles con archivos locales. Este template incluye instrucciones específicas para Codex (`AGENTS.md`), Claude (`CLAUDE.md`), Gemini (`GEMINI.md`) y Cursor (`.cursor/rules/`).

### 3. Copia tus documentos

Abre la carpeta:

```text
profile_sources/
```

Copia allí los documentos que quieras usar como evidencia profesional. Por ejemplo:

```text
profile_sources/
├── CV.pdf
├── CV_academico.docx
├── certificados.pdf
└── publicaciones.md
```

Puedes usar `.pdf`, `.docx`, `.txt` y `.md`.

No conviertas el PDF a Word solo para usar este proyecto. Si la IA puede leer el PDF directamente, debe hacerlo. Si necesita extracción adicional y tiene herramientas locales, el propio agente debe encargarse.

### 4. Abre la carpeta completa con tu IA

#### ChatGPT Desktop

1. Abre ChatGPT Desktop.
2. Selecciona **Work** o **Codex**.
3. Elige la opción para abrir una carpeta local.
4. Selecciona la carpeta completa que acabas de descomprimir.
5. Concede acceso a los archivos cuando la aplicación lo solicite.

#### Cursor

1. Abre Cursor.
2. Elige **Open Folder**.
3. Selecciona la carpeta completa del proyecto.
4. Abre el agente/chat de Cursor.

#### Claude

Abre el proyecto con la modalidad de Claude que permita trabajar con archivos locales y selecciona la carpeta completa. El archivo `CLAUDE.md` indica al agente que use `AGENTS.md` como contrato central.

### 5. Escribe solamente esto

```text
Lee AGENTS.md y EMPIEZA_AQUI.md. Inicializa mi perfil usando los documentos de profile_sources. Haz tú todo el procesamiento técnico necesario. No inventes información. Muéstrame los hechos que requieren revisión antes de comenzar a buscar empleos.
```

A partir de este punto, **la IA debe encargarse del trabajo técnico**. El usuario no debería tener que abrir una terminal ni ejecutar scripts.

### 6. Revisa el perfil

El agente construirá o actualizará archivos como:

```text
profile/FACTS_VERIFIED.md
profile/PROFILE_SUMMARY.md
```

Revisa especialmente los elementos marcados como `NEEDS_REVIEW`, `CONFLICT` o `UNVERIFIED`.

### 7. Define qué trabajo buscas

Puedes escribir, por ejemplo:

```text
Quiero buscar cargos de Data Science y Machine Learning en Chile y remoto. No quiero cargos junior. Antes de guardar estos criterios, pregúntame solo por la información imprescindible que falte.
```

El agente guardará los criterios en el workspace para reutilizarlos.

### 8. Empieza la búsqueda

Cuando el perfil esté revisado, escribe:

```text
Inicia mi búsqueda laboral.
```

También puedes pegar una oferta directamente:

```text
Analiza esta oferta: <URL>
```

### 9. Preparar una postulación

Cuando quieras avanzar con una vacante:

```text
Prepara la postulación para esta oferta. Adapta mi CV utilizando únicamente hechos verificados y muéstrame todo antes de cualquier envío.
```

El agente puede generar CV, carta y respuestas para formularios según las herramientas disponibles. Nunca debe enviar una postulación definitiva sin autorización explícita.

## ¿Y los scripts de Python?

Son **herramientas opcionales para desarrolladores y agentes**. Existen para hacer la extracción reproducible, ejecutar OCR, validar el workspace y probar el proyecto.

Un usuario normal no necesita ejecutarlos. Si el agente dispone de terminal y necesita uno de esos scripts, debe ejecutarlo por su cuenta.

Consulta `docs/ADVANCED_SETUP.md` solo si quieres desarrollar, automatizar o modificar el template.
