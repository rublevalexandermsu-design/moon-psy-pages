# Moonn Staging Source Link Cleanup Batch 1

Generated: 2026-05-02T11:10:00+03:00

## Scope

- Project: `Moonn Staging` / Tilda project `25075076`.
- Purpose: test source-level cleanup of repeated link defects on copied Tilda pages before applying the same operation to production `moonn.ru`.
- API role: read/export verification only. Official Tilda API does not expose block editing methods, so source changes must be made in the Tilda editor and then verified by export.

## Current Staging Audit

- Pages checked: `148`.
- Pages with known link issues: `60`.
- `http_wa`: `90`.
- `bad_domain`: `39`.
- `bad_plus_wa`: `0`.
- `internalized_bad_plus_wa`: `0`.

## First UI Batch

| Priority | Staging page id | Alias/file | `http_wa` | `bad_domain` | Staging URL |
|---|---:|---|---:|---:|---|
| 1 | 138694136 | `abuse_gaslight` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/abuse_gaslight |
| 2 | 138691296 | `article_diary_of_emotions` | 1 | 1 | https://carry-pacific-flatfish.tilda.ws/article_diary_of_emotions |
| 3 | 138694396 | `article_femininity` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/article_femininity |
| 4 | 138694256 | `article_gadget_addiction` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/article_gadget_addiction |
| 5 | 138694546 | `article_toxic_job` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/article_toxic_job |
| 6 | 138662406 | `baza-znaniy-emocionalnyy-intellekt-psihologiya` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/baza-znaniy-emocionalnyy-intellekt-psihologiya |
| 7 | 138693676 | `eintellect` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/eintellect |
| 8 | 138665336 | `events` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/events |
| 9 | 138682696 | `geshtalt` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/geshtalt |
| 10 | 138682206 | `kpt` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/kpt |
| 11 | 138665516 | `lectures1` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/lectures1 |
| 12 | 138677976 | `otzivi` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/otzivi |
| 13 | 138661976 | `psiholog-konsultacii-moskva` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/psiholog-konsultacii-moskva |
| 14 | 138679376 | `psy4psy` | 1 | 0 | https://carry-pacific-flatfish.tilda.ws/psy4psy |
| 15 | 138682476 | `psychoanalys` | 2 | 1 | https://carry-pacific-flatfish.tilda.ws/psychoanalys |

## Edit Contract

For each page in the batch:

1. Pass the Tilda browser session gate below.
2. Open the staging page editor, not production.
3. Replace `http://wa.me/79777770303` with `https://wa.me/79777770303`.
4. Replace `http://.moonn.ru` with `https://moonn.ru`.
5. Save and publish the staging page.
6. Re-export the page through Tilda API and require both old-pattern counters to become `0`.
7. Only after the staging batch passes, apply the same page/block pattern to production pages.

## Tilda Browser Session Gate

Before any Tilda save or publish action:

1. Visible browser URL must be on `tilda.ru`, not `timepad.ru`, `moonn.ru`, or the staging public domain.
2. The Tilda account must already be authenticated; login pages and `tilda.ru/404/pagenotpublished/` do not pass.
3. The editor/project context must show staging project `25075076` / `Moonn Staging`, not production project `8326812`.
4. The active page id must match the current batch row.
5. If any of these checks fail, stop before editing and restore the correct Tilda session.

Current blocked state, 2026-05-02:

- Visible desktop Chrome window is on `TimePad.ru`, not Tilda.
- Browser Use in-app tab opens the direct staging editor URL as `https://tilda.ru/404/pagenotpublished/`.
- No staging page source edits were made in this session after the audit.

## UI Incident

- Symptom: while preparing the first staging UI edit, manual pointer automation switched focus to an unrelated Chrome/Timepad tab.
- Root cause: the current visible Chrome session contains several active browser tabs/windows, and coordinate-based clicks are too easy to misroute for mass edits.
- Rule: before mass Tilda UI edits, open a dedicated Chrome window/tab for one Tilda project and verify the address/project breadcrumb before every save/publish action.
