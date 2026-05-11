# 2026-05-11 Pause Handoff — Tatiana Moonn Art Gallery / Tilda Publication

Use this handoff to resume the art-gallery publication workstream without mixing it with the consultation-banner workstream.

## Workstream

- Project: Moonn / Tatiana Moonn art gallery.
- Repository: `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`
- Branch: `codex/moonn-art-gallery`
- Intended page alias: `kartiny-tatiany-munn`
- Intended live URL: `https://moonn.ru/kartiny-tatiany-munn`

## Current Pause State

- User asked to stop the art-gallery publication task safely and return later.
- The canonical generator compiles:
  - `python -m py_compile scripts\build_tatiana_munn_art_gallery_site.py`
- Work in progress is limited to `scripts/build_tatiana_munn_art_gallery_site.py`.
- No Tilda live publication was performed in this paused state.
- No payment provider flow was tested for the gallery in this paused state.

## What Was Started

- Added early Tilda publication constants for:
  - GitHub/jsDelivr base URL.
  - Tilda page alias.
  - Tilda project/homepage identifiers.
- Added artwork checkout fields into generated artwork records:
  - `priceValue`
  - `priceCurrency`
  - `sku`
  - `checkoutName`
  - `checkoutImage`
  - `tildaProductHref`
- Started adapting generated gallery assets to work with a Tilda/CDN base URL:
  - `window.MOONN_ART_GALLERY_BASE_URL`
  - `window.MOONN_ART_GALLERY_TILDA_MODE`
  - `assetUrl(...)` in gallery JS.
- Started adding public catalog and personal-code sections into `index.html`.

## Not Yet Done

- Finish native Tilda cart bridge in `APP_JS`.
- Generate Tilda-ready artifacts:
  - `docs/tatiana-munn-art-gallery/tilda-page-final.html`
  - `docs/tatiana-munn-art-gallery/tilda-head-loader-final.html`
  - `docs/tatiana-munn-art-gallery/tilda-head-seo-final.html`
  - `docs/tatiana-munn-art-gallery/homepage-art-gallery-block-final.html`
  - `docs/tatiana-munn-art-gallery/data/tilda-payment-products.json`
  - `docs/tatiana-munn-art-gallery/publication-report-2026-05-11.md`
- Run local browser QA for the Tilda-safe page.
- Create/update the actual Tilda page.
- Add required native Tilda cart block (`ST100` / `.t706`) before payment testing.
- Publish and verify live HTML/browser/cart behavior.

## Resume Checklist

1. Stay on `codex/moonn-art-gallery`.
2. Read this handoff, then the latest art-gallery entries in `docs/codex-chat-history.md`.
3. Finish generator changes before touching Tilda live.
4. Regenerate the static package.
5. Run browser QA.
6. Only then publish to Tilda with native cart present.
7. Verify live page, cart product, amount and provider screen without submitting a real payment.

## Guardrail

Do not mix this paused art-gallery work with the consultation-banner workstream. Consultation homepage/payment work should use a separate branch.
