# 2026-05-11 Tatiana Moonn Art Gallery Tilda Publication Packet

## Scope

- Project: Moonn / Tatiana Moonn art gallery.
- Branch: `codex/moonn-art-gallery`.
- Intended URL: `https://moonn.ru/kartiny-tatiany-munn`.
- Homepage page id: `42678538`.
- Tilda project id: `8326812`.

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
