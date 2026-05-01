# Codex Chat History

Canonical append-only chat history for `moon-psy-site`.

## 2026-05-01T12:07:00+03:00 — Tilda API sync and staging copy

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: connect Tilda API for `moonn.ru`, create a safe copy/staging version before changing the main site, open it in browser, and later audit SEO and analytics.
- Decisions:
  - Treat production Tilda project `Moonn.ru` as the protected source.
  - Store API keys only in local `.env`; keep them out of GitHub.
  - Use Tilda API for read-only local snapshots and audits.
  - Do not claim that API can create an editable Tilda project copy; official Tilda copy path goes through the cabinet UI.
  - For editable staging in Tilda, use UI duplication/move flow and account for the 100-new-pages-per-day limit.
- Created or changed files:
  - `.gitignore`
  - `scripts/tilda_sync_snapshot.py`
  - `docs/tilda-api-staging.md`
  - `docs/codex-chat-history.md`
- Local artifacts:
  - `.env`
  - `output/tilda-snapshot/project.json`
  - `output/tilda-snapshot/pages.json`
  - `output/tilda-snapshot/published-pages.json`
  - `output/tilda-snapshot/pages/*.html`
  - `output/tilda-snapshot/snapshot-manifest.json`
- Verified facts:
  - Tilda API returned project `Moonn.ru` with project id `8326812`.
  - Full local snapshot exported 131 published pages.
  - Local homepage opened at `http://127.0.0.1:8787/index.html`.
  - Browser console reported one error: `Unexpected token 'function'`.
- Initial SEO observations:
  - Homepage title length is 90 characters.
  - Homepage description length is 166 characters.
  - Homepage has 5 H1 headings, 0 H2 headings, 55 images without alt, and 74 scripts.
- Open questions:
  - Whether to create the editable Tilda staging project manually through cabinet access.
  - Whether to copy all pages or only the canonical production pages, because the current project includes drafts, tests, and archive-style pages.
  - Which analytics source is active for traffic and click data: Yandex Metrica, Google Analytics, Tilda statistics, or another tool.
- Risks:
  - API keys were exposed in chat/screenshot and should be regenerated after the workflow is stable.
  - A direct copy of every page may carry old tests, duplicate pages, and SEO debt into the staging project.
