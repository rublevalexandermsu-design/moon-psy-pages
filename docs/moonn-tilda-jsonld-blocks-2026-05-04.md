# Moonn Tilda JSON-LD Blocks — 2026-05-04

Workstream: `moonn-live-seo-audit`  
Branch: `codex/moonn-seo-audit`  
Status: prepared, no live Tilda edits

## Purpose

This packet contains ready JSON-LD objects for the 9 priority Moonn pages audited on 2026-05-03.

Use it only through supported Tilda page head/code fields. Do not use undocumented Tilda endpoints.

## Included Pages

- `https://moonn.ru/`
- `https://moonn.ru/events_tp`
- `https://moonn.ru/lectures1`
- `https://moonn.ru/psiholog-moskva-online`
- `https://moonn.ru/psiholog-konsultacii-moskva`
- `https://moonn.ru/uslugi_depression`
- `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei`
- `https://moonn.ru/emotional-intelligence/knowledge-base/empathy`
- `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication`

## Entity Bridge

All graphs connect to the same public person entity:

- `Татьяна Мунн`
- `Кумскова Татьяна Михайловна`
- `Татьяна Мунн (Кумскова)`
- `Психолог МГУ, эксперт по эмоциональному интеллекту`

sameAs links:

- `https://moonn.ru/`
- `https://moonn.timepad.ru/events/`
- `https://miiiips.ru/author-tatyana-munn-kumskova.html`
- `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`
- `https://istina.msu.ru/workers/816305440/`
- `https://psyjournals.ru/authors/15337`

## Deliberate Safety Limits

- No `AggregateRating`.
- No `Review`.
- No copied Yandex review text.
- No private video links.
- No price/payment/product data.
- No medical treatment guarantees or `MedicalBusiness`.

## Tilda Application Rule

For each page:

1. Open the page settings in Tilda.
2. Insert the matching JSON-LD graph into the supported page head/code field.
3. Publish the page.
4. Re-audit the live URL for `application/ld+json`.
5. Request indexing only after live verification.

The machine-readable source is:

`docs/moonn-tilda-jsonld-blocks-2026-05-04.json`

## Notes

- Lecture `ItemList` nodes intentionally have empty `itemListElement` until public lecture cards are verified.
- FAQPage nodes intentionally have empty `mainEntity` until visible FAQ text is verified on each page.
- Reviews schema is excluded until the Yandex Services reviews gate is approved.
