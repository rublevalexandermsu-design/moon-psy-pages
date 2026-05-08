# Moonn RKN/Privacy Live Verification — 2026-05-08

## Scope

- Site: `https://moonn.ru`
- Workstream: RKN/privacy technical compliance mitigation.
- Verification time: `2026-05-08 16:01:38 +03:00`.

## Published Changes

- Updated the Tilda global head for the Moonn project with the privacy compliance frontend layer.
- Re-published the protected production SEO scope: `80/80` pages in `docs/moonn-seo-scope-publish-report-2026-05-07.json`.
- Published the existing legal page `/politic` and kept it as the canonical policy URL.
- Did not publish or reference `https://umun.ru/`; it is not part of this project.

## Live Checks

| URL | Status | Privacy layer | Cookie/Yandex.Metrika notice | Consent checkbox | Policy content |
|---|---:|---:|---:|---:|---:|
| `https://moonn.ru/` | `200` | yes | yes | `2` forms / `2` required unchecked checkboxes | link to `/politic` |
| `https://moonn.ru/politic` | `200` | yes | yes | n/a | operator, INN, OGRNIP, email, cookies, Yandex.Metrika/Webvisor |
| `https://moonn.ru/psiholog-konsultacii-moskva` | `200` | yes | yes | no native forms detected on rendered page | link to `/politic` |
| `https://moonn.ru/events_tp` | `200` | yes | not separately rendered in this check | not separately rendered in this check | link layer present |

## Verified Rendered Policy Data

The rendered `/politic` page includes:

- `индивидуальный предприниматель Кумскова Татьяна Михайловна`;
- `ИНН 770906685276`;
- `ОГРНИП 316774600553212`;
- `moonn.official@yandex.ru`;
- cookies, Yandex.Metrika and Webvisor disclosure;
- user rights and request/withdrawal/deletion procedure.

## Consent Checkbox Verification

Rendered homepage forms include injected required checkboxes:

- checkbox name: `moonn_personal_data_consent`;
- default state: unchecked;
- `required: true`;
- policy link: `https://moonn.ru/politic`;
- visible text mentions personal-data processing, cookies and Yandex.Metrika.

## Important Limitation

`scripts/moonn_privacy_compliance_audit.py` is a raw-HTML scanner. It does not execute JavaScript, so it still reports `forms_without_detected_checkbox` for many pages even though rendered browser verification confirms the compliance layer on republished pages. For RKN hardening, the next stronger step is source-level/native Tilda form checkboxes and native policy text blocks, not only the global JS layer.

## Native Policy Source-Level Hardening

After the rendered privacy layer was published, `/politic` was also hardened at the native Tilda block level.

Verification:

| Layer | Result |
|---|---|
| Tilda API `getpagefull`, page `58199199` | native text contains `Политика обработки персональных данных` |
| Tilda API `getpagefull`, page `58199199` | legacy title `ПОЛИТИКА КОНФИДЕНЦИАЛЬНОСТИ` no longer found |
| Tilda API `getpagefull`, page `58199199` | INN `770906685276`, OGRNIP `316774600553212`, `moonn.official@yandex.ru`, Yandex.Metrika/Webvisor text found |
| Live raw HTML `https://moonn.ru/politic?native-check=20260508` | HTTP `200`; same native policy markers found |
| Live raw HTML | privacy compliance layer still present |

Native policy text artifact:

- `docs/moonn-native-politic-text-2026-05-08.txt`

## Native Form Inventory

Created native form inventory:

- `docs/moonn-native-form-inventory-2026-05-08.json`

Inventory scope:

- `15` production pages with form-like Tilda blocks.
- `21` form/cart/custom-code candidate blocks.
- `1` block already has a native checkbox signal: `https://moonn.ru/st1`, rec `1060387556`.
- `20` blocks require review because some are true forms and some are false positives such as cart/custom-code/lecture sections.

High-priority first native checkbox target:

- Homepage `https://moonn.ru/`, page `42678538`, real contact form rec `691008996`.

Current live mitigation remains active: the JS privacy layer adds required unchecked consent checkboxes on rendered forms. The stronger native checkbox pass is still open and should be done block-by-block through supported Tilda form settings, with API/live verification after each batch.

## Remaining Hardening

- Clean duplicated legacy SEO/schema tail from Tilda global head when a stable native editor path is available.
- Add native unchecked consent checkboxes in Tilda form settings on confirmed real forms, starting with the homepage form `rec691008996`.
- Decide whether to create or redirect `/privacy`, `/personal-data-consent`, `/cookies`, and `/data-subject-request` to `/politic`.
- Legal review is still required before treating the site as fully compliant; this is technical mitigation, not legal advice.
