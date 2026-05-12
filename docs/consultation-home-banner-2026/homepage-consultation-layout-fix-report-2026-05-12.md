# Moonn Homepage Consultation Banner Layout Fix — 2026-05-12

## Scope

- Project: Moonn / Tatiana Munn site.
- Branch: `codex/moonn-homepage-consultation-fix`.
- Target: homepage T123 record `2251351151`, page `42678538`.

## Incident

- Symptom: the homepage consultation banner visually stretched downward and absorbed the next native Tilda blocks, including the `Татьяна Мунн / Направления` area.
- Root cause: the consultation section in the combined homepage artifacts was truncated inside the summer-price markup and did not close its HTML tags or `</section>`.
- Fix: replaced the broken section with a compact, bounded consultation block while preserving the Tilda native cart bridge and product SKUs.

## Changed Artifacts

- `scripts/fix_moonn_homepage_consultation_banner.py`
- `docs/consultation-home-banner-2026/tilda-html-block-compact-final.html`
- `docs/consultation-home-banner-2026/homepage-t123-combined-compact-preview.html`
- `docs/tatiana-munn-exam-prep/homepage-t123-combined-2026-05-12.html`
- `docs/tatiana-munn-art-gallery/homepage-t123-combined-2026-05-12.html`

## Local Verification

- `python -m py_compile scripts\fix_moonn_homepage_consultation_banner.py`
- `python scripts\fix_moonn_homepage_consultation_banner.py`
- Playwright preview check across 1280px, 825px, and 390px widths.

Evidence:

- `docs/consultation-home-banner-2026/homepage-consultation-compact-preview-2026-05-12.json`
- `docs/consultation-home-banner-2026/homepage-consultation-compact-preview-desktop-2026-05-12.png`
- `docs/consultation-home-banner-2026/homepage-consultation-compact-preview-tablet825-2026-05-12.png`
- `docs/consultation-home-banner-2026/homepage-consultation-compact-preview-mobile390-2026-05-12.png`

## Live Publication

- Git commit used for the published artifact: `ab2d71861f04d9171cf7b8a68de1fb00777fe11a`.
- Tilda homepage page id: `42678538`.
- Tilda homepage T123 record: `2251351151`.
- Save confirmation in Tilda console: `MOONN_CONSULT_FIX_SAVED 106478`.
- Published URL: `https://moonn.ru/`.

Live verification:

- Raw HTML `https://moonn.ru/?consultation-layout-fix=20260512-ab2d718` returned status `200`.
- Raw HTML contains `data-moonn-consultation-compact="2026-05-12"`.
- Raw HTML does not contain the old broken marker `moonn-consultation-home-signature`.
- Playwright live render at 825px confirms the consultation banner height is `519px`.
- The next `Татьяна Мунн / Направления` block starts at the consultation banner bottom, with no overlap.

Live evidence:

- `docs/consultation-home-banner-2026/homepage-consultation-compact-live-2026-05-12.json`
- `docs/consultation-home-banner-2026/homepage-consultation-compact-live-tablet825-2026-05-12.png`

## Readiness Rule

Homepage promo T123 updates are not complete until the combined artifact is parsed/rendered and adjacent block bounding boxes are checked for order and height. Marker-only checks are insufficient.
