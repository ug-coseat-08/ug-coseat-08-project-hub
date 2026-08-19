# Repo State Report: `backend`

> URL: https://github.com/ug-coseat-08/backend · Package: `cuponz_backend`
> Last commit: 2025-12-24 · 263 commits · branch `main` · PRIVATE

## Overview

- **Stack**: Node.js / Fastify backend with Knex migrations, MySQL, pnpm package manager.
- **Testing**: `tap` unit tests over `test/utils/` (11 files). Script: `pnpm test` (`tap run -j 8 --disable-coverage`).
- **CI**: ❌ No GitHub Actions workflow.
- **Docs**: README + JSDoc setup + a committed 48 KB generated `TEST_REPORT.md`.

## Installation

⚠️ `pnpm install` **fails on Windows without Visual Studio Build Tools**: `sqlite3@5.1.7` has no prebuilt binary for Node 24 (ABI 137) and its old node-gyp (8.4.1) cannot find VS.

Workaround used: `pnpm install --ignore-scripts` — acceptable here because the unit tests stub the DB layer and never load the sqlite3 native binding.

## Test Results

### Run 1 — bare `pnpm test` (fresh clone, no `.env`)

| Metric | Value |
|---|---|
| Total | 58 |
| Pass | 49 |
| Fail | 9 |

Four test files **crash at module load**:

- `utils/cipher.js` calls `generateCipherMap(process.env.CIPHER_SECRET)` at import time → throws `Valid cipher key is required` (breaks cipher, jwt, otp, preHandler test files)
- `utils/jwt.js` requires `NODE_ENV=development` (per `.env.example`) or `JWT_PRIVATE_KEY_PATH`/`JWT_PUBLIC_KEY_PATH` files → throws `ERR_INVALID_ARG_TYPE` otherwise

### Run 2 — with `NODE_ENV=development` + `CIPHER_SECRET=<dummy>`

| Metric | Value |
|---|---|
| Total | 198 |
| Pass | 185 |
| Fail | 13 |

**Failing files & root causes:**

1. `test/utils/email.js` (3 failures) — tests stub `sendMail` but not the OAuth2 transporter creation. `getNodemailerTransporter` throws `OauthAccessTokenError: Failed to obtain access token: No refresh token or refresh handler callback is set.` → tests are stale relative to the current `email.js` implementation.
2. `test/utils/preHandler.js` (~6 failures) — sinon stubs `jwt.verify` in multiple tests without restoring: `TypeError: Attempted to wrap verify which is already wrapped` — a test-isolation bug (missing `sinon.restore()` / `t.afterEach`).
3. `test/utils/recaptcha.js` (4 failures) — tests expect `recaptchaTokenValidate` to throw on network failure / missing secret / non-200 responses, but the implementation returns `false` instead. Either the tests or the implementation needs to change (decide the intended contract).

## Findings

| Type | Finding | Severity |
|---|---|---|
| Test bug | Tests not self-contained — require `CIPHER_SECRET`, `NODE_ENV` env vars to even load | High |
| Test bug | email.js tests don't mock OAuth2 transporter | High |
| Test bug | preHandler.js sinon double-wrapping (no restore) | High |
| Test bug | recaptcha.js expects throws; impl returns false | Medium |
| Security | `dev/samplekey.pem` is a committed EC **private key** (sample/dev, but should not be in git) | Medium |
| Hygiene | Generated `TEST_REPORT.md` (48 KB) committed to repo | Low |
| Portability | sqlite3 native build fails on Windows / Node 24 | Medium |

## Recommended Actions

1. Make tests self-contained: set required env vars inside test setup (`tap` bootstrap or each file), or lazy-load `CIPHER_MAP`.
2. Fix email tests to stub `getNodemailerTransporter`.
3. Add `afterEach`/`t.teardown` sinon restores in preHandler tests.
4. Align recaptcha contract between tests and implementation.
5. Remove `dev/samplekey.pem` and `TEST_REPORT.md` from git (add to `.gitignore`).
6. Add CI (GitHub Actions) running the tap suite with required env vars.
7. Consider upgrading `sqlite3` (or switch to `better-sqlite3`) so fresh installs work on modern Node.

## Verdict

⚠️ **Needs work** — solid test infrastructure exists (198 assertions) but 13 real failures + env-dependent test loading + no CI.
