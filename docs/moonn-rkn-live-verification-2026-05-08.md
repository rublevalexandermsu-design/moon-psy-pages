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

## Remaining Hardening

- Clean duplicated legacy SEO/schema tail from Tilda global head when a stable native editor path is available.
- Convert `/politic` from rendered JS replacement to native Tilda text blocks, so raw HTML contains the same policy text.
- Add native unchecked consent checkboxes in Tilda form settings on high-traffic forms, starting with the homepage forms.
- Decide whether to create or redirect `/privacy`, `/personal-data-consent`, `/cookies`, and `/data-subject-request` to `/politic`.
- Legal review is still required before treating the site as fully compliant; this is technical mitigation, not legal advice.
