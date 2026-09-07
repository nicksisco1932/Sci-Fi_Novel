# Proposed Fixes Phase 1 - 2026-09-01

Status: proposed audit and correction queue. No candidate in this file is approved for replacement or promotion.

Purpose: correct the highest-propagation visual discrepancies before auditing the full scene corpus. This phase follows `visual_discrepancy_audit_SOP.md`, excludes `concept_sketches/`, preserves every accepted source, and uses versioned candidates for author review.

Author review entry point: `PHASE_1_AUTHOR_REVIEW_2026-09-01.md` links and previews every candidate that still requires a decision without moving or duplicating the production assets.

## Phase 1 Selection

Phase 1 deliberately concentrates on visual authorities and current stress tests:

- all four Chapter 1 wake-up craft/style assets;
- every production character continuity sheet;
- all three Almelah dojo master source/pilot iterations, reviewed as one correction lineage;
- the protected Korin partial-face human-detail reference;
- the current Chapter 13 and Chapter 14 contextual correction candidates.

Eighteen files were inspected at fit-to-page and full-resolution scale. The selection contains one protected reference that passes for its narrow role, eight files with a highest provisional severity of `2`, and nine files with a highest provisional severity of `3`. These scores are evidence for the proposed queue, not automatic permission to edit or replace an asset.

The remaining production sources move to later phases after these locks are corrected. The `82` concept sketches remain excluded. The `50` proof PNGs remain a verification layer after source corrections rather than independent Phase 1 targets.

## Scoring Key

Scores use `0` pass, `1` watch, `2` focused rework, `3` priority rework, and `N/A` not applicable. The asset inherits its highest score; scores are never averaged.

| Code | Gate |
|---|---|
| `MAT` | Material coherence |
| `FAC` | Facial form and identity |
| `DET` | Human microdetail |
| `HND` | Hand and foot anatomy |
| `ANA` | Whole-body anatomy |
| `KIN` | Pose and movement mechanics |
| `CNT` | Contact, balance, and weight |
| `PER` | Perspective, scale, and occlusion |
| `CST` | Character-state continuity |
| `ENV` | Environment and object continuity |
| `LGT` | Lighting and physical causality |
| `PNL` | Panel and action continuity |
| `ART` | Generated artifacts and prohibited content |
| `STY` | Style and readability |

Only nonzero, applicable scores are listed below. Unlisted gates provisionally pass or are not applicable.

## Audit Findings

| ID | Asset | Dimensions | Highest | Nonzero gate scores | Primary evidence and proposed disposition |
|---|---|---:|---:|---|---|
| `A01` | `chapter_01_wakeup/continuity-sheet.png` | `1536x1024` | `2` | `MAT2 FAC2 DET2 HND1 ANA1 CST1 STY1` | Cloudy/etched variation crosses Cassian's scrubs, skin, and attendant uniforms; Cassian's repeated head studies shift subtly in facial planes. Refine as the first dependency root while preserving layout, room, attendants, tools, labels, and foundational line/value grammar. |
| `A02` | `chapter_01_wakeup/page-01.png` | `1024x1536` | `2` | `MAT2 DET2 HND2 ANA1 KIN2 CNT2 STY1` | Skin and fabric carry the shared mottling. The final knife reach has an overlong-looking arm/hand, ambiguous fingertip contact, and weak shoulder-to-hand mechanics. Rework only after `A01` and Cassian's dedicated sheet are corrected. |
| `A03` | `chapter_01_wakeup/page-02.png` | `1024x1536` | `2` | `MAT2 DET2 HND2 ANA2 KIN2 CNT2 PNL1` | The POV hand is bulky and simplified; the choke/knife tableau needs clearer shoulder, wrist, grip, neck contact, stance, and reaction-force logic. Repeated tableau panels should remain narratively continuous without looking mechanically copied. |
| `A04` | `chapter_01_wakeup/page-03.png` | `1024x1536` | `2` | `MAT2 DET2 HND2 ANA1 KIN2 CNT2 PNL1` | Knife grip, throat contact, releasing posture, and kneeling hands require anatomical refinement; skin and cloth still share etched surface noise. Preserve approved lettering and exact story order. |
| `A05` | `characters/cassian-rho/continuity-sheet.png` | `1672x941` | `3` | `MAT3 FAC2 DET3 HND2 ANA2 KIN2 CST2 STY2` | Severe geometric mottling crosses scrubs, arms, neck, and face. Repeated faces vary in nose, cheek, jaw, and age. The defensive pose has questionable extended-hand anatomy, arm length, wrist rotation, and shoulder mechanics. Priority identity/material lock. |
| `A06` | `characters/korin-tal/continuity-sheet.png` | `1672x941` | `2` | `MAT2 FAC1 DET2 HND1 ART2 STY1` | Suit and skin carry low-frequency patterning; small hands are simplified. The schematic contains unreadable generated microtext. Preserve Korin's controlled identity, suit cut, posture, and overall sheet layout while removing accidental lettering and surface noise. |
| `A07` | `characters/alyen-ithra/continuity-sheet.png` | `1672x941` | `3` | `MAT3 FAC3 DET2 HND2 ANA1 KIN2 CNT2 CST2 STY2` | Pale uniform and skin show pervasive marbling. The rage expression becomes a different, over-carved face. Table brace and wall interaction need credible finger spread, palm pressure, wrist alignment, shoulder loading, and contact. Priority identity/material lock. |
| `A08` | `characters/thena/continuity-sheet.png` | `1672x941` | `3` | `MAT3 FAC2 DET2 HND2 ANA2 KIN2 CNT2 CST2 STY2` | Legitimate wear is mixed with shared skin-and-cloth mottling. Head studies shift in facial structure. The grounded crouch has a long support arm, uncertain palm contact, and a pistol grip that needs clearer hand mechanics. Preserve role-specific grime, patched gear, and weapon placement. |
| `A09` | `characters/gor-of-almelah/continuity-sheet-young.png` | `1024x1536` | `3` | `MAT3 FAC2 DET2 HND2 ANA3 KIN3 CNT3 STY2` | Skin and training clothes are heavily marbled. Heroic bulk, oversized hands/feet, the extended-palm stance, and the lower interaction pose require joint-chain, balance, support, and contact review; the lower seated/standing bodies do not resolve cleanly as a physical transition. |
| `A10` | `characters/gor-of-almelah/continuity-sheet.png` | `1024x1536` | `3` | `MAT3 FAC2 DET2 HND2 ANA3 KIN3 CNT3 CST2 STY2` | Armor, sensor weave, cloth, and skin share the artifact. Raised palm, knife grip, running/ready pose, and carried-body study need anatomical and force-path correction. Preserve accepted augmentation geometry, scars, blade, rain state, and young-to-augmented identity. |
| `A11` | `characters/almelah-dojo-master/continuity-sheet.png` | `1024x1536` | `3` | `MAT3 DET2 HND1 ANA1 KIN1 CNT1 STY2` | Original source has severe skin/fabric marbling but retains the strongest identity and geometry authority for this lineage. Keep as source-only evidence; do not promote or overwrite. |
| `A12` | `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot.png` | `1024x1536` | `2` | `MAT2 FAC1 DET1 HND1 STY1` | First pilot reduces broad marbling but retains cloudy trousers and some skin/fabric texture. Preserve only as an iteration record. |
| `A13` | `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot-v2.png` | `1024x1536` | `2` | `MAT1 FAC2 DET2 HND1 STY2` | Second pilot further stabilizes values, but faint angular trouser pattern remains and faces/hair/skin are over-cleaned toward a flatter, more cartoon-like treatment. Use as a material-behavior reference, not a final identity/detail authority. |
| `A14` | `characters/broken-clinic-leader-and-guard/continuity-sheet.png` | `1024x1536` | `3` | `MAT3 FAC2 DET3 HND3 ANA2 CNT2 CST1 STY2` | Shared grime/marbling crosses skin and clothing. The med-kit panel contains oversized, elongated, weakly jointed hands with uncertain contact around the case. Leader and guard faces need stronger separation and continuity. Priority before Chapter 14 page correction. |
| `A15` | `characters/below-the-map-escort/continuity-sheet.png` | `1024x1536` | `3` | `MAT3 FAC2 DET2 HND3 ANA1 KIN2 CNT2 CST2 STY2` | Dense shared texture obscures distinct materials and faces. Stop-palm anatomy, rifle/tool grips, hand-to-object contact, and several role silhouettes need clarification. Preserve differentiated clothing, dampness, tools, and formation roles. |
| `A16` | `experiments/korin-office-meditation/assets/study-02-partial-face.png` | `1024x1536` | `1` | `MAT1 HND1` | Passes for its approved narrow role. Minor etched skin texture and long-finger emphasis should not be copied literally. Preserve unchanged as the reference for pores, fine lines, stubble, hair grouping, brows, lashes, nails, and hand specificity. |
| `A17` | `experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-perspective-v2.png` | `1024x1536` | `3` | `MAT2 FAC3 DET2 HND2 ANA3 KIN3 CNT3 PER2 CST3 PNL2 STY2` | First-panel Thena scale is corrected. The second-row Cassian face remains chunky and etched; raised palm, grapple, impact contact, and final airborne pose need hand/anatomy/movement correction. Cassian's short sleeves and Gor's bulky armor remain continuity drift. Priority after character locks. |
| `A18` | `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-material-refinement-test.png` | `1024x1536` | `2` | `MAT2 FAC1 DET1 HND2 ANA1 KIN1 CNT2 PER1 CST1 STY1` | Material separation is improved, but the leader's wrist-treatment hands remain thick and mechanically ambiguous, with weak palm/finger contact around Thena's bandage. Retain clinic population, light, grime, blocking, and improved faces while correcting treatment mechanics. |

## Source Fingerprints

Use these hashes to verify that audit targets remain unchanged before a proposed correction begins:

| ID | SHA-256 |
|---|---|
| `A01` | `A50B0AB6178167159E0B0AAD2A30DBA825E66532404E44256872D990A49F41D3` |
| `A02` | `262D68A9573013A87DF586F42331A4255A8ED7EAF31EFBEDD8F2CB031304BB4B` |
| `A03` | `DCE5D20749102A0834DE731A5721D1E2B1BEB94D2D18114999E6CC7B14A30ED9` |
| `A04` | `471173EB59C9B39AA8EDE03095494DE33F7EB8859DEA3CD1C884E78ADBA3FBC8` |
| `A05` | `CD3AE8020F28E81EBFC771399CCBA24B101EEA4BA1A804AB496D4CAEB78C14FE` |
| `A06` | `33D86EAE66DCF30C3A0997113A2028F28F20C4BC94D3D00ACC4CC6E19F53ADBB` |
| `A07` | `01296C098CBC44C0E83654C235402C941699C5B9710C7B8ACA54D1FAB91D4C3F` |
| `A08` | `BE4223E8B08BE4D77AAA127D82135320D658208F7C07E9D2F615F6BF09B795F6` |
| `A09` | `991F03A1F1EACBD1723FCA4368C3A8C9DE26841F7CF488FA91718D9059D33C4D` |
| `A10` | `EBFF2C25481771565F88365C323C805F09BC179D2F93772F79929B403CA4C97C` |
| `A11` | `368BAEDD1D8D1767C1A00E0FBE1A35EDB418C4722A55FC669373FABB2CCF4269` |
| `A12` | `D3F71AAFEF17DEAD3D031E62FC88AB536F5AB7846506CD8771B93BEEB2B0065D` |
| `A13` | `1FEE6AAB02394C55282ABA43DEC73481AF2D5B55F5375698EF8EA6B0A7A5E657` |
| `A14` | `0C1B1990FE3058924B7A8EC09472D3B954E6C612A55735048711CE200F5322FB` |
| `A15` | `547703ECBAACFEECECA79C67BBF4DF2810926D93614CE37D850E12C799F19F5D` |
| `A16` | `F09E76C54E49BEE6ACDAFB2D038636CC0A89A0F891668D95C54AF73CE398C33E` |
| `A17` | `6B2EAF4107ED86E4AD76AA57A2A063CFA7F4613AF6E3F05682C5547E4AB46CB8` |
| `A18` | `6228C00772174071036D910AADEFD486C70231B118BD0BCCC720E7D26714C97D` |

## Proposed Fix Queue

Do not execute a task until its listed prerequisites are approved. Each task uses one image-generation call per asset, saves a versioned sibling, and repeats all six SOP inspection passes before author review.

### Authority Locks

- [x] **`PF1-001` - Refine the Chapter 1 combined continuity authority (`A01`).**
  - Priority: dependency root; highest observed severity `2`.
  - Fix: remove uncaused skin/uniform/scrub mottling; stabilize Cassian's face across views; refine visible hands without changing gestures.
  - Preserve: sheet geometry, attendants, room, tools, labels, palette, line clarity, and all production-reference information.
  - Acceptance: every applicable score `0` or `1`; author approves the candidate as a replacement style authority before dependent work.
  - Decision: author approved `chapter_01_wakeup/continuity-sheet-phase1-refinement-v2.png` on `2026-09-01` as the Phase 1 working craft authority. The registered source remains unchanged pending final Phase 1 reconciliation.

- [x] **`PF1-002` - Rebuild Cassian's dedicated continuity candidate (`A05`).**
  - Prerequisite: use `PF1-001` candidate as craft authority only after approval.
  - Fix: coherent scrubs and complexion; one stable face across all views; natural skin/stubble/hair detail; correct extended-hand digits, wrist rotation, arm length, shoulder loading, and defensive movement arc.
  - Preserve: accepted Cassian identity, age, lean build, clothing construction, view layout, expressions, and restrained defensive intent.
  - Acceptance: `MAT`, `FAC`, `DET`, `HND`, `ANA`, `KIN`, and `CST` all `0` or `1`.
  - Decision: author approved `characters/cassian-rho/continuity-sheet-phase1-refinement-v2.png` on `2026-09-01` as the Phase 1 working Cassian authority. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-003` - Rebuild Alyen's continuity candidate (`A07`).**
  - Prerequisite: `PF1-001`.
  - Fix: uniform/skin coherence; keep one face through controlled and furious expressions; correct table-brace and wall-contact hands, wrists, shoulder loading, and reaction force.
  - Preserve: uniform cut, bun, controlled command presence, fury-break intent, interface and wall context.
  - Acceptance: rage remains recognizably Alyen; contacts and joint chains are physically credible; no generated text or symbols.
  - Decision: author approved `characters/alyen-ithra/continuity-sheet-phase1-refinement-v2.png` on `2026-09-01`; the approved action reads as angry removal rather than repair. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-004` - Rebuild Thena's continuity candidate (`A08`).**
  - Prerequisite: `PF1-001`.
  - Fix: separate legitimate grime/wear from shared mottling; stabilize face; correct crouch support arm, grounded palm, balance, pistol grip, and hand-to-tool contact.
  - Preserve: patched gear, armor plates, straps, holster, scarf, dampness, alert posture, and role-specific wear.
  - Acceptance: action poses can be entered and exited physically; gear and injuries remain continuous.
  - Decision: author approved `characters/thena/continuity-sheet-phase1-refinement-v1-canvas-normalized.png` on `2026-09-01` as the Phase 1 working Thena authority. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-005` - Rebuild young Gor's continuity candidate (`A09`).**
  - Prerequisite: `PF1-001`.
  - Fix: coherent skin/training cloth; restrained anatomical mass; correct hands/feet, extended-palm stance, pelvis/ribcage alignment, balance, and lower interaction-pose contact.
  - Preserve: Gor's established size and strength without generic superhero inflation, training clothing, face, hair, and Almelah restraint.
  - Acceptance: no ambiguous limbs or unsupported bodies; martial poses have credible preparation, contact, and recovery paths.
  - Decision: author approved `characters/gor-of-almelah/continuity-sheet-young-phase1-refinement-v2.png` on `2026-09-01` as the Phase 1 young-Gor identity authority, unlocking `PF1-006`. The registered source remains unchanged pending final reconciliation.

- [ ] **`PF1-006` - Rebuild augmented Gor's continuity candidate (`A10`).**
  - Prerequisites: approved `PF1-005` identity and `PF1-001` craft lock.
  - Fix: separate armor, weave, cloth, skin, scar, and rain behavior; correct palms, knife grip, ready/running mechanics, and carried-body weight/support.
  - Preserve: accepted pale composite geometry, sensor weave, scars, blade, augmentation restraint, rain state, and identity continuity with young Gor.
  - Acceptance: armor is consistent across rotations; carried-body study shows explicit support and plausible center of mass.
  - Author score: `D4 H4 C4 F3 A1 M4`; preserve successful anatomy, use medium-brown tight curls, make the face clearly distinct, and correct the distracting material artifact.
  - Reset decision: author recorded `D4` on `2026-09-07`; v7 has a known grid-like skin texture in the face. `characters/gor-of-almelah/candidates/phase1-reset/continuity-sheet-face-material-v8.png` is a targeted sibling candidate preserving v7's layout, anatomy, curls, armor, blade, and rain state. It awaits review. `PF1-014` remains gated until explicit approval.

- [x] **`PF1-007` - Refine Korin's continuity candidate (`A06`).**
  - Prerequisite: `PF1-001`.
  - Fix: remove suit/skin patterning, refine hands, and remove or replace unreadable schematic microtext with text-free functional geometry.
  - Preserve: exact identity, suit cut, controlled posture, expressions, and schematic purpose.
  - Acceptance: Korin remains distinct from the protected detail study's rendering treatment; no accidental lettering.
  - Decision: author approved `characters/korin-tal/continuity-sheet-phase1-refinement-v1.png` on `2026-09-01` as the Phase 1 working Korin authority. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-008` - Rebuild the broken-clinic leader and guard continuity candidate (`A14`).**
  - Prerequisite: `PF1-001`.
  - Fix: separate grime from artifact; stabilize and distinguish both faces; correct med-kit hand size, digits, joints, grip, and contact.
  - Preserve: labor-built leader, uncertain guard, clothing wear, med-kit contents, doorway, lamp, and clinic restraint.
  - Acceptance: med-kit interaction passes `HND`, `ANA`, and `CNT`; both roles remain visually distinct.
  - Decision: author approved `characters/broken-clinic-leader-and-guard/continuity-sheet-phase1-refinement-v2.png` on `2026-09-01` as the Phase 1 working pair authority. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-009` - Rebuild the Below-the-Map escort group candidate (`A15`).**
  - Prerequisite: `PF1-001`.
  - Fix: distinguish skin, masks, damp cloth, leather, metal, and tools; correct stop palm, weapon/tool grips, contact, and role silhouettes.
  - Preserve: older leader, masked watcher, runner, route cloth, differentiated equipment, controlled formation, and environmental wear.
  - Acceptance: every hand-held object has a credible grip and contact point; group identities remain distinct across views.
  - Decision: author approved `characters/below-the-map-escort/continuity-sheet-phase1-refinement-v1.png` on `2026-09-01` as the Phase 1 working escort authority. The registered source remains unchanged pending final reconciliation.

- [x] **`PF1-010` - Produce Almelah dojo master refinement v3 from the full lineage (`A11-A13`).**
  - Prerequisite: `PF1-001`.
  - Source roles: `A11` controls identity, anatomy, pose, garment construction, and layout; `A13` supplies the cleaner material direction; `A16` supplies only human-detail behavior.
  - Fix: remaining trouser pattern, over-cleaned skin/hair, and flattened facial modeling; retain subtle age, pores, fine lines, and material distinction.
  - Preserve: exact older lean identity, all poses, bare feet, wrap construction, expressions, border, and off-white sheet layout.
  - Acceptance: `MAT`, `FAC`, `DET`, `HND`, `ANA`, and `STY` all `0` or `1`; no cartoon or photoreal drift.
  - Decision: author approved `characters/almelah-dojo-master/continuity-sheet-material-refinement-v3.png` on `2026-09-01` as the Phase 1 working dojo-master authority. The registered source and earlier pilots remain unchanged pending final reconciliation.

### Dependent Page Corrections

- [ ] **`PF1-011` - Correct Chapter 1 page 01 (`A02`).**
  - Prerequisites: approved `PF1-001` and `PF1-002`.
  - Fix: material coherence and human detail; final-panel reaching arm, hand, fingertip/knife contact, and shoulder mechanics.
  - Preserve: approved lettering, panel count, POV sequence, attendant, room, interface tool, knife, and timing.
  - Author score: `D3 E2 R1 K1 S4 T1`; retain the reach, contact and text; carry restrained tension mainly in Cassian's final-panel eyes; correct the distracting material artifact.
  - Reset decision: author recorded `D4` on `2026-09-07`; stop iterating on the inherited page. The new shared asset pack is at `chapter_01_wakeup/asset-pack-phase1-reset/`; `chapter_01_wakeup/candidates/phase1-reset/page-01-art-only-v1-canvas-normalized.png` is the first unlettered downstream page candidate and awaits review.

- [ ] **`PF1-012` - Correct Chapter 1 page 02 (`A03`).**
  - Prerequisites: approved `PF1-001` and `PF1-002`.
  - Fix: POV hand anatomy; choke/knife grips, wrists, shoulders, stance, neck contact, reaction force, and pulse progression.
  - Preserve: approved alien-language story beat, panels, room geometry, pulse effect, and attendant identities.
  - Author score: `D5 O5 A5 K5 T1 S2`; rebuild restraint ownership, action mechanics and knife interaction while preserving text.
  - Reset decision: author recorded `D4` on `2026-09-07`; do not continue the inherited page line. Rebuild with the shared room, character, action, and food-knife assets. `chapter_01_wakeup/candidates/phase1-reset/page-02-art-only-v1-canvas-normalized.png` is the first unlettered downstream page candidate and awaits review.

- [ ] **`PF1-013` - Correct Chapter 1 page 03 (`A04`).**
  - Prerequisites: approved `PF1-001` and `PF1-002`.
  - Fix: knife hand/throat contact, release mechanics, kneeling hands, skin/cloth coherence, and panel-to-panel body continuity.
  - Preserve: all approved dialogue/captions, emotional restraint, panel sequence, attendants, room, and dropped knife.
  - Author score: `D5 O5 R1 E2 K1 T5 S5`; rebuild ownership and lettering; preserve release/kneeling and dropped knife; keep emotion controlled; remove dominant surface artifact. Author note: the dialogue did not make sense.
  - Reset decision: author recorded `D4` on `2026-09-07`; accumulated page issues require an art-first rebuild rather than another lettering/action correction. `chapter_01_wakeup/candidates/phase1-reset/page-03-art-only-v1-canvas-normalized.png` is the first unlettered downstream page candidate and awaits review. Manuscript remains unchanged.

- [ ] **`PF1-014` - Correct the Chapter 13 contextual test (`A17`).**
  - Prerequisites: approved `PF1-002`, `PF1-004`, and `PF1-006`.
  - Fix cluster 1: marked second-row Cassian face, neck, stubble, hairline, and shirt texture.
  - Fix cluster 2: raised palm, grapple, Gor/Cassian contact, impact reaction, and final airborne trajectory/limb placement.
  - Fix cluster 3: restore Cassian's approved outerwear and Gor's accepted armor geometry without changing weather or story action.
  - Preserve: corrected first-panel Thena scale, doorway depth, rain, lightning, breach geometry, panel layout, and contextual contrast.
  - Acceptance: consider separate versioned calls if facial, continuity, and movement clusters cannot be corrected without collateral drift; author reviews each stage.

- [ ] **`PF1-015` - Correct the Chapter 14 contextual test (`A18`).**
  - Prerequisites: approved `PF1-002`, `PF1-004`, and `PF1-008`.
  - Fix: leader hand size, digits, palm orientation, wrist support, bandage contact, and treatment posture; remove remaining shared mottling without cleaning away clinic grime.
  - Preserve: improved faces/hair, low practical lighting, patients, beds, med-kit, corridor/clinic geometry, panel order, and restrained interaction.
  - Author score: `D4 H1 M1 G4 L1 P1`, with an explicit request to darken by approximately `10%`; preserve hands, material separation, population and geometry, reduce pervasive grime toward mostly clean, and retain low-light readability.
  - Reset decision: author recorded `D4` on `2026-09-07`; retain the successful armor, fabric separation, character distinction, geometry, and dark exposure. `experiments/visual-language-hierarchy/assets/candidates/phase1-reset/chapter_14_broken_clinic-page-01-contextual-focused-v4.png` is a focused treatment-contact sibling candidate and awaits review.

### Phase Completion Gate

- [ ] **`PF1-016` - Validate and reconcile Phase 1.**
  - Verify source hashes before each edit and candidate hashes/dimensions afterward.
  - Repeat all six visual-discrepancy inspection passes on every candidate.
  - Require all applicable scores to be `0` or `1`; record any residual watch item explicitly.
  - Compare every character candidate to its source and direct dependent pages for identity, costume, equipment, injury, handedness, and geometry drift.
  - Inspect affected proof reproductions only after their source candidates are approved.
  - Update `material_coherence_audit.md`, `asset_registry.md`, experiment notes, and this checklist only after explicit author decisions.
  - Run `git diff --check`, verify all registered paths, inspect Git LFS pointers for new PNGs, and leave canon/manuscript sources unchanged.

## Phase 1 Completion Definition

Phase 1 is complete only when:

- every `PF1` checkbox has evidence-backed completion or an explicit author-approved defer decision;
- no severity `2` or `3` discrepancy remains in the approved Phase 1 candidates;
- the Chapter 1 and character authority hierarchy is internally consistent;
- dependent Chapter 1, Chapter 13, and Chapter 14 candidates have been rechecked against those authorities;
- originals and iteration history remain recoverable;
- no concept sketch has been promoted implicitly;
- no manuscript, lore, or canon term has changed;
- the documentation, registry, dimensions, hashes, LFS state, and Git diff all validate.
