# Senior designer critique rubric

Score each dimension from 1 (poor) to 5 (excellent). Multiply by the weight. Use `N/A` only when the dimension genuinely does not apply, and renormalize the total. Scores support prioritization; they do not replace written evidence.

| Dimension | Weight | 1 — weak | 3 — adequate | 5 — strong |
|---|---:|---|---|---|
| Intent and relevance | 15 | Visual choices disconnected from task | Mostly supports task | Every major choice serves audience and purpose |
| Hierarchy and clarity | 15 | No clear entry point or scan path | Primary content identifiable | Effortless, deliberate reading order |
| Composition and rhythm | 15 | Awkward proportions, alignment, or density | Functional but ordinary | Balanced, intentional, memorable composition |
| Typography and content | 10 | Hard to scan or inconsistent | Readable with basic hierarchy | Distinctive, legible, content-aware system |
| Color and surfaces | 10 | Weak contrast or arbitrary decoration | Coherent but generic | Purposeful roles, depth, contrast, restraint |
| Specificity and character | 10 | Template-like or mismatched | Some contextual choices | Distinctive and defensible for this product |
| Responsive integrity | 10 | Overflow or broken reflow | Works at common widths | Recomposition preserves hierarchy across widths |
| Accessibility and interaction | 10 | Keyboard/state/contrast failures | Main flows usable | Semantics, focus, states, motion and contrast considered |
| Craft and performance | 5 | Fragile CSS or heavy assets | Maintainable enough | Precise, efficient, and consistent |

## Score interpretation

- **90–100:** high craft; only minor improvements remain.
- **80–89:** strong; address the highest-impact remaining issue.
- **70–79:** acceptable foundation; one or more design dimensions need refinement.
- **Below 70:** revisit the design thesis, hierarchy, or composition before polishing.

A score is not a claim of WCAG conformance or pixel fidelity. Accessibility needs actual checks; visual fidelity needs matched screenshots; performance needs measurement.

## Critique format

For each finding, state:

- **Evidence:** what is visibly or technically wrong?
- **Impact:** why does it matter to the user or brand?
- **Priority:** P0–P3.
- **Fix:** the smallest high-leverage change.
- **Verification:** how will we know the fix worked?

## Iteration rules

1. Fix blockers and hierarchy before micro-polish.
2. Change one coherent group of issues at a time.
3. Recheck the full composition after local changes; local fixes can disturb global balance.
4. Stop when the brief is met and remaining issues are low-impact or subjective.
5. Never inflate scores to make a result look successful. Note unavailable evidence.