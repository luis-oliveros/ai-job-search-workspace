# AGENTS.md

## Purpose

This workspace supports a user's job search while preserving factual accuracy, provenance, privacy, and human control. Treat files as persistent state. Never rely on chat memory when the workspace contains a more authoritative source.

## 1. Source hierarchy

Use evidence in this order:

1. `profile/FACTS_VERIFIED.md` for claims already reviewed and approved.
2. `profile/normalized_sources/*.md` for extracted text from source documents.
3. Original documents in `profile_sources/` when the current agent can inspect them directly.
4. `profile/PROFILE_SUMMARY.md` as a convenience summary only.
5. `search/SEARCH_CRITERIA.md` only for preferences and constraints, never as evidence of experience.

If sources conflict, do not silently reconcile them. Record the conflict and ask the user to resolve it before using that fact in an application.

## 2. Document ingestion

The workspace accepts `.pdf`, `.docx`, `.txt`, and `.md` profile sources. The default user experience is **no-code**: never require the user to run Python, PowerShell, Git, or terminal commands just to initialize the workspace.

Use this order:

1. Inspect files in `profile_sources/` directly with the file-reading capabilities available in the current client.
2. When the client can reliably read the original PDF/DOCX/TXT/MD, use the original document as evidence and create or update the provenance files yourself.
3. If deterministic extraction is useful and the environment gives you terminal/tool access, run the helper script yourself: `python scripts/ingest_profile.py`. Do not hand this command to a normal user as a prerequisite.
4. If a PDF appears scanned and OCR tools are available, you may run `python scripts/ingest_profile.py --ocr auto` yourself.
5. If a file cannot be read with the available tools, identify that specific limitation and ask the user only for an accessible copy of that file. Do not pretend it was parsed.

Whenever possible, maintain `profile/SOURCE_INDEX.json` and `profile/PROFILE_EVIDENCE.md`. Every factual claim prepared for `FACTS_VERIFIED.md` should identify the supporting source and location such as PDF page, DOCX section/paragraph, table, or text-file section.

Treat OCR-derived text as lower-confidence evidence until reviewed by a human.

## 3. No fabrication

Never invent or infer as fact:

- jobs, employers, responsibilities, dates, seniority, or achievements;
- technologies, certifications, licenses, degrees, or skill levels;
- quantitative results, budgets, revenue, team size, or years of experience;
- language proficiency;
- compensation history or salary expectations;
- work authorization, immigration status, relocation availability, or identity data;
- publications, awards, grants, references, or contact details.

You may rewrite a verified fact to match the terminology of a vacancy only when the meaning remains unchanged.

## 4. Verified facts ledger

`profile/FACTS_VERIFIED.md` is the operational evidence ledger.

For each fact include:

- the factual statement;
- source file;
- source location;
- status: `VERIFIED`, `CONFLICT`, or `NEEDS_REVIEW`;
- optional notes.

Only `VERIFIED` facts may be asserted without qualification in application materials.

## 5. Search criteria

Read `search/SEARCH_CRITERIA.md` at the beginning of each search session.

A hard constraint can exclude a job. A preference affects prioritization but does not automatically exclude it. `UNCONFIRMED` values cannot become hard constraints and cannot be presented as facts about the user.

## 6. Job capture

For every evaluated job capture, when available:

- stable job ID;
- role;
- organization;
- location and work mode;
- source URL;
- publication date;
- review date;
- essential requirements;
- preferred requirements;
- source platform;
- current status.

Avoid duplicates. Compare organization, role, location, external requisition ID when available, canonical URL, and materially identical descriptions.

## 7. Match analysis

Analyze each essential requirement separately against verified evidence.

Use evidence states:

- `SUPPORTED`: a verified fact directly supports the requirement;
- `PARTIAL`: evidence is relevant but incomplete;
- `UNVERIFIED`: the workspace does not prove the claim;
- `CONFLICT`: sources disagree;
- `NOT_APPLICABLE`: requirement does not apply.

A numeric compatibility score may be used only as a secondary summary. Never hide a disqualifying or uncertain requirement behind an aggregate score.

Operational job states:

- `PRIORITIZE`: hard constraints are met and essential requirements are substantially supported;
- `REVIEW`: plausible fit with a meaningful uncertainty or gap;
- `DISCARD`: a hard constraint or clearly mandatory requirement is not met.

## 8. CV and resume tailoring

Do not assume a DOCX source exists. Source documents can be PDF, DOCX, TXT, or MD.

When the user has provided an editable master DOCX, preserve it and work on a copy. When only a PDF exists, use its extracted evidence to draft a new editable application document if the user asks for one. Never overwrite source files.

Tailoring may reorder, shorten, and emphasize verified content. Do not add keywords when doing so would create an unsupported claim.

Store generated materials inside the corresponding application folder.

## 9. Cover letters and form answers

Use the vacancy and verified facts. When a question requires unavailable data, write `REQUIRES USER INPUT` instead of guessing.

Keep sensitive information out of reusable templates unless the specific application requires it.

## 10. Human approval boundary

Never submit a final application without explicit user authorization for that specific job.

Before submission, surface the organization, role, destination URL, documents selected, draft form answers, sensitive fields, unresolved uncertainties, and any declarations the user must review.

CAPTCHAs, identity verification, signatures, legal declarations, and consent checkboxes remain user-controlled.

## 11. Tracking

After an application is explicitly confirmed as submitted, update `applications/APPLICATIONS.csv` and `tracking/ACTIVE_PROCESSES.md` as appropriate.

Do not mark a process closed without evidence or a direct instruction from the user.

## 12. Privacy

Never store passwords, session cookies, API tokens, government identification numbers, secret answers, or authentication material in this repository.

Respect `.gitignore`. Do not move ignored personal files into tracked locations merely to make them easier to access.

## 13. Default language

Use the user's chosen language. Match the language of application documents to the vacancy when appropriate.

## 14. Operational commands

### `Initialize my profile`

1. Inspect `profile_sources/`.
2. Read the source documents directly when possible.
3. If technical extraction or OCR is needed and you have local execution tools, perform it yourself using the helper utilities.
4. Build or update `profile/SOURCE_INDEX.json` and `profile/PROFILE_EVIDENCE.md` when possible.
5. Build or update `profile/FACTS_VERIFIED.md` with provenance.
6. Build or update `profile/PROFILE_SUMMARY.md` using verified facts only.
7. Report conflicts and missing fields.
8. Do not ask a normal user to open a terminal unless there is no other viable path in the current client.

### `Start my job search`

1. Read verified facts and search criteria.
2. Read `search/JOBS.csv` to avoid duplicates.
3. Search only with tools actually available in the current environment.
4. Record evaluated opportunities.
5. Present `PRIORITIZE` before `REVIEW`.
6. Do not prepare application documents unless asked.

### `Analyze this job: <URL or text>`

1. Obtain the complete description when possible.
2. Create or update a job record using `templates/JOB_RECORD.md`.
3. Map every essential requirement against verified evidence.
4. Record gaps and uncertainties.
5. Identify which verified content is most relevant to emphasize.

### `Prepare application for <job>`

1. Confirm a job record exists.
2. Create an application folder yourself. You may use `scripts/new_application.py` when local execution is available, but the user should not need to run it manually.
3. Prepare requested editable documents without overwriting sources.
4. Draft form answers.
5. Run `templates/SUBMISSION_CHECKLIST.md`.
6. Stop before final submission.
