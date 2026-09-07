# Graphic Novel Visual-Discrepancy Audit SOP

Purpose: provide a repeatable acceptance and rework procedure for production artwork. This SOP evaluates visual execution only. It does not canonize adaptation choices or authorize manuscript, lore, or accepted-asset replacement.

## Scope

Apply this SOP to character and location references, scene pages, lore plates, motif and technology references, experiment candidates intended for possible production use, and final proofs.

Exclude the `concept_sketches/` corpus from this detail standard until a concept is selected for production development. Do not count proof reproductions as independent source targets; inspect them after their underlying source assets are corrected.

## Review Principles

1. Diagnose before generating. Screening never authorizes a rerender.
2. Review one unique SHA-256 image once, then map the result to identical paths.
3. Score each applicable gate independently as `0`, `1`, `2`, `3`, or `N/A`.
4. The asset inherits its highest severity. Never average away a serious discrepancy.
5. Record an exact panel, figure, object, or coordinate for every score above `0`.
6. Correct continuity sources before dependent pages.
7. Preserve originals and save every candidate as a versioned sibling.
8. Promotion or replacement requires explicit author review.

## Severity Scale

| Score | Meaning | Required action |
|---|---|---|
| `0` | Pass; no visible discrepancy at intended size or full-resolution inspection. | No action. |
| `1` | Watch; faint or peripheral issue that does not impair identity, physics, continuity, or reading. | Record it; correct only during another justified edit. |
| `2` | Focused rework; visible discrepancy weakens material, anatomy, action, continuity, or readability. | Block promotion and make a narrow correction. |
| `3` | Priority rework; focal, repeated, identity-breaking, physically impossible, or propagating failure. | Block dependent work and correct before reuse. |

## Review Gates

Score every applicable gate defined in `material_coherence_audit.md`:

1. Material coherence.
2. Facial form and identity.
3. Human microdetail.
4. Hand and foot anatomy.
5. Whole-body anatomy.
6. Pose and movement mechanics.
7. Contact, balance, and weight.
8. Perspective, scale, and occlusion.
9. Character-state continuity.
10. Environment and object continuity.
11. Lighting and physical causality.
12. Panel and action continuity.
13. Generated artifacts and prohibited content.
14. Style and readability.

## Required Inputs

Before review, identify:

- asset path and SHA-256;
- asset role and registry status;
- manuscript or adaptation scene, when applicable;
- accepted character, location, equipment, and style authorities;
- earlier and later panels or temporal variants;
- duplicate paths and dependent assets;
- intended display size and full image dimensions.

## Inspection Procedure

### Pass 1: Fit-To-Page Read

Inspect the full image at intended reading size without zooming.

Check panel order, silhouette clarity, relative figure scale, camera perspective, eyelines, screen direction, action trajectory, tonal hierarchy, negative space, and whether the story beat reads without explanation. Flag oversized background figures, floating poses, discontinuous motion, unclear contact, and any focal region that looks cartoon-like or mechanically generated.

### Pass 2: Full-Resolution Human Inspection

Inspect every visible face, hand, foot, joint, and exposed skin region at full resolution.

Check identity, facial planes, pores, fine lines, complexion, stubble, brows, lashes, hair roots and grouping, ear structure, neck transitions, digit count, finger and toe joints, nails, palm and sole structure, grip, foreshortening, and whether hands actually contact the object or person they affect.

### Pass 3: Anatomy And Movement Trace

For every active or weight-bearing figure:

1. Identify the pelvis and ribcage orientation.
2. Trace both shoulder-to-hand and hip-to-foot joint chains.
3. Check joint range, limb length, foreshortening, and left/right consistency.
4. Identify the center of mass and the supporting foot, seat, hand, wall, or opponent.
5. Trace the movement vector from preparation through contact to follow-through.
6. Verify that leading and trailing limbs match that vector and that an arm is not placed where it could not produce, resist, or recover from the motion.
7. At impacts, verify contact point, reaction force, body compression, displaced mass, debris direction, and the next panel's continuation.
8. At running, falling, reaching, grappling, sitting, or crouching, verify balance, clearance, contact, and a physically possible transition into and out of the pose.

If the pose could exist only as a frozen silhouette but could not be entered, sustained, or exited physically, score pose and movement mechanics at least `2`.

### Pass 4: Continuity And Geometry

Compare against accepted references and adjacent panels. Check face, body, handedness, clothing, equipment, augmentation, injuries, bandages, dirt, wetness, props, architecture, openings, furniture, damage, object scale, and relative positions.

For repeated locations or rotating cameras, mentally reconstruct the plan and elevation. Doors, windows, bridges, furniture, and structural landmarks must remain on the same faces and axes unless the scene visibly changes them.

### Pass 5: Material, Light, And Environment

Check that skin, hair, cloth, armor, metal, glass, water, smoke, bedding, walls, and debris remain materially distinct. Variation must follow construction, anatomy, wear, contact, dampness, gravity, light, or environment.

Trace important lights to their sources. Verify cast-shadow direction, reflection behavior, wet highlights, weather exposure, smoke drift, falling debris, and accumulated grime. Reject decorative effects that ignore the depicted surfaces or forces.

### Pass 6: Artifact And Content Sweep

Inspect borders, gutters, background figures, hands near frame edges, repeated faces, dense machinery, and debris fields for extra or fused limbs, duplicated people or props, melted objects, accidental text, numbers, logos, signatures, insignia, watermarks, unexplained symbols, gore, or unintended color.

## Audit Record

Create one record per unique image with:

| Field | Required content |
|---|---|
| Asset | Repo-relative path and SHA-256. |
| Role | Character lock, scene page, location, lore, experiment, proof, or other. |
| Authorities | Identity, costume, location, style, and scene references used for comparison. |
| Duplicate paths | Identical registered or mirrored paths. |
| Gate scores | All applicable gate scores; use `N/A` explicitly. |
| Finding | Concrete visual discrepancy, not a vague quality judgment. |
| Location | Panel number and figure/object, plus coordinate when available. |
| Evidence | What anatomy, reference, perspective, material, or physical rule is violated. |
| Correction boundary | The smallest region or property allowed to change. |
| Invariants | Everything that must remain unchanged. |
| Dependencies | Assets that inherit or reproduce this design. |
| Status | Pass, watch, focused rework, priority rework, candidate review, or approved. |

## Triage Order

1. Style and identity authorities, including Chapter 1 and character continuity sheets.
2. Severity `3` discrepancies that propagate into dependent assets.
3. Close-up faces, hands, feet, and focal action anatomy.
4. Severity `2` movement, contact, scale, continuity, and material failures.
5. Group sheets and wider human scenes.
6. Human-bearing lore, location, motif, and technology plates.
7. Non-human material, lighting, geometry, and artifact findings.
8. Proof verification after source corrections.

Within a severity level, correct the asset with the most dependents first.

## Focused Rework Procedure

1. Select one asset and one tightly bounded discrepancy or compatible cluster.
2. Name the edit target and every reference role explicitly.
3. State the mutable region, required correction, and hard invariants.
4. For movement, state the intended motion vector, contact point, supporting body part, joint chain, and before/after action state.
5. For hands, state digit visibility, grip/contact, palm orientation, foreshortening, and the object or body being affected.
6. Use the accepted character sheet for identity and costume, Chapter 1 for overall craft, and the Korin partial-face study only for human-detail behavior.
7. Make one image-generation call per asset and save a versioned sibling without overwriting the source.
8. Repeat all six inspection passes on the candidate. Compare source and candidate for new drift outside the correction boundary.
9. Record dimensions, SHA-256, prompt summary, result, residual scores, and author-review status.
10. Do not promote, replace, or propagate the candidate without explicit approval.

## Acceptance Rule

An asset is acceptance-compliant only when every applicable gate is `0` or `1`, no prohibited content is present, all required paths resolve, dimensions match their production contract, and the author has approved any replacement of an existing reference or page.

After approval, audit dependent assets and final proofs. A corrected source does not retroactively clear pages that inherited the earlier discrepancy.
