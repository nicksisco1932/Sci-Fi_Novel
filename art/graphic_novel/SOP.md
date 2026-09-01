# Graphic Novel Generation SOP

Purpose: keep graphic-novel generation canon-bound, reusable, and fast enough to scale across the manuscript.

Generated art is adaptation material. It does not canonize faces, costumes, room designs, props, or landscapes unless a later manuscript or lore pass explicitly says so.

## Source Order

Use sources in this order before generating or revising any image:

1. `docs/canonical_md/` for active manuscript scene text.
2. `docs/lore_registry.md` for canon names, locations, technology, constraints, and world texture anchors.
3. `docs/canonical_md/Current Timeline Summary.md` for chapter order and event context.
4. `docs/character_dossiers/` for character behavior, role, and relationship constraints.
5. `art/graphic_novel/style_guide.md` for the approved Chapter 1 graphic-novel style.
6. Existing files under `art/graphic_novel/` for visual continuity.

Do not use Obsidian vault files as the source unless the task explicitly asks for Obsidian sync or comparison.

## Directory Layout

Save generated assets under `art/graphic_novel/`:

| Asset type | Default path |
|---|---|
| Character continuity sheet | `characters/<slug>/continuity-sheet.png` |
| Character variants | `characters/<slug>/variant-##.png` |
| Location or landscape reference | `locations/<slug>/landscape-reference.png` |
| Tech or prop reference | `tech/<slug>/reference.png` |
| Visual motif reference | `motifs/<slug>/reference.png` |
| Lore scene plate | `lore/<topic>/<slug>.png` |
| Rendered scene pages | `scenes/chapter_##_<scene_slug>/page-##.png` |
| Scene-specific combined set | `chapter_##_<scene_slug>/` |

The existing wake-up render remains in `chapter_01_wakeup/` until a later reorganization is explicitly requested.

## Asset Statuses

Use these exact statuses in `asset_registry.md`:

| Status | Meaning |
|---|---|
| Available | A usable generated asset already exists in the repo. |
| Style Reference | An approved asset defines house style and should be used as a reference. |
| Needs Continuity Sheet | A recurring character or role needs a reusable sheet before more scene pages. |
| Needs Landscape Render | A recurring place or environment needs a stable reference image. |
| Needs Tech Render | A recurring object, interface, vessel, or system needs a stable reference image. |
| Needs Motif Render | A recurring symbolic or visual language needs a stable reference image. |
| Needs Scene Render | A page or sequence should be generated after required references exist. |
| Needs Style Rerender | A generated asset exists but does not match the approved Chapter 1 style closely enough. |
| Deferred | Not worth rendering yet under the current filter. |
| Canon Check Needed | The manuscript does not yet give enough visual permission, or rendering would risk spoiling or prematurely fixing a reveal. |

## Render Filter

Render an asset when at least one condition is true:

- It is a named or recurring character.
- It is a major location or landscape used across scenes.
- It is a recurring technology, prop, interface, vessel, alert state, or visual motif.
- It affects blocking, threat, identity, navigation, or reader comprehension.
- It must stay visually consistent across multiple pages.

Defer an asset when it appears once, is visually generic, can be handled by a scene prompt, or would take time without improving continuity.

Do not render a scene page until the necessary character and location references are `Available` or explicitly marked as provisional.

## Generation Workflow

For each scene:

1. Identify the source span in `docs/canonical_md/` and extract only visible, audible, or directly staged details.
2. Check `asset_registry.md` for required characters, locations, tech, props, and motifs.
3. Check `style_guide.md` and include Chapter 1 style references in the prompt when supported.
4. Generate or update missing continuity sheets before rendering pages.
5. Build a compact storyboard with panel count, panel purpose, exact dialogue or captions, and required references.
6. Render pages in short batches, preserving the same references and style language.
7. Review for style drift and canon drift before accepting the page.
8. Save accepted images under the appropriate `art/graphic_novel/` directory.
9. Update `asset_registry.md` with the new status, path, source, and notes.

## Prompt Discipline

Prompts should preserve the manuscript's restraint:

- Match the Chapter 1 wake-up render style: sophisticated painted graphic-novel realism, clean restrained ink contours, readable faces, controlled values, and low-saturation color.
- For reference assets, match `chapter_01_wakeup/continuity-sheet.png` specifically: off-white production board, separated panels, fine linework, controlled hatching, and readable material studies.
- Use controlled care, containment, procedural order, damaged infrastructure, and human suspicion where the canon calls for them.
- Avoid heroic gloss, melodrama, overt prison imagery, gore, villainous exaggeration, extra guards, and explanatory visual symbolism unless present in the source.
- Keep Hive spaces precise, friction-managed, symmetrical, bright, and sterile without making them cartoonishly evil.
- Keep Lower Grid and Below the Map spaces inhabited, adaptive, repaired, and locally governed rather than empty ruins.
- Treat the Reversionist's intervention as competent but bounded by damaged infrastructure.
- Do not accept dark archival concept-art drift as final, even for lore scenes.

When adding visible text to a page, use only manuscript dialogue, captions, sound effects, or short labels needed by the graphic-novel format. Do not add new exposition.

## Review Checklist

Before marking an asset `Available`, check:

- Canon terms match `docs/lore_registry.md`.
- Style matches `style_guide.md` and the Chapter 1 wake-up reference set.
- The image does not add plot, lore, faction markings, visible injuries, restraints, weapons, or relationships not present in the source.
- Character posture and expression fit the dossier or scene behavior.
- Locations preserve their world-texture guardrails.
- Tech matches its stated limits and does not become omnipotent.
- Dialogue and captions are spelled correctly and do not replace manuscript wording with summary.
- Page sequence reads clearly without requiring non-canon explanation.

If a visual choice could become canon-significant, mark the asset `Canon Check Needed` instead of treating it as final.
