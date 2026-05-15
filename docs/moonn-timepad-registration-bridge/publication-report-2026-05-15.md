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

## Poster Source Correction

- User reported that the Moonn bridge used old-looking right-side banner images.
- Root cause: the bridge manifest consumed the earlier `visual_card` fallback URLs from GitHub instead of the standalone Timepad poster images already used in the Fast Psychology lecture cards.
- Correction:
  - replaced bridge `poster_url` values with the canonical Timepad `ucare.timepad.ru/.../poster_event_*.jpg` poster URLs;
  - changed the bridge poster CSS to `object-fit: contain` so the generated lecture posters are not cropped;
  - republished native Tilda T123 record `2273574411`.
- Live raw HTML check for `https://moonn.ru/timepad-registration?lecture=7`:
  - status `200`;
  - marker `moonn-timepad-registration-bridge` present;
  - `poster_event_3944310.jpg` present;
  - old `raw.githubusercontent.com/rublevalexandermsu-design/moon-psy-pages/...visual_card...` source absent;
  - `noindex` present;
  - H1 count `1`.
- Live rendered check for `?lecture=7`:
  - right-side hero image loaded from `https://ucare.timepad.ru/c8751919-3b7d-4eb3-863e-810e2c57185f/-/preview/308x600/-/format/jpeg/poster_event_3944310.jpg`;
  - image loaded successfully with natural size `308x173`;
  - selected registration form opened for `18 мая 2026, 19:00`.

## Follow-up Rule

- Moonn bridge/page manifests for Timepad lectures must use the same poster source as the live Timepad agenda report.
- `visual_card` files may remain only as fallback/archive assets after a usage scan; they must not be the default public bridge poster once standalone event posters exist.

## Downstream

- Timepad cards were updated in the separate `codex/timepad-relations-series` workstream to use `https://moonn.ru/timepad-registration?lecture=N`.
- Temporary `school.miiiips.ru` helper pages remain fallback artifacts and are no longer the live Timepad card target.

## Evidence

- Screenshot: `docs/moonn-timepad-registration-bridge/live-bridge-lecture-09-2026-05-15.png`
- Screenshot after poster correction: `docs/moonn-timepad-registration-bridge/live-bridge-poster-update-2026-05-15.png`
