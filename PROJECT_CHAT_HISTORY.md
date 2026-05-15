# Project Chat History

Append-only project history for `moon-psy-pages`.

## 2026-05-15 13:05 Europe/Moscow - Timepad Direct Registration Widget Pages

- Project: Moonn / Tatyana Munn / Timepad registration UX.
- Workstream: Timepad relations recurring lecture series.
- Branch: `main` because GitHub Pages deployment for `school.miiiips.ru` runs only from `main`.
- User request:
  - verify the live click from Timepad lecture cards;
  - find a way for each lecture card to open the selected registration form, not the recurring date list.
- Verified facts:
  - Clicking `https://moonn.timepad.ru/event/3889452/#register` redirects back to the recurring master page and shows the date-choice list.
  - Timepad's widget supports `prefill.recurringEvent` when embedded directly.
  - A local generated page with `prefill.recurringEvent=3889452` opens the form for `18 мая 2026, 19:00` with the email/name/phone fields visible.
- Decision:
  - Add static noindex registration-helper pages under `/timepad/relations-lecture-XX-register/`.
  - These pages are not SEO pages; they are UX bridges from Timepad lecture cards to preselected Timepad widget forms.
- Created or changed files:
  - `build_site.py`
  - `data/timepad-registration-pages.json`
- Verification:
  - `python -m py_compile build_site.py`
  - `python build_site.py --output dist_test_timepad_widget`
  - Playwright opened local `relations-lecture-07-register` and confirmed selected form state: form visible, date list absent, `18 мая 2026` present.
- Next downstream step:
  - Update the Timepad master event cards to link to these `school.miiiips.ru` registration-helper pages after GitHub Pages deployment is live.
