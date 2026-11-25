# Seeing: how to read any design

A designer looking at a page sees three layers at once: the **idea** (why it looks the way it does), the **system** (the rules that make it consistent), and the **execution** (the specific values and techniques). Beginners see only the surface: "it's clean", "nice colours". Your job is to name all three layers precisely enough that someone could rebuild the design from your notes, and to explain why it works so the approach can be reused elsewhere.

## Contents
1. The order of looking
2. Measuring from a screenshot
3. Measuring from code or a live page
4. Naming the concept
5. Why it works (and where it doesn't)
6. Report format
7. Rebuilding a design faithfully

## 1. The order of looking

Go from coarse to fine. Each pass answers one question.

**Pass 1: the glance (1 second).** Look as a visitor. What do you see first, second, third? What is this page *about* before reading a word? What mood does it give (calm, urgent, premium, friendly, technical, rough)? Write this down before analysing, because analysis destroys first impressions.

**Pass 2: the skeleton.** Squint (or imagine it blurred). Now only big shapes are left: blocks of dark and light, where the mass sits, where the empty space is. Describe the composition: centred or asymmetric, how many columns, full-bleed or contained, how sections alternate (light/dark, image left/right, wide/narrow). Count the distinct left edges in the page; a disciplined design has few (2–4).

**Pass 3: the grid and space.** Find the container width and side margins. Find the columns: where do text blocks and images start and stop? Find the spacing unit: measure gaps between related things (small) and between sections (large); they are usually multiples of one base (4 or 8px) or follow a ratio. Note where the design *breaks* its grid on purpose (a full-bleed image, an element hanging into the margin): breaks are often the signature.

**Pass 4: type.** For each text role (display, h1–h3, body, small, label, button, nav) record family, size, weight, line height, letter spacing, case. Compute the scale: divide adjacent sizes. A consistent ratio (1.2, 1.25, 1.333, 1.5) means a modular scale; jumps (e.g. 16 → 64) mean a deliberate contrast between display and text. Identify the font *category* even if you can't name the exact font (geometric sans, grotesque, humanist sans, transitional serif, slab, mono, display). Note measure (characters per line) and how headings break.

**Pass 5: colour.** List the colours and give each a *role*: ground (background), surface (cards/panels), ink (text, usually 2–3 levels), accent (action/brand), signal (success/warn/error), decoration. Then estimate the **proportions**: roughly what share of the screen is each role? Most strong designs are 70–90% ground, 5–25% ink and surfaces, under 5–10% accent. Note temperature (warm or cool neutrals), whether neutrals are tinted toward the brand hue, and contrast levels.

**Pass 6: shape and depth.** Radius values and their logic (sharp everywhere? rounded buttons only? nested radii concentric?). How layers are separated: whitespace only, borders, tonal surfaces, shadows (soft/hard, one or layered, tinted or grey), blur/glass. Line weights. Icon style (outline/filled, stroke width, corner style).

**Pass 7: imagery and graphics.** Photo style (documentary, staged, product on colour, abstract), cropping (tight, wide, bleed), treatment (duotone, grain, rounded, masked into shapes). Illustrations: one graphic language or mixed? Decorative elements (lines, blobs, patterns, noise): what job do they do?

**Pass 8: interaction and motion** (live pages only). Hover and focus states, transitions, scroll effects, what moves and how fast. Is motion functional (showing where something came from) or decorative?

**Pass 9: content and voice.** Headline style (claim, question, name, number), length of copy, density. The voice is part of the design: a terse, confident page and a chatty one need different typography.

## 2. Measuring from a screenshot

You cannot inspect a picture, so measure it. Know the image's real width first (a 1920px design shown at 960px is a 0.5 scale: double what you measure).

- Use Python + Pillow when available to crop regions and sample pixel colours exactly:
  ```python
  from PIL import Image
  im = Image.open("ref.png").convert("RGB")
  print(im.size, im.getpixel((x, y)))          # exact colour at a point
  im.crop((x0, y0, x1, y1)).save("zoom.png")    # then look at the zoom
  ```
  Look at zoomed crops for type, icons, borders and shadows; at full size, small details are invisible.
- Cap height ≈ 0.7 × font size for most sans fonts; x-height ≈ 0.5. Measure a capital letter's height and divide by 0.7 to estimate font size.
- Line height = distance between baselines of two lines.
- Colours from screenshots are approximate (compression, antialiasing). Sample a flat area, not an edge, and round to a sensible value.
- State your confidence. "~48px (±4)" is honest; "48px" from a JPEG is not.

## 3. Measuring from code or a live page

Prefer real values over estimates. In code: read the tokens/variables file, the theme config (e.g. Tailwind config), global styles, then one or two representative components. On a live page: use computed styles (browser devtools, Playwright's `getComputedStyle`, or the chrome-devtools tools if available) for the elements that matter. Collect the actual set of font sizes, colours, spacings and radii in use, and notice which values repeat (the system) versus one-offs (drift or special cases).

## 4. Naming the concept

The concept is the single idea the rest serves. Find it by asking: *if I removed one thing, which removal would make this page stop being itself?* That thing points to the concept.

Good concept statements are specific and causal:
- "A logistics company that wants to feel dependable: everything sits on a rigid 12-column grid, the photography is documentary (real warehouses, real staff), and the only colour besides neutrals is a safety orange reserved for actions, like the hi-vis on a loading dock."
- "Editorial calm: one serif at large sizes carries all the personality, so everything else (colour, shapes, UI) is deliberately quiet."

Weak ones describe a style: "modern and clean", "minimalist with bold typography". If your statement would fit a thousand sites, keep looking.

## 5. Why it works (and where it doesn't)

Explain each important decision by its effect on the reader: what it makes them notice, feel, trust or do. Tie it to principles where relevant: hierarchy through contrast of size/weight/colour, proximity grouping, alignment creating order, repetition creating identity, rhythm from alternating sections, restraint making the accent powerful, white space signalling confidence or calm.

Then be honest about weaknesses. Senior designers respect a design without worshipping it. Common ones: weak contrast in secondary text, inconsistent spacing between sections, a hierarchy that competes (two things shouting), text over busy images, a mobile layout that is just the desktop one stacked. Separate *deliberate rule-breaking* (consistent, serves the idea) from *drift* (inconsistent, serves nothing).

## 6. Report format

Use this structure for analysis tasks. Adjust length to the request: a quick question gets a short version.

```markdown
## First impression
What you notice in order (1st, 2nd, 3rd), and the mood, in 2–3 lines.

## The concept
One or two sentences: the idea and how the design expresses it.

## The system
| Part | What it is | Values |
|---|---|---|
| Grid & layout | … | container, columns, margins, gutters |
| Type | … | families/categories, sizes per role, ratio, weights, leading, tracking |
| Colour | roles and proportions | values (oklch or hex) per role, rough % of screen |
| Space | base unit and scale | the scale actually used |
| Shape & depth | … | radii, borders, shadows |
| Imagery & graphics | … | style, crop, treatment |
| Motion | … | (if visible) |

## Why it works
3–6 points, each a decision and its effect on the reader.

## Weak spots
What a senior designer would change, most important first, each with a fix.

## How to build it
The structure (landmarks and sections), the CSS approach for the non-obvious parts (e.g. "the image bleeds left while the text stays on the grid: grid with a named full-bleed column line"), and the tokens to start from.

## Carry it elsewhere
What part of this approach is reusable for a different subject, and what is specific to this one.
```

## 7. Rebuilding a design faithfully

When asked to recreate a design, fidelity comes first, your taste second. Match the measured system exactly, then build with good modern CSS. Where the reference has a flaw (low contrast, broken alignment), keep it visually faithful but mention it, and fix it only if the user asked for improvement or it fails the floor (accessibility). Use placeholder blocks with the right aspect ratio and a tone close to the photo's average colour when the original images are not available, so the composition still reads. After building, render your version and the reference at the same width and compare them side by side region by region (header, first section, …), listing differences and fixing them.