# Designer Sense — evaluation report (v0.4.1)

## What was reviewed

This update was based on a direct review of the supplied Claude package:
- `SKILL.md`
- `references/seeing.md`
- `references/deciding.md`
- `references/css-craft.md`
- `references/drawing.md`
- `references/judging.md`
- `scripts/shoot.py`

It was compared against the previous Designer Sense package, including:
- existing `SKILL.md`
- `visual-analysis.md`
- `css-visual-toolkit.md`
- `critique-rubric.md`
- `test-cases.md`
- six paired HTML/CSS fixtures
- the previous `TEST-REPORT.md`

## Changes made

1. Replaced the shorter CSS visual-toolkit overview with a deeper CSS craft reference covering cascade architecture, tokens, grid, subgrid, container queries, fluid typography, OKLCH, interaction states, motion, support tiers, performance, accessibility, and stack translation.
2. Added detailed design decision knowledge: subject inventory, swap test, mode-specific expression budget, composition, type, colour, materials, imagery, motion, and detail craft.
3. Added a complete drawing reference covering CSS geometry, clip-path, masks, SVG paths, strokes, patterns, texture, filters, semantics, and render-and-fix.
4. Added a dedicated judging reference with glance/squint/geometry/type/colour/detail passes, worst-case content, severity ordering, and stopping criteria.
5. Adopted the multi-viewport screenshot helper from the supplied package.
6. Preserved the previous weighted critique rubric, repeatable test cases, and paired fixtures.
7. Reworked the core `SKILL.md` to connect all phases and add evidence boundaries, fidelity rules, browser-support caution, and honest verification requirements.

## Validation performed for this release

- Reviewed all source files in the supplied ZIP.
- Confirmed that every path referenced by the new core skill exists in the package.
- Checked the screenshot helper's Python syntax with `py_compile`.
- Checked that the ZIP can be reopened and contains the expected files.
- Did not run a new model-vs-model or with-skill-vs-without-skill generation experiment.
- Did not claim fresh browser screenshot comparison or accessibility conformance.

## Existing paired exercises

The previous package contains three paired tasks:
- Climate observatory landing page.
- Warehouse shift operations dashboard.
- Editorial culture magazine.

Their prior source-level findings and provisional scores remain in `tests/fixtures/` and the prior test report history. They are not presented as new v0.2.0 empirical results. The original report explicitly states that screenshot capture did not complete, so the scores are estimates from source review, not blinded or rendered comparisons.

## Recommended next empirical pass

1. Use the same model, context, assets, prompt, and time/tool budget for each baseline and skill-guided run.
2. Use a fresh context for each run.
3. Capture 390px, 768px, and 1440px screenshots (plus the project's actual target widths).
4. Have reviewers score anonymized outputs with `references/critique-rubric.md`.
5. Test keyboard navigation, focus, contrast, 200% zoom, reduced motion, long content, and relevant browser fallbacks.
6. Run at least two independent repetitions per task before drawing strong conclusions.


## v0.3.0 review-driven update

This release incorporates the seven concrete recommendations from the follow-up Claude review. Structural checks were rerun for the package and script syntax. This is not a new model A/B study or a fresh browser-rendered design comparison; the earlier source-review observations remain historical and should not be read as empirical proof that v0.3.0 improves generated visual output.

Checks performed for this package:
- Confirmed every local path referenced by `SKILL.md` exists.
- Compiled `scripts/shoot.py` with Python's syntax compiler.
- Confirmed the original six paired HTML fixtures remain present.
- Confirmed the ZIP archive passes integrity testing.


## v0.4.0 research-driven update

The new research material was integrated into `SKILL.md` and documented in `RESEARCH.md`. Structural and package checks were rerun. No fresh model A/B generation study or browser-rendered comparison was performed for this release. The source research informs the process design; it does not constitute empirical evidence that generated designs have improved.

## v0.4.1 review-driven maintenance

- Narrowed the skill description to explicit design critique, visual improvement, and reference-matching requests so routine frontend work remains with the project's existing specialist skills.
- Made the design brief internal by default; it is shown for new pages, major redesigns, or when requested.
- Clarified that iteration effort scales with task size rather than requiring multiple rounds for localized fixes.
- Updated the screenshot helper to use the page `load` event instead of `networkidle`.
- Restricted the Chrome CLI fallback to Playwright import/browser-launch failures. Navigation and screenshot failures now surface instead of being silently masked.
- Added explicit warnings when the CLI fallback cannot honour dark-mode or full-page capture.

Validation status for this maintenance update: source changes are committed; no rendered A/B comparison or visual-quality improvement is claimed. Run the helper in an environment with Playwright browsers and in a CLI-fallback environment to verify both paths.
