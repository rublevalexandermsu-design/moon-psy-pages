# Moonn Chat Restore Prompts - 2026-05-09

Use this file to recreate Moonn project chats after Codex reinstall.

Workflow:

1. Create a new Codex chat in the Moonn project/workspace.
2. Rename the chat exactly as shown in the `Chat name` line.
3. Paste the corresponding prompt.
4. Let the new chat read the referenced recovery files before doing any work.
5. Do not paste secrets, tokens, passwords, payment data or private video links into the prompt.

Core recovery files for every restored chat:

- `C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md`
- `C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md`
- `C:\пайто н тесты\moon-psy-pages\PROJECT_CHAT_HISTORY.md`
- `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md`

## Prompt 1 - Early Tilda Access

Chat name:

`Найти способ доступа в Тильду`

Prompt:

```text
Ты восстанавливаешь старый Moonn/Tilda-чат после переустановки Codex.

Контур: Moonn / Tilda access recovery.
Старый thread id: 019cc87d-9e44-78f0-be29-3683890d2b92.
Рабочее правило: это чат только про безопасное восстановление доступа, маршрута входа и структуры Tilda, не про публикацию и не про правки сайта.

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Если нужен raw-архив, используй только metadata/session_index сначала:
- C:\Users\yanta\.codex_backup\session_index.jsonl

Границы:
- не проси и не записывай пароли, секреты, cookies, token values;
- не меняй Tilda, Timepad, GitHub Pages, API и формы без отдельного явного разрешения;
- не публикуй сайт;
- не выполняй payment/legal/publication действия.

Твоя задача в этом чате:
1. восстановить карту доступа к Tilda без секретов;
2. найти, какие repo/worktree/branch связаны с Tilda;
3. назвать безопасный следующий шаг для доступа или аудита;
4. если находишь повторяемое правило, записать его в PROJECT_CHAT_HISTORY или предложить registry update.
```

## Prompt 2 - Tatyana Moonn Activity Research

Chat name:

`Изучи деятельность Татьяны Мун`

Prompt:

```text
Ты восстанавливаешь старый исследовательский чат по Татьяне Мунн после переустановки Codex.

Контур: Moonn / Tatyana Moonn entity research.
Старый thread id: 019ce137-4454-7720-b375-5d704bafc014.
Назначение чата: биография, деятельность, публичные факты, экспертное позиционирование, provenance для SEO/schema/public pages.

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Если нужен raw/thread context, ищи thread id 019ce137-4454-7720-b375-5d704bafc014 в:
- C:\Users\yanta\.codex_backup\session_index.jsonl
- C:\Users\yanta\.codex_backup\sessions
- C:\Users\yanta\.codex_backup\archived_sessions

Границы:
- не выдавай непроверенные факты как подтвержденные;
- для современных публичных фактов сначала проверяй источники;
- не публикуй страницу и не меняй Tilda/Timepad/API;
- отделяй публичный текст от internal rationale и маркетинговых токенов.

Твоя задача в этом чате:
1. собрать проверенную entity-карту Татьяны Мунн;
2. разделить verified facts, assumptions и recommendations;
3. определить, какие факты можно использовать в schema.org, SEO, Timepad, Yandex Services и публичных текстах;
4. отметить, какие факты требуют повторной проверки перед публикацией.
```

## Prompt 3 - Public Links / Entity Discovery

Chat name:

`Ищи публичные ссылки Татьяны Мунн`

Prompt:

```text
Ты восстанавливаешь старый чат по поиску публичных ссылок Татьяны Мунн.

Контур: Moonn / public links / entity bridge.
Старый thread id: 019d1ffb-aaca-7083-b0db-9262f963bcd0.
Назначение чата: найти и поддерживать проверенный список публичных профилей, страниц, выступлений, Timepad/Yandex/МГУ/Истина/прочих источников для SEO, schema.org и продвижения.

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Если нужен raw/thread context, ищи thread id 019d1ffb-aaca-7083-b0db-9262f963bcd0 в backup index и sessions.

Границы:
- публичные ссылки и статусы могут устареть, поэтому проверяй интернет перед использованием;
- не добавляй внешние домены в legal/privacy/schema как owned без проверки ownership/control;
- не публикуй и не меняй внешние профили.

Твоя задача в этом чате:
1. восстановить список публичных источников Татьяны Мунн;
2. для каждой ссылки указать provenance: источник, дата проверки, где используется, downstream files/pages;
3. классифицировать ссылки: canonical, supporting, unverified, do-not-use;
4. предложить registry format для постоянного хранения entity links.
```

## Prompt 4 - Yandex / Timepad / Promotion / School / Site

Chat name:

`яндекс Тани, таймпад-агент/школа/Сайт.продвижение`

Prompt:

```text
Ты восстанавливаешь главный Moonn-чат по Яндекс Услугам, Timepad, продвижению, школе и сайту.

Контур: Moonn / Yandex Services / Timepad / promotion / school / site.
Старый thread id: 019dafdf-b8d6-7c02-b267-7e5e50ed8b7b.
Этот thread переименовывался. Его известные имена:
- Проанализировать профиль Татьяны
- яндекс Тани, таймпад и продвижение Тани
- яндекс Тани, таймпад/Сайт.продвижение
- яндекс Тани, таймпад/школа/Сайт.продвижение
- яндекс Тани, таймпад-агент/школа/Сайт.продвижение

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\PROJECT_CHAT_HISTORY.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Raw archive path if exact old detail is needed:
- C:\Users\yanta\.codex_backup\sessions\2026\04\21\rollout-2026-04-21T14-49-28-019dafdf-b8d6-7c02-b267-7e5e50ed8b7b.jsonl

Рабочая логика:
- не начинай с нуля;
- этот чат отвечает за полный маршрут: профиль/источник -> Timepad/мероприятия -> визуалы -> сайт -> SEO/schema -> legal/publication gate -> проверка;
- различай current static repo C:\пайто н тесты\moon-psy-pages и rich Tilda worktree C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site.

Границы:
- не публикуй сайт;
- не меняй Tilda/Timepad/Yandex Services/API;
- не отправляй формы;
- не используй накрутку отзывов или искусственную активность;
- не публикуй отзывы, имена, скриншоты или персональные данные без legal/platform gate.

Твоя задача в этом чате:
1. восстановить карту Яндекс Услуги / Timepad / школа / сайт / продвижение;
2. найти уже существующие rules, reports, assets и branches;
3. предложить следующий безопасный recovery-step;
4. если задача касается мероприятия или публичной страницы, требовать manifest -> registry -> publication gate -> verification.
```

## Prompt 5 - Tilda API Setup

Chat name:

`Подключить API к Tilda`

Prompt:

```text
Ты восстанавливаешь главный Moonn-чат по подключению Tilda API.

Контур: Moonn / Tilda API / snapshots / staging / runtime guardrails.
Старый thread id: 019de2b9-84d4-7ff2-938d-7b278d021c9b.
Известные названия:
- Подключить API к Tilda
- тут будем подключать аппи к тильде к сайту-moonn.ru

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Проверь ветки и файлы:
- origin/codex/tilda-api-sync
- docs/tilda-api-staging.md
- docs/tilda-radiant-sanctuary.md
- registry/tilda/moonn-staging-page-map.json
- scripts/tilda_sync_snapshot.py

Raw archive path if exact old detail is needed:
- C:\Users\yanta\.codex_backup\sessions\2026\05\01\rollout-2026-05-01T11-48-22-019de2b9-84d4-7ff2-938d-7b278d021c9b.jsonl

Safety:
- never print or store Tilda secret values;
- only variable names are allowed: TILDA_PUBLIC_KEY, TILDA_SECRET_KEY, TILDA_API_BASE_URL, TILDA_PROJECT_ID;
- do not call write endpoints unless explicitly approved;
- do not use undocumented Tilda write endpoints;
- do not publish live Tilda pages without explicit gate.

Твоя задача в этом чате:
1. восстановить безопасную Tilda API architecture;
2. проверить .gitignore/runtime-secret guardrails;
3. отличить read-only snapshots от live UI/API changes;
4. предложить next step через documented/read-only API first.
```

## Prompt 6 - Newer Tilda API / Moonn Reconnect

Chat name:

`тут будем подключать аппи к тильде к сайту-moonn.ru`

Prompt:

```text
Ты восстанавливаешь newer reconnect чат по Moonn/Tilda API после переустановки Codex.

Контур: Moonn / post-reinstall Tilda API reconnect.
Thread id from backup state: 019e0b74-78f5-7802-8067-e99870f94306.
Связанный старый главный Tilda API thread: 019de2b9-84d4-7ff2-938d-7b278d021c9b.

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Raw evidence if needed:
- C:\Users\yanta\.codex_backup\archived_sessions\rollout-2026-05-09T09-37-23-019e0b74-78f5-7802-8067-e99870f94306.jsonl

Границы:
- этот чат не заменяет старый Tilda API thread, а связывает post-reinstall recovery с ним;
- не читай/не печатай секреты;
- не меняй persistent runtime, Tilda, GitHub Pages или внешние интеграции без gate.

Твоя задача в этом чате:
1. понять, что было восстановлено после переустановки Codex;
2. сопоставить новый reconnect thread со старым thread 019de2b9;
3. определить, какие артефакты уже есть в repo и backup;
4. предложить, какие recovery files надо читать в future Tilda API tasks.
```

## Prompt 7 - Current Recovery Coordination

Chat name:

`Восстановить контур Moonn`

Prompt:

```text
Ты координируешь текущий recovery-контур Moonn после переустановки Codex.

Контур: Moonn / context recovery / chat restoration.
Связанные current recovery thread ids:
- 019e0d01-5134-7152-8cd5-a15eeafbe01b - Восстановить контур Moonn
- 019e0d0e-d874-7260-9589-c49dcb016055 - Найти историю чата Moon
- 019e0d16-5686-7942-8658-5d1a39aa1391 - Найти репозиторий чатов Moonn / Подключить API к Tilda
- 019e0d26-421a-7cb3-b9bc-fe9b1381a955 - Яндекс Тани, Timepad, агент/школа/сайт

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\PROJECT_CHAT_HISTORY.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-restore-prompts-2026-05-09.md

Главное правило:
- не решай продуктовые задачи в этом чате, если они относятся к отдельному workstream;
- маршрутизируй их в правильный восстановленный чат: Tilda API, Яндекс/Timepad, SEO, privacy/RKN, paid lectures, teen camp.

Твоя задача:
1. поддерживать карту чатов и восстановленных workstream;
2. обновлять PROJECT_CHAT_HISTORY.md после значимых recovery steps;
3. предлагать, какой новый чат/ветку использовать для каждой следующей задачи;
4. не публиковать и не менять внешние системы.
```

## Prompt 8 - Moonn SEO / Tilda Production Audit

Chat name:

`Moonn SEO / Tilda production audit`

Prompt:

```text
Ты восстанавливаешь Moonn SEO/Tilda production audit чат из старого project history.

Контур: Moonn / SEO / schema / Tilda production pages / GSC/Yandex.
Основной старый worktree:
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site
Основная старая ветка:
- codex/moonn-seo-audit

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Особенно найди записи:
- Live Moonn SEO Metadata Audit
- Moonn Tilda SEO Patch Packets
- Moonn Tilda JSON-LD Blocks
- Final Moonn Sitemap SEO Audit
- Corrected Production Scope SEO Audit
- Moonn Production SEO Strengthening Packets
- Moonn Production SEO Applied Through Tilda UI
- Moonn H1/H2 Source Cleanup Pilot
- Moonn JSON-LD Schema Rollout And Archive Packet
- Moonn GSC/Yandex Reindex Submission
- Moonn Manual Google URL Inspection Priority Requests

Границы:
- не публикуй Tilda без explicit approval;
- не повторяй массовую отправку 83 URLs в Google URL Inspection;
- работай от production scope, а не от всего sitemap, если задача не про sitemap cleanup;
- отделяй raw HTML audit, rendered DOM audit и indexing status.

Твоя задача:
1. восстановить SEO/sitemap/schema/H1/H2 status;
2. использовать существующие reports прежде чем запускать новый audit;
3. предложить следующий safe SEO step;
4. если нужен live check, сначала назвать risk и verification plan.
```

## Prompt 9 - Moonn Privacy / RKN / Forms

Chat name:

`Moonn RKN privacy compliance`

Prompt:

```text
Ты восстанавливаешь Moonn privacy/RKN/forms compliance чат.

Контур: Moonn / legal-publication gate / privacy / cookies / forms / RKN.
Основной старый worktree:
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site
Старая рабочая ветка была связана с codex/moonn-seo-audit, но future work лучше вести в отдельном privacy/legal workstream.

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Особенно найди записи:
- Moonn RKN/Privacy Compliance Intake
- Moonn Privacy Compliance Packet and Audit Script
- Moonn Privacy Operator Details Filled
- Incident: Wrong External Domain Added To Privacy Packet
- Moonn RKN/Privacy Layer Published And Verified
- Moonn Native Policy Source Hardening

Границы:
- legal/publication changes are high-risk;
- не публикуй legal text, не отправляй RKN notification, не меняй forms/cookies/live Tilda без explicit approval;
- не добавляй external domains в legal docs без ownership/control verification;
- проверяй rendered browser и raw HTML отдельно.

Твоя задача:
1. восстановить status privacy/RKN/forms/cookies;
2. проверить старые reports before new action;
3. зафиксировать blockers and missing operator/legal facts;
4. предлагать только безопасные reversible next steps until approval.
```

## Prompt 10 - Paid Lectures / YouTube / Payment

Chat name:

`Moonn paid lectures and protected access`

Prompt:

```text
Ты восстанавливаешь чат по платным лекциям Moonn, YouTube matching, Tilda payment и protected access.

Контур: Moonn / paid lectures / events_tp / Tilda payment / protected video access.
Старая ветка:
- codex/moonn-paid-video-lectures
Старый operational summary:
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Особенно найди записи:
- Paid Video Lectures On events_tp
- Private YouTube Matching For Paid Lectures
- Moonn Post-Payment Tilda HEAD Rollout Verification

Границы:
- payment, seller details, private videos and access control are high-risk;
- не вводи card details, не отправляй оплату, не публикуй private video links;
- private YouTube ids/Studio URLs хранить только в ignored local output, не в Git;
- live payment provider tests only with explicit approval.

Твоя задача:
1. восстановить manifest/status платных лекций;
2. найти blockers: видео, duplicate recordings, Tilda payment provider, protected access;
3. предложить safe next test that does not charge money;
4. вести manifest-first approach: products -> videos -> access groups -> page -> verification.
```

## Prompt 11 - Teen Psychology Camp / Timepad School

Chat name:

`Moonn teen psychology camp / Timepad school`

Prompt:

```text
Ты восстанавливаешь чат по подростковому лагерю/школе, Timepad visual assets, homepage banner and payment CTA.

Контур: Moonn / teen psychology camp / Timepad school / Tilda landing / payment CTA.
Связанные branches:
- origin/codex/timepad-school-moderation-russian-assets
- origin/codex/timepad-school-poster-replacement
- codex/moonn-seo-audit in old rich worktree

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\codex-chat-history.md

Особенно найди записи:
- Moonn Teen Psychology Camp Page Publication
- Moonn Teen Camp Homepage Banner Completed
- Moonn Teen Camp Payment CTA Completed

Проверь local assets:
- C:\пайто н тесты\moon-psy-pages\assets\teen-softskills
- C:\пайто н тесты\moon-psy-pages\assets\timepad\visuals\tatyana-munn
- C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site\docs\teen-psychology-camp-2026

Границы:
- не публикуй Tilda/Timepad;
- не отправляй платежи;
- не меняй external integrations без gate;
- для публичных страниц проверяй legal/publication gate, links, PDF, Telegram, schema, images and rendered result.

Твоя задача:
1. восстановить status teen camp landing, homepage banner, Timepad assets and payment CTA;
2. определить, какие screenshots/untracked files нужно сохранить;
3. предложить safe next verification step;
4. не смешивать camp workstream with general SEO or Tilda API unless explicitly needed.
```

## Prompt 12 - Moonn Chat Registry / Memory Compression

Chat name:

`Moonn chat registry and compressed memory`

Prompt:

```text
Ты восстанавливаешь и развиваешь системную память Moonn-проекта.

Контур: Moonn / chat registry / compressed context / project memory.
Текущая recovery ветка:
- codex/moonn-context-recovery

Сначала прочитай:
- C:\пайто н тесты\moon-psy-pages\PROJECT_CHAT_HISTORY.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-recovery-audit-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-recovery-index-2026-05-09.md
- C:\пайто н тесты\moon-psy-pages\docs\moonn-chat-restore-prompts-2026-05-09.md

Цель:
создать machine-first memory layer so future Codex sessions do not reread 800MB-1GB raw chats.

Рекомендуемая структура:
- registry/codex_context/moonn/raw-session-map.json
- registry/codex_context/moonn/compressed-chat-index.json
- registry/codex_context/moonn/project-memory.md
- registry/codex_context/moonn/incident-ledger.md
- registry/codex_context/moonn/open-questions.md

Границы:
- не копируй полные raw chats в Git;
- не записывай secrets, private video links, cookies, passwords, credential file paths;
- не смешивай Moonn memory with АНО/EI/grants memory unless adding cross-project links explicitly.

Твоя задача:
1. сделать schema-first compressed context plan;
2. создать minimal prototype registry files;
3. backfill only summaries, thread ids, dates, raw paths, branches, decisions, incidents and open questions;
4. проверить secret/localhost/path leakage before commit.
```
