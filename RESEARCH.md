# Designer Sense research and change log

Version 0.4.0 · 2026-11-25

## Research basis

This release incorporates:
1. The original Designer Sense research and skill architecture.
2. The user's supplied `findings.md` (2026-11-25).
3. The user's supplied Claude-generated `designer-sense123.zip`, including its `SKILL.md`, five reference documents, and `scripts/shoot.py`.
4. The previously prepared Designer Sense package, including its evidence-boundary guidance, critique rubric, test protocol, paired HTML fixtures, and limitations report.
5. The installed Figma skills inspected in this environment: `figma-design-to-code`, `figma-generate-design`, `figma-generate-library`, and `figma-use`.

## Findings from the supplied research

The supplied findings identify useful strengths in several specialist approaches:

- **hallmark:** fixed floor rules, explicit decision block, mirror test, and signature move. Its dealt theme catalogue and restrictive taste bans are not appropriate as a general design skill.
- **Anthropic frontend-design:** plan before code, reason about palette/type/wireframe, recognize AI-default looks, and concentrate boldness. It needs deeper analysis, drawing, and critique.
- **taste-skill:** treats a page as an argument, uses a competitor/swap test, and applies repeated screenshot critique. Its house style and runtime assumptions should not become mandatory.
- **ui-ux-pro-max:** prioritizes rule groups, layered tokens, and design dials. Catalogue lookup and library defaults cannot replace design reasoning.
- **emil-design-eng / animate / choreograph:** useful motion sequencing and implementation choices, but motion-only.
- **apple-design:** strong material and scroll-edge techniques, but intentionally aesthetic-specific.
- **break-ui:** worst-case data and failure-signature testing. This is a valuable robustness pass, not a complete design process.
- **modern-web-guidance / paulirish modern-css:** deep modern CSS recipes, but technology capability does not decide what a design should be or why.
- **impeccable:** useful modes, preservation-vs-redesign distinction, critique agents, heuristics, and interaction craft.
- **Vercel Web Interface Guidelines:** practical craft checks such as layered shadows, concentric radii, hue-tinted borders/shadows, contrast, and avoiding `transition: all`.
- **OneRedOak design-review:** phased multi-viewport live review and severity ordering.
- **SVG-focused skills:** useful path construction and render/inspect/fix loops, but too narrow to supply the overall design process.

The supplied gap statement is adopted as the core product thesis: read an existing design as a system; decide in a style-neutral way; select modern CSS by intent; connect drawing technique to design judgment; and critique rendered output without assuming one special toolchain.

## Installed skills inspected

- `figma-design-to-code`: strong screenshot-as-target workflow, high-fidelity design context, stack adaptation, asset reuse, and geometry verification. Figma-specific.
- `figma-generate-design`: strong design-system discovery, components, variables, Code Connect, editable layers, and composed views. Figma-specific.
- `figma-generate-library`: useful design-system foundations, tokens, variants, and reusable components. Library-oriented.
- `figma-use`: detailed Plugin API, mutation, typography, variables, and validation instructions. Tool-specific.

These skills are valuable specialists. Designer Sense should provide the cross-cutting design judgment, not duplicate their tool-specific workflows.

## What changed in v0.2.0

### Adopted from the Claude package

- Four practical experience modes: operate, read, persuade, experience.
- Subject inventory, visual-device selection, and the swap test to make concepts specific without forcing decorative gimmicks.
- A stronger order of decisions: purpose → idea → composition → system → details.
- Deep reference material for typography, colour, spacing, shape/material, imagery, motion, and the detail layer.
- Design-first drawing workflow: concept → silhouette → construction → tone → line/detail → integration.
- Detailed SVG construction, filters, patterns, masks, strokes, path commands, theming, and accessibility.
- A standalone multi-viewport screenshot helper.
- Robustness checks for worst-case content, 320px layouts, 200% zoom, long translations, keyboard use, and missing content.
- Explicit preservation-versus-redesign reasoning.

### Retained and strengthened from the previous Designer Sense package

- Evidence boundaries: distinguish observed facts from inferences and estimates.
- Reference fidelity: recreate first; do not silently replace the reference with personal taste.
- Existing project and design-system inspection before edits.
- CSS/SVG/media selection by need rather than novelty.
- A weighted critique rubric and repeatable with/without-skill test cases.
- Honest reporting: source-level inspection is not browser-rendered validation.
- Cross-style quality floor for accessibility, responsiveness, semantics, and performance.

### Deliberately not adopted as hard rules

- Any fixed theme/style catalogue or default aesthetic.
- Taste bans that prohibit glass, gradients, illustration, cards, or other techniques categorically.
- Framework, CLI, runtime, or browser automation dependencies as mandatory prerequisites.
- Hard-coded claims that every modern CSS feature is supported everywhere. Compatibility is time-sensitive and must be checked against the project's target browsers.

## Browser support note

The supplied findings include a web-features 3.47 snapshot dated 2026-11-19. It categorizes features into broadly safe, newly Baseline with fallback, and partial/enhancement-only groups. This snapshot is useful as a research input, not a permanent truth. The skill therefore requires checking current compatibility against the project's browser matrix before relying on a newer feature. Use progressive enhancement and preserve a complete baseline experience.

## Research references

- Anthropic frontend-design: https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design
- Anthropic frontend aesthetics cookbook: https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics
- Impeccable: https://github.com/pbakaus/impeccable
- UI Craft: https://github.com/educlopez/ui-craft
- ReadyDesign-Skill: https://github.com/ZethRise/ReadyDesign-Skill
- Vercel Web Interface Guidelines: https://github.com/vercel-labs/web-interface-guidelines
- MDN container queries: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries
- MDN SVG filters: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

## Supplied findings document

The supplied findings document is retained verbatim in `references/external-findings.md` for traceability.


## Additional research reviewed for v0.4.0

### Core idea: design sense as educated intuition

The user's supplied LinkedIn post frames design sense as intuition developed through design education, immersion, and the ability to explain why a choice serves a purpose. This reinforces the skill's central rule that design decisions should not be arbitrary. The post is user-supplied text, not independently attributed or verified here.

### Radilson Gomes — “Beyond the Surface: Activating Your Design Sense in UI Design” (Medium, 2023)

Useful ideas:
- Curiosity: investigate how a small design detail was made and why it works.
- Repertoire: collect references from both digital and non-digital environments, annotated with what makes them effective.
- Learn by copying: reproduce a small element to understand technique and construction, then create an adapted, original result.
- Learn conventions before breaking them; interaction expectations and platform patterns matter.
- Aesthetic craft and usability should reinforce each other.

Adopted as an explicit notice → collect → deconstruct → reproduce-to-learn → adapt → judge/reflection loop. Reproduction is bounded as a learning exercise and does not authorize copying protected expression.

### Jakub — “Is Design Sense Learned or Born?” (rausr.com, 4 May 2026)

The article describes design sense as a bundle of perception, memory, judgment, pattern recognition, cultural reference, restraint, speed, taste, and the ability to solve briefs under pressure. It distinguishes predisposition from trainable habits and argues that deliberate practice, feedback, context, and reliability matter. It also stresses that design quality is hard to score independently of the audience, brief, market, and evaluator.

Adopted with care:
- The skill treats design sense as improvable through deliberate observation, comparison, critique, and repetition.
- It avoids claiming all aesthetic judgment is objective or that practice guarantees identical outcomes.
- Important decisions include rationale, trade-offs, and confidence/evidence type.

### Amaneno — Note article resolved from the supplied URL

The supplied URL resolves to “3 Reasons Why Designs from Agencies Miss the Mark” (published 20 April 2026), not a general design-sense essay. It argues for defining (1) what artifact/service is being requested, (2) what success looks like in concrete terms, and (3) who makes the final decision. The key takeaway is to translate vague feedback such as “the vibe is off” into observable, actionable conditions.

Adopted conceptually in the brief and rationale guidance: identify the requested artifact, success criteria, decision authority where relevant, and express critique as observations plus specific fixes.

### Owl-Listener — Designer Skills Pack

Repository inspected: https://github.com/Owl-Listener/designer-skills

The repository describes a broad design-practice suite (research, design systems, UX strategy, UI design, interaction design, prototyping/testing, design operations, designer toolkit, and visual critique). Relevant skill files inspected include:
- `ui-design/skills/visual-hierarchy/SKILL.md`
- `ui-design/skills/color-system/SKILL.md`
- `ui-design/skills/typography-scale/SKILL.md`
- `visual-critique/skills/critique-composition/SKILL.md`
- `visual-critique/skills/critique-affordance/SKILL.md`
- `visual-critique/skills/critique-information-density/SKILL.md`
- `designer-toolkit/skills/design-rationale/SKILL.md`
- `ux-strategy/skills/design-principles/SKILL.md`
- `prototyping-testing/skills/parallel-concepts/SKILL.md`

Adopted:
- explicit lenses for hierarchy, composition, affordance, and information density;
- neutral observation → problem interpretation → actionable fix;
- rationale that records decision, context, alternatives/evidence, reasoning, trade-offs, and validation;
- optional parallel concept exploration when an early direction is uncertain.

Not adopted wholesale: this repository is a large modular catalogue. Designer Sense remains a single cross-cutting skill and should delegate specialist tasks rather than duplicate research, design-system governance, UX strategy, or testing frameworks.

### Sources not fully retrievable

- The supplied Skills Directory URL for `hamza-ali-shahjahan-design-sense` did not resolve in the browser. A similarly named search result for `simhacker-design-sense` was a different skill/author and was not treated as the requested source.
- The supplied note URL itself resolved to the Amaneno agency-design article above; the search engine also surfaced a different Amaneno article title. The supplied URL is treated as the user's intended source.