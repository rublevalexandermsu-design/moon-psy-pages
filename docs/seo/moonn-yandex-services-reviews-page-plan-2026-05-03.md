# Moonn Yandex Services Reviews Page Plan

- Date: 2026-05-03
- Workstream: Moonn SEO/AEO reviews page
- Source profile: `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`
- Goal: create or improve a `moonn.ru` reviews page that strengthens entity trust for `Татьяна Мунн / Кумскова Татьяна Михайловна`, links back to Yandex Services, and gives search engines/AI systems a clean evidence layer.

## Strategic Assessment

1. Platform value: high. Reviews are external proof, useful for SEO, AEO, conversion, and entity trust.
2. Obsolescence risk: medium. Reviews change over time, so the page needs refresh rules and provenance.
3. Stronger architecture: use a reviews manifest with per-review provenance plus screenshots/OCR evidence, not a one-off page.
4. Reuse: high. The same workflow can support Timepad reviews, course feedback, event feedback, and future author profiles.
5. 3-12 month risk if ignored: reviews remain isolated inside Yandex Services and do not strengthen `moonn.ru` entity trust.

## Safety / Legal / Platform Gate

Do not publish screenshots automatically until these questions are cleared:

- Do screenshots show client names, avatars, faces, phone fragments, or other personal data?
- Does the Yandex Services interface allow public reuse of review screenshots outside Yandex?
- Should reviewer identities be blurred or cropped?
- Is each review clearly attributable to Yandex Services as the source?
- Does the page avoid implying medical guarantees or guaranteed therapy outcomes?
- Are negative/neutral reviews represented fairly if present?

Default safe rule: use grouped screenshots only after manual approval or anonymization. For SEO text, prefer summarized review themes and short compliant excerpts over copying all review text verbatim.

## Verification / Provenance Rule

Every review used on `moonn.ru` must be independently checkable.

Required manifest fields per review:

- `source_platform`: `Yandex Services`.
- `source_profile_url`: `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`.
- `source_review_url`: direct URL to the individual review if Yandex exposes one.
- `source_review_id`: review id or stable DOM/link identifier if available.
- `captured_at`: date/time when the review was checked.
- `review_date`: visible date from Yandex.
- `rating`: visible rating if available.
- `reviewer_display`: public display name only if approved; otherwise anonymized label.
- `public_excerpt`: short visible excerpt or approved OCR text.
- `screenshot_file`: SEO-named evidence image if screenshots are approved.
- `screenshot_hash`: SHA-256 hash of the evidence image.
- `privacy_status`: `public`, `anonymized`, or `do_not_publish`.

If Yandex does not provide direct links to individual reviews, do not pretend that it does. Use the Yandex profile URL as the source link and add a visible source note on the page: `Источник: профиль Татьяны Мунн на Яндекс Услугах; отзыв проверен по дате, рейтингу и скриншоту`. In that case each review block should still carry `captured_at`, `review_date`, `rating`, `screenshot_file`, and `screenshot_hash` in the internal manifest.

## Proposed Page Structure

- URL candidate: `https://moonn.ru/reviews-yandex-services` or improve existing `https://moonn.ru/otzivi` if it is the canonical reviews page.
- Title: `Отзывы о психологе Татьяне Мунн — Яндекс Услуги, консультации, лекции`
- Description: `Отзывы клиентов о консультациях и лекциях Татьяны Мунн, психолога МГУ и эксперта по эмоциональному интеллекту. Источник отзывов: профиль Яндекс Услуг.`
- H1: `Отзывы о Татьяне Мунн`
- Sections:
  - summary trust block: rating, review count, source link;
  - source disclosure: reviews are from Yandex Services profile;
  - each visible review includes a source link to the individual Yandex review when available;
  - if individual review links are not available, each visible review links to the Yandex Services profile and the internal manifest stores evidence fields;
  - grouped screenshots, 7-10 reviews per image if privacy allows;
  - OCR text layer only after review and cleanup;
  - thematic review clusters: consultation, anxiety/stress, relationships, emotional intelligence, lectures;
  - CTA to consultation/events;
  - link to Yandex Services profile;
  - FAQ block about reviews and booking.

## SEO/AEO Layer

- `Person` schema connected to `Татьяна Мунн`, `Кумскова Татьяна Михайловна`, `moonn.ru`, `miiiips.ru/person.json`, Timepad and Yandex Services.
- `Review` or `AggregateRating` schema only if ratings/reviews are represented in a way allowed by Google/Yandex guidelines and the source is transparent.
- `ImageObject` schema for approved screenshots.
- Image filenames in Latin:
  - `tatyana-munn-yandex-services-reviews-consultation-01.webp`
  - `tatyana-munn-kumskova-psychologist-msu-yandex-reviews-02.webp`
- Alt text examples:
  - `Отзывы клиентов о психологе Татьяне Мунн на Яндекс Услугах`
  - `Отзывы о консультациях Татьяны Мунн, психолога МГУ`
- Canonical: chosen reviews URL.
- Internal links:
  - homepage;
  - consultations;
  - events/lectures;
  - paid products;
  - author/entity bridge.

## Implementation Options

1. Safe first pass:
   - create a reviews page plan and SEO metadata;
   - add source link to Yandex Services;
   - add summarized review themes without screenshots.

2. Screenshot pass after approval:
   - capture grouped screenshots from Yandex Services;
   - blur names/avatars if needed;
   - export SEO-named images;
   - upload through Tilda visual editor or documented workflow;
   - add image alt/title where Tilda exposes fields.

3. OCR/text pass after approval:
   - OCR screenshots locally;
   - remove personal data;
   - keep short excerpts or summarized themes;
   - avoid mass-copying 200 full reviews into page text.

## User Inputs Needed

- Visual access to Yandex Services review page in Chrome if reviews are not publicly accessible.
- Decision: publish reviewer names/avatars as visible screenshots or blur/anonymize them.
- Tilda visual editor access for the final screenshot/image upload step, because official Tilda API does not provide safe source-level media replacement.

## Stop Conditions

- Do not publish until privacy/platform reuse decision is made.
- Do not use undocumented Tilda endpoints.
- Do not generate fake review text.
- Do not add `AggregateRating` unless the source rating/count is verified and represented accurately.
