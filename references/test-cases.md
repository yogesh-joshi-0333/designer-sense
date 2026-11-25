# Designer Sense evaluation tasks

Use these repeatable tasks to evaluate whether the skill improves design reasoning and implementation decisions. Run each task once with the skill and once without it, using the same model, project context, assets, constraints, and time/tool budget. Save prompts, generated diffs, screenshots, and scores.

## Task A — Distinctive marketing page

**Prompt:** Design a responsive landing page for a small independent climate-data observatory. Its audience is municipal planners and journalists. It publishes trustworthy local heat-risk data. The page needs a clear explanation, a live-data preview, methodology credibility, and a request-access action. No brand system or visual style is supplied. Avoid inventing unsupported statistics.

**Tests:** Contextual visual direction, original composition, content hierarchy, restrained data visualization, typography, CSS/SVG visual storytelling, responsive behavior.

## Task B — Dense operational dashboard

**Prompt:** Redesign an existing operational dashboard for a warehouse supervisor who checks it repeatedly during a shift. Show urgent exceptions, throughput, delayed orders, and equipment status. The interface must work on a 1280px desktop and a 390px mobile screen. Prioritize scan speed and action clarity over marketing aesthetics. Use realistic sample data and explicit status labels.

**Tests:** Information architecture, density, grouping, hierarchy, accessible status, responsive transformation, data readability, useful states. Penalize a dashboard made from identical decorative cards.

## Task C — Reference analysis and recreation

**Prompt:** Given a screenshot of an editorial culture magazine homepage, explain its visual concept, hierarchy, grid, typography roles, image treatment, and likely construction techniques. Then recreate the visible first viewport in the existing project without flattening it into an image. Preserve supplied assets and match the screenshot at the same viewport.

**Tests:** Observation versus inference, visual reverse engineering, exact asset handling, geometry, typography, fidelity, and honest verification.

## Evaluation protocol

1. Use a fresh context for each run to avoid cross-contamination.
2. Do not provide the skill's design thesis or tokens to the baseline run.
3. Keep the same task prompt and project snapshot for both runs.
4. Record planning quality, implementation quality, defects, and verification evidence separately.
5. Score both outputs with `critique-rubric.md`; ideally use a blinded reviewer who does not know which run used the skill.
6. Compare rendered screenshots at identical viewport sizes. Do not infer visual superiority from code length or descriptive confidence.
7. Run at least two independent repetitions per task before making strong claims.

## Known limitation of this packaged evaluation

If no browser automation or screenshot renderer is available, perform a source-level review only and mark visual comparison as **not run**. Do not present a hypothetical or hand-authored comparison as an empirical browser test.