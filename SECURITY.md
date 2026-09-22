# Security and privacy

This template is intended to store sensitive career information locally. The default `.gitignore` excludes personal source documents, normalized extracts, verified facts, generated application folders, and process tracking.

Before making a repository public, run:

```bash
git status
python scripts/validate_workspace.py
```

Review every staged file manually.

Do not commit passwords, cookies, API keys, authentication tokens, identity documents, government identifiers, private references, or confidential employer material.

If sensitive data was committed to Git history, removing the current file is not sufficient. Rewrite the repository history or rotate the exposed secret as appropriate before publishing.
