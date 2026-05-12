# Moonn Positioning Architecture — 2026-05-12

## Scope

This is a planning and governance artifact. It does not publish Tilda changes.

- Branch: `codex/moonn-seo-positioning-architecture`.
- Source live audit: `docs/moonn-final-seo-audit-2026-05-12.json`.
- Public-page rule: analyze open semantic pages only; closed, opaque, test, legal and transactional URLs are cleanup/hygiene, not positioning assets.
- User constraint: avoid visual Tilda/Chrome control while planning; use repository, HTTP checks and headless audits.

## Verdict On The Submitted Research

I agree with the core diagnosis. The site has strong brand/entity material, but its public sitemap currently spreads Tatyana Munn across too many equal-looking topics: private psychology, emotional intelligence, teen/exam products, events, gallery, older method pages and off-topic wellness pages. This weakens the site's primary purpose signal.

The stronger strategy is not to create more pages for every broad keyword. The stronger strategy is to make the homepage a brand/entity gateway and build three search lanes with pillar pages, supporting pages, internal links and clear safety boundaries.

## Current Live Evidence

- Live audit checked `151` URLs.
- `45` URLs are opaque/test/numeric and should be renamed, redirected or removed/noindexed.
- `105` URLs need SEO strengthening.
- `1` public psychology URL is blocked by robots and needs a technical fix.
- `92` pages have no detected H1; `16` have multiple H1; `33` duplicate descriptions.
- Homepage raw HTML has `5` H1 elements and mixes lecture headings, education, recommendations and Yandex services into the same semantic level.
- `/panicheskie_ataki` has `7` H1 elements and overpromising medical-adjacent text; it should not remain a core landing in its current form.
- `/psiholog` is cleaner conceptually but currently has no raw H1.
- `/speaker` is the clearest current EI/spiker page: one H1, no fringe/medical risk hits in the sampled text.

## Strategic Positioning

Primary entity:

> Татьяна Мунн — психолог МГУ и эксперт по эмоциональному интеллекту: консультации в Москве и онлайн, работа с тревогой, выгоранием, отношениями, подростками и экзаменационным стрессом; лекции и программы по эмоциональному интеллекту для людей и команд.

This should be the stable bio/entity wording across homepage, `/psiholog`, `/speaker`, `/otzivi`, schema, Yandex profile links, Timepad descriptions and future page templates.

## Search Lanes

### 1. Private Practice

Goal: convert adults who search for help with anxiety, burnout, relationships and emotional states.

Pillar: `/psiholog`.

Support pages to keep/merge/rewrite:

- `/trevozhnost`
- `/emotsionalnoe-vygoranie`
- `/otnosheniya-i-granitsy`
- `/samoocenka-i-uverennost`
- `/depressivnoe-sostoyanie`
- `/panicheskie_ataki` only after claim cleanup and one-H1 rebuild

Do not try to win the broad head term `психолог Москва` as the main bet. Use it as a local modifier, not as the positioning core.

### 2. Emotional Intelligence And Leadership

Goal: make Tatyana visible as an expert, speaker and educator in emotional intelligence, self-regulation and soft skills.

Pillars: `/speaker` and `/emotional-intelligence/`.

Support pages:

- `/articles/eq-dlya-rukovoditeley`
- `/emotional-intelligence/knowledge-base/*` after H1 fixes
- `/kurs-ei`
- `/events` and `/events_tp` as evidence, not as the main content hub

This is the most defensible non-brand SEO lane because it matches her public lectures, MSU/education proof, schema `knowsAbout`, and existing content cluster.

### 3. Teens, Exams And Family Support

Goal: own narrower high-intent pages around teen communication, exam anxiety and parent support.

Pillars: `/psypodgotovka1` or a future semantic slug `/psihologicheskaya-podgotovka-k-ekzamenam`, plus `/podrostkovyy-lager-psihologiya` for the seasonal product.

Support pages:

- `/uslugi_podrostki`
- `/article_gadget_addiction`
- `/vospitanie_article`
- future pages for `страх ЕГЭ`, `тревога перед экзаменом`, `подросток и гаджеты`, `как родителям поддержать подростка`

## Homepage Rule

The homepage should stop being a catalog of everything. It should become a concise brand/entity gateway:

1. One H1 with name + positioning.
2. Three route cards: consultations, emotional intelligence/speaker, teens/exams.
3. Proof layer: MSU, lectures, reviews, Yandex/B17/Timepad/YouTube links.
4. Current campaigns as compact banners below the strategic routes.
5. Gallery and other secondary products should be lower priority or moved out of the main SEO route.

## Pages To De-Emphasize Or Archive

These pages should not be equal homepage/SEO signals unless rewritten with clear evidence, psychological boundaries and a reason to exist:

- `/aromatherapy`
- `/microbiom`
- `/phytotherapy`
- `/salt`
- `/water`
- `/vacuum_cups`
- `/geshtalt`, `/kpt`, `/schematherapy`, `/psychoanalys` if they are only method labels and not strong unique service pages
- `/kartiny-tatiany-munn` as a public product page, not a psychology SEO lane

Recommended action: keep accessible where needed, but remove from homepage priority and sitemap/index unless each page is rebuilt as a safe, sourced, user-first article.

## Technical SEO Gates For Every Open Public Page

- Exactly one raw H1.
- Self-canonical for unique public pages.
- Unique title and description matched to one intent.
- Visible content must support the structured data.
- No internal SEO/debug wording in public text.
- No medical guarantees or promises of complete/fast cure.
- For medical-adjacent topics: add boundary text that psychological consultation is not emergency or medical care and that medication questions belong to physicians.
- Images: meaningful alt on hero/content images first.
- Pages not assigned to one of the three lanes must not remain in the main sitemap as active SEO targets.

## AIO / AI Search Rule

Do not create special `AI SEO` files as the main work. Google says AI features use the same fundamental SEO requirements and no special AI markup/files are needed. Yandex fast answers are generated automatically from indexed, well-structured, well-written pages. So the practical AI plan is: clean indexable pages, clear headings, strong authorship/entity proof, structured data that matches visible content, and concise answer blocks.

## Implementation Order

### Phase 1: Stop Dilution

1. Create a public URL decision register from this map.
2. Remove/redirect/noindex the `45` opaque/test URLs.
3. Fix robots block for `/psiholog-moskva-online` or decide to redirect it.
4. Move off-topic wellness pages out of the main SEO path.

### Phase 2: Rebuild Core Pages

1. Homepage: one-H1 brand gateway with three routes.
2. `/psiholog`: main private-practice pillar.
3. `/speaker`: EI/speaker pillar.
4. `/emotional-intelligence/`: content hub without unfinished blocks.
5. `/psypodgotovka1`: either keep alias but strengthen canonical/slug strategy, or redirect to a semantic slug after a migration plan.

### Phase 3: Cluster Content

Build 5-8 supporting pages per lane. Each support page must link up to its pillar and sideways only inside its cluster.

### Phase 4: External Entity Reinforcement

Align sameAs/profile facts across schema, Yandex Services, Timepad, B17/other profiles, YouTube and site bio. Use verified review summaries and source links, not fake aggregate-rating markup.

## Machine Map

- JSON: `docs/moonn-public-positioning-map-2026-05-12.json`
- CSV: `docs/moonn-public-positioning-map-2026-05-12.csv`

## Sources Checked

- Google Search Central, AI features and your website: https://developers.google.com/search/docs/appearance/ai-features?hl=en
- Google Search Central, helpful reliable people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central, URL structure: https://developers.google.com/search/docs/crawling-indexing/url-structure/?hl=en
- Google Search Central, review snippets: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Yandex Webmaster, fast answer: https://yandex.ru/support/webmaster/ru/search-appearance/fast

## Done Criteria For The Next Implementation Branch

- Public URL register updated after Tilda changes.
- Live raw HTML confirms one H1 on homepage and each rebuilt pillar.
- Sitemap no longer contains closed/opaque/test URLs.
- Homepage no longer gives equal weight to off-topic products and wellness pages.
- A fresh `scripts/moonn_final_seo_audit.py` run shows reduced duplicate descriptions, multiple H1 and opaque slug counts.
- Browser render verifies that the homepage is visually coherent after the SEO restructure.
