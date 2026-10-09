# Graphic Novel Style Guide

Purpose: lock the approved visual language for all graphic-novel renders.

The approved house style is `chapter_01_wakeup/continuity-sheet.png`.

Use that file as the primary visual authority for all reference assets. Other Chapter 1 images can help with page flow, but they do not override the continuity sheet's clean production-reference look.

Future renders should use these files as references whenever the image tool supports references:

| Reference | Path | Use |
|---|---|---|
| Wake-up continuity sheet | `chapter_01_wakeup/continuity-sheet.png` | Primary style lock: model-sheet layout, clean off-white background, fine ink contours, restrained painted realism, subdued palette. |
| Wake-up page 01 | `chapter_01_wakeup/page-01.png` | Panel rhythm, soft clinical light, blurred POV, restrained captions. |
| Wake-up page 02 | `chapter_01_wakeup/page-02.png` | Action blocking, controlled tension, clean readable motion. |
| Wake-up page 03 | `chapter_01_wakeup/page-03.png` | Dialogue placement, sterile background restraint, fade-to-black pacing. |
| Cassian Rho sheet | `characters/cassian-rho/continuity-sheet.png` | Dedicated character continuity for Cassian only. |
| Korin partial-face study | `experiments/korin-office-meditation/assets/study-02-partial-face.png` | Human-detail lock for anatomically caused skin variation, minor imperfections, stubble, hair grouping, brows, lashes, hands, and nails. It does not override character identity, the Chapter 1 graphic-novel finish, palette, exposure, composition, or continuity-sheet layout. |
| Surface Age stacks style reference | `style_refs/surface-age-stacks-style-reference.png` | Approved environmental mood reference for stack-field landscapes: vast water horizon, storm shelf, monumental vertical stacks, muted yellow-gray light. |
| Surface Age silo stack landscape | `locations/surface-age-stack-field/landscape-reference.png` | Approved scale and geometry reference: high oblique perspective, one broad silo reaching the cloud deck, restrained footing, and an otherwise empty flooded wasteland. |

## Approved Look

- Sophisticated painted graphic-novel realism.
- Clean restrained ink contours.
- Realistic anatomy and grounded body language.
- Low-saturation palette with controlled accents.
- Clean off-white production-reference backgrounds for continuity sheets and lore reference sheets.
- Clear, readable panel composition.
- Precise environments with enough detail to imply systems, not dense concept-art noise.
- Human faces that feel observed and specific without becoming glamour portraits.
- Tension carried by posture, blocking, light, and negative space.

## Human Detail Reference

Use `experiments/korin-office-meditation/assets/study-02-partial-face.png` as the protected detail reference for focused character corrections. Its useful qualities are anatomically organized pores and fine lines, minor complexion irregularities, uneven stubble density, distinct eyebrow and eyelash growth, grouped hair strands with believable roots and flyaways, and specific hand, tendon, nail, and knuckle detail.

Carry those qualities into the established painted graphic-novel language rather than copying the study's near-photographic finish. Do not import Korin's identity into another character, deepen every image to its near-black exposure, reproduce its severe crop, or add skin texture at a uniform strength. Detail should vary with focus, distance, age, anatomy, grooming, light, and the needs of a readable panel.

At close range, preserve the specific transition among brow, temple, cheek, nose, mouth, jaw, ear, and neck. Do not simplify a face into a few swollen or chiseled wedges, a stone-carved mask, or generic heroic bulk. Material coherence cannot compensate for lost facial form or identity.

## Line And Paint

- Use fine ink outlines and controlled hatching.
- Keep brush texture visible but quiet.
- Avoid heavy digital matte-painting density.
- Avoid excessive grime overlays that obscure faces, props, or wall details.
- Keep contrast readable on a page: darks should support staging, not swallow the frame.

## Material-Coherence Correction Factor

Evaluate every reference asset and finished page for material coherence. This factor corrects a recurring generated-image artifact in which cloudy or marbled patches drift across fabric and skin without being caused by form, light, wear, or environment.

Use these severity levels:

| Level | Meaning | Action |
|---|---|---|
| `MCF-0` | Coherent local values; variation follows physical causes. | Pass. |
| `MCF-1` | Faint residual texture that does not disrupt identity or material reading. | Watch; correct only when the asset is otherwise being revised. |
| `MCF-2` | Visible uncaused mottling changes the apparent dye, complexion, or material across a surface or repeated view. | Focused material rework before the asset is reused as a generation reference. |
| `MCF-3` | Severe or repeated mottling compromises a continuity lock or is already propagating into dependent art. | Priority focused rework and review before further dependent rendering. |

An image passes only when:

- each garment panel holds one coherent local value across repeated views;
- cloth variation follows folds, seams, overlap, weave direction, damage, dampness, or documented wear;
- one character's exposed skin maintains a coherent complexion across face, neck, hands, arms, and repeated poses;
- skin variation follows anatomy, age, cast light, injury, grime, or another visible physical cause;
- different materials remain distinguishable instead of sharing the same cloudy surface noise.

Do not mistake physically explained variation for the artifact. Preserve rain-darkening, soot, rust, bruising, scars, patina, repairs, and ingrained dirt when the source or environment supports them. The correction removes only variation that floats independently of the depicted object.

## Color

- Default palette: silver-white, graphite, muted gray, bone, clinical blue-gray, dull amber.
- Lower Grid and Below the Map may add ochre, rust, red-brown, soot gray, and dirty amber, but still must keep the Chapter 1 clarity and line discipline.
- Do not let lore scenes drift into a single dark brown/ochre concept-art palette.
- Use bright color only when canon or scene function requires it.

## Composition

- Build images as graphic-novel references or pages, not cinematic key art.
- Favor clear silhouettes, readable spatial relationships, and deliberate empty space.
- Lore scenes should usually be rendered as continuity/reference sheets with separated panels, unless the task explicitly asks for a finished comic page.
- Stack-field landscapes may use wide cinematic environmental framing when the goal is scale, weather, and geography rather than a model sheet.
- Character sheets need front/side/back views, head angles, expression studies, and a small number of action poses.
- Scene pages need panel hierarchy, readable captions/dialogue, and continuity with approved references.
- Lore plates should still look like they belong in the same book as Chapter 1.

## Text

- Use manuscript text only.
- Keep text sparse and readable.
- If generated text is wrong, correct it with a targeted edit or rerender.
- Do not invent labels, slogans, faction names, exposition, or document text.

## Avoid

- Dark archival concept-art drift.
- Overpainted environments with muddy faces or unreadable props.
- Photoreal movie stills.
- Superhero anatomy or heroic poster staging.
- Fantasy armor, cyberpunk neon, or generic dystopian grime.
- Villain/saint simplification for historical figures.
- Gore, spectacle, or battle-poster treatment unless the manuscript explicitly requires it.

## Style QA

Before accepting a render, compare it to the Chapter 1 wake-up files and complete `visual_discrepancy_audit_SOP.md`:

1. Does it look like the same graphic novel?
2. Is the linework as clear as Chapter 1?
3. Is the palette restrained without becoming muddy?
4. Are faces, hands, props, and setting details readable?
5. Is the image useful as continuity material, not just mood art?
6. Does it avoid adding non-canon symbols, costumes, factions, or spectacle?
7. Does it pass the material-coherence correction factor without uncaused fabric or skin mottling?
8. Do close faces retain specific anatomy and identity without chunky planar simplification, plastic smoothing, or uniformly stamped microtexture?
9. Are hands and feet anatomically complete, correctly jointed, and making believable contact?
10. Do body proportions, shoulders, pelvis, limbs, and joints remain credible for the character and camera angle?
11. Could each pose be entered, supported, and exited physically, with limb placement matching the depicted movement and momentum?
12. Do scale, perspective, occlusion, weight, lighting, weather, damage, and panel-to-panel continuity remain coherent?
13. Is the image free of extra or fused anatomy, duplicated forms, accidental text, logos, insignia, watermarks, and unexplained symbols?

If any answer fails, mark the asset `Needs Style Rerender` in `asset_registry.md`.
