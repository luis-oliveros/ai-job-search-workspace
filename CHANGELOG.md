# Changelog

## 1.2.1 - 2026-09-22

- Updated upstream attribution to the current `agent-data/job-search` repository while preserving the original shared URL.
- Added `THIRD_PARTY_NOTICES.md` with the upstream MIT copyright and license notice.
- Prepared the package for safer public publication on GitHub.

## 1.2.0 - No-code onboarding

- Reworked the default experience around GitHub **Code > Download ZIP**.
- Removed Python, PowerShell, Git, and terminal commands from the normal-user setup path.
- Added `START_HERE.md`, `EMPIEZA_AQUI.md`, `FIRST_PROMPT.txt`, and `PRIMER_MENSAJE.txt`.
- Changed `AGENTS.md` so the agent handles document extraction/OCR itself when tools are available.
- Made direct PDF/DOCX reading the primary path and deterministic scripts an optional fallback.
- Added `docs/ADVANCED_SETUP.md` for developer-only Python/OCR/test instructions.
- Rewrote English and Spanish installation guides for non-technical users.

## 1.1.0 - 2026-09-22

- Added complete English and Spanish installation guides.
- Added official download/setup links for ChatGPT Desktop + Codex, Claude Desktop / Claude Code, Gemini CLI, Cursor and Ollama.
- Added agent compatibility adapters: `CLAUDE.md`, `GEMINI.md` and a persistent Cursor rule.
- Expanded README onboarding with a beginner route from a clean computer to first profile initialization.
- Added Python, Git and Tesseract setup references.
- Documented the distinction between a local model runtime and a file-operating AI agent.

## 1.0.0 - 2026-09-22

- Generalized the original workspace concept for public reuse.
- Added PDF, DOCX, TXT and Markdown profile ingestion.
- Added optional OCR for scanned PDF pages.
- Added source hashes, normalized evidence and provenance tracking.
- Added verified facts, job tracking, application workspaces, privacy defaults, tests and GitHub Actions.
