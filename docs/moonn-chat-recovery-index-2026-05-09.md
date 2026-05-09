# Moonn Chat Recovery Index - 2026-05-09

## Purpose

This file is the fast recovery index for Moonn-related Codex chats after Codex reinstall.
Use it before opening raw session files.

Rules:

- Start from this index.
- Then read `PROJECT_CHAT_HISTORY.md`.
- Then read old `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md`.
- Open raw `*.jsonl` only when exact details are needed.
- Do not copy whole raw sessions into the repo.

## Strategic Assessment

- Platform value: high. Without a chat index, Moonn work will restart from memory and duplicate old Tilda/SEO/legal decisions.
- Obsolescence risk: high. Raw session paths can move, and renamed chats hide that several names point to the same thread id.
- Stronger architecture: use a layered memory model: raw sessions -> compressed chat index -> project chat history -> pinned decisions/incidents.
- Reuse: this same recovery pattern should be reused for AHO Institute, EI course, grants and rowing_agent.
- 3-12 month risk if not fixed: duplicated Tilda edits, wrong branch continuation, repeated legal/privacy mistakes, lost payment/video blockers and stale automation targets.

## Project Chat Sources

| Source | Path | Status | Use |
| --- | --- | --- | --- |
| Current project history | `C:\пайто н тесты\moon-psy-pages\PROJECT_CHAT_HISTORY.md` | Created in recovery branch | Current canonical append-only history for this repo. |
| Recovery audit | `C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md` | Created in recovery branch | Map of repo/worktree/raw-chat recovery. |
| Old rich project history | `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md` | Found | Most useful operational history for Tilda/SEO/legal workstreams. |
| Restore report | `C:\Users\yanta\codex_restore_report.md` | Found | High-level list of large recovered chats and raw paths. |
| Current session index | `C:\Users\yanta\.codex\session_index.jsonl` | Found | Current restored thread ids and names. |
| Backup session index | `C:\Users\yanta\.codex_backup\session_index.jsonl` | Found | Pre-reinstall thread ids and names. |
| Backup sessions | `C:\Users\yanta\.codex_backup\sessions` and `C:\Users\yanta\.codex_backup\archived_sessions` | Found | Raw session recovery archive. |

## Thread Groups To Restore / Continue

### 1. Early Tilda Access

- Thread id: `019cc87d-9e44-78f0-be29-3683890d2b92`
- Chat name: `Найти способ доступа в Тильду`
- Date from index: `2026-03-07T13:30:52Z`
- Source: `C:\Users\yanta\.codex_backup\session_index.jsonl`
- Likely use: early access and login route for Tilda.
- Recovery priority: medium. Useful for access history, but do not reuse old credentials or secrets from chat.

### 2. Tatyana Moonn Activity Research

- Thread id: `019ce137-4454-7720-b375-5d704bafc014`
- Chat name: `Изучи деятельность Татьяны Мун`
- Date from index: `2026-03-12T08:44:02Z`
- Source: `C:\Users\yanta\.codex_backup\session_index.jsonl`
- Likely use: person/entity background, public positioning, initial activity map.
- Recovery priority: medium-high. Use for public biography/provenance, but re-check facts before publication.

### 3. Public Links / Entity Discovery

- Thread id: `019d1ffb-aaca-7083-b0db-9262f963bcd0`
- Chat name: `Ищи публичные ссылки Татьяны Мунн`
- Date from index: `2026-03-24T13:14:46Z`
- Source: `C:\Users\yanta\codex_restore_report.md`; `C:\Users\yanta\.codex_backup\session_index.jsonl`
- Likely use: public links, external profiles, entity bridge.
- Recovery priority: high for provenance, SEO and schema; all external facts must be re-verified before live use.

### 4. Yandex Services / Timepad / Promotion / School / Site

- Thread id: `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b`
- Raw path: `C:\Users\yanta\.codex_backup\sessions\2026\04\21\rollout-2026-04-21T14-49-28-019dafdf-b8d6-7c02-b267-7e5e50ed8b7b.jsonl`
- Known names:
  - `Проанализировать профиль Татьяны`
  - `яндекс Тани, таймпад и продвижение Тани`
  - `яндекс Тани, таймпад/Сайт.продвижение`
  - `яндекс Тани, таймпад/школа/Сайт.продвижение`
  - `яндекс Тани, таймпад-агент/школа/Сайт.продвижение`
- Date range from index: `2026-04-21` to `2026-04-26`
- Source: current and backup `session_index.jsonl`; `C:\Users\yanta\codex_restore_report.md`
- Likely use:
  - Yandex Services profile analysis and rules.
  - Timepad promotion and event visual strategy.
  - School/site promotion bridge.
  - Tatyana Moonn positioning.
- Recovery priority: very high. This is the main pre-Tilda Moonn promotion thread.
- Note: several names are aliases of the same thread id, not separate chats.

### 5. Tilda API Setup

- Thread id: `019de2b9-84d4-7ff2-938d-7b278d021c9b`
- Raw path: `C:\Users\yanta\.codex_backup\sessions\2026\05\01\rollout-2026-05-01T11-48-22-019de2b9-84d4-7ff2-938d-7b278d021c9b.jsonl`
- Known names:
  - `Подключить API к Tilda`
  - `тут будем подключать аппи к тильде к сайту-moonn.ru`
- Date from index: `2026-05-01`
- Source: current and backup `session_index.jsonl`; `C:\Users\yanta\codex_restore_report.md`
- Related branch: `origin/codex/tilda-api-sync`
- Likely use:
  - Tilda API credential variable names.
  - Snapshot workflow.
  - Runtime secret guardrails.
  - Staging page map and Tilda API notes.
- Recovery priority: very high.
- Safety: never restore secret values from chat; only restore variable names, scripts and docs.

### 6. Newer Tilda API / Moonn Reconnect After Reinstall

- Thread id: `019e0b74-78f5-7802-8067-e99870f94306`
- Name from backup state: `тут будем подключать аппи к тильде к сайту-moonn.ru`
- Raw evidence: `C:\Users\yanta\.codex_backup\archived_sessions\rollout-2026-05-09T09-37-23-019e0b74-78f5-7802-8067-e99870f94306.jsonl`
- Source: backup state scan and restore report evidence.
- Likely use: post-reinstall recovery of the same Tilda API workstream.
- Recovery priority: high, but file appears small/truncated in the current backup listing; use state/report metadata first.

### 7. Moonn Reinstall Recovery Chats

- Thread ids and names from current index:
  - `019e0d01-5134-7152-8cd5-a15eeafbe01b` - `Восстановить контур Moonn`
  - `019e0d0e-d874-7260-9589-c49dcb016055` - `Найти историю чата Moon`
  - `019e0d16-5686-7942-8658-5d1a39aa1391` - `Найти репозиторий чатов Moonn` / `подключить аппи к тильда` / `Подключить API к Tilda`
  - `019e0d26-421a-7cb3-b9bc-fe9b1381a955` - `Яндекс Тани, Timepad, агент/школа/сайт`
- Date from index: `2026-05-09`
- Source: `C:\Users\yanta\.codex\session_index.jsonl`
- Likely use: current recovery attempts after reinstall.
- Recovery priority: high as bridge context, but not source of original decisions.

## Workstream History Recovered From Old Project History

The old `moon-psy-site` project history contains these operational workstreams:

| Date | Workstream | Continue in |
| --- | --- | --- |
| 2026-05-03 | Paid video lectures on `events_tp` | `codex/moonn-paid-video-lectures` or new scoped payment branch |
| 2026-05-03 | Private YouTube matching for paid lectures | same paid video lectures workstream |
| 2026-05-03 | Live Moonn SEO metadata audit | `codex/moonn-seo-audit` |
| 2026-05-03 | Moonn Tilda SEO patch packets | `codex/moonn-seo-audit` |
| 2026-05-04 | Moonn Tilda JSON-LD blocks | `codex/moonn-seo-audit` |
| 2026-05-04 | Yandex Services review URL canonicalization | `codex/moonn-seo-audit` plus legal/platform gate |
| 2026-05-04 | Final Moonn sitemap SEO audit | `codex/moonn-seo-audit` |
| 2026-05-04 | Corrected production scope SEO audit | `codex/moonn-seo-audit` |
| 2026-05-04 | Moonn production SEO strengthening packets | `codex/moonn-seo-audit` |
| 2026-05-04 | Moonn production SEO applied through Tilda UI | `codex/moonn-seo-audit` |
| 2026-05-06 | Moonn H1/H2 source cleanup pilot | `codex/moonn-seo-audit` or new H1/H2 branch |
| 2026-05-07 | Moonn scoped H1/H2 publish follow-up | `codex/moonn-seo-audit` |
| 2026-05-07 | Moonn Tilda folder governance inventory | `codex/moonn-seo-audit` or governance branch |
| 2026-05-08 | Moonn post-payment Tilda HEAD rollout verification | paid/video/payment or SEO branch depending task |
| 2026-05-08 | Moonn JSON-LD schema rollout and archive packet | `codex/moonn-seo-audit` |
| 2026-05-08 | Moonn GSC/Yandex reindex submission | `codex/moonn-seo-audit` |
| 2026-05-08 | Moonn manual Google URL Inspection priority requests | `codex/moonn-seo-audit` |
| 2026-05-08 | Moonn RKN/privacy compliance intake | privacy/legal workstream |
| 2026-05-08 | Moonn privacy compliance packet and audit script | privacy/legal workstream |
| 2026-05-08 | Moonn privacy operator details filled | privacy/legal workstream |
| 2026-05-08 | Incident: wrong external domain added to privacy packet | incident log / privacy gate |
| 2026-05-08 | Moonn RKN/privacy layer published and verified | privacy/legal workstream |
| 2026-05-08 | Moonn native policy source hardening | privacy/legal workstream |
| 2026-05-08 | Moonn teen psychology camp page publication | teen camp workstream |
| 2026-05-08 | Moonn teen camp homepage banner completed | teen camp workstream |
| 2026-05-09 | Moonn teen camp payment CTA completed | teen camp/payment workstream |

## Branch Map

Existing remote branches relevant to recovery:

- `origin/codex/moon-psy-site`: early/static site and Tilda brief.
- `origin/codex/tilda-api-sync`: Tilda API snapshot/staging notes and runtime guardrails.
- `origin/codex/timepad-school-moderation-russian-assets`: Russian Timepad school covers.
- `origin/codex/timepad-school-poster-replacement`: replacement Timepad school posters.
- `origin/codex/moonn-context-recovery`: current recovery branch.

Old local rich worktree branch:

- `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site` at audit time was on `codex/moonn-seo-audit`.

## Recommended Chat Restoration Actions

1. Restore/keep the thread group `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` as the main Yandex/Timepad/promotion context.
2. Restore/keep the thread group `019de2b9-84d4-7ff2-938d-7b278d021c9b` as the main Tilda API context.
3. Use `docs/codex-chat-history.md` from old `moon-psy-site` as the operational summary before opening raw sessions.
4. Backfill current `PROJECT_CHAT_HISTORY.md` gradually from old project history, not by copying every raw chat.
5. If a future task is about paid lectures, continue the paid/video workstream, not the SEO branch.
6. If a future task is about privacy/RKN/forms/cookies, create or continue a privacy/legal branch and do not mix it with SEO.
7. If a future task is about Timepad school assets, continue from the Timepad poster branches or create a scoped Timepad branch.
8. If a future task is about current repo recovery only, continue `codex/moonn-context-recovery`.

## Open Gaps

- The current Codex UI may show restored chat names but not full raw threads for every old session.
- Some current 2026-05-09 recovery sessions are tiny in the filesystem listing and may be metadata-only.
- The rich old worktree has untracked payment verification screenshots; do not discard them until their status is reviewed.
- No automated compressed chat index exists yet for Moonn comparable to the wider `registry/codex_context` standard.

## Next Canonical Improvement

Create a Moonn-specific compressed context package:

- `registry/codex_context/moonn/raw-session-map.json`
- `registry/codex_context/moonn/compressed-chat-index.json`
- `registry/codex_context/moonn/project-memory.md`
- `registry/codex_context/moonn/incident-ledger.md`
- `registry/codex_context/moonn/open-questions.md`

This would let future Codex sessions recover context without reading 800 MB to 1 GB raw chat logs.
