# Judging: critique like a senior designer

The judgement is made on the rendered result, not on the code. Code can be clean and the page still feel wrong; the reverse also happens. Render, look, critique, fix, render again.

## Contents
1. Render
2. Look like a visitor first
3. The critique passes
4. Robustness checks
5. Severity and the fix table
6. When to stop
7. Reviewing someone else's work

---

## 1. Render

```bash
python3 <skill-dir>/scripts/shoot.py page.html --out shots --widths 390,768,1440 --dark --full
```
Look at every screenshot (open them with your image-reading tool). If you have a browser tool (Playwright or Chrome DevTools MCP), you can also hover, focus, resize and check states. If nothing can render, say so plainly and do the passes below against the code, more carefully, imagining the result at each width.

## 2. Look like a visitor first

Before checking any rule, look at the 1440 and 390 screenshots for a few seconds each and answer honestly:
- **Glance (1 second):** What do I see first, second, third? Is that the order the brief wanted?
- **Five seconds:** Do I know what this is, who it's for, and what to do next?
- **Feeling:** Does it feel like the brief's mood? Does it feel *made for this subject*, or could the logo be swapped for any other company's? (Cover the logo/name in your mind and ask what this could be.)
- **Memory:** What would I remember tomorrow? If nothing, the signature is missing or too timid.

Write these answers down. They are the most important findings and the easiest to lose once you start checking details.

## 3. The critique passes

Go through each. Note problems with their location.

1. **Hierarchy.** Squint: is the intended level-1 element still the strongest shape? Are levels 1 and 2 clearly different? Is there one primary action per view? Is anything competing for attention that shouldn't?
2. **Composition and alignment.** Count left edges: few and intentional? Do things that should align, align (text baselines across columns, card tops, buttons)? Is the grid broken only on purpose? Is the visual weight balanced?
3. **Spacing and rhythm.** Is space inside groups clearly smaller than between groups? Are section gaps generous and consistent? Any cramped areas, any accidental big holes? Does the page have pace (variation between sections), or is it monotonous?
4. **Typography.** Is the scale decisive? Line lengths within 45–75ch? Headings broken well (no orphans, no awkward splits)? Leading and tracking right for each size? Too many sizes or weights?
5. **Colour.** Do proportions match the plan (accent rare)? Do neutrals feel intentional? Any contrast failures (check secondary text and text on images/tints)? Does dark mode work: surfaces, borders, shadows, images?
6. **Shape and depth.** One radius logic, nested radii concentric? One method of layer separation? Shadows soft, layered and believable?
7. **Imagery and drawings.** One graphic language? Crops intentional? Drawings well-proportioned, clean curves, consistent strokes?
8. **Details.** Focus states, hover states, link styling, selection colour, number alignment, icon alignment, real typographic characters.
9. **Specificity.** Is anything here generic (see the defaults table in `deciding.md`)? Is the signature present and well executed? Did anything get added that the brief doesn't justify? Remove one thing.

## 4. Robustness checks

A design that only works with perfect content is not finished. Check (in renders or by reasoning about the CSS):
- 320px width: no horizontal scroll, nothing overflowing, tap targets usable.
- Very long words/URLs/names (`overflow-wrap: anywhere` where needed; `min-width: 0` on flex/grid children that contain text).
- Short and missing content (an empty list, a card without an image, a one-word title).
- 200% zoom / larger default font size.
- Dark mode and forced-colors (if supported).
- Translations that are 30–40% longer (buttons, nav).
- Keyboard: every interactive element reachable with a visible focus style, in a sensible order.

## 5. Severity and the fix table

Classify each problem:
- **P0 – broken**: unreadable, inaccessible, broken layout, misleading.
- **P1 – weakens the design**: wrong hierarchy, generic, inconsistent system, poor mobile.
- **P2 – polish**: details, small alignments, refinement.

Then write a table and fix P0 and P1, and the P2s that are cheap:

| # | Sev | Where | Problem | Fix | Why |
|---|---|---|---|---|---|
| 1 | P1 | hero, 390px | Headline and subhead are 34px vs 28px: no clear first read | Headline to `--step-4`, subhead to `--step-1`, muted ink | Hierarchy needs a decisive jump |

"Why" matters: it is what makes the fix reusable knowledge, and it lets the user disagree with the reasoning rather than the taste.

## 6. When to stop

Re-render after fixing and run the glance test again. Stop when:
- No P0/P1 problems remain, and
- the glance test gives the intended order and mood, and
- the remaining notes are taste ("could be bolder") rather than faults.

Usually 2–3 rounds. If a round makes things worse, revert that change: not every idea survives contact with pixels.

## 7. Reviewing someone else's work

For a review-only task, use the same passes, but:
- Start with what works and why (designers who only list problems are not trusted, and the user needs to know what to keep).
- Be concrete: location, problem, fix, why. "The spacing feels off" is not feedback; "the 24px gap between the pricing cards' title and price equals the gap between cards, so the cards don't read as units — tighten inside to 12px" is.
- Respect the design's intent: judge it against what it is trying to be, not against your preferred style. Flag rule-breaking only if it is drift rather than intention.
- Rank by impact, and keep the list to what matters (5–10 items), with the P2 polish as a short tail.