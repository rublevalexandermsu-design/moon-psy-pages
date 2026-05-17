# Moonn Homepage Reviews Banner — 2026-05-17

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: homepage promotion banners and reviews trust route.
- Branch: `codex/moonn-homepage-reviews-banner`.
- Target homepage: `https://moonn.ru/`.
- Canonical reviews page: `https://moonn.ru/otzivi`.

## Verified Facts

- Live homepage returned `200` on 2026-05-17.
- Live homepage already contains the existing homepage promo blocks:
  - `moonn-teen-camp-home-banner`;
  - `moonn-art-gallery-home-banner`;
  - `moonn-exam-prep-home-banner`;
  - `moonn-consultation-home-banner`.
- Initial live homepage check did not contain `moonn-reviews-home-banner`.
- After Tilda publication on 2026-05-17, live homepage raw HTML contains `moonn-reviews-home-banner`.
- Live reviews page `https://moonn.ru/otzivi` returned `200` on 2026-05-17.
- Live reviews page contains the Yandex reviews runtime layers and the canonical Yandex Services profile id `TatyanaKumskovamunn-948629`.

## Decision

Create one new homepage banner that points to `/otzivi`. Do not create a second reviews page and do not claim an unverified review count or rating in the homepage banner.

## Prepared Artifacts

- `docs/tatiana-munn-reviews-home-banner/tilda-html-block-final.html`
- `docs/tatiana-munn-reviews-home-banner/homepage-reviews-banner-preview.html`
- `docs/tatiana-munn-reviews-home-banner/manifest.json`

## Tilda Placement Packet

- Updated existing homepage T123 record `2251351151` on Tilda page `42678538`.
- Appended `tilda-html-block-final.html` into the same homepage promo-banner family after the consultation banner.
- Published the homepage only.
- Do not edit the global homepage HEAD for this placement.

## Publication Result

- Published URL: `https://moonn.ru/`.
- Raw live HTML check:
  - `moonn-reviews-home-banner`: present;
  - `/otzivi`: present;
  - existing homepage markers still present:
    - `moonn-teen-camp-home-banner`;
    - `moonn-art-gallery-home-banner`;
    - `moonn-exam-prep-home-banner`;
    - `moonn-consultation-home-banner`.
- Browser verification:
  - desktop reviews block screenshot: `live-reviews-block-desktop-2026-05-17.png`;
  - mobile reviews block screenshot: `live-reviews-block-mobile-2026-05-17.png`;
  - CTA click from the new homepage banner opens `https://moonn.ru/otzivi`;
  - `/otzivi` contains `moonn-yandex-reviews-quality-layer`.
- Layout verification:
  - desktop: no overflow inside `#moonn-reviews-home-banner`;
  - mobile: no overflow inside `#moonn-reviews-home-banner`;
  - global mobile page overflow existed outside the new reviews block and is not introduced by this change.

## Publication Gate

Before calling this live:

- raw homepage HTML contains `moonn-reviews-home-banner`;
- rendered homepage shows the banner on desktop and mobile without text overflow;
- both CTA and right-side media panel navigate to `/otzivi`;
- `/otzivi` returns `200`;
- visible public text has no internal implementation language.

## Follow-up Rule

Future homepage promotion cards should be treated as a canonical banner family: one isolated Tilda block per promoted route, each with a manifest, preview, live marker, and browser verification.

Tilda publication popup or visible editor state is not sufficient evidence. A homepage Tilda change is complete only after raw live HTML marker verification and browser/click verification.
