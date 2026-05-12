# Moonn SEO Repositioning Live Rollout Status — 2026-05-12

## Scope

- Branch: `codex/moonn-seo-positioning-architecture`.
- Source register: `docs/moonn-seo-repositioning-2026-05-12/url-decision-register.json`.
- Live apply report: `docs/moonn-seo-repositioning-2026-05-12/tilda-seo-ui-live-apply-report.json`.

## Applied Live

SEO settings were applied through Tilda page settings UI and published for these core pages:

- `/`
- `/psiholog`
- `/speaker`
- `/emotional-intelligence/`
- `/psypodgotovka1`
- `/otzivi`

Noindex/nofollow settings were applied and published for these archive/offtopic pages:

- `/aromatherapy`
- `/geshtalt`
- `/kpt`
- `/microbiom`
- `/water`
- `/salt`
- `/vacuum_cups`
- `/phytotherapy`

The remaining noindex queue from the 2026-05-12 register was also applied through the scoped Tilda page settings UI after the user explicitly allowed use of the already-open Alexander Chrome session:

- Total noindex queue: `47` pages.
- Tilda settings saved: `47/47`.
- Scoped page publish requested/completed from the page editor: `47/47`.
- Independent raw live verification immediately after publication: `18/47` already expose a `noindex` marker.
- The delayed set is mostly old numeric `page*.html` URLs; these require a cache/re-publish follow-up gate before they can be marked search-ready.

## Raw HTML Verification

- Core page titles and canonicals are present after publication.
- `/speaker` has raw H1 count `1`.
- `/psypodgotovka1` has raw H1 count `1`.
- Homepage still has raw H1 count `5`; it requires a separate content/T123 gateway change.
- `/psiholog` has raw H1 count `0`; it requires a separate content/H1 change.
- `/emotional-intelligence/` has raw H1 count `0`; it requires a separate content/H1 change.
- `/otzivi` has raw H1 count `2`; it requires H1 cleanup if it remains the trust pillar.
- Applied archive/offtopic pages include a live noindex marker after publication.
- Full noindex verification evidence: `docs/moonn-seo-repositioning-2026-05-12/noindex-live-verification-2026-05-12.json`.

## Incident

- Symptom: repeated Chrome/Tilda UI automation runs disturbed the user's active browser session and triggered re-opening/re-authentication/anti-bot friction.
- Root cause: after successful page publication, DevTools/Tilda UI state sometimes hid the Chrome address bar from UIA; the automation recovered by toggling DevTools and, once, launching Chrome. That violates the user's requirement to avoid occupying or disturbing the visible computer.
- Immediate correction: live UI automation is stopped. No more Chrome closing/restarting/reopening should be done in this rollout without explicit approval.
- Follow-up rule: remaining Moonn live SEO changes must use either a verified non-visual Tilda write path or a tightly scheduled user-approved visible session. The agent must not recover from UIA failures by restarting Chrome.
- 2026-05-12 follow-up correction after explicit visible-session approval:
  - Chrome selection was pinned to windows titled `Google Chrome`, avoiding Chromium-Gost.
  - The save button detector now accepts both `Сохранить изменения` and `Сохранить`.
  - The project-page reset now requires `tilda.ru/projects/`, not just any Tilda URL.
  - Publish popup closing now targets only the Tilda popup area, avoiding the Chrome tab close button.

## Remaining Work

- Homepage content layer: replace/restructure the top semantic block so the raw HTML has exactly one H1 and four positioning routes.
- Core H1 cleanup: `/psiholog`, `/emotional-intelligence/`, `/otzivi`.
- Noindex cache gate: recheck the delayed `29` pages from `noindex-live-verification-2026-05-12.json`; if still missing, use a safer redirect/remove-from-sitemap route instead of repeating blind UI saves.
- Redirect queue from the register.
- Schema/AEO answer sections and final sitemap/reindex packet after all live changes pass raw HTML and rendered checks.
