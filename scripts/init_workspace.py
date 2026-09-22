#!/usr/bin/env python3
"""Create local, git-ignored user state from tracked example files."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

MAPPINGS = {
    "profile/FACTS_VERIFIED.example.md": "profile/FACTS_VERIFIED.md",
    "profile/PROFILE_SUMMARY.example.md": "profile/PROFILE_SUMMARY.md",
    "search/SEARCH_CRITERIA.example.md": "search/SEARCH_CRITERIA.md",
    "search/JOBS.example.csv": "search/JOBS.csv",
    "applications/APPLICATIONS.example.csv": "applications/APPLICATIONS.csv",
    "tracking/ACTIVE_PROCESSES.example.md": "tracking/ACTIVE_PROCESSES.md",
}

def parse_args(argv=None):
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=root)
    parser.add_argument("--force", action="store_true", help="Overwrite existing local state files.")
    return parser.parse_args(argv)

def main(argv=None) -> int:
    args = parse_args(argv)
    created = 0
    skipped = 0
    for src_rel, dst_rel in MAPPINGS.items():
        src = args.root / src_rel
        dst = args.root / dst_rel
        if not src.exists():
            raise FileNotFoundError(f"Missing example file: {src_rel}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists() and not args.force:
            print(f"SKIP {dst_rel} (already exists)")
            skipped += 1
            continue
        shutil.copyfile(src, dst)
        print(f"CREATE {dst_rel}")
        created += 1
    print(f"Created: {created}; skipped: {skipped}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
