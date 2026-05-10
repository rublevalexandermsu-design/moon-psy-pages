# Moonn Homepage Experiment Plan - 2026-05-10

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: SEO-safe landing experiment.
- Current canonical homepage: `https://moonn.ru/`.
- Primary candidate local HTML source: `C:\пайтонннн.. тесты\код сайт татьяна мунн\Коды для сайта татьяны.готовые\Окончательный.код.сай..html`.
- Previous candidate `Сайт.6..резервный.последний.копия.html` is demoted and should not be used as the publication base unless a later diff proves it contains something missing from the primary candidate.

## Checked Facts

Current live homepage:

- URL returns `200`.
- Title: `Татьяна Мунн — психолог МГУ в Москве и онлайн`.
- Meta description: `Татьяна Мунн (Кумскова Татьяна Михайловна) — психолог МГУ: консультации в Москве и онлайн, эмоциональный интеллект, отношения, стресс и подростки.`
- Canonical: `https://moonn.ru/`.
- Detected JSON-LD blocks: `2`.
- Detected H1 count: `5`, which remains a separate SEO cleanup item.

Primary candidate local page:

- File size: `113006` bytes.
- Last modified: `2026-02-15`.
- No detected `<title>`.
- No detected meta description.
- No detected canonical.
- No detected robots meta.
- Detected H1 count: `1`.
- Detected H2 count: `16`.
- Detected JSON-LD blocks: `1`.
- Contains fewer internal hints than the previous candidate, but still contains `Если Тильда позволяет - перенеси <title>, meta description, og:* в HEAD страницы.`
- Contains real Timepad links for the Park Gorky lecture carousel.
- Contains direct Telegram/WhatsApp/card/SBP booking and payment text that must be reconciled with the newer Timepad payment/booking strategy before publication.
- Does not include detected Yandex Metrica code, so experiment measurement must be added through the target Tilda page/project settings or a safe head layer.

## Route Decision

Do not replace the current homepage yet.

Recommended route:

1. Keep `https://moonn.ru/` unchanged as the canonical root page.
2. Turn the candidate page into a separate semantic landing on the same domain, not a new domain and not a duplicate homepage.
3. Use `Окончательный.код.сай..html` as the source candidate.
4. Choose one search intent for the new page, for example:
   - `https://moonn.ru/psiholog-tatiana-munn`
   - or another existing semantic Tilda page if it already maps to this intent.
5. Give the new landing a self-canonical only if its content is materially different from the homepage.
6. Add it to sitemap only after it passes content, legal/publication, SEO and visual QA gates.
7. Measure it as an experiment through Yandex Metrica / Google Search Console:
   - organic impressions;
   - clicks;
   - scroll depth;
   - consultation CTA clicks;
   - Timepad click-through;
   - WhatsApp/Telegram click-through only if those CTAs remain intentionally.

## Routes Rejected

Replacing the root homepage now:

- High risk because the current root page already ranks and has known canonical signals.
- A design/content change on `/` would mix UX experiment risk with SEO migration risk.

Creating a separate new domain:

- Weak for SEO because it splits authority and creates more maintenance.
- Worse for platform governance because Moonn already has too many Tilda pages and opaque/test URLs.

Publishing the primary local HTML as-is:

- Blocked because it has no title/description/canonical.
- Blocked because it still contains one internal setup instruction.
- Blocked until consultation CTAs are aligned with the current Timepad paid booking route.

## Required Cleanup Before Publication

- Remove internal/publication instructions from visible HTML.
- Add title, description, canonical and Open Graph metadata.
- Decide final URL slug before publishing.
- Reconcile CTAs with current Timepad consultation funnel:
  - primary: Timepad paid booking / consultation event;
  - secondary: reviews page;
  - optional: WhatsApp/Telegram only as contact/support channels, not as the main paid-booking bypass.
- Replace placeholder carousel captions with editorial captions or remove them.
- Add experiment measurement:
  - Yandex Metrica counter if not inherited by the Tilda project;
  - CTA click events for consultation, Timepad, reviews, Telegram and WhatsApp;
  - scroll-depth events if available through the current analytics setup.
- Add schema.org:
  - `Person`;
  - `WebPage`;
  - `ProfessionalService`;
  - optionally `FAQPage` if FAQ content is clean and public-ready.
- Run visual QA on desktop and mobile.
- Run public text leak scan for internal words:
  - `НАСТРОЙКА`;
  - `вставь реальные`;
  - `если Тильда`;
  - `резервный`;
  - `копия`;
  - `MVP`;
  - `технический`;
  - `TODO`.

## External SEO Basis

- Google treats a canonical URL as the representative URL from a duplicate set: `https://support.google.com/webmasters/answer/10347851`.
- Yandex recommends canonical/noindex handling for duplicate pages: `https://yandex.com/support/webmaster/en/yandex-indexing/about-doubles`.

## Next Practical Step

Create a cleaned experimental landing package from `Окончательный.код.сай..html` inside the repository, then decide whether to publish it into an existing semantic Tilda page or a new semantic alias.

The experiment should start as a same-domain semantic page, not as a replacement homepage.
