# Job Search Agent Workspace Template

A reusable workspace that turns a local-file-capable AI agent into a persistent job-search assistant. It can read career documents, build an evidence-backed profile, analyze vacancies, tailor application materials, and track applications without relying on one chat history.

**Built for non-technical users. You do not need Python, PowerShell, Git, or programming knowledge to get started.**

[README en español](README_ES.md) · [Start here](START_HERE.md)

## Start in 5 minutes

### 1. Download the ZIP

On GitHub click:

**Code → Download ZIP**

Unzip the folder anywhere on your computer. You do not need to clone the repository.

### 2. Install one desktop AI client

Choose one. For a graphical experience, **ChatGPT Desktop** or **Cursor** are recommended.

| AI / agent | Official link | Integration |
| --- | --- | --- |
| **ChatGPT Desktop + Work/Codex** | https://chatgpt.com/download/ | Opens a local folder; Codex reads `AGENTS.md` |
| **Cursor** | https://cursor.com/download | Opens the folder as a project; rules included under `.cursor/rules/` |
| **Claude** | https://claude.com/download | `CLAUDE.md` points to the central contract |
| **Gemini CLI** | https://github.com/google-gemini/gemini-cli | `GEMINI.md` points to the central contract; more technical |
| **Ollama** | https://ollama.com/download | Local-model option; requires a compatible file/tool agent client |

OpenAI's desktop documentation describes opening local folders in Work or Codex: https://help.openai.com/en/articles/20001275/

### 3. Add your resume and documents

Open:

```text
profile_sources/
```

and copy your files there, for example:

```text
profile_sources/
├── resume.pdf
├── academic_cv.docx
├── certificates.pdf
└── publications.md
```

The template accepts **PDF, DOCX, TXT, and Markdown**. You do not need to convert a PDF into Word first.

### 4. Open the whole folder in your AI client

In ChatGPT Desktop use **Work or Codex → open local folder**. In Cursor use **Open Folder**. Select the whole unzipped project folder, not just the resume.

### 5. Paste this prompt

```text
Read AGENTS.md and START_HERE.md. Initialize my profile from the documents in profile_sources. Handle any technical processing yourself. Do not invent information. Show me facts that require review before starting a job search.
```

That is enough to begin.

The AI agent should handle file reading, workspace initialization, evidence generation, and any optional extraction/OCR it can perform with its available local tools.

## After initialization

Review:

```text
profile/FACTS_VERIFIED.md
profile/PROFILE_SUMMARY.md
```

Then describe the jobs you want and ask the agent to save the criteria. Finally use:

```text
Start my job search.
```

Or provide a vacancy directly:

```text
Analyze this job: <URL>
```

## What it can do

Depending on the capabilities of the chosen AI client, the agent can read career evidence, identify essential job requirements, compare them against verified facts, maintain a job registry, prepare tailored resume versions, draft letters and form answers, and track active hiring processes.

The agent **must not submit a final application without explicit authorization for that specific job**.

## PDF and Word support

The project does not assume an editable Word resume exists. Original PDF, DOCX, TXT, and Markdown sources can all be used. Multiple documents and resume versions may coexist.

```text
PDF / DOCX / TXT / MD
        ↓
agent reads source evidence
        ↓
provenance + verified facts
        ↓
FACTS_VERIFIED.md
        ↓
job analysis and tailored materials
```

Image-only PDFs can use optional OCR when the agent environment supports it. Helper utilities are included, but **normal users are not expected to run them manually**.

## Inspiration and improvements

This project was inspired by [`agent-data/job-search`](https://github.com/agent-data/job-search) (originally shared at `ackyer/job-search-agent-template`). It carries forward the idea of a persistent filesystem workspace that an AI agent can read and update across sessions.

This implementation generalizes that pattern with a no-code end-user flow, PDF/DOCX/TXT/MD support, direct agent reading, optional OCR, source provenance, a verified-facts ledger distinct from preferences, privacy defaults, multi-agent adapters, isolated application folders, duplicate control, and an explicit human approval boundary before final submission.

See [ATTRIBUTION.md](ATTRIBUTION.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution and upstream license notices.

## Privacy

`profile_sources/` and core user-generated personal files are ignored by Git by default, reducing the risk of publishing resumes, contact information, references, or application history with the template.

Never store passwords, session cookies, API tokens, government IDs, or authentication secrets in the repository.

## Files normal users should know

```text
START_HERE.md             simple English guide
EMPIEZA_AQUI.md           simple Spanish guide
AGENTS.md                 central agent rules
profile_sources/          put your resume/documents here
profile/                  evidence-backed profile generated by the agent
search/                   criteria and jobs
applications/             per-job application materials
tracking/                 active processes
```

## Developers

Python helpers, OCR, tests, and GitHub Actions remain available as an advanced layer. They are not required for the standard user flow.

See [docs/ADVANCED_SETUP.md](docs/ADVANCED_SETUP.md).

## License

MIT. See [LICENSE](LICENSE).
