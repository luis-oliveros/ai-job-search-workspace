# Advanced setup for developers

This document is optional. The standard end-user flow is documented in `START_HERE.md` and `EMPIEZA_AQUI.md` and does not require terminal commands.

## Why helper scripts exist

The repository includes Python utilities for deterministic document extraction, optional OCR, workspace initialization, validation, application-folder creation, and automated tests. They improve reproducibility and are useful for contributors or for agents that can execute local commands.

## Environment

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Deterministic ingestion

```bash
python scripts/ingest_profile.py
```

For scanned PDFs, install the optional OCR dependencies and Tesseract, then run:

```bash
pip install -r requirements-ocr.txt
python scripts/ingest_profile.py --ocr auto
```

## Validation and tests

```bash
pip install -r requirements-dev.txt
python scripts/validate_workspace.py
pytest -q
```

These commands are not part of the beginner workflow.
