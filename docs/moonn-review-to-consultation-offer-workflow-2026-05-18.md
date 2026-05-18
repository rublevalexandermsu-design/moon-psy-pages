# Moonn Review To Consultation Offer Workflow

Date: 2026-05-18
Project: Moonn / Tatyana Munn site
Branch: `codex/moonn-homepage-reviews-banner`

## Goal

Build a conversion route after a visitor leaves a rating or text review:

1. Visitor can voluntarily leave a Yandex Services rating or a Moonn.ru text review.
2. Visitor can then see a consultation offer.
3. Visitor can book through YCLIENTS / iClients.
4. Visitor can open Telegram with a prepared message to Tatyana Munn.

## Checked Facts

- Current Moonn review funnel URL:
  `https://moonn.ru/otzivi?ostavit-otzyv=1&source=homepage_reviews_banner#moonn-review-funnel`
- Current YCLIENTS/iClients public booking entry found in project history:
  `https://n461584.yclients.com/`
- Current YCLIENTS widget script on `/otzivi`:
  `https://w461584.yclients.com/widgetJS`
- Current Telegram contact found in the repo:
  `https://t.me/Tatiana_Moonn`
- Moonn text reviews can be verified by our backend because the Apps Script response returns success and the review list.
- Yandex rating submission cannot be verified by Moonn.ru unless Yandex provides an official callback/API for this exact action. Opening the Yandex rating page is not proof that the rating was submitted or moderated.
- A Telegram deep link can prefill a message, but the user must press send in Telegram. A website cannot silently send a personal Telegram message.

## Compliance Risk

Yandex guidance for business reviews says not to offer money in exchange for reviews and not to offer discounts for positive comments. Source checked on 2026-05-18:

- `https://yandex.ru/support/business-priority/ru/manage/reviews`

Therefore the unsafe pattern is:

- "Leave a Yandex rating and receive 1,000 RUB discount."
- "Leave a Moonn review and receive 2,000 RUB discount."
- "Show us your review to claim the discount."

## Safer Architecture

Use a voluntary review flow and a separate participant offer:

1. Review/rating block:
   - Text: visitor may leave a Yandex rating or a Moonn text review.
   - No promise that a discount is paid for a review.

2. Thank-you state:
   - After Moonn text review succeeds, show: "Спасибо, отзыв отправлен. Если вы планировали первую консультацию, можно записаться на специальное первое посещение для участников мероприятий Moonn."
   - For Yandex rating click, show only: "Форма Яндекс Услуг открыта. Вы можете вернуться и оставить текстовый отзыв на Moonn.ru."

3. Booking:
   - CTA: "Записаться на консультацию" opens YCLIENTS/iClients.
   - The offer should be framed as a campaign for participants, not as payment for review.

4. Confirmation:
   - After booking, if YCLIENTS supports return URL, JS callback, webhook, or API access, generate a Telegram link with real booking date/time.
   - If no callback/API is available, use a manual Telegram confirmation message:
     `Здравствуйте, я записался(лась) на первую консультацию через онлайн-запись. Прошу проверить возможность применить специальное условие для участников Moonn.`

## Strong Version

Build a small `review_offer_token` backend:

1. Moonn review submission returns `reviewId`.
2. Backend creates `offerToken` with:
   - reviewId
   - source
   - createdAt
   - selected context
   - visitor public name
   - offer type
3. Thank-you UI opens `/otzivi?offer=<token>` or in-place success panel.
4. Booking CTA appends `offerToken` to the YCLIENTS route only if YCLIENTS supports UTM/custom fields.
5. YCLIENTS webhook/API confirms appointment:
   - client name
   - date/time
   - service duration: 2 hours
   - first consultation flag, if available
6. Backend marks `offerToken` as `booked`.
7. Telegram link is shown with confirmed appointment data.

## Minimal Safe Prototype

Implement only after approval:

1. On successful Moonn text review submission, show a compact thank-you panel:
   - "Спасибо, отзыв отправлен."
   - "Для участников мероприятий Moonn доступно специальное первое посещение для себя или близкого."
   - Buttons:
     - `Записаться онлайн`
     - `Написать Татьяне в Telegram`
     - `Закрыть страницу`
2. Telegram prefilled text should not claim a verified discount. It should request confirmation:
   - `Здравствуйте, я оставил(а) отзыв на Moonn.ru и хочу уточнить возможность специального первого посещения для себя или близкого.`
3. Do not show a reward after Yandex rating click until there is a compliant legal wording and platform-safe decision.

## Open Questions

- Exact Telegram handle to use: repo currently has `Tatiana_Moonn`; confirm it is still correct.
- Does YCLIENTS/iClients support a success callback, webhook, UTM pass-through, custom client field, or API endpoint for created appointments?
- Exact public legal wording for the participant offer.
- Whether the offer is available to all event participants or only first-time consultation clients.
- Whether "2,000 RUB" is a discounted final price or a discount amount from a standard two-hour consultation price.

## Recommendation

Do not implement a public "discount for Yandex rating/review" mechanic.

Implement a compliant participant-offer funnel instead:

`voluntary review/rating -> thank-you panel -> booking -> Telegram confirmation`

The first production version can be manual-confirmation based. The stronger version needs YCLIENTS/iClients API or webhook access.
