# Moonn Live SEO Metadata Audit — 2026-05-03

Workstream: `moonn-live-seo-audit`  
Branch: `codex/moonn-seo-audit`  
Mode: read-only audit, no Tilda edits

## Summary

- Checked URLs: 9
- HTTP `200`: 9
- Canonical present: 9
- `og:image` present: 9
- JSON-LD present: 1
- JSON-LD missing: 8
- Missing detected H1: 5
- Multiple detected H1: 3
- Short description: 1
- Overlong title: 2

## Main Findings

1. Most checked pages do not expose JSON-LD.
   Add page-specific schema: `Person`, `ProfessionalService`, `Event`, `ItemList`, `Article`, `FAQPage`, `BreadcrumbList`.

2. Several indexable pages have no detected H1:
   - `https://moonn.ru/events_tp`
   - `https://moonn.ru/lectures1`
   - `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei`
   - `https://moonn.ru/emotional-intelligence/knowledge-base/empathy`
   - `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication`

3. The main page and depression page have too many detected H1 elements:
   - `https://moonn.ru/` — 5
   - `https://moonn.ru/uslugi_depression` — 6

4. `https://moonn.ru/events_tp` has a weak description:
   `расписание лекций по психологии`

5. `https://moonn.ru/` and `https://moonn.ru/uslugi_depression` have overlong titles.

## URL Decisions

| URL | Status | JSON-LD | H1 Count | Action |
| --- | ---: | --- | ---: | --- |
| `https://moonn.ru/` | 200 | no | 5 | Shorten title, add `Person`/`ProfessionalService`, reduce to one H1 |
| `https://moonn.ru/events_tp` | 200 | no | 0 | Add one H1, rewrite description, add `ItemList`/`Event` schema |
| `https://moonn.ru/lectures1` | 200 | no | 0 | Add one H1, clean description, add lecture schema |
| `https://moonn.ru/psiholog-moskva-online` | 200 | yes | 1 | Use as implementation reference |
| `https://moonn.ru/psiholog-konsultacii-moskva` | 200 | no | 2 | Reduce to one H1, add `ProfessionalService` schema |
| `https://moonn.ru/uslugi_depression` | 200 | no | 6 | Shorten title, reduce H1 count, add `FAQPage` and service schema |
| `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei` | 200 | no | 0 | Add H1 and `Article`/`FAQPage`/`BreadcrumbList` |
| `https://moonn.ru/emotional-intelligence/knowledge-base/empathy` | 200 | no | 0 | Add H1 and `Article`/`FAQPage`/`BreadcrumbList` |
| `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication` | 200 | no | 0 | Add H1 and `Article`/`FAQPage`/`BreadcrumbList` |

## Next Safe Step

Prepare page-specific SEO patch packets for Tilda:

- title;
- description;
- one-H1 instruction;
- JSON-LD block;
- canonical confirmation;
- image alt/OG image note.

Do not apply live Tilda edits until the supported Tilda path and target pages are confirmed.
