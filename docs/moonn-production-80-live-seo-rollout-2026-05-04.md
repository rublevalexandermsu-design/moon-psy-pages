# Moonn Production SEO UI Rollout — 2026-05-04

## Scope

- Project: Moonn / Tilda.
- Tilda project id: `8326812`.
- Workstream branch: `codex/moonn-seo-audit`.
- Source packets: `docs/moonn-production-seo-strengthening-packets-2026-05-04.json`.
- Application path: authenticated Google Chrome profile `Alexander`, visible Tilda UI only.

## Applied

- Applied native Tilda page SEO settings for `77` ready production pages:
  - `meta_title`
  - `meta_descr`
  - `link_canonical`
  - `nosearch = false`
  - `meta_nofollow = false`
- Published each page after saving.
- Fixed the robots prefix issue created by legacy page `/psiholog`:
  - pageId: `114846506`
  - removed page-level noindex/nofollow
  - set canonical to `https://moonn.ru/psiholog-konsultacii-moskva`
  - published the page
- Applied native Tilda page SEO settings for the `3` pages that were previously blocked by `Disallow: /psiholog`:
  - `https://moonn.ru/psiholog-konsultacii-moskva`
  - `https://moonn.ru/psiholog_moskva`
  - `https://moonn.ru/psihology`

## Verification

Final live verification file:

- `docs/moonn-production-80-live-seo-verification-2026-05-04.json`

Final live verification summary:

- total checked pages: `80`
- HTTP 200: `80`
- title matches packet: `80`
- description matches packet: `80`
- canonical matches packet: `80`
- robots clear: `80`
- errors: `0`

Robots verification:

- Removed broad blocking rule: `Disallow: /psiholog`
- The three real production pages are no longer blocked by robots prefix matching.

## Incident / Rule

Symptom:

- The first bulk attempt saved one page, then continued from the page editor instead of returning to the project page.

Root cause:

- The UI automation route was not resetting navigation state between pages after publishing.

Fix:

- `scripts/tilda_page_seo_settings_ui_rollout.py` now calls `ensure_project_page()` before each page settings operation.

Follow-up rule:

- For Tilda bulk UI work, every page iteration must start from a known canonical screen before opening page settings. Do not assume the previous publish screen is a valid context for the next page.

## Residual SEO Work

Not done in this rollout:

- Source-level H1/H2 cleanup inside Tilda blocks.
- Source-level image replacement/filename migration in Tilda file storage.
- Review/noindex/rename decision for `st1` and `st2`.
- Legal/compliant Yandex Services reviews page.
- Manual external profile synchronization for Yandex Services and MGU Istina.
