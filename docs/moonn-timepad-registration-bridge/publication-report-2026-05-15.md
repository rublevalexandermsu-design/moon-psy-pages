# Moonn Timepad Registration Bridge — 2026-05-15

## Scope

- Project: Moonn / Tatyana Munn site.
- Branch: `codex/moonn-timepad-registration-bridge`.
- Live URL: `https://moonn.ru/timepad-registration`.
- Purpose: direct registration bridge from Timepad lecture cards to a selected recurring-session form.

## Tilda

- Project id: `8326812`.
- Page id: `141821916`.
- Alias: `timepad-registration`.
- T123 record id: `2273574411`.
- Page title: `Регистрация на лекцию Татьяны Мунн`.
- Index policy: `noindex,follow`.

## Generated Artifacts

- `data/moonn-timepad-registration-bridge.json`
- `scripts/build_moonn_timepad_registration_bridge.py`
- `docs/moonn-timepad-registration-bridge/tilda-html-block-final.html`
- `docs/moonn-timepad-registration-bridge/tilda-page-final.html`
- `docs/moonn-timepad-registration-bridge/manifest.json`

## Verification

- Local preview `?lecture=9` selected recurring event `3889454`.
- Local Timepad iframe showed the selected form for `1 июня 2026, 19:00`; the date-choice list was absent.
- Live raw HTML `https://moonn.ru/timepad-registration?lecture=9` returned `200`.
- Live raw HTML contains:
  - `moonn-timepad-registration-bridge`
  - `data-timepad-widget-v2`
  - `noindex`
  - exactly one H1
  - no SoundCloud marker
- Live rendered browser check for `?lecture=9` showed:
  - selected lecture title `Как детство влияет на наши отношения`
  - selected form for `1 июня 2026, 19:00`
  - visible `E-mail`, `Фамилия`, `Имя`, `Телефон (Whatsapp)` fields
  - date-choice list absent
  - no page errors and no failed requests

## Downstream

- Timepad cards were updated in the separate `codex/timepad-relations-series` workstream to use `https://moonn.ru/timepad-registration?lecture=N`.
- Temporary `school.miiiips.ru` helper pages remain fallback artifacts and are no longer the live Timepad card target.

## Evidence

- Screenshot: `docs/moonn-timepad-registration-bridge/live-bridge-lecture-09-2026-05-15.png`
