# CSS craft: modern CSS in the service of design

Choose CSS features by what the design needs, not by novelty. Each section starts from a design intent and shows the platform feature that serves it. Support status is as of late 2026 (from the web-features / Baseline data); re-check when in doubt.

## Contents
1. Architecture
2. Tokens from the brief
3. Layout
4. Fluid type and space
5. Colour systems
6. State and interaction without JavaScript
7. Motion
8. Support levels and fallbacks
9. Performance
10. Accessibility in CSS
11. Same design, other stacks

---

## 1. Architecture

Keep the cascade predictable so the design stays consistent as it grows.

```css
@layer reset, tokens, base, layout, components, utilities;
```
- **@layer** (safe everywhere): later layers win regardless of selector specificity, so a utility always beats a component without `!important`. Unlayered styles beat all layers, which is useful for overriding third-party CSS: put the library in a low layer (`@import url(lib.css) layer(vendor);`).
- **Nesting** (safe): nest states and children, but keep it shallow (2 levels) so specificity stays low.
- **Low specificity**: class selectors, `:where()` for base styles that should be easy to override. Avoid IDs and long chains in styles.
- **Custom properties** for every design decision that repeats; component-level properties for variants (`.btn { --btn-bg: var(--accent); background: var(--btn-bg) }` and `.btn.secondary { --btn-bg: transparent }`).
- **@scope** (newly Baseline): limit a component's styles to its subtree, including a lower boundary (`@scope (.card) to (.card-content)`). Fine to use; don't depend on it for critical isolation in older browsers.

## 2. Tokens from the brief

Translate the brief into a small token set. Name tokens by role, not by value (`--ink-muted`, not `--grey-500`).

```css
@layer tokens {
  :root {
    color-scheme: light dark;
    /* colour: roles, built in oklch; neutrals tinted toward the brand hue (h = 250 here) */
    --hue: 250;
    --ground:   light-dark(oklch(0.985 0.004 var(--hue)), oklch(0.17 0.01 var(--hue)));
    --surface:  light-dark(oklch(1 0 0),                  oklch(0.21 0.012 var(--hue)));
    --ink:      light-dark(oklch(0.22 0.02 var(--hue)),   oklch(0.95 0.01 var(--hue)));
    --ink-muted:light-dark(oklch(0.45 0.02 var(--hue)),   oklch(0.75 0.015 var(--hue)));
    --line:     color-mix(in oklch, var(--ink) 14%, transparent);
    --accent:   light-dark(oklch(0.6 0.19 35), oklch(0.72 0.16 35));
    --on-accent: oklch(0.99 0 0);

    /* type */
    --font-display: "Fraunces", Georgia, serif;
    --font-text: "Inter", system-ui, sans-serif;
    --step-0: clamp(1rem, 0.96rem + 0.2vw, 1.125rem);
    --step-1: clamp(1.25rem, 1.1rem + 0.6vw, 1.5rem);
    --step-2: clamp(1.6rem, 1.3rem + 1.4vw, 2.25rem);
    --step-3: clamp(2.2rem, 1.5rem + 3vw, 3.75rem);
    --step-4: clamp(2.8rem, 1.6rem + 5.5vw, 6rem);

    /* space: 4px base */
    --space-1: .25rem; --space-2: .5rem; --space-3: .75rem; --space-4: 1rem;
    --space-6: 1.5rem; --space-8: 2rem; --space-12: 3rem; --space-16: 4rem; --space-24: 6rem;
    --section: clamp(4rem, 3rem + 6vw, 9rem);

    /* shape & depth */
    --radius: 14px;
    --shadow-1: 0 1px 2px oklch(0.2 0.02 var(--hue) / .08), 0 2px 8px oklch(0.2 0.02 var(--hue) / .06);
    --shadow-2: 0 2px 4px oklch(0.2 0.02 var(--hue) / .08), 0 12px 32px -8px oklch(0.2 0.02 var(--hue) / .18);

    /* motion */
    --ease-out: cubic-bezier(.2, .8, .2, 1);
    --dur-1: 150ms; --dur-2: 260ms;
  }
}
```
`light-dark()` needs `color-scheme` set; it is safe everywhere now. If the site has a manual theme toggle, set `color-scheme: light` / `dark` on `:root[data-theme]` and the same tokens follow.

## 3. Layout

**Grid for two-dimensional structure, flex for one-dimensional flow.**

- **Page grid with full-bleed escape.** One grid where content sits in the middle and any child can break out:
  ```css
  .page {
    display: grid;
    grid-template-columns:
      [full-start] minmax(var(--gutter, 1rem), 1fr)
      [content-start] min(100% - 2 * var(--gutter, 1rem), 72rem) [content-end]
      minmax(var(--gutter, 1rem), 1fr) [full-end];
  }
  .page > * { grid-column: content; }
  .page > .bleed { grid-column: full; }
  ```
  For an image that bleeds to one edge while text stays on the grid, span `full-start / content-end` and put the text in its own column.
- **Responsive without breakpoints**: `grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr))`.
- **Subgrid** (safe) aligns parts across sibling cards (titles, prices and buttons line up even when text lengths differ):
  ```css
  .plans { display: grid; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); }
  .plan  { display: grid; grid-row: span 4; grid-template-rows: subgrid; }
  ```
- **Container queries** (safe) make components respond to the space they get, not the viewport. Use them for anything that can appear in different places:
  ```css
  .card-wrap { container-type: inline-size; }
  @container (width > 32rem) { .card { grid-template-columns: 12rem 1fr; } }
  .card h3 { font-size: clamp(1.1rem, 4cqi, 1.6rem); }   /* cqi = 1% of container inline size */
  ```
- **Viewport units**: `min-height: 100svh` for hero sections (no jump when mobile browser bars move).
- **Logical properties** (`margin-inline`, `padding-block`, `inset-inline-start`) so RTL works for free.
- **`aspect-ratio`** for media and placeholders; `object-fit: cover` + `object-position` to control the crop.
- **Overlap** with grid: put two items in the same cell (`grid-area: 1 / 1`) instead of absolute positioning, so the layout still flows.
- **Masonry** (`display: grid-lanes`) is Safari only: use a normal grid or CSS columns as the base.

## 4. Fluid type and space

- `clamp(min, preferred, max)` with a `rem + vw` preferred value scales smoothly and still respects user zoom (don't use pure `vw`).
- Compute: for size S1 at viewport V1 and S2 at V2, slope = (S2 − S1)/(V2 − V1); preferred = `S1 − slope·V1 + slope·100vw`. Example 40px@375 → 96px@1440: slope 0.0526 → `clamp(2.5rem, 1.27rem + 5.26vw, 6rem)`.
- Space can be fluid too (`--section` above), so desktop gets generous gaps without mobile getting huge ones.
- `text-wrap: balance` on headings (safe); `text-wrap: pretty` on paragraphs (harmless where unsupported).
- `hanging-punctuation: first` (Safari) and `font-feature-settings`/`font-variant-numeric` for refinement.
- `text-box: trim-both cap alphabetic` (Chrome/Safari) trims the extra space above caps and below baselines for precise alignment in buttons and badges; enhancement only.

## 5. Colour systems

- **oklch()** for every colour (safe). Predictable lightness steps; wide gamut available with chroma.
- **Relative colour** (newly Baseline) derives states and variants from one base:
  ```css
  --accent-hover: oklch(from var(--accent) calc(l - .06) c h);
  --accent-soft:  oklch(from var(--accent) .95 calc(c * .3) h);    /* tinted background */
  --accent-ring:  oklch(from var(--accent) l c h / .35);            /* focus ring */
  ```
- **color-mix()** (safe) for tints, translucency and mixing with the ground: `color-mix(in oklch, var(--accent) 12%, var(--surface))`.
- **Gradients in oklch** avoid grey dead zones: `linear-gradient(in oklch, …)`. For hue sweeps choose the direction: `in oklch longer hue`.
- **contrast-color()** is still landing (Interop 2026); compute "on" colours yourself for now.
- **Wide gamut**: `@media (color-gamut: p3)` can raise chroma for vivid accents on capable screens.

## 6. State and interaction without JavaScript

- **`:has()`** (safe) lets a parent react to its children: highlight a card when its checkbox is checked (`.plan:has(input:checked)`), style a form group with an invalid field (`.field:has(:user-invalid)`), change layout when an image exists (`.card:has(img)`). Scope it to a component, not `body`, for performance.
- **`:user-invalid`** (safe): show errors only after the user interacts, not on page load.
- **`:focus-visible`**: focus rings for keyboard users only.
- **Popover** (newly Baseline): `<div popover id="menu">` + `<button popovertarget="menu">` gives a dismissible layer with no JS. **Invoker commands** (`commandfor` + `command="show-modal"`) open `<dialog>`s declaratively (newly Baseline; tiny JS fallback if old browsers matter).
- **Anchor positioning** (works in Chrome, Firefox 147+, Safari 26; not yet Baseline) tethers tooltips and menus to their trigger:
  ```css
  .trigger { anchor-name: --menu; }
  .menu { position: absolute; position-anchor: --menu; top: anchor(bottom); left: anchor(left);
          position-try-fallbacks: flip-block; }
  ```
  Always leave a usable default position for browsers without it.
- **`<details>`/`<summary>`** for disclosure; style the marker; `::details-content` (Chrome) can be transitioned as an enhancement.
- **`field-sizing: content`** (newly Baseline) for auto-growing textareas.
- **Customizable select** (`appearance: base-select`, Chrome/Safari) as an enhancement; the native select is the fallback.

## 7. Motion

- **Transitions**: list properties explicitly (`transition: background-color var(--dur-1), transform var(--dur-1) var(--ease-out)`), never `transition: all`.
- **Entry animations with `@starting-style`** (newly Baseline): animate elements in when they appear or when `display` changes, without JS:
  ```css
  .toast { transition: opacity .25s, translate .25s var(--ease-out), display .25s allow-discrete; }
  @starting-style { .toast { opacity: 0; translate: 0 8px; } }
  [popover]:not(:popover-open) { opacity: 0; }
  ```
- **`linear()` easing** (safe) for springs and bounces in pure CSS.
- **Individual transforms** (`translate`, `scale`, `rotate`) so states can combine without overwriting each other.
- **@property** (newly Baseline) makes custom properties animatable: animate a gradient angle or a colour stop.
  ```css
  @property --angle { syntax: "<angle>"; inherits: false; initial-value: 0deg; }
  .ring { background: conic-gradient(from var(--angle), …); animation: spin 6s linear infinite; }
  @keyframes spin { to { --angle: 360deg; } }
  ```
- **Scroll-driven animations** (Baseline since Oct 2026 with Firefox 159): progress bars, reveals and parallax with no scroll listeners. Wrap in `@supports` and reduced motion:
  ```css
  @media (prefers-reduced-motion: no-preference) {
    @supports (animation-timeline: view()) {
      .reveal { animation: rise linear both; animation-timeline: view(); animation-range: entry 0% cover 30%; }
    }
  }
  @keyframes rise { from { opacity: 0; translate: 0 2rem; } }
  ```
  The content must be visible without the animation (the `from` keyframe only applies when it runs).
- **View transitions**: same-document (`document.startViewTransition`, newly Baseline; feature-check it) for state changes; cross-document (`@view-transition { navigation: auto; }`, Chrome/Safari) for multi-page sites. Unsupported browsers just navigate normally.
- **`interpolate-size: allow-keywords`** (Chrome only) animates to `height: auto`; elsewhere it simply doesn't animate, which is acceptable.

## 8. Support levels and fallbacks

| Use freely | Use with a light fallback | Enhancement only |
|---|---|---|
| @layer, nesting, :has, container size queries + cq units, subgrid, oklch, color-mix, light-dark, clamp, trig functions, round/mod, text-wrap: balance, linear(), dvh/svh, :user-invalid, mask, clip-path (polygon/path/circle), aspect-ratio, logical properties, shape-outside | relative colour, @property, popover, commandfor, @starting-style, allow-discrete, same-document view transitions, scroll-driven animations, @scope, shape(), container style queries, backdrop-filter, field-sizing, content-visibility, sibling-index() | anchor positioning, cross-document view transitions, text-wrap: pretty, text-box-trim, typed attr(), base-select, calc-size / interpolate-size, corner-shape, if(), @function, random(), scroll-state queries, ::scroll-marker carousels, grid-lanes masonry |

The pattern: write the solid version first, then layer the enhancement with `@supports` or rely on the browser ignoring what it doesn't understand. The design must look complete without the enhancement.

## 9. Performance

- Animate only `transform`, `opacity` (and `filter` sparingly). Never animate width, height, top, left or margin in a loop.
- `content-visibility: auto; contain-intrinsic-size: auto 600px;` on long off-screen sections.
- `contain: layout paint` on independent widgets.
- `will-change` only just before an animation, never globally.
- Big blurs, stacked `backdrop-filter`, SVG filters over large areas and many blend-mode layers are expensive: keep them small and few.
- Fonts: WOFF2, only the weights used, `font-display: swap`, preload the one critical font, fallback with `size-adjust` to reduce layout shift.
- Images: correct `width`/`height` or `aspect-ratio`, `loading="lazy"` below the fold, `fetchpriority="high"` for the hero image, modern formats.
- Scope `:has()` to components; avoid `:has()` on `html`/`body` with broad arguments.
- Ship less CSS: delete unused rules; drawings in CSS gradients are lighter than images, but a 200-line CSS illustration is not lighter than a 2KB SVG.

## 10. Accessibility in CSS

- `:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }` and never `outline: none` without a replacement.
- `@media (prefers-reduced-motion: reduce)`: remove movement.
- `@media (forced-colors: active)`: borders/outlines stay visible; use `CanvasText`/`ButtonText` system colours if custom backgrounds carry meaning.
- `@media (prefers-contrast: more)`: strengthen borders and muted text if the design relies on subtle tones.
- Don't convey meaning with colour alone (add an icon, text or pattern).
- Hide decorative SVGs (`aria-hidden="true"`), label meaningful ones (`role="img"` + `<title>`).
- Visually hidden text for icon-only buttons.
- Text must survive 200% zoom: use rem, avoid fixed heights on text containers.

## 11. Same design, other stacks

The design decisions don't change with the stack; only the syntax does. Follow the project's conventions.

- **Tailwind**: put tokens in the theme (`@theme { --color-accent: oklch(…); --font-display: …; }` in v4, or `tailwind.config` in v3). Use the arbitrary-value syntax for one-offs (`[grid-template-columns:…]`, `bg-[color-mix(in_oklch,var(--accent)_12%,transparent)]`). Put complex things (drawings, scroll animations, @property) in a CSS file with `@layer components`. Don't fight utilities with `!important`.
- **CSS Modules / Sass**: tokens as custom properties in a global file; modules for components. Prefer native nesting, custom properties and `color-mix` over Sass functions so values stay live at runtime.
- **CSS-in-JS** (styled-components, Emotion, vanilla-extract, Panda): tokens in the theme object mapped to CSS variables; keep static styles static (extracted) for performance.
- **Component libraries** (MUI, Chakra, shadcn, Bootstrap, daisyUI…): change the theme/tokens first, then component overrides. Respect the library's structure; style through its supported hooks.
- **Frameworks** (React, Vue, Svelte, Astro, server templates): no difference for CSS except scoping style; the HTML semantics and the design are the same.
- **Email**: a different world. Tables, inline styles, no modern CSS. Keep the design decisions; drop the features.