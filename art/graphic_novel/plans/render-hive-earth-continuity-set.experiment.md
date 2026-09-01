# Render Hive Earth Continuity Set - Experiment

Purpose: editable working copy for testing how plan changes affect a new Codex run. The original is preserved in `render-hive-earth-continuity-set.original.md`.

## Experiment Controls

Edit these values first. They have the clearest visible effect.

| Control | Current value | What it changes |
|---|---|---|
| Deliverable count | 2 reference plates | Number of image-generation calls and review surface. |
| Output format | Text-free continuity plates | Whether the result is reusable reference art or a lettered comic page. |
| Canvas | `1024x1536` portrait | Framing, panel density, and composition. |
| Primary style authority | Chapter 1 continuity sheet | Linework, rendering, palette, and production-board treatment. |
| Scale authority | Approved Hive Earth references | Footprint, vertical depth, and population read. |
| Canon strictness | Canon-bound adaptation | Whether visual invention may become lore. Keep this setting unchanged unless canon work is explicitly requested. |
| Generation strategy | Sequential built-in ImageGen | Continuity and iteration behavior. |
| Text policy | No generated text | Prevents garbled lettering and preserves later dialogue control. |
| Documentation | Brief + registry + catalogue | Which production records Codex updates after rendering. |
| Mutation boundary | No manuscript edits | Protects `docs/canonical_md/`. Keep this setting unchanged for art experiments. |

## Summary

Create two text-free reference plates using the approved Chapter 1 graphic-novel style and the current Hive visual briefs:

1. A Hive city exterior and depth study.
2. A planetary view showing discrete Hives and unequal system integration.

Treat every generated design as adaptation material. Do not modify manuscript canon.

## Reference Hierarchy

1. `docs/canonical_md/Chapter 1 – The Return.md` for visible Hive architecture and resident behavior.
2. `docs/canonical_md/Chapter 11 – Contingencies.md` for planetary integration inequality.
3. `art/graphic_novel/chapter_01_wakeup/continuity-sheet.png` for graphic-novel rendering style.
4. `art/graphic_novel/locations/hive-earth/visual-brief.md` for approved scale and structural interpretation.
5. Existing accepted Hive images for continuity, not as immutable compositions.

## Production

### Hive City Plate

- Show a broad multi-kilometer urban body capable of housing approximately 25 million people.
- Establish visible spindle crowns, dense stacked districts, transit depth, and a buried body deeper than the skyline.
- Use pale procedural materials and restrained functional lighting.
- Keep resident behavior calculated and prompt-driven rather than commercial, leisurely, or military.

### Hive Earth Plate

- Preserve natural oceans, continents, atmosphere, clouds, and polar geography.
- Show discrete Hive structures connected through physical corridors and service reach rather than a luminous global grid.
- Distinguish integrated and neglected regions through maintenance, spacing, continuity, and dead infrastructure.

## Documentation

- Update the Hive visual brief only when an approved visual rule changes.
- Update `asset_registry.md` when an asset is accepted or replaced.
- Update `remaining_scene_catalogue.md` only when a scene dependency changes.
- Do not mark Chapter 11 rendered until actual scene pages exist.

## QA

- Inspect every reference before generation.
- Generate one asset per built-in ImageGen call.
- Save accepted outputs inside the repository.
- Confirm exact requested dimensions and text-free output.
- Reject canon drift, style drift, literal hive imagery, invented symbols, and generic cyberpunk treatment.
- Confirm `docs/canonical_md/` remains unchanged.
- Run `git diff --check`.
- Create no commit, push, or Obsidian sync unless separately requested.

## Test Prompt

In a new Codex turn with Plan mode enabled, use:

> Read `art/graphic_novel/plans/render-hive-earth-continuity-set.experiment.md`. Treat it as the working specification. Explain how my changes alter the deliverables, generation prompts, and QA, then produce a revised decision-complete plan. Do not render or edit files yet.
