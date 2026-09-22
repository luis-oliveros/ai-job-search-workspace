# Contributing

Contributions are welcome when they preserve the project's evidence-first and human-control principles.

Before opening a pull request:

```bash
pip install -r requirements-dev.txt
pytest -q
python scripts/validate_workspace.py
```

Do not include real resumes, personal contact information, authentication material, or real application records in tests or examples. Use synthetic data.
