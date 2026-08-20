# ug-coseat-08 — Repository State Report

> Generated: **2026-08-20** (Australia/Sydney) · Org: https://github.com/orgs/ug-coseat-08/repositories
> All 12 repositories were cloned locally and tested one by one. Nothing was pushed back to GitHub.

## Test Environment

| Tool | Version |
|---|---|
| OS | Windows 11 (PowerShell) |
| Node.js | v24.13.0 |
| pnpm | 11.22.0 |
| Python | 3.11.2 (system) / 3.13 (miniconda pip) |
| Flutter | 3.35.7 & 3.47.1 stable (installed for testing only) |
| gh CLI | 2.93.0 (authenticated) |

## Summary Matrix

| # | Repo | Stack | Tests | Result | CI | Report |
|---|---|---|---|---|---|---|
| 1 | backend | Fastify (Node) | tap, 11 files | ⚠️ 185/198 pass | ❌ None | [01-backend.md](01-backend.md) |
| 2 | ConnectMyTask | Express + Docker | Jest, 18 suites / 196 | ✅ All pass | ✅ Green | [02-ConnectMyTask.md](02-ConnectMyTask.md) |
| 3 | Web-connectmytask | React (CRA) | Jest, 25 suites / 165 | ✅ All pass | ✅ Green | [03-Web-connectmytask.md](03-Web-connectmytask.md) |
| 4 | frontend | Vite + React SSR | Vitest, 1 file / 4 | ✅ All pass (thin) | ❌ None | [04-frontend.md](04-frontend.md) |
| 5 | mobile-app | Expo SDK 54 | None (lint only) | ❌ Lint fails | ❌ None | [05-mobile-app.md](05-mobile-app.md) |
| 6 | Mobile-connectmytask | Flutter | widget_test (1) | ❌ Fails | ❌ None | [06-Mobile-connectmytask.md](06-Mobile-connectmytask.md) |
| 7 | propcalc | Flask + Next.js | None | ❌ Build broken | ❌ None | [07-propcalc.md](07-propcalc.md) |
| 8 | deploy | VitePress docs | n/a | ❌ Docs build fails | ❌ None | [08-deploy.md](08-deploy.md) |
| 9 | coupon-scraper | Python | None | ✅ Smoke OK | ❌ None | [09-coupon-scraper.md](09-coupon-scraper.md) |
| 10 | ug-coseat-08-project-hub | Docs only | n/a | ✅ Healthy | ❌ None | [10-ug-coseat-08-project-hub.md](10-ug-coseat-08-project-hub.md) |
| 11 | Project-B | zip only | n/a | 🗑️ Not a real repo | ❌ None | [11-Project-B.md](11-Project-B.md) |
| 12 | create-debug-test | — | — | 🗑️ Empty (0 commits) | ❌ None | [12-create-debug-test.md](12-create-debug-test.md) |

## Verdicts

- ✅ **Healthy**: ConnectMyTask, Web-connectmytask, ug-coseat-08-project-hub, coupon-scraper
- ⚠️ **Needs work**: backend, frontend, mobile-app, Mobile-connectmytask
- ❌ **Broken**: propcalc, deploy
- 🗑️ **Dead weight**: Project-B, create-debug-test

## Org-wide Recommendations

1. **Add CI to the 10 repos without it.** Two green workflows already exist (ConnectMyTask, Web-connectmytask) to copy from.
2. **Fix failing tests**: backend (13 failures), Flutter counter test, propcalc empty page file.
3. **Scrub committed artifacts/secrets**: `node_modules`, `__pycache__`, `.env`, `dev/samplekey.pem`, Project-B zip.
4. **Standardize package managers** (backend/deploy = pnpm, frontend has both npm + pnpm lockfiles).
5. **Delete dead repos**: create-debug-test (empty), Project-B (zip only, potential secrets inside).

## Locations

- Source: cloned from https://github.com/orgs/ug-coseat-08/repositories and tested locally; local clone paths are member-specific and not recorded here.
