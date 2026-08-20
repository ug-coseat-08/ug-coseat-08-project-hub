# Repo State Report: `mobile-app`

> URL: https://github.com/ug-coseat-08/mobile-app · Package: `capstone-mobileapp`
> Last commit: 2025-10-29 · 11 commits · branch `main` · PRIVATE

## Overview

- **Stack**: Expo (SDK 54) + React Native + TypeScript, Expo Router, Firebase, i18n.
- **Testing**: ❌ **No test script at all** — only `lint` (`expo lint`) exists.
- **CI**: ❌ No GitHub Actions workflow.

## Verification Results

`npm install` clean (980 packages). `npm run lint` **fails**:

| Metric | Value |
|---|---|
| Errors | **4** |
| Warnings | 19 |

### Errors

1. `components/CouponForm.tsx:253` — `'EncodingType' not found in imported namespace 'FileSystem'` — **this is a real runtime bug**: the code uses `FileSystem.readAsStringAsync(asset.uri, { encoding: FileSystem.EncodingType.Base64 })`, but expo-file-system v19 (bundled with SDK 54) removed the legacy `FileSystem` API. Logo upload will crash at runtime. Fix: `import * as FileSystem from 'expo-file-system/legacy'` or migrate to the new File/Directory API.
2. `app/index.tsx:278`, `app/profile/edit.tsx:212`, and one more — `react/no-unescaped-entities` (unescaped `'` in JSX text).

### Warnings (19)

Missing `useEffect` dependencies (`loadInitialData`, `loadData`, `filterCoupons`, `checkExistingAuth`, `loadUserData`), unused variables (`rememberMe`, `setRememberMe`, `isAppleAuthAvailable`, `handleAppleSignIn`, `handleAppleSignUp`, `setLogoChanged`).

## Findings

| Type | Finding | Severity |
|---|---|---|
| Bug | `FileSystem.EncodingType` removed in expo-file-system v19 → runtime crash in CouponForm | **High** |
| Coverage | Zero tests in an Expo app | High |
| Lint | 4 errors / 19 warnings block a clean lint run | Medium |

## Recommended Actions

1. Fix `CouponForm.tsx` FileSystem import (use `expo-file-system/legacy`) — highest priority.
2. Escape JSX apostrophes (`&apos;` or `{"'"}`).
3. Resolve unused-variable and hook-dependency warnings.
4. Add Jest + `@testing-library/react-native` and write first tests (auth flows, coupon form).
5. Add CI running lint + tests.

## Verdict

❌ **Needs work** — no tests, lint failing, one confirmed runtime-breaking bug.
