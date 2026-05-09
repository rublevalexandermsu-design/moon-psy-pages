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

## 2026-05-09 17:45 Europe/Moscow - Moonn Chat Recovery Index

- Project: Moonn / Tatyana Moonn site / promotion / Timepad.
- Workstream: recovery audit and chat restoration.
- Branch: `codex/moonn-context-recovery`.
- User request:
  - identify which old chats belonged to the Moonn project before Codex reinstall;
  - explain which chats should be restored or continued so work is not restarted from scratch;
  - preserve the recovery map inside the project.
- Decisions:
  - Continue the existing recovery branch rather than opening a new workstream.
  - Treat old `moon-psy-site/docs/codex-chat-history.md` as the richest operational summary.
  - Treat raw `*.jsonl` sessions as recovery archive only, not as the first working memory layer.
  - Group renamed chats by thread id because several visible chat names are aliases of the same thread.
- Created or changed files:
  - `docs/moonn-chat-recovery-index-2026-05-09.md`
- Important recovered thread groups:
  - `019cc87d-9e44-78f0-be29-3683890d2b92` - early Tilda access.
  - `019ce137-4454-7720-b375-5d704bafc014` - Tatyana Moonn activity research.
  - `019d1ffb-aaca-7083-b0db-9262f963bcd0` - public links / entity discovery.
  - `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` - Yandex Services / Timepad / promotion / school / site.
  - `019de2b9-84d4-7ff2-938d-7b278d021c9b` - Tilda API setup.
  - `019e0b74-78f5-7802-8067-e99870f94306` - newer Tilda API / Moonn reconnect after reinstall.
  - 2026-05-09 recovery chats: `019e0d01`, `019e0d0e`, `019e0d16`, `019e0d26`.
- Risks and incidents:
  - Some old raw chats are very large and should not be loaded wholesale.
  - Some 2026-05-09 recovered session files appear tiny or metadata-only.
  - The same Moonn task appears under multiple chat names; route by thread id and workstream, not only visible title.
- Open questions:
  - Whether to create a full Moonn compressed context package under `registry/codex_context/moonn/`.
  - Whether to backfill `PROJECT_CHAT_HISTORY.md` with summarized entries from all 26 old `moon-psy-site` workstreams.
- Commit hash:
  - `944f896` for the chat recovery index.
