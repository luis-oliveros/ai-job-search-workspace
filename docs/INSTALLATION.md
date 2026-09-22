# Installation and use for non-technical users

This is the recommended flow for someone who discovers the project on GitHub and wants to use it without a terminal, Python, PowerShell, or Git.

## Step 1. Download from GitHub

On the repository page:

1. Click the green **Code** button.
2. Select **Download ZIP**.
3. Unzip the downloaded file.
4. Move the folder somewhere easy to find.

## Step 2. Install a compatible AI client

### Recommended: ChatGPT Desktop

Official download:

https://chatgpt.com/download/

OpenAI documents local-folder access in Work and Codex on desktop here:

https://help.openai.com/en/articles/20001275/

### Alternative: Cursor

Official download:

https://cursor.com/download

### Claude

Official download:

https://claude.com/download

The repository includes `CLAUDE.md` so compatible Claude environments can discover the central `AGENTS.md` contract.

## Step 3. Add your career documents

Copy PDF, DOCX, TXT, or Markdown files into:

```text
profile_sources/
```

You may add multiple resume versions, certificates, publication lists, or other factual sources. A PDF does not need to be converted to Word first.

## Step 4. Open the whole project folder

In ChatGPT Desktop, use Work or Codex and open the local project folder. In Cursor, use Open Folder. Select the entire unzipped repository so the agent can see both your documents and the workspace instructions.

## Step 5. First prompt

```text
Read AGENTS.md and START_HERE.md. Initialize my profile from the documents in profile_sources. Handle any technical processing yourself. Do not invent information. Show me facts that require review before starting a job search.
```

The AI should inspect PDF, DOCX, TXT, and Markdown directly when possible. If additional extraction is needed and the current environment exposes local execution tools, the agent should perform that work itself.

## Step 6. Review

Review `profile/FACTS_VERIFIED.md` and any items marked `CONFLICT`, `NEEDS_REVIEW`, or `UNVERIFIED`.

## Step 7. Define your search

Describe what you want conversationally and ask the agent to save the criteria.

## Step 8. Start the search

```text
Start my job search.
```

Or:

```text
Analyze this job: <URL>
```

## Step 9. Prepare an application

```text
Prepare my application for this job. Tailor my resume using verified facts only and show me the materials before any submission.
```

## Scanned PDFs

Image-only PDFs may require OCR. Normal users are not expected to install or run OCR tools manually. The agent should use available tools where possible or clearly identify the inaccessible source.

## Advanced/developer setup

See `docs/ADVANCED_SETUP.md` for optional Python helpers, deterministic extraction, OCR configuration, validation, and tests.
