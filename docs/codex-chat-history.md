# Codex Chat History

Canonical append-only chat history for `moon-psy-site`.

## 2026-05-01T12:07:00+03:00 — Tilda API sync and staging copy

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: connect Tilda API for `moonn.ru`, create a safe copy/staging version before changing the main site, open it in browser, and later audit SEO and analytics.
- Decisions:
  - Treat production Tilda project `Moonn.ru` as the protected source.
  - Store API keys only in local `.env`; keep them out of GitHub.
  - Use Tilda API for read-only local snapshots and audits.
  - Do not claim that API can create an editable Tilda project copy; official Tilda copy path goes through the cabinet UI.
  - For editable staging in Tilda, use UI duplication/move flow and account for the 100-new-pages-per-day limit.
- Created or changed files:
  - `.gitignore`
  - `scripts/tilda_sync_snapshot.py`
  - `docs/tilda-api-staging.md`
  - `docs/codex-chat-history.md`
- Local artifacts:
  - `.env`
  - `output/tilda-snapshot/project.json`
  - `output/tilda-snapshot/pages.json`
  - `output/tilda-snapshot/published-pages.json`
  - `output/tilda-snapshot/pages/*.html`
  - `output/tilda-snapshot/snapshot-manifest.json`
- Verified facts:
  - Tilda API returned project `Moonn.ru` with project id `8326812`.
  - Full local snapshot exported 131 published pages.
  - Local homepage opened at `http://127.0.0.1:8787/index.html`.
  - Browser console reported one error: `Unexpected token 'function'`.
- Initial SEO observations:
  - Homepage title length is 90 characters.
  - Homepage description length is 166 characters.
  - Homepage has 5 H1 headings, 0 H2 headings, 55 images without alt, and 74 scripts.
- Open questions:
  - Whether to create the editable Tilda staging project manually through cabinet access.
  - Whether to copy all pages or only the canonical production pages, because the current project includes drafts, tests, and archive-style pages.
  - Which analytics source is active for traffic and click data: Yandex Metrica, Google Analytics, Tilda statistics, or another tool.
- Risks:
  - API keys were exposed in chat/screenshot and should be regenerated after the workflow is stable.
  - A direct copy of every page may carry old tests, duplicate pages, and SEO debt into the staging project.

## 2026-05-01T12:22:00+03:00 — Tilda editable staging project created

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: use the corrected Tilda password, enter the cabinet, and set up a Tilda-side staging project so future changes can be tested in Tilda before production.
- Decisions:
  - Use Playwright MCP as fallback because Browser Use backend `iab` still fails with missing `codex app-server`.
  - Create a separate Tilda project instead of changing `Moonn.ru`.
  - Name the staging project `Moonn Staging`.
  - Do not bulk-copy pages yet; require a copy scope because the source project has many drafts/tests and Tilda has a new-page limit.
- Created or changed files:
  - `docs/tilda-api-staging.md`
  - `docs/codex-chat-history.md`
  - local `.env` updated with `TILDA_STAGING_PROJECT_ID`.
- Verified facts:
  - Login to Tilda succeeded.
  - Production project `Moonn.ru` is visible in the account.
  - Business plan allows 5 sites; 3 were used before creating staging.
  - Created Tilda project `Moonn Staging`, project id `25075076`.
- Open questions:
  - Copy scope: homepage pilot, canonical public pages, or full page copy in batches.
  - Whether to connect a temporary public staging domain before or after copying the first page.
- Risks:
  - Bulk copy can pollute staging with old test pages and may hit Tilda's daily page creation limit.
  - Production safety rule: duplicate first, move only duplicates, never move original pages.

## 2026-05-01T12:28:00+03:00 — Browser Use repair

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: repair Browser Use after Codex restart and Browser MCP extension setup.
- Symptom:
  - Browser Use `iab` could create a session and tab, and could open local URLs.
  - External navigation failed with `failed to start codex app-server: Системе не удается найти указанный путь. (os error 3)`.
- Root cause:
  - `node_repl.exe` reported its runtime path as `C:\Users\yanta\AppData\Local\OpenAI\Codex\bin`, but that directory did not exist.
  - Browser Use permission checks for external URLs need `codex.exe app-server`; node_repl could not locate `codex.exe` beside its reported runtime path.
- Fix:
  - Created `C:\Users\yanta\AppData\Local\OpenAI\Codex\bin`.
  - Copied installed `codex.exe` from the Codex WindowsApps resources directory into that local bin directory.
- Verification:
  - Browser Use opened `https://example.com/` through the in-app browser.
  - Returned title `Example Domain` and URL `https://example.com/`.
- Follow-up rule:
  - If Browser Use can open localhost but fails on external URLs with app-server path errors, check whether local `C:\Users\yanta\AppData\Local\OpenAI\Codex\bin\codex.exe` exists and refresh it from the installed Codex resources directory after app updates.

## 2026-05-01T12:47:00+03:00 — Tilda staging homepage copy published

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: use repaired Browser Use so the user can see the Tilda cabinet actions, create an editable staging copy, publish it on a temporary address, and keep production `Moonn.ru` untouched.
- Actions:
  - Logged into Tilda through Browser Use.
  - Opened production project `Moonn.ru`, project id `8326812`.
  - Located production homepage `pageid=42678538`.
  - Duplicated the homepage inside production and received new page id `138660066`.
  - Moved only the duplicate, not the original page, into staging project `Moonn Staging`, project id `25075076`.
  - Renamed the staging page to remove `Copy of`.
  - Enabled `noindex` and `nofollow` for the staging page before publication.
  - Assigned the staging page as the project homepage in site settings.
  - Published all pages in the staging project.
- Verified facts:
  - Staging project contains one copied page.
  - Temporary staging URL is `https://carry-pacific-flatfish.tilda.ws/`.
  - Browser Use opened the published staging root URL successfully.
  - Production `Moonn.ru` was not edited directly; only a duplicate page was created and moved.
- Incident:
  - Symptom: first publication opened the copied page at `/page138660066.html`, while the staging root showed a Tilda stub/404.
  - Root cause: the Tilda project did not have a homepage selected; clearing the page URL was not sufficient and briefly made the root return 404.
  - Resolution: set `pageid=138660066` as the project homepage in site settings, saved settings, republished, and verified the root URL.
  - Follow-up rule: after moving pages into a Tilda staging project, always set the staging homepage in site settings and verify the root URL, not only the direct page URL.
- Open questions:
  - Which additional canonical production pages should be copied next.
  - Whether internal links in staging should continue pointing to production pages or be rewired to copied staging pages as those pages are added.
  - Which analytics source should be treated as authoritative for traffic/click data.

## 2026-05-01T13:00:00+03:00 — Tilda staging core pages copied

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue the Tilda staging setup through Browser Use and carry the work as far as practical.
- Actions:
  - Copied five core production pages into `Moonn Staging`:
    - `135430346` -> `138661976`, alias `psiholog-konsultacii-moskva`.
    - `135442186` -> `138662086`, alias `vystupleniya-lekcii-treningi-psiholog-tatiana-moonn`.
    - `135444166` -> `138662216`, alias `platnye-treningi-seminary-programmy-tatiana-moonn`.
    - `135534246` -> `138662406`, alias `baza-znaniy-emocionalnyy-intellekt-psihologiya`.
    - `66814657` -> `138662576`, alias `events_tp`.
  - Removed `Copy of` from the copied staging page titles.
  - Restored the public aliases for the copied staging pages.
  - Republished the staging project.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/`
  - `https://carry-pacific-flatfish.tilda.ws/psiholog-konsultacii-moskva`
  - `https://carry-pacific-flatfish.tilda.ws/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn`
  - `https://carry-pacific-flatfish.tilda.ws/platnye-treningi-seminary-programmy-tatiana-moonn`
  - `https://carry-pacific-flatfish.tilda.ws/baza-znaniy-emocionalnyy-intellekt-psihologiya`
  - `https://carry-pacific-flatfish.tilda.ws/events_tp`
- Incident:
  - Symptom: a long Browser Use copy loop exceeded the tool timeout after several page moves.
  - Root cause: copying multiple pages through the Tilda UI is slow and each duplicate/move step waits on live cabinet navigation.
  - Resolution: verified the staging state after timeout, confirmed all five pages were actually copied, then normalized titles and aliases in a separate shorter operation.
  - Follow-up rule: for Tilda UI copy work, use smaller batches and verify staging project state after every timeout instead of restarting or duplicating pages again.
- Open questions:
  - Internal links inside copied Tilda blocks still include some absolute `moonn.ru` URLs. These require either manual block-level link rewiring or a reliable staging-only site code injection once the Tilda code editor input path is stable.
  - Need decide whether to copy news/event child pages next or keep staging focused on the conversion/navigation core first.

## 2026-05-01T13:13:00+03:00 — Tilda staging copy expanded and mapped

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue toward an identical Tilda staging copy so future edits can be made and tested in Tilda before production transfer.
- Strategic decision:
  - Full identity requires copying all published pages and tracking every `source_page_id -> staging_page_id` pair.
  - Tilda does not expose a visible full-project duplicate action in `Moonn.ru` site settings; only transfer, delete, and unpublish were visible.
  - Continue via page-copy batches, because Tilda has a daily new-page limit and the production project has 131 published pages.
- Actions:
  - Enabled site-level noindex for `Moonn Staging`.
  - Added a machine-readable staging map at `registry/tilda/moonn-staging-page-map.json`.
  - Copied and verified three more pages:
    - `87231366` -> `138664896`, alias `speaker`.
    - `53668815` -> `138665336`, alias `events`.
    - `68295899` -> `138665516`, alias `lectures1`.
  - Republished staging after the new pages were copied.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/speaker`
  - `https://carry-pacific-flatfish.tilda.ws/events`
  - `https://carry-pacific-flatfish.tilda.ws/lectures1`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 9.
  - Pending staging pages: 122.
- Incident:
  - Symptom: copying a 3-page batch timed out before the tool returned.
  - Root cause: Tilda UI duplicate/move/rename operations are slow enough that multi-page batches can exceed the Browser Use tool timeout.
  - Resolution: verified actual staging state, found that only `speaker` completed, then copied `events` and `lectures1` one page at a time.
  - Follow-up rule: use one-page copy operations for Tilda UI work unless a faster authenticated API route is identified and safely validated.
- Open questions:
  - Whether to continue copying all 122 remaining pages over multiple batches/days, or first prioritize pages linked from navigation, forms, and conversion paths.
  - Whether to solve internal absolute `moonn.ru` links by block-level editing or by a reliable staging-only code injection path.

## 2026-05-01T13:25:00+03:00 — Tilda priority pages for EI and courses copied

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: prioritize pages related to lectures, courses, paid products, videos, and future large site branches.
- Site strategy recorded:
  - Homepage is the hub.
  - Four core branches: personal consultations; speaking/lectures/events; paid products/courses/masterclasses; knowledge base/expertise/emotional intelligence/search pages.
  - Staging should prioritize these branches before low-value archive or test pages.
- Actions:
  - Copied and normalized five high-priority pages:
    - `90977486` -> `138667076`, alias `emotional-intelligence/`.
    - `91652626` -> `138667176`, alias `emotional-intelligence/knowledge-base`.
    - `91871866` -> `138667346`, alias `emotional-intelligence/articles`.
    - `124264896` -> `138667516`, alias `kurs-ei`.
    - `124963886` -> `138667746`, alias `programmakursa`.
  - Republished the staging project.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles`
  - `https://carry-pacific-flatfish.tilda.ws/kurs-ei`
  - `https://carry-pacific-flatfish.tilda.ws/programmakursa`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 14.
  - Pending staging pages: 117.
- Follow-up priority:
  - Next copy candidates: individual EI knowledge-base pages, individual EI article pages, `st1`, `st2`, `seminar555`, masterclass/seminar pages, and key search pages that support paid products or expertise.

## 2026-05-01T13:32:00+03:00 — Tilda EI article pages copied

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the pages recommended by the staging strategy, especially lectures, courses, paid products, videos, and knowledge/expertise pages.
- Actions:
  - Copied and normalized four priority emotional-intelligence article pages:
    - `90782146` -> `138668556`, alias `emotional-intelligence/articles/what-is-emotional-intelligence`.
    - `90952996` -> `138668766`, alias `emotional-intelligence/articles/emotional-intelligence-skills`.
    - `91163626` -> `138668916`, alias `emotional-intelligence/articles/why-ei-matters`.
    - `91171146` -> `138669216`, alias `emotional-intelligence/articles/benefits-of-ei`.
  - Republished the staging project.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/what-is-emotional-intelligence`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/emotional-intelligence-skills`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/why-ei-matters`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/benefits-of-ei`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 18.
  - Pending staging pages: 113.
- Follow-up priority:
  - Continue with EI knowledge-base child pages and paid-product pages (`st1`, `st2`, `seminar555`, masterclass/seminar pages) before broad article/archive copying.


## 2026-05-01T14:05:00+03:00 — Tilda EI knowledge-base core pages copied

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the priority staging pages for lectures, courses, paid products, and knowledge/expertise pages.
- Strategic assessment:
  - Platform value: high, because staging becomes an editable Tilda mirror for the EI knowledge branch.
  - Obsolescence risk: medium if copying remains purely manual; the registry keeps state until a safer automation route is built.
  - Stronger architecture: keep canonical page map and batch verification, then later turn this into a repeatable Tilda sync workflow.
  - Reuse: same copy-map-verify pattern applies to courses, grants, event pages, and future platform sites.
  - 3-12 month risk if skipped: staging diverges from production and page edits become unreliable when moved back to the main Moonn site.
- Actions:
  - Copied and normalized four core EI knowledge-base pages:
    - `91652966` -> `138670456`, alias `emotional-intelligence/knowledge-base/emotional-intelligence`.
    - `91665726` -> `138670576`, alias `emotional-intelligence/knowledge-base/self-awareness`.
    - `91670976` -> `138670746`, alias `emotional-intelligence/knowledge-base/self-regulation`.
    - `91686486` -> `138670916`, alias `emotional-intelligence/knowledge-base/empathy`.
  - Published/verified the staging pages through the Browser Use visible browser flow.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/emotional-intelligence`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/self-awareness`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/self-regulation`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/empathy`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 22.
  - Pending staging pages: 109.
- Incident / process note:
  - Symptom: clicking the project-level publish control caused the Browser Use bridge to time out once.
  - Root cause: Tilda publish UI can hang the automation bridge even when the page state has already changed.
  - Resolution: reconnected to the visible browser tab and verified the live public URLs directly.
  - Follow-up rule: after any Tilda publish/control timeout, verify live URLs before retrying or reporting failure.
- Follow-up priority:
  - Continue copying the remaining EI knowledge-base skill pages (`emotional-literacy`, `social-intelligence`, `intrinsic-motivation`, `burnout`, `nonviolent-communication`) and then paid-product/seminar pages.


## 2026-05-01T14:32:00+03:00 — Remaining EI knowledge-base skill pages copied

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue the same priority copying flow for the EI knowledge-base pages.
- Strategic assessment:
  - Platform value: high, because the EI knowledge-base branch now has the main skill/competency pages available for safe Tilda-side edits.
  - Obsolescence risk: medium while publication depends on UI automation; reduced by keeping exact source-to-staging page IDs in the registry.
  - Stronger architecture: continue toward a canonical Tilda staging sync workflow with copy map, publication step, and live URL verification.
  - Reuse: the same flow applies to paid products, event pages, course pages, and future staging projects.
  - 3-12 month risk if skipped: staging remains incomplete and future edits may be tested on a non-identical branch.
- Actions:
  - Copied and normalized five EI knowledge-base pages:
    - `91692166` -> `138672296`, alias `emotional-intelligence/knowledge-base/emotional-literacy`.
    - `91696586` -> `138672476`, alias `emotional-intelligence/knowledge-base/social-intelligence`.
    - `91701376` -> `138672636`, alias `emotional-intelligence/knowledge-base/intrinsic-motivation`.
    - `91715996` -> `138672816`, alias `emotional-intelligence/knowledge-base/burnout`.
    - `91720476` -> `138672976`, alias `emotional-intelligence/knowledge-base/nonviolent-communication`.
  - Published all pages in the staging project and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/emotional-literacy`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/social-intelligence`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/intrinsic-motivation`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/burnout`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/knowledge-base/nonviolent-communication`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 27.
  - Pending staging pages: 104.
- Incident / process note:
  - Symptom: after copying, four of five pages initially returned 404 on their staging aliases.
  - Root cause: page duplication/move succeeded, but Tilda had not published all copied pages until the project-level publish confirmation was explicitly completed.
  - Resolution: opened the project-level `Опубликовать все страницы` control, confirmed `Да`, then verified each public URL.
  - Follow-up rule: copied Tilda pages are not complete until their staging aliases return a non-404 live page with the expected title.
- Follow-up priority:
  - Move next to paid-product/course/seminar pages (`st1`, `st2`, `seminar555`, masterclass/seminar pages), then remaining high-value search and expertise pages.


## 2026-05-01T14:40:00+03:00 — Tilda staging copy selection rule updated

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: for future copy runs, copy only source pages that are available/published; do not copy inaccessible or unpublished test pages from Tatiana's original Tilda project.
- Strategic assessment:
  - Platform value: high, because staging should mirror the real public site, not internal experiments.
  - Obsolescence risk: low; the rule is based on current production visibility and can be verified before each batch.
  - Stronger architecture: source-page eligibility must be an explicit gate before duplication: published/accessibly live in production -> copy candidate; unpublished/inaccessible/test -> skip.
  - Reuse: the same eligibility gate should be used for courses, events, articles, grants, and future Tilda staging projects.
  - 3-12 month risk if ignored: staging becomes polluted with old test pages, making future edits, navigation checks, SEO review, and migration back to production less reliable.
- Decision:
  - Canonical copy rule: only duplicate production pages that are published and accessible in the original Moonn project.
  - Do not copy pages that are not in access, are unpublished, or are known test/draft pages from Tatiana's original project.
  - Before each batch, check source `published` status and, when needed, source live URL accessibility.
- Follow-up implementation note:
  - Next batches should filter pending pages by `published`/live availability before opening the Tilda UI.
  - The registry can keep skipped pages as non-copy candidates instead of treating them as missing staging work.


## 2026-05-01T15:05:00+03:00 — Tilda paid/course pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying priority pages, using the new rule to copy only source pages that are published and accessible.
- Strategic assessment:
  - Platform value: high, because paid/course pages are part of the conversion branch that must be safely editable in staging.
  - Obsolescence risk: medium while the source pages contain date-specific offers; staging copy still preserves the public production baseline before edits.
  - Stronger architecture: use the eligibility gate first (`published` + live source URL 200), then duplicate/move/publish/verify.
  - Reuse: this paid-product copy flow should become the standard for future product, course, event, and grant landing pages.
  - 3-12 month risk if skipped: product edits may be tested on incomplete pages or accidentally applied to production without a safe mirror.
- Eligibility check:
  - `https://moonn.ru/st2` returned `200`.
  - `https://moonn.ru/st1` returned `200`.
  - `https://moonn.ru/seminar555` returned `200`.
  - Pages with empty alias or obvious test wording were not copied in this batch.
- Actions:
  - Copied and normalized three paid/course pages:
    - `98329166` -> `138676856`, alias `st2`.
    - `69732653` -> `138676976`, alias `st1`.
    - `57927493` -> `138677186`, alias `seminar555`.
  - Published all pages in `Moonn Staging` and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/st2`
  - `https://carry-pacific-flatfish.tilda.ws/st1`
  - `https://carry-pacific-flatfish.tilda.ws/seminar555`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 30.
  - Pending staging pages: 101.
- Follow-up priority:
  - Continue with other published/accessibly live paid-product, consultation, event, and high-value SEO pages.
  - Keep skipping inaccessible, unpublished, empty-alias/test-looking pages unless the user explicitly confirms they are part of the public copy scope.


## 2026-05-01T15:22:00+03:00 — Tilda consultation and trust pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/accessibly live pages into the Tilda staging project.
- Strategic assessment:
  - Platform value: high, because consultation, review, and recommendation pages support the main conversion path.
  - Obsolescence risk: low for trust pages, medium for service landing pages if offers/contact blocks change later.
  - Stronger architecture: keep building staging around real public navigation and conversion branches before lower-value archive pages.
  - Reuse: the eligibility gate and copy/publish/verify pattern remains the standard for future batches.
  - 3-12 month risk if skipped: staging would lack key trust and consultation pages, making future edits to the public funnel harder to validate safely.
- Eligibility check:
  - `https://moonn.ru/recomend` returned `200`.
  - `https://moonn.ru/otzivi` returned `200`.
  - `https://moonn.ru/psiholog_moskva` returned `200`.
  - `https://moonn.ru/psiholog` returned `200`.
- Actions:
  - Copied and normalized four consultation/trust pages:
    - `62977405` -> `138677856`, alias `recomend`.
    - `81167556` -> `138677976`, alias `otzivi`.
    - `62119659` -> `138678166`, alias `psiholog_moskva`.
    - `114846506` -> `138678336`, alias `psiholog`.
  - Published all pages in `Moonn Staging` and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/recomend`
  - `https://carry-pacific-flatfish.tilda.ws/otzivi`
  - `https://carry-pacific-flatfish.tilda.ws/psiholog_moskva`
  - `https://carry-pacific-flatfish.tilda.ws/psiholog`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 34.
  - Pending staging pages: 97.
- Follow-up priority:
  - Continue with published/accessibly live consultation service pages (`semeyniy_psiholog`, `psy4psy`, `selfharm`, `psypodgotovka1`, `panicheskie_ataki`) and/or key public events/news pages.


## 2026-05-01T15:37:00+03:00 — Tilda consultation service pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/accessibly live pages into the Tilda staging project.
- Strategic assessment:
  - Platform value: high, because these consultation service pages are practical conversion and SEO entry points.
  - Obsolescence risk: medium, because service promises and dates/offers may need future editorial review; staging preserves the production baseline for safe edits.
  - Stronger architecture: keep copying public service branches in batches with source-live eligibility, then verify staging live URLs before marking complete.
  - Reuse: the same flow is now a stable Tilda page-copy workflow for service, event, product, and knowledge pages.
  - 3-12 month risk if skipped: service pages remain outside staging, so later improvements could be tested on an incomplete mirror.
- Eligibility check:
  - `https://moonn.ru/semeyniy_psiholog` returned `200`.
  - `https://moonn.ru/psy4psy` returned `200`.
  - `https://moonn.ru/selfharm` returned `200`.
  - `https://moonn.ru/psypodgotovka1` returned `200`.
  - `https://moonn.ru/panicheskie_ataki` returned `200`.
- Actions:
  - Copied and normalized five consultation service pages:
    - `62920697` -> `138679266`, alias `semeyniy_psiholog`.
    - `62908693` -> `138679376`, alias `psy4psy`.
    - `62890623` -> `138679646`, alias `selfharm`.
    - `62652841` -> `138679846`, alias `psypodgotovka1`.
    - `62126761` -> `138680006`, alias `panicheskie_ataki`.
  - Published all pages in `Moonn Staging` and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/semeyniy_psiholog`
  - `https://carry-pacific-flatfish.tilda.ws/psy4psy`
  - `https://carry-pacific-flatfish.tilda.ws/selfharm`
  - `https://carry-pacific-flatfish.tilda.ws/psypodgotovka1`
  - `https://carry-pacific-flatfish.tilda.ws/panicheskie_ataki`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 39.
  - Pending staging pages: 92.
- Follow-up priority:
  - Continue with the remaining published consultation/service pages (`phytotherapy`, `microbiom`, `aromatherapy`, `salt`, `vacuum_cups`, `water`) or public event/news pages, skipping test-looking pages unless explicitly requested.


## 2026-05-01T15:55:00+03:00 — Tilda wellness/service pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/accessibly live pages into the Tilda staging project.
- Strategic assessment:
  - Platform value: medium-high, because these wellness/service SEO pages expand the public consultation and content funnel in staging.
  - Obsolescence risk: medium, because health-adjacent topics may need later editorial/legal review before major public changes.
  - Stronger architecture: keep these pages as source-identical staging copies first, then improve content through a separate reviewed workflow.
  - Reuse: the same source-live gate and live staging verification applies to the remaining service and article pages.
  - 3-12 month risk if skipped: future SEO/content edits would happen against an incomplete staging mirror.
- Eligibility check:
  - `https://moonn.ru/phytotherapy` returned `200`.
  - `https://moonn.ru/microbiom` returned `200`.
  - `https://moonn.ru/aromatherapy` returned `200`.
  - `https://moonn.ru/salt` returned `200`.
  - `https://moonn.ru/vacuum_cups` returned `200`.
  - `https://moonn.ru/water` returned `200`.
- Actions:
  - Copied and normalized six wellness/service pages:
    - `62462299` -> `138680626`, alias `phytotherapy`.
    - `62477227` -> `138680856`, alias `microbiom`.
    - `62470081` -> `138680976`, alias `aromatherapy`.
    - `63131581` -> `138681236`, alias `salt`.
    - `63138325` -> `138681366`, alias `vacuum_cups`.
    - `63552425` -> `138681466`, alias `water`.
  - Published all pages in `Moonn Staging` and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/phytotherapy`
  - `https://carry-pacific-flatfish.tilda.ws/microbiom`
  - `https://carry-pacific-flatfish.tilda.ws/aromatherapy`
  - `https://carry-pacific-flatfish.tilda.ws/salt`
  - `https://carry-pacific-flatfish.tilda.ws/vacuum_cups`
  - `https://carry-pacific-flatfish.tilda.ws/water`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 45.
  - Pending staging pages: 86.
- Follow-up priority:
  - Continue with published psychotherapy/service method pages (`kpt`, `psychoanalys`, `geshtalt`, `schematherapy`, `uslugi_*`) or high-value event/news pages, still skipping test-looking pages unless explicitly requested.


## 2026-05-01T16:12:00+03:00 — Tilda psychotherapy method pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying published/live pages from the original Moonn project into staging.
- Strategic assessment:
  - Platform value: high, because these method/service pages support the professional expertise and consultation funnel.
  - Obsolescence risk: medium, because psychology-method pages may later need editorial and legal/compliance review before public changes.
  - Stronger architecture: source-live eligibility -> duplicate -> move -> publish staging -> verify live URL remains the canonical copy workflow.
  - Reuse: the same process applies to the remaining `uslugi_*` service pages and public events/news pages.
  - 3-12 month risk if skipped: staging lacks core expertise pages, so future SEO/service changes cannot be tested against a complete mirror.
- Eligibility check:
  - `https://moonn.ru/kpt` returned `200`.
  - `https://moonn.ru/psychoanalys` returned `200`.
  - `https://moonn.ru/geshtalt` returned `200`.
  - `https://moonn.ru/schematherapy` returned `200`.
  - `https://moonn.ru/uslugi_fin_blocks` returned `200`.
- Actions:
  - Copied and normalized five method/service pages:
    - `63403669` -> `138682206`, alias `kpt`.
    - `63398035` -> `138682476`, alias `psychoanalys`.
    - `63388057` -> `138682696`, alias `geshtalt`.
    - `63409841` -> `138682896`, alias `schematherapy`.
    - `63711321` -> `138683016`, alias `uslugi_fin_blocks`.
  - Published all pages in `Moonn Staging` and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/kpt`
  - `https://carry-pacific-flatfish.tilda.ws/psychoanalys`
  - `https://carry-pacific-flatfish.tilda.ws/geshtalt`
  - `https://carry-pacific-flatfish.tilda.ws/schematherapy`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_fin_blocks`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 50.
  - Pending staging pages: 81.
- Follow-up priority:
  - Continue with remaining published `uslugi_*` service pages and public EI/event/news pages, skipping test-looking pages unless explicitly requested.


## 2026-05-01T16:30:00+03:00 — Tilda uslugi service pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/live service pages from the original Moonn project into staging.
- Strategic assessment:
  - Platform value: high, because these consultation/service pages are part of the future editable staging mirror for commercial and SEO workflows.
  - Obsolescence risk: medium, because health-adjacent service pages should later pass editorial and legal/publication review before major text changes.
  - Stronger architecture: keep the staging mirror source-identical first, then improve pages through a separate reviewed content workflow.
  - Reuse: the same live-source gate, Tilda duplicate/move flow, staging publish, and public URL verification applies to all remaining `uslugi_*` pages.
  - 3-12 month risk if skipped: future changes could be tested against an incomplete copy and then behave differently on production.
- Eligibility check:
  - `https://moonn.ru/uslugi_podrostki` returned `200`.
  - `https://moonn.ru/uslugi_konflikti_na_rabote` returned `200`.
  - `https://moonn.ru/uslugi_otnosheniya_v_kollektive` returned `200`.
  - `https://moonn.ru/uslugi_depression` returned `200`.
  - `https://moonn.ru/uslugi_obida_na_roditelei` returned `200`.
- Actions:
  - Copied and normalized five service pages:
    - `63713227` -> `138683686`, alias `uslugi_podrostki`.
    - `63716871` -> `138683936`, alias `uslugi_konflikti_na_rabote`.
    - `63718371` -> `138684096`, alias `uslugi_otnosheniya_v_kollektive`.
    - `63747017` -> `138684276`, alias `uslugi_depression`.
    - `63749211` -> `138684406`, alias `uslugi_obida_na_roditelei`.
  - Published the `Moonn Staging` project and verified the new public URLs through Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_podrostki`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_konflikti_na_rabote`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_otnosheniya_v_kollektive`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_depression`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_obida_na_roditelei`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 55.
  - Pending staging pages: 76.
- Follow-up priority:
  - Continue with remaining published `uslugi_*` pages: `uslugi_procrastination`, `uslugi_sohranit_brak`, `uslugi_razvod`, `uslugi_lubovnaya_zavisimost`, `uslugi_gtr`, `uslugi_aerofobia`, then public EI/event/news pages.


## 2026-05-01T16:58:00+03:00 — Tilda remaining uslugi pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/live service pages from the original Moonn project into staging.
- Strategic assessment:
  - Platform value: high, because this completes the currently visible `uslugi_*` service batch in the staging mirror.
  - Obsolescence risk: medium, because service pages should later be improved through a content/compliance workflow, not edited ad hoc in production.
  - Stronger architecture: the copy workflow now includes a stricter publish-completion gate before live URL checks.
  - Reuse: the same gate applies to all future Tilda page batches and reduces false 404 incidents.
  - 3-12 month risk if skipped: staging would lag behind production on high-intent consultation pages and future edits could be tested against an incomplete mirror.
- Eligibility check:
  - `https://moonn.ru/uslugi_procrastination` returned `200`.
  - `https://moonn.ru/uslugi_sohranit_brak` returned `200`.
  - `https://moonn.ru/uslugi_razvod` returned `200`.
  - `https://moonn.ru/uslugi_lubovnaya_zavisimost` returned `200`.
  - `https://moonn.ru/uslugi_gtr` returned `200`.
  - `https://moonn.ru/uslugi_aerofobia` returned `200`.
- Actions:
  - Copied and normalized six service pages:
    - `63750667` -> `138685516`, alias `uslugi_procrastination`.
    - `63752263` -> `138685686`, alias `uslugi_sohranit_brak`.
    - `63755367` -> `138685886`, alias `uslugi_razvod`.
    - `63757347` -> `138686066`, alias `uslugi_lubovnaya_zavisimost`.
    - `63758713` -> `138686216`, alias `uslugi_gtr`.
    - `63836583` -> `138686506`, alias `uslugi_aerofobia`.
  - Published the `Moonn Staging` project and waited for Tilda's explicit `Все страницы опубликованы успешно` message.
  - Verified the new public URLs through Browser Use after the publish-completion gate.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_procrastination`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_sohranit_brak`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_razvod`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_lubovnaya_zavisimost`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_gtr`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_aerofobia`
- Incident note:
  - Symptom: initial live checks returned intermittent `404`/`Tilda` titles for the new pages.
  - Root cause: verification was started before Tilda completed the project publish job.
  - Solution: wait for the explicit Tilda success text `Все страницы опубликованы успешно` before marking pages verified.
  - Follow-up rule: every future Tilda batch must include a publish-completion gate, not just a fixed timeout after clicking publish.
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 61.
  - Pending staging pages: 70.
- Follow-up priority:
  - Continue with published article, EI knowledge-base, event/news, and legal/service pages; keep skipping unpublished/test-looking pages unless explicitly requested.


## 2026-05-01T17:25:00+03:00 — Tilda article and program pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/live pages from the original Moonn project into staging.
- Strategic assessment:
  - Platform value: high, because this expands the staging mirror beyond service pages into articles and program/education pages.
  - Obsolescence risk: medium, because article pages can later need SEO, legal/publication, and editorial review before changes are transferred to production.
  - Stronger architecture: keep copying source-identical pages first, then run improvement batches through a separate content QA workflow.
  - Reuse: the same source-live gate, duplicate/move flow, publish gate, Browser Use verification, and registry update now covers service and article pages.
  - 3-12 month risk if skipped: content and SEO improvements would be tested against an incomplete staging site, increasing transfer risk.
- Eligibility check:
  - `https://moonn.ru/psihology` returned `200`.
  - `https://moonn.ru/shppp333` returned `200`.
  - `https://moonn.ru/vospitanie_article` returned `200`.
  - `https://moonn.ru/semeynie_konflikti_article` returned `200`.
  - `https://moonn.ru/vigoranie_article` returned `200`.
  - `https://moonn.ru/article_diary_of_emotions` returned `200`.
- Actions:
  - Copied and normalized six pages:
    - `44682379` -> `138690346`, alias `psihology`.
    - `43765245` -> `138690486`, alias `shppp333`.
    - `62923037` -> `138690686`, alias `vospitanie_article`.
    - `62923441` -> `138690986`, alias `semeynie_konflikti_article`.
    - `62988415` -> `138691116`, alias `vigoranie_article`.
    - `62966623` -> `138691296`, alias `article_diary_of_emotions`.
  - Published the `Moonn Staging` project and verified the public URLs through Browser Use and direct HTTP checks.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/psihology`
  - `https://carry-pacific-flatfish.tilda.ws/shppp333`
  - `https://carry-pacific-flatfish.tilda.ws/vospitanie_article`
  - `https://carry-pacific-flatfish.tilda.ws/semeynie_konflikti_article`
  - `https://carry-pacific-flatfish.tilda.ws/vigoranie_article`
  - `https://carry-pacific-flatfish.tilda.ws/article_diary_of_emotions`
- Process note:
  - Tilda publishing triggered reliably through the visible DOM button and confirmation, while the earlier CSS click path sometimes did not start the publish job.
  - Follow-up rule: when publish progress is not visible after selector click, use the visible DOM node for `Опубликовать все страницы` and verify with HTTP plus Browser Use.
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 67.
  - Pending staging pages: 64.
- Follow-up priority:
  - Continue with published article/EI pages: `eintellect`, `trauma`, `abuse_gaslight`, `article_gadget_addiction`, `article_femininity`, `article_toxic_job`, then deeper EI knowledge-base and event/news pages.


## 2026-05-01T17:45:00+03:00 — Tilda EI and psychology article pages copied to staging

- Project: `moon-psy-site`.
- Workstream: `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: continue copying the next published/live pages from the original Moonn project into staging.
- Strategic assessment:
  - Platform value: high, because these EI/psychology articles extend the SEO and knowledge-base layer in the staging mirror.
  - Obsolescence risk: medium, because later content edits should pass SEO/editorial/legal review instead of being mixed with raw copying.
  - Stronger architecture: keep source-identical staging first, then improve content in separate reviewed batches.
  - Reuse: the one-page copy rhythm reduced timeout risk and should be preferred for Tilda batches.
  - 3-12 month risk if skipped: staging would miss high-value article pages and future SEO work could diverge from production behavior.
- Eligibility check:
  - `https://moonn.ru/eintellect` returned `200`.
  - `https://moonn.ru/trauma` returned `200`.
  - `https://moonn.ru/abuse_gaslight` returned `200`.
  - `https://moonn.ru/article_gadget_addiction` returned `200`.
  - `https://moonn.ru/article_femininity` returned `200`.
  - `https://moonn.ru/article_toxic_job` returned `200`.
- Actions:
  - Copied and normalized six pages:
    - `63574637` -> `138693676`, alias `eintellect`.
    - `63579285` -> `138693896`, alias `trauma`.
    - `63684093` -> `138694136`, alias `abuse_gaslight`.
    - `63692311` -> `138694256`, alias `article_gadget_addiction`.
    - `64057747` -> `138694396`, alias `article_femininity`.
    - `64061157` -> `138694546`, alias `article_toxic_job`.
  - Published the `Moonn Staging` project.
  - Verified the public URLs through direct HTTP checks and Browser Use.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
- Verified live staging URLs:
  - `https://carry-pacific-flatfish.tilda.ws/eintellect`
  - `https://carry-pacific-flatfish.tilda.ws/trauma`
  - `https://carry-pacific-flatfish.tilda.ws/abuse_gaslight`
  - `https://carry-pacific-flatfish.tilda.ws/article_gadget_addiction`
  - `https://carry-pacific-flatfish.tilda.ws/article_femininity`
  - `https://carry-pacific-flatfish.tilda.ws/article_toxic_job`
- Current copy state:
  - Published production pages: 131.
  - Copied and verified staging pages: 73.
  - Pending staging pages: 58.
- Follow-up priority:
  - Continue with deeper EI and knowledge-base pages: `emotional-intelligence/knowledge-base/male-loneliness-russia`, `articles/eq-dlya-rukovoditeley`, `emotional-intelligence/ei-leader-12`, `personal-boundaries`, `active-listening`, `emotional-contagion`.


## 2026-05-01T18:10:00+03:00 — Tilda Radiant Sanctuary design pilot prepared

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: inspect the uploaded redesign ZIP and start applying a unified design style to the staging homepage before rolling it out to copied pages.
- Strategic assessment:
  - Platform value: high, because a reusable Tilda theme layer can unify consultation, lecture, product, and knowledge-base pages.
  - Obsolescence risk: medium, because a purely decorative redesign without a reusable theme contract would drift again across pages.
  - Stronger architecture: create a canonical CSS theme and page-level pilot first, then roll out through a controlled QA workflow.
  - Reuse: the same CSS theme can later be inserted page-by-page or promoted to site-level styling after approval.
  - 3-12 month risk if skipped: pages will keep diverging visually, making future SEO/product/payment improvements harder to test and transfer.
- Source design packet:
  - `C:\Users\yanta\Downloads\stitch_moonn.ru_modern_tilda_redesign (1).zip`.
  - Archive contains `DESIGN.md` only, not ready-to-upload assets.
  - Design direction: `The Radiant Sanctuary`.
- Actions:
  - Extracted and reviewed `DESIGN.md`.
  - Created canonical theme file `assets/tilda-radiant-sanctuary.css`.
  - Created implementation note `docs/tilda-radiant-sanctuary.md`.
  - Built a local preview from the published staging homepage at `output/tilda-design-preview/index.html`.
  - Opened local preview in Browser Use at `http://127.0.0.1:8788/` and confirmed the homepage DOM/content still loads.
  - Located the Tilda insertion point for the staging homepage:
    - Page id: `138660066`.
    - Tilda path: `Настройки страницы -> Дополнительно -> Html-код для вставки внутрь HEAD -> Редактировать код`.
- Boundary:
  - No Tilda page was modified in this step.
  - No production project was touched.
  - Before actual insertion and staging publication, an explicit action-time confirmation is required because it modifies a public staging page.
- Next step:
  - After confirmation, insert the theme snippet into the staging homepage HEAD, publish only `Moonn Staging`, then verify desktop/mobile rendering and links.


## 2026-05-01T18:35:00+03:00 — Radiant Sanctuary theme applied to staging homepage

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: after explicit confirmation, apply the prepared `Radiant Sanctuary` theme to the staging homepage.
- Strategic assessment:
  - Platform value: high, because this creates the first live Tilda proof of the unified visual system.
  - Obsolescence risk: medium, because the theme still needs broader multi-page QA before site-level rollout.
  - Stronger architecture: page-level pilot first, then reusable rollout to copied pages after review.
  - Reuse: the same snippet and editor workflow can be used for other staging pages.
  - 3-12 month risk if skipped: visual drift remains unresolved and product/payment pages would inherit inconsistent styles.
- Actions:
  - Inserted the theme snippet into the staging homepage page HEAD code.
  - Published only `Moonn Staging`.
  - Verified the live HTML contains `moonn-radiant-sanctuary` and `moonn-radiant-sanctuary-theme`.
  - Opened the live staging homepage in Browser Use and confirmed main content, navigation, CTA links, and buttons still appear in the DOM.
  - Captured a first-screen Browser Use screenshot and found no critical first-screen overlap.
  - Updated `docs/tilda-radiant-sanctuary.md`.
- Live staging URL:
  - `https://carry-pacific-flatfish.tilda.ws/`
- Incident/process note:
  - Initial save attempt using the hidden `textarea[name="headcode"]` did not persist.
  - Root cause: Tilda's code editor uses a visible editor field and syncs into the hidden `headcode` field.
  - Follow-up rule: insert code through the visible editor, save, reload the editor, and confirm the hidden field contains the snippet before publishing.
- Boundary:
  - Production `moonn.ru` was not changed.


## 2026-05-01T19:25:00+03:00 — Homepage SEO/AEO pilot manifest for Moonn staging

- Project: `moon-psy-site`.
- Workstream: `seo-aeo-retrofit`.
- Branch: `codex/tilda-api-sync`.
- Request: start the second task after the Tilda visual rollout: maximize SEO/AEO for 2026, first on the homepage, then scale context-specific SEO across all copied pages; include image SEO, metadata, query/indexing analysis, and a plan for why pages are or are not found.
- Strategic assessment:
  - Platform value: high, because the homepage is the routing hub for consultations, lectures, paid products, and the knowledge base.
  - Obsolescence risk: high if one generic SEO template is reused across all pages.
  - Stronger architecture: page-specific SEO/AEO manifests with schema.org, image maps, heading plans, canonical rules, and QA gates.
  - Reuse: the manifest pattern can scale to all copied staging pages.
  - 3-12 month risk if skipped: duplicate metadata, weak entity signals, poor image SEO, and no reliable way to diagnose indexing.
- Verified facts:
  - Production homepage is live at `https://moonn.ru/`.
  - Staging homepage is live at `https://carry-pacific-flatfish.tilda.ws/` and intentionally has `noindex,nofollow`.
  - Current homepage has no JSON-LD.
  - Current heading structure has multiple H1 section headings and no detected H2 headings in the sampled DOM.
  - Most meaningful homepage images have empty `alt`; current `og:image` uses a weak Tilda CDN filename `___.jpg`.
  - Public search can show partial brand coverage, but real query frequency, CTR, and index exclusion reasons require Google Search Console and Yandex Webmaster.
- Created or changed files:
  - `registry/seo/moonn-homepage-seo-aeo-2026.json`
  - `docs/seo/moonn-homepage-seo-aeo-pilot.md`
  - `docs/seo/moonn-homepage-jsonld-draft.html`
  - `assets/images/tatiana-munn-psiholog-mgu-moscow-consultation.webp`
- Decisions:
  - Keep staging pages `noindex,nofollow` during SEO testing to avoid duplicate indexation.
  - Avoid guarantee-like wording and medical-status ambiguity in SEO metadata unless credentials and legal wording are confirmed.
  - Do not add FAQ or Review schema until visible page content and review sources are verified.
- Open questions:
  - Need Google Search Console and Yandex Webmaster access or exports for real query and indexing diagnostics.
  - Need confirmation before inserting the SEO pilot into the Tilda staging homepage and publishing it.
- Boundary:
  - Production `moonn.ru` was not changed.


## 2026-05-01T19:45:00+03:00 — Entity linking for Tatiana Moonn, Yandex Services, and MSU Istina

- Project: `moon-psy-site`.
- Workstream: `seo-aeo-retrofit`.
- Branch: `codex/tilda-api-sync`.
- Request: account for the fact that Yandex Services uses the required real-name variant `Татьяна Мунн (Кумскова)` / `Татьяна Кумскова`, while the site mostly says `Татьяна Мунн`; also find and connect the MSU Istina profile.
- Strategic assessment:
  - Platform value: high, because external high-authority profiles help search engines connect reviews, academic credibility, and the official site.
  - Obsolescence risk: high if the site keeps only the public name and external platforms keep the legal/platform name.
  - Stronger architecture: explicit entity graph using visible biography text plus `Person.alternateName` and `Person.sameAs`.
  - Reuse: the same entity-linking model can be reused on speaker, reviews, consultations, lectures, and paid-course pages.
  - 3-12 month risk if skipped: Yandex/Google/AI search may treat Moonn, Kumskova, Yandex Services, and Istina as weakly related or separate entities.
- Verified facts:
  - Yandex Services profile URL found from public snippets/descriptions: `https://yandex.ru/uslugi/profile/TatyanaKumskova-948629`.
  - A public search result shows the name form `Татьяна Кумскова ( Татьяна Мунн)` on Yandex Services.
  - MSU Istina profile found: `https://istina.msu.ru/workers/816305440/`.
  - Istina profile name: `Кумскова Татьяна Михайловна`; IRID: `816305440`; public activity summary includes 4 articles, 1 учебный курс, and 4 conference talks.
- Changed files:
  - `registry/seo/moonn-homepage-seo-aeo-2026.json`
  - `docs/seo/moonn-homepage-seo-aeo-pilot.md`
  - `docs/seo/moonn-homepage-jsonld-draft.html`
  - `docs/codex-chat-history.md`
- Decision:
  - Add both a visible identity bridge and schema-level `alternateName`/`sameAs`; do not hide the name connection only in structured data.
- Boundary:
  - Tilda staging was not changed in this step.
  - Production `moonn.ru` was not changed.


## 2026-05-01T19:58:00+03:00 — Tilda-native SEO controls added to Moonn SEO pilot

- Project: `moon-psy-site`.
- Workstream: `seo-aeo-retrofit`.
- Branch: `codex/tilda-api-sync`.
- Request: user noted that Tilda itself may contain SEO information and asked to gather it for the SEO work.
- Verified Tilda facts from official help:
  - Tilda SEO Assistant exists under Site Settings → SEO → SEO Assistant and can show indexing/SEO errors.
  - Page-level SEO title/description/social preview/canonical settings are available under Page Settings.
  - H1/H2/H3 can be set through block title tag settings; Tilda recommends one H1 per page.
  - Image alt can be set through the image menu/content panel; decorative backgrounds do not require alt.
  - Tilda can connect/verify Google Search Console through Site Settings → SEO or ownership verification.
  - Tilda generates `robots.txt` and `sitemap.xml`, and supports HTTPS/WWW and 301 redirect settings.
  - JSON-LD/microdata can be added through page/head custom HTML.
- Decision:
  - Use Tilda native controls for title, description, canonical, social preview, headings, image alt, redirects, robots/sitemap checks, and SEO Assistant.
  - Use custom Head code only for schema.org JSON-LD/entity graph.
- Changed files:
  - `registry/seo/moonn-homepage-seo-aeo-2026.json`
  - `docs/seo/moonn-homepage-seo-aeo-pilot.md`
  - `docs/codex-chat-history.md`
- Incident:
  - Symptom: Browser Use timed out while attempting to open Search Console, GA4, Yandex Webmaster, and Metrica tabs together.
  - Root cause: multi-tab browser automation call exceeded the tool timeout / browser context closed.
  - Solution: continue fact gathering from official docs and retry browser access in smaller single-tab steps after the user has the in-app browser active.
- Boundary:
  - No external account settings were changed.
  - Tilda staging and production were not changed.


## 2026-05-01T19:13:04+03:00 — All copied Tilda pages audited for card/grid regression

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: check all other copied staging pages so the same card/text-column substrate problem does not remain elsewhere.
- Strategic assessment:
  - Platform value: high, because the visual system must be reliable before payment/video and SEO work starts.
  - Obsolescence risk: medium while pages depend on a mutable branch CDN URL with stale cache behavior.
  - Stronger architecture: commit-pinned CSS per staging page plus automated card/grid audit after each theme change.
  - Reuse: the audit can be reused for future batches of copied Tilda pages.
  - 3-12 month risk if skipped: layout regressions will recur whenever a generic Tilda block class appears on a copied page.
- Audit results:
  - Checked copied staging pages: `73`.
  - Live pages with HTTP success: `73`.
  - Pages with theme marker: `73`.
  - Pages already pinned to verified CSS `@102fb3d`: `2`.
  - Pages still loading branch CSS `@codex/tilda-api-sync`: `71`.
  - Pages with browser audit completed: `72`.
  - Pages with suspicious card/grid blocks: `59`.
  - One page, `/events_tp`, timed out on `networkidle` but live HTTP was `200`; it should be rechecked after the pinned rollout.
- Root cause:
  - The two manually hotfixed pages are clean, but most pages still load the mutable branch CDN URL. jsDelivr continued to serve the old broad CSS for that branch even after purge.
- Recommended action:
  - Pin all `copied_verified` staging pages to `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@102fb3d/assets/tilda-radiant-sanctuary.css`.
  - Republish staging pages.
  - Rerun the card/grid audit and require `branch_css = 0`, `pages_with_suspicious_card_or_grid_blocks = 0` except manually reviewed page-specific layouts.
- Changed files:
  - `registry/tilda/moonn-staging-page-map.json`
  - `docs/codex-chat-history.md`
- Boundary:
  - Production `moonn.ru` was not changed.
  - No mass Tilda page HEAD update was performed during this audit entry because that would publish public staging-page changes and requires action-time confirmation.


## 2026-05-01T19:39:57+03:00 — All copied Tilda pages pinned to verified CSS and republished

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: after confirmation, fix the same card/text-column regression on all copied staging pages.
- Actions:
  - Updated page-level HEAD snippets for all `73` `copied_verified` staging pages to use the verified pinned CSS:
    `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@102fb3d/assets/tilda-radiant-sanctuary.css`.
  - Recovered from a mid-run Tilda login reset and retried the five missed pages:
    `psychoanalys`, `geshtalt`, `schematherapy`, `uslugi_fin_blocks`, `uslugi_podrostki`.
  - Published all pages in `Moonn Staging`.
- Verification:
  - Live pages checked: `73`.
  - Pages loading pinned CSS `@102fb3d`: `73`.
  - Pages still loading branch CSS `@codex/tilda-api-sync`: `0`.
  - Browser card/grid audit completed: `73`.
  - Real card/grid regressions after final audit: `0`.
  - One final warning on `/emotional-intelligence/` was reviewed as a false positive: the `t686` block has native `overflow:hidden` and matching 1200px/560px geometry on production.
- Incident/process note:
  - Browser Use MCP became unresponsive during the long Tilda editor run; fallback Playwright was used in a separate browser window after the user confirmed and reauthenticated Tilda.
  - Follow-up rule: long Tilda mass edits should run in bounded batches with progress artifacts and login recovery, then publish only after every editor page verifies.
- Artifacts:
  - `artifacts/tilda-pin-all-102fb3d-playwright/editor-results.json`
  - `artifacts/tilda-pin-all-102fb3d-playwright/retry-5-results.json`
  - `artifacts/tilda-pin-all-102fb3d-playwright/live-html-results.json`
  - `artifacts/tilda-all-pages-card-audit-102fb3d-final/summary.json`
- Boundary:
  - Production `moonn.ru` was not changed.


  - This is a staging homepage pilot only, not a full site-level rollout.
- Next step:
  - User visual review of the staging homepage.
  - After approval, apply the theme to a small second batch: one consultation page, one lecture/product page, and one knowledge-base article, then compare for collisions.


## 2026-05-01T19:10:00+03:00 — Animated gradient orbs added to staging homepage

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: make the unified Tilda design visibly closer to the reference by adding soft moving pink/violet/cyan gradient circles behind the white sections and first-screen content.
- Strategic assessment:
  - Platform value: high, because the orbs become part of the reusable visual language for consultation, lecture, product, and knowledge-base pages.
  - Obsolescence risk: low if kept in the canonical CSS theme instead of per-page manual shapes.
  - Stronger architecture: one theme layer in Git, inserted into staging HEAD, then rolled out to selected pages after QA.
  - Reuse: direct reuse on copied staging pages without touching Tilda block content.
  - 3-12 month risk if skipped: the visual system remains too subtle and page-by-page redesign work will drift again.
- Actions:
  - Updated `assets/tilda-radiant-sanctuary.css` with animated ambient gradients and section-level orb pseudo-elements.
  - Added Zero Block-specific orb support for `.t396__artboard`.
  - Restored the staging homepage HEAD code to exactly one `moonn-radiant-sanctuary-theme` block.
  - Published only `Moonn Staging`.
  - Verified the live staging homepage HTML contains `moonn-radiant-sanctuary-theme`, `moonnSectionOrbA`, and `t396__artboard::before`.
  - Opened the live staging homepage in Browser Use and confirmed the main homepage DOM text remains present.
  - Updated `docs/tilda-radiant-sanctuary.md`.
- Live staging URL:
  - `https://carry-pacific-flatfish.tilda.ws/`
- Incident:
  - Symptom: replacing existing Tilda page HEAD through the visible Ace textarea produced a duplicate theme block; a subsequent cleanup attempt saved an empty HEAD.
  - Root cause: Tilda's Ace editor and hidden `textarea[name="headcode"]` do not sync reliably when using direct fill/clipboard replacement against an already populated editor.
  - Solution: restore from the canonical CSS file, type the snippet into an empty Ace editor state, save, reload, and verify the hidden `headcode` contains exactly one theme block.
  - Follow-up rule: for future Tilda HEAD replacements, do not rely on hidden textarea fill and do not declare success until the editor reload shows exactly one canonical block and the public HTML contains the expected markers.
- Boundary:
  - Production `moonn.ru` was not changed.
  - This remains a staging homepage pilot until the user approves rollout to a small second batch.


## 2026-05-01T19:35:00+03:00 — Gradient orbs changed to scroll-bound behavior

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: make the two large gradient circles move with scrolling and continue down the page instead of staying fixed to the first screen.
- Strategic assessment:
  - Platform value: high, because the behavior becomes part of the reusable visual system.
  - Obsolescence risk: low, because the behavior is implemented in the canonical CSS file rather than manual Tilda shapes.
  - Stronger architecture: scroll-bound document background plus section-local orbs gives the homepage and future pages the same design logic.
  - Reuse: direct rollout to copied staging pages after visual approval.
  - 3-12 month risk if skipped: the circles would feel like a first-screen decoration rather than a site-wide design language.
- Actions:
  - Changed `body::before` from `position: fixed` to document-bound `position: absolute`.
  - Added `background-repeat: repeat-y` with staggered gradient layer sizes and positions.
  - Kept slow background-position animation so the circles still drift subtly while scrolling.
  - Replaced the Tilda homepage HEAD with exactly one canonical theme block.
  - Published only `Moonn Staging`.
  - Performed a slow Browser Use scroll check on the live staging homepage.
  - Verified live HTML contains exactly one `moonn-radiant-sanctuary-theme` block and the scroll-bound markers `background-repeat: repeat-y` and `moonnSectionOrbA`.
- Live staging URL:
  - `https://carry-pacific-flatfish.tilda.ws/`
- Boundary:
  - Production `moonn.ru` was not changed.


## 2026-05-01T19:55:00+03:00 — Tilda button gradients preserved

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: compare staging buttons with the original site because the user noticed button color changes; original buttons had gradient color and hover highlighting.
- Strategic assessment:
  - Platform value: high, because CTA appearance affects conversion and trust.
  - Obsolescence risk: medium if the shared theme keeps overriding per-page Tilda button styles.
  - Stronger architecture: preserve page-authored Tilda button gradients and use the shared theme only for non-destructive hover polish.
  - Reuse: this prevents the same button regression on consultation, lecture, product, and knowledge-base pages.
  - 3-12 month risk if skipped: global design rollout could silently damage existing CTA styles across many copied pages.
- Findings:
  - Production and staging HTML both contained the original Tilda gradient:
    `background-image:linear-gradient(0.5turn,rgba(127,0,255,1) 0%,rgba(225,0,255,1) 100%)`.
  - The shared theme was overriding button background/color globally via `.t-btn`, `.t-btnflex`, `.t1028__btn`, and `.tn-atom__button`.
- Actions:
  - Removed the forced theme button background.
  - Removed forced white button text and forced border reset.
  - Kept hover brightness/saturation, slight lift, and purple shadow.
  - Replaced the Tilda homepage HEAD with exactly one canonical theme block.
  - Published only `Moonn Staging`.
  - Verified live staging contains the original Tilda gradient, exactly one theme block, and no removed forced theme gradient.
  - Browser Use live DOM check confirmed the relevant buttons remain present.
- Live staging URL:
  - `https://carry-pacific-flatfish.tilda.ws/`
- Boundary:
  - Production `moonn.ru` was not changed.


## 2026-05-01T20:55:00+03:00 — Radiant Sanctuary rolled out to all copied staging pages

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: apply the approved visual design to all copied staging pages, preserve original button gradients, then provide several pages for visual review.
- Strategic assessment:
  - Platform value: high, because the staging copy now has one reusable visual system before payment/video and SEO work begins.
  - Obsolescence risk: medium if each page stores a full CSS copy; lower after switching to a short CDN snippet tied to the canonical Git CSS.
  - Stronger architecture: canonical CSS in Git, short page-level Tilda HEAD snippet per copied page, machine verification across the registry.
  - Reuse: the same rollout pattern can be used for future copied pages and other Tilda projects.
  - 3-12 month risk if skipped: copied pages would drift visually, and product/payment pages would be tested on inconsistent layouts.
- Actions:
  - Tried project-level Tilda HEAD first; it saved in Tilda but did not propagate reliably to already published pages.
  - Cleared the unused project-level HEAD after deciding against it.
  - Added a short marked page-level snippet to all `73` `copied_verified` pages.
  - Snippet loads canonical CSS from:
    `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@codex/tilda-api-sync/assets/tilda-radiant-sanctuary.css`.
  - Re-ran missing pages in verified mode after the first quick pass showed some Tilda saves were not reflected live.
  - Published staging and ran a live HTTP check across all `73` copied URLs.
  - Opened one control page in Browser Use:
    `https://carry-pacific-flatfish.tilda.ws/psiholog-konsultacii-moskva?review-theme=1`.
  - Updated `registry/tilda/moonn-staging-page-map.json`.
  - Updated `docs/tilda-radiant-sanctuary.md`.
- Verification:
  - Checked live staging URLs: `73`.
  - URLs with theme/CDN marker: `73`.
  - Failed URLs: `0`.
  - Confirmed forced theme button gradient is absent.
  - Confirmed forced white button text is absent.
- Review sample URLs:
  - `https://carry-pacific-flatfish.tilda.ws/psiholog-konsultacii-moskva`
  - `https://carry-pacific-flatfish.tilda.ws/events_tp`
  - `https://carry-pacific-flatfish.tilda.ws/kurs-ei`
  - `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/benefits-of-ei`
  - `https://carry-pacific-flatfish.tilda.ws/uslugi_depression`
- Incident:
  - Symptom: Tilda project-level HEAD and first publish-all attempt left a subset of pages without the theme in live HTML.
  - Root cause: project-level HEAD did not reliably propagate to already published pages; quick page HEAD saves also needed editor reload verification, and final publication only completed after using publish-all from the project/search context.
  - Solution: use page-level marked CDN snippets, verify editor persistence after save for pages that miss live checks, then verify live output across every copied URL.
  - Follow-up rule: for future Tilda mass rollouts, do not trust editor save or publish-all alone; require registry-driven live URL verification.
- Boundary:
  - Production `moonn.ru` was not changed.


## 2026-05-01T18:38:29+03:00 — Tilda card substrates preserved after theme regression

- Project: `moon-psy-site`.
- Workstream: `staging-design-system` under `tilda-api-sync`.
- Branch: `codex/tilda-api-sync`.
- Request: check copied staging pages where text columns/cards on white substrates appeared shifted or lost their original backing after the visual theme rollout.
- Strategic assessment:
  - Platform value: high, because the shared design system must not damage reusable Tilda content blocks.
  - Obsolescence risk: medium if the theme keeps targeting generic Tilda classes that change meaning across block types.
  - Stronger architecture: keep the shared theme as a non-destructive visual layer and preserve Tilda-authored card/substrate geometry.
  - Reuse: the rule protects consultation, lecture, paid product, and knowledge-base pages.
  - 3-12 month risk if skipped: every future copied page with `.t-item` or card grids could silently lose its layout or readable substrates.
- Incident:
  - Symptom: staging pages such as `/emotional-intelligence/articles/benefits-of-ei` and `/uslugi_depression` showed text/card columns that looked clipped, shifted, or stripped of their original white backing.
  - Root cause: the all-page CSS rollout used broad selectors for `.t-item`, `.t-card__col`, and related Tilda wrappers, forced `.t-rec` background/overflow rules, and narrowed the standard `.t-container` width from Tilda's 1200px grid.
  - Solution: remove global card/substrate restyling, remove the forced odd-section background override, remove forced transparent background/overflow clipping from `.t-rec`, and remove global `.t-container` width narrowing.
  - Live hotfix: pinned the two reported pages to commit CSS `@102fb3d` because the jsDelivr branch URL continued serving stale CSS after purge.
  - Follow-up rule: future shared Tilda themes may enhance buttons, typography, and ambient background, but must not globally override generic Tilda block/card/container classes without page-specific QA.
- Verification:
  - `/emotional-intelligence/articles/benefits-of-ei`: staging now uses a 1200px `.t-container`, keeps three `.t-card__col` items in one row, and does not force card backgrounds.
  - `/uslugi_depression`: staging now matches production card substrate geometry: white `.t858__inner-col`, 5px radius, original shadow, 1200px container, three card items.
  - Both live pages contain pinned CSS `@102fb3d` and no longer contain the stale branch CSS URL.
- Changed files:
  - `.gitignore`
  - `assets/tilda-radiant-sanctuary.css`
  - `docs/tilda-radiant-sanctuary.md`
  - `registry/tilda/moonn-staging-page-map.json`
- Boundary:
  - Production `moonn.ru` was not changed.
