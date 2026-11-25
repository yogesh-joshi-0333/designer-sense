# Designer Sense

**A research-informed design-thinking skill for AI coding agents.**

Designer Sense helps an AI agent approach interface and visual work with the judgment of a thoughtful designer—not just the ability to generate markup and CSS. It teaches a repeatable process for understanding a brief, reading visual references, forming a concept, choosing an appropriate visual language, implementing it, and critically evaluating the rendered result.

It is deliberately **framework-independent, technology-independent, and style-neutral**. It does not force a house aesthetic, a component library, or a preferred stack.

> Good design is intentional. The agent should be able to explain what it chose, why that choice serves the task, what trade-off it creates, and how the result was evaluated.

## Why this skill exists

AI can produce interfaces quickly. Speed alone does not guarantee that an interface communicates clearly, fits its audience, feels coherent, or solves the right problem.

Designer Sense focuses on the part that is often missing: **design judgment**.

The skill treats design sense as educated intuition—intuition strengthened by observation, reference knowledge, practice, critique, and reflection. It asks the agent to reason about the purpose behind visual decisions instead of decorating a page with familiar patterns.

## Research and development

This skill was developed through iterative research and synthesis, rather than by copying a single prompt or visual template.

The research process included:

1. **Design practice and visual judgment** — examining how designers build taste, learn conventions, develop a reference repertoire, and explain design decisions.
2. **Existing agent skills** — reviewing approaches to frontend design, visual critique, design rationale, design systems, drawing, and implementation craft.
3. **Specialist design workflows** — inspecting relevant material on hierarchy, composition, typography, colour, affordance, information density, and parallel concept exploration.
4. **Implementation craft** — studying modern CSS and SVG techniques while keeping technology choices subordinate to design intent.
5. **Evaluation and robustness** — retaining repeatable test cases, screenshot-based inspection guidance, viewport checks, and explicit evidence boundaries.
6. **Iteration** — incorporating supplied research and a second independently generated skill package, then comparing overlaps, gaps, and unsuitable constraints before updating the skill.

### Research sources

The research notes document what was inspected, what was adopted, and what was deliberately excluded. Selected sources include:

- [Anthropic — Frontend Design skill](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design)
- [Anthropic — Frontend aesthetics cookbook](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics)
- [Impeccable](https://github.com/pbakaus/impeccable)
- [UI Craft](https://github.com/educlopez/ui-craft)
- [ReadyDesign-Skill](https://github.com/ZethRise/ReadyDesign-Skill)
- [Vercel — Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines)
- [Owl-Listener — Designer Skills Pack](https://github.com/Owl-Listener/designer-skills)
- [Beyond the Surface: Activating Your Design Sense in UI Design](https://medium.com/design-bootcamp/beyond-the-surface-activating-your-design-sense-in-ui-design-67e578d4ad58)
- [Is Design Sense Learned or Born?](https://rausr.com/blog/is-design-sense-learned-or-born/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [MDN — CSS Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries)
- [MDN — SVG Filter Element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter)

The full research log is in [RESEARCH.md](RESEARCH.md). It records source-specific findings, adoption decisions, and retrieval limitations. User-provided research notes are preserved separately in [references/external-findings.md](references/external-findings.md).

## The design process

The skill uses a flexible workflow. It selects the appropriate mode based on the task instead of forcing every request through every phase.

| Phase | Purpose |
|---|---|
| **See** | Understand the brief, audience, content, constraints, existing product, and visual references. |
| **Decide** | Establish the design thesis, concept, hierarchy, composition, and visual system. |
| **Build / Draw** | Implement the idea using the medium and techniques that best serve it. |
| **Judge** | Inspect rendered output, critique meaningful issues, and refine the result. |

### The Design Sense Loop

Design judgment develops through practice. The skill makes that practice explicit:

1. **Notice** — observe what attracts attention and what feels unresolved.
2. **Collect** — build a reference repertoire and record why examples work.
3. **Deconstruct** — identify the hierarchy, proportion, rhythm, typography, colour, material, and interaction choices behind the effect.
4. **Reproduce to learn** — recreate a small element when useful to understand its construction.
5. **Adapt** — apply the underlying principle to the current audience, task, brand, and constraints.
6. **Judge and reflect** — inspect the result, explain the outcome, and retain the learning.

This is a learning method, not a mandate to copy references or add unnecessary exercises to routine work.

## What makes it different

- **Intent before decoration:** every consequential visual decision should serve a purpose.
- **Evidence-aware reasoning:** distinguish what is observed from what is inferred or subjectively judged.
- **Style neutrality:** no fixed aesthetic, theme catalogue, or categorical ban on visual techniques.
- **Context preservation:** inspect the existing project and design system before changing them.
- **Reference fidelity:** recreate the supplied reference before introducing personal taste.
- **Conceptual exploration:** when the brief is uncertain, compare genuinely different directions—not superficial colour variations.
- **Technology follows intent:** use CSS, SVG, raster imagery, Canvas, or existing assets according to the design problem.
- **Rendered critique:** evaluate what users will actually see and interact with, not just source code.
- **Quality as a whole:** accessibility, responsiveness, semantics, performance, and maintainability are part of design quality.

## Installation

### Claude Code — project-local

Copy the extracted repository into your project's skills directory:

```bash
mkdir -p .claude/skills/designer-sense
cp -R ./* .claude/skills/designer-sense/
```

### Claude Code — personal

```bash
mkdir -p ~/.claude/skills/designer-sense
cp -R ./* ~/.claude/skills/designer-sense/
```

Then ask Claude Code to use `designer-sense` when designing, implementing, recreating, or reviewing an interface.

## Repository contents

The complete v0.4.0 source package—including `SKILL.md`, research notes, references, scripts, test fixtures, and validation report—is available as [designer-sense-v0.4.0.zip](designer-sense-v0.4.0.zip). Extract it to use the full skill.

## Evaluation and current limitations

The release includes paired HTML fixtures and a repeatable evaluation protocol, plus a screenshot helper for inspecting multiple viewport widths.

**Be precise about what has and has not been validated:** the current release has passed package-integrity, reference-path, and screenshot-script syntax checks. Earlier source-level reviews were not blind user studies or browser-rendered A/B experiments. A fresh controlled comparison of rendered outputs is still a planned validation step.

See [TEST-REPORT.md](TEST-REPORT.md) in the package for the exact validation status. Do not interpret the existence of test fixtures or a screenshot script as proof of visual superiority.

## Design philosophy

Designer Sense is not intended to make every interface look the same. It is intended to help an AI agent understand the problem, make deliberate design decisions, explain those decisions, and evaluate the result honestly.

**The goal is not more decoration. The goal is better design judgment.**

## Version

Current version: **0.4.0**
