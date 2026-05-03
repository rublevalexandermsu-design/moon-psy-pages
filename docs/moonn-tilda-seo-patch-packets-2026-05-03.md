# Moonn Tilda SEO Patch Packets — 2026-05-03

Workstream: `moonn-live-seo-audit`  
Branch: `codex/moonn-seo-audit`  
Status: prepared, no live Tilda edits

## Boundary

This packet is ready to use as a Tilda SEO editing checklist. It does not change live Tilda pages by itself.

Do not use undocumented Tilda endpoints. Do not touch payments, products, private videos, review screenshots or personal data in this workstream.

## Global Entity

Use this identity consistently:

- Primary public name: `Татьяна Мунн`
- Legal/authority bridge: `Кумскова Татьяна Михайловна`
- Public formulation: `Татьяна Мунн (Кумскова Татьяна Михайловна), психолог МГУ`
- sameAs:
  - `https://moonn.ru/`
  - `https://moonn.timepad.ru/events/`
  - `https://miiiips.ru/author-tatyana-munn-kumskova.html`
  - `https://uslugi.yandex.ru/profile/TatyanaKumskovatatyanamunn-948629`
  - `https://istina.msu.ru/workers/816305440/`
  - `https://psyjournals.ru/authors/15337`

## Patch Packets

| URL | Title | Description | H1 | Schema |
| --- | --- | --- | --- | --- |
| `https://moonn.ru/` | `Татьяна Мунн — психолог МГУ в Москве и онлайн` | `Татьяна Мунн (Кумскова Татьяна Михайловна) — психолог МГУ, консультации в Москве и онлайн, эмоциональный интеллект, отношения, стресс и подростки.` | `Психолог МГУ Татьяна Мунн` | `Person`, `ProfessionalService`, `WebSite`, `BreadcrumbList` |
| `https://moonn.ru/events_tp` | `Лекции Татьяны Мунн по психологии и эмоциональному интеллекту` | `Расписание лекций Татьяны Мунн (Кумскова Татьяна Михайловна): отношения, эмоциональный интеллект, стресс, подростки и практическая психология.` | `Лекции по психологии Татьяны Мунн` | `ItemList`, `Event`, `Person`, `BreadcrumbList` |
| `https://moonn.ru/lectures1` | `Лекции по психологии от Татьяны Мунн, психолога МГУ` | `Архив и список лекций Татьяны Мунн: эмоциональный интеллект, отношения, подростки, стресс и практическая психология для взрослых.` | `Лекции Татьяны Мунн по психологии` | `ItemList`, `Event`, `Person`, `BreadcrumbList` |
| `https://moonn.ru/psiholog-moskva-online` | `Психолог МГУ Татьяна Мунн — консультации в Москве и онлайн` | `Консультации психолога МГУ Татьяны Мунн в Москве и онлайн: тревога, выгорание, отношения, эмоциональный интеллект и быстрые практические встречи.` | `Психолог МГУ в Москве и онлайн` | `ProfessionalService`, `Person`, `FAQPage`, `BreadcrumbList` |
| `https://moonn.ru/psiholog-konsultacii-moskva` | `Консультации психолога в Москве — Татьяна Мунн, МГУ` | `Индивидуальные и семейные консультации Татьяны Мунн в Москве и онлайн: отношения, стресс, подростки, эмоциональный интеллект и поддержка взрослых.` | `Консультации психолога Татьяны Мунн` | `ProfessionalService`, `Person`, `FAQPage`, `BreadcrumbList` |
| `https://moonn.ru/uslugi_depression` | `Депрессивное состояние — консультация психолога Татьяны Мунн` | `Помощь при депрессивном состоянии, стрессе и эмоциональном истощении: консультации Татьяны Мунн, психолога МГУ, в Москве и онлайн.` | `Депрессивное состояние: психологическая поддержка` | `ProfessionalService`, `Person`, `FAQPage`, `BreadcrumbList` |
| `https://moonn.ru/emotional-intelligence/articles/benefits-of-ei` | `Преимущества эмоционального интеллекта в жизни и работе` | `Как эмоциональный интеллект помогает снижать конфликты, улучшать отношения, продуктивность и устойчивость к выгоранию. Автор: Татьяна Мунн.` | `Преимущества эмоционального интеллекта` | `Article`, `Person`, `FAQPage`, `BreadcrumbList` |
| `https://moonn.ru/emotional-intelligence/knowledge-base/empathy` | `Эмпатия как навык эмоционального интеллекта — Татьяна Мунн` | `Что такое эмпатия, как её развивать и применять в отношениях, лидерстве и обучении. База знаний по эмоциональному интеллекту от Татьяны Мунн.` | `Эмпатия в эмоциональном интеллекте` | `Article`, `Person`, `FAQPage`, `BreadcrumbList` |
| `https://moonn.ru/emotional-intelligence/knowledge-base/nonviolent-communication` | `Ненасильственное общение: 4 шага NVC — Татьяна Мунн` | `Ненасильственное общение: наблюдение, чувства, потребности и просьбы. Примеры, упражнения и связь с эмоциональным интеллектом.` | `Ненасильственное общение и эмоциональный интеллект` | `Article`, `Person`, `FAQPage`, `BreadcrumbList` |

## H1 Rules

- Exactly one visible H1 per indexable page.
- Main page and `uslugi_depression` currently need H1 cleanup.
- `events_tp`, `lectures1` and emotional-intelligence article pages currently need one visible H1.

## JSON-LD Rules

- Use the canonical URL as the `@id` base.
- Connect `Person.sameAs` to Moonn, Timepad, MIIIIPS, Yandex Services, MSU Istina and PsyJournals.
- Do not add fake ratings or reviews until the reviews compliance gate is complete.
- Do not use medical treatment claims or `MedicalBusiness` unless separately reviewed.
- For lecture pages, generate `ItemList`/`Event` only from verified public lecture cards.

## Image/OG Rules

- Keep latin filenames for any new image assets.
- Use short visible captions; keep context in `alt`, `og:image`, image sitemap and schema.
- Suggested alt patterns are stored in the JSON packet.

## Next Step

Generate final JSON-LD blocks per page and apply through supported Tilda page head/code fields after the safe Tilda path is confirmed.
