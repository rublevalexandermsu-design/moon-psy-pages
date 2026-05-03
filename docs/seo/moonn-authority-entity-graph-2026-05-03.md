# Moonn Authority Entity Graph

Date: 2026-05-03
Scope: `moonn.ru` production SEO/AEO, 83-page enhancer asset.

## Decision

Do not use hidden keyword text for SEO. The Moonn/Kumskova/MSU/MIBS connection must be expressed through:

- a small visible editorial bridge near the page footer;
- `schema.org/Person` `alternateName`, `sameAs`, `affiliation`, and `subjectOf`;
- consistent off-site profile text on Timepad, Yandex Services, MSU Istina, PsyJournals, and the institute site.

## Verified Entity Links

- Primary site: `https://moonn.ru/`
- Yandex Services: `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`
- Timepad events/organizer: `https://moonn.timepad.ru/events/`
- MSU Istina: `https://istina.msu.ru/workers/816305440/`
- PsyJournals author page: `https://psyjournals.ru/authors/15337`
- Institute/MIBS contour: `https://miiiips.ru/`

The canonical registry for this graph is `registry/seo/moonn-authority-entity-graph.json`.

## Implemented In Code

`scripts/build_moonn_seo_enhancer.py` now reads the entity graph registry and applies it to every generated page schema:

- adds `Татьяна Мунн (Кумскова)`, `Татьяна Кумскова`, `Кумскова Татьяна Михайловна` to `Person.alternateName`;
- adds Yandex Services, Timepad, MSU Istina, PsyJournals, and MIBS/MIIIIPS to `Person.sameAs`;
- adds `Person.affiliation` for the institute contour;
- adds `Person.subjectOf` references for external public profiles;
- injects a visible footer-level identity bridge with profile links.

## Off-Site SEO/AEO Backlog

1. Create or update the author page on `miiiips.ru` for Tatiana Munn/Kumskova with the same `Person` JSON-LD and reciprocal links to `moonn.ru`, Timepad, Yandex Services, Istina, and PsyJournals.
2. Update Timepad organizer/event descriptions with a consistent speaker block: `Татьяна Мунн (Кумскова Татьяна Михайловна), психолог МГУ, эксперт по эмоциональному интеллекту`, plus a link to `https://moonn.ru/`.
3. Ensure Yandex Services visible text includes both name variants and the site link where the platform allows it.
4. Add a controlled institute profile page to the Moonn/entity graph before trying weaker directory links.
5. After live deployment, request indexing in Google Search Console and Yandex Webmaster for the homepage, lecture hub, consultation hub, paid products, and the new institute author page.

## Deployment Note

Production Tilda pages currently load `moonn-seo-aeo-enhancer.js` pinned to commit `8dd2572`. This code update is ready in GitHub, but it will not affect the live Tilda pages until the Tilda head snippets are updated to the new asset URL or to a stable loader. The stronger long-term route is a one-time Tilda update to a stable loader so future SEO/AEO graph changes can be deployed by code without occupying the user's browser.
