# Moonn Native Form Consent Hardening Plan — 2026-05-08

## Scope

- Site: `https://moonn.ru`
- Tilda project: `8326812`
- Workstream: native/source-level personal-data consent hardening.
- Canonical policy URL: `https://moonn.ru/politic`

## Current Verified State

- `/politic` is now source-level native Tilda content, not only a rendered JavaScript replacement.
- The global privacy layer still adds required unchecked consent checkboxes on rendered forms.
- Native form inventory exists in `docs/moonn-native-form-inventory-2026-05-08.json`.

## Inventory Summary

- Pages with form-like candidate blocks: `15`.
- Candidate form/cart/custom-code blocks: `21`.
- Already has native checkbox signal: `1` block.
- Needs review: `20` blocks.

## First Native Pilot

Priority target:

- URL: `https://moonn.ru/`
- Page ID: `42678538`
- Record ID: `691008996`
- Block type: `712`
- Current raw state: no native checkbox signal detected.
- Current rendered state: protected by JS layer.

Native checkbox text to add through supported Tilda form settings:

`Я согласен(на) на обработку персональных данных в соответствии с Политикой обработки персональных данных, а также ознакомлен(а) с использованием cookies и Яндекс.Метрики.`

Link target:

- `Политикой обработки персональных данных` -> `/politic`

Field requirements:

- Checkbox must be unchecked by default.
- Checkbox must be required before form submission.
- Existing form fields, Telegram/CRM delivery and button styling must not be changed.

## Verification Gate

After each native form edit:

1. Save and publish the changed Tilda page.
2. Fetch the page through Tilda API `getpagefull`.
3. Confirm the edited record contains a native checkbox or consent marker.
4. Fetch live raw HTML for the URL and confirm the marker is present.
5. Render the live page and confirm the form cannot be submitted without consent.
6. Record the result in `docs/moonn-rkn-live-verification-2026-05-08.md`.

## Safety Rule

Do not run mass UI changes across all candidate blocks until the homepage pilot proves the exact Tilda form-field path. Some candidates in the inventory are not real lead forms and should not receive form fields.
