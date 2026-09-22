#!/usr/bin/env python3
"""Validate repository structure and local evidence consistency."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

REQUIRED_TRACKED = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursor/rules/job-search-agent.mdc",
    "README.md",
    "README_ES.md",
    "ATTRIBUTION.md",
    "ARCHITECTURE.md",
    "docs/INSTALLATION.md",
    "docs/INSTALACION_ES.md",
    "docs/AI_CLIENTS.md",
    "docs/CLIENTES_IA_ES.md",
    "requirements.txt",
    "scripts/init_workspace.py",
    "scripts/ingest_profile.py",
    "scripts/new_application.py",
    "templates/JOB_RECORD.md",
    "templates/MATCH_ANALYSIS.md",
    "templates/SUBMISSION_CHECKLIST.md",
    "search/SEARCH_CRITERIA.example.md",
    "profile/FACTS_VERIFIED.example.md",
]
SUPPORTED = {".pdf", ".docx", ".txt", ".md"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_TRACKED:
        if not (root / rel).exists():
            errors.append(f"Missing required file: {rel}")

    source_dir = root / "profile_sources"
    for path in source_dir.iterdir() if source_dir.exists() else []:
        if path.is_file() and path.name not in {".gitkeep", "README.md"} and path.suffix.lower() not in SUPPORTED:
            warnings.append(f"Unsupported profile source ignored by ingestion: {path.name}")

    index_path = root / "profile" / "SOURCE_INDEX.json"
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            for item in index.get("sources", []):
                source = source_dir / item["source_file"]
                if not source.exists():
                    warnings.append(f"Indexed source no longer exists: {item['source_file']}")
                    continue
                actual = sha256_file(source)
                if actual != item.get("sha256"):
                    warnings.append(f"Source changed since ingestion: {item['source_file']}")
        except Exception as exc:
            errors.append(f"Could not parse profile/SOURCE_INDEX.json: {exc}")

    print("Workspace validation")
    print(f"Errors: {len(errors)}")
    for message in errors:
        print(f"  ERROR: {message}")
    print(f"Warnings: {len(warnings)}")
    for message in warnings:
        print(f"  WARNING: {message}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
