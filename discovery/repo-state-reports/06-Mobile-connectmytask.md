# Repo State Report: `Mobile-connectmytask`

> URL: https://github.com/ug-coseat-08/Mobile-connectmytask
> Last commit: 2026-03-19 · 180 commits · branch `main` · PRIVATE
> Note: git history references `SyncMyTask/Mobile-connectmytask` — this appears to be a fork/mirror.

## Overview

- **Stack**: Flutter app (Dart SDK `^3.7.2`) — full marketplace app: auth (incl. Facebook login), Firebase (core/messaging/crashlytics), maps, socket.io chat, notifications, easy_localization.
- **Testing**: `flutter test` — **single file** `test/widget_test.dart`.
- **CI**: ❌ No GitHub Actions workflow.

## Verification Results (multi-step)

1. Flutter not installed locally — installed Flutter 3.47.1 stable to test.
2. **`flutter pub get` fails on 3.47.1**: `intl 0.20.2` (exact pin in pubspec) conflicts with `easy_localization` → `flutter_localizations` (needs `intl ^0.20.3`). Also found a **pubspec/lock inconsistency**: pubspec pins `intl: 0.20.2` but `pubspec.lock` resolved `intl 0.20.3`.
3. With pin temporarily relaxed to `^0.20.3`: **compile fails** — `google_fonts 6.2.1` uses `FontWeight` keys in a const map, which newer Dart rejects ("does not have a primitive operator `==`").
4. Installed **Flutter 3.35.7** (matching the lockfile era: dart ≥3.8, flutter ≥3.27):
   - `flutter pub get` ✅ succeeds
   - `flutter test` ❌ **fails**:

```
TestFailure: Expected: exactly one matching candidate
Actual: Found 0 widgets with text "0"
```

**Root cause**: `widget_test.dart` is the untouched **default Flutter counter template** ("Counter increments smoke test") while the actual app renders a splash screen (`MyApp` → `SplashScreen` with Firebase init). The test never matched the app. (Repo files were restored to clean state after testing.)

## Findings

| Type | Finding | Severity |
|---|---|---|
| Test bug | Only test is boilerplate counter test → always fails | High |
| Dependency | pubspec pins `intl: 0.20.2`, lock has `0.20.3` — inconsistent; plain `flutter pub get` fails on current stable | High |
| Dependency | `google_fonts 6.2.1` doesn't compile on Flutter ≥3.38 — project locked to older SDK | Medium |
| Coverage | No real widget/unit tests for a 180-commit production app | High |

## Recommended Actions

1. Delete or rewrite `widget_test.dart` — pump `SplashScreen`/`MyApp` with mocked Firebase instead of counter assertions.
2. Align `intl` constraint with the lockfile (`^0.20.3`) and regenerate `pubspec.lock`.
3. Upgrade `google_fonts` to a version compatible with current Flutter, then re-pin the SDK range.
4. Add real tests: auth screens, models/services.
5. Add CI (flutter analyze + flutter test).

## Verdict

❌ **Needs work** — the only test fails, and dependency state blocks current-Flutter onboarding.
