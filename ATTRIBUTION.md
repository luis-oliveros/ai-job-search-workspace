# Attribution

This repository was inspired by the persistent job-search workspace/agent pattern from the project originally shared as:

- Original URL: https://github.com/ackyer/job-search-agent-template
- Current upstream repository: https://github.com/agent-data/job-search
- Current upstream license: MIT
- Current upstream copyright notice: Copyright (c) 2026 Aptiq Labs, Inc.

The implementation in this repository generalizes that idea for a no-code-first workflow in which a user can download a ZIP, add PDF/DOCX/TXT/Markdown profile sources, open the folder in a compatible AI agent, and begin from a single instruction.

Major additions include document-source ingestion, optional OCR support, evidence/provenance tracking, separation of verified facts from preferences, application-specific workspaces, privacy-by-default rules, multi-agent entry files, human approval before final submission, and developer-facing validation/tests that remain optional for ordinary users.

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the upstream MIT notice retained with this distribution.
