# designer-sense: research findings (2026-11-25)

## 1. Installed design skills

| Skill | Good at | Tied to | Missing for our goal |
|---|---|---|---|
| hallmark | Fixed floor rules, a "Picks block" listing every decision before code, mirror test, signature move, grain recipe | ~100 dealt themes, Node scripts, strong taste bans (no eyebrows, no drawn illustration) | Analysis of a given design, modern CSS, drawing (banned) |
| frontend-design (Anthropic) | Plan (4–6 colours, type, ASCII wireframe), then "would a similar prompt land here?", 5 named AI-default looks, "spend boldness in one place" | Light taste bans | Analysis, CSS technique, drawing; critique is one line |
| taste-skill | Page as an argument, the "[X] becomes [device]" sentence plus competitor test, 14-pass screenshot critique, colour proportion (ground 70–90%, accent <5%) | Node 22 + Chrome scripts, a no-ornament house style, marketing pages | Analysis of a given design, deep CSS, drawing technique |
| ui-ux-pro-max | Priority order of rule groups, three-layer tokens, design dials | CSV lookup of 79 styles / 192 palettes, shadcn + Tailwind, image APIs | Reasoning (it looks designs up), CSS depth, analysis |
| emil-design-eng | Animation decision order, clip-path reveals, @starting-style, Before/After/Why table | React + Motion; motion only | Static design, colour, layout, drawing |
| apple-design | Materials as hierarchy, scroll-edge masks, size-specific tracking | Apple aesthetic | Layout, colour, CSS, analysis |
| animate / choreograph | Cheapest tool that works, no invented values, extend existing tokens | Motion library | Everything outside motion |
| break-ui | Worst-case data; failure signature → cause → fix | Component fixtures | It is QA only (reused here as the robustness pass) |
| tailwind-design-system, daisyui, pick-ui-library | Semantic oklch roles | Tailwind / daisyUI / React | Design judgement |
| modern-web-guidance (Chrome team) | Deepest modern CSS with fallbacks: anchor, view transitions, scroll-driven, :has, container queries | npx and network; recipe per use case | Any design judgement ("how", never "what/why") |

## 2. GitHub and web

| Source | Good at | Tied to / misses |
|---|---|---|
| impeccable (pbakaus) | 4 modes (Persuade/Operate/Read/Experience), "refinement preserves, redesign replaces", two separate critique agents, Nielsen heuristics scored 0–4, craft floor (selection, caret, scrollbar) | Own CLI and detector, taste bans, almost no modern CSS, no drawing |
| Vercel Web Interface Guidelines | Layered shadows, concentric radii, hue-tinted borders and shadows, APCA, never `transition: all` | Checklist only, no process |
| paulirish modern-css | @layer, container queries, oklch, relative colour, anchor, view transitions, scroll timelines, Baseline checks | No design judgement |
| OneRedOak design-review | Phased live-page review at 1440/768/375, "problems over prescriptions", severity scale | Needs Playwright MCP; QA-style |
| superdesign | Numbered design iterations side by side | Tailwind CDN required; unmaintained |
| SVG skills (possumworx, tryopendata, dvy1987) | Render SVG → look → fix coordinates loop; path primitives | Narrow, no design reasoning |

## 3. The gap (what nobody does)

1. Read an existing design (screenshot, URL, code) and name its concept, its system (grid, type ratio, colour roles and proportions, spacing, radius and depth logic) and why it works, so the approach can be carried to new work.
2. A decision process that is style-neutral. Every taste skill decides by dealing from its own catalogue or banning looks; none can deliberately build glass, gradients or a dense dashboard when the brief asks for it.
3. Modern CSS chosen by design intent. The CSS skills have no intent; the design skills write 2018-era CSS.
4. Drawing technique (hand-built SVG paths, clip-path/shape(), masks, filter chains, texture) joined to design sense.
5. One critique loop that judges rendered pixels and needs no special tooling.

## 4. Browser support snapshot (web-features 3.47, 2026-11-19)

Safe everywhere: @layer, :has, container size queries + cqi, nesting, oklch, color-mix, light-dark, subgrid, trig functions, round/mod, text-wrap: balance, linear(), dvh/svh, :user-invalid, mask, clip-path (polygon/path), shape-outside.
Newly Baseline (use with a light fallback): relative colour, @property, popover, commandfor, same-document view transitions, scroll-driven animations (Firefox 159, Oct 2026), @starting-style, allow-discrete, @scope, shape(), container style queries, field-sizing, content-visibility, backdrop-filter, sibling-index().
Partial (enhancement only): anchor positioning (core in all 3, not Baseline yet), cross-document view transitions, text-wrap: pretty, text-box-trim, typed attr(), base-select, calc-size/interpolate-size, corner-shape, if(), @function, random(), scroll-state queries, ::scroll-marker, masonry/grid-lanes.