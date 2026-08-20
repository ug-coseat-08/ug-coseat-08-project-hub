# Repo State Report: `Project-B`

> URL: https://github.com/ug-coseat-08/Project-B
> Last commit: 2025-11-10 · 3 commits · branch `main` · PRIVATE

## Overview

- **Stack**: None — the repo contains **only** a zip file: `Project-A-main (28).zip` (397 KB).
- **Testing**: n/a.
- **CI**: ❌ No GitHub Actions workflow.

## Contents of the Zip

The archive holds `Project-A-main/` — a Python "trading_tool" (Flask backend with auth, Telegram notifications, indicators, AI agent routes, backtesting, social features). Notable files inside:

```
Project-A-main/cookies.txt
Project-A-main/trading_tool/.env
Project-A-main/trading_tool/backend/credentials.json
Project-A-main/trading_tool/backend/chat_id.txt
Project-A-main/trading_tool/backend/auth/routes.py
Project-A-main/trading_tool/backend/routes/Telegram_noti.py
...
```

⚠️ The zip contains files that look like **real credentials/secrets** (`credentials.json`, `.env`, `cookies.txt`, `chat_id.txt`). Zipping a working project folder with its secrets and committing it to git is a security risk — anyone with repo access (and the full git history) has them.

## Findings

| Type | Finding | Severity |
|---|---|---|
| Security | Potential secrets inside committed zip (`credentials.json`, `.env`, `cookies.txt`, `chat_id.txt`) | **High** |
| Structure | Repo is a zip, not a project — no history, no diffing, no CI possible | High |

## Recommended Actions

1. **Treat any credentials inside the zip as compromised and rotate them** (they are in git history even if removed later).
2. Either extract the project properly (scrubbed secrets + `.gitignore`) or **delete the repo**.
3. If kept, add a README explaining what Project-B is and its relationship to Project-A.

## Verdict

🗑️ **Dead weight / security risk** — not a maintainable repository in its current form.
