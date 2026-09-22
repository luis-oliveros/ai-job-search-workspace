# Start here

This project is designed to work **without requiring Python, PowerShell, Git, or programming knowledge from the end user**.

## The simplest workflow

### 1. Download the project

On GitHub:

1. Click the green **Code** button.
2. Choose **Download ZIP**.
3. Unzip it anywhere on your computer.

You do not need to clone the repository.

### 2. Install one AI desktop client that can work with local folders

Choose one:

- **ChatGPT Desktop**: https://chatgpt.com/download/
- **Cursor**: https://cursor.com/download
- **Claude**: https://claude.com/download

Other local-file-capable agents may also work. The template includes agent instructions for Codex (`AGENTS.md`), Claude (`CLAUDE.md`), Gemini (`GEMINI.md`), and Cursor (`.cursor/rules/`).

### 3. Add your documents

Open:

```text
profile_sources/
```

Copy your professional source documents into it, for example:

```text
profile_sources/
├── resume.pdf
├── academic_cv.docx
├── certificates.pdf
└── publications.md
```

Supported source types are `.pdf`, `.docx`, `.txt`, and `.md`.

Do not convert a PDF to Word just to use this project. The agent should inspect the original PDF when its client supports it. If extra extraction is needed and local tools are available, the agent should handle that technical step itself.

### 4. Open the whole project folder in your AI client

With ChatGPT Desktop, open **Work** or **Codex**, choose a local folder, and select the unzipped project folder. With Cursor, use **Open Folder**. Use the equivalent local-project workflow in other supported agents.

### 5. Paste this prompt

```text
Read AGENTS.md and START_HERE.md. Initialize my profile from the documents in profile_sources. Handle any technical processing yourself. Do not invent information. Show me facts that require review before starting a job search.
```

From this point on, the **agent should handle the technical workflow**. A normal user should not need to open a terminal or run scripts.

### 6. Review your profile

The agent will build or update files such as:

```text
profile/FACTS_VERIFIED.md
profile/PROFILE_SUMMARY.md
```

Review anything marked `NEEDS_REVIEW`, `CONFLICT`, or `UNVERIFIED`.

### 7. Tell the agent what kind of job you want

Example:

```text
I want Data Science and Machine Learning roles in my country and remote. Do not include junior roles. Ask me only for essential missing preferences before saving the criteria.
```

### 8. Start

```text
Start my job search.
```

Or analyze a specific vacancy:

```text
Analyze this job: <URL>
```

### 9. Prepare an application

```text
Prepare an application for this job. Tailor my resume using verified facts only and show me everything before any submission.
```

The agent must not submit a final application without explicit authorization.

## What are the Python scripts for?

They are **optional developer and agent tools** for reproducible extraction, OCR, validation, and testing. A normal user does not need to run them. If an agent has terminal access and needs a helper script, it should run it itself.

See `docs/ADVANCED_SETUP.md` only if you want to develop, automate, or modify the template.
