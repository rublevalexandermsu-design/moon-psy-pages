# Project Chat History

Append-only project history for `moon-psy-pages`.

## 2026-05-09 17:05 Europe/Moscow - Moonn Context Recovery Audit

- Project: Moonn / Tatyana Moonn site / promotion / Timepad.
- Workstream: recovery audit and context restoration.
- Branch: `codex/moonn-context-recovery`.
- User request:
  - restore the Moonn / Tatyana site / promotion / Timepad contour;
  - run recovery audit first;
  - do not publish the site;
  - do not change Tilda, Timepad, APIs, external integrations or forms;
  - check Git, branches, assets, pages, data registry, SEO/schema, image sitemap, integration notes and chat history;
  - use `C:\Users\yanta\codex_restore_report.md`, `C:\Users\yanta\.codex_backup`, and `C:\Users\yanta\.codex_broken_after_sessions`;
  - find raw chats for Yandex/Tanya/Timepad/promotion and Tilda API setup.
- Decisions:
  - Created and used branch `codex/moonn-context-recovery` from `main`.
  - Treated current repo `C:\пайто н тесты\moon-psy-pages` as the static GitHub Pages / school subdomain layer.
  - Identified `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site` as the richer existing local Tilda/API/SEO/legal operations worktree.
  - Did not call Tilda API, Timepad, forms, live publication, or external integration write paths.
- Created or changed files:
  - `PROJECT_CHAT_HISTORY.md`
  - `docs/moonn-recovery-audit-2026-05-09.md`
- Important artifacts:
  - Recovery audit: `docs/moonn-recovery-audit-2026-05-09.md`
  - Restore report: `C:\Users\yanta\codex_restore_report.md`
  - Backup automation: `C:\Users\yanta\.codex_backup\automations\moonn-seo-leftovers-morning-check\automation.toml`
  - Old project chat archive: `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md`
- Risks and incidents:
  - Current repo lacked a root `PROJECT_CHAT_HISTORY.md`.
  - Static public pages contain internal/rationale language such as `машинный слой` and `SEO / AEO / IEO-слой`.
  - Current repo lacks an image sitemap.
  - Current repo does not copy `assets/timepad` into `dist`.
  - Automation still points to old worktree path; do not update it until canonical local repo/worktree decision is made.
- Open questions:
  - Should old `moon-psy-site` remain the canonical Moonn operations worktree?
  - Should the root `PROJECT_CHAT_HISTORY.md` be backfilled from old `docs/codex-chat-history.md`?
  - Should Timepad visual assets be part of public static dist or only source assets for external upload?
  - Should `.gitignore` guardrails from `origin/codex/tilda-api-sync` be promoted to `main`?
- Commit hash:
  - `8ceb78a` for the initial recovery audit documentation.
