# Moonn Homepage SEO/AEO Pilot

Date: 2026-05-01
Project: `moon-psy-site`
Workstream: `seo-aeo-retrofit`
Page: `https://moonn.ru/`
Staging page: `https://carry-pacific-flatfish.tilda.ws/`

## Strategic Assessment

1. Platform value: high. The homepage is the routing hub for consultations, lectures, paid products, and the knowledge base.
2. Obsolescence risk: high if SEO is handled as one shared text block across all pages. Search and AI answers need page-specific entity/context signals.
3. Stronger architecture: use a schema-first SEO manifest per page, then generate Tilda settings, JSON-LD, image metadata, and QA checks from that manifest.
4. Reuse: the same pattern can scale to consultations, lectures, paid courses, articles, and knowledge-base pages.
5. 3-12 month risk if skipped: duplicate metadata, weak image signals, unstable indexing, no clear entity graph, and manual edits that drift between production and staging.

## Verified Facts

- Production homepage returns HTTP 200.
- Staging homepage returns HTTP 200 and has `noindex,nofollow`, which should stay while it is a test copy.
- Current homepage has no JSON-LD.
- Current page structure has several H1 headings, but the main hero offer is not the primary H1.
- No H2 headings were detected in the sampled DOM.
- Most meaningful homepage images have empty `alt`.
- Current `og:image` points to a Tilda CDN image named `___.jpg`.
- Public search shows brand coverage for queries around `Татьяна Мунн`, but real frequency, CTR, and indexing causes require Google Search Console and Yandex Webmaster.

## Pilot Metadata

Recommended production title:

```text
Психолог МГУ Татьяна Мунн в Москве | быстрая психология
```

Recommended description:

```text
Татьяна Мунн — психолог МГУ в Москве. Индивидуальные консультации онлайн и в кабинете: стресс, выгорание, отношения, эмоции и эмоциональный интеллект.
```

Why this is stronger:

- It keeps the main entity at the start: `Психолог МГУ Татьяна Мунн`.
- It avoids guarantee-like wording such as `быстрый результат за 1-3 встречи`.
- It keeps the primary service and local context.
- It gives AI/search systems a concise entity + service + topic summary.

## AEO Entity Model

For the homepage, use a page-level JSON-LD graph with:

- `WebSite`: `moonn.ru` as the site entity.
- `WebPage`: the homepage as the routing hub.
- `Person`: Tatiana Munn as the expert entity.
- `ProfessionalService`: psychological consultations in Moscow/online.
- `OfferCatalog`: consultation, lectures, paid programs, knowledge base.
- `BreadcrumbList`: homepage root.

Do not add `FAQPage` or `Review` schema until those questions/reviews are visible on the page and verified.

## Entity Linking: Moonn, Kumskova, Yandex Services, MSU Istina

The public site mostly uses `Татьяна Мунн`, while important authority platforms use the legal/platform variant:

- Yandex Services profile: `https://yandex.ru/uslugi/profile/TatyanaKumskova-948629`
- MSU Istina profile: `https://istina.msu.ru/workers/816305440/`
- Istina observed name: `Кумскова Татьяна Михайловна`, IRID `816305440`

This should be handled on two levels:

- visible text, so users and crawlers can read the identity bridge;
- structured data, so search/AI systems can merge the entity graph.

Recommended visible bridge near the biography/trust section:

```text
Татьяна Мунн — публичное имя психолога Татьяны Михайловны Кумсковой. Внешние профили: Яндекс Услуги с отзывами клиентов и научно-образовательный профиль МГУ ИСТИНА.
```

Recommended schema updates:

- `Person.name`: `Татьяна Мунн`
- `Person.alternateName`: `Татьяна Мунн (Кумскова)`, `Татьяна Кумскова`, `Кумскова Татьяна Михайловна`, `Татьяна.К.М.`
- `Person.sameAs`: Yandex Services, MSU Istina, Telegram and other verified public profiles.

Do not put the legal-name bridge only inside invisible JSON-LD. For entity reconciliation it should also appear in a concise, natural, visible biography/trust block.

## Image SEO

Primary SEO asset prepared in the repo:

```text
assets/images/tatiana-munn-psiholog-mgu-moscow-consultation.webp
```

Target use:

- `og:image`
- `schema.org` image
- primary meaningful portrait/image replacement if uploaded to Tilda

Recommended alt:

```text
Татьяна Мунн, психолог МГУ в Москве
```

Rules for scaling:

- File names use Latin characters only.
- Internal marketing tokens may exist in filenames or metadata, but not in visible page text.
- Decorative gradients/orbs should use empty alt.
- Meaningful photos, certificates, lecture previews, and course covers need concise contextual alt text.

## Heading Structure

Recommended H1:

```text
Психолог МГУ Татьяна Мунн в Москве
```

Recommended H2 sections:

- Индивидуальные консультации
- Эмоциональный интеллект и психология эмоций
- Лекции, выступления и корпоративные программы
- Стоимость и форматы работы
- Отзывы и доверие
- База знаний по эмоциональному интеллекту

Current section titles that should not remain H1:

- `ТЕМЫ ЛЕКЦИЙ, КОТОРЫЕ Я ЧИТАЮ`
- `ТЕМЫ ЛЕКЦИЙ, КОТОРЫЕ ЧИТАЮ`
- `ОБРАЗОВАНИЕ - МГУ`
- `психолог Татьяна Мунн рекомендует`
- `Яндекс-Услуги`

## Link Cleanup

Before production transfer, fix malformed links found on the homepage:

- `https://moonn.ru/http://n461584.yclients.com/`
- `https://moonn.ru/http://wa.me/+79777770303`
- internal `http://moonn.ru/...` links should become `https://moonn.ru/...`
- old domains such as `moonn-psy.ru` should be checked and either redirected or replaced.

## Data Needed For Real Query And Indexing Analysis

Public search can show that some pages are indexed, but it cannot answer what people really type, how often pages appear, CTR, or why pages are excluded.

Required access:

- Google Search Console for `moonn.ru`
- Yandex Webmaster for `moonn.ru`
- Yandex Metrica or GA4
- Tilda/analytics goal data for buttons/forms

Exports needed:

- top queries for the last 16 months;
- top pages by impressions/clicks;
- pages indexed/excluded;
- sitemap status;
- Core Web Vitals/page experience;
- click goals for forms, messengers, payments, and course pages.

## Tilda Implementation Order

1. Keep staging `noindex,nofollow`.
2. Update staging homepage title and description in page SEO settings.
3. Add JSON-LD in the staging homepage HEAD.
4. Set social title/description/image on the staging homepage.
5. Fix homepage H1/H2 hierarchy in content.
6. Add alt text to meaningful homepage images.
7. Publish staging only.
8. Verify browser result, page source, metadata, schema, and image preview.
9. After approval, repeat the same manifest pattern for every page category.

## Tilda-Native SEO Tools To Use

Tilda should remain the operational source for page-level SEO settings, not a place where we paste one giant uncontrolled code block. Use the native controls first:

- Site Settings → SEO → SEO Assistant: check pages, indexing errors, redirects, favicon, HTTPS/WWW settings.
- Site Settings → SEO → Google Search Console: connect or verify Google ownership.
- Site Settings → SEO → 301 redirects: fix old page URLs and malformed legacy paths.
- Page Settings → SEO → Customize search results preview: unique title, description, keywords, canonical URL.
- Page Settings → Social media → Customize social media preview: social title, description, and preview image.
- Block settings → SEO title tag: set exactly one H1, then H2/H3 for sections.
- Block content/image menu: set image alt text for meaningful images; skip decorative backgrounds.
- Page Settings → Additional → HTML code for Head: add JSON-LD/schema.org for entity graph and AEO.
- `/robots.txt` and `/sitemap.xml`: Tilda generates these automatically, but they must be checked after publishing.

For Moonn, this means:

- native Tilda fields handle title, description, canonical, social preview, H1/H2/H3, alt text, redirects;
- custom Head code handles JSON-LD only;
- SEO Assistant becomes the first QA gate before browser/source-code checks.

## Scaling Plan

Page-specific SEO manifests should be created for these clusters:

- Homepage and brand pages.
- Consultation/service pages.
- Lectures, events, and corporate training pages.
- Paid products, courses, video lectures, and checkout pages.
- Emotional intelligence articles and knowledge-base pages.
- Reviews, credentials, contacts, and trust pages.

Each page manifest must include:

- URL and Tilda page id;
- search intent cluster;
- title/description;
- H1/H2 plan;
- image map and alt plan;
- schema.org graph;
- canonical URL;
- internal links;
- compliance notes;
- QA status.

## Sources

- Google title links: https://developers.google.com/search/docs/appearance/title-link
- Google image SEO: https://developers.google.com/search/docs/appearance/google-images
- Google structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Tilda SEO guide: https://help.tilda.cc/search-engine
- Tilda microdata guide: https://help.tilda.cc/microdata
- Tilda ownership verification: https://help.tilda.cc/domain-confirm
