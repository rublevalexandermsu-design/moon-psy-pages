# Moonn Recovery Audit - 2026-05-09

## Scope

- Project: Moonn / Tatyana Moonn site / promotion / Timepad.
- Current working repo: `C:\пайто н тесты\moon-psy-pages`.
- Recovery branch: `codex/moonn-context-recovery`.
- Boundary: read-only recovery audit for external systems. No Tilda API calls, no Timepad changes, no form submissions, no live publication.

## Strategic Score

- Platform value: high. The Moonn contour connects public site, Tilda, Timepad, SEO, images, legal gates and future promotion automation.
- Obsolescence risk: high if the current static `moon-psy-pages` repo is treated as the whole system. The richer Tilda/SEO/legal contour exists in another local worktree.
- Stronger architecture opportunity: high. The system needs one explicit control map that separates Tilda production, GitHub Pages SEO layer, Timepad event assets and compliance records.
- Reuse potential: high. The same recovery pattern should be reused for AHO Institute events, EI course, grants and future publication pipelines.
- 3-12 month failure mode: duplicated pages, stale Tilda automation target, missing legal/privacy gates, public internal text leaks, and image/SEO assets drifting away from event registries.

## Verified Facts

- `C:\пайто н тесты\moon-psy-pages` is a Git repo with remote `https://github.com/rublevalexandermsu-design/moonn-psy-pages.git`.
- Recovery branch `codex/moonn-context-recovery` was created from `main`.
- `main` equals `origin/main` at `0de7867 Add remaining Timepad school posters` at audit start.
- Existing remote workstreams include:
  - `origin/codex/moon-psy-site`
  - `origin/codex/tilda-api-sync`
  - `origin/codex/timepad-school-moderation-russian-assets`
  - `origin/codex/timepad-school-poster-replacement`
- Current repo source of truth for generated static pages is `data/site.json`.
- Current generated public output is in `dist/`.
- Current GitHub Pages workflow deploys only on `main` and `workflow_dispatch`.
- Current CNAME is `school.miiiips.ru`.
- Current repo did not have `PROJECT_CHAT_HISTORY.md` before this recovery audit.

## Recovery Sources Checked

- `C:\Users\yanta\codex_restore_report.md`
- `C:\Users\yanta\.codex_backup`
- `C:\Users\yanta\.codex_broken_after_sessions`
- `C:\Users\yanta\.codex\session_index.jsonl`
- Current repo `C:\пайто н тесты\moon-psy-pages`
- Existing older/richer worktree `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`

## Raw Chat Map

| Thread | ID | Source path / evidence | Notes |
| --- | --- | --- | --- |
| `яндекс Тани, таймпад и продвижение Тани` | `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` | `C:\Users\yanta\.codex\session_index.jsonl`; raw backup `C:\Users\yanta\.codex_backup\sessions\2026\04\21\rollout-2026-04-21T14-49-28-019dafdf-b8d6-7c02-b267-7e5e50ed8b7b.jsonl` | Same thread later renamed across Timepad/site/promotion variants. |
| `яндекс Тани, таймпад/Сайт.продвижение` | `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` | `C:\Users\yanta\.codex\session_index.jsonl` | Updated 2026-04-24. |
| `яндекс Тани, таймпад/школа/Сайт.продвижение` | `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` | `C:\Users\yanta\.codex\session_index.jsonl` | Updated 2026-04-25. |
| `яндекс Тани, таймпад-агент/школа/Сайт.продвижение` | `019dafdf-b8d6-7c02-b267-7e5e50ed8b7b` | `C:\Users\yanta\codex_restore_report.md` | Listed as a large archived session. |
| `Подключить API к Tilda` | `019de2b9-84d4-7ff2-938d-7b278d021c9b` | `C:\Users\yanta\.codex\session_index.jsonl`; raw backup `C:\Users\yanta\.codex_backup\sessions\2026\05\01\rollout-2026-05-01T11-48-22-019de2b9-84d4-7ff2-938d-7b278d021c9b.jsonl` | Tilda API sync thread; remote branch `origin/codex/tilda-api-sync`. |
| `тут будем подключать аппи к тильде к сайту-moonn.ru` | `019e0b74-78f5-7802-8067-e99870f94306` and earlier `019de2b9-84d4-7ff2-938d-7b278d021c9b` | Backup state evidence inside `C:\Users\yanta\.codex_backup\state_5.sqlite`; archived session path was found in restore scan | Treat as continuation of Tilda API/Moonn recovery, not a separate public-site source. |

## Current Repo Map

### Site

- Static subdomain: `school.miiiips.ru`.
- Brand domain referenced: `moonn.ru`.
- Pages generated from `data/site.json`:
  - `index.html`
  - `psycholog-online-consultation.html`
  - `podrostkovyy-psiholog.html`
  - `trevoga-strahi-samoocenka.html`
  - `otnosheniya-semeynye-konflikty.html`
  - `gipnoz.html`
  - `reviews.html`
- Separate hand-written page:
  - `teen-softskills/index.html`

### Assets

- Static page styles: `assets/site.css`.
- Teen school posters: `assets/teen-softskills/`.
- Timepad visual cards: `assets/timepad/visuals/tatyana-munn/`.
- Asset names are Latin-script, which matches the project naming rule.
- Current `dist/assets` contains only part of copied assets, because `build_site.py` copies `assets/teen-softskills` but does not copy `assets/timepad`.

### SEO / Schema

- `build_site.py` emits canonical URLs, robots, sitemap, `llms.txt`, and JSON-LD for `WebPage`, `Person`, `FAQPage`, and `Service`.
- `dist/sitemap.xml` includes the generated pages plus `/teen-softskills/`.
- No image sitemap was found in current repo.
- `teen-softskills/index.html` has `og:image` and JSON-LD, but is not driven by `data/site.json`.

### Tilda / Timepad Integration Notes

- Current `main` does not contain the rich Tilda docs from `origin/codex/tilda-api-sync` or old `moon-psy-site`.
- `origin/codex/tilda-api-sync` contains:
  - `docs/tilda-api-staging.md`
  - `docs/tilda-radiant-sanctuary.md`
  - `registry/tilda/moonn-staging-page-map.json`
  - `scripts/tilda_sync_snapshot.py`
- Old local worktree `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site` contains the main Tilda/SEO/legal recovery corpus.

## Rich Moonn Worktree Map

Existing local worktree:

- Path: `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`
- Branch at audit: `codex/moonn-seo-audit`
- Remote: same `moonn-psy-pages` repository.
- Local untracked files exist:
  - `docs/teen-psychology-camp-2026/payment-after-setting-check.png`
  - `docs/teen-psychology-camp-2026/payment-submit-test-check.png`
  - `docs/teen-psychology-camp-2026/payment-ux-fix-check.png`

Important artifacts found there:

- `docs/codex-chat-history.md`
- `docs/moonn-gsc-yandex-reindex-report-2026-05-08.md`
- `docs/moonn-privacy-compliance-audit-2026-05-08.md`
- `docs/moonn-rkn-compliance-rollout-plan-2026-05-08.md`
- `docs/moonn-schema-layer-packet-2026-05-08.md`
- `docs/moonn-tilda-page-governance-inventory-2026-05-07.md`
- `docs/moonn-tilda-archive-execution-packet-2026-05-08.md`
- `docs/moonn-tilda-folder-governance-plan-2026-05-08.md`
- `scripts/moonn_privacy_compliance_audit.py`
- `output/tilda-production-current-snapshot/pages/`

## External System Map

### Tilda API

- Official read-only inventory previously identified Tilda project id `8326812`.
- Old governance inventory counted `164` Tilda pages.
- Work scope protected pages: `83`.
- Tilda API credential variable names from prior thread: `TILDA_PUBLIC_KEY`, `TILDA_SECRET_KEY`, `TILDA_API_BASE_URL`, `TILDA_PROJECT_ID`.
- Secret values were not read or recorded in this recovery audit.

### Timepad

- Current repo has Timepad-oriented visual cards under `assets/timepad/visuals/tatyana-munn/`.
- Old paid lecture history says `events_tp` is the canonical pilot storefront and 10 unique Timepad event IDs were extracted from that page.
- Paid video lectures remain blocked until private video registry and payment/provider checks are complete.

### SEO / Indexing

- Old reindex report says Moonn production scope was `83` URLs.
- Live sitemap at `https://moonn.ru/sitemap.xml` had `149` URLs at 2026-05-08 check.
- Google sitemap submission and limited URL Inspection were done in old workflow.
- Yandex re-crawl submission for 83 URLs was done in old workflow.
- Stop rule: do not manually submit all 83 URLs through Google URL Inspection.

### Legal / Publication Gate

- Old privacy audit found `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` returning `404` on 2026-05-08.
- Old RKN plan proposed strengthening existing `/politic` first and only then adding standard aliases or redirects.
- Form checkbox/cookie disclosure gaps were found across most of the 83 production-scope pages.
- Legal/publication changes remain high-risk and require explicit approval before live Tilda edits.

### Public Text vs Hidden Marketing Tokens

- Current repo uses Latin image file names with marketing tokens in filenames.
- Public text in generated cluster pages includes internal/rationale phrases such as `машинный слой`, `SEO / AEO / IEO-слой`, and `зачем нужен отдельный поддомен`.
- This is a publication-quality risk: internal explanations should move to registry/docs, while public pages should be editorial reader-facing text.

## Recovery Findings

1. The current folder is not the full Moonn operational control plane. It is the static GitHub Pages/subdomain layer.
2. The richer Tilda/API/SEO/legal operational contour exists in `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`.
3. The backup automation `moonn-seo-leftovers-morning-check` still points to the old worktree path and thread `019de2b9-84d4-7ff2-938d-7b278d021c9b`.
4. Current `main` lacks `PROJECT_CHAT_HISTORY.md`; the old worktree has `docs/codex-chat-history.md`.
5. Current `main` lacks an image sitemap and does not copy `assets/timepad` into `dist`.
6. Current `.gitignore` is weaker than the Tilda API branch guard and does not explicitly ignore `.env`, token, credential and local runtime artifacts.
7. Several public static pages expose internal platform/rationale language.
8. No external systems were changed during this audit.

## Recommended Recovery Route

1. Treat `moon-psy-site` as the canonical Tilda/Moonn production operations worktree until proven otherwise.
2. Treat `moon-psy-pages` as the static GitHub Pages SEO/Timepad-support layer.
3. Merge or cherry-pick only documentation and safe guardrails into `main` after reviewing branch history:
   - `docs/codex-chat-history.md` or a project-level `PROJECT_CHAT_HISTORY.md`
   - `docs/tilda-api-staging.md`
   - `registry/tilda/moonn-staging-page-map.json`
   - `.gitignore` runtime/secrets guard
4. Do not publish or edit Tilda until:
   - legal/privacy variables are confirmed;
   - `/politic` vs `/privacy` canonical route is chosen;
   - Tilda form checkbox/cookie plan is approved;
   - one low-risk visual/browser verification path is defined.
5. Before any future static-site publication, add a validation gate for:
   - internal-public text leak scan;
   - schema validity;
   - image references;
   - image sitemap coverage;
   - canonical/sitemap consistency.

## Open Questions

- Should `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site` be renamed/moved or kept as the canonical local Moonn operations worktree?
- Should `PROJECT_CHAT_HISTORY.md` become the root canonical history file in every branch, while `docs/codex-chat-history.md` remains the old imported archive?
- Should the automation `moonn-seo-leftovers-morning-check` keep targeting the old worktree or be updated after a clean canonical repo decision?
- Should Timepad visual cards in `assets/timepad` be copied into `dist`, or are they only source assets for external Timepad/manual upload?

## Verification Performed

- Git status and remote refs checked.
- Current repo files, data registry, generated pages, sitemap, robots and `llms.txt` checked.
- Restore report and session index checked.
- Backup automation checked.
- Old rich worktree existence and key docs checked.
- No browser/live/publication verification was performed because the task is recovery-audit only and explicitly forbids external publication/integration changes.
