# Moonn Review Funnel Architecture - 2026-05-18

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: Yandex Services rating + Moonn-owned text review intake.
- Existing branch: `codex/moonn-homepage-reviews-banner`.
- Canonical reviews page: `https://moonn.ru/otzivi`.
- Tilda page id: `81167556`.
- QR target: `https://moonn.ru/otzivi?ostavit-otzyv=1&source=qr_event#moonn-review-funnel`.
- Homepage entry target: `https://moonn.ru/otzivi?ostavit-otzyv=1&source=homepage_reviews_banner#moonn-review-funnel`.
- Updated entry behavior: the review-intake form is visible only when `ostavit-otzyv=1` is present in the URL, for example `https://moonn.ru/otzivi?ostavit-otzyv=1&source=homepage_reviews_banner#moonn-review-funnel`.

## Strategic Check

- Platform value: high. Reviews and ratings are a trust layer for consultations, lectures, camps, and paid products.
- Risk of obsolete solution: high if QR points only to Yandex, because text comments may remain unpublished there and get lost.
- Stronger architecture: two-channel funnel: official Yandex rating plus Moonn-controlled text review queue.
- Reuse: the same funnel can be reused after Timepad events, Telegram follow-ups, Tilda pages, and offline QR slides.
- 3-12 month risk if skipped: split feedback, manual copying from messengers, no moderation log, weak proof layer on `moonn.ru`.

## Candidate Routes

- A: QR goes straight to Yandex add-review URL.
  - Fastest and best for star ratings.
  - Weak for text reviews because Yandex may not publish comments.

- B: QR goes to a Moonn-owned `/otzivi` funnel.
  - First CTA opens the official Yandex rating modal.
  - Second step collects a text comment into a Moonn moderation queue.
  - Stronger because it keeps one public URL and one controlled review workflow.

- C: Fully custom review page that visually copies Yandex.
  - Rejected. It risks confusing visitors and can be treated as impersonating a platform interface.

## Chosen Route

Use route B.

The page may use a restrained yellow/star visual cue, but it must state that the star rating happens on the official Yandex Services page. The Moonn text-review form must be clearly labeled as a Moonn-owned form.

The Yandex rating button must not claim automatic rating submission. It opens the official Yandex Services rating URL in a new tab, marks the local button as opened, shows the next-step message, and scrolls the visitor to the Moonn text-review form. This is the strongest safe behavior because Moonn cannot submit or verify a Yandex rating on behalf of the visitor.

## Implementation Packet

- `registry/reviews/moonn-review-funnel.schema.json`
- `registry/reviews/moonn-review-funnel.manifest.json`
- `scripts/build_moonn_review_funnel_artifacts.py`
- `docs/tatiana-munn-review-funnel/review-funnel-tilda-block.html`
- `docs/tatiana-munn-review-funnel/review-funnel-prototype.html`
- `docs/tatiana-munn-review-funnel/qr-moonn-review-funnel.svg`
- `docs/tatiana-munn-review-funnel/qr-moonn-review-funnel.png`
- `scripts/build_moonn_reviews_home_banner.py`
- `docs/tatiana-munn-reviews-home-banner/tilda-html-block-final.html`
- `docs/tatiana-munn-reviews-home-banner/homepage-reviews-banner-preview.html`

## Production Backend Decision

Production backend is Apps Script with a JSONP endpoint because Tilda static pages cannot safely receive direct cross-origin form posts without a backend layer.

Current backend:

- Apps Script project: `Moonn Reviews Intake`.
- Apps Script script id: `1I2jTuAaTw0o9imbfrFPsk_Kqc2sfa63kp-2soTlN43h549qDl42oHrSX`.
- Public endpoint: `https://script.google.com/macros/s/AKfycbx62eyhvrBVb3rt21le1iHfUrvJwhdcAJoAht_Chu0AL_PZjIR6I3r1FxKvI7pr-tz8/exec`.
- Public actions: `health`, `list`, `submit`.
- Admin action: `hide`, protected by a local/admin token stored outside Git.
- Storage: Apps Script `PropertiesService`, key `moonn_reviews_v1`.

The owner requested immediate publication for the first version. Therefore text comments are auto-published after validation, consent, honeypot check, and length limits. The backend still preserves an admin hide operation for cleanup and abuse handling.

Review fields:

- `created_at`
- `source`
- `rating`
- `context`
- `name_public`
- `comment_raw`
- `publication_consent`
- `published_at`
- `hidden`

## Publication Gate

Published to `moonn.ru` on 2026-05-18:

- `/otzivi` Tilda page id: `81167556`.
- `/otzivi` T123 record id: `1353112591`.
- The existing YClients widget snippet is preserved after the funnel block.
- Homepage Tilda page id: `42678538`.
- Homepage T123 record id: `2251351151`.

Verified on live site:

- `https://moonn.ru/` contains `moonn-reviews-home-banner`.
- `https://moonn.ru/otzivi` contains `moonn-review-funnel`.
- On the ordinary `https://moonn.ru/otzivi` reading page the review-intake block removes itself from the rendered DOM, so the form does not visually sit above the reviews.
- Homepage `Оставить отзыв` and QR both route to `https://moonn.ru/otzivi?ostavit-otzyv=1&source=homepage_reviews_banner#moonn-review-funnel`.
- Yandex rating CTA opens the official `uslugi.yandex.ru` rating URL.
- A clearly marked test Moonn review was submitted through the live form.
- The test Moonn review appeared on the public page and backend list.
- The test Moonn review was hidden through the admin endpoint and disappeared after page reload.
- Mobile rendering of the `/otzivi` funnel is visible.

QA report: `output/playwright/moonn-review-live-e2e-2026-05-18/qa-report.json`.

## Follow-Up Rule

Any future review request should route through:

`QR / follow-up link -> /otzivi?ostavit-otzyv=1 -> Moonn review funnel -> official Yandex rating -> Moonn text intake -> public /otzivi renderer -> admin hide if needed`.

Do not create a second reviews page unless `/otzivi` cannot support the funnel technically.

If reviews volume grows, migrate storage from Apps Script properties to a table-backed queue with explicit moderation states before adding imports from Telegram, Timepad, or Yandex follow-up campaigns.
