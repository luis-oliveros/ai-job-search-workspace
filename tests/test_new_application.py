from __future__ import annotations

import importlib.util
import json
from pathlib import Path


def load_module(root: Path):
    path = root / "scripts" / "new_application.py"
    spec = importlib.util.spec_from_file_location("new_application", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_new_application_workspace(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    mod = load_module(repo_root)

    (tmp_path / "templates").mkdir()
    for name in [
        "JOB_RECORD.md",
        "MATCH_ANALYSIS.md",
        "COVER_LETTER.md",
        "FORM_ANSWERS.md",
        "SUBMISSION_CHECKLIST.md",
    ]:
        (tmp_path / "templates" / name).write_text(f"# {name}\n", encoding="utf-8")

    rc = mod.main(["Example Org", "Data Scientist", "--job-id", "J-123", "--root", str(tmp_path)])
    assert rc == 0

    folders = [p for p in (tmp_path / "applications").iterdir() if p.is_dir()]
    assert len(folders) == 1
    metadata = json.loads((folders[0] / "application.json").read_text(encoding="utf-8"))
    assert metadata["organization"] == "Example Org"
    assert metadata["role"] == "Data Scientist"
    assert metadata["job_id"] == "J-123"
    assert metadata["submitted"] is False
