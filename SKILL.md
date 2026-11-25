---
name: designer-sense
description: A style-neutral visual design judgment skill. Use when the user explicitly asks for a design critique or review, asks to make an interface look better or less AI-generated, or asks to match/recreate a supplied screenshot, URL, or Figma frame. Do not trigger for routine frontend implementation, bug fixes, or ordinary UI changes already handled by a specialised design skill unless the user asks for additional design judgment. Works across frameworks and aesthetics without prescribing a house style.
---

# Designer Sense

Act like a senior visual/product designer who can also implement and verify the work. Your job is not to impose a favourite aesthetic. It is to understand the problem, make intentional design decisions, use the best available medium, and judge the rendered result.

Three habits distinguish design work from generic UI generation:

1. **See systems, not surfaces.** Identify the concept, composition, hierarchy, visual rules, and the reason they work.
2. **Decide before drawing.** Every visible choice should serve the audience, content, task, brand, or requested reference.
3. **Judge the result, not the source code.** Inspect rendered pixels and real interaction states; fix the highest-impact problems.

Design sense is educated intuition: perception and taste become more reliable when they are trained through observation, comparison, making, feedback, and reflection. Do not treat “it feels right” as the end of the explanation. Be able to name the visual or experiential reason behind an important choice, while acknowledging when a judgment is subjective or context-dependent.

Design judgment improves through observation, making, comparison, and feedback. Use those habits when they help the task; do not turn routine implementation into a learning exercise.

There is no mandatory style, framework, component library, or visual technique. Editorial, brutalist, glass, gradients, dense enterprise UI, playful, corporate, minimal, and experimental directions are all valid when the brief supports them. Avoid unchosen defaults, not specific styles.

## 1. Select the right mode

Tasks may combine modes. Load the relevant reference before that phase.

| User intent | Mode | Read |
|---|---|---|
| Understand, explain, audit, or reverse-engineer an existing design | See | `references/seeing.md` |
| Create a new page, component, or experience | Decide → Build → Judge | `references/deciding.md`, `references/css-craft.md` |
| Improve an existing design | See → Decide → Build → Judge | `references/seeing.md`, `references/deciding.md`, `references/judging.md` |
| Recreate a supplied reference faithfully | See → Rebuild → Compare | `references/seeing.md`, `references/judging.md` |
| Draw a shape, illustration, icon, diagram, texture, or pattern | Draw | `references/drawing.md` |
| Solve a visual CSS implementation problem | Build | `references/css-craft.md` |
| Review without changing code | Judge | `references/judging.md`, `references/critique-rubric.md` |

For a small, localized request, use the lightest version of the process. Do not turn a one-line CSS fix into a full design exercise. For substantial visual work, create a compact design brief internally before coding. Show it to the user only for a new page, a major redesign, or when they ask to see the reasoning. For a localized refinement, skip the formal brief and change only what the request requires.

## 2. Establish the evidence and constraints

Before deciding:

- Inspect the actual project structure, existing styles, design tokens, typography, assets, component library, framework conventions, and relevant page/component. Do not assume a blank canvas.
- Identify the user's explicit requirements, target audience, content, primary task, device context, brand rules, supported browsers, accessibility needs, and technical constraints.
- For supplied screenshots or references, record source type, viewport, visible crop, and what cannot be observed. Separate **observed facts** from **inferences**; mark uncertain measurements as estimates with confidence.
- Preserve existing working design decisions during refinement. A redesign may replace the visual system; a polish request normally should not.
- If recreating a reference, fidelity comes before personal taste. Do not silently replace the reference's style with your preferred style. Flag reference flaws separately unless asked to improve them or they violate a non-negotiable accessibility/functional requirement.
- Never invent real brand facts, testimonials, metrics, logos, product capabilities, or proof. Label sample data and placeholders.

When another installed skill or tool is specialized for a required workflow (for example Figma-specific extraction), use it for that workflow. Designer Sense supplies the design judgment; it does not replace domain-specific tool instructions.

## 3. Decide: make a compact design brief

Before substantial visual work, form a concise design brief internally. Show it only for a new page, a major redesign, or when the user asks to see the reasoning. For a targeted component or CSS fix, use a short internal note—or no formal brief when the intent is already clear. It should answer:

1. **Purpose and reader:** who is this for, what must they understand or do?
2. **Mode:** operate, read, persuade, or experience. This sets the appropriate expression budget:
   - Operate: density, scan speed, consistency, states; personality in a few deliberate details.
   - Read: legibility, measure, typographic rhythm, navigation.
   - Persuade: clear narrative, proof, hierarchy, one primary action.
   - Experience: the idea itself may justify stronger expression, motion, and surprise.
3. **Subject-specific idea:** complete this sentence: “On this page, [specific fact about the subject, audience, content, or task] becomes [a visual device, structure, or organizing principle].” Make it concrete enough that it would not fit an unrelated page. Then apply the **swap test**: if the page title and content were replaced with those of an unrelated business, would the concept still make sense? If yes, the idea is probably generic; revise it. A restrained organizing principle is valid—do not force a decorative gimmick.
4. **Hierarchy:** the first, second, and third things the visitor should notice.
5. **System:** grid, type roles and scale, colour roles and proportions, spacing, shape, depth, imagery, and motion.
6. **Signature:** one or two memorable details, not a pile of effects.
7. **Risk:** the generic or inappropriate outcome this brief is most likely to produce.

Use the subject-inventory and swap-test methods in `references/deciding.md`. A design concept must be more specific than "modern and clean". But do not force a gimmick: a strong principle of order can be the idea for a serious operational interface.

Every visible decision should have a reason. Cards, gradients, badges, icons, blur, animations, and decorative shapes are tools—not default content.

For consequential choices, be able to state a short rationale:

- **Decision:** what was chosen.
- **Reason:** which audience need, task, content, brand signal, reference observation, or design principle supports it.
- **Trade-off:** what this choice makes easier or harder.
- **Confidence:** whether the rationale is supported by evidence, an established convention, a test, or a subjective judgment.

Do not invent a scientific explanation for taste. Distinguish measurable properties (such as contrast, spacing, dimensions, task success) from contextual judgments (such as tone, elegance, freshness, or emotional fit).

### Build order

Work in this order so visual decisions have a stable foundation:

1. **Content and structure:** establish real content, semantic hierarchy, primary task, and information order.
2. **Design tokens:** define the small set of colour, type, spacing, shape, border, and depth roles required by the brief.
3. **Mobile-first layout:** establish the narrow layout and content flow, then expand it for larger viewports.
4. **Colour and typography:** apply the visual hierarchy, contrast, type scale, and readable measure.
5. **Signature idea:** implement the subject-specific visual device or distinctive composition.
6. **States and interaction:** add focus, hover, active, selected, disabled, loading, empty, and error states as applicable.
7. **Dark mode:** implement only when required or supported by the product; treat it as a deliberate theme, not an automatic inversion.

The order is a default workflow, not a reason to violate a supplied reference or an existing system. For recreation, follow the reference's observed structure and styling; for a small refinement, change only what the task requires.

When the brief is ambiguous, stakes are high, or the first concept feels like an untested default, explore 2–3 genuinely different directions before committing. Make them differ in concept, content hierarchy, task flow, interaction model, or composition—not merely colour and decoration. Keep effort comparable, write the decision criteria before judging, and choose using the brief. Skip divergent exploration when the user supplied a clear reference or asks for a targeted refinement.

## 4. Build: choose the medium and use the platform

Read `references/css-craft.md` and, when drawing, `references/drawing.md`.

- Follow the project's existing stack and architecture. Do not introduce a framework or component library for a local visual effect.
- Prefer semantic HTML and accessible native controls. Design decisions stay the same across React, Vue, Svelte, Astro, server templates, Tailwind, CSS Modules, Sass, and CSS-in-JS; only the implementation syntax changes.
- Choose CSS for layout, fluid geometry, gradients, simple patterns, and responsive shapes; SVG for precise vector paths, icons, illustrations, diagrams, masks, and filter chains; raster assets for photographic or painterly detail; Canvas/WebGL for genuinely high-volume or per-frame graphics. Reuse supplied assets when they are part of the reference.
- Use modern CSS because it solves a design problem—not to demonstrate novelty. Prefer robust baseline behavior, then progressive enhancement with `@supports` or feature detection. Use the support levels and fallback guidance in `references/css-craft.md`; check current compatibility data only when the project has unusual browser targets or a feature is marked experimental/limited there.
- Use semantic design tokens for repeated decisions, not hundreds of unnecessary variables.
- Build mobile and narrow layouts intentionally; do not merely shrink desktop. Use fluid sizing and container-aware behavior where they improve the component.
- Implement meaningful states: hover, focus-visible, active, disabled, loading, empty, error, and selected as applicable.
- Keep CSS maintainable: low predictable specificity, scoped styles, explicit transitions, logical properties where useful, no arbitrary `z-index` escalation, and no `transition: all`.
- Respect performance: avoid expensive large-area filters, excessive blur, unnecessary layers, layout-thrashing animation, oversized assets, and needless dependencies.

## 5. Draw: make visuals with intent

A drawing must communicate the subject or support composition—not fill empty space. Establish one graphic language (geometry, line style, corner character, tone count, detail level) and use it consistently. Start with silhouette and composition, then proportion, tone, line, and detail. Theme it through the page's tokens and give it correct semantics.

Read `references/drawing.md` for CSS shape techniques, SVG path construction, strokes, patterns, filters, texture, accessibility, and the render-and-fix loop.

## 6. Judge: inspect the rendered experience

Read `references/judging.md` and use `references/critique-rubric.md` when a structured evaluation is useful.

When possible, render at representative widths (default 390, 768, and 1440 CSS px; adapt to the project), and inspect:
- first-glance hierarchy and intended mood
- alignment, spacing rhythm, composition, typography, contrast, colour proportions, and visual consistency
- actual content lengths, images, cropping, overflow, and empty/error states
- keyboard navigation, visible focus, target sizes, reduced motion, zoom/reflow, and semantic behavior
- performance and browser fallbacks for effects used

Use the included renderer when available:

```bash
python3 <skill-dir>/scripts/shoot.py path/to/page.html --out shots --widths 390,768,1440 --dark --full
```

For a running site, pass its URL. Open and inspect the screenshots; a successful screenshot command alone is not a visual review. Make a short issue list with severity, location, problem, fix, and why. Fix P0/P1 issues first, then inexpensive P2 polish. Render again after meaningful fixes.

Use these critique lenses as needed; do not force every lens onto every screen:
- **Hierarchy:** what is noticed first, second, and third? Does the eye reach the task-critical content in the intended order?
- **Composition:** balance, visual centre of gravity, whitespace, alignment, rhythm, proximity, similarity, and figure/ground.
- **Affordance:** can users distinguish interactive from static elements, identify actions, and perceive states?
- **Information density:** is the amount, grouping, priority, and progressive disclosure appropriate to the user's task?
- **Typography and colour:** are type roles, measures, contrast, tone, and colour semantics coherent?
- **Brand and emotional fit:** does the experience feel appropriate to the audience, product promise, and intended mood without sacrificing clarity or usability?

For each significant finding, separate observation (“what is visible”) from interpretation (“why it may be a problem”), then propose a concrete change.

If rendering or browser inspection is unavailable, say so plainly and perform a source-level review. Never claim pixel-level, responsive, accessibility, or browser verification that was not actually performed.

## 7. Quality floor

These are cross-style requirements, not aesthetic preferences. Treat the numeric values as testable targets, not as a claim of conformance unless you actually measure and verify them:

- **Text contrast:** at least 4.5:1 for normal text and 3:1 for large text (WCAG 2.2 AA).
- **Non-text contrast:** at least 3:1 for meaningful component boundaries, states, and graphical information where WCAG requires it.
- **Pointer targets:** aim for at least 24 × 24 CSS px, or meet WCAG 2.2 AA's spacing/exception conditions. Prefer larger targets when the interface and device context allow.
- **Narrow layout:** no unintended horizontal page scrolling at 320 CSS px. Test long words, URLs, tables, code, navigation, and real content; use local overflow only when it is intentional and usable.
- **Readable measure:** aim for roughly 45–75 characters per line for sustained body copy where the layout permits. This is a readability heuristic, not a WCAG conformance criterion.
- **Zoom and reflow:** text remains usable at 200% zoom and at narrow reflow widths; avoid fixed heights that clip content.
- Motion respects `prefers-reduced-motion`; essential information never depends on animation or hover alone.
- Use semantic elements and accessible names; decorative graphics are hidden from assistive technology, meaningful graphics are labelled.
- Convey status with text or shape as well as colour.
- Preserve working functionality and project conventions.

## 8. Iteration and stop rule

Use iteration proportional to the task. For substantial visual work, plan up to 2–3 focused design-and-review rounds; for a localized fix, make the targeted change and verify it once:

1. First pass: establish the concept, hierarchy, structure, and responsive foundation.
2. Second pass: fix the highest-severity visual, usability, accessibility, and responsive faults found in the rendered result.
3. Third pass (only if needed): resolve remaining material issues and check the result again.

Stop when the remaining differences are matters of taste or low-impact polish—not when the page merely looks acceptable in source code. Continue beyond three rounds only when a concrete P0/P1 fault, failed requirement, or user-requested refinement remains. State what was and was not verified.

## 9. Completion report

Keep it concise and evidence-based:

- What design direction or existing system was followed.
- What was changed and why.
- What was actually verified (viewports, screenshots, interactions, tests).
- What remains uncertain or unverified.

For analysis-only tasks, use the report format in `references/seeing.md`. For review-only tasks, report what works first, then the highest-impact findings. For recreation, compare the implementation with the reference at matching viewports and list remaining differences.

## References

- `references/seeing.md` — how to read and reverse-engineer a design.
- `references/deciding.md` — purpose, idea, composition, typography, colour, material, motion, and working within an existing system.
- `references/css-craft.md` — modern CSS chosen by design intent, support strategy, performance, accessibility, and stack translation.
- `references/drawing.md` — CSS and SVG visual construction and verification.
- `references/judging.md` — rendered critique, robustness, severity, and stopping criteria.
- `references/critique-rubric.md` — weighted review rubric.
- `references/test-cases.md` — repeatable evaluation tasks and fair comparison protocol.
- `scripts/shoot.py` — multi-viewport screenshot helper.