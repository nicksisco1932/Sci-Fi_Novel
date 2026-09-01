# Render Hive Earth Continuity Set

Backup status: immutable snapshot of the plan shown in the Codex sidebar.

## Summary

Create two text-free `1024x1536` reference plates in the approved Chapter 1 graphic-novel style:

1. **Spindle city exterior**, based on Chapter 1's physical description.
2. **Planetary Hive integration map**, based on Chapter 11's system-wide description.

These are adaptation assets only. Do not modify manuscript canon.

## Production

### Spindle City Exterior

Save to `art/graphic_novel/locations/hive-spindle-city/landscape-reference.png`.

Compose a portrait reference plate showing:

- A central spindle surrounded by disciplined columns of white towers.
- Stacked districts connected by precisely timed elevation rails.
- Aligned yellow-white window bands differentiated by residential, work, and medical functions.
- Pale vapor rising through spindle crowns from the infrastructure concealed below.
- Amber, pressure-sealed avenues at lower levels.
- Treated rain running down executive glass into controlled runoff channels.
- Residents moving with procedural efficiency rather than military discipline.

The result should feel friction-managed, immense, and inhabited. Avoid literal honeycomb imagery, insect motifs, architectural ornament, cyberpunk neon, utopian gloss, and generic dystopian decay.

### Planetary Integration Map

Save to `art/graphic_novel/motifs/hive-integration-density-planetary-map/reference.png`.

Compose a portrait reference plate showing:

- A recognizable Earth with oceans, atmosphere, clouds, and regional geography.
- A dense integration mesh spanning the planet without replacing its natural surface.
- Bright, uninterrupted core systems around Spindle 1, the Arkline Arcologies, and Equatorial Core Belts.
- Fragmented service paths and dead nodes around Spindles 22 and 31, the Polar Grids, and other degraded regions.
- Detail studies contrasting anticipatory core services with failing identity, medical, food, translation, and checkpoint systems.

Do not depict a metal-encased planet, national borders, readable labels, propaganda symbols, planetary destruction, or a uniformly functional network.

## Documentation

Create `art/graphic_novel/locations/hive-earth/visual-brief.md` containing:

- Chapter 1 and Chapter 11 source anchors.
- The distinction between the Hive as a civilizational system and individual Spindles.
- Canon requirements and adaptation-only design decisions.
- Prohibited literal-hive and generic dystopian imagery.

Update the asset registry and remaining-scene catalogue:

- Mark the Spindle city exterior and planetary integration map available.
- Mark Chapter 11's integration-map dependency available.
- Keep Central Cognition, Spindle 31, and other dedicated location designs outstanding.
- Do not mark Chapter 11 itself rendered.

## QA

- Generate sequentially with the built-in image renderer, reusing the Chapter 1 continuity sheet and existing Hive interior references.
- Confirm both assets are text-free and exactly `1024x1536`.
- Verify the city plate incorporates the Chapter 1 architectural, lighting, vapor, transit, and rain details.
- Verify the planetary plate preserves oceans and atmosphere while communicating unequal system integration.
- Reject literal insect imagery, invented insignia, garbled lettering, metal-shell Earth, cyberpunk drift, or a uniformly ruined Hive.
- Confirm `docs/canonical_md/` remains unchanged and run `git diff --check`.
- Create no commit, push, or Obsidian sync.
