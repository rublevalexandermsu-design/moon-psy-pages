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

## 2026-05-08 — Moonn JSON-LD Schema Rollout And Archive Packet

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Commit: `0148735` (`Roll out Moonn JSON-LD schema layer`).
- Trigger: user asked to finish JSON-LD/schema and careful Tilda folder/archive cleanup before moving to GSC/Yandex reindexing, Yandex Services reviews and Yandex Services/MSU Istina synchronization.
- Actions:
  - Created a global rendered JSON-LD schema layer for the `83` Moonn production-scope URLs.
  - Added a global entity schema in Tilda HEAD for `Person`/`WebSite` linking Tatyana Moonn, Kumskova identity, Moonn and external entity signals.
  - Saved the updated Tilda global HEAD through the real authenticated Alexander Google Chrome session.
  - Published only the scoped `80/80` SEO packet pages, then the `3/3` extra live pages: `/psiholog`, `/st1`, `/st2`.
  - Created a rendered schema audit so JSON-LD readiness is checked in the same rendered layer as the semantic H1/H2 fix.
  - Created a Tilda archive execution packet for exactly `8` clear archive candidates.
- Changed files:
  - `assets/moonn-schema-layer.js`
  - `scripts/build_moonn_schema_layer.py`
  - `scripts/moonn_rendered_schema_audit.py`
  - `scripts/tilda_publish_moonn_extra_live_pages_ui.py`
  - `scripts/build_moonn_tilda_archive_execution_packet.py`
  - `docs/moonn-global-head-code-with-schema-2026-05-08.html`
  - `docs/moonn-schema-layer-packet-2026-05-08.json`
  - `docs/moonn-schema-layer-packet-2026-05-08.md`
  - `docs/moonn-rendered-schema-audit-2026-05-08.json`
  - `docs/moonn-rendered-schema-audit-2026-05-08.md`
  - `docs/moonn-rendered-schema-audit-2026-05-08.csv`
  - `docs/moonn-tilda-archive-execution-packet-2026-05-08.json`
  - `docs/moonn-tilda-archive-execution-packet-2026-05-08.md`
  - `docs/moonn-tilda-archive-execution-packet-2026-05-08.csv`
- Verification:
  - `node --check assets\moonn-schema-layer.js` passed.
  - Live HTML spot checks for `/`, `/emotional-intelligence/knowledge-base/empathy`, `/events_tp`, `/psiholog-konsultacii-moskva`, `/psiholog`, `/st1`, `/st2` all returned:
    - `moonn-global-entity-schema`: true;
    - `moonn-schema-layer`: true;
    - schema commit marker `0e5967eaa5d2fcca54900772ff632f91f090f073`: true;
    - `application/ld+json`: true.
  - `python scripts\moonn_rendered_schema_audit.py`:
    - `83/83` URLs HTTP `200`;
    - `83/83` have schema layer script;
    - `83/83` have global entity schema;
    - `83/83` have JSON-LD;
    - `83/83` have `Person`, `WebSite`, `WebPage`, `BreadcrumbList`;
    - `0` JSON errors;
    - `0` page errors.
  - `python scripts\moonn_rendered_heading_audit.py` remains green:
    - `83/83` loaded;
    - `83/83` have exactly one rendered H1;
    - `52/52` target H1/H2 checks matched.
- Folder/archive decision:
  - Official Tilda folder documentation says an Archive Folder is excluded from “Publish all pages”; source recorded in the execution packet: `https://help.tilda.cc/folders`.
  - Live movement was not executed in this step because the safe gate still requires confirming the destination folder in Tilda UI as an Archive Folder.
  - Only the `8` clear candidates in `docs/moonn-tilda-archive-execution-packet-2026-05-08.json` are ready for possible movement. Legal, payment, reviews, news/event, media-holder and ambiguous pages remain protected from automatic movement.
- Incident rule:
  - For Tilda SEO retrofits, distinguish three audit layers: raw HTML, rendered DOM, and search-console indexing state. A raw audit can correctly flag source HTML limitations while rendered audits verify JS-layer remediation.
- Residual work:
  - Execute archive-folder movement only after UI confirmation that the destination folder is an Archive Folder.
  - Image `alt` issues remain in the raw audit and should be handled through supported Tilda image/block fields or a separate image replacement workflow.
  - GSC/Yandex reindexing can start for the 83 production URLs after this schema rollout verification.

## 2026-05-08 — Moonn GSC/Yandex Reindex Submission

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to do GSC/Yandex reindexing for the 83 Moonn production URLs after JSON-LD/schema rollout.
- Actions:
  - Built a reindexing packet for all `83` production-scope URLs:
    - `docs/moonn-gsc-yandex-reindex-packet-2026-05-08.json`
    - `docs/moonn-yandex-reindex-urls-2026-05-08.txt`
    - `docs/moonn-google-priority-indexing-urls-2026-05-08.txt`
  - Verified live `https://moonn.ru/sitemap.xml` has `149` URL entries and includes all `83/83` production-scope URLs.
  - Submitted `sitemap.xml` in Google Search Console for property `https://moonn.ru/`.
  - Submitted all `83` URLs in Yandex Webmaster via `Индексирование -> Переобход страниц`.
- Verification:
  - Google Search Console UI showed `Sitemap submitted successfully`.
  - Yandex Webmaster showed daily limit `470` before submission and `387` remaining after submission, matching `83` submitted URLs.
  - Yandex UI cleared the textarea and showed the submitted-pages section after send.
- Changed files:
  - `docs/moonn-gsc-yandex-reindex-packet-2026-05-08.json`
  - `docs/moonn-yandex-reindex-urls-2026-05-08.txt`
  - `docs/moonn-google-priority-indexing-urls-2026-05-08.txt`
  - `docs/moonn-gsc-yandex-reindex-report-2026-05-08.json`
  - `docs/moonn-gsc-yandex-reindex-report-2026-05-08.md`
- Decision:
  - Google bulk reindexing was handled through sitemap submission, not 83 individual URL Inspection requests, because Google documentation recommends sitemap for multiple URLs and quota-limits individual indexing requests.
  - Yandex supports bulk URL submission in the Reindex Pages tool and accepted the full 83-URL packet within the visible daily quota.
- Sources:
  - Google recrawl documentation: `https://developers.google.com/search/docs/advanced/crawling/ask-google-to-recrawl`
  - Google Search Console help: `https://support.google.com/webmasters/answer/10351509`
  - Yandex reindex documentation: `https://yandex.ru/support/webmaster/ru/robot-workings/site-reindex`
  - Yandex Webmaster quotas: `https://yandex.ru/support/webmaster/ru/indexing-options/quotas`
- Follow-up rule:
  - Do not keep resubmitting the same URLs every day. First check Yandex statuses after several days and repeat only failed URLs. In Google, check sitemap last-read and Pages indexing; use URL Inspection only for priority URLs if key pages stay stale.

## 2026-05-08 — Moonn Manual Google URL Inspection Priority Requests

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to try Google manually after sitemap submission and add Google status checks to the follow-up automation.
- Actions:
  - Used the real Google Chrome profile with the already-authenticated Alexander Rublev Google account.
  - Opened Google Search Console URL Inspection for property `https://moonn.ru/`.
  - Manually requested indexing for priority URLs:
    - `https://moonn.ru/`
    - `https://moonn.ru/events_tp`
    - `https://moonn.ru/lectures1`
    - `https://moonn.ru/psiholog-konsultacii-moskva`
  - Updated:
    - `docs/moonn-gsc-yandex-reindex-report-2026-05-08.json`
    - `docs/moonn-gsc-yandex-reindex-report-2026-05-08.md`
- Verification:
  - GSC showed `Indexing requested` for all four priority URLs.
  - For `/events_tp`, GSC showed the important pre-request status: `Page is not indexed: Discovered - currently not indexed`.
  - For `/`, `/lectures1`, and `/psiholog-konsultacii-moskva`, GSC showed the pages as already indexed before the manual request.
- Decision:
  - Do not manually submit all `83` URLs through URL Inspection because it is quota-limited and Google recommends sitemap submission for bulk recrawling.
  - The next check must include Google sitemap last-read, Pages indexing, and URL Inspection statuses for the four manually requested priority URLs.

## 2026-05-08 — Moonn RKN/Privacy Compliance Intake

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user raised Roskomnadzor personal-data/cookie/form-policy scanner risk and asked whether bot access can be limited.
- Actions:
  - Checked live standard policy endpoints:
    - `/privacy`: `404`
    - `/policy`: `404`
    - `/personal-data`: `404`
    - `/soglasie`: `404`
  - Checked `https://moonn.ru/robots.txt`: `200`.
  - Checked main page signals: Yandex Metrika `96397286` active with clickmap/trackLinks/Webvisor; no Google Analytics signal found in the sampled main HTML.
  - Created audit artifact:
    - `docs/moonn-rkn-privacy-compliance-audit-2026-05-08.md`
- Decision:
  - Treat privacy/RKN compliance as a separate legal/privacy workstream, not as an SEO subtask.
  - Do not try to hide non-compliance from RKN bots. First publish correct documents and form consents, then add conservative bot-control for non-essential AI/scraper bots.
- Blockers:
  - Need confirmed legal operator details and whether an RKN operator notification already exists.
  - Need legal approval before publishing final policy/consent wording.

## 2026-05-08 — Moonn Privacy Compliance Packet and Audit Script

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to execute the first compliance steps: documents, form consents, cookies/analytics notice, and automation; RKN operator notification excluded for now.
- Actions:
  - Created publication packet:
    - `docs/moonn-privacy-publication-packet-2026-05-08.md`
  - Created technical audit script:
    - `scripts/moonn_privacy_compliance_audit.py`
  - Ran the audit against the `83` production-scope URLs.
  - Created reports:
    - `docs/moonn-privacy-compliance-audit-2026-05-08.json`
    - `docs/moonn-privacy-compliance-audit-2026-05-08.md`
    - `docs/moonn-rkn-compliance-rollout-plan-2026-05-08.md`
- Verification:
  - `python scripts\moonn_privacy_compliance_audit.py` completed.
  - `python -m json.tool docs\moonn-privacy-compliance-audit-2026-05-08.json` passed.
  - Audit result: `83/83` production URLs have form signals, `79` pages lack detected checkbox, `58` pages lack detected consent text, and required policy endpoints currently return `404`.
- Decision:
  - Do not publish final legal pages until operator variables are confirmed.
  - Do not add GA4/Google Analytics while the cross-border/legal posture is unresolved; current checked main HTML did not show GA signals.
  - Use Yandex Metrika as the primary analytics layer for now and disclose it clearly in `/cookies` and `/privacy`.
- Automation:
  - Updated `moonn-seo-leftovers-morning-check` into `Moonn SEO and privacy compliance supervisor`.
  - Added weekly privacy/RKN scan duties: rerun `scripts\moonn_privacy_compliance_audit.py`, check legal endpoints, form checkbox/consent text, cookie/Yandex Metrika disclosure, GA/gtag drift, and robots.txt SEO safety.
  - Gate preserved: no live Tilda legal text, RKN notification, personal data publication, payment changes or bot-blocking rules without explicit approval.

## 2026-05-08 — Moonn Privacy Operator Details Filled

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user provided public email `moonn.official@yandex.ru` and asked to prepare privacy pages for Moonn.
- Actions:
  - Checked public sources for ИП Кумскова Татьяна Михайловна.
  - Filled publication packet with:
    - operator: `Индивидуальный предприниматель Кумскова Татьяна Михайловна`;
    - INN: `770906685276`;
    - OGRNIP: `316774600553212`;
    - email: `moonn.official@yandex.ru`.
  - Updated:
    - `docs/moonn-privacy-publication-packet-2026-05-08.md`
    - `docs/moonn-rkn-compliance-rollout-plan-2026-05-08.md`
- Provenance:
  - User-confirmed: public email.
  - Public search result confirmed ИП реквизиты via business profile snippets; full address not copied.
- Remaining gate:
  - Do not publish until the public correspondence/legal address is explicitly confirmed by user or legal source.

## 2026-05-08 — Incident: Wrong External Domain Added To Privacy Packet

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Symptom: `https://umun.ru/` was added to the privacy packet as a related site.
- Root cause: assistant treated a user correction mentioning a domain as ownership confirmation without a domain ownership verification gate.
- Fix:
  - Removed `umun.ru` from:
    - `docs/moonn-privacy-publication-packet-2026-05-08.md`
    - `docs/moonn-rkn-compliance-rollout-plan-2026-05-08.md`
    - the operative history entry above.
- Follow-up rule:
  - Never add an external domain to legal/privacy documents unless ownership/control is verified through Tilda/project settings, DNS/registrar, official site text, or an explicit unambiguous user confirmation after showing the exact domain.

## 2026-05-08 — Moonn RKN/Privacy Layer Published And Verified

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked whether the RKN/privacy site changes were actually done and, if not, to finish policy, consent and related page changes.
- Actions:
  - Published the privacy compliance frontend layer through the Moonn Tilda global head.
  - Re-published the protected production scope pages: `80/80` pages in `docs/moonn-seo-scope-publish-report-2026-05-07.json`.
  - Published the existing `/politic` page as the canonical privacy/personal-data policy page.
  - Re-ran the raw privacy audit:
    - `docs/moonn-privacy-compliance-audit-2026-05-08.json`
    - `docs/moonn-privacy-compliance-audit-2026-05-08.md`
  - Created rendered/live verification:
    - `docs/moonn-rkn-live-verification-2026-05-08.md`
- Live verification:
  - `https://moonn.ru/`, `https://moonn.ru/politic`, `https://moonn.ru/psiholog-konsultacii-moskva`, and `https://moonn.ru/events_tp` returned `200` and included `moonn-privacy-compliance-layer`.
  - The rendered homepage had `2` forms and `2` required unchecked `moonn_personal_data_consent` checkboxes linking to `https://moonn.ru/politic`.
  - Rendered `/politic` included ИП Кумскова Татьяна Михайловна, ИНН `770906685276`, ОГРНИП `316774600553212`, `moonn.official@yandex.ru`, cookies, Yandex Metrika and Webvisor disclosure.
  - No checked live page contained `umun.ru`.
- Incident / limitation:
  - The current raw scanner does not execute JavaScript, so it still reports missing checkboxes on many pages even though rendered browser verification confirms the injected layer.
  - Tilda global HEAD editing can duplicate old code if hidden textarea and ACE editor state are mixed.
- Follow-up rule:
  - For RKN/compliance readiness, rendered JS mitigation is not the final source-level state. Next hardening must move the policy text and form checkboxes into native Tilda blocks/settings where possible, and then verify both raw HTML and rendered browser output.

## 2026-05-08 — Moonn Native Policy Source Hardening

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: continue the RKN/privacy hardening after the rendered compliance layer was published.
- Actions:
  - Converted `/politic` page `58199199` from rendered JS replacement dependency to native Tilda text content.
  - Added canonical native text artifact:
    - `docs/moonn-native-politic-text-2026-05-08.txt`
  - Created native form candidate inventory:
    - `docs/moonn-native-form-inventory-2026-05-08.json`
  - Created native form hardening plan:
    - `docs/moonn-native-form-hardening-plan-2026-05-08.md`
  - Updated:
    - `docs/moonn-rkn-live-verification-2026-05-08.md`
- Verification:
  - Tilda API `getpagefull` for `/politic` found native `Политика обработки персональных данных`.
  - Tilda API no longer found old native title `ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ`.
  - Tilda API and live raw HTML found INN `770906685276`, OGRNIP `316774600553212`, `moonn.official@yandex.ru`, and Yandex.Metrika/Webvisor disclosure.
  - Live raw `https://moonn.ru/politic?native-check=20260508` returned `200`.
- Form inventory:
  - `15` production pages have form-like blocks.
  - `21` candidate blocks were detected.
  - `1` block already has a native checkbox signal.
  - Homepage real contact form `42678538` / `rec691008996` is the first native checkbox pilot target.
- Incident / limitation:
  - Direct rich-text paste into Tilda selected only one word in the editor, so source edits must be verified through Tilda API and live raw HTML before being reported as done.
  - The homepage form currently has old consent text but no native required checkbox signal in raw source; rendered JS mitigation remains active, but native checkbox work is still open.
- Follow-up rule:
  - Do not mass-edit all Tilda form blocks until one real form pilot proves the supported Tilda field path and passes API/live/browser verification.

## 2026-05-08 — Moonn Teen Psychology Camp Page Publication

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: publish the teen psychology camp page from local HTML to `moonn.ru`, integrate it into the Moonn site, and preserve SEO/RKN checks.
- Actions:
  - Cleaned the local camp page from external/local residue and base64 image payloads.
  - SEO-renamed and published assets through the GitHub/jsDelivr asset path.
  - Created Tilda page `140348786` with alias `podrostkovyy-lager-psihologiya`.
  - Added page-specific SEO metadata, canonical, OG metadata, JSON-LD and `/politic` link through Tilda HEAD.
  - Published the page to `https://moonn.ru/podrostkovyy-lager-psihologiya`.
  - Prepared homepage banner artifacts and an external banner JS asset.
- Verification:
  - Live camp page returned `200`.
  - Live camp page includes the camp H1/hero text, JSON-LD, canonical URL and `/politic` link.
  - Live camp page does not include Kaspersky residue, base64 payloads or `data:image`.
- Incident / limitation:
  - Tilda accepted page-specific HEAD injection on the new camp page, but the homepage HEAD editor rolled back/rejected additional banner snippets and kept only the previous `moonn-radiant-sanctuary` code.
  - Therefore homepage integration is not complete and must be done as a native Tilda block/card rather than another forced HEAD injection.
- Follow-up rule:
  - For public homepage integrations, do not report completion until the live homepage HTML or rendered browser output contains the new internal link and the visual banner/card is verified.
  - Prefer native Tilda blocks for homepage marketing placements; use HEAD/JS only for low-risk page-local enhancements where Tilda demonstrably preserves the code.

## 2026-05-08 — Moonn Teen Camp Homepage Banner Completed

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user interrupted the previous run and asked to continue: add the teen camp banner to the Moonn homepage, publish it, and verify the camp page buttons, PDF, Telegram and SEO.
- Actions:
  - Added a visible homepage banner through a native Tilda `T123` HTML block on homepage page `42678538`.
  - Published only the homepage from the Tilda page editor, not the whole project.
  - Verified the live homepage HTML includes `moonn-teen-camp-home-banner`, `/podrostkovyy-lager-psihologiya`, camp text and SEO image.
  - Verified in Chrome that the banner is visible and the `Узнать программу` button opens the camp page.
  - Verified the live camp page has title, canonical, JSON-LD, PDF link and Telegram link.
  - Click-tested Telegram: it opens `t.me/moonn_official` and shows the Telegram Desktop handoff prompt.
  - Opened the PDF in Chrome and clicked the PDF viewer download button; the downloaded file content starts with `%PDF-`.
- Live URLs:
  - `https://moonn.ru/`
  - `https://moonn.ru/podrostkovyy-lager-psihologiya`
- Incident / limitation:
  - The camp page button `Узнать про стоимость и рассрочку` currently links to WhatsApp, not to a price section anchor. This is a working contact path, but if the intended UX is scroll-to-price, it needs a small separate edit.
  - The PDF link exists in the page HTML and opens correctly, but it is lower in the materials section; direct PDF verification was used after confirming the link exists in source.
- Follow-up rule:
  - For future Moonn landing pages, homepage integration must be a native visible block first, with live HTML + rendered browser + primary CTA checks before reporting completion.

## 2026-05-09 — Moonn Teen Camp Payment CTA Completed

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: add a real payment entry point to the teen psychology camp landing page and verify that the user can pay 30 000 ₽ through the existing Tilda/T-Bank flow.
- Actions:
  - Updated teen camp page artifacts with the product price, `Оплатить участие` CTA and native Tilda order link.
  - Preserved the native Tilda cart record `rec2251553291` / block `706` instead of replacing it with a custom payment layer.
  - Added runtime repair so the custom-rendered landing page restores `.t706` cart DOM that the older loader had displaced.
  - Bound the payment CTA to native Tilda cart functions: `tcart__addProduct`, `tcart__reDrawCartIcon`, `tcart__openCart`.
  - Purged the encoded jsDelivr branch URL so Tilda loaded the current external page artifact.
  - Added payment rollout report:
    - `docs/teen-psychology-camp-2026/payment-rollout-report-2026-05-09.md`
  - Added verification screenshot:
    - `docs/teen-psychology-camp-2026/cart-headless-check.png`
- Verification:
  - Live page keeps the native Tilda cart script and `.t706` cart record.
  - PDF link returns `200`, `application/pdf`, size `245793`.
  - Headless browser click on `Оплатить участие` opens the cart modal with product `Подростковый лагерь по психологии`, SKU `teen-camp-2026`, price `30 000р.`, T-Bank card payment and T-Bank installment option.
  - Real Google Chrome check also showed the visible cart modal with order, price and T-Bank payment options.
  - No card details were entered and no real payment was submitted.
- Incident / root cause:
  - The first custom Tilda loader replaced body content and broke/displaced the native cart DOM.
  - Tilda timed out on a large HEAD payload, so the stable approach is compact loader plus external artifact.
  - Native `#order` parsing did not bind reliably after custom rendering, so the CTA now calls native Tilda cart functions directly.
- Follow-up rule:
  - For future paid Moonn/Tilda pages, reuse native Tilda cart/payment blocks where they exist, verify the real provider-backed cart in browser, and keep real payment submission as a separate explicitly approved test.

## 2026-05-09 — Moonn Chat Recovery Index

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user reopened Codex after reinstall and asked to recover which prior Moonn-related chats/workstreams existed, so future work continues in the right project instead of recreating unrelated chats.
- Actions:
  - Confirmed the active Moonn repository is `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`, not `C:\пайто н тесты\курсэмоциональный интеллект`.
  - Checked global Codex `session_index.jsonl` for Moonn/Tatiana Munn/Tilda/Timepad/payment-related thread records.
  - Checked local raw sessions under `C:\Users\yanta\.codex\sessions`.
  - Created recovery index:
    - `docs/moonn-chat-recovery-index-2026-05-09.md`
- Verification:
  - Found older thread ids/names for March-April and May 1, but their raw session files are missing locally after reinstall.
  - Found May 9 recovery raw sessions locally.
  - Confirmed `docs/codex-chat-history.md` remains the canonical project-level memory for Moonn workstreams.
- Follow-up rule:
  - Before restarting any Moonn workstream, first read `docs/moonn-chat-recovery-index-2026-05-09.md` and `docs/codex-chat-history.md`; only open raw sessions when the exact thread id is present locally or restored from backup.

## 2026-05-09 — Moonn Chat Restore Prompts

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked for one startup prompt per recovered chat title, so newly created Codex chats can be renamed to old chat names and reconnected to the correct repository/workstream.
- Actions:
  - Created restore prompt packet:
    - `docs/moonn-chat-restore-prompts-2026-05-09.md`
  - Included prompts for research, public links, Yandex/Timepad/site promotion, school/event promotion, Tilda API, Moonn recovery, chat repository discovery and current Yandex/Timepad/agent continuation.
- Verification:
  - Each prompt points to the canonical repository `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`.
  - Each prompt instructs the restored chat to read `docs/moonn-chat-recovery-index-2026-05-09.md` and `docs/codex-chat-history.md` first.
  - High-risk gates for payment, legal/privacy, personal data, Tilda publish-all and live external changes are preserved.
- Follow-up rule:
  - When creating a replacement chat for a missing raw Moonn thread, use the exact old chat title plus the matching prompt from `docs/moonn-chat-restore-prompts-2026-05-09.md`; do not start from a blank generic prompt.

## 2026-05-09 — Moonn Teen Camp Tilda/T-Bank Payment Completed

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to finish real payment for `Подростковый лагерь по психологии` on `moonn.ru` through the correct Tilda route, not through a detached custom HTML payment workaround.
- Actions:
  - Kept native Tilda ST100/T-Bank as the payment layer.
  - Updated the external page artifact so `Оплатить участие` opens native Tilda cart through `tcart__addProduct`, `tcart__reDrawCartIcon` and `tcart__openCart`.
  - Updated the Tilda page HEAD loader to the committed bridge artifact.
  - Corrected the Tilda HEAD save path by writing through the Ace editor model, then reopened and verified persistence.
  - Published Tilda page `140348786` in project `8326812`.
- Verification:
  - Live HTML check: `@b7fc89f` is present, old `@6e83435` is absent, `20260509-native-cart-bridge` is present.
  - Chrome Alexander profile check: clicking `Оплатить участие` opens the Tilda cart with one product, SKU `teen-camp-2026`, amount `30 000 р.`.
  - Checkout form check: test name/email/phone and consent reveal `Перейти к оплате через T-Bank`.
  - Provider check: the flow redirects to `pay.tbank.ru` and shows T-Bank card-entry fields with `30 000 ₽`.
  - No card details were submitted and no real payment was made.
- Commits:
  - `b7fc89f` — `Open teen camp checkout via native Tilda cart`
  - `6ca1991` — `Point teen camp Tilda head loader to native cart bridge`
- Incident / root cause:
  - Native `#order`/hash binding was not reliable after custom HEAD rendering, and the first Tilda HEAD save attempts changed textarea/accessibility state without persisting the Ace editor value.
- Follow-up rule:
  - For paid Moonn/Tilda pages, verify the full chain before reporting readiness: Tilda HEAD reopen -> Tilda publish -> live HTML -> one-product cart -> provider card-entry page. Real payment submission remains a separate high-risk action requiring explicit approval.

## 2026-05-09 — Payment Fix Learning Note

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked why the payment problem took too long and requested that the error path and solution be recorded for future self-learning.
- What failed in the previous approach:
  - I trusted Tilda's visible save state too early instead of verifying the Ace editor value after reopening the HEAD settings.
  - I assumed a custom CTA/order hash would behave like a native Tilda product block, even though the page body is custom-mounted from an external artifact.
  - I treated "a cart opens" as sufficient progress, while the actual acceptance criterion was stricter: exactly one product, `30 000 р.`, and provider-backed T-Bank card entry.
- Key turning point:
  - The problem was reframed from "make payment work in custom HTML" to "keep native Tilda/T-Bank as the source of truth and build only a minimal bridge from the custom page to native cart functions."
  - The deeper behavioral turning point was that I rechecked my own actions and stopped trusting visual confirmations. The green Tilda save banner was only a UI signal, not proof of persistence or publication.
- Reusable solution:
  - Native payment layer: ST100/T-Bank.
  - Custom page bridge: `tcart__addProduct` -> `tcart__reDrawCartIcon` -> `tcart__openCart`.
  - Anti-duplication step: clear stale cart products before adding the current product.
  - Persistence check: write through Ace editor, reopen HEAD, then publish.
  - Readiness check: live HTML -> browser cart -> checkout button -> `pay.tbank.ru` card-entry page.
- New rule:
  - For Tilda payment tasks, do not report success from screenshots, editor messages, or partial cart opening. Success requires provider-page verification up to card-entry screen, without submitting a real payment unless explicitly approved.

## 2026-05-09 20:59 MSK — Fast Continuation Chat Started

- Project: Moonn / Tilda site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user opened a new Codex chat to continue the prior Moonn/Tilda payment workstream without the slowdown from the old heavy chat, while keeping the old chat as archive.
- Context read:
  - `docs/codex-handoffs/2026-05-09-fast-restart-moonn-payment.md`
  - latest 2026-05-09 entries from `docs/codex-chat-history.md`
- Confirmed state:
  - Repository is `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`.
  - Active branch is `codex/moonn-seo-audit`.
  - Latest commit is `822e1ad` — `Add fast restart handoff for Moonn payment`.
  - Remaining local untracked files are the three pre-existing PNG verification screenshots in `docs/teen-psychology-camp-2026/`.
- Decision:
  - Continue Moonn/Tilda work in this chat on the existing canonical branch.
  - Do not create a new repository or duplicate branch for this continuation.
  - Do not read the full old heavy chat unless a specific missing detail cannot be recovered from the handoff, project memory or recovery index.
- Follow-up rule:
  - If this chat becomes slow, create another fast continuation chat from the handoff pattern instead of changing repositories, duplicating branches or reloading raw chat archives.

## 2026-05-09 — Moonn Yandex Services Reviews SEO Restart

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user returned from Timepad workstream to the older SEO workstream about connecting Moonn site visibility with the Yandex Services profile `Татьяна Кумскова (Мунн)` and asked to build/strengthen a reviews page on `moonn.ru`.
- Context checked:
  - Active automation `moonn-seo-leftovers-morning-check`, which listed Yandex Services reviews/profile synchronization as a blocked SEO item.
  - Existing live page `https://moonn.ru/otzivi`.
  - Local schema and SEO packets in `assets/moonn-schema-layer.js`, `scripts/build_moonn_schema_layer.py`, and `docs/moonn-schema-layer-packet-2026-05-08.*`.
- Verified facts:
  - `https://moonn.ru/otzivi` already exists and returned `200`.
  - The page already contains client reviews with Yandex Services source links.
  - The page still includes weak public wording such as `дублирую информацию` and `поиска информации в интернете`.
  - The working Yandex Services profile resolves as `https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629`.
- Decision:
  - Do not create a duplicate reviews page and do not mirror the Yandex Services profile one-to-one.
  - Keep `/otzivi` as the canonical reviews page and strengthen it with source links, profile provenance, schema, and user-facing editorial wording.
  - Supersede the 2026-05-04 assumption that `TatyanaKumskovatatyanamunn-948629` was canonical; 2026-05-09 live check showed `TatyanaKumskovamunn-948629` as the working profile path.
- Local artifacts changed/prepared:
  - `data/site.json`
  - `scripts/build_moonn_schema_layer.py`
  - `assets/moonn-schema-layer.js`
  - `assets/moonn-yandex-reviews-quality-layer.js`
  - `docs/moonn-schema-layer-packet-2026-05-08.json`
  - `docs/moonn-schema-layer-packet-2026-05-08.md`
  - `docs/moonn-global-head-code-with-schema-2026-05-08.html`
  - `docs/moonn-yandex-services-reviews-seo-packet-2026-05-09.md`
- Risk / limitation:
  - The rendered JS quality layer can remove weak wording visually after deployment, but raw Tilda HTML still needs native source cleanup for the strongest SEO/compliance result.
  - Live Tilda HEAD currently pins schema scripts to an older commit; Git changes require a scoped Tilda HEAD update and page publish before they affect `moonn.ru`.
- Follow-up rule:
  - Public review pages must not expose internal SEO rationale. Use trust/provenance wording, source links, and structured data, and avoid synthetic ratings or unsupported review counts.

## 2026-05-09 23:05 MSK — Moonn Yandex Services Reviews SEO Live Applied

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: continue the Yandex Services reviews SEO task to actual Tilda/live deployment, not just local packet preparation.
- Actions:
  - Hardened `assets/moonn-schema-layer.js` so the current page-specific schema layer updates an existing `script#moonn-page-schema-jsonld` instead of silently no-oping when an older global schema node exists.
  - Hardened `assets/moonn-yandex-reviews-quality-layer.js` so the Yandex Services source panel can attach to Tilda text elements and patched review text, not only native `h1/h2`.
  - Saved Tilda page-specific HEAD for page `81167556` with commit `b9930a83da11cdbfaeae98a9f92309fe1d2d4464`.
  - Published only page `81167556`.
- Verification:
  - Raw live `https://moonn.ru/otzivi` returned `200`.
  - Raw live HTML contains `moonn-yandex-reviews-quality-layer` and pinned commit `b9930a83da11cdbfaeae98a9f92309fe1d2d4464`.
  - Wrong typo commit `ba39941e95b8a623a7566ba58d281d34e8a16a13` is absent.
  - Rendered Playwright check: `script#moonn-page-schema-jsonld` has `data-moonn-schema-path="/otzivi"` and `data-moonn-schema-updated="true"`.
  - Rendered JSON-LD includes `Person`, `WebSite`, `WebPage`, `ProfilePage`, `ItemList`, `BreadcrumbList`.
  - Rendered JSON-LD includes `https://moonn.ru/otzivi#yandex-services-profile` and `https://moonn.ru/otzivi#verified-yandex-review-summaries`.
  - Rendered page includes the panel `Проверяемые отзывы с Яндекс Услуг`.
  - Rendered page no longer shows `дублирую информацию` or `поиска информации в интернете`.
- Remaining risk / follow-up:
  - Raw Tilda HTML still contains the old weak phrases and the older Yandex profile URL variant. The runtime layer corrects the rendered page, but a native Tilda block cleanup remains the stronger final SEO/compliance state.
- Commits:
  - `b9930a8` — `Harden Yandex reviews runtime layers`
- Follow-up rule:
  - When a global runtime layer and a page-specific runtime layer both write the same DOM node, the page-specific layer must update/replace stale node content and expose a verification attribute, not silently skip.

## 2026-05-09 — Moonn Yandex Services All Reviews Requirement

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user clarified that `/otzivi` must include all reviews, not only four or five selected examples.
- Verification:
  - Rendered Yandex Services profile showed `190 оценок`.
  - Browser scan collected `136` unique visible public text-review records from the paginated reviews section.
  - `190 оценок` is not the same as `190` text reviews; some Yandex ratings may not expose public review text.
- Decision:
  - Treat “all reviews” as all public text reviews visible on Yandex Services at scan time.
  - Do not hard-code a handful of summaries as the final state.
  - Do not publish the full verbatim external review corpus to `moonn.ru` or GitHub until legal/platform/personal-data gate is passed.
- Artifact:
  - `docs/moonn-yandex-services-all-reviews-scan-2026-05-09.md`
- Follow-up rule:
  - Review pages need a canonical review manifest and count-verification gate. Selected summaries are acceptable only as an interim SEO/provenance layer, not as the complete reviews page.

## 2026-05-10 — Moonn Reviews Page Runtime Regression Fixed

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user opened `https://moonn.ru/otzivi` and pointed out that the page showed only the Yandex source panel, not the actual reviews.
- Root cause:
  - `assets/moonn-yandex-reviews-quality-layer.js` searched broad `div` containers for weak SEO phrases and replaced `innerHTML`.
  - On the Tilda page this matched a large page container, so the runtime layer removed the visible original reviews and left only the source panel.
- Fix:
  - Removed destructive text replacement from the review quality layer.
  - Kept only a non-destructive source/provenance panel insertion.
  - Re-pinned Tilda page-specific HEAD for page `81167556` to commit `ca82ebe2e33335c04f6bf05245b8630e9c25c759`.
  - Published only page `81167556`.
- Verification:
  - Live raw HTML contains commit `ca82ebe2e33335c04f6bf05245b8630e9c25c759`.
  - Previous runtime commit `b9930a83da11cdbfaeae98a9f92309fe1d2d4464` is absent from live HTML.
  - Playwright rendered check found the original hero and review names/text again.
  - Manual browser scroll showed visible review cards with source text and links.
- Commit:
  - `ca82ebe` — `Stop destructive Yandex reviews patching`
- Follow-up rule:
  - Runtime content patches on Tilda must not replace `innerHTML` of broad containers (`div`, record wrappers, body-level sections). Use additive overlays or leaf-node-only changes with tight length/class guards and visual verification.

## 2026-05-10 — Moonn Yandex Reviews 2026 Archive Layer Published

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user noticed that the live `/otzivi` page started with 2025 reviews and missed newer Yandex Services reviews from 2026; user also asked for a clearer Yandex Services source block and removal of the dark first review block.
- Actions:
  - Added `assets/moonn-yandex-all-reviews-layer.js`.
  - Updated `assets/moonn-yandex-reviews-quality-layer.js` to:
    - place a light Yandex Services provenance block near the top;
    - keep the profile block before reviews;
    - hide the dark legacy hero block `rec1353100721`;
    - avoid destructive HTML replacement.
  - Published Tilda page-specific HEAD for page `81167556` with commit `9df3edab278d5c27dbc98e2216de692ae247da6f`.
  - Published only page `81167556`.
- Verification:
  - Local browser preview before publication found the order: intro -> Yandex Services panel -> profile -> all-reviews layer -> native Tilda review cards.
  - Live raw HTML contains both `moonn-yandex-reviews-quality-layer` and `moonn-yandex-all-reviews-layer` pinned to commit `9df3edab278d5c27dbc98e2216de692ae247da6f`.
  - Live rendered Playwright check found `123` review summary cards, including 2026 dates `15.04.2026`, `05.04.2026`, and `28.02.2026`.
  - Live rendered page contains the Yandex Services badge and `актуальные отзывы 2026`.
  - Live rendered page hides the dark legacy hero block (`display: none`).
- Commit:
  - `9df3eda` — `Add Yandex reviews archive layer`
- Risk / limitation:
  - The full verbatim Yandex review corpus is still not republished because the legal/platform/personal-data gate for copying external review text remains unresolved. The published layer uses summary cards with source links.
- Follow-up rule:
  - For external-review archive pages, publish the user-facing trust layer as summaries plus source links until the full-text republication gate is explicitly cleared.

## 2026-05-10 — Moonn Reviews Link And Code-Leak Incident Fixed

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user reported two live defects on `/otzivi`:
  - internal escaped HEAD/script code was visible at the top of the public page;
  - review-card links opened Yandex reviewer profiles instead of Tatyana Munn's Yandex Services profile.
- Root cause:
  - The previous validation checked card count and 2026 dates but did not click/inspect card link destinations.
  - The Tilda page contained an escaped legacy page-specific HEAD payload as a body text node; runtime scripts could not remove it until the correct commit hash was published.
  - A wrong full commit hash was briefly written into Tilda HEAD even though the short hash looked correct.
- Fix:
  - Updated `assets/moonn-yandex-all-reviews-layer.js` so every review-card link points to `https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629`.
  - Updated `assets/moonn-yandex-reviews-quality-layer.js` to remove leaked escaped HEAD text nodes from rendered `body`.
  - Hid empty decorative Tilda block `rec1353368171`, which visually overlapped the Yandex source panel.
  - Republished Tilda page `81167556` with the correct commit `8739444484729fb768f29522ef6e7a16bf06299b`.
- Verification:
  - Live rendered Playwright check found no visible `moonn-radiant-sanctuary-theme:start` or `cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages` leak text.
  - Live rendered page still has the Yandex source panel and `123` review cards.
  - Live rendered check found `0` review-card links pointing to `reviews.yandex.ru/user`.
  - First 10 sampled card links all point to `https://uslugi.yandex.ru/profile/TatyanaKumskovamunn-948629`.
  - Decorative divider block `rec1353368171` is `display: none`.
- Commit:
  - `8739444` — `Fix Yandex reviews public links and leaked code`
- Follow-up rule:
  - Public-page validation for review archives must include link-destination checks, visible-code leak checks, and exact full commit hash verification, not only card count and text/date presence.

## 2026-05-10 — Moonn Reviews Exact Excerpt Layer Published

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user reported that the `/otzivi` review cards were semantic paraphrases, not the review texts, and asked for the pink/lilac background plus exact per-review Yandex links where possible.
- Root cause:
  - The previous archive layer optimized for a safe summary/provenance format and passed count/link checks, but the validation gate did not distinguish exact review text from generated meaning.
  - The Yandex scan contains reviewer-profile URLs, not verified stable URLs for individual reviews; using reviewer-profile URLs was the wrong destination.
  - Tilda/Ace can keep separate visible-editor and hidden-textarea values, so saving must be followed by raw live HTML and rendered browser checks.
- Fix:
  - Added `scripts/build_moonn_yandex_all_reviews_layer.js`, a deterministic builder from `output/yandex-services-reviews-scan-2026-05-09.json`.
  - Regenerated `assets/moonn-yandex-all-reviews-layer.js` with exact source excerpts rather than paraphrases.
  - Removed public use of `reviews.yandex.ru/user` reviewer-profile links.
  - Kept a pink/lilac/light-blue gradient background for the archive layer.
  - Republished Tilda page `81167556` with runtime layers pinned to commit `bc10db72289925361507bfee71b6d2c6d854b8c4`.
- Verification:
  - CDN asset for commit `bc10db72289925361507bfee71b6d2c6d854b8c4` returns `200`, contains `132` `excerpt` records, contains no generated summary phrases, and contains no `reviews.yandex.ru/user` URLs.
  - Live raw HTML contains `bc10db72289925361507bfee71b6d2c6d854b8c4` and no old `17c88b3e6933a5194642f9005d5be2566cd6609a`.
  - Live rendered Playwright check found `132` cards, `0` reviewer-profile links, no visible internal code, no generated summary phrases, no Yandex UI noise text, and a pink/lilac/light-blue gradient.
  - First rendered review text starts with the exact scanned source fragment: `Хожу к Татьяне на бесплатные лекции))`.
  - Screenshot proof: `output/moonn-otzivi-live-excerpt-verify-2026-05-10.png`.
- Risk / limitation:
  - Exact per-review deep links are not implemented because the collected source does not contain verified stable review URLs; cards honestly link to Tatyana Munn's Yandex Services profile until exact review URLs are verified.
  - Live raw Tilda HEAD still contains an extra closing `</script> </script>` tail after the page-specific HEAD block. It is not visible and does not break rendered checks, but it remains a Tilda/Ace cleanup item.
  - Full verbatim mirroring of all review texts remains behind the legal/platform/personal-data gate; the current public layer uses exact excerpts from the collected visible text.
- Commit:
  - `bc10db7` — `Render Yandex review excerpts from scan`
- Follow-up rule:
  - Review-page releases must validate semantic fidelity (`exact excerpt` vs `generated summary`), source-link type (`provider profile` vs `reviewer profile` vs `verified review permalink`), raw HEAD cleanliness, and rendered browser output before reporting completion.

## 2026-05-10 — Moonn Timepad Consultation MVP Draft Created

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user approved a minimal MVP for paid psychological consultations through Timepad, with email/manual notification for Rublev and later iClient/YCLIENTS mirroring.
- Strategic decision:
  - Use Timepad as the visible booking/payment layer, not a page that primarily sends users to iClient/YCLIENTS, because Timepad moderation may treat an external paid-booking link as bypass.
  - Keep iClient/YCLIENTS as the specialist's working calendar, but mirror paid Timepad orders manually in the MVP.
  - Future stronger architecture: Timepad `order_change` webhook -> registry/notification -> iClient/YCLIENTS booking/blocking.
- Action:
  - Created draft Timepad event in Tatyana Munn's personal organization `426753` / `moonn`.
  - Draft event: `https://moonn.timepad.ru/event/3973843/`.
  - Status verified by API: `access_status=draft`, `moderation_status=not_moderated`.
  - Initial placeholder slot: 2026-05-18 12:00-14:00 MSK.
  - Tickets: 2-hour consultation `10 000 ₽`, 1-hour consultation `6 000 ₽`, package of 5 consultations `40 000 ₽`.
- Artifact:
  - `docs/timepad-consultation-mvp-2026-05-10.md`
- Verification:
  - Timepad API returned event id `3973843`.
  - Read-back via Timepad API confirmed organization `426753`, category `Психология и самопознание`, draft status, location, prices and total ticket limit `1`.
- Known limitations before publication:
  - Poster image is not uploaded yet.
  - Slot schedule is not yet synced against iClient/YCLIENTS.
  - Custom registration questions need UI verification because Timepad API rejected custom `field_id` values.
  - Event is not published and not submitted as complete.
- Follow-up rule:
  - Paid Timepad consultation pages are not ready until the slot schedule is checked against the specialist's working calendar and the registration/payment path is verified in the UI. API-created drafts must still pass Timepad UI checks before publication.

## 2026-05-10 — Moonn Timepad Consultation Event Published With Poster

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user provided a poster image for the consultation event and asked to rename it with SEO-style Latin filename, attach it to the Timepad event, publish the event, verify paid/public status, open the page, and prepare support text.
- Actions:
  - Copied the supplied image to `assets/timepad/tatyana-munn-psychological-consultation-msu-online-offline-moscow-timepad-2026.png`.
  - Pushed the image to GitHub and verified CDN availability through jsDelivr.
  - Updated Timepad event `3973843` through API with the poster and `access_status=public`.
  - Opened the public event page in the browser.
- Verification:
  - Timepad API confirmed `status=ok`, `access_status=public`, `moderation_status=not_moderated`.
  - Timepad API confirmed paid range `6000-40000`, registration open, total ticket limit `1`, and three active paid ticket types.
  - Public URL `https://moonn.timepad.ru/event/3973843/` returned HTTP `200`.
  - Public HTML contains event title, poster marker, and prices `6 000`, `10 000`, `40 000`.
- Commit:
  - `d991bfa` — `Add Timepad consultation poster`
- Risk / limitation:
  - The event is public but still `not_moderated`, so Timepad support/Afisha approval is not yet complete.
  - Custom questionnaire fields still need Timepad UI verification because API rejected custom question field ids.
  - iClient/YCLIENTS slot reconciliation remains required before scaling beyond this first slot.
- Follow-up rule:
  - Timepad publication is not fully complete at `access_status=public`; for business readiness, also verify paid prices on the public page, poster, moderation status, and calendar/slot reconciliation.

## 2026-05-10 — Moonn Timepad Consultation Address And Recurring Schedule Path

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user noticed that the public Timepad event showed an ambiguous place (`метро Марьина Роща / онлайн`) and asked to show a real address on the map; user also asked how participants can choose dates through the end of the year.
- Fix:
  - Updated Timepad event `3973843` through API to use `Москва, Цветной бульвар, д. 19, стр. 4`.
  - Added the same address to the public description.
- Verification:
  - API read-back confirmed city `Москва`, address `Москва, Цветной бульвар, д. 19, стр. 4`, `status=ok`, `access_status=public`, registration open, paid prices `6000/10000/40000`.
  - Public HTML check returned `200`, contains the address, no longer contains the vague `метро Марьина Роща / онлайн` wording, contains a map link, and still contains paid prices.
- Recurring schedule decision:
  - Do not mass-create many independent weekly duplicate events by API.
  - Use Timepad's master-event/schedule mechanism for weekly consultation slots from 2026-05-18 through 2026-12-28 inclusive.
  - Ask Timepad to use calendar-style schedule display if available, so visitors can choose a date visually.
  - Official Timepad help says the schedule/master-event option is connected by writing to support with the first event link; this matches the support route for the current event.
- Follow-up rule:
  - For paid consultation scheduling, prefer one Timepad master event with session slots and capacity `1` over many standalone cloned events; independent copies create moderation, duplicate, and calendar-sync risk.

## 2026-05-10 — Moonn Timepad Consultation Reception Days Correction

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user corrected the schedule assumption: Tatyana currently consults on Tuesday, Saturday, and Sunday, not Monday; a single fixed slot does not let visitors choose a suitable time.
- Fix:
  - Updated Timepad event `3973843` through API from `2026-05-18 12:00-14:00` to `2026-05-16 12:00-14:00`.
  - Updated public short and full descriptions to say consultations are held on Tuesday, Saturday, and Sunday.
  - Updated the support request model: ask Timepad for schedule/master-event slots across reception days with selectable dates and times, not one Monday recurring slot.
  - Removed internal `technical first date` wording from the public page and replaced it with client-facing fallback text: if the desired time is not visible, the organizer helps choose a suitable time in the reception days.
- Verification:
  - API read-back confirmed `starts_at=2026-05-16T12:00:00+03:00`, `ends_at=2026-05-16T14:00:00+03:00`, address `Москва, Цветной бульвар, д. 19, стр. 4`, `access_status=public`, `moderation_status=not_moderated`.
  - Public HTML check returned `200`, contains Tuesday/weekend wording, address, paid prices, and no internal `technical` / `MVP` wording.
- Tooling note:
  - Gmail connector install/activation was requested but not completed in this session, so email sending is still blocked without manual browser use.
- Follow-up rule:
  - Consultation schedule assumptions must be verified against the current iClient/YCLIENTS calendar before publication or support submission; Timepad support requests should ask for multiple selectable reception-day slots.

## 2026-05-10 — Moonn Timepad Support Email Sent

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user explicitly asked to send the support email to Timepad after the consultation reception days were corrected.
- Action:
  - Gmail connector became available after tool discovery.
  - Sent email from `rublevalexandermsu@gmail.com` to `support@timepad.ru`.
  - Subject: `Просим проверить консультацию психолога Татьяны Мунн и подключить расписание`.
  - Message asked Timepad to check event `https://moonn.timepad.ru/event/3973843/` and connect schedule/master-event mode for Tuesday, Saturday, and Sunday consultation slots through the end of 2026.
- Verification:
  - Gmail send response returned message id `19e1152a116ae61a`, thread id `19e1152a116ae61a`, label `SENT`.
- Follow-up:
  - Wait for Timepad response or moderation result.
  - If Timepad asks for a different technical format, update the Timepad event and this project history before resubmitting.

## 2026-05-10 — Moonn Homepage Replacement Experiment Routed

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked how to publish and test an older/newer local HTML page without replacing the currently ranking homepage.
- Checked facts:
  - Current live homepage `https://moonn.ru/` returns `200`, has title/description, self-canonical to `/`, and detected JSON-LD.
  - Candidate local HTML file exists outside the repository and has one H1 and many sections, but no detected title, description, canonical or robots meta.
  - Candidate page contains internal setup text and incomplete Timepad/WhatsApp instructions, so it is not safe to publish as-is.
- Decision:
  - Do not replace the root homepage now.
  - Use a same-domain semantic experimental landing instead of a new domain or duplicate root page.
  - Clean the local HTML, choose a semantic URL, add metadata/schema, and publish only after content/legal/SEO/visual QA.
- Artifact:
  - `docs/moonn-homepage-experiment-plan-2026-05-10.md`
- Follow-up rule:
  - Alternative homepages must be launched as semantic same-domain experiments with clear search intent, self-canonical only when materially unique, and Metrica/Search Console measurement before any root homepage migration.

## 2026-05-10 — Moonn Homepage Experiment Candidate Switched

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user clarified that `Окончательный.код.сай..html` is the better working page and should be used instead of `Сайт.6..резервный.последний.копия.html`.
- Checked facts:
  - New candidate exists at `C:\пайтонннн.. тесты\код сайт татьяна мунн\Коды для сайта татьяны.готовые\Окончательный.код.сай..html`.
  - File size: `113006` bytes; last modified `2026-02-15`.
  - Detected one H1, sixteen H2 sections and one JSON-LD block.
  - No detected title, meta description, canonical or robots meta.
  - Internal hints reduced to `3`, but one visible setup instruction remains: `Если Тильда позволяет - перенеси <title>, meta description, og:* в HEAD страницы.`
  - Page contains real Timepad links for the lecture carousel, but consultation booking/payment text still uses Telegram/WhatsApp/card/SBP and must be aligned with the newer Timepad paid booking route.
- Decision:
  - Use `Окончательный.код.сай..html` as the primary candidate for the same-domain SEO landing experiment.
  - Demote the previous `Сайт.6..резервный.последний.копия.html` candidate.
- Artifact updated:
  - `docs/moonn-homepage-experiment-plan-2026-05-10.md`.

## 2026-05-10 — Moonn Psychologist SEO Landing Published

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user approved building and publishing the additional SEO/AI/EE optimized page from `Окончательный.код.сай..html`, keeping the current homepage intact.
- Route:
  - Continued the existing additional semantic URL `https://moonn.ru/psiholog-tatiana-moonn` instead of replacing `/` or creating a duplicate domain.
  - Cleaned the local HTML into a deterministic generated artifact.
  - Published through the native Tilda `T123` record `rec1863545891` on page `115095616`, not through a HEAD takeover.
- Changes:
  - Removed old visible setup hints and legacy payment modal markers.
  - Replaced consultation payment CTAs with direct iClient/YCLIENTS booking: `https://n461584.yclients.com/`.
  - Replaced old embedded YouTube video IDs with the current YouTube channel link: `https://youtube.com/channel/UCyAQlNoDtg7En6BdwbctSrQ`.
  - Added SEO title, description, canonical, JSON-LD and Yandex Metrika click goals for iClient/YouTube/reviews.
- Artifacts:
  - `scripts/build_moonn_psychologist_landing_experiment.py`
  - `docs/psychologist-tatiana-munn-landing/tilda-html-block-final.html`
  - `docs/psychologist-tatiana-munn-landing/tilda-page-final.html`
  - `docs/psychologist-tatiana-munn-landing/tilda-head-seo-final.html`
  - `docs/psychologist-tatiana-munn-landing/tilda-head-loader-final.html`
  - `docs/psychologist-tatiana-munn-landing/quality-report.json`
  - `docs/psychologist-tatiana-munn-landing/publication-report-2026-05-10.md`
- Verification:
  - Local quality report: title/description/canonical present, H1 count `1`, JSON-LD count `1`, iClient present, YouTube channel present, old YouTube embeds `0`, visible/raw internal hits `0`.
  - Tilda API after publish: `meta_title` and `meta_descr` updated; HTML contains iClient and YouTube channel; old setup hint and old YouTube embed IDs absent.
  - Live HTML `https://moonn.ru/psiholog-tatiana-moonn?qa=final`: status `200`, title updated, canonical correct, H1 count `1`, JSON-LD count `3`, iClient links `17`, YouTube channel present, old YouTube IDs absent, legacy payment modal markers absent.
  - Desktop headless Chrome visual QA confirmed the new page renders publicly with the Moonn cookie/compliance layer.
- Commits:
  - `4c38497` — `Add Moonn psychologist SEO landing artifact`
  - `72ac8de` — `Add Tilda loader for psychologist landing`
- Follow-up rule:
  - For this page type, prefer native Tilda `T123` block replacement over HEAD document replacement when the page already consists of a single canonical HTML block. HEAD loaders remain fallback artifacts, not the primary publication route.

## 2026-05-10 — Moonn Psychologist Landing Summary Card Removed

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-seo-audit`.
- Trigger: user asked to remove the visible top block `Кратко о консультациях` and verify SEO after deletion.
- Route:
  - Kept the same canonical additional landing URL: `https://moonn.ru/psiholog-tatiana-moonn`.
  - Updated the generator rather than manually deleting the block only in Tilda, so future regenerations do not restore the removed section.
  - Published through native Tilda `T123` record `rec1863545891` on page `115095616`.
- Changes:
  - Added deterministic removal of the `#ai-summary` section before the hero.
  - Regenerated `docs/psychologist-tatiana-munn-landing/tilda-html-block-final.html`, `tilda-page-final.html`, and `quality-report.json`.
  - Added visual QA artifact `docs/psychologist-tatiana-munn-landing/visual-remove-summary-2026-05-10.png`.
  - Updated `docs/psychologist-tatiana-munn-landing/publication-report-2026-05-10.md`.
- Verification:
  - Local generated artifacts: no `Кратко о консультациях` / `ai-summary` matches outside the removal rule in the generator.
  - Local quality report: title/description/canonical present, H1 count `1`, JSON-LD count `1`, iClient present, YouTube channel present, old YouTube embeds `0`, visible/raw internal hits `0`.
  - Tilda editor save confirmation: block length `89843`, `hasSummary=false`, `hasHero=true`.
  - Tilda API after publish: `has_summary=false`, iClient present, YouTube channel present, old YouTube embeds absent, legacy payment markers absent.
  - Live HTML `https://moonn.ru/psiholog-tatiana-moonn?qa=remove-summary-1778414288`: status `200`, title unchanged, canonical correct, H1 count `1`, JSON-LD count `3`, iClient present, YouTube channel present, old YouTube IDs absent, legacy payment markers absent.
  - Visual Edge/browser check confirmed the page starts with the hero block and the removed top summary card is absent.
- Follow-up rule:
  - For public Tilda pages, visual deletion requests must be implemented in the generator/source artifact first, then published, then verified through Tilda API, live HTML, and browser render.

## 2026-05-10 — Tatiana Moonn Art Gallery Site Package

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user provided gallery/3D-scroll prototypes and generated artwork images, asking for a premium multi-page 3D gallery site for selling Tatyana Munn's paintings.
- Route:
  - Split this into a new product workstream branch instead of continuing the SEO/Timepad branch.
  - Built a deterministic static site generator so the gallery can be regenerated from source images and structured artwork records.
  - Kept real payment out of the public package until prices, inventory, legal seller, delivery/return terms and payment product IDs are confirmed.
- Changes:
  - Added `scripts/build_tatiana_munn_art_gallery_site.py`.
  - Generated `docs/tatiana-munn-art-gallery/` with `index.html`, catalog, individual artwork pages, code form, about/contact pages, optimized WebP artwork assets, local Three.js vendor file, favicon, `data/artworks.json`, README and `build-report.json`.
  - Created the local archive `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Local server `http://127.0.0.1:8765/` returned `200`.
  - Playwright/Chrome QA passed desktop and mobile canvas checks: visible nonblank WebGL canvas, no console/page errors.
  - Interaction QA passed: preview modal opens, artwork flips, code form returns a numeric code, catalog has `10` cards, first detail page opens.
  - Public text scan passed for the generated site excluding vendored Three.js: no visible single-`н` `Татьяна Мун`, no `MVP`, `прототип`, `Tilda`, `ST100`, `data-demo` or internal payment layer.
- Incident / correction:
  - Initial 3D frame was modeled as one solid box and visually occluded artwork textures in the gallery scene.
  - Fixed by replacing the solid frame with four separate frame bars and moving the image plane slightly forward.
- Follow-up rule:
  - For 3D gallery/public frontend tasks, visual QA must include not only nonblank canvas checks but also screenshot inspection for occlusion, lighting and readability of the actual products.

## 2026-05-10 — Tatiana Moonn Art Gallery Walkthrough Refinement

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user reviewed the local 3D gallery, left browser comments 1-8 and clarified that the entry doors must open into the real gallery without a persistent background mockup, the camera must approach paintings like a visitor, plaques must be readable, and the code/features sections should match the premium banner direction.
- Route:
  - Continued the existing art-gallery workstream and edited the canonical generator instead of hand-editing generated HTML.
  - Kept the package static and offline-safe; no real payment integration was added.
- Changes:
  - Added animated semi-closed entry doors that fade out after the entrance instead of keeping the concept banner behind the 3D room.
  - Reworked the camera route into explicit artwork stops, with lower look targets so paintings and plaques stay in frame.
  - Brightened opaque gallery walls/floor, added benches and stronger ceiling/wall lighting.
  - Added plaque backplates and corrected center/pedestal plaque placement so the title plaques are visible above the floor.
  - Shortened story-panel visibility windows so text cards do not keep covering paintings after the visitor passes them.
  - Added the `Почему мои картины особенные` feature strip and upgraded `code.html` with the banner-style personal-code section.
  - Regenerated `docs/tatiana-munn-art-gallery/` and `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Generator compiles with `python -m py_compile`.
  - Static build regenerated successfully with `10` artworks.
  - Browser QA via Playwright passed with no console/page errors.
  - Checked screenshots for entry doors, first artwork/plaque, later gallery stops, modal flip, feature strip, code page, and mobile top screen.
  - Code form updates a deterministic numeric result: `928 433 318` in the QA scenario.
  - Public generated-site scan passed for internal strings and local-address leaks in gallery HTML/CSS/JS/JSON/README.
- Incident / correction:
  - During refinement, the entry-door DOM layer initially used the banner image as a persistent background. This made the real 3D walls look transparent and showed duplicate paintings behind the room.
  - Fixed by removing the banner background from the entry layer and making the entry overlay disappear based on scroll progress.
  - A temporary QA script used stale selectors for the flip/code controls; corrected the selectors and added a stable `#codeValue` id.
- Follow-up rule:
  - For generated public frontend packages, always scan the generated output for accidental concept/mockup layers, local-address references and internal wording after regeneration, not only the source generator.

## 2026-05-10 — Tatiana Moonn Art Gallery 3D Material Correction

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user reviewed the 3D gallery again and flagged that wall plaques, floor, walls, ceiling, entry doors, benches, pedestal and artwork relief still looked too flat or like old 2D/game-style assets.
- Route:
  - Continued the existing art-gallery workstream and kept `scripts/build_tatiana_munn_art_gallery_site.py` as the canonical source.
  - Used newly supplied generated scene images as source assets for the gallery environment, with Latin filenames under `assets/scene/`.
  - Kept the bench model sheet as a reference only because it contains working labels and a white presentation background unsuitable for the public scene.
- Changes:
  - Added scene assets for parquet floor, wall panel, coffered ceiling, ornate entry doors and blue tufted bench reference.
  - Replaced the flat sports-like floor with a glossy herringbone/parquet material.
  - Replaced repeated wall-door texture misuse with dark base walls plus separate clean lighted wall panels behind artworks.
  - Added procedural panel trims, ceiling lights, stronger spotlighting and material bump maps.
  - Moved plaque positions up, improved plaque canvas resolution and removed artwork "breathing"; motion is now applied as subtle camera bob only.
  - Added artwork bump/displacement maps and sheen overlays for more tactile canvas relief.
  - Raised and reshaped the central pedestal and corrected the center plaque so it does not sink into the floor.
  - Reworked benches to use geometry, tufting marks, gold trim and straightened shorter legs rather than stretching a 2D bench image onto a box.
  - Regenerated `docs/tatiana-munn-art-gallery/` and `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Generator compiles with `python -m py_compile`.
  - Static build regenerated successfully with `10` artworks.
  - Local page `http://127.0.0.1:8765/` returned `200`.
  - Playwright QA screenshots were saved under `output/playwright/art-gallery-3d-upgrade-3/`.
  - Browser console/page-error log is empty.
  - Public generated-site scan passed for localhost, internal workflow wording, `MVP`/`прототип`, and single-`н` visible `Татьяна Мун` leaks.
- Incident / correction:
  - The first attempt mapped the supplied door image as a repeated side-wall texture, causing door handles to appear behind paintings on the left wall.
  - Fixed by remapping wall panels to the clean lit wall image and restricting door imagery to the entry-door overlay only.
  - Another weak assumption was applying product-like object motion to the painting groups. This made the paintings and plaques feel as if they were jumping; fixed by keeping product geometry static and moving only the camera.
- Follow-up rule:
  - For premium product 3D scenes, do not stretch full reference images onto arbitrary boxes or walls. Use clean texture crops only for matching surfaces, keep working/model sheets out of public assets, and validate by screenshot before reporting.

## 2026-05-11 — Tatiana Moonn Art Gallery Door, Lighting And Plaque Fix

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user reviewed the latest local gallery and flagged that the entry door handles were not mirrored toward the center opening, the gallery became too dark, artwork lights should activate when approaching a painting, and the two center paintings had plaque text visually blocked by stand/floor geometry.
- Route:
  - Continued the existing art-gallery workstream and edited the canonical generator, not the generated HTML by hand.
  - Kept the static package offline-safe; no payment/provider integration was added.
- Changes:
  - Generated `gallery-door-ornate-mirror.webp` and assigned mirrored/original door assets to the left/right entry leaves; disabled the duplicate CSS handle overlay.
  - Increased renderer exposure and ambient/hemisphere/ceiling light intensity, added artwork self-illumination and dynamic warm focus lights for wall panels and individual paintings.
  - Raised central/pedestal artworks so their plaques stay above the parquet plane.
  - Removed center-art pedestal creation and lowered the main pedestal rim so plaque text is no longer covered by stand geometry.
  - Rebuilt plaque textures at higher canvas resolution with stronger type and disabled mipmap blur for readability.
  - Regenerated `docs/tatiana-munn-art-gallery/` and `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Static build regenerated successfully with `10` artworks.
  - Local page `http://127.0.0.1:8765/` returned `200`.
  - Playwright QA screenshots were saved under `output/playwright/art-gallery-door-lighting-fix-2/`.
  - Browser console/page-error log is empty.
  - Public page text scan passed for localhost, `127.0.0.1`, `MVP`, `прототип`, `не дубль` and `технический`.
- Incident / correction:
  - Root cause of blocked center plaque text was geometric, not only styling: center artwork plaques were placed below the floor plane while the central pedestal rim also sat in front of the label area.
  - Root cause of the door issue was reusing a single baked door image for both leaves and adding a separate CSS handle layer, which made handle placement look inconsistent.
- Follow-up rule:
  - For generated 3D product scenes, verify hero entry, mid-gallery lighting and every center/pedestal label after each geometry change; visual labels must clear the floor plane and nearby decorative geometry before the task is reported as ready.

## 2026-05-11 — Tatiana Moonn Art Gallery Main Pedestal Recheck

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user clarified that entry doors are now correct and asked to recheck the remaining issue: the center pedestal under gallery paintings looked partly under the floor / overlapping the lower plaque.
- Route:
  - Rechecked the current local build first instead of assuming the previous fix was complete.
  - Continued editing only the canonical generator `scripts/build_tatiana_munn_art_gallery_site.py`.
- Verified fact:
  - The two later center artworks no longer use the round pedestal and their plaques are readable.
  - The remaining issue was the main round center artwork: the cylindrical pedestal depth and front rim still visually overlapped the lower plaque line.
- Changes:
  - Moved the main pedestal plaque forward relative to the cylinder.
  - Made the main cylinder shallower, lowered it slightly, and moved its decorative rings away from the plaque text zone.
  - Regenerated `docs/tatiana-munn-art-gallery/` and `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Generator compiles with `python -m py_compile`.
  - Public generated-site scan passed for local-address leaks, internal workflow wording and single-`н` visible `Татьяна Мун` leaks.
  - Playwright screenshots were saved under `output/playwright/art-gallery-main-pedestal-fix-20260511/` and confirmed that the main pedestal no longer blocks the plaque text.
- Follow-up rule:
  - When a user reports that a 3D object is “under the floor”, verify both the literal floor-plane relation and the camera/occlusion relation; a front-facing object can look sunken because its depth overlaps a label even if its Y-position is technically above the floor.

## 2026-05-11 — Tatiana Moonn Art Gallery 3D Artwork Replacement

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user supplied the latest 10 generated 3D-style artwork images and asked to replace the existing gallery paintings while preserving their current visual positions.
- Route:
  - Continued the existing art-gallery workstream.
  - Edited only the canonical generator `scripts/build_tatiana_munn_art_gallery_site.py`; generated HTML/JS/CSS were rebuilt from it.
  - Kept existing artwork slugs, titles, prices, placement and scene coordinates so downstream links and detail pages remain stable.
- Changes:
  - Replaced all 10 `Artwork.source` image paths with the latest `2026-05-11 00_08` generated images from Downloads.
  - Mapped images by visual identity: central blue flower, turquoise eye, lotus balance, violet resource mandala, orchid rings, speed restoration, financial realization, sensitivity, eye vortex and wide gate composition.
  - Regenerated all `assets/art/*.webp` and thumbnails under `docs/tatiana-munn-art-gallery/`.
  - Updated the internal build-report single-`н` check to avoid a false grep match from the validator string itself.
  - Regenerated `docs/tatiana-munn-art-gallery/` and `output/tatiana-munn-art-gallery-site.zip`.
- Verification:
  - Generator compiles with `python -m py_compile`.
  - Static build regenerated successfully with `10` artworks.
  - Public generated-site scan passed for localhost/`127.0.0.1`, internal workflow wording and single-`н` visible `Татьяна Мун` leaks.
  - Build report checks passed: double-`н` name present, single-`н` visible hits `0`, Three.js present, purchase drawer present, artwork JSON present, asset names are Latin.
  - Playwright QA loaded all 10 new artwork webp files; nine square/round images loaded at `1254x1254`, the wide artwork loaded at `1448x1086`.
  - Browser QA screenshots were saved under `output/playwright/tatiana-gallery-art-replace/`; console/page-error and failed-request logs are empty.
- Follow-up rule:
  - For future artwork swaps, change only source image mapping in the generator and verify the rebuilt manifest plus browser-loaded asset dimensions before reporting readiness.

## 2026-05-11 — Tatiana Moonn Art Gallery Tilda Publication Paused

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user asked to stop the gallery publication task safely and continue later, then switched to a separate consultation-banner/payment task for the homepage.
- Route:
  - Kept the gallery workstream on its existing branch and did not mix it with the new consultation-banner workstream.
  - Created a pause handoff: `docs/codex-handoffs/2026-05-11-art-gallery-tilda-publication-pause.md`.
- Current state:
  - The art-gallery generator has partial Tilda/CDN/payment preparation fields.
  - `scripts/build_tatiana_munn_art_gallery_site.py` compiles with `python -m py_compile`.
  - No Tilda publication was performed for the gallery in this paused step.
  - No gallery payment flow was tested in this paused step.
- Next step for this workstream:
  - Resume from the handoff, finish native Tilda-cart bridge and Tilda-ready artifacts, then run local and live verification before publishing.
- Follow-up rule:
  - When a user pauses a public/payment workstream mid-change, checkpoint the exact branch and unfinished scope before switching tasks; do not carry partial public/payment changes into the next workstream.

## 2026-05-11 — Tatiana Moonn Art Gallery Tilda Packet Resumed

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user asked to resume the frozen gallery publication workstream, create a Tilda page for the art gallery, and add a homepage banner linking to it near the consultation banner.
- Route:
  - Continued the existing gallery branch instead of using the consultation-banner branch.
  - Edited the canonical generator `scripts/build_tatiana_munn_art_gallery_site.py`, not generated HTML by hand.
  - Kept live Tilda publication as a separate high-risk step requiring real page/cart verification.
- Changes:
  - Added Tilda-safe gallery artifacts: `tilda-html-block-final.html`, `tilda-page-final.html`, `tilda-head-loader-final.html`, `tilda-head-seo-final.html`.
  - Added homepage banner artifact: `homepage-art-gallery-block-final.html`.
  - Added native Tilda cart product manifest: `data/tilda-payment-products.json`.
  - Strengthened generated `app.js` so artwork payment buttons use native Tilda cart/T-Bank through `tcart__addProduct`, `tcart__reDrawCartIcon`, `tcart__openCart`, and repair native T706 order-form handlers.
  - Fixed generator asset rebuild logic so scene/art assets are reachable inside `build_assets()` instead of dead code after a `return`.
- Verification:
  - `python -m py_compile scripts\build_tatiana_munn_art_gallery_site.py` passed.
  - `python scripts\build_tatiana_munn_art_gallery_site.py` regenerated the gallery, Tilda packet, payment products and ZIP.
  - Local Playwright desktop/mobile checks confirmed the generated gallery renders and the first screen is not blank.
  - Generated build report confirms Tilda page, homepage banner, payment-products manifest and Latin asset names.
- Publication gate:
  - Live Tilda page creation/update is still pending.
  - Homepage banner insertion is still pending.
  - Do not submit a real payment during QA.
  - Before reporting completion, verify live page marker `moonn-art-gallery-tilda-page`, homepage marker `moonn-art-gallery-home-banner`, native cart amount/name for at least one artwork, and T-Bank provider transition without card submission.

## 2026-05-12 — Tatiana Moonn Art Gallery Published On Tilda

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user reported that the gallery banner was absent on the homepage and asked to verify whether the gallery page was really created in Tilda.
- Route:
  - Continued the gallery workstream in `codex/moonn-art-gallery`.
  - Confirmed through Tilda API and live HTML that `/kartiny-tatiany-munn` did not yet exist before this step.
  - Created a new Tilda page instead of reusing the consultation-banner branch.
- Changes:
  - Created Tilda page `140864526` with alias `kartiny-tatiany-munn`.
  - Added gallery `T123` record `2258253531` and native cart `ST100` / `T706` record `2258267581`.
  - Inserted the gallery homepage banner into existing homepage T123 record `2251351151`, preserving teen-camp and consultation markers.
  - Added evidence artifact `docs/tatiana-munn-art-gallery/homepage-t123-combined-2026-05-12.html`.
- Verification:
  - Gallery live HTML: status `200`, marker `moonn-art-gallery-tilda-page` present, cart markers present, first artwork SKU present, SoundCloud absent.
  - Gallery browser render: page title correct, `#galleryCanvas` present, native cart present, SoundCloud absent.
  - Homepage live HTML: status `200`, teen-camp marker present, gallery banner marker present, consultation marker present, gallery link present, SoundCloud absent.
  - Homepage browser render: gallery banner visible and button links to `/kartiny-tatiany-munn`.
  - Gallery cart smoke test after clearing previous cart state: first artwork opened native cart with SKU `moonn-art-gallery-01-blue-flower-harmony` and amount `700 000р.`.
  - No real payment was submitted.
- Incident:
  - Wrong draft attempt used Tilda internal template id `123`, which is a SoundCloud/media block, not T123 custom HTML.
  - The erroneous unpublished draft page `140863116` was deleted and verified absent through Tilda API.
- Follow-up rule:
  - For Tilda custom HTML blocks, use and verify `data-record-type="131"` plus the target marker before publishing; do not infer custom HTML from template id `123`.

## 2026-05-12 — Tatiana Moonn Art Gallery Compact Homepage Banner

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Trigger: user confirmed the gallery page looked good, then clarified that the homepage gallery banner should be a compact rectangular block directly below the teen-camp banner, in the same visual family, not the previous dark premium banner.
- Route:
  - Continued the existing gallery workstream.
  - Kept teen-camp and consultation workstreams untouched.
  - Updated the canonical generator first, then regenerated the homepage T123 evidence artifact.
- Changes:
  - Reworked `homepage-art-gallery-block-final.html` into a light compact banner matching the teen-camp block structure: text left, image right, pill metadata, gradient CTA.
  - Updated `homepage-t123-combined-2026-05-12.html` to preserve homepage order: teen camp -> gallery -> consultation.
  - Saved the refreshed T123 code into existing homepage Tilda record `2251351151`.
  - Published the homepage from the logged-in Tilda editor.
- Verification:
  - `python -m py_compile scripts\build_tatiana_munn_art_gallery_site.py` passed.
  - Generator rebuild passed with `10` artworks.
  - Local browser preview confirmed gallery block width `1160`, height `577`, teen block height `565`, CTA `/kartiny-tatiany-munn`, old dark CSS absent.
  - GitHub raw artifact for commit `c8efbdcd381daafc3c95c83103c8dc43aec26835` returned `200`, compact marker present, old dark marker absent.
  - Tilda save confirmation: `saved home T123 22155 compact=true`.
  - Live homepage HTML returned `200`, teen/gallery/consultation markers present, gallery link present, compact CSS marker present, old dark marker and SoundCloud absent.
  - Browser screenshot artifacts:
    - `docs/tatiana-munn-art-gallery/homepage-gallery-compact-preview-2026-05-12.png`
    - `docs/tatiana-munn-art-gallery/homepage-gallery-compact-live-viewport-2026-05-12.png`
    - `docs/tatiana-munn-art-gallery/homepage-gallery-compact-live-2026-05-12.png`
- Commits:
  - `c8efbdc` prepared and pushed the compact banner source/artifacts before Tilda fetch.
- Follow-up rule:
  - For homepage promo blocks, verify not only marker presence but visual proportion against adjacent blocks; a banner can be technically live and still fail if its scale/palette does not match the neighboring canonical promo block.

## 2026-05-12 — Tatiana Moonn Exam Prep Tilda Packet

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-exam-prep-tilda`.
- Trigger: user asked to publish the self-contained exam-prep landing from Downloads and add a compact homepage banner below the art-gallery banner.
- Route:
  - Started from `origin/codex/moonn-art-gallery` to preserve the latest homepage T123 ordering.
  - Kept the exam-prep publication as a separate workstream from the art-gallery and consultation payment workstreams.
- Prepared artifacts:
  - `docs/tatiana-munn-exam-prep/tilda-html-block-final.html`
  - `docs/tatiana-munn-exam-prep/tilda-page-final.html`
  - `docs/tatiana-munn-exam-prep/homepage-exam-prep-block-final.html`
  - `docs/tatiana-munn-exam-prep/homepage-t123-combined-2026-05-12.html`
  - `docs/tatiana-munn-exam-prep/manifest.json`
- Publication target:
  - Intended URL: `https://moonn.ru/psihologicheskaya-podgotovka-k-ekzamenam`.
  - Homepage T123 record: `2251351151`.
- Verification gates before completion:
  - Live page marker `moonn-exam-prep-tilda-page` present.
  - Homepage marker `moonn-exam-prep-home-banner` present below `moonn-art-gallery-home-banner`.
  - Link `/psihologicheskaya-podgotovka-k-ekzamenam` opens the exam-prep page.
  - No SoundCloud/media block regression.

## 2026-05-12 — Tatiana Moonn Exam Prep Tilda Publication Completed

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-exam-prep-tilda`.
- Trigger: continue the exam-prep publication request after the generated Tilda packet was prepared.
- Decisions:
  - Preserved the existing Tilda alias `psypodgotovka1` instead of creating a duplicate long alias.
  - Used a lightweight native T123 loader for the exam-prep page because the self-contained HTML is large due to inline images.
  - Kept root `codex/ano-context-recovery` context-backup/screenshot changes out of the Moonn publication commit.
- Tilda updates:
  - Published page `62652841` at `https://moonn.ru/psypodgotovka1`.
  - Updated page T123 record `2258994191`.
  - Updated homepage T123 record `2251351151`.
  - Published homepage `42678538` at `https://moonn.ru/`.
- GitHub:
  - Pushed branch `codex/moonn-exam-prep-tilda`.
  - Latest pushed commit before live publication checks: `72059438c1fcba2433af7055f729a9a8556583d1`.
- Verification:
  - Tilda API and live HTML for `https://moonn.ru/psypodgotovka1` contain the exam-prep loader marker and no SoundCloud marker.
  - Browser render confirms full page marker `moonn-exam-prep-tilda-page`, H1 `Психологическая подготовка к экзаменам без паники`, and form presence.
  - Tilda API and live HTML for homepage contain markers in order: teen camp, art gallery, exam prep, consultation.
  - Browser render confirms homepage banner title `Экзамены без паники` and CTA href `/psypodgotovka1`.
- Evidence:
  - `docs/tatiana-munn-exam-prep/publication-report-2026-05-12.md`
  - `docs/tatiana-munn-exam-prep/exam-prep-live-render-2026-05-12.png`
  - `docs/tatiana-munn-exam-prep/homepage-exam-prep-live-render-2026-05-12.png`

## 2026-05-12 — Tatiana Moonn Exam Prep SEO Gate Correction

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-exam-prep-tilda`.
- Trigger: user reminded that published pages must keep the earlier Moonn SEO optimization and be visible in search.
- Incident:
  - Initial visual/browser publication was correct, but raw live HTML still contained old Tilda page content with multiple stale H1 headings.
  - Root cause: the custom T123 loader hid old records at runtime, but legacy Tilda records were still published server-side and visible to crawlers.
  - Algorithm correction: for Tilda loader-based replacements, do not close publication on rendered DOM alone; verify raw HTML, Tilda meta fields and legacy-record state.
- Changes:
  - Added a SEO-visible loader fallback with one H1 to `scripts/build_tatiana_munn_exam_prep_tilda.py`.
  - Regenerated `docs/tatiana-munn-exam-prep/tilda-html-loader-final.html` and `manifest.json`.
  - Pushed commit `9126a5d` before Tilda update.
  - Updated page T123 record `2258994191` from the pushed CDN artifact.
  - Switched off `19` legacy Tilda records on page `62652841`.
  - Updated Tilda page SEO settings: title, description, canonical and indexing flags.
  - Republished `https://moonn.ru/psypodgotovka1`.
- Verification:
  - Live raw HTML returns title `Психологическая подготовка к ОГЭ и ЕГЭ — Татьяна Мунн`.
  - Live raw HTML returns canonical `https://moonn.ru/psypodgotovka1`.
  - Live raw HTML has exactly one H1: `Психологическая подготовка к экзаменам без паники`.
  - Old lecture H1/text markers and SoundCloud markers are absent.
  - Playwright render confirms full page marker, form presence, no SoundCloud iframe, no failed requests and no page errors.
- Evidence:
  - `docs/tatiana-munn-exam-prep/publication-report-2026-05-12.md`
  - `docs/tatiana-munn-exam-prep/exam-prep-seo-render-debug-2026-05-12.png`
- Follow-up rule:
  - For every future Moonn/Tilda page publication, SEO gate is mandatory before completion: Tilda meta fields, canonical, raw H1 count, old record visibility, browser render and report update.

## 2026-05-12 — Moonn Homepage Consultation Banner Layout Incident

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-homepage-consultation-fix`.
- Trigger: user reported that the homepage block `Онлайн-консультации для вас и ваших близких` stretched down and overlapped the next native Tilda sections, while the teen camp, art gallery and exam-prep banners were visually correct.
- Incident:
  - Symptom: consultation banner became unbounded and absorbed lower homepage content.
  - Root cause: the combined homepage T123 artifact was truncated inside the consultation summer-price markup and did not close the section.
  - Algorithm correction: homepage publication cannot be closed by marker/order checks alone; compact banner insertions must pass rendered bounding-box checks against neighboring blocks.
- Changes:
  - Added `scripts/fix_moonn_homepage_consultation_banner.py`.
  - Replaced the broken consultation section in the exam-prep and art-gallery combined homepage artifacts with a compact bounded section.
  - Preserved Tilda native cart bridge, product SKUs `moonn-consultation-online-1-2026` and `moonn-consultation-online-3-summer-2026`, and public Timepad detail link.
- Verification:
  - `python -m py_compile scripts\fix_moonn_homepage_consultation_banner.py`
  - Local Playwright preview at 1280px, 825px and 390px confirmed correct block order and no overlap.
  - At 825px, consultation banner height is `519px`, close to the adjacent compact promo blocks.
  - Tilda homepage T123 record `2251351151` was updated from pushed commit `ab2d71861f04d9171cf7b8a68de1fb00777fe11a` and the homepage was published.
  - Live raw HTML contains `data-moonn-consultation-compact="2026-05-12"` and does not contain `moonn-consultation-home-signature`.
  - Live Playwright render at 825px confirms consultation banner height `519px`; `Татьяна Мунн / Направления` starts at the banner bottom with no overlap.
- Evidence:
  - `docs/consultation-home-banner-2026/homepage-consultation-layout-fix-report-2026-05-12.md`
  - `docs/consultation-home-banner-2026/homepage-consultation-compact-preview-2026-05-12.json`
  - `docs/consultation-home-banner-2026/homepage-consultation-compact-live-2026-05-12.json`
- Follow-up rule:
  - For homepage T123 combined blocks, always validate valid closing markup plus rendered adjacent bounding boxes before publishing to Tilda.

## 2026-05-12 — Moonn SEO Positioning Architecture Audit

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-seo-positioning-architecture`.
- Trigger: user provided a strategic SEO/positioning analysis and asked to verify it, avoid occupying visible Chrome/Tilda, focus on open public pages only, and define a stronger site architecture before implementation.
- Decisions:
  - Treat this as a planning/governance workstream, not a Tilda publication task.
  - Analyze open semantic public pages as positioning assets; treat closed, opaque, test, legal and transactional URLs as hygiene, not SEO clusters.
  - Agree with the core diagnosis: the site currently dilutes Tatyana Munn's entity across too many equal-weight topics.
  - Collapse positioning into three lanes: private practice, emotional intelligence/leadership, teens/exams/family support.
  - Do not use visible Chrome/Tilda for this planning pass; use repository, HTTP checks and headless audits.
- Created or changed files:
  - `scripts/build_moonn_positioning_architecture.py`
  - `docs/moonn-final-seo-audit-2026-05-12.json`
  - `docs/moonn-final-seo-audit-2026-05-12.md`
  - `docs/moonn-final-seo-audit-2026-05-12.csv`
  - `docs/moonn-public-positioning-map-2026-05-12.json`
  - `docs/moonn-public-positioning-map-2026-05-12.csv`
  - `docs/moonn-positioning-architecture-2026-05-12.md`
- Verification:
  - `python scripts\moonn_final_seo_audit.py` checked `151` live URLs.
  - `python scripts\build_moonn_positioning_architecture.py` generated the public URL map and strategy.
  - `python -m py_compile scripts\build_moonn_positioning_architecture.py` passed.
- Key findings:
  - `45` opaque/test/numeric URLs should be redirected, renamed or deindexed.
  - `92` pages have no detected H1; `16` have multiple H1; `33` duplicate descriptions.
  - Homepage raw HTML currently has `5` H1 elements and mixes unrelated semantic blocks.
  - `/psiholog` is a cleaner private-practice pillar candidate but lacks raw H1.
  - `/speaker` is the cleanest current emotional-intelligence/speaker page.
  - Off-topic wellness pages and gallery should not be equal SEO signals for the psychology/EI entity.
- Commit: pending.

## 2026-05-12 — Moonn SEO Repositioning Pipeline Implementation

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-seo-positioning-architecture`.
- Trigger: user approved the Moonn SEO Repositioning Implementation Plan and asked to implement the new SEO/AIOSEO algorithm.
- Decisions:
  - Implement the new pipeline as deterministic GitHub artifacts first: public URL decision register -> cluster assignment -> index/canonical decision -> SEO packet -> AI/AEO/schema packet -> Tilda apply queue -> verification gates.
  - Treat AIOSEO as both the internal SEO packet generator and the visible AI/AEO/schema/entity layer.
  - Use the Tilda API only for read/export verification and page-id sync; do not write live Tilda changes through undocumented endpoints.
  - Keep the gallery public as `secondary`, not as a psychology SEO pillar.
  - Keep live Tilda mass apply blocked until a non-visual write-capable path is proven or explicitly replaced by a scoped supported UI pilot.
- Tilda API verification:
  - Official read-only API access was verified for project `8326812` (`Moonn.ru`).
  - `getpageslist` returned `166` pages and confirmed core aliases `psiholog`, `speaker`, `psypodgotovka1`, `otzivi`, `kartiny-tatiany-munn`.
  - New gallery page id synced into the generator fallback map: `140864526`.
- Created or changed files:
  - `scripts/build_moonn_seo_repositioning_packets.py`
  - `docs/moonn-seo-repositioning-2026-05-12/url-decision-register.json`
  - `docs/moonn-seo-repositioning-2026-05-12/url-decision-register.csv`
  - `docs/moonn-seo-repositioning-2026-05-12/seo-aeo-tilda-apply-packets.json`
  - `docs/moonn-seo-repositioning-2026-05-12/seo-aeo-tilda-apply-packets.md`
  - `docs/moonn-seo-repositioning-2026-05-12/search-reindex-packet.json`
  - `docs/moonn-seo-repositioning-2026-05-12/homepage-strategic-gateway-tilda-block.html`
  - `docs/moonn-seo-repositioning-2026-05-12/implementation-report.md`
- Verification:
  - `python -m py_compile scripts\build_moonn_seo_repositioning_packets.py`
  - `python scripts\build_moonn_seo_repositioning_packets.py`
  - Dry-run register classified all `151` audited URLs with no `review` action left.
  - Actions: `81` rewrite, `18` redirect, `47` noindex, `5` keep indexed.
  - Clusters: `private_practice`, `emotional_intelligence`, `teen_exam_family`, `reviews_trust`, `secondary`, `archive`.
  - Determinism check passed: repeated generator run did not change output hashes.
  - Secret/local-path scan passed for generated artifacts and generator.
  - Homepage gateway block has exactly one H1.
  - Reviews schema packet contains no `AggregateRating`.
- Follow-up rule:
  - Future Moonn SEO live changes must be applied from the URL decision register, not directly from sitemap enumeration. Tilda API read/export can verify state and page ids; live writes require a documented write path or a scoped supported UI pilot with raw HTML and browser verification.
- Commit: pending.

## 2026-05-12 — Moonn SEO Repositioning Partial Live Rollout and Chrome Incident

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-seo-positioning-architecture`.
- Trigger: user asked to start implementing the five live SEO changes, then objected that Chrome was being closed/reopened and required repeated robot checks.
- Applied live:
  - SEO settings and publish: `/`, `/psiholog`, `/speaker`, `/emotional-intelligence/`, `/psypodgotovka1`, `/otzivi`.
  - Noindex/nofollow and publish: `/aromatherapy`, `/geshtalt`, `/kpt`, `/microbiom`, `/water`, `/salt`, `/vacuum_cups`, `/phytotherapy`.
- Verification:
  - Raw HTTP checks confirmed updated titles/canonicals on core pages.
  - `/speaker` and `/psypodgotovka1` have raw H1 count `1`.
  - Homepage still has raw H1 count `5`.
  - `/psiholog` and `/emotional-intelligence/` still have raw H1 count `0`.
  - `/otzivi` still has raw H1 count `2`.
- Incident:
  - Symptom: UI automation disturbed the user's visible Chrome session and caused re-opening/re-authentication friction.
  - Root cause: after Tilda publication, DevTools/Tilda UI state sometimes hid Chrome address bar controls from UIA; the recovery path included DevTools toggling and one Chrome launch.
  - Correction: stopped live UI automation immediately after the user's objection; do not recover Tilda UI failures by restarting Chrome.
  - Follow-up rule: remaining live SEO rollout must use a verified non-visual write path or a user-approved scheduled visible Tilda session. If Chrome state is unstable, stop and report instead of restarting or taking over.
- Evidence:
  - `docs/moonn-seo-repositioning-2026-05-12/tilda-seo-ui-live-apply-report.json`
  - `docs/moonn-seo-repositioning-2026-05-12/live-rollout-status-2026-05-12.md`
- Commit: pending.

## 2026-05-12 — Moonn SEO Repositioning Noindex Queue Continuation

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-seo-positioning-architecture`.
- Trigger: user explicitly allowed continuing the visible Tilda session, with the constraint to use only the already-open Alexander Google Chrome profile and not Chromium-Gost or a new browser.
- Applied live through scoped Tilda UI:
  - Completed the full noindex queue from the repositioning register: `47/47` pages had noindex/nofollow saved in Tilda page settings.
  - Published each affected page from its page editor; no project-wide publish-all was used.
- Automation corrections:
  - Pinned Chrome selection to `Google Chrome` windows.
  - Expanded the save-button matcher from only `Сохранить изменения` to also accept `Сохранить`.
  - Forced reset to `tilda.ru/projects/?projectid=8326812` before each page settings edit.
  - Fixed publish-popup closing so it does not click the Chrome tab close button.
  - Added reusable live noindex verifier `scripts/verify_moonn_noindex_live.py`.
- Verification:
  - `python -m py_compile scripts\tilda_apply_moonn_repositioning_seo_ui.py` passed after each script correction.
  - `python -m py_compile scripts\verify_moonn_noindex_live.py` passed.
  - `python scripts\verify_moonn_noindex_live.py --delay 0.05` refreshed the noindex verification report and exited non-zero because not all URLs are live-confirmed yet.
  - `python scripts\moonn_final_seo_audit.py` completed and refreshed `docs/moonn-final-seo-audit-2026-05-12.*`.
  - `docs/moonn-seo-repositioning-2026-05-12/noindex-live-verification-2026-05-12.json` checked all `47` noindex URLs.
  - Immediate raw HTML noindex result: `18/47` confirmed live; `29/47` remain delayed or not propagated, mostly numeric `page*.html` URLs.
- Incident update:
  - Symptom: earlier close-popup logic could select the Chrome tab close button because it matched any visible `Закрыть`.
  - Root cause: popup close predicate was too broad and sorted by top-left coordinates.
  - Correction: popup close is now constrained to the Tilda popup area only.
  - Follow-up rule: Tilda UI scripts must distinguish browser chrome controls from Tilda modal controls by coordinate/window-region constraints before clicking destructive or closing controls.
- Remaining:
  - Recheck the delayed noindex pages after cache/publish propagation.
  - If numeric `page*.html` URLs still do not expose noindex, switch to redirect/remove-from-sitemap governance rather than repeating page settings saves.
  - Homepage gateway/H1, core H1 cleanup, schema/AEO visible answer sections, redirect queue and reindex packet are still open.
- Commit: pending.

## 2026-05-15 — Moonn SEO Repositioning Noindex Cache Recheck

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-seo-positioning-architecture`.
- Trigger: scheduled heartbeat `moonn-noindex-cache-recheck`.
- Scope: recheck noindex propagation only; no Chrome, Tilda UI, redirects, payments, secrets, deletion, or public publication.
- Verification:
  - Ran `python scripts\verify_moonn_noindex_live.py --delay 0.05`.
  - Refreshed `docs/moonn-seo-repositioning-2026-05-12/noindex-live-verification-2026-05-12.json`.
  - Current confirmed noindex count remains `18/47`.
  - Missing noindex remains `29/47`, mostly numeric `page*.html` URLs plus `/schematherapy`.
- Decision:
  - Delayed pages still need a redirect/remove-from-sitemap route or a verified non-visual Tilda write path.
  - Do not repeat blind Tilda UI saves for the delayed set.
- Updated files:
  - `docs/moonn-seo-repositioning-2026-05-12/noindex-live-verification-2026-05-12.json`
  - `docs/moonn-seo-repositioning-2026-05-12/live-rollout-status-2026-05-12.md`
  - `docs/codex-chat-history.md`

## 2026-05-15 — Moonn Timepad Registration Bridge

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-timepad-registration-bridge`.
- Trigger: user asked to move the Timepad direct-registration helper from `school.miiiips.ru` to the canonical `moonn.ru` domain.
- Decision:
  - Use one noindex Tilda page with query parameter `?lecture=N` instead of seven duplicate public pages.
  - Keep Timepad as the payment/registration processor; the Moonn page is only a UX bridge to the selected recurring session.
- Prepared artifacts:
  - `data/moonn-timepad-registration-bridge.json`
  - `scripts/build_moonn_timepad_registration_bridge.py`
  - `docs/moonn-timepad-registration-bridge/tilda-html-block-final.html`
  - `docs/moonn-timepad-registration-bridge/tilda-page-final.html`
  - `docs/moonn-timepad-registration-bridge/manifest.json`
- Publication target:
  - `https://moonn.ru/timepad-registration?lecture=7`
- Verification gate:
  - Local and live browser checks must confirm that the selected Timepad registration form opens directly, not the recurring date list.

### Publication result

- Published Tilda page `141821916` at `https://moonn.ru/timepad-registration`.
- Saved native T123 record `2273574411` with the generated bridge block.
- Set alias `timepad-registration`, page title `Регистрация на лекцию Татьяны Мунн`, and noindex bridge behavior.
- Live raw HTML check:
  - status `200`;
  - marker `moonn-timepad-registration-bridge` present;
  - Timepad widget marker present;
  - `noindex` present;
  - H1 count `1`;
  - SoundCloud marker absent.
- Rendered browser check:
  - `https://moonn.ru/timepad-registration?lecture=9` opened the selected form for `1 июня 2026, 19:00`;
  - `E-mail`, `Фамилия`, `Имя`, `Телефон (Whatsapp)` fields visible;
  - recurring date list absent.
- Evidence:
  - `docs/moonn-timepad-registration-bridge/publication-report-2026-05-15.md`
  - `docs/moonn-timepad-registration-bridge/live-bridge-lecture-09-2026-05-15.png`
