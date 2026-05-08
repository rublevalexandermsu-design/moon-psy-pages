# Moonn RKN Compliance Rollout Plan — 2026-05-08

## Goal

Bring Moonn into a defensible personal-data/cookie/form compliance posture without damaging SEO and without publishing unapproved legal claims.

## What Was Done Now

- Created legal publication packet: `docs/moonn-privacy-publication-packet-2026-05-08.md`.
- Created live technical audit script: `scripts/moonn_privacy_compliance_audit.py`.
- Ran audit for the `83` production-scope URLs.
- Created reports:
  - `docs/moonn-privacy-compliance-audit-2026-05-08.json`
  - `docs/moonn-privacy-compliance-audit-2026-05-08.md`

## Audit Result

- Policy endpoints currently return `404`:
  - `/privacy`
  - `/personal-data-consent`
  - `/cookies`
  - `/data-subject-request`
- `83/83` checked production URLs have Tilda form signals.
- `79` pages have form signals without detected checkbox.
- `58` pages have form signals without detected consent text.

## Required Live Tilda Work

### 1. Publish documents

Create or publish pages:

- `/privacy`
- `/personal-data-consent`
- `/cookies`
- `/data-subject-request`

Use `docs/moonn-privacy-publication-packet-2026-05-08.md`.

Gate: fill operator variables first:

- legal operator name: `Индивидуальный предприниматель Кумскова Татьяна Михайловна`;
- legal status: `индивидуальный предприниматель`;
- INN: `770906685276`;
- OGRNIP: `316774600553212`;
- legal/postal address: `АДРЕС_ДЛЯ_КОРРЕСПОНДЕНЦИИ_ТРЕБУЕТ_ПОДТВЕРЖДЕНИЯ`;
- public email for personal-data requests: `moonn.official@yandex.ru`.

### 2. Add required form checkbox

Add a native Tilda required checkbox under every public form:

`Я согласен(на) на обработку персональных данных в соответствии с Политикой обработки персональных данных и Согласием на обработку персональных данных, а также ознакомлен(а) с использованием cookies и Яндекс.Метрики.`

Links:

- `Политикой обработки персональных данных` -> `/privacy`
- `Согласием на обработку персональных данных` -> `/personal-data-consent`
- `cookies и Яндекс.Метрики` -> `/cookies`

Checkbox must be:

- separate from submit text;
- unchecked by default;
- required for submission.

### 3. Add cookie/analytics notice

Add a visible cookie notice:

`Сайт использует cookies и Яндекс.Метрику, включая аналитику посещений, карту кликов и Webvisor, чтобы улучшать работу страниц. Продолжая использовать сайт, вы соглашаетесь с использованием cookies. Подробнее — в уведомлении об использовании cookies.`

Link:

- `уведомлении об использовании cookies` -> `/cookies`

### 4. Verify

Run:

```powershell
python scripts\moonn_privacy_compliance_audit.py
```

Expected:

- `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request` return `200`.
- Form pages have detected checkbox and consent text.
- Cookie/Metric text is visible.
- Google/Yandex crawling remains allowed.

## Google Analytics Decision

The current main-page audit did not detect Google Analytics/gtag. Do not add GA4 until there is a separate legal decision about cross-border transfer / notification posture. Use Yandex Metrika as the primary analytics layer for now.

## Bot-Control Decision

Do not block Google/Yandex/Bing and do not try to hide the public site from official checks.

Allowed later, after compliance pages are fixed:

- block non-essential AI/scraper bots only;
- keep sitemap and SEO bots open;
- verify robots.txt after every change.

## Current Blockers

- Operator variables are mostly filled; only the public correspondence/legal address remains unconfirmed.
- Legal text is drafted but not lawyer-approved.
- Live Tilda form checkbox rollout requires authenticated Tilda UI/API-safe application.
