# Repo State Report: `propcalc`

> URL: https://github.com/ug-coseat-08/propcalc · Package: `investment-property-calculator-main`
> Last commit: 2025-08-02 · 56 commits · branch `my-original-version` · PRIVATE

## Overview

- **Stack**: Monorepo — Python/Flask + MongoDB backend (`backend/`), Next.js 15 + TypeScript frontend (`frontend/`).
- **Testing**: ❌ **No tests anywhere** (root and frontend `test` scripts are the default `"Error: no test specified"`).
- **CI**: ❌ No GitHub Actions workflow.

## Verification Results

### Backend (Python/Flask)

- `python -m py_compile` over all 25 `.py` files → ✅ **0 syntax failures**.
- Committed `__pycache__` files are from Python 3.12; a local run needs `pip install -r requirements.txt` (heavy: scikit-learn, jupyter, etc.) + MongoDB at `mongodb://localhost:27017`.

### Frontend (Next.js)

- `npm run build` with the **committed `node_modules`** → ❌ fails: `next/dist/bin/next` missing — the committed node_modules is **incomplete/broken** (226 files).
- After a fresh `npm install` (525 packages): build compiles ✅ then ❌ **fails type-checking**:

```
.next/types/app/add-property/page.ts:2:24
Type error: File 'src/app/add-property/page.tsx' is not a module.
```

**Root cause**: `src/app/add-property/page.tsx` is a **0-byte empty file** committed to the repo. Next.js requires every `page.tsx` to export a component.

## Findings

| Type | Finding | Severity |
|---|---|---|
| Bug | `src/app/add-property/page.tsx` is empty (0 bytes) → production build fails | **High** |
| Hygiene | **226 `node_modules` files committed** to git — and they're broken/incomplete | High |
| Hygiene | 8 `__pycache__` / `.pyc` files committed | Medium |
| Security | `backend/.env` committed (contains `JWT_SECRET_KEY=super-secret`, local Mongo URI) | Medium |
| Hygiene | Large PDFs committed (`PropCalc.pdf` 868 KB, `project setup guide.pdf` 120 KB) | Low |
| Coverage | Zero tests for both backend and frontend | High |

## Recommended Actions

1. **Implement or delete `add-property/page.tsx`** — one-file fix to unblock the build.
2. `git rm -r --cached frontend/node_modules` and the `__pycache__` folders; add a proper `.gitignore`.
3. Remove `backend/.env` from git history (rotate JWT secret if ever used beyond local dev).
4. Add tests: pytest for Flask services/routes; Jest/RTL for Next.js pages.
5. Replace committed PDFs with a `/docs` folder or wiki links.

## Verdict

❌ **Broken** — production build fails; worst repo hygiene in the org.
