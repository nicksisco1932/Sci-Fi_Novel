# Graphic Novel Visual-Discrepancy And Material-Coherence Audit

Purpose: evaluate visual discrepancies systematically across the production-art corpus without triggering broad redesigns or overwriting accepted assets.

This is a production-quality audit, not canon. Use `visual_discrepancy_audit_SOP.md` for the complete review procedure. `MCF` remains the material-specific score; the other gates prevent material improvement from concealing anatomy, movement, continuity, or perspective failures.

## Protected Human-Detail Reference

Use `experiments/korin-office-meditation/assets/study-02-partial-face.png` for focused correction work involving skin, hair, stubble, or hands. Preserve the file unchanged at that path.

- Dimensions: `1024x1536`
- SHA-256: `F09E76C54E49BEE6ACDAFB2D038636CC0A89A0F891668D95C54AF73CE398C33E`

Extract these qualities: minor skin imperfections that follow anatomy, varied stubble density, individual and grouped hair behavior, specific brows and lashes, restrained lip texture, and believable tendons, knuckles, nails, and fine hand hair. Do not extract Korin's identity, the study's severe crop, near-black exposure, office composition, or near-photographic rendering level. The Chapter 1 continuity sheet remains the overall graphic-novel style lock.

## Expanded Human-Rendering Review

The material-coherence score is necessary but not sufficient. A page can lose the cloudy artifact and still render a face as a few oversized, cartoon-like masses. Review every production asset through every applicable gate, using the same `0` pass, `1` watch, `2` focused rework, and `3` priority rework severity:

| Gate | What passes | Typical failure |
|---|---|---|
| Material coherence | Skin and cloth variation follows form, light, wear, or environment. | Cloudy, marbled, etched, or camouflage-like value patches cross unrelated surfaces. |
| Facial form and identity | Brow, nose, cheek, mouth, jaw, and neck resolve as specific anatomy consistent with the accepted character. | Features collapse into broad wedges, swollen planes, a stone-carved mask, or generic heroic bulk. |
| Human microdetail | Pores, fine lines, complexion, stubble, brows, lashes, and hair grouping vary naturally with scale. | Plastic smoothing, uniformly stamped texture, clumped beard shadow, or helmet-like hair. |
| Hand and foot anatomy | Digit count, length, joints, webbing, nails, palm/sole structure, grip, and foreshortening are credible. | Fused, missing, duplicated, boneless, overlong, or backward digits; impossible grips or flattened feet. |
| Whole-body anatomy | Head, torso, pelvis, shoulders, limbs, joints, and muscle volumes remain proportionate to the character and view. | Broken shoulders, rubber limbs, telescoped forearms, twisted torsos, dislocated joints, or unexplained body-shape drift. |
| Pose and movement mechanics | Limbs occupy positions that could produce or follow the depicted action within credible joint ranges and momentum. | Arms trail or lead the wrong motion, strikes lack a usable arc, running limbs contradict direction, or a body changes direction without force. |
| Contact, balance, and weight | Feet, seats, hands, impacts, carried objects, and body supports meet surfaces and bear weight convincingly. | Floating bodies, unsupported crouches, sliding feet, weightless impacts, missing reaction force, or hands that do not contact what they grasp. |
| Perspective, scale, and occlusion | Figure and object size, overlap, depth, horizon, and foreshortening agree with the camera. | Oversized background figures, inconsistent head scale, impossible overlap, or depth that changes within a panel. |
| Character-state continuity | Identity, costume, equipment, augmentation, injury, dirt, wetness, handedness, and carried props match the scene and adjacent panels. | Costume swaps, migrating bandages, missing equipment, changed armor geometry, or unexplained cleaning and damage. |
| Environment and object continuity | Architecture, openings, furniture, props, debris, and damage retain coherent geometry and location. | Rotated buildings, moving doors, changing room plans, duplicated props, or damage that disappears between views. |
| Lighting and physical causality | Highlights, shadows, reflections, rain, smoke, debris, wear, and motion follow visible sources and forces. | Contradictory shadows, decorative rain, uniform grime, reflection errors, or debris moving against the impact. |
| Panel and action continuity | Screen direction, eyelines, relative positions, action trajectory, time, and cause/effect read across panels. | Teleporting characters, reversed pursuit direction, broken eyelines, repeated beats, or missing motion transitions. |
| Generated artifacts and prohibited content | Anatomy and objects are complete; no accidental marks, text, logos, insignia, watermarks, or duplicated forms appear. | Extra limbs, fused objects, unreadable generated lettering, symbols, signatures, or accidental gore. |
| Style and readability | Line clarity, value separation, detail density, silhouettes, and lettering space serve the established graphic-novel language. | Cartoon drift, photoreal movie-still drift, muddy blacks, visual noise, or unreadable staging. |

Any `2` or `3` blocks promotion until the failing region receives a focused review. The asset inherits its highest applicable severity; never average a severe hand, anatomy, movement, face, or perspective error into an otherwise successful page.

### Current Chapter 13 Finding

Asset: `experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-perspective-v2.png`

The close Cassian profile in the second row, left panel fails despite the improved overall material pass:

- Material coherence: `2` - angular etched/marbled patches remain across cheek, temple, neck, and wet shirt.
- Facial form and identity: `3` - the brow, cheek, nose, jaw, and neck resolve as oversized hard planes, producing a clunky, chunky stone-carved face and weakening Cassian's accepted identity.
- Human microdetail: `2` - stubble and wet-skin variation read as clumped surface pattern rather than fine, anatomically organized detail.
- Spatial and anatomical credibility: `0` for this panel; the separate first-panel Thena scale problem is corrected in this version.

Status: not approval-ready. The next edit should isolate Cassian's marked face, hairline, stubble, ear, and neck while preserving the corrected first-panel scale and every other page invariant.

## Recent Correction Record

1. Defined the Material-Coherence Correction Factor for uncaused fabric and skin mottling.
2. Preserved the Korin partial-face study as the protected human-detail reference for skin imperfections, stubble, hair, brows, lashes, hands, and nails.
3. Produced two non-destructive Almelah dojo master pilots; the second removes the dominant marbling but retains an `MCF-1` trouser residual.
4. Produced Chapter 13 and Chapter 14 contextual material-refinement tests using the Chapter 1 craft lock and Korin human-detail reference.
5. Corrected Thena's first-panel scale and grounding in the Chapter 13 test so her seated figure reads deeper inside the doorway recess.
6. Preserved the original contextual pages, all intermediate candidates, dimensions, and hashes; no accepted source has been overwritten or promoted.

## Production Audit Scope

Repository inventory on 2026-09-01:

- `240` total graphic-novel PNGs.
- `82` files under the concept-sketch corpus are excluded from this detail audit as requested.
- `50` proof PNGs are derivative review outputs. They are deferred to final verification after their source art is corrected rather than counted as independent correction targets.
- `108` remaining source, reference, scene, and experiment PNG paths.
- `102` unique image contents after SHA-256 deduplication; five duplicate-content groups account for six redundant path instances.

The `102` unique review images comprise `46` scene pages, `15` lore images, `12` location references, `11` experiment images, `10` character references, `4` Chapter 1 images, `3` motif/technology images, and `1` external style reference.

Proofs are not exempt from quality control. Once a source correction is approved, inspect the corresponding proof page to ensure layout, scaling, and reproduction have not reintroduced or concealed a failure.

## Efficient Review Path

Current evidence-backed correction queue: `PROPOSED_FIXES_PHASE_1_2026-09-01.md`.

1. **Audit authority locks first.** Review the Chapter 1 set and all character continuity sheets at full resolution. Correct reusable identity sources before their dependent pages.
2. **Hash-deduplicate.** Review one visual instance of each unique SHA-256 and propagate the result to identical registered paths.
3. **Use two viewing scales.** A fit-to-page contact-sheet pass catches perspective, scale, silhouette, and tonal drift; a full-resolution face/hand pass catches mottling, chunky facial planes, hair, stubble, and hand failures.
4. **Score, do not rerender during screening.** Record every applicable gate severity and the exact panel or region. `0` and `1` require no immediate edit; `2` and `3` enter the focused queue.
5. **Prioritize by propagation risk.** Character sheets first, then close-up scene pages, then group sheets and wider scenes, then human-bearing lore/location plates, then non-human material plates.
6. **Make one focused edit per asset.** Use the target for composition, the accepted character sheet for identity and costume, Chapter 1 for craft, and the Korin study only for human detail. Preserve a versioned sibling and review it before continuing.
7. **Recheck dependencies and proofs.** After a corrected lock is approved, review every dependent scene and its proof reproduction. Do not batch-promote candidates.

The first screening pass should therefore produce a compact manifest with path, SHA-256 group, authority role, applicable gate scores, exact failing region, dependency count, and action. This avoids generating during diagnosis and concentrates rework on the small set of high-impact sources.

## Acceptance Target

The Almelah dojo master second-pass candidate is the initial correction target:

- Source: `characters/almelah-dojo-master/continuity-sheet.png`
- First pilot: `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot.png`
- Second-pass candidate: `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot-v2.png`
- Status: candidate only; user review required before registry promotion or source replacement.

The second-pass candidate removes the dominant cloudy marbling and gives the skin and dark wrap substantially more stable local values. Full-resolution review still finds faint low-contrast angular texture in parts of the light trousers, provisionally `MCF-1`; keep the image as a candidate until the user decides whether that residual warrants one narrower pass.

## Contextual Page Tests

Two versioned candidates test the correction factor under complex environmental conditions without altering the contextual originals:

| Asset | Conditions tested | Initial result | Status |
|---|---|---|---|
| `experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-perspective-v2.png` | Rain, wet skin, wet cloth, composite armor, abrasion, lightning, action, and recessed seated-figure perspective | Shared cloudy mottling is substantially reduced and Thena's first-panel scale is corrected, but the second-row Cassian profile retains `2` material/microdetail failures and a `3` chunky facial-form failure. Pre-existing costume, armor, and staging drift is intentionally unchanged. | Needs focused Cassian face rework |
| `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-material-refinement-test.png` | Multiple ages and complexions, stubble, hair, hands, gauze, worn cloth, bedding, metal, damp walls, and low practical light | Material separation and human detail improve without cleaning away legitimate clinic grime. | Candidate; user review required |

These tests do not replace accepted Chapter 13 or Chapter 14 pages and do not promote the contextual variants. They isolate material rendering only.

The earlier Chapter 13 material-test file is retained as an iteration record but is superseded for review because its first-panel seated Thena was too large for the perspective.

## Focused Rework Queue

Work from reusable character references outward. Do not begin a corpus-wide rerender.

| Order | Asset | Initial MCF | Focus | Status |
|---|---|---:|---|---|
| Pilot | Almelah dojo master continuity sheet | `MCF-3` source; `MCF-1` residual in candidate | Dark wrap, light trousers, exposed skin across repeated views | Second-pass candidate ready for review |
| 1 | Young Gor continuity sheet | `MCF-3` | Dark training wrap, trousers, arms, chest, hands, and face | Pending focused rework |
| 2 | Cassian Rho continuity sheet | `MCF-2` | Dark medical clothing and repeated face/arm complexion | Pending focused rework |
| 3 | Alyen Ithra continuity sheet | `MCF-2` | Pale uniform panels and repeated face/hand complexion | Pending focused rework |
| 4 | Korin Tal continuity sheet | `MCF-2` | Suit panels and repeated facial complexion | Pending focused rework |
| 5 | Thena continuity sheet | `MCF-2` | Separate uncaused mottling from legitimate wear, rust, and grime | Pending focused rework |
| 6 | Augmented Gor continuity sheet | `MCF-3` | Separate skin, sensor weave, composite armor, rain-dark cloth, scars, and wear | Pending focused rework |
| 7 | Broken-clinic leader and guard sheet | `MCF-3` | Preserve ingrained dirt while removing shared skin-and-cloth marbling | Pending focused rework |
| 8 | Below-the-Map escort group sheet | `MCF-2` | Preserve role-specific wear and dampness; remove floating cloudy texture | Pending focused rework |

## Controlled Rollout

1. Approve the Almelah master second-pass target or request one narrow correction.
2. Rework the first four single-character sheets one image at a time, saving versioned candidates.
3. Review identity and material behavior after every asset; do not batch-promote.
4. Continue to the complex gear and group sheets only after the simpler references establish a stable correction prompt.
5. Audit scene pages, locations, technology, lore plates, and the Volume One proof only after the relevant continuity sources are approved.
6. Assign `MCF-0` or `MCF-1` without rerendering when the artifact is absent or too faint to affect reading.

## Rework Prompt Factor

Add this requirement to focused edits:

> Remove uncaused cloudy, smoky, marbled, camouflage-like, or watercolor value patches from fabric and skin. Give each material one coherent local value. Permit variation only where caused by folds, seams, overlap, weave direction, anatomy, age, cast light, documented wear, injury, dampness, grime, or another visible physical cause. For close human detail, follow the Korin partial-face study's anatomically organized pores, imperfections, stubble, hair grouping, and hand detail while retaining the target character's exact identity and the Chapter 1 painted graphic-novel finish. Preserve geometry, composition, and all story information exactly.

The correction factor does not authorize broad style transfer, palette normalization, cleanup of legitimate environmental wear, character redesign, or changes to accepted blocking.
