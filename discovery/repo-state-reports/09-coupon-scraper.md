# Repo State Report: `coupon-scraper`

> URL: https://github.com/ug-coseat-08/coupon-scraper
> Last commit: 2025-10-28 · 3 commits · branch `main` · PRIVATE

## Overview

- **Stack**: Single-file Python CLI (`youtube_coupon_scraper.py`, 16 KB) that scrapes YouTube video descriptions for coupon codes, with optional OpenAI-based extraction. Deps: yt-dlp, openai, requests, beautifulsoup4.
- **Testing**: ❌ No tests. Verification = syntax check + dependency install + CLI smoke test.
- **CI**: ❌ No GitHub Actions workflow.

## Verification Results

| Check | Result |
|---|---|
| `python -m py_compile` | ✅ 0 errors |
| `pip install -r requirements.txt` (fresh venv) | ✅ clean |
| `python youtube_coupon_scraper.py --help` | ✅ prints full usage (search/urls, date/sort filters, `--method openai/regex`, `--only-codes`) |
| Missing-dependency handling | ✅ exits gracefully with clear message ("yt-dlp not installed…") |

## Findings

| Type | Finding | Severity |
|---|---|---|
| Coverage | No tests at all | Medium |
| Note | `from openai import OpenAI` is a top-level import — the script crashes with ImportError if openai isn't installed, even for `--method regex` runs | Low |

## Recommended Actions

1. Add unit tests for the coupon-code regex extraction (pure functions — easy wins).
2. Move the `openai` import inside the OpenAI-method code path so regex-only users don't need it.
3. Add a `pyproject.toml` / entry point instead of running the script directly.

## Verdict

✅ **Healthy** for a small utility repo — functional, clean, graceful errors; would benefit from a few tests.
