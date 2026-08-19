# Repo State Report: `frontend`

> URL: https://github.com/ug-coseat-08/frontend · Package: `cuponz`
> Last commit: 2025-12-27 · 284 commits · branch `main` · PRIVATE

## Overview

- **Stack**: Vite + React SSR (entry-server), Tailwind, vitest, Husky hooks.
- **Testing**: Vitest — **only one test file** (`test/components/captcha.test.jsx`). Script: `npm test` (`vitest run`).
- **CI**: ❌ No GitHub Actions workflow.

## Test Results

| Metric | Value |
|---|---|
| Test files | 1 / 1 passed |
| Tests | **4 / 4 passed** |
| Duration | ~23 s |

✅ All pass — but coverage is **very thin**: only the ReCaptcha component is tested. No tests for pages, hooks, services, or utils.

## Findings

| Type | Finding | Severity |
|---|---|---|
| Coverage | Only 1 test file (captcha component) in a full SSR app | High |
| Hygiene | Both `package-lock.json` **and** `pnpm-lock.yaml` committed — mixed package managers confuse installs | Medium |
| Hygiene | Generated `TEST_REPORT.json` committed | Low |
| Hygiene | Stale build artifact `vite.config.js.timestamp-1729081519487-*.mjs` committed | Low |
| Hygiene | 1 MB `graph.png` committed at repo root | Low |

## Recommended Actions

1. Choose **one** package manager (pnpm is used by sibling `backend`), delete the other lockfile.
2. Expand test coverage: services (API layer), hooks, and key page components.
3. Remove generated artifacts (`TEST_REPORT.json`, vite timestamp file) and add to `.gitignore`.
4. Add CI running `npm run lint` + `npm test`.

## Verdict

✅ Tests pass, but ⚠️ **needs work** — minimal coverage, no CI, mixed lockfiles.
