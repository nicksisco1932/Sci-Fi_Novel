# Layered Visual-Language Experiment Report

## Experiment Record

- Branch: `codex/visual-language-hierarchy-experiment`
- Baseline: `95876ac`
- Renderer: built-in image renderer, one asset per call
- Output format: text-free PNG, `1024x1536`
- Accepted assets modified: none
- Production policy modified: none

The test asks whether Chapter 1 can remain the project's foundational craft authority while accepted scene and location references govern local atmosphere, camera, contrast, texture, and rhythm.

## Inputs And Controls

The pre-generation hashes are preserved in `accepted-assets-before.sha256`. The experiment used these exact reference sets.

### Chapter 14 Variant

1. `art/graphic_novel/chapter_01_wakeup/continuity-sheet.png` - foundational rendering grammar.
2. `art/graphic_novel/characters/cassian-rho/continuity-sheet.png` - Cassian identity.
3. `art/graphic_novel/characters/thena/continuity-sheet.png` - Thena identity and injured hand.
4. `art/graphic_novel/characters/broken-clinic-leader-and-guard/continuity-sheet.png` - clinic personnel.
5. `art/graphic_novel/locations/broken-clinic/landscape-reference.png` - architecture, materials, and local atmosphere.

Comparison authority:

- `art/graphic_novel/scenes/chapter_14_broken_clinic/page-01.png`

### Chapter 13 Variant

1. `art/graphic_novel/chapter_01_wakeup/continuity-sheet.png` - foundational rendering grammar.
2. `art/graphic_novel/characters/cassian-rho/continuity-sheet.png` - Cassian identity.
3. `art/graphic_novel/characters/thena/continuity-sheet.png` - Thena identity and injured hand.
4. `art/graphic_novel/characters/gor-of-almelah/continuity-sheet.png` - augmented Gor identity and equipment.
5. `art/graphic_novel/locations/rain-sector-ambush/landscape-reference.png` - weather, breach, and spatial logic.

Comparison authority:

- `art/graphic_novel/scenes/chapter_13_soft_edge/page-01.png`

### Additional Accepted Regimes Assessed

- `art/graphic_novel/locations/hive-spindle-city/landscape-reference.png`
- `art/graphic_novel/locations/hive-earth/visual-brief.md`

During the experiment, the author confirmed that the accepted Hive plate should be expanded with complementary views rather than replaced. This is consistent with the layered model: an accepted contextual authority can govern a regime while later assets extend its coverage.

## Generated Assets

### Broken Clinic

- Path: `assets/chapter_14_broken_clinic-page-01-contextual.png`
- SHA-256: `09665C9E071FC6B3749E093DB1130F0B102E9CD3C48CDA4CBE5894A767C82422`
- Dimensions: `1024x1536`
- Text: none

Observed contextual changes:

- Stronger warm practical lights against brown-black shadow.
- Denser patched construction and damp surface texture.
- More compressed, human-height framing.
- Increased environmental population and visible clinic function.

Stable invariants:

- Finished linework and controlled rendering.
- Credible anatomy, hands, and spatial construction.
- Cassian and Thena remain recognizable; Thena's bandage remains visible.
- The leader remains labor-built and procedural rather than heroic or villainous.
- Med-kit, cots, crates, cloth, skin, and wet metal remain materially differentiated.

Improvements:

- The setting feels occupied and operational rather than generically ruined.
- Lighting now reads as a property of this improvised clinic rather than a darkened version of the Chapter 1 room.
- Hands, wound handling, and the leader's physical evaluation remain legible despite the low exposure.

Drift and risks:

- The brown-black treatment is close to monochrome and could become monotonous across several pages.
- Dense background detail competes with some of the negative lettering space.
- Reusing this contrast regime outside the clinic would turn a contextual solution into a new universal style.

Assessment: **successful contextual variation**. It preserves foundational craft while giving the location genuine authority.

### Rain Ambush

- Path: `assets/chapter_13_soft_edge-page-01-contextual.png`
- SHA-256: `5BC6159A92A863C55D6F040D396B93E0FC2763E18650C3020F0B8E3D182957B3`
- Dimensions: `1024x1536`
- Text: none

Observed contextual changes:

- Stronger directional rain and wet specular separation.
- Colder blue-gray values, white lightning, and deeper storm blacks.
- Faster panel rhythm and more aggressive camera movement.
- Clear escalation from weather observation to the wall-breaking impact.

Stable invariants:

- Cassian, Thena, and Gor remain recognizable.
- Rain, skin, wet cloth, structural metal, and composite armor retain distinct material behavior.
- The wall breach has coherent before-and-after spatial logic.
- The impact is delivered through Gor's mass rather than an invented energy effect.

Improvements:

- Rain behaves as a physical force instead of a decorative overlay.
- The lightning and wet deck provide excellent action readability.
- Gor's arrival has weight and the sequence reads without captions.

Drift and risks:

- Cassian's approved outerwear is simplified into a short-sleeved shirt. Costume and equipment therefore need to be named explicitly as higher-order continuity, not left implicit under identity.
- Gor's pale composite armor becomes bulkier and more conventional than the accepted reference.
- The final airborne pose approaches superhero staging even though the initiating collision is physically legible.
- Repeated lightning and dense rain reduce quiet negative space and could overpower dialogue on a lettered page.

Assessment: **useful but not replacement-ready**. The contextual authority succeeds, but the variant exposes higher-order costume, equipment, and impact-physics constraints that require stronger locks.

## Cross-Regime Findings

1. Chapter 1 works well as a craft authority when its palette and lighting are not treated as universal.
2. Contextual references materially improve environmental specificity, especially practical lighting, weather, texture, and camera behavior.
3. Character identity must explicitly include costume, equipment, augmentation geometry, and current injury state.
4. Physical credibility must govern both static anatomy and the complete motion path of an impact.
5. Contextual authority should extend accepted regimes with additional views; it should not silently replace an accepted asset.
6. A successful local treatment must not become a new global default.

## Recommendation

Adopt the layered authority model **with strengthened continuity wording** after review. The policy should explicitly place costume, equipment, augmentation geometry, and injury state under canon and identity, and should state that accepted contextual assets are expanded rather than superseded unless replacement is separately approved.

Recommended final wording:

> `chapter_01_wakeup/continuity-sheet.png` establishes the project's foundational rendering grammar: linework restraint, anatomical credibility, material specificity, perspective coherence, physical plausibility, and production finish. It does not impose a universal palette, lighting scheme, contrast structure, texture density, camera language, or panel rhythm. Canon and identity govern content, including face, body, costume, equipment, augmentation geometry, injury state, chronology, and established technology. Accepted references directly relevant to location, era, character state, and scene function may govern variable atmosphere and local cinematography. Scene-specific departures must be traceable to manuscript context and may not override higher authorities. Accepted contextual assets should be expanded with complementary views, not silently replaced. When authorities conflict, canon and identity govern content; foundational grammar governs craft; contextual references govern atmosphere and local cinematography. New treatments remain experimental until compared and approved.

## Generation Specifications

The prompts below are retained so the test can be repeated or ablated without reconstructing its assumptions.

### Chapter 14 Prompt

```text
Use case: illustration-story
Asset type: experimental graphic-novel page variant, art only
Primary request: Create one complete portrait graphic-novel page for the opening of Chapter 14, Broken Clinic. This is a context-authority experiment, not a redesign. Preserve the approved characters, clothing, physical setting, and production quality from the references.
Reference roles: Image 1 is the foundational rendering grammar for restrained linework, credible anatomy, materials, perspective, and finished page discipline. Image 2 locks Cassian Rho's face, build, hair, coat, and physical presence. Image 3 locks Thena's face, build, clothing, and wounded/bandaged hand. Image 4 locks the broad clinic leader and entrance guard. Image 5 governs the broken clinic's architecture, patched construction, damp surfaces, lanterns, and spatial logic.
Scene sequence: Cassian and Thena descend a dark wet corridor toward a scavenged clinic; Thena protects her wounded bandaged hand. A crooked doorway and weak pulsing practical lantern reveal thin patients on improvised cots among crates, with coolant damp and patched metal. At the entrance a guarded man assesses them while Cassian subtly blocks his view of Thena. Inside, the broad clinic leader in a greasy work jacket takes Thena's wrist without asking beside a plain med-kit.
Composition/framing: 1024x1536 portrait page, five or six clearly separated panels, coherent left-to-right/top-to-bottom sequence, compressed interior framing, readable hands and faces, deliberate blank negative space suitable for later lettering without adding text.
Style/medium: finished cinematic graphic-novel illustration; fine disciplined ink and controlled painterly values. Match Chapter 1's craft and finish, not its sterile palette.
Lighting/mood: contextual broken-clinic authority; low-key brown-black interior with warm impure amber practical lights, damp green-gray undertones, constrained pools of visibility, heavy pressure without losing shadow detail.
Materials/textures: wet patched metal, worn work cloth, cheap medical plastics, coolant condensation, crates, improvised cots, human skin; every material physically specific and consistent.
Text: none.
Constraints: text-free; exact 1024x1536 portrait; realistic anatomy and hand geometry; Cassian and Thena identities stable; Thena's hand injury readable but non-graphic; leader labor-built rather than heroic; no canon additions.
Avoid: speech balloons, captions, signs, lettering, logos, watermarks, gore, villain caricature, generic ruined-city grime, neon cyberpunk, fantasy styling, superhero poses, extra weapons, faction insignia, crushed unreadable blacks, loose concept-art finish.
```

### Chapter 13 Prompt

```text
Use case: illustration-story
Asset type: experimental graphic-novel page variant, art only
Primary request: Create one complete portrait graphic-novel page for the opening of Chapter 13, Soft Edge. This is a context-authority experiment, not a redesign. Preserve the approved characters, armor, clothing, physical setting, and production quality from the references.
Reference roles: Image 1 is the foundational rendering grammar for restrained linework, credible anatomy, material specificity, coherent perspective, and finished page discipline. Image 2 locks Cassian Rho's face, build, hair, coat, and physical presence. Image 3 locks Thena's face, build, clothing, and wounded/bandaged hand. Image 4 locks augmented Gor's harsh face, massive upper body, pale composite armor, dark sensor weave, and physical weight. Image 5 governs the rain-sector overhang, wet deck, wall breach, drainage, and spatial logic.
Scene sequence: Cassian steps out into real hard rain and registers the physical weather while Thena waits under a broken overhang. A vibration through the deck becomes approaching heavy footfalls. Cassian raises one hand for quiet. Lightning reveals the wet corridor. Augmented Gor explodes from concealment and drives a brutally weighted shoulder into Cassian, throwing him through a weak metal wall as Thena reacts from cover. End on Cassian amid the breached wall, pain and rain obscuring his view but without gore.
Composition/framing: 1024x1536 portrait page, five or six clearly separated panels, coherent left-to-right/top-to-bottom sequence, dynamic but spatially legible camera placement, realistic impact progression, faces and hands readable, deliberate blank negative space suitable for later lettering without adding text.
Style/medium: finished cinematic graphic-novel illustration; fine disciplined ink and controlled painterly values. Match Chapter 1's craft and finish, not its sterile palette or measured camera.
Lighting/mood: contextual harsh-weather authority; cold blue-gray rain, near-black wet metal, sharp white lightning, hard wet specular separation, deep storm pressure, no neon.
Materials/textures: directional rain, standing water, wet cloth, composite armor, sensor weave, stressed structural metal, shattered weak wall panels; every material physically specific.
Text: none.
Constraints: text-free; exact 1024x1536 portrait; stable Cassian, Thena, and Gor identities; realistic anatomy and collision geometry; Gor's force comes from mass, acceleration, and planted mechanics; Cassian is thrown by a surprise impact, not an energy effect; non-graphic injury; no canon additions.
Avoid: speech balloons, captions, signs, lettering, logos, watermarks, gore, superhero posing, acrobatics, speed trails, energy effects, fantasy styling, neon cyberpunk, extra combatants, extra weapons, faction insignia, illegible rain, broken anatomy, loose concept-art finish.
```

## Compute Checkpoint Follow-Up

The persistent reasoning-effort checkpoint remains a separate follow-up for `main`. It was not implemented, staged, or committed as part of this experiment.
