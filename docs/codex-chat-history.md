# Codex Chat History

Append-only project history for `moon-psy-site`.

## 2026-05-03 — Paid Video Lectures On `events_tp`

- Project: Moonn / Tilda site.
- Workstream: paid video lectures and protected access.
- Branch: `codex/moonn-paid-video-lectures`.
- User request:
  - convert `https://moonn.ru/events_tp` from a registration/event page into a paid lecture storefront;
  - use price `1300 RUB` per lecture;
  - connect Tilda payment and protected video viewing;
  - use QR code and direct page link for promotion;
  - user approved one test scenario.
- Decisions:
  - Treat `events_tp` as the canonical pilot storefront, not `lectures1`.
  - Use Tilda products/cart plus Members/Courses access after payment.
  - Do not expose raw YouTube links on the public sales page.
  - Do not create or change live T-Bank/Tinkoff payment settings until seller/payment details are visually verified.
  - Use manifest-first rollout so product SKUs, Members groups, videos and QR links stay synchronized.
- Created or changed files:
  - `scripts/tilda_paid_lecture_audit.py`
  - `scripts/build_events_tp_paid_manifest.py`
  - `registry/products/paid-video-lectures-audit-2026-05-03.json`
  - `registry/products/paid-video-lectures.schema.json`
  - `registry/products/paid-video-lectures.manifest.json`
  - `assets/qr/tatyana-munn-paid-lectures-events-tp-qr.png`
  - `docs/paid-video-lectures-tilda-plan-2026-05-03.md`
- Verified:
  - Read-only Tilda API audit completed.
  - `events_tp` Tilda page id is `66814657`.
  - 10 unique Timepad event IDs were extracted from `events_tp`.
  - JSON files are syntactically valid.
  - QR image was generated for `https://moonn.ru/events_tp`.
- Open questions / blockers:
  - Video URL is still needed for each lecture.
  - User clarified that YouTube recordings are private/hidden, so public channel scan is insufficient.
  - YouTube Studio access or an exported owner video list is needed to match videos to lectures.
  - Confirm whether Timepad event `3334362` is a sellable recording or only a series/archive entry.
  - Tilda payment provider must be checked visually; read-only API did not expose active payment details.
  - Before production, run one staging or safe live test purchase and verify post-payment access.
- Risk notes:
  - Money/payment settings, seller requisites and paid content access are high-risk.
  - YouTube unlisted links are not real copy protection; use protected Tilda access as the minimum safe layer.

## 2026-05-03 — Private YouTube Matching For Paid Lectures

- Project: Moonn / Tilda site.
- Workstream: paid video lectures and protected access.
- Branch: `codex/moonn-paid-video-lectures`.
- User request:
  - use owner access to the YouTube channel because recordings are private/hidden;
  - match recordings by title/date to the `events_tp` lecture list;
  - prepare the paid-access rollout without exposing raw private links.
- Decisions:
  - Store private video ids and Studio URLs only in local ignored output, not in Git.
  - Commit only sanitized match status and manifest state.
  - Keep live payment/product creation behind a high-risk gate until Tilda payment provider/seller settings are visually verified.
- Created or changed files:
  - `.gitignore`
  - `registry/products/paid-video-lectures.manifest.json`
  - `registry/products/paid-video-lectures-youtube-match-status-2026-05-03.json`
  - `docs/paid-video-lectures-youtube-matching-status-2026-05-03.md`
  - `docs/paid-video-lectures-tilda-plan-2026-05-03.md`
- Verified:
  - YouTube Studio owner view opened for the correct channel.
  - February-March 2026 lecture recordings were found in Studio.
  - Five lecture mappings are unique enough for a first protected Tilda pilot.
  - Four lecture mappings need owner selection because multiple plausible recordings exist.
- Open questions / blockers:
  - Select the correct duplicate for `2604 Духовная психология`.
  - Select the correct duplicate for `2607 Психология мужчины`.
  - Select the correct `2608 ИИ и ЭИ` recording.
  - Decide whether `Быстрая психология` should sell part 1, part 2, or both as one product.
  - Verify Tilda payment provider and run one approved test purchase.
- Risk notes:
  - Shared credentials and private video links are sensitive; rotate the password after the setup session.
  - Public sales pages must not expose raw private or unlisted YouTube links.

## 2026-05-03 — Live Moonn SEO Metadata Audit

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit.
- Branch: `codex/moonn-seo-audit`.
- Trigger: SEO heartbeat continued safe follow-up work while paid video lectures remain paused.
- User-facing boundary:
  - No Tilda edits were made.
  - No payment/product/private-video changes were made.
- Created files:
  - `docs/moonn-live-seo-metadata-audit-2026-05-03.json`
  - `docs/moonn-live-seo-metadata-audit-2026-05-03.md`
- Verified:
  - 9 priority Moonn URLs return HTTP `200`.
  - All 9 have canonical and `og:image`.
  - Only `https://moonn.ru/psiholog-moskva-online` exposes JSON-LD.
- Findings:
  - 8 of 9 checked pages need page-specific JSON-LD.
  - 5 pages have no detected H1.
  - Main page and depression page have too many detected H1 tags.
  - `events_tp` has a very short generic description.
- Follow-up rule:
  - Next safe SEO step is a per-page Tilda SEO patch packet, not direct live edits: title, description, one-H1 instruction, JSON-LD, canonical confirmation and image/OG note.

## 2026-05-03 — Moonn Tilda SEO Patch Packets

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit.
- Branch: `codex/moonn-seo-audit`.
- Trigger: SEO heartbeat continued from the live metadata audit.
- User-facing boundary:
  - No live Tilda edits were made.
  - No undocumented Tilda endpoints were used.
  - No payment/product/private-video/review-screenshot changes were made.
- Created files:
  - `docs/moonn-tilda-seo-patch-packets-2026-05-03.json`
  - `docs/moonn-tilda-seo-patch-packets-2026-05-03.md`
- Result:
  - Prepared page-specific SEO packets for 9 Moonn priority URLs.
  - Each packet includes proposed title, description, H1, canonical, schema types, image alt pattern and reindex flag.
  - The packets preserve the public entity bridge: `Татьяна Мунн`, `Кумскова Татьяна Михайловна`, МГУ, Moonn, Timepad, MIIIIPS, Yandex Services, MSU Istina and PsyJournals.
- Follow-up rule:
  - Next safe step is generating final JSON-LD code blocks per page, then applying them only through supported Tilda page head/code fields after the safe path is confirmed.

## 2026-05-04 — Moonn Tilda JSON-LD Blocks

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit.
- Branch: `codex/moonn-seo-audit`.
- Trigger: SEO heartbeat continued from the Tilda SEO patch packets.
- User-facing boundary:
  - No live Tilda edits were made.
  - No undocumented Tilda endpoints were used.
  - No review, rating, payment, product or private-video data was added.
- Created files:
  - `docs/moonn-tilda-jsonld-blocks-2026-05-04.json`
  - `docs/moonn-tilda-jsonld-blocks-2026-05-04.md`
- Result:
  - Prepared JSON-LD graph objects for 9 priority Moonn URLs.
  - Connected each page to the same person/entity bridge: Татьяна Мунн / Кумскова Татьяна Михайловна / МГУ / Moonn / Timepad / MIIIIPS / Yandex Services / MSU Istina / PsyJournals.
  - Excluded `Review`, `AggregateRating`, copied reviews, private videos, prices and medical treatment claims by design.
- Follow-up rule:
  - Insert JSON-LD only through supported Tilda page head/code fields, then re-audit live HTML for `application/ld+json` before requesting indexing.

## 2026-05-04 — Yandex Services Review URL Canonicalization

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit / reviews page.
- Branch: `codex/moonn-seo-audit`.
- Trigger: SEO heartbeat final self-check found an old Yandex Services profile slug in the local reviews page data.
- Changed files:
  - `data/site.json`
- Decision:
  - Replace the old review profile URL `TatyanaKumskovamunn-948629` with the canonical redirected profile URL `TatyanaKumskovatatyanamunn-948629`.
  - Do not publish reviews, screenshots, reviewer names, avatars or copied review text.
- Verified:
  - The old Yandex Services profile URL redirects to the canonical URL.
  - `data/site.json` remains valid JSON.
- Follow-up rule:
  - Any future reviews page rollout must use the canonical Yandex Services profile URL and must pass personal-data/platform/legal gates before showing review evidence.

## 2026-05-04 — Final Moonn Sitemap SEO Audit

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit.
- Branch: `codex/moonn-seo-audit`.
- User request:
  - run the final SEO audit for Moonn pages.
- Boundary:
  - Read-only live audit.
  - No Tilda edits, no payment/product/private-video changes, no review publication.
- Created files:
  - `scripts/moonn_final_seo_audit.py`
  - `docs/moonn-final-seo-audit-2026-05-04.json`
  - `docs/moonn-final-seo-audit-2026-05-04.md`
  - `docs/moonn-final-seo-audit-2026-05-04.csv`
  - `docs/moonn-final-seo-action-plan-2026-05-04.md`
- Verified:
  - `https://moonn.ru/sitemap.xml` contains 148 URLs.
  - All 148 checked URLs returned HTTP `200`.
  - `robots.txt` is live and references the sitemap.
- Findings:
  - 98 URLs should be strengthened for SEO.
  - 45 opaque/test URLs should be reviewed for noindex, semantic rename or 301.
  - 5 important psychology URLs are blocked by broad `Disallow: /psiholog`.
  - 139 URLs have no detected JSON-LD.
  - 91 URLs have no detected H1.
  - 52 URLs have duplicate descriptions.
  - 8 URLs have canonical mismatch.
- Incident:
  - Symptom: current `robots.txt` blocks useful `/psiholog...` pages.
  - Root cause: broad legacy disallow rule `Disallow: /psiholog` matches current semantic psychology URLs by prefix.
  - Resolution: recorded as P0 fix; update Tilda/robots settings to block only exact legacy URLs, then retest in GSC/Yandex.
  - Follow-up rule: never add broad robots rules for short commercial prefixes when semantic pages may share the same prefix.

## 2026-05-04 — Corrected Production Scope SEO Audit

- Project: Moonn / Tilda site.
- Workstream: live SEO/AEO audit.
- Branch: `codex/moonn-seo-audit`.
- User correction:
  - The intended audit scope is not every URL in `sitemap.xml`, but the real published production pages we worked with earlier.
- Decision:
  - Treat `output/production-73-rollout-pages.json` plus `output/build-production-83-scope.log` additions as the canonical working scope.
  - Keep the previous 148-URL sitemap audit only as sitemap-hygiene evidence, not as the main production-page SEO scope.
- Created / updated files:
  - `scripts/moonn_final_seo_audit.py`
  - `docs/moonn-production-scope-seo-audit-2026-05-04.json`
  - `docs/moonn-production-scope-seo-audit-2026-05-04.md`
  - `docs/moonn-production-scope-seo-audit-2026-05-04.csv`
  - `docs/moonn-production-scope-seo-action-plan-2026-05-04.md`
- Verified:
  - Corrected scope contains 83 URLs.
  - All 83 URLs return HTTP `200`.
- Findings:
  - 77 URLs need SEO strengthening.
  - 3 real pages are blocked by broad robots rules and need robots fix before strengthening.
  - 2 URLs, `st1` and `st2`, need semantic rename or noindex/redirect decision.
  - 1 legacy `/psiholog` page should stay out of index or be removed/redirected.
  - 82 of 83 scoped pages have no detected JSON-LD.
  - 44 scoped pages have no detected H1.
- Follow-up rule:
  - Future Moonn SEO progress checks must use the production scope file, not the whole Tilda sitemap, unless the task is explicitly sitemap cleanup.

## 2026-05-04 — Moonn Production SEO Strengthening Packets

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to strengthen SEO for the `77` pages from the corrected production scope, then handle the `3` robots-blocked pages.
- Strategic decision:
  - Treat the work as a machine-first Tilda application packet because the documented Tilda API is read/export oriented and does not provide a supported bulk write endpoint for page SEO fields.
  - Do not use undocumented Tilda endpoints for live production edits.
  - Generate per-page title, description, canonical, H1 action, image alt pattern and JSON-LD instead of applying one generic SEO block to all pages.
- Created or changed files:
  - `scripts/build_moonn_production_seo_strengthening_packets.py`
  - `docs/moonn-production-seo-strengthening-packets-2026-05-04.json`
  - `docs/moonn-production-seo-strengthening-packets-2026-05-04.md`
  - `docs/moonn-production-seo-strengthening-packets-2026-05-04.csv`
  - `docs/moonn-robots-fix-packet-2026-05-04.md`
- Results:
  - `77` pages marked `ready_to_apply`.
  - `3` pages marked `apply_after_robots_fix`.
  - CSV validation: `80` rows.
  - Max title length: `68`.
  - Max description length: `158`.
  - No short descriptions and no unfinished description punctuation.
- Robots finding:
  - Live `robots.txt` has broad `Disallow: /psiholog`, which blocks real working URLs:
    - `https://moonn.ru/psiholog-konsultacii-moskva`
    - `https://moonn.ru/psiholog_moskva`
    - `https://moonn.ru/psihology`
- Open questions / blockers:
  - Live Tilda application still requires supported UI editing or another documented write-capable path.
  - Robots change should be applied in Tilda settings and then verified live before applying the three page packets.
- Follow-up rule:
  - For Moonn/Tilda SEO, generate deterministic per-page packets first; apply live changes only through supported Tilda fields, then re-run `python scripts/moonn_final_seo_audit.py --production-scope`.

## 2026-05-04 — Moonn Production SEO Applied Through Tilda UI

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to start live application in the real Google Chrome profile already logged into Tilda, not Playwright or Codex in-app browser.
- Routing:
  - Used visible Google Chrome window with Tilda account `Alexander`.
  - Browser MCP extension was visually enabled but tool transport still returned `Transport closed`; did not switch to Playwright for Tilda.
  - Used supported Tilda page settings UI (`EditPageSettings`) and native save/publish controls; did not use undocumented Tilda write endpoints.
- Created files:
  - `scripts/tilda_page_seo_settings_ui_rollout.py`
  - `docs/moonn-ready-77-live-seo-verification-2026-05-04.json`
  - `docs/moonn-production-80-live-seo-verification-2026-05-04.json`
  - `docs/moonn-production-80-live-seo-rollout-2026-05-04.md`
- Live changes:
  - Applied page-specific `meta_title`, `meta_descr`, `link_canonical`, `nosearch=false`, `meta_nofollow=false` for `77` ready production pages.
  - Published every changed page.
  - Fixed legacy `/psiholog` page robots prefix issue by removing noindex/nofollow and setting canonical to `https://moonn.ru/psiholog-konsultacii-moskva`.
  - Applied the same SEO settings to the `3` formerly robots-blocked production pages.
- Verified:
  - `77/77` ready pages returned HTTP `200` and matched title/description/canonical packets.
  - `robots.txt` no longer contains broad `Disallow: /psiholog`.
  - Final `80/80` production pages returned HTTP `200`.
  - Final `80/80` title, description and canonical matched packets.
  - Final `80/80` are clear of robots blocks.
- Incident:
  - Symptom: first bulk attempt produced false errors after the first page because the next iteration started from the Tilda page editor after publish.
  - Root cause: UI automation did not reset to the canonical project page before each page settings operation.
  - Resolution: updated rollout script to call `ensure_project_page()` before every page settings edit.
  - Follow-up rule: Tilda UI batch automation must reset to a known canonical screen per item before opening settings, saving or publishing.
- Residual work:
  - Source-level H1/H2 cleanup inside Tilda blocks.
  - Source-level image replacement/filename migration in Tilda storage.
  - Review/noindex/rename decision for `st1` and `st2`.
  - Compliant Yandex Services reviews page.
  - Manual profile text synchronization for Yandex Services and MGU Istina.

## 2026-05-06 — Moonn H1/H2 Source Cleanup Pilot

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to finish morning checklist points 2 and 3: final SEO audit and H1/H2 cleanup plan/application on original published pages.
- Created files:
  - `docs/moonn-production-scope-seo-audit-2026-05-06.json`
  - `docs/moonn-production-scope-seo-audit-2026-05-06.md`
  - `docs/moonn-production-scope-seo-audit-2026-05-06.csv`
  - `docs/moonn-h1-h2-source-cleanup-packet-2026-05-06.json`
  - `docs/moonn-h1-h2-source-cleanup-packet-2026-05-06.md`
  - `docs/moonn-h1-h2-block-map-2026-05-06.json`
  - `docs/moonn-h1-h2-block-map-2026-05-06.md`
  - `docs/moonn-h1-h2-ui-apply-plan-2026-05-06.json`
  - `docs/moonn-h1-h2-ui-apply-plan-2026-05-06.md`
  - `docs/moonn-h1-h2-ui-apply-report-2026-05-06.json`
  - `docs/moonn-h1-h2-capability-buckets-2026-05-06.json`
  - `docs/moonn-h1-h2-capability-buckets-2026-05-06.md`
  - `docs/moonn-h1-h2-implementation-status-2026-05-06.md`
  - `scripts/build_moonn_h1_h2_block_map.py`
  - `scripts/build_moonn_h1_h2_ui_apply_plan.py`
  - `scripts/build_moonn_h1_h2_capability_buckets.py`
  - `scripts/tilda_h1_h2_gui_apply.py`
- Live change:
  - Applied `SEO: тег для заголовка -> H1` to `https://moonn.ru/aromatherapy`, page `62470081`, record `860030752`, block type `485`.
- Verified:
  - Live production audit after the pilot: `83/83` URLs returned HTTP `200`.
  - `missing_h1` decreased from `44` to `43`.
  - `multiple_h1` remains `14`.
  - Capability buckets: `1` supported block-setting action, `24` unsupported actions needing design solution, `27` manual-verify actions.
- Incident:
  - Symptom: automation initially tried to operate on the wrong Chrome tab / Codex window and later failed on several blocks.
  - Root cause: GUI automation was not pinned to the authenticated Tilda tab strongly enough, and the initial plan assumed all Tilda blocks expose the same heading-tag UI field.
  - Resolution: switched navigation to the real Chrome address-bar control and verified block capability visually. Found that block type `485` supports the SEO heading tag field, while tested block types `18` and `578` do not expose it.
  - Follow-up rule: H1/H2 cleanup must be bucketed by proven Tilda block capability. Do not batch-apply SEO heading tags to block types until one record of that type has been verified in Tilda UI.
- Residual work:
  - Rebuild H1/H2 plan into `supported_block_setting`, `unsupported_needs_design_solution`, and `manual_verify`.
  - For unsupported missing-H1 pages, choose a supported design-level solution: add a semantic H1 block or replace the hero/title block type.
  - For multiple-H1 pages, test each secondary heading block type before live batch changes.

## 2026-05-07 — Moonn Scoped H1/H2 Publish Follow-Up

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to continue from the stopped point and avoid publishing all Tilda pages; target scope is the original published Moonn work set, not all `164` project pages.
- Created/updated files:
  - `scripts/tilda_publish_moonn_seo_scope_ui.py`
  - `docs/moonn-seo-scope-publish-report-2026-05-07.json`
  - `docs/moonn-extra-live-pages-publish-report-2026-05-07.json`
- Actions:
  - Verified that live `moonn.ru` still served semantic heading layer `@9483a34`, not final `@1e53aae`.
  - Verified that live global HEAD still had broken Yandex.Metrika JavaScript (`m[i]=m[i]function...`) after earlier UI attempts.
  - Saved corrected global HEAD in the Tilda global HEAD editor and confirmed the editor value after reload contained `@1e53aae` and valid `m[i]=m[i]||function`.
  - Published only the scoped `80` SEO packet pages through Tilda UI.
  - Published `3` extra live pages through Tilda UI: `/psiholog`, `/st1`, `/st2`.
- Verification:
  - Tilda UI publish reports marked `80/80` scoped pages and `3/3` extra live pages as published.
  - Live/API HTML verification still returned old global HEAD `@9483a34` and broken Metrika. The global HEAD change did not propagate to public HTML through scoped page publishing.
  - A one-page page-level HEAD pilot on `/` also did not persist into Tilda API/published HTML when changed through UIA field value alone.
- Incident:
  - Symptom: Tilda editor UI can display corrected HEAD after reload, while public HTML and Tilda API still return the old published HEAD.
  - Root cause: UIA `set_edit_text`/accessibility-field edits can update the visible Ace editor value without reliably updating Tilda's underlying Ace/editor model submitted to the server.
  - Resolution so far: stopped before claiming completion or using publish-all. Scoped publish report was recorded; live result remains old.
  - Follow-up rule: for Tilda Ace editors, do not treat UIA field value as proof. The readiness gate is: persisted server value or published HTML/API contains the expected marker. If only publish-all can propagate global HEAD, get explicit approval because it may touch non-target project pages.
- Residual work:
  - Continue H1/H2 completion only after choosing a safe Tilda-supported write path: real Ace keyboard editing verified by API, supported Tilda UI field per page/block, or explicit approval for project-level publish-all if it is confirmed to publish only already-public pages.
  - Re-run `python scripts\moonn_rendered_heading_audit.py` only after live HTML contains `@1e53aae`.

## 2026-05-07 — Moonn Tilda Folder Governance Inventory

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user approved the stronger Tilda folder governance path before global HEAD publish: move test/draft pages into archive folders, then use Tilda's supported folder-aware publish flow.
- Verified external rule:
  - Tilda Help says pages can be moved to folders through drag-and-drop or Page Settings → Additional.
  - Tilda Help says folders can be marked as archive, and archived folders are excluded from publish-all/folder publish flows.
- Created files:
  - `docs/moonn-tilda-page-governance-inventory-2026-05-07.json`
  - `docs/moonn-tilda-page-governance-inventory-2026-05-07.md`
- Read-only inventory:
  - Official Tilda API `getpageslist` returned `164` project pages.
  - `83` pages are protected work scope and must remain publishable.
  - `8` pages are clear archive candidates by title/alias: tests, copies, old teen-camp pages.
  - `73` pages are published outside the current SEO scope and require human/content classification before moving; they include legal pages, payment success pages, news, old SEO landing pages, code/media holder pages and no-alias article pages.
- UI finding:
  - The real Alexander Chrome/Tilda session opened the Moonn project and existing folder `ТЕСТЫ для АЛЕКС МАРК` (`folderid=2421516`).
  - The project currently shows a Tilda subscription-expired banner: "Пожалуйста, оплатите подписку / Время истекло".
  - Folder settings button did not open a settings dialog during this check, likely because project management is restricted while the subscription is expired.
- Decision:
  - Do not move `73` published outside-scope pages automatically. Several are legitimate public/legal/payment pages.
  - Do not run project publish-all until archive-folder settings are confirmed and the excluded folder set is verified.
- Follow-up rule:
  - For Tilda global HEAD rollout, the required safety gate is: protected work-scope list, archive-candidate list, folder archive state verified in UI, then controlled publish. If subscription is expired or folder settings cannot be opened, stop and record blocker instead of forcing a broad publish.

## 2026-05-08 — Moonn Post-Payment Tilda HEAD Rollout Verification

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user paid Tilda Business and asked whether the unpaid subscription caused previous changes not to appear.
- Context:
  - Tilda Business is paid through `2026-06-08`; project controls are available again.
  - The real Alexander Google Chrome/Tilda session was used. OBS was minimized after it interfered with visible desktop coordinates.
- Actions:
  - Rechecked live HTML after payment: protected URLs still served old global HEAD `@9483a34` and broken Yandex.Metrika before publication.
  - Verified the Tilda global HEAD editor persisted the corrected code after navigating away and back:
    - semantic heading layer `@1e53aae`;
    - valid Yandex.Metrika snippet with `m[i]=m[i]||function`.
  - Published a one-page pilot (`/`) through supported Tilda UI and confirmed live HTML switched to `@1e53aae`.
  - Published the remaining scoped `80/80` SEO packet pages through `scripts/tilda_publish_moonn_seo_scope_ui.py`.
  - Published `3/3` extra live pages through Tilda UI: `/psiholog`, `/st1`, `/st2`.
- Changed files:
  - `docs/moonn-seo-scope-publish-report-2026-05-07.json`
  - `docs/moonn-extra-live-pages-publish-report-2026-05-07.json`
  - `docs/moonn-rendered-heading-audit-2026-05-06.json`
  - `docs/moonn-rendered-heading-audit-2026-05-06.md`
  - `docs/moonn-rendered-heading-audit-2026-05-06.csv`
  - `docs/moonn-production-scope-seo-audit-2026-05-07.json`
  - `docs/moonn-production-scope-seo-audit-2026-05-07.md`
  - `docs/moonn-production-scope-seo-audit-2026-05-07.csv`
- Verification:
  - Live HTML spot checks for `/`, `/emotional-intelligence/knowledge-base/empathy`, `/events_tp`, `/psiholog-konsultacii-moskva`, `/psiholog`, `/st1`, `/st2` all returned:
    - `@1e53aae`: true;
    - `@9483a34`: false;
    - `m[i]=m[i]||function`: true.
  - `python scripts\moonn_rendered_heading_audit.py`:
    - `83/83` pages loaded;
    - `83/83` pages have semantic layer script;
    - `83/83` pages have exactly one rendered H1;
    - `0` missing H1;
    - `0` multiple H1;
    - `52/52` target H1/H2 checks matched;
    - `0` errors.
  - `python scripts\moonn_final_seo_audit.py --production-scope`:
    - `83/83` URLs returned HTTP `200`;
    - raw HTML audit still flags `missing_h1`/`multiple_h1` because this audit does not execute the semantic heading JS layer.
- Decision:
  - Payment was a blocker for management access, but it was not the only reason changes did not appear. The actual live rollout required supported Tilda save plus scoped page publication.
  - H1/H2 readiness should now be judged by rendered audit, not raw HTML audit alone, because the implemented solution is a global semantic JS layer.
- Incident rule:
  - When Tilda global HEAD changes are used, the readiness gate is three-stage: persisted editor value after navigation, scoped published live HTML marker, rendered browser audit.
  - Do not treat raw HTML H1/H2 findings as final when the chosen implementation is a rendered semantic layer; pair raw audits with rendered audits and explicitly label the difference.
- Residual work:
  - Folder/archive governance remains open: only `8` clear archive candidates can be considered for archive movement; `73` outside-scope published pages need content classification before moving.
  - SEO image alt/title and JSON-LD work remain separate follow-ups; current turn closed the HEAD/H1-H2 rollout.
