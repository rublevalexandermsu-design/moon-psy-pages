# Moonn RKN/Privacy Compliance Audit — 2026-05-08

## Scope

- Site: `https://moonn.ru/`
- Workstream: legal/privacy compliance, separate from SEO.
- Trigger: user raised RKN personal-data/cookie/form-policy risk and asked whether bot access can be limited.
- Method: live read-only checks, official/legal source review, no Tilda edits.

## Strategic Assessment

1. Platform value: high. Privacy compliance affects Moonn, MIIIIPS, Timepad funnels, paid products, reviews, forms, analytics and future AI modules.
2. Risk of obsolete solution: high. Personal-data rules and platform enforcement are changing; one static policy page is not enough.
3. Stronger architecture: create a compliance registry and recurring audit, not one-off text edits.
4. Reuse: the same compliance gate should be reused for MIIIIPS, institute events, paid lectures, reviews pages and future forms.
5. 3–12 month risk if ignored: fines, blocked analytics, invalid form consents, unsafe publication of employee/reviewer personal data, and inconsistent downstream documents.

## Verified Live Facts

- `https://moonn.ru/robots.txt` returns `200`.
- Standard policy URLs checked and currently return `404`:
  - `https://moonn.ru/privacy`
  - `https://moonn.ru/policy`
  - `https://moonn.ru/personal-data`
  - `https://moonn.ru/soglasie`
- The main page includes Yandex Metrika counter `96397286` with:
  - `clickmap:true`
  - `trackLinks:true`
  - `accurateTrackBounce:true`
  - `webvisor:true`
- The main page contains Tilda form code signals (`t-form`) but the checked main HTML did not show a visible default-unchecked consent checkbox marker.
- Google Analytics / gtag signals were not detected in the checked main HTML.
- Tilda page root includes `data-tilda-cookie="no"`, so the detected cookie-consent posture needs manual/Tilda-level verification.

## Official/Legal Source Baseline

- 152-FZ requires personal data processing to be lawful, tied to specific predefined legitimate purposes, and not excessive.
- 152-FZ Article 9 baseline: consent must be specific, informed and conscious; the operator bears the burden of proving consent or another legal basis.
- 152-FZ Article 22 baseline: operators generally notify Roskomnadzor before processing personal data unless a statutory exception applies.
- RKN regional operator guidance states that site owners collecting identifiable data are personal-data operators and should use the RKN personal-data portal for operator notifications.
- RKN personal-data portal provides a mechanism/template for consent to processing personal data permitted for distribution under Article 10.1.

## Current High-Risk Gaps

1. Missing public policy endpoints.
   - Risk: users and scanners cannot find a policy at standard URLs.
   - Required fix: publish canonical pages for privacy policy, personal-data processing consent, cookie/analytics notice and contact/request procedure.

2. Form consent gate likely incomplete.
   - Risk: Tilda forms may submit without a separate unchecked consent checkbox.
   - Required fix: audit every form block and add a required unchecked checkbox with links to policy and consent.

3. Yandex Metrika/Webvisor disclosure.
   - Risk: analytics, clickmap and Webvisor are active but cookie/analytics disclosure was not confirmed.
   - Required fix: add visible cookie/analytics notice and describe Yandex Metrika/Webvisor in policy.

4. Operator notification evidence unknown.
   - Risk: if no RKN operator notification exists or it does not match the site, the site remains exposed.
   - Required fix: check RKN operator registry/notification status for the actual legal operator, likely IP Kumskova or another named operator.

5. Published personal data of Tatiana/team/reviewers.
   - Risk: public names/photos/biographical facts must have a legal basis and, for third-party/reviewer content, separate publication/compliance gate.
   - Required fix: maintain publication-consent evidence and avoid publishing review screenshots/names/avatars without approval.

6. Duplicate analytics snippets.
   - Observation: main HTML showed repeated Yandex Metrika snippets in the head.
   - Required fix: verify whether this is Tilda duplication from global/page head code and reduce to one canonical counter if safe.

## Bot Access Strategy

Do not use bot blocking as a substitute for compliance. RKN or other official checks may use changing infrastructure and can still review a public site.

Safe bot-control layer:

- Keep search engines allowed for SEO: Yandex, Google, Bing where needed.
- Add `robots.txt` rules for non-essential AI/scraper bots only, for example:
  - `GPTBot`
  - `CCBot`
  - `ClaudeBot`
  - `PerplexityBot`
  - `Bytespider`
  - `Amazonbot`
- Add noindex only to real private/test/system pages, not public service/content pages.
- If Cloudflare/CDN becomes available, add rate-limits and bot-fight rules for aggressive scraping, but do not block legitimate search or official access.
- Do not rely on robots.txt for legal secrecy; it is advisory and does not remove public-data obligations.

## Recommended Implementation Packet

Phase 1 — canonical documents:

- `/privacy` — Политика обработки персональных данных.
- `/personal-data-consent` — Согласие на обработку персональных данных.
- `/cookies` — Уведомление об использовании cookies, Яндекс.Метрики, Webvisor/clickmap.
- `/data-subject-request` or section in policy — порядок запросов: доступ, уточнение, удаление, отзыв согласия.

Phase 2 — Tilda form hardening:

- Inventory all Tilda form blocks on 83 production pages.
- Add required unchecked checkbox under every form.
- Checkbox text must link to policy and consent pages.
- Verify form cannot submit without checkbox.

Phase 3 — RKN notification alignment:

- Confirm legal operator name, INN/OGRNIP, address, contact email.
- Check whether operator is already in RKN registry.
- If notification exists, align site policy with it.
- If not, prepare notification draft for legal review.

Phase 4 — analytics/cookie governance:

- Confirm active counters: Yandex Metrika `96397286`, any GA4/Google tools, Tilda analytics, Timepad, payment widgets.
- Remove duplicate Metrika injection if confirmed.
- Document each third-party processor/platform and storage/cross-border implications.

Phase 5 — recurring automation:

- Weekly compliance scan:
  - policy pages return 200;
  - form pages contain required consent checkbox;
  - analytics/cookie notice present;
  - robots.txt has no accidental SEO breakage;
  - no private/test pages in sitemap;
  - no unapproved personal-data screenshots/reviews;
  - report drift and required manual approvals.

## Current Blockers

- Need confirmed legal operator details for the policy and RKN notification.
- Need confirmation whether an RKN operator notification already exists.
- Need legal approval before publishing final policy/consent wording.
- Need Tilda UI/API-safe path for form-checkbox rollout.

