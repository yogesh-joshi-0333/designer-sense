# Drawing with CSS and SVG

When a design needs a visual and no real image fits (an illustration, a decorative shape, a texture, a pattern, an icon, a diagram), draw it. Drawn graphics are sharp at any size, themable with tokens, animatable, and tiny. This file covers *what* to draw (design) and *how* (technique).

## Contents
1. Design first: what makes a drawing good
2. Choosing the tool
3. CSS shapes and gradients
4. clip-path, shape() and masks
5. SVG: building paths by hand
6. Strokes, patterns, textures and filters
7. Composing an illustration
8. Theming, motion and accessibility
9. Check the drawing by rendering it

---

## 1. Design first: what makes a drawing good

- **One graphic language.** Decide the style once and apply it to every drawn element on the page: geometric or organic, outline or filled, stroke width, corner style (round or sharp joins), number of tones, level of detail. Mixed languages (a flat icon next to a gradient-shaded blob next to a line drawing) look like clip art.
- **Few tones, flat steps.** 2–4 tones per object (base, shadow, highlight, line) read cleaner than smooth gradients everywhere. Light comes from one direction for the whole scene.
- **Three levels of detail.** Big silhouette shapes (read from far), medium forms (read on a glance), small details (reward a close look). Most weak drawings are all medium.
- **Silhouette test.** Fill the drawing in one flat colour. Is it still recognisable? If not, the shapes are wrong, not the colours.
- **Palette from the tokens.** Drawings use the page's palette (ink, accent, tinted neutrals), so they belong to the design and follow dark mode.
- **Purpose.** A drawing must say something about the subject (the idea in the brief) or support structure (a divider, a frame, a texture). Decoration that says nothing is noise.
- **Restraint with complexity.** A simple, well-proportioned geometric drawing beats an ambitious one with wobbly proportions. Pick a style you can execute precisely.

## 2. Choosing the tool

| Need | Tool |
|---|---|
| Background glow, mesh-like colour field, stripes, dots, checker, simple geometric pattern | CSS gradients (`background` layers) |
| A non-rectangular box, angled section edge, cut corner, image in a shape | `clip-path` (polygon/shape/path) |
| Fading edges, image vignettes, cut-outs, patterns that reveal content | `mask-image` |
| Small, simple shapes (circle, pill, triangle, ring) as part of a UI | CSS on an element/pseudo-element |
| Anything with curves you design, icons, illustrations, logos, charts, waves, blobs | Inline SVG |
| Grain, paper, noise, displacement, gooey effects | SVG filters |
| Thousands of particles, physics, generative per-frame art | Canvas/WebGL (outside this skill) |

Rule of thumb: if you are stacking more than ~4 gradients or 3 pseudo-elements to draw one object, switch to SVG. It will be shorter, clearer and easier to adjust.

## 3. CSS shapes and gradients

Gradients are an image layer; stack them with commas (first is on top), position and size each one.

```css
/* soft light field: two radial glows on a tinted ground */
.hero {
  background:
    radial-gradient(60% 50% at 15% 20%, oklch(0.85 0.12 70 / .55), transparent 70%),
    radial-gradient(50% 60% at 85% 70%, oklch(0.75 0.12 250 / .4), transparent 70%),
    var(--ground);
}

/* dot grid */
.dots { background: radial-gradient(circle, var(--line) 1px, transparent 1.5px) 0 0 / 20px 20px; }

/* hairline grid paper */
.grid-paper {
  background:
    linear-gradient(var(--line) 1px, transparent 1px) 0 0 / 32px 32px,
    linear-gradient(90deg, var(--line) 1px, transparent 1px) 0 0 / 32px 32px;
}

/* diagonal stripes */
.stripes { background: repeating-linear-gradient(-45deg, var(--accent) 0 6px, transparent 6px 14px); }

/* pie / progress ring with conic-gradient + mask */
.ring {
  --p: 68%;
  background: conic-gradient(var(--accent) var(--p), var(--line) 0);
  border-radius: 50%;
  mask: radial-gradient(farthest-side, transparent calc(100% - 10px), #000 calc(100% - 9px));
}
```

Technique notes:
- Hard colour stops (`red 50%, blue 0`) make sharp edges; add 0.5–1px between stops to avoid jagged edges.
- `background-blend-mode` and `mix-blend-mode` create overlaps and duotones (`multiply` on light, `screen` on dark). Use `isolation: isolate` on the parent to keep blending contained.
- Pseudo-elements (`::before`, `::after`) give two extra drawable layers per element; position them with `inset` and `z-index: -1` inside an `isolation: isolate` parent.
- `border-radius` with eight values (`40% 60% 55% 45% / 50% 40% 60% 50%`) makes organic blob shapes cheaply.
- `box-shadow` can draw copies of a shape (dots, stars) but is hard to maintain; prefer SVG.

## 4. clip-path, shape() and masks

```css
/* angled section edge */
.section { clip-path: polygon(0 0, 100% 0, 100% calc(100% - 4vw), 0 100%); }

/* cut corner card */
.ticket { clip-path: polygon(0 0, calc(100% - 20px) 0, 100% 20px, 100% 100%, 0 100%); }

/* curved shape that scales with the element: shape() (newly Baseline) with polygon fallback */
.wave-top { clip-path: polygon(0 8%, 100% 0, 100% 100%, 0 100%); }
@supports (clip-path: shape(from 0 0, line to 1px 1px)) {
  .wave-top {
    clip-path: shape(from 0% 10%, curve to 50% 6% with 25% 0%, smooth to 100% 4%,
                     line to 100% 100%, line to 0% 100%, close);
  }
}

/* fade the bottom edge of a scroll area */
.scroller { mask-image: linear-gradient(to bottom, #000 85%, transparent); }

/* image revealed through a pattern or an SVG shape */
.photo { mask: url(#blob) center / contain no-repeat; }   /* or a data-URI SVG */
```

- `path()` in clip-path uses absolute pixel units (doesn't scale); `shape()` uses percentages and scales with the element. Prefer `shape()` with a `polygon()` fallback, or an SVG `<clipPath clipPathUnits="objectBoundingBox">` (coordinates 0–1), which works everywhere.
- clip-path also clips shadows: put the shadow on a parent with `filter: drop-shadow(…)`.
- Masks use alpha (or luminance with `mask-mode`): black/opaque = visible.

## 5. SVG: building paths by hand

Design on a grid. Pick a `viewBox` with round numbers (`0 0 100 100`, or 24×24 for icons), sketch in coordinates, then refine.

**Path commands** (uppercase = absolute, lowercase = relative):
- `M x y` move, `L x y` line, `H x`/`V y` horizontal/vertical line, `Z` close.
- `C x1 y1 x2 y2 x y` cubic bézier: the two control points pull the curve. For a smooth join between two curves, the control points on either side of the join must be on one straight line through it (`S` does this automatically).
- `Q x1 y1 x y` quadratic (one control point), `T` continues it smoothly.
- `A rx ry rotation large-arc sweep x y` elliptical arc: for circles and rounded parts.

**Practical construction**
- Start with primitives (`<circle>`, `<rect rx>`, `<ellipse>`, `<polygon>`, `<line>`) and combine them; only use `<path>` for shapes primitives can't make.
- A wave: `M0 50 C 25 30, 25 30, 50 50 S 75 70, 100 50 V100 H0 Z`. A blob: 5–8 points around a circle, each moved in/out a little, joined with `C` curves whose control points are tangent to the circle.
- Group parts (`<g>`) by layer and give them classes; style with CSS (`fill: var(--accent)`), so the drawing is themable.
- Put transforms on `<g>`, and use `transform-box: fill-box; transform-origin: center;` when animating parts so they rotate around their own centre.
- `preserveAspectRatio="none"` stretches a drawing to any box (good for dividers/waves); the default keeps proportions (good for illustrations).
- `vector-effect: non-scaling-stroke` keeps line widths constant when the SVG scales.
- Reuse: `<symbol>` + `<use>` for repeated shapes (stars, leaves, icons).
- Keep it readable: round numbers to 1 decimal; avoid huge generated paths.

## 6. Strokes, patterns, textures and filters

**Strokes**
- `stroke-linecap="round"` and `stroke-linejoin="round"` give a friendly line style; `butt`/`miter` a technical one. Decide once.
- Line-drawing animation: `pathLength="1"` on the path, then `stroke-dasharray: 1; stroke-dashoffset: 1` animated to 0.
- `paint-order: stroke` puts the stroke behind the fill (clean outlined text or shapes).

**Patterns**: `<pattern>` with `patternUnits="userSpaceOnUse"` for tiles (hatching, dots, waves) inside SVG; CSS gradients for page backgrounds.

**Texture and noise** (keep it subtle; it should be felt, not seen):
```html
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .6 0"/>  <!-- noise → black specks with alpha -->
  </filter>
</svg>
```
```css
.grain::after { content: ""; position: absolute; inset: 0; filter: url(#grain); opacity: .06;
                pointer-events: none; mix-blend-mode: multiply; }
```
Or as a static background image: an SVG data URI containing the filter on a `<rect>`, tiled, which avoids re-filtering on every paint.

**Other filter effects**
- `feDisplacementMap` with turbulence: hand-drawn wobble, water, torn paper edges.
- `feGaussianBlur` + `feColorMatrix` alpha threshold: "gooey" merging blobs.
- `feDropShadow`, `feMorphology` (outline/thicken), `feComponentTransfer` (posterise, duotone).
- `filter: drop-shadow()` in CSS follows the shape's alpha (for clipped or SVG shapes), unlike `box-shadow`.
Filters are expensive over large areas: apply them to small elements or pre-render as background tiles.

## 7. Composing an illustration

1. **Concept**: what the drawing shows and why (from the brief's idea). One subject, one action.
2. **Silhouette and composition**: block in the big shapes first in one colour. Check balance, the focal point, how it sits in its layout box (leave breathing room; let it bleed off one edge if the layout wants it).
3. **Construction**: refine shapes with primitives and paths on the grid. Check proportions against reality (a bicycle wheel is not an oval).
4. **Tone**: add the 2–4 flat tones; one light direction.
5. **Line and detail**: add the small level of detail last, sparingly.
6. **Integrate**: palette from tokens, scale relative to type, alignment to the grid.

Scenes made of simple geometric parts (circles, rounded rects, arcs, triangles) with a consistent stroke and a 3-tone palette are the most reliable to execute well in code. Tilted overlapping planes, cut-outs and layered silhouettes (mountains, waves, city skylines) add depth cheaply.

## 8. Theming, motion and accessibility

- Colours via `currentColor` or CSS variables (`fill: var(--accent)`), so drawings follow the theme and dark mode.
- Animate parts with CSS (`transform`, `opacity`, stroke dash), keep loops slow and subtle, pause them with `prefers-reduced-motion`.
- Decorative drawings: `aria-hidden="true"` and no focusable elements. Meaningful ones: `role="img"` and a `<title>` (or `aria-label`).
- Inline SVG when it needs theming or animation; external file (`<img src="x.svg">`) when it is static and reused (it gets cached).

## 9. Check the drawing by rendering it

Coordinates that look right in your head are often wrong. Render the drawing (`scripts/shoot.py` on a small test page, or the whole page), look at it zoomed, and fix: shapes misaligned or overlapping wrongly, curves with kinks (control points not tangent), inconsistent stroke widths, proportions off, parts outside the viewBox, poor contrast against the background. Do at least one render-and-fix round for every illustration.