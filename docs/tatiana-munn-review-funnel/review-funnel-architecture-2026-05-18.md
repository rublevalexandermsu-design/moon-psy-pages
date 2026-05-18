# Moonn Review Funnel Architecture - 2026-05-18

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: Yandex Services rating + Moonn-owned text review intake.
- Existing branch: `codex/moonn-homepage-reviews-banner`.
- Canonical reviews page: `https://moonn.ru/otzivi`.
- Tilda page id: `81167556`.
- QR target: `https://moonn.ru/otzivi?source=qr_event#moonn-review-funnel`.
- Homepage entry target: `https://moonn.ru/otzivi?source=homepage_reviews_banner#moonn-review-funnel`.

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

The prototype intentionally does not auto-submit comments yet.

Choose one production intake backend before publishing:

- Tilda Form -> email/CRM/Google Sheet: fastest if the existing Tilda account already has forms configured.
- Google Sheet + Apps Script/Worker: better for moderation queue and future renderer.
- Telegram `moonn_review_bot`: good for event follow-up, but currently requires runtime/secret confirmation.
- Cloudflare Worker + private registry: strongest for reusable moderation and API contracts.

Recommended first production step: Tilda Form or Google Sheet queue with moderation fields:

- `created_at`
- `source`
- `rating`
- `context`
- `name_public`
- `comment_raw`
- `publication_consent`
- `moderation_status`
- `published_at`
- `published_url`

## Publication Gate

Do not publish to `moonn.ru` until:

- final backend is selected;
- final consent checkbox text is approved;
- comment submissions are stored in a private moderation queue;
- raw comments are not auto-published;
- Playwright/browser visual QA passes for desktop and mobile;
- Yandex rating CTA opens the official Yandex URL;
- QR target URL is confirmed.
- homepage reviews banner has both `Читать отзывы` and `Оставить отзыв` actions;
- homepage QR points to the same canonical review funnel instead of a duplicate page.

## Follow-Up Rule

Any future review request should route through:

`QR / follow-up link -> Moonn review funnel -> official Yandex rating -> Moonn text queue -> moderation -> public /otzivi renderer`.

Do not create a second reviews page unless `/otzivi` cannot support the funnel technically.
