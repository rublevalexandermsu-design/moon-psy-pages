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
