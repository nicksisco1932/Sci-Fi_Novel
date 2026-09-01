# Graphic Novel Continuity Milestone

Date: 2026-08-31

## Achievement

This repository now contains a sustained AI-assisted graphic-novel adaptation system rather than a collection of unrelated generated images.

Across recurring characters, locations, historical material, infrastructure, and sequential scenes, the work maintains a recognizable visual language derived from the Chapter 1 wake-up continuity sheet. Character identities remain legible across different pages and physical states. Locations retain material and architectural rules. Later imagery can inherit scale, atmosphere, and geometry from approved references instead of starting over with each prompt.

The resulting consistency is a significant project achievement. It demonstrates that image generation can be directed as a continuity-managed production process: canon first, references before pages, controlled iteration, explicit adaptation boundaries, and durable review records.

## What Made It Work

- **One primary style authority:** `chapter_01_wakeup/continuity-sheet.png` governs rendering, linework, palette, and production-reference treatment.
- **Continuity before scenes:** recurring characters and environments receive stable references before sequential pages are generated.
- **Canon separated from adaptation:** manuscript facts remain authoritative while faces, costumes, architecture, and staging remain adaptation designs until approved separately.
- **Sequential generation:** distinct assets are generated one at a time with the same accepted references instead of relying on unrelated batch outputs.
- **Precise visual revision:** image annotations target one posture, object, scale relationship, lighting condition, or behavioral read while preserving everything else.
- **Art separated from lettering:** pages can be corrected visually without repeatedly regenerating dialogue, and manuscript text remains auditable.
- **Production memory:** the SOP, style guide, asset registry, scene catalogue, lettering specifications, and visual briefs preserve decisions that would otherwise disappear into chat history.
- **Verification:** accepted assets are saved into the repository, dimensions are checked, intentional duplicates are hash-compared, and manuscript isolation is verified.

## Preservation Set

The minimum set needed to study or reconstruct this workflow is:

1. `SOP.md`
2. `style_guide.md`
3. `asset_registry.md`
4. `remaining_scene_catalogue.md`
5. `dialogue_correction_todo.md`
6. `chapter_01_wakeup/continuity-sheet.png`
7. Accepted character and location continuity sheets
8. Location-specific visual briefs
9. Scene sequence indexes and lettering specifications
10. `plans/render-hive-earth-continuity-set.original.md`
11. `plans/render-hive-earth-continuity-set.experiment.md`

The rendered PNG files are primary research artifacts. They should not be discarded merely because a later model can generate replacements; model behavior is nondeterministic, and the accepted images are the evidence of what this workflow achieved.

## Transfer Protocol

To apply the system to another novel, game, film concept, or visual world:

1. Copy the SOP, style-guide structure, plan experiment, and empty registry/catalogue templates into the new project.
2. Select one approved image as the new project's primary visual authority.
3. Replace this novel's canon paths and terminology with the new project's source-of-truth documents.
4. Lock recurring characters, environments, technology, and motifs before generating sequential scenes.
5. Keep generated visual decisions explicitly separate from source canon.
6. Generate one asset per call and reuse accepted references consistently.
7. Record every accepted asset, replacement, dependency, and unresolved continuity risk.
8. Preserve art without generated text until the visual sequence is stable.
9. Add lettering from an auditable specification.
10. Commit milestone states so experiments can proceed without risking the accepted baseline.

## Useful Experiments

Change one production variable at a time and compare against the preserved baseline:

- Primary style reference
- Reference ordering
- Number of reference images
- Canvas orientation
- Continuity-sheet versus full-page composition
- Prompt specificity
- Negative constraints
- Character identity emphasis
- Environmental scale anchors
- Art-first versus text-in-image generation

Do not change canon strictness, manuscript protection, style authority, and multiple visual variables simultaneously. A controlled comparison is more useful than a visually impressive result with unknown causes.

## Commit Context

The repository's preceding `First` commit captured the initial complete production body. This milestone note and the Plan snapshots preserve the method and make that body easier to study, reproduce, and transfer.
