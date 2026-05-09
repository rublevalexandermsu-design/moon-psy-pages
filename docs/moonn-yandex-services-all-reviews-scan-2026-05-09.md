# Moonn Yandex Services All Reviews Scan — 2026-05-09

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: Yandex Services reviews completeness for `https://moonn.ru/otzivi`.
- Source profile checked: `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`.
- Related public page: `https://moonn.ru/otzivi`.

## Verified Facts

- The Yandex Services profile exposes a reviews section in rendered browser output.
- The rendered profile showed `190 оценок`.
- Browser scan on 2026-05-09 collected `136` unique visible text-review records across the paginated reviews UI.
- `190 оценок` should not be treated as `190` public text reviews: ratings can exist without public text.
- Current Moonn schema layer contains only a small review-summary subset, so it is not yet an all-reviews layer.

## Decision

The target state for `moonn.ru/otzivi` should be:

- all public text reviews that are visible on Yandex Services;
- one card per unique review;
- author/display name, date, text, and source/provenance link where available;
- no invented ratings, no invented review count, no hidden SEO wording;
- clear distinction between Yandex-sourced reviews and reviews submitted directly on `moonn.ru`.

## Publication Gate

Do not publish all Yandex review texts verbatim to `moonn.ru` until this gate is passed:

1. Confirm the copyright/platform policy posture for republishing Yandex Services user review text on an external site.
2. Confirm personal-data/public-distribution posture for reviewer display names and review text.
3. Decide whether full text is permitted, or whether the safer format is excerpt/summary + source link.
4. If full text is approved, generate a canonical reviews manifest and render all review cards from that manifest.
5. If full text is not approved, render all review records as short summaries/excerpts with source links.
6. Verify live page: card count, source links, no duplicate cards, no internal SEO text, rendered JSON-LD count matches the public page count used.

## Recommended Architecture

Use a machine-first manifest rather than hard-coding review cards in Tilda:

- `registry/reviews/moonn-yandex-services-reviews.schema.json`
- `registry/reviews/moonn-yandex-services-reviews.manifest.json`
- runtime renderer for `/otzivi`
- audit script that compares Yandex visible count against manifest count
- moderation queue for new reviews submitted directly on `moonn.ru`

## Current Status

- All-reviews requirement identified and quantified.
- Full text publication is blocked pending legal/platform gate.
- Safe next implementation step: build manifest schema and renderer, but keep full-text publication disabled until approval.
