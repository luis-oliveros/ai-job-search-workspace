#!/usr/bin/env python3
"""Create a local application workspace from repository templates."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "item"


def parse_args(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("organization")
    parser.add_argument("role")
    parser.add_argument("--url", default="")
    parser.add_argument("--job-id", default="")
    parser.add_argument("--root", type=Path, default=root)
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    today = date.today().isoformat().replace("-", "")
    base_name = f"{today}_{slugify(args.organization)}_{slugify(args.role)}"
    app_root = args.root / "applications"
    app_root.mkdir(parents=True, exist_ok=True)

    folder = app_root / base_name
    suffix = 2
    while folder.exists():
        folder = app_root / f"{base_name}_{suffix}"
        suffix += 1
    folder.mkdir()

    template_dir = args.root / "templates"
    mapping = {
        "JOB_RECORD.md": "job_record.md",
        "MATCH_ANALYSIS.md": "match_analysis.md",
        "COVER_LETTER.md": "cover_letter.md",
        "FORM_ANSWERS.md": "form_answers.md",
        "SUBMISSION_CHECKLIST.md": "submission_checklist.md",
    }
    for src_name, dst_name in mapping.items():
        src = template_dir / src_name
        if src.exists():
            (folder / dst_name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    metadata = {
        "application_id": folder.name,
        "job_id": args.job_id or None,
        "organization": args.organization,
        "role": args.role,
        "url": args.url or None,
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "DRAFT",
        "submitted": False,
    }
    (folder / "application.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(folder)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
