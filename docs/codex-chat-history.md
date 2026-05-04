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
