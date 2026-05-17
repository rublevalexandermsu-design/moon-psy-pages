# Moonn Timepad Consultation Full-Payment Update — 2026-05-17

## Scope

- Project: Moonn / Tatyana Munn site and Timepad promotion.
- Workstream: Timepad consultation booking, full-payment model, slot-sync risk.
- Branch: `codex/moonn-timepad-consultation-full-payment-sync`.
- Main Timepad event: `https://moonn.timepad.ru/event/3973843/`.
- Checked event from the user message: `https://moonn.timepad.ru/event/3982132/`.
- Open future sample slot: `https://moonn.timepad.ru/event/3982055/`.

## Strategic Assessment

- Platform value: high. This is the paid consultation acquisition route and must be consistent across Timepad, Moonn, iClient/YCLIENTS and support communication.
- Risk of obsolete local fix: high. Editing only one Timepad URL would leave the recurring series with old 500-ruble text.
- Stronger architecture: Timepad should be the paid checkout surface for Timepad slots; iClient/YCLIENTS should remain the working calendar until a real two-way sync exists.
- Reuse: high. The same pattern applies to future paid one-person slots: canonical slot registry, full ticket payment, one ticket per slot, webhook/order ledger.
- 3-12 month risk if unchanged: duplicate slot sales, Timepad moderation refusal, support mismatch, manual reconciliation errors, and stale event copies.

## Verified Facts

- Timepad support rejected the previous model because it looked like partial payment / service payment rather than full payment for a ticket.
- Before the update, `3973843`, `3982132` and future generated slots used:
  - title: `Бронь консультации с Татьяной Мунн`;
  - ticket: `Подтверждение брони консультации`;
  - price: `500`;
  - public text that sent participants first to the external iClient/YCLIENTS booking flow.
- Timepad recurring schedule is already active: future slots exist for Tuesday, Saturday and Sunday, generally at `10:00`, `12:00`, `15:00`, `17:00`, `19:00`.
- Public iClient/YCLIENTS page shows two-hour consultation services priced at `10 000 ₽`, so the Timepad full-price ticket was aligned to that value.
- Timepad API has an `order_change` webhook configured for organization `426753`, pointing to a Google Apps Script endpoint. The endpoint exists, but this task did not prove that it creates or blocks appointments in iClient/YCLIENTS.
- The Timepad API rate-limited bulk updates. The final batch was completed with throttling.

## Applied Changes

Updated 49 Timepad consultation-series events with no existing orders:

- title changed to `Индивидуальная психологическая консультация с Татьяной Мунн`;
- short description changed to full-payment wording;
- long description changed to full-payment wording;
- ticket changed to `Индивидуальная консультация, 2 часа`;
- ticket price changed to `10 000 ₽`;
- event limit remains one ticket per slot;
- questionnaire changed to:
  - `Формат консультации`: `Очно в Москве` / `Онлайн`;
  - `Телефон / WhatsApp для подтверждения деталей`;
  - `Кратко опишите запрос или важный комментарий`;
  - standard Timepad fields remain: email, surname, name.

## Verification

API sample verified after the update:

- `3973843`: title updated, ticket price `10000`, no old 500-ruble wording, registration closed because the slot is past.
- `3982132`: title updated, ticket price `10000`, no old 500-ruble wording, registration closed because the slot is past.
- `3982133`: title updated, ticket price `10000`, old wording absent, registration open at the time of check.
- `3982055`: title updated, ticket price `10000`, old wording absent, registration open.
- `3982145`: title updated, ticket price `10000`, old wording absent, registration open.
- `3982174`: title updated, ticket price `10000`, old wording absent, registration open.
- `3982189`: title updated, ticket price `10000`, old wording absent, registration open.

Browser verification:

- Public page `https://moonn.timepad.ru/event/3982055/` shows the updated title and description.
- Registration section shows selectable dates and times.
- Each visible slot shows `1 билет` and `10000 руб.`.
- Browser-visible old terms `Бронь`, `бронь`, `предоплат`, `500` were not found in the checked future public page.

Evidence screenshot:

- `tmp_timepad_registration_3982055_after.png` was generated locally as transient evidence and was not committed because it is a temporary screenshot.

## Support Draft

Created Gmail draft to `support@timepad.ru`:

- Draft ID: `r7433309802949927658`.
- Subject: `Обновили консультацию Татьяны Мунн: полная оплата билета через Timepad`.
- Status: draft only, not sent.

## Slot Sync Decision

The schedule conflict with iClient/YCLIENTS is not fully solved by the Timepad edits alone.

Current safe operating rule:

- Before scaling the Timepad schedule, compare Timepad slots against iClient/YCLIENTS availability.
- After a paid Timepad order, the same slot must be created or blocked in iClient/YCLIENTS.
- Until the webhook is proven end-to-end, this blocking is a manual or semi-manual operations step.

Target architecture:

`Timepad order_change webhook -> order registry -> slot-lock decision -> iClient/YCLIENTS booking/block -> notification -> audit log`

Needed next verification:

- Inspect the existing Google Apps Script webhook handler.
- Confirm whether it writes to a registry, sends a notification, and/or calls iClient/YCLIENTS.
- If it only notifies, add a slot-lock registry and either an iClient/YCLIENTS API connector or a documented manual blocking checklist.

## Security / Incident Note

- The Timepad API token was pasted into chat and used only for this task.
- The Timepad webhook response exposed its secret in API output.
- Action required: rotate the Timepad API token and webhook secret after this workstream is closed.

## Follow-up Rule

For paid Timepad consultation schedules, do not use partial-payment or external-preselection text. A public Timepad slot must be represented as one full-price ticket for one concrete time slot, with raw API and browser verification after batch updates.
