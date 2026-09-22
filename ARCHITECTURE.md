# Architecture

## Design goals

The workspace is designed around durable state, evidence provenance, client portability, privacy, and human-controlled submission.

The main user experience is agent-native and no-code. Helper scripts exist for reproducibility and development, but they are not prerequisites for a normal user.

## Primary no-code flow

```text
GitHub: Code > Download ZIP
          |
          v
unzip project
          |
          v
copy PDF/DOCX/TXT/MD into profile_sources/
          |
          v
open the whole folder in a local-file-capable AI agent
          |
          v
"Initialize my profile"
          |
          v
agent reads original documents
          |
          +--> SOURCE_INDEX / evidence ledger when possible
          +--> FACTS_VERIFIED.md
          +--> PROFILE_SUMMARY.md
          |
          v
search criteria + job analysis
          |
          v
applications/<application-id>/
          |
          v
human review and explicit approval
          |
          v
submission + tracking
```

## Optional deterministic extraction path

When an agent has local execution tools, it can use the included helper scripts itself:

```text
profile_sources/
      |
      | agent optionally runs scripts/ingest_profile.py
      v
profile/normalized_sources/
      |
      +--> profile/SOURCE_INDEX.json
      +--> profile/PROFILE_EVIDENCE.md
      |
      v
profile/FACTS_VERIFIED.md
```

This path is useful for reproducibility, OCR, automated testing, and contributor workflows. It is not required from the end user.

## Why keep a verified-facts layer

A document may be outdated, duplicated, ambiguous, or inconsistent with another source. `FACTS_VERIFIED.md` records which claims are safe to reuse. It is intentionally distinct from job-search preferences and from model-generated summaries.

## PDF and DOCX handling

The original document remains authoritative evidence and must never be overwritten. If the current AI client can inspect the PDF or DOCX directly, it should do so. If direct inspection is insufficient and local execution is available, the agent may use the deterministic extraction helper. OCR is a fallback for image-only PDFs and must be treated as lower-confidence evidence.

## Submission boundary

The architecture supports research, drafting, and form preparation, but it defines a hard control point before external submission. Final applications, declarations, consent, identity checks, and similar actions remain under human control.
