# Put your CV and professional documents here

For the normal no-code workflow, simply copy your files into this folder and then open the **whole repository folder** in your AI desktop client.

Supported source types:

- PDF (`.pdf`)
- Word (`.docx`)
- Markdown (`.md`)
- Plain text (`.txt`)

Examples:

```text
profile_sources/
├── CV.pdf
├── academic_cv.docx
├── certificates.pdf
└── publications.md
```

Then tell your AI:

```text
Read AGENTS.md and initialize my profile from the documents in profile_sources. Handle any technical processing yourself.
```

You do **not** need to run Python or PowerShell yourself.

This directory is ignored by Git except for this README and `.gitkeep`, which reduces the risk of publishing personal documents by mistake.
