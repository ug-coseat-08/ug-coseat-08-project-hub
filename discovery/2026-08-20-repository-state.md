# Repository State — 2026-08-20

**Prepared by:** Md Mudabbirul Islam Saad · **Status:** Draft for team review · **Evidence:** [Per-repo state reports](repo-state-reports/README.md)

Repository access was granted and verified on 20 August 2026. All twelve repositories in the [ug-coseat-08 GitHub organisation](https://github.com/orgs/ug-coseat-08/repositories) were cloned, installed, and tested one by one on Windows 11 (Node.js 24, pnpm 11, Python 3.11/3.13, Flutter 3.35.7 and 3.47.1). Nothing was pushed back to any client repository. Full per-repo detail, including failure messages and recommended fixes, is in the linked state reports; this page records the consolidated result.

## Summary matrix

| # | Repository | Stack | Tests | Result | CI |
|---|---|---|---|---|---|
| 1 | `backend` | Fastify + MySQL/MariaDB (pnpm) | tap, 198 assertions | ⚠️ 185 pass, 13 fail | None |
| 2 | `ConnectMyTask` | Express + Docker Compose/Traefik | Jest, 18 suites / 196 tests | ✅ All pass | ✅ Green |
| 3 | `Web-connectmytask` | React (CRA) + Tailwind | Jest, 25 suites / 165 tests | ✅ All pass | ✅ Green |
| 4 | `frontend` | Vite + React SSR | Vitest, 1 file / 4 tests | ✅ Pass, very thin coverage | None |
| 5 | `mobile-app` | Expo SDK 54 + React Native | None (lint only) | ❌ Lint fails; one runtime-breaking bug | None |
| 6 | `Mobile-connectmytask` | Flutter + Firebase | 1 boilerplate test | ❌ Fails; dependency pins block current Flutter | None |
| 7 | `propcalc` | Flask + MongoDB / Next.js 15 | None | ❌ Production build broken | None |
| 8 | `deploy` | VitePress docs | n/a | ❌ Docs build fails (dead link) | None |
| 9 | `coupon-scraper` | Python CLI | None | ✅ Smoke test OK | None |
| 10 | `ug-coseat-08-project-hub` | Docs only | n/a | ✅ Healthy | None |
| 11 | `Project-B` | Zip archive only | n/a | 🗑️ Not a real repository | None |
| 12 | `create-debug-test` | Empty | n/a | 🗑️ Zero commits | None |

## Verdicts

- **Healthy:** `ConnectMyTask`, `Web-connectmytask`, `coupon-scraper`, `ug-coseat-08-project-hub`. The two ConnectMyTask repositories are the strongest in the organisation and are the reference for testing and CI practice.
- **Needs work:** `backend` (13 failing tests, environment-dependent test loading, no CI), `frontend` (one test file, mixed lockfiles, no CI), `mobile-app` (`FileSystem.EncodingType` runtime crash in coupon logo upload, no tests), `Mobile-connectmytask` (default counter test that never matched the app, `intl` pin inconsistent with the lockfile).
- **Broken:** `propcalc` (empty `src/app/add-property/page.tsx` fails the Next.js build; 226 committed `node_modules` files; committed `backend/.env`) and `deploy` (one dead link in `server-manual.md` blocks the docs build).
- **Dead weight:** `Project-B` contains only a zip archive of a Flask trading tool, and `create-debug-test` is empty.

## Proposed application-to-repository mapping — pending client confirmation

| Client application | Repositories | Confidence |
|---|---|---|
| Lead-generation coupons ("CuponZ") | `backend`, `frontend`, `mobile-app`, `coupon-scraper`, `deploy` | High — package names (`cuponz_backend`, `cuponz`) and coupon functionality align |
| Task marketplace ("ConnectMyTask") | `ConnectMyTask`, `Web-connectmytask`, `Mobile-connectmytask` | High — matching product names and shared API |
| Property-portfolio calculator ("PropCalc") | `propcalc` | High — direct name and feature match |
| Algorithmic trading | `Project-B` (zip archive of a Flask `trading_tool`) | Medium — archive contents match the description, but the repository form is unusable as-is |

This mapping is an inference from repository contents, not a client-confirmed fact. It must be confirmed with Ishtiaq Ahmad Anan, including whether all five coupon repositories are in scope and what should happen to the trading application, before per-application scope is agreed.

## Security finding — report privately before anything else

The `Project-B` zip contains files that look like real credentials (`trading_tool/.env`, `backend/credentials.json`, `cookies.txt`, `chat_id.txt`), and they remain in Git history. Similar exposures exist in `propcalc` (`backend/.env` with a JWT secret) and `backend` (`dev/samplekey.pem`). No values were opened, copied, or used, and none are reproduced in these records. These must be reported privately to Md Shaik Said and Ishtiaq Ahmad Anan, treated as compromised, and rotated by the authorised owner. See RISK-009 and `SECURITY.md`.

## What this means for scope

- The first client milestone — access, local setup, and recorded setup problems — is effectively complete, and the evidence is ready for a milestone update to the client.
- The four applications differ sharply in maturity. ConnectMyTask has 361 passing tests and green CI, while PropCalc cannot build and the trading application is not yet a usable repository. Any semester plan must be sized per application rather than evenly.
- The client's production-readiness goal now has a concrete basis for the conversation the team needs to have with the supervisor and the client: what is realistically achievable this semester, per application.
- Candidate improvement items identified by the reports (CI for ten repositories, the one-line `deploy` link fix, the `propcalc` build fix, the `mobile-app` FileSystem bug, backend test repairs, Flutter dependency alignment) remain proposals until the client confirms priorities through `UGC08-3`.
