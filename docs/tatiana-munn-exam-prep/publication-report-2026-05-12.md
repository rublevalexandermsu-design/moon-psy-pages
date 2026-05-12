# Tatiana Moonn Exam Prep Tilda Publication — 2026-05-12

## Scope

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-exam-prep-tilda`.
- Source HTML: `C:\Users\yanta\Downloads\tatiana-moonn-exam-landing-v3-self-contained.html`.
- Published page URL: `https://moonn.ru/psypodgotovka1`.
- Homepage URL: `https://moonn.ru/`.

## Tilda Targets

- Project: `8326812`.
- Exam-prep page: `62652841`.
- Exam-prep T123 record: `2258994191`.
- Homepage: `42678538`.
- Homepage T123 record: `2251351151`.

## GitHub/CDN

- Branch pushed: `codex/moonn-exam-prep-tilda`.
- Latest pushed commit during publication: `72059438c1fcba2433af7055f729a9a8556583d1`.
- Page loader points to generated content commit: `124daecc2f8fe05460b6884d6c5edccb73391aca`.

## Artifacts

- `docs/tatiana-munn-exam-prep/tilda-html-block-final.html`
- `docs/tatiana-munn-exam-prep/tilda-html-loader-final.html`
- `docs/tatiana-munn-exam-prep/tilda-page-final.html`
- `docs/tatiana-munn-exam-prep/homepage-exam-prep-block-final.html`
- `docs/tatiana-munn-exam-prep/homepage-t123-combined-2026-05-12.html`
- `docs/tatiana-munn-exam-prep/manifest.json`

## Verification

- Tilda API page check: live page HTML contains `moonn-exam-prep-tilda-page-loader` and commit `124daecc2f8fe05460b6884d6c5edccb73391aca`.
- Live page check: `https://moonn.ru/psypodgotovka1` returns `200`, contains the loader marker, has no SoundCloud marker.
- Browser render check: loader is removed after fetch, `#moonn-exam-prep-tilda-page` appears, H1 is `Психологическая подготовка к экзаменам без паники`, form exists.
- Tilda API homepage check: homepage HTML contains these markers in order:
  - `moonn-teen-camp-home-banner`
  - `moonn-art-gallery-home-banner`
  - `moonn-exam-prep-home-banner`
  - `moonn-consultation-home-banner`
- Live homepage check: `https://moonn.ru/` returns `200`, exam-prep CTA href is `/psypodgotovka1`, SoundCloud marker is absent.
- Browser homepage render check: exam-prep banner title is `Экзамены без паники`, CTA href is `/psypodgotovka1`.

## Evidence Screenshots

- `docs/tatiana-munn-exam-prep/exam-prep-live-render-2026-05-12.png`
- `docs/tatiana-munn-exam-prep/homepage-exam-prep-live-render-2026-05-12.png`

## Notes

- The existing alias `psypodgotovka1` was preserved to avoid creating a duplicate public URL.
- The full page is served through a lightweight Tilda loader because the self-contained page is large due to inline images.
- The root `codex/ano-context-recovery` uncommitted context-backup files were not mixed into this Moonn publication branch.
