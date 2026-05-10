# Timepad Consultation MVP - 2026-05-10

## Scope

- Project: Moonn / Tatyana Munn.
- Workstream: Timepad consultation booking MVP.
- Timepad organization: `426753`, subdomain `moonn`.
- Draft event: `https://moonn.timepad.ru/event/3973843/`.
- Created at: 2026-05-10 12:04 MSK.
- Status after creation: `access_status=draft`, `moderation_status=not_moderated`.
- Published after poster upload: 2026-05-10 12:04-12:05 MSK.
- Current verified status: `status=ok`, `access_status=public`, `moderation_status=not_moderated`.

## Strategic Decision

The MVP should use Timepad as the visible booking and payment layer, not as a link-only bypass to iClient/YCLIENTS.

Reason:

- Timepad moderation may reject pages that primarily route users away from Timepad for paid booking.
- Payment and registration should remain inside Timepad.
- iClient/YCLIENTS remains Tatyana's working calendar, but in the MVP the paid Timepad order must be manually mirrored into iClient/YCLIENTS.
- The stronger future architecture is `Timepad order webhook -> registry/notification -> iClient/YCLIENTS block/booking`, but this needs a separate integration step.

## Created Draft

Title:

`Психологическая консультация с Татьяной Мунн`

Poster image:

- Source file: `assets/timepad/tatyana-munn-psychological-consultation-msu-online-offline-moscow-timepad-2026.png`.
- Public CDN URL after push: `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@codex/moonn-seo-audit/assets/timepad/tatyana-munn-psychological-consultation-msu-online-offline-moscow-timepad-2026.png`.

Initial slot:

- Date: 2026-05-18.
- Time: 12:00-14:00 MSK.
- Purpose: placeholder first consultation slot for MVP setup. Final slot schedule must be checked against iClient/YCLIENTS before publication.

Location:

`Москва, Цветной бульвар, д. 19, стр. 4`

Category:

- `453` - `Психология и самопознание`.

Tickets:

- `8110182` - `Индивидуальная консультация, 2 часа` - `10 000 ₽`.
- `8110183` - `Индивидуальная консультация, 1 час` - `6 000 ₽`.
- `8110184` - `Пакет 5 консультаций` - `40 000 ₽`.

Event-level ticket limit:

- `1`, so the draft behaves like a single consultation slot until a proper slot schedule is configured.

## Known Limitations Before Publication

- Final slot schedule is not synced with iClient/YCLIENTS yet.
- Custom registration questions were not added through API because Timepad rejected custom `field_id` values; add or verify fields in the Timepad UI before publication:
  - phone;
  - online/offline format;
  - short request theme;
  - safe optional comment;
  - personal data consent wording.
- API returned default `buy_amount_max=30` for ticket types, but the event-level limit is `1`. Before publication, verify in the Timepad UI that a buyer cannot reserve more than one slot/order.
- Event is public on Timepad but not yet moderated into the Timepad Afisha: `moderation_status=not_moderated`.

## Publication Verification - 2026-05-10

API read-back:

- `status=ok`.
- `access_status=public`.
- `moderation_status=not_moderated`.
- `registration_data.price_min=6000`.
- `registration_data.price_max=40000`.
- `registration_data.tickets_limit=1`.
- `registration_data.is_registration_open=true`.
- Timepad copied the poster to Uploadcare: `poster_event_3973843.jpg`.

Public HTTP check:

- `https://moonn.timepad.ru/event/3973843/` returns `200`.
- Public HTML contains the event title.
- Public HTML contains the poster marker.
- Public HTML contains paid prices `6 000`, `10 000`, and `40 000`.

## Anti-Duplicate Booking Rule

Before making the event public:

1. Compare the Timepad slot list with Tatyana's iClient/YCLIENTS calendar.
2. Publish only slots that are actually free in iClient/YCLIENTS.
3. After every paid Timepad order, manually create/block the same slot in iClient/YCLIENTS.
4. If a Timepad order is refunded or cancelled, unblock the slot only after verifying that no replacement booking exists.

Future automation candidate:

`Timepad order_change webhook -> order registry -> email/Telegram notification -> iClient/YCLIENTS booking/blocking`.

## Recurring Schedule Decision

The single event `3973843` should become the first event of a weekly consultation schedule, not a set of manually duplicated unrelated events.

Target schedule:

- Weekly from 2026-05-18 through 2026-12-28 inclusive.
- Baseline time: Monday, 12:00-14:00 MSK.
- Each slot must keep capacity `1`.
- Prefer Timepad's calendar-style schedule display so visitors can choose a date visually.
- The slot list must be reconciled with iClient/YCLIENTS before publishing many dates.

Reason:

- Timepad represents repeating events as a master event with separate session events.
- Mass-creating many independent copies through API would create moderation and duplicate-management risk.
- Timepad's help article says the schedule/master-event option can be enabled by support after sending a link to the first event of the series.

## Support Message Draft

Subject:

`Просим проверить консультацию психолога Татьяны Мунн и подключить расписание`

Body:

```text
Здравствуйте!

Просим проверить мероприятие в личном кабинете организатора «Психолог Татьяна Мунн (МГУ) - "Быстрая Психология"» и помочь подключить к нему расписание:

Психологическая консультация с Татьяной Мунн
https://moonn.timepad.ru/event/3973843/

Это не лекция и не дубль ранее опубликованных бесплатных мероприятий. Это отдельная страница записи на индивидуальную платную консультацию психолога Татьяны Мунн: онлайн или очно в Москве по адресу Цветной бульвар, д. 19, стр. 4.

Запись, выбор билета и оплата проходят через Timepad. Слот консультации настроен как ограниченная запись с лимитом мест, чтобы не было двойного бронирования. После оплаты организатор подтверждает встречу и переносит запись в рабочий календарь специалиста.

Просим:

1. Проверить и одобрить мероприятие.
2. Подключить к нему функцию расписания / мастер-события, чтобы посетитель мог выбрать дату консультации.
3. Настроить еженедельные слоты по понедельникам с 12:00 до 14:00 с 18 мая 2026 года по 28 декабря 2026 года включительно, с лимитом 1 место на каждый слот.
4. По возможности включить отображение расписания в виде календаря, чтобы посетитель мог выбрать удобную дату на странице мероприятия.

Если лучше выбрать другой технический формат внутри Timepad, пожалуйста, подскажите, что именно нужно изменить, чтобы страница соответствовала правилам Timepad и корректно работала как запись на платные консультации.

Спасибо!
```

## Publication Gate

Completed:

- Poster uploaded and visually checked.
- Timepad event updated through API.
- API confirms public status and paid registration.
- Public URL returns `200`.

Still required:

- Timepad UI check of registration form fields.
- iClient/YCLIENTS slot reconciliation.
- Support message submission or reply from Timepad.
- Afisha/moderation result check after Timepad support response.
- Timepad support should enable recurring schedule/master-event mode instead of creating many independent duplicate events.
