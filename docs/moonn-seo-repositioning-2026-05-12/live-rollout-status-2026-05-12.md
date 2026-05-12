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

## Raw HTML Verification

- Core page titles and canonicals are present after publication.
- `/speaker` has raw H1 count `1`.
- `/psypodgotovka1` has raw H1 count `1`.
- Homepage still has raw H1 count `5`; it requires a separate content/T123 gateway change.
- `/psiholog` has raw H1 count `0`; it requires a separate content/H1 change.
- `/emotional-intelligence/` has raw H1 count `0`; it requires a separate content/H1 change.
- `/otzivi` has raw H1 count `2`; it requires H1 cleanup if it remains the trust pillar.
- Applied archive/offtopic pages include a live noindex marker after publication.

## Incident

- Symptom: repeated Chrome/Tilda UI automation runs disturbed the user's active browser session and triggered re-opening/re-authentication/anti-bot friction.
- Root cause: after successful page publication, DevTools/Tilda UI state sometimes hid the Chrome address bar from UIA; the automation recovered by toggling DevTools and, once, launching Chrome. That violates the user's requirement to avoid occupying or disturbing the visible computer.
- Immediate correction: live UI automation is stopped. No more Chrome closing/restarting/reopening should be done in this rollout without explicit approval.
- Follow-up rule: remaining Moonn live SEO changes must use either a verified non-visual Tilda write path or a tightly scheduled user-approved visible session. The agent must not recover from UIA failures by restarting Chrome.

## Remaining Work

- Homepage content layer: replace/restructure the top semantic block so the raw HTML has exactly one H1 and four positioning routes.
- Core H1 cleanup: `/psiholog`, `/emotional-intelligence/`, `/otzivi`.
- Remaining noindex/redirect queue from the register.
- Schema/AEO answer sections and final sitemap/reindex packet after all live changes pass raw HTML and rendered checks.
