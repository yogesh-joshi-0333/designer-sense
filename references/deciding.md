# Deciding: the knowledge behind the design brief

This file is the designer's knowledge for each line of the brief. It is organised the way decisions flow: purpose → idea → structure → system → details. Every section explains *why*, because the right answer changes with the project and you need the reasoning to adapt it.

## Contents
1. Start from content and purpose
2. Finding the idea
3. Composition and hierarchy
4. Grid and space
5. Typography
6. Colour
7. Shape, depth and material
8. Imagery and graphics
9. Motion
10. The detail layer
11. Generic defaults and how to escape them
12. Working inside an existing system

---

## 1. Start from content and purpose

Design is the arrangement of content for a reader. Before choosing anything visual, know:
- **What the content actually is.** Collect the real text, data, images. If there are none, write realistic content: real-length headlines, plausible numbers (labelled as samples), real product names from the brief. Lorem ipsum hides every layout problem.
- **What the reader must do or understand**, in priority order. A pricing page exists to let someone pick a plan with confidence; a dashboard exists to show what changed and whether to act.
- **The argument.** For persuasive pages, write the page as a sequence of claims, each with its proof: "Bookkeeping takes 10 minutes a week → screenshot of the weekly review". A section without a claim and proof is filler; cut it. For product UI, the equivalent is the task flow: what the user does first, next, and what they need to see at each step.

**Mode sets the budget for expression.**
| Mode | Example | Expression budget | Priority |
|---|---|---|---|
| Operate | app UI, dashboard, admin, forms | Low: personality in 1–2 details only | Density, scannability, consistency, states |
| Read | docs, articles, long reports | Low–medium: in type | Measure, rhythm, navigation |
| Persuade | landing, marketing, pricing | Medium–high | Hierarchy, proof, one clear action |
| Experience | portfolio, campaign, art, game | High | The idea itself |

## 2. Finding the idea

An idea is what makes a design belong to its subject. Ways to find one:
- **Inventory the subject.** List 8–12 things only this subject has: materials, tools, places, vocabulary, artefacts, rituals, numbers. A bike repair shop: chain grease, spoke tension, the paper repair tag tied to the handlebar, worn workbenches, gear ratios, tyre tread. Then pick one to become a visual device: the repair tag becomes the pricing card shape; the tread pattern becomes a section divider.
- **Borrow a structure from the subject's world.** A recipe site laid out like a mise-en-place tray; a finance report like a ledger; a train company's timetable as the navigation.
- **Exaggerate one property.** Make the one thing that matters most enormous, or make everything else disappear.
- **Find the tension.** A serious subject with one playful element, or a playful brand with strict typographic discipline. Contrast reads as intention.

Then run the swap test: replace the subject with a neighbour (another bike shop → a coffee shop). If the design idea still works unchanged, it isn't an idea yet.

Ideas do not need to be loud. "All UI is set in one size; hierarchy comes only from weight and colour" is an idea. In operate mode, the idea is often a principle of order rather than a visual flourish.

## 3. Composition and hierarchy

**Hierarchy is contrast.** The eye goes first to whatever differs most from its surroundings: in size, weight, colour, isolation (space around it), or position. Use few levers at once. If everything is bold, nothing is.

- Decide the **1-2-3**: the one thing seen first, the second, the third. Make level 1 decisively bigger (2–4× the body size for display text), give it space, and keep level 2 clearly smaller. Weak hierarchy usually means levels 1 and 2 are too close.
- **One primary action per view.** Secondary actions look secondary (outline, ghost, text link).
- **Proximity groups.** Space inside a group must be clearly smaller than space between groups (≥1.5–2×). A label belongs to its field; a heading belongs to the section below it (more space above a heading than below).
- **Alignment creates order.** Fewer alignment edges = calmer. Align text left for anything longer than two lines; centre only short, symmetrical compositions.
- **Rhythm.** Sections should vary in a pattern (wide/narrow, light/dark, image/text, dense/sparse) so the page has pace. A long page of identical sections is a list, not a composition.
- **Tension and balance.** Symmetry is calm and formal; asymmetry is dynamic. An asymmetric layout is balanced by weight: a large light area balances a small dark one.
- **Full-bleed vs contained.** Edge-to-edge elements feel immersive and bold; contained ones feel orderly. Mixing them on purpose (text on the grid, images bleeding off it) is a classic, strong move.
- **Density follows the task.** Dashboards and tools need density (compact rows, 13–14px UI text, tight spacing) to keep everything in view; marketing pages need air. Don't apply marketing spaciousness to a data table.

**Layout patterns to choose from, not default to.** Split (text one side, visual the other), stacked centre, asymmetric offset, bento/mosaic, index/list, overlapping layers, a single giant element, editorial columns, cards in a grid, timeline, table. Cards in a grid is the default answer to everything; use it when items really are parallel, comparable and independent, not as a generic container for any content.

## 4. Grid and space

- **Container**: pick a max width for the content (e.g. 1120–1280px for marketing, wider for apps) and side margins that grow with the viewport (`clamp(16px, 5vw, 64px)`).
- **Columns**: 12 for flexible marketing layouts, 4–6 for simpler ones, or a content-driven grid (`repeat(auto-fit, minmax(…))`). Text blocks rarely span the full width: measure limits them.
- **Spacing scale**: a base unit (4 or 8px) and a scale that grows (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). Use few values. Large gaps between sections (64–160px on desktop) are what make a page feel designed rather than stacked; spacing that is the same everywhere feels flat.
- **Optical adjustments** beat mathematical ones: icons next to text need nudging, round shapes need to overshoot, text in buttons needs slightly less top padding than bottom with some fonts, large display type needs negative tracking and tighter leading.
- **Vertical rhythm**: set line heights and gaps from the same scale so the page feels even.

## 5. Typography

Type does most of the design's work. A page with good type and nothing else looks designed; a page with weak type and lots of decoration does not.

**Choosing families**
- One family can carry a whole design if it has a range of weights. Two is common (display + text). Three needs a reason.
- Pair by **contrast with a shared quality**: a serif display with a sans text that has similar proportions; a geometric display with a humanist text. Avoid two fonts that are similar but not the same (two geometric sans) — it reads as a mistake.
- Match the category to the voice: grotesque/neo-grotesque = neutral, modern, institutional; geometric sans = clean, friendly, technical; humanist sans = warm, readable; transitional/old-style serif = literary, trustworthy; high-contrast didone = luxury, fashion; slab = sturdy, mechanical; mono = code, data, technical; display/script = personality, use sparingly.
- Use what the project has. Otherwise prefer a well-made free font (Google Fonts or system stacks) and load only the weights you use. A carefully set system font stack is better than a poorly chosen web font.
- Check the font actually has the weights, styles and characters (accents, numerals, symbols like €) the content needs.

**Setting the scale**
- Pick a ratio by mode: dense UI 1.125–1.2; reading 1.2–1.25; marketing 1.25–1.333 for text levels with a big jump to display (often 3–5× body).
- Body size: 16–18px for reading, 14–16 for UI, 13–14 for dense tools.
- Fluid sizing for display text so it scales with the viewport: `font-size: clamp(2.5rem, 1.6rem + 4vw, 5rem)`.

**Fine-tuning by size**
- Large text: tighter leading (1.0–1.15) and slightly negative tracking (-0.01 to -0.03em). Small text: looser leading (1.5–1.6) and neutral or slightly positive tracking.
- Uppercase labels need positive tracking (+0.04 to +0.1em) and a smaller size.
- Weight contrast carries hierarchy as much as size: pair a heavy display with a regular body, not medium with regular.
- `text-wrap: balance` for headings (no orphans), `text-wrap: pretty` for paragraphs. Use `font-variant-numeric: tabular-nums` in tables and prices so digits line up.
- Measure: 45–75 characters (`max-width: 65ch` on paragraphs).
- Use real typographic characters: curly quotes, en/em dashes, ×, →, non-breaking spaces between number and unit.

## 6. Colour

**Think in roles and proportions, not swatches.** A palette is: ground, surface(s), ink (2–3 levels: primary text, secondary, muted), border, accent (1, sometimes 2), and signals (success, warning, danger, info). Assign each a job. Then decide proportions: ground and neutrals carry the page (70–90%); the accent is rare (under 5–10%), which is exactly what gives it power. An accent used everywhere stops being an accent.

**Build palettes in oklch.** OKLCH is perceptually uniform: equal changes in L look equally lighter, so you can build steps and states predictably.
- Pick the brand/accent hue (H) and chroma (C).
- Tint the neutrals toward the brand hue with very low chroma (0.005–0.02). Pure grey (chroma 0) looks dead next to colour; tinted neutrals look intentional.
- Generate steps by changing L; reduce C near very light and very dark ends (high chroma at extreme lightness falls out of gamut and looks garish).
- Hover/active states: shift L by ~0.05–0.08 (`oklch(from var(--accent) calc(l - 0.06) c h)`) instead of picking new colours.

**Temperature and mood.** Warm neutrals (hue ~60–90, cream, sand) feel human and soft; cool neutrals (~240–260) feel technical and crisp. Saturation signals energy; muted palettes signal calm or premium. Dark themes are not inverted light themes: surfaces get *lighter* as they rise (elevation), text is off-white (L ~0.93–0.97, not pure white), accents usually need more lightness and less chroma.

**Contrast.** Check every text/background pair (target 4.5:1 body, 3:1 large/UI). Secondary grey text on a tinted surface is the most common failure. Coloured text on coloured backgrounds needs explicit checking.

**Gradients** are fine when chosen: interpolate in oklch (`linear-gradient(in oklch, …)`) to avoid muddy grey middles; keep hue shifts small for subtlety, or go bold on purpose. Gradients as atmosphere (soft radial glows behind content) need restraint: one or two, low opacity.

## 7. Shape, depth and material

- **Radius is a personality dial**: 0 = precise, editorial, technical; 4–8 = neutral, professional; 12–24 = friendly, soft; full pills = playful or app-like. Pick a logic and keep it. Nested radii must be concentric: inner radius = outer radius − padding.
- **Separating layers** — pick one primary method and stick to it:
  - Space alone (calmest, most editorial).
  - Tonal surfaces (a slightly different background; calm and modern).
  - Borders (precise, dense UIs; use translucent borders, e.g. `color-mix(in oklch, var(--ink) 12%, transparent)`, so they adapt to any surface).
  - Shadows (physical, tactile). Real shadows are layered (a tight dark one for contact + a wide soft one for ambient light), offset downward, and tinted with the background's hue rather than pure black. One elevation scale (e.g. 3 levels) for the whole design.
- **Material effects** (glass/blur, grain, inner highlights, gloss) belong to the idea or not at all. Glass needs something colourful behind it to read and a solid fallback; grain needs to stay subtle (opacity 3–8%).
- **Lines** are a strong graphic tool: hairline rules for editorial order, thick bars for emphasis. Keep weights consistent (1px and maybe one heavy).

## 8. Imagery and graphics

- Real photography beats illustration beats stock beats nothing — when it's relevant. A strong single image is better than many weak ones.
- Crop with intent: tight crops feel intimate and energetic; wide crops feel calm and contextual. Let images bleed off the edge for scale.
- Unify mixed images with one treatment (same aspect ratio, same colour grade, duotone, consistent rounding).
- Text on images needs a guaranteed contrast plan: a scrim gradient, a solid panel, or an image area kept quiet.
- When there are no images, don't fake them with grey boxes or random gradients. Use typography, a drawn graphic in one consistent style (see `drawing.md`), real UI rendered in HTML, data visualised, or an honest, labelled placeholder with the right aspect ratio.
- Icons: one set, one stroke width, one size grid, one corner style. Icons support labels; they rarely replace them.

## 9. Motion

Animate only when motion explains something (where an element came from, what changed, what is loading, what responds to the user) or when the brief is "experience". Default choices:
- Durations: 120–200ms for small UI feedback, 200–350ms for panels and overlays, up to 500–800ms for large page-level transitions. Exits are faster than entrances.
- Easing: ease-out for entering things (fast start, gentle stop), ease-in-out for moving between positions, never linear for UI (except for spinners and progress bars).
- Animate `transform` and `opacity` (cheap); avoid animating layout properties.
- Scroll-linked effects: subtle, few, and never blocking reading.
- Always provide the `prefers-reduced-motion: reduce` version (remove movement, keep fades or nothing).

## 10. The detail layer

Details are what separate "fine" from "designed". Cover the ones that apply:
- Selection colour (`::selection`), caret colour, accent colour for native controls, scrollbar colours where visible.
- Focus rings that match the design (offset outline in the accent colour), not the browser default or none.
- Link styling: underline offset and thickness (`text-underline-offset: .2em; text-decoration-thickness: 1px`), hover change.
- Hover, active (pressed), disabled, loading, empty and error states for every interactive component.
- Numbers: tabular figures in tables; currency and units formatted consistently.
- Favicon, `theme-color`, `color-scheme` for proper scrollbars and form controls in dark mode.
- Images with `aspect-ratio` and `object-fit` so nothing jumps while loading.
- Hairline separators, small icon alignments (optical centre), consistent ellipsis on truncated text.

## 11. Generic defaults and how to escape them

Some outcomes appear whenever a design is not really decided. None of them is forbidden; each is a warning sign if it arrived without a reason. Name the one your brief is most at risk of, and decide consciously.

| Default | Symptom | What a decision looks like instead |
|---|---|---|
| The SaaS kit | Centered hero + gradient blob + 3 icon feature cards + logo strip + testimonial cards + CTA band | Sections chosen from the argument; layouts varied by content; one signature device |
| Purple-blue gradient on white or dark | Indigo/violet accent with a glow, because "tech" | Colour drawn from the subject or brand; accent rare |
| Everything centred | Every section centred and the same width | Left-aligned reading structure; centre only short statements |
| Card soup | Every piece of content in a rounded, shadowed box | Separation by space and type; cards only for real, parallel objects |
| Uniform spacing | Same gap everywhere | Tight within groups, generous between sections |
| Timid type | Display only ~2× body, one weight | Decisive scale jump, weight contrast |
| Decoration as filler | Floating blobs, random emoji/icons, badges on everything | Every graphic has a job and one language |
| Fake numbers | "10,000+ happy users" with no source | Real proof or none |
| The trendy kit | Glass everywhere, bento grid for everything, grain for no reason | The effect earns its place by the idea |

Also recognise the opposite failure: overdesign. Too many ideas, effects, typefaces and colours at once. Senior work usually has **one** strong idea, executed consistently, with everything else quiet. Before finishing, remove one thing.

## 12. Working inside an existing system

When the project has a design system, brand guide, component library or framework (Tailwind theme, CSS variables, MUI/Chakra theme, a Figma library):
- Its tokens, components and conventions win. Read them before deciding. Your job is to find the best design *within* them.
- Extend instead of fork: if you need a new value, add it to the token set in the same naming style.
- Match the existing level of density, radius, and expression, even if you would choose differently on a blank page. Mention improvements separately instead of silently changing the system.
- A redesign request replaces the system on purpose; a refinement request preserves it. Ask yourself which one you have.