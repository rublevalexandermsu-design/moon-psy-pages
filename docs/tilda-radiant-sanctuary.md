# Tilda Radiant Sanctuary Redesign

## Source

- Design packet: `C:\Users\yanta\Downloads\stitch_moonn.ru_modern_tilda_redesign (1).zip`
- Extracted source file: `DESIGN.md`
- Creative direction: `The Radiant Sanctuary`

## Scope

First implementation target is the staging homepage only:

- Staging project: `Moonn Staging`, project id `25075076`
- Staging homepage page id: `138660066`
- Public URL: `https://carry-pacific-flatfish.tilda.ws/`

Production `moonn.ru` must not be changed until the staging page is reviewed and explicitly approved.

## Implementation Strategy

Use a Tilda-compatible CSS theme layer instead of rebuilding Tilda blocks manually.

Reasons:

- The staging homepage is already a large Tilda page with many blocks.
- A CSS theme keeps content, forms, links, Tilda block logic, and future page transfer behavior intact.
- The same theme can later be reused across consultation, lecture, product, and knowledge-base pages.
- Page-by-page rollout lets us catch layout collisions before applying the style globally.

## Canonical Theme File

- `assets/tilda-radiant-sanctuary.css`

The CSS adds:

- Plus Jakarta Sans typography.
- Light radiant surface background.
- Animated pink/violet/cyan gradient orbs behind the page and inside Zero Block artboards.
- Glass-style buttons and navigation.
- Original Tilda button gradients are preserved; the theme only adds hover brightness/shadow.
- Original Tilda card and text-column substrates are preserved; the theme does not globally restyle `.t-item` or `.t-card__col` geometry.
- Original Tilda container widths are preserved; the theme does not globally override `.t-container` or `.t-container_flex` width.
- Tilda button normalization.
- Focus states for forms.
- Reduced-motion safety.

The CSS intentionally avoids destructive layout changes. It does not reorder blocks, remove content, alter links, or change payment/form behavior.

## Tilda Insertion Contract

For a page-level pilot, insert the CSS into the page head or page custom HTML as:

```html
<script>
document.documentElement.classList.add('moonn-radiant-sanctuary');
</script>
<style>
/* paste assets/tilda-radiant-sanctuary.css here */
</style>
```

If Tilda strips `@import` inside a page-level style block, move the Google Fonts import to the page head or site head and leave the rest inside the style block.

## QA Gate

The page is not considered ready until these checks pass:

- Public staging URL opens with HTTP 200.
- Browser Use opens the page visually.
- No obvious overlapping text or CTA collisions on desktop viewport.
- Mobile viewport spot-check passes.
- Buttons remain clickable.
- Main forms remain visible.
- No production project publishing happened.

## Deployment Log

### 2026-05-01

- Inserted the theme snippet into the staging homepage HEAD code.
- Published only `Moonn Staging`.
- Confirmed the live homepage HTML contains:
  - `moonn-radiant-sanctuary`
  - `moonn-radiant-sanctuary-theme`
- Opened the live staging homepage in Browser Use.
- First-screen visual check passed: primary hero, menu, CTA buttons, and portrait area remain visible.
- Production `moonn.ru` was not changed.

### 2026-05-01 animated orb enhancement

- User feedback: the first live theme pass was too subtle and did not show the requested moving gradient circles.
- Added a stronger ambient layer:
  - scroll-bound page-level radial gradients on `body::before` and `body::after`;
  - per-section orbs on `.t-rec::before` and `.t-rec::after`;
  - Zero Block-specific orbs on `.t396__artboard::before` and `.t396__artboard::after`;
  - slow `moonnAmbient*` and `moonnSectionOrb*` animations;
  - reduced-motion support.
- Restored the staging homepage HEAD to exactly one `moonn-radiant-sanctuary-theme` block after Tilda editor cleanup produced a duplicate/empty state.
- Published only `Moonn Staging`.
- Confirmed the live staging HTML contains:
  - `moonn-radiant-sanctuary-theme`
  - `moonnSectionOrbA`
  - `t396__artboard::before`
- Browser Use opened the live staging homepage and confirmed the main homepage text is present in the live DOM.
- Production `moonn.ru` was not changed.

### 2026-05-01 scroll-bound orb behavior

- User clarification: the two large background circles should move with the page during scrolling, not stay pinned to the first viewport.
- Changed the ambient `body::before` layer from viewport-fixed to document-bound absolute positioning.
- Added vertical `repeat-y` gradient layers with staggered background sizes and positions so the circles continue through lower white sections.
- Kept slow background-position animation for subtle independent movement.
- Published only `Moonn Staging`.
- Performed a slow Browser Use scroll check on the live staging homepage.
- Confirmed the live staging HTML contains:
  - exactly one `moonn-radiant-sanctuary-theme` block;
  - `background-repeat: repeat-y`;
  - `moonnSectionOrbA`.
- Production `moonn.ru` was not changed.

### 2026-05-01 button gradient preservation

- User concern: the theme appeared to change button colors; original buttons had a purple/pink gradient and hover highlighting.
- Compared production `https://moonn.ru/` and staging HTML.
- Confirmed both contain the original Tilda button gradient:
  - `background-image:linear-gradient(0.5turn,rgba(127,0,255,1) 0%,rgba(225,0,255,1) 100%)`.
- Removed the theme-level forced button `background`, forced white text, and forced border reset.
- Kept a lightweight hover enhancement:
  - brighter/saturated hover filter;
  - subtle lift;
  - purple shadow.
- Published only `Moonn Staging`.
- Confirmed the live staging HTML:
  - still contains the original Tilda button gradient;
  - has exactly one `moonn-radiant-sanctuary-theme` block;
  - no longer contains the removed forced theme button gradient.
- Production `moonn.ru` was not changed.

### 2026-05-01 rollout to copied staging pages

- Applied the `Radiant Sanctuary` theme to all `copied_verified` staging pages from `registry/tilda/moonn-staging-page-map.json`.
- Scope:
  - checked copied staging pages: `73`;
  - live pages with theme after final publication: `73`;
  - failures after final live check: `0`.
- Final implementation:
  - each copied page has a short marked page-level HEAD snippet;
  - the snippet adds `moonn-radiant-sanctuary` to `<html>`;
  - the snippet loads the canonical CSS from GitHub CDN:
    `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@codex/tilda-api-sync/assets/tilda-radiant-sanctuary.css`.
- Reason for page-level CDN snippet:
  - project-level HEAD saved in Tilda but did not reliably appear on already published staging pages;
  - inserting full CSS into 73 pages would create large duplicated page HEAD blocks;
  - the CDN snippet keeps each page small and lets future theme changes happen through the canonical Git file.
- Button regression guard:
  - final live check confirmed the old forced theme button gradient is absent;
  - original Tilda button gradients remain page-authored.
- Production `moonn.ru` was not changed.

### 2026-05-01 card substrate preservation

- User reported that text columns/cards on copied staging pages looked shifted and lost their original white substrates.
- Root cause: the first all-page CSS rollout used broad selectors for `.t-item`, `.t-card__col`, and related Tilda block wrappers, plus a forced odd-section background override.
- Fixed the canonical CSS to preserve Tilda-authored card geometry and section backgrounds:
  - removed global card/substrate restyling for `.t-item` and `.t-card__col`;
  - removed global `.t-rec:nth-of-type(odd)` background override;
  - removed forced transparent background and overflow clipping from `.t-rec`.
  - removed global `.t-container` width narrowing that could wrap 3-column Tilda grids into 2-column layouts.
- Kept the shared visual layer:
  - page/section gradient orbs;
  - Zero Block orb styling;
  - original button gradients with hover enhancement.
- Because jsDelivr's branch URL continued to serve a stale cached copy after purge, pinned the two reported pages to the verified commit CSS URL:
  `https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@102fb3d/assets/tilda-radiant-sanctuary.css`.
- Production `moonn.ru` was not changed.

Review sample URLs:

- `https://carry-pacific-flatfish.tilda.ws/psiholog-konsultacii-moskva`
- `https://carry-pacific-flatfish.tilda.ws/events_tp`
- `https://carry-pacific-flatfish.tilda.ws/kurs-ei`
- `https://carry-pacific-flatfish.tilda.ws/emotional-intelligence/articles/benefits-of-ei`
- `https://carry-pacific-flatfish.tilda.ws/uslugi_depression`

## Tilda Editor Note

The page HEAD code editor has both a visible code editor textarea and a hidden `textarea[name="headcode"]`.

Do not fill only the hidden `headcode` textarea. It does not reliably persist through Tilda's save action.

Use the visible Ace editor field, save, reload the editor, and confirm the saved code appears in `headcode` before publishing.

If the HEAD editor needs to be replaced completely, first ensure the editor is empty. A direct `fill` into the visible Ace textarea can append a second copy when existing code is present. The verified recovery route for the current Tilda editor was:

1. Clear the editor to an empty saved state.
2. Type the full canonical snippet into the Ace input.
3. Save and reload the editor.
4. Confirm `textarea[name="headcode"]` contains exactly one `moonn-radiant-sanctuary-theme` block.

## Follow-Up Workstreams

The user's broader request splits into three workstreams:

1. `staging-design-system`: unify visual style across copied staging pages.
2. `paid-video-membership`: identify paid lecture/video pages and design payment plus protected viewing through Tilda-compatible mechanisms.
3. `seo-aeo-retrofit`: after design and paid access are stable, run SEO/AEO improvements page by page with metadata, schema, canonical, image alt, and content QA gates.

The paid video/membership workstream must be handled separately because it affects payments, access control, and user entitlements.
