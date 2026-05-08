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

Initially prepared a homepage banner and external JS asset, but the current Tilda page HEAD editor for the homepage rejected/rolled back both:

1. a full inline banner snippet;
2. a shorter external script reference.

The live homepage integration was then completed through a native Tilda `T123` HTML block on the homepage, placed after the first running blue text strip and before the next large content section.

Live homepage check `https://moonn.ru/?camp-banner-check=20260508-2141`:

- HTTP: `200`
- Banner marker `moonn-teen-camp-home-banner`: yes
- Link `/podrostkovyy-lager-psihologiya`: yes
- Camp text `Подростковый лагерь`: yes
- SEO image `tatiana-moonn-teen-psychology-camp-hero-2026.jpg`: yes

Rendered Chrome verification:

- The homepage banner is visible in the early homepage flow.
- The banner button `Узнать программу` opens `https://moonn.ru/podrostkovyy-lager-psihologiya`.
- The banner image also points to the camp page.

## Decision

Do not keep forcing homepage HEAD edits through Tilda because it risks corrupting the existing homepage design/SEO layer. Homepage marketing placements should use native Tilda blocks/cards first, then be verified through live HTML and rendered Chrome.

## Button and asset verification

Checked `https://moonn.ru/podrostkovyy-lager-psihologiya?camp-page-check=20260508-2142`:

- HTTP: `200`
- Page title: `Подростковый лагерь по психологии — Татьяна Мунн`
- Canonical URL: yes
- JSON-LD: yes
- PDF link: yes
- Telegram link: yes
- Live H1: `Лето, которое помогает подростку понять себя и стать увереннее`

Interactive checks in Chrome:

- `Записаться в Telegram` opens `https://t.me/moonn_official` and shows the Telegram Desktop handoff prompt.
- Direct PDF URL opens in Chrome PDF viewer.
- Chrome PDF viewer download button created a new file in Downloads; first bytes verified as `%PDF-`.
- `Узнать про стоимость и рассрочку` currently opens WhatsApp. This is acceptable as a contact path, but if the intended behavior is scroll-to-price, that link should be changed in a separate Tilda edit.

## RKN / compliance

The landing page currently has no form. Therefore no form consent checkbox was required on this page. The page links to `/politic`. If a registration/payment form is added later, it must include an unchecked required consent checkbox and links to policy/consent documents before publication.
