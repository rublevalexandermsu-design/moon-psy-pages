# Moonn Teen Psychology Camp Publication Report — 2026-05-08

## Scope

Publish the teen psychology camp landing page on `moonn.ru`, preserve SEO/AEO and RKN checks, and start homepage integration.

## Published page

- Live URL: https://moonn.ru/podrostkovyy-lager-psihologiya
- Tilda project: `8326812`
- Tilda page id: `140348786`
- Page title: `Подростковый лагерь по психологии — Татьяна Мунн`
- URL alias: `podrostkovyy-lager-psihologiya`

## Source artifacts

- `assets/teen-psychology-camp-2026/` — SEO-named image/PDF assets.
- `docs/teen-psychology-camp-2026/asset-manifest.json` — asset provenance.
- `docs/teen-psychology-camp-2026/tilda-page-final.html` — full cleaned page.
- `docs/teen-psychology-camp-2026/tilda-html-block-final.html` — body HTML block variant.
- `docs/teen-psychology-camp-2026/tilda-head-injection-final.html` — page HEAD injection used in Tilda.
- `assets/teen-psychology-camp-2026/moonn-home-teen-camp-banner.js` — prepared external homepage banner asset.

## Live verification

Checked `https://moonn.ru/podrostkovyy-lager-psihologiya?final-check=20260508b`:

- HTTP: `200`
- Hero/H1 text present: yes
- JSON-LD present: yes
- Canonical URL present: yes
- `/politic` privacy link present: yes
- Kaspersky source residue: no
- Base64 payloads: no
- `data:image`: no
- CDN asset references: yes

## Homepage integration status

Prepared a homepage banner and external JS asset, but the current Tilda page HEAD editor for the homepage rejected/rolled back both:

1. a full inline banner snippet;
2. a shorter external script reference.

The live homepage still does not contain `/podrostkovyy-lager-psihologiya`, so homepage integration is not reported as completed.

## Decision

Do not keep forcing homepage HEAD edits through Tilda because it risks corrupting the existing homepage design/SEO layer. The next safe step is to add a native Tilda block/card on the homepage, or use a supported existing block and link it to `/podrostkovyy-lager-psihologiya`, then publish and verify live.

## RKN / compliance

The landing page currently has no form. Therefore no form consent checkbox was required on this page. The page links to `/politic`. If a registration/payment form is added later, it must include an unchecked required consent checkbox and links to policy/consent documents before publication.
