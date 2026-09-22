# Publish the template to GitHub

Before publishing, validate the repository and confirm that no private files are staged.

```bash
python scripts/validate_workspace.py
git status
```

Initialize the repository if needed:

```bash
git init
git add .
git status
git commit -m "Initial public release"
git branch -M main
```

Create an empty repository on GitHub, then add the remote and push:

```bash
git remote add origin https://github.com/<your-user>/<your-repository>.git
git push -u origin main
```

## Privacy check

The default `.gitignore` excludes personal profile sources and local job-search state. Still inspect `git status` before every public push. Do not publish resumes, contact details, references, application records, tokens, cookies, or authentication material unless you intentionally want those files public.

## Recommended first release

Tag the first stable version after the GitHub Actions test workflow passes:

```bash
git tag v1.0.0
git push origin v1.0.0
```
