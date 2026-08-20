# Repo State Report: `deploy`

> URL: https://github.com/ug-coseat-08/deploy · Package: `deploy`
> Last commit: 2025-10-29 · 19 commits · branch `main` · PRIVATE

## Overview

- **Stack**: VitePress documentation site (`docs/`) + deployment scaffolding (`deploy/` dir, `.gitmodules`).
- **Testing**: n/a (docs repo). Verification = `pnpm docs:build`.
- **CI**: ❌ No GitHub Actions workflow.

## Verification Results

- `pnpm install` ✅ clean (vitepress 1.4.1).
- `pnpm docs:build` ❌ **fails**:

```
(!) Found dead link ./development-manual in file server-manual.md
[vitepress] 1 dead link(s) found.
✖ Build failed
```

**Root cause**: `docs/server-manual.md` (line 5) links to a "development manual" at `./development-manual.md`, but no such file exists. The docs folder contains:

```
docs/api-examples.md
docs/index.md
docs/maintaining-manual.md
docs/markdown-examples.md
docs/server-manual.md
docs/systeminstallation-manual.md
```

The intended target is almost certainly `./systeminstallation-manual.md` (likely renamed at some point).

## Findings

| Type | Finding | Severity |
|---|---|---|
| Bug | Docs build fails — dead link `./development-manual` in `server-manual.md` | **High** (blocks publish) |
| Hygiene | `README.md` is 0 bytes (empty) | Low |
| Hygiene | Committed PDFs (`redemptions_coupon_28.pdf`, `user-manual.pdf`) in docs | Low |

## Recommended Actions

1. Fix the link in `server-manual.md`: `./development-manual.md` → `./systeminstallation-manual.md` (one-line fix, unblocks the build).
2. Write a real README describing what this repo deploys and how.
3. Replace committed PDFs with Markdown pages.
4. Add CI that runs `pnpm docs:build` on every push.

## Verdict

❌ **Broken** — but it's a one-line fix away from building.
