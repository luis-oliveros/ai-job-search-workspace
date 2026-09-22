from __future__ import annotations

import importlib.util
from pathlib import Path

def load_module(root: Path):
    path = root / "scripts" / "init_workspace.py"
    spec = importlib.util.spec_from_file_location("init_workspace", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module

def test_init_workspace(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    mod = load_module(repo_root)
    for src_rel in mod.MAPPINGS:
        p = tmp_path / src_rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("example\n", encoding="utf-8")
    assert mod.main(["--root", str(tmp_path)]) == 0
    for dst_rel in mod.MAPPINGS.values():
        assert (tmp_path / dst_rel).read_text(encoding="utf-8") == "example\n"
