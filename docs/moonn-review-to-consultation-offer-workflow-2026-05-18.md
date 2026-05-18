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

## Implemented Minimal Safe Prototype

Implemented after user approval:

1. On successful Moonn text review submission, show a compact thank-you panel:
   - "Спасибо, отзыв отправлен."
   - "Для участников мероприятий Moonn доступно специальное условие на первое двухчасовое посещение для себя или близкого."
   - Buttons:
     - `Записаться онлайн`
     - `Написать Татьяне в Telegram`
     - `Скопировать сообщение`
     - `Закрыть страницу`
2. Telegram direct-message prefill is not reliable for arbitrary personal chats. Implemented as:
   - generated message textarea;
   - `Скопировать сообщение`;
   - `Открыть Telegram Татьяны`.
3. The generated message includes:
   - public name;
   - visit context;
   - Moonn review id returned by the backend.
4. Booking opens:
   - `https://n461584.yclients.com/`
5. Telegram opens:
   - `https://t.me/Tatiana_Moonn`
6. Do not show a reward after Yandex rating click until there is a compliant legal wording and platform-safe decision.

## Live Safe Verification

Checked on 2026-05-18 against the published `/otzivi` page:

1. Opened:
   `https://moonn.ru/otzivi?ostavit-otzyv=1&source=live_safe_demo_after_fix#moonn-review-funnel`
2. Submitted a test review as `Alex Markss` with the Moonn backend JSONP request intercepted in Playwright, so no fake public review was stored.
3. Confirmed the post-review participant offer appears.
4. Confirmed the generated Telegram message is:
   `Здравствуйте, Татьяна.`
   `Я оставил(а) отзыв на сайте Moonn.ru и хочу уточнить специальное условие для участника мероприятия Moonn на первое двухчасовое посещение для себя или близкого.`
   `Имя для публикации: Alex Markss.`
   `Что посетил(а): Лекция.`
   `ID отзыва: test-live-safe-alex-markss-2026-05-18.`
5. Confirmed `Скопировать сообщение` writes the message to clipboard.
6. Confirmed `Записаться онлайн` points to:
   `https://n461584.yclients.com/`
7. Confirmed `Открыть Telegram Татьяны` opens:
   `https://t.me/Tatiana_Moonn`

## Review Proof Attachment

Implemented on 2026-05-18:

1. After a Moonn text review is accepted, the browser generates a PNG proof card from the returned backend review data:
   - review id;
   - public name;
   - visit context;
   - rating;
   - review comment;
   - date;
   - `https://moonn.ru/otzivi`.
2. The offer panel shows:
   - `Скачать подтверждение`;
   - `Поделиться подтверждением` only when the browser supports Web Share with files;
   - `Открыть Telegram Татьяны`.
3. The Telegram message now includes:
   `Прикрепляю подтверждение отзыва с сайта Moonn.ru.`

Important limitation:

- A normal website link to a personal Telegram profile cannot silently attach a generated file or send a message for the user. The safe implementation is: generate PNG -> user downloads or shares it -> user attaches/sends it in Telegram.

UX correction after live user test on 2026-05-18:

- After a successful Moonn review submission, the Yandex rating card and the filled review form are hidden.
- The visitor is moved to a single success state instead of seeing the empty form again.
- The status wording is now:
  `Отзыв опубликован на странице Татьяна Мун.ру.`
- The proof image is shown directly inside the success state; the old `Скачать подтверждение` and `Скопировать сообщение` buttons were removed.
- The primary action is now:
  `Скопировать текст и открыть Telegram Татьяны`
- On supported mobile browsers, an additional user-facing file-share action can appear:
  `Отправить текст и подтверждение`
- UX correction after the Windows/Unigram test on 2026-05-19:
  - Proof preview is displayed compactly at `260x330` instead of taking the full card width.
  - The share action is now explicitly labeled:
    `Отправить текст и подтверждение в Telegram`
  - The share action copies the Telegram text to clipboard before opening the system share sheet, because Windows/Unigram may send the file but ignore the Web Share `text` field.
  - The PNG proof itself now includes the offer-context line, so the image remains meaningful even if the target app sends only the file.

Verification:

- Live safe Playwright check intercepted the backend JSONP submit request, so no fake public review was stored.
- The generated proof link was a `data:image/png;base64,...` URL.
- Downloaded proof file passed PNG signature check.
- Live safe UX check confirmed:
  - `.rf-intro` is hidden after submit;
  - the form is hidden after submit;
  - status strip is hidden after submit;
  - success panel is visible;
  - proof preview image is visible;
  - Telegram button copies the text and opens `https://t.me/Tatiana_Moonn`.
  - Windows/Unigram UX follow-up confirmed compact preview size, Telegram-specific share button wording, and restored spacing in the copied message after Tilda minification.
- Verification artifacts:
  - `output/playwright/moonn-review-proof-card-2026-05-18/result.json`
  - `output/playwright/moonn-review-proof-card-2026-05-18/download-result.json`
  - `output/playwright/moonn-review-proof-card-2026-05-18/offer-with-proof.png`
  - `output/playwright/moonn-review-submitted-ux-fix-2026-05-18/result.json`
  - `output/playwright/moonn-review-submitted-ux-fix-2026-05-18/mobile-telegram-result.json`
  - `output/playwright/moonn-review-proof-share-ux-2026-05-19/result.json`
  - `output/playwright/moonn-review-proof-share-ux-2026-05-19/text-fix-result.json`

Verification artifacts:

- `output/playwright/moonn-review-live-safe-demo-2026-05-18-after-fix/result.json`
- `output/playwright/moonn-review-live-safe-demo-2026-05-18-after-fix/telegram-open-result.json`
- `output/playwright/moonn-review-live-safe-demo-2026-05-18-after-fix/offer-panel.png`

Correction found during live verification:

- Tilda minification removed spaces inside `join(': ')` string fragments in the generated Telegram message. The builder now assembles field lines through `label + ':'` and `join(' ')` so the published message keeps spaces after punctuation.

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
