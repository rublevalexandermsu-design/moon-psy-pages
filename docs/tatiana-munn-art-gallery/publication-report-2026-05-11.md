# 2026-05-11 Tatiana Moonn Art Gallery Tilda Publication Packet

## Scope

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Intended URL: `https://moonn.ru/kartiny-tatiany-munn`.
- Homepage page id: `42678538`.
- Tilda project id: `8326812`.
- CDN ref for Tilda assets: `132d5486ee27e3782f5d00905c94baba75c2a927`.

## Generated Artifacts

- `tilda-html-block-final.html` - native Tilda T123 block for the gallery page.
- `tilda-page-final.html` - standalone preview page using the same Tilda-safe block.
- `tilda-head-loader-final.html` - minimal head/base snippet.
- `tilda-head-seo-final.html` - SEO and schema layer.
- `homepage-art-gallery-block-final.html` - homepage banner linking to `/kartiny-tatiany-munn`.
- `data/tilda-payment-products.json` - native Tilda cart product manifest.

## Payment Products

- Products: `10` artworks.
- Price range: `170000`-`700000` RUB.
- Payment route: native Tilda cart / T-Bank through `tcart__addProduct`, `tcart__reDrawCartIcon`, `tcart__openCart`.

## Publication Gate

- Do not submit a real payment.
- Create or update the Tilda page with alias `kartiny-tatiany-munn`.
- Add a native Tilda cart/payment block (`T706`/`ST100`) on the gallery page before payment QA.
- Publish the gallery page.
- Add `homepage-art-gallery-block-final.html` to the homepage near the existing consultation/camp promo banners.
- Verify live HTML contains `moonn-art-gallery-tilda-page` and `moonn-art-gallery-home-banner`.
- Verify at least one artwork CTA opens the native cart with the correct artwork name and amount.
- Verify T-Bank provider screen is reachable without entering card data.

## Live Publication

- Created Tilda page `140864526`.
- Page alias: `kartiny-tatiany-munn`.
- Live URL: `https://moonn.ru/kartiny-tatiany-munn`.
- Page title: `Картины Татьяны Мунн | 3D-галерея и персональный код`.
- Added native Tilda `T123` record `2258253531` with `tilda-html-block-final.html`.
- Added native Tilda cart/payment record `2258267581`, block type `ST100` / `T706`.
- Published the gallery page from the Tilda editor.

## Homepage Banner Publication

- Homepage page id: `42678538`.
- Existing homepage T123 record: `2251351151`.
- Preserved existing promo markers:
  - `moonn-teen-camp-home-banner`
  - `moonn-consultation-home-banner`
- Inserted `homepage-art-gallery-block-final.html` into the same homepage T123 block before the consultation banner.
- Evidence artifact: `homepage-t123-combined-2026-05-12.html`.
- Published the homepage from the Tilda editor.

## Compact Homepage Banner Refresh

- Date: `2026-05-12`.
- User correction: the homepage gallery block must visually match the compact teen-camp banner and sit directly below it, not use the previous dark premium banner style.
- Updated canonical generator `scripts/build_tatiana_munn_art_gallery_site.py`.
- Regenerated `homepage-art-gallery-block-final.html`.
- Updated `homepage-t123-combined-2026-05-12.html` so the existing homepage T123 record keeps this order:
  - teen camp banner
  - compact art gallery banner
  - consultation banner
- Local visual preview:
  - Gallery block width: `1160`.
  - Gallery block height: `577`.
  - Teen-camp block height in same preview: `565`.
  - CTA href: `/kartiny-tatiany-munn`.
  - Dark banner CSS marker `#090b12` absent.
- Preview artifact: `homepage-gallery-compact-preview-2026-05-12.png`.
- Tilda live refresh status: prepared; final live verification is pending after updating record `2251351151`.

## Live Verification

- Gallery live HTML check: `https://moonn.ru/kartiny-tatiany-munn?gallery-live-check=20260512-0126`.
  - HTTP status `200`.
  - `moonn-art-gallery-tilda-page` present.
  - Native cart markers present.
  - `moonn-art-gallery-01-blue-flower-harmony` present.
  - `soundcloud` absent.
- Gallery browser render check:
  - Page title is correct.
  - `#moonn-art-gallery-tilda-page` present.
  - `#galleryCanvas` present.
  - Native cart present.
  - SoundCloud absent.
- Homepage live HTML check before compact refresh: `https://moonn.ru/?homepage-gallery-banner-check=20260512-0141`.
  - HTTP status `200`.
  - `moonn-teen-camp-home-banner` present.
  - `moonn-art-gallery-home-banner` present.
  - `moonn-consultation-home-banner` present.
  - `/kartiny-tatiany-munn` link present.
  - `soundcloud` absent.
- Homepage compact-banner live verification: pending after publishing the refreshed T123 code.
- Gallery cart smoke test after clearing previous Tilda cart state:
  - `Гармония и чувственность — картина Татьяны Мунн` opened native Tilda cart.
  - SKU: `moonn-art-gallery-01-blue-flower-harmony`.
  - Amount: `700 000р.`.
  - No real payment was submitted.

## Incident Note

- Symptom: an initial attempt used Tilda internal template id `123`, which created an unwanted SoundCloud/media block in an unpublished draft page.
- Root cause: Tilda template id `123` is not the `T123` custom HTML block; the correct custom HTML block has `data-record-type="131"` and saves code through the `code` field.
- Resolution: deleted the unpublished erroneous draft page `140863116`, verified through Tilda API that it no longer exists, then used template id `131` for the gallery page.
- Follow-up rule: for Tilda custom HTML work, verify `data-record-type="131"` and the expected marker before publishing; never infer `T123` from template id `123`.

## Status

- Gallery page is live.
- Homepage gallery banner is live, but compact visual refresh is pending final Tilda record update and live check.
- Native cart opens with the correct first artwork product, SKU and amount.
- T-Bank provider transition without card submission still remains a separate high-risk payment QA step.
