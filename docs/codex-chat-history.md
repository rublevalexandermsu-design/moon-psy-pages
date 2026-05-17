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

## 2026-05-17 — Paid Lecture Checkout Price And Bundle Contract

- Project: Moonn / Tilda site.
- Workstream: paid video lectures and protected access.
- Branch: `codex/moonn-paid-video-lectures`.
- User request:
  - return to the paid lecture page task while iClient access is pending;
  - turn the existing `events_tp` lecture page into a paid recording storefront;
  - set each lecture recording price to `2000 RUB`;
  - add a `5000 RUB` package for five recordings on choice;
  - after payment, show the recording inside the site rather than sending visitors away to YouTube;
  - include Tatyana Munn's Telegram/support route for access problems.
- Decisions:
  - Continue the existing `codex/moonn-paid-video-lectures` branch instead of mixing this with the Timepad consultation sync branch.
  - Keep `https://moonn.ru/events_tp` / Tilda page `66814657` as the canonical storefront.
  - Use Tilda catalog/cart plus Members/Courses protected pages as the access model.
  - Treat raw YouTube/unlisted links as insufficient copy protection; do not use them as public fulfillment.
  - Use the five-recording bundle as a separate product with post-payment selection/access registry, not as five unrelated cart items.
- Created or changed files:
  - `scripts/prepare_paid_video_lecture_products.py`
  - `registry/products/paid-video-lectures.schema.json`
  - `registry/products/paid-video-lectures.manifest.json`
  - `registry/products/paid-video-lectures-tilda-catalog-2026-05-17.csv`
  - `docs/paid-video-lectures-checkout-2026-05-17.md`
  - `docs/paid-video-lectures-tilda-plan-2026-05-03.md`
  - `docs/codex-chat-history.md`
- Verified:
  - manifest price contract is now single `2000`, bundle `5000`, bundle size `5`;
  - generated Tilda CSV contains 10 lecture products plus 1 bundle product;
  - generated manifest/CSV contain no raw YouTube watch/embed URLs;
  - official Tilda docs confirm cart/payment plus Members access after successful payment and CSV/YML catalog import;
  - official YouTube Help confirms unlisted videos are accessible/shareable by anyone with the link.
- Open questions / blockers:
  - Confirm Tatyana Munn's exact Telegram URL/handle before adding it to public fulfillment text.
  - Verify current Tilda payment provider/seller settings in the UI before live checkout.
  - Create protected watch pages/groups for the five uniquely matched recordings first.
  - Owner still needs to choose correct videos for four ambiguous YouTube matches and decide how to treat `3334362`.
- Risk notes:
  - Money/payment settings and paid content access remain high-risk; do not publish live payment flow before visual checkout and access testing.
  - If a buyer can pay before a watch page exists, the operation needs a controlled pending-access process and support SLA.
