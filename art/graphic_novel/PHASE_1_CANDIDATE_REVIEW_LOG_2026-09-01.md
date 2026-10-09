# Phase 1 Candidate Review Log - 2026-09-01

Author-facing review entry point: `PHASE_1_AUTHOR_REVIEW_2026-09-01.md`.

Status: active correction log. Entries marked `Candidate review` are not approved replacements and must not be propagated into dependent assets until the author explicitly approves them.

This log records the evidence required by `visual_discrepancy_audit_SOP.md` without changing the approval checkboxes in `PROPOSED_FIXES_PHASE_1_2026-09-01.md`.

## PF1-001 - Chapter 1 Combined Continuity Authority

### Immutable Source

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/continuity-sheet.png` |
| SHA-256 | `A50B0AB6178167159E0B0AAD2A30DBA825E66532404E44256872D990A49F41D3` |
| Dimensions | `1536x1024` |
| Role | Primary Chapter 1 character, craft, room, attendant, equipment, and graphic-language authority. |
| Authorities | Source controls all layout, identities, poses, proportions, garments, room geometry, props, labels, palette, and line/value grammar. `experiments/korin-office-meditation/assets/study-02-partial-face.png` controls only fine human-detail behavior. |
| Duplicate paths | None used. |
| Dependencies | `PF1-002` through `PF1-015`; all dependent character and page candidates remain gated. |

The source hash was rechecked before both image-generation edits and remained unchanged.

### v1 - Rejected Iteration

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/continuity-sheet-phase1-refinement-v1.png` |
| SHA-256 | `3A148A232AD9517AADCF688D8A3C13C4E271C3C1A3B20B50B130B35E80260BF8` |
| Dimensions | `1536x1024` |
| Prompt summary | Preserve the source pixel-close while removing uncaused cloudy, marbled, camouflage-like, geometric, and watercolor surface variation; stabilize Cassian's repeated face; refine visible hands; use the Korin study only for pores, fine lines, stubble, hair grouping, nails, and restrained human specificity. |
| Six-pass result | Fit-to-page composition and continuity passed. Full-resolution comparison found persistent low-frequency tonal islands across Cassian's trousers and the attendants' pale sleeves and trouser legs. No label, object, room, or prohibited-content failure was observed. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA0 KIN0 CNT0 PER0 CST0 ENV0 LGT0 PNL0 ART0 STY1` |
| Status | `Focused rework`; retained only as an iteration record. Not eligible for approval or propagation. |

### v2 - Approved Working Authority

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/continuity-sheet-phase1-refinement-v2.png` |
| SHA-256 | `E256B4E9F8B87EFAFBBC4CA4FC5F0D2C43444370346229A302C406DD28085A91` |
| Dimensions | `1536x1024` |
| Prompt summary | Use v1 as the edit target and the original as immutable geometry/identity authority; decisively remove low-frequency tonal islands from dark scrubs, pale uniforms, and skin while retaining only construction-, fold-, contact-, wear-, anatomy-, and light-caused variation. Preserve all labels verbatim and all nonmaterial content pixel-close. |
| Correction boundary | Rendering of Cassian's scrubs and skin, attendant uniforms and skin, repeated facial detail, and visible hand detail only. |
| Hard invariants | Exact sheet dimensions and composition; all borders, panels, figures, poses, proportions, faces, garment construction, visors, room architecture, bed, tray, knife, interface tools, closeups, palette, and the labels `CASSIAN`, `ATTENDANT A`, `ATTENDANT B`, `HIVE SPINDLE 9`, and `LINGUISTIC INTERFACE`. |
| Pass 1 - fit-to-page | Pass. Panel order, figure scale, silhouettes, tonal hierarchy, and production-reference readability remain intact. |
| Pass 2 - full-resolution human inspection | Watch. Cassian remains identifiable across views; faces, stubble, hair grouping, hands, and nails are clearer without photoreal drift. Small hand scale limits certainty, but no malformed or fused digit is visible. |
| Pass 3 - anatomy and movement | Pass. Static poses, joint chains, balance, and hand placement remain consistent with the source; no pose or proportion was materially changed. |
| Pass 4 - continuity and geometry | Pass. Attendants, garments, room, bed, tray, knife, interface tools, object scale, and relative locations remain recognizable and stable. |
| Pass 5 - material, light, and environment | Watch. The shared cloudy surface treatment is substantially reduced. Remaining cloth variation follows seams, folds, overlap, knees, cuffs, and directional form shading closely enough to retain as `MAT1` pending author inspection. |
| Pass 6 - artifact and content sweep | Pass. The five required labels are legible and correctly spelled. No added text, numbers, logos, signatures, insignia, watermarks, unexplained symbols, gore, unintended color, duplicated figures, or fused objects were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA0 KIN0 CNT0 PER0 CST0 ENV0 LGT0 PNL0 ART0 STY1` |
| Status | `Approved working authority`; author approved this candidate on `2026-09-01` for Phase 1 propagation. It does not replace the registered production source until final reconciliation. |

### Tool And Preservation Record

- Both candidates were produced through the built-in image-generation edit workflow, one call per version.
- The source was never overwritten.
- Both candidates are versioned siblings and are covered prospectively by the `art/graphic_novel/**/*phase1*.png` Git LFS rule.
- No candidate has been staged, committed, pushed, registered as `Available`, or promoted into a style or continuity hierarchy.
- No manuscript, lore, canon, or Obsidian source was changed.

## Queue Readiness Check

All `18` Phase 1 audit inputs (`A01-A18`) were rechecked on `2026-09-01` against the fingerprints and dimensions recorded in `PROPOSED_FIXES_PHASE_1_2026-09-01.md`. All `18` paths resolved, all `18` SHA-256 hashes matched, and all `18` dimensions matched. This readiness check does not approve any candidate or waive the prerequisite order.

## PF1-002 - Cassian Dedicated Continuity Candidate

### Immutable Source And Authorities

| Field | Record |
|---|---|
| Asset | `characters/cassian-rho/continuity-sheet.png` |
| SHA-256 | `CD3AE8020F28E81EBFC771399CCBA24B101EEA4BA1A804AB496D4CAEB78C14FE` |
| Dimensions | `1672x941` |
| Role | Dedicated Cassian identity, rotation, expression, costume, and defensive-pose source. |
| Authorities | Source controls layout and pose inventory. Approved `chapter_01_wakeup/continuity-sheet-phase1-refinement-v2.png` controls Cassian identity and craft. The protected Korin partial-face study controls only fine human-detail behavior. |
| Dependencies | Chapter 1 pages and the Chapter 13 contextual test remain gated on author approval of the final candidate. |

### v1 - Rejected Iteration

| Field | Record |
|---|---|
| Generated asset | `characters/cassian-rho/continuity-sheet-phase1-refinement-v1.png` |
| Generated dimensions | `1670x941` |
| Generated SHA-256 | `A1CEA7CD90A3B64F7AD484702E0949C67F880AAA1915BAED8B7B6D7BC76AA11E` |
| Canvas-normalized evidence | `characters/cassian-rho/continuity-sheet-phase1-refinement-v1-canvas-normalized.png`, `1672x941`, SHA-256 `746AF93681AC52967343018023D470A0F945312279136D7070ADC8A1A816D038` |
| Finding | Identity and neutral anatomy improved, but angular tonal islands remained across the scrubs and the page-right defensive arm remained too straight and visually overlong. |
| Residual scores | `MAT2 FAC1 DET1 HND2 ANA1 KIN2 CNT1 CST1 STY1` |
| Status | `Focused rework`; preserved as iteration evidence and not eligible for propagation. |

The one-pixel columns added to each side of the v1 canvas-normalized evidence duplicate the existing outer edge pixels; no illustrated content was rescaled or regenerated.

### v2 - Candidate Review

| Field | Record |
|---|---|
| Asset | `characters/cassian-rho/continuity-sheet-phase1-refinement-v2.png` |
| SHA-256 | `394F6A182665CA1E3FD009E14DCC7A4309CD980787186B2C03C29D1C77C98E01` |
| Dimensions | `1672x941` |
| Prompt summary | Use v1 as edit target, original as immutable layout authority, approved PF1-001 as identity/craft authority, and the Korin study only for fine human detail. Remove the remaining false cloth/skin pattern and shorten the page-right defensive reach with a modest elbow flex, continuous joint chain, natural wrist, and five-digit open palm. |
| Pass 1 - fit-to-page | Pass. View count, hierarchy, silhouette clarity, scale, and negative space remain intact. |
| Pass 2 - full-resolution human inspection | Watch. All repeated faces read as one Cassian; stubble, hair, hands, nails, and skin retain restrained specificity. |
| Pass 3 - anatomy and movement | Watch. Neutral rotations remain proportionate. The action arm is shorter, slightly flexed, and recoverable; both guarding hands have plausible joint chains and five-digit structure. |
| Pass 4 - continuity and geometry | Pass. Layout, rotations, expression inventory, garment construction, footwear, and crop remain stable. |
| Pass 5 - material, light, and environment | Watch. Scrubs now read as one coherent charcoal cloth with remaining variation localized to construction, folds, overlap, and form light. Skin and cloth no longer share the original broad geometric artifact. |
| Pass 6 - artifact and content sweep | Pass. No text, symbols, logos, insignia, watermarks, extra views, fused digits, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ART0 STY1` |
| Status | `Approved working authority`; author approved on `2026-09-01`. Eligible for Phase 1 dependent-page propagation; the registered source remains unchanged pending final reconciliation. |

## PF1-003 - Alyen Dedicated Continuity Candidate

### v1 - Superseded Candidate

| Field | Record |
|---|---|
| Source | `characters/alyen-ithra/continuity-sheet.png`, SHA-256 `01296C098CBC44C0E83654C235402C941699C5B9710C7B8ACA54D1FAB91D4C3F`, `1672x941` |
| Generated evidence | `characters/alyen-ithra/continuity-sheet-phase1-refinement-v1.png`, `1671x941`, SHA-256 `5BE053071F00F7718931AC1C7536992E76DCADE5D99C7E8CCA6C6DE96A902341` |
| Review candidate | `characters/alyen-ithra/continuity-sheet-phase1-refinement-v1-canvas-normalized.png`, `1672x941`, SHA-256 `A7AA17831E5E55990A884498DE7D0CE65692D9654A2AAD9BFEC708A7E2D95313` |
| Authorities | Source controls layout, uniform, poses, label, table, and damaged-wall mechanism. Approved PF1-001 controls craft. The protected Korin study controls only fine human-detail behavior. |
| Prompt summary | Remove pale-fabric and skin marbling; keep one identity through neutral, downward-control, and furious expressions; preserve the uniform and bun; make both table palms bear weight with aligned wrists and give the wall interaction two explicit, force-aligned hand contacts. |
| Canvas note | The review candidate duplicates the generated image's final outer-edge column once. No illustrated content was rescaled or regenerated. |
| Pass 1 - fit-to-page | Pass. Label, view hierarchy, figure scale, action panels, and negative space remain stable. |
| Pass 2 - full-resolution human inspection | Watch. Alyen's facial structure remains consistent through the fury study; hair, skin, fingers, and nails retain restrained specificity. |
| Pass 3 - anatomy and movement | Watch. Table fingers spread under load, palms meet the plane, wrists align with forearms, and the shoulders transmit the forward brace. Wall hands act on separate components with plausible force direction. |
| Pass 4 - continuity and geometry | Pass. Uniform tailoring, bun, table, interface geometry, wall breach, mechanism, and panel placements remain intact. The label remains `ALYEN ITHRA`. |
| Pass 5 - material, light, and environment | Watch. Pale cloth and skin are materially separated; remaining variation follows seams, folds, contact, anatomy, and room light. |
| Pass 6 - artifact and content sweep | Pass. No new text, symbols, logos, insignia, watermarks, fused digits, extra figures, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ART0 STY1` |
| Status | `Superseded`; internally acceptance-compliant for the original correction brief, but rejected after author feedback because the damaged-wall pose read as careful repair rather than angry removal. |

### v2 Action-Corrected Candidate

| Field | Record |
|---|---|
| Asset | `characters/alyen-ithra/continuity-sheet-phase1-refinement-v2.png` |
| SHA-256 | `6169D1312FF4578CE4FF815CA05C04DD87EA2A31459CE971176B246EBD3DCC93` |
| Dimensions | `1672x941` |
| Author correction | The damaged-wall action must show Alyen angry and ripping the assembly out, not frustrated while repairing it. |
| Prompt summary | Preserve the normalized v1 sheet pixel-close outside the bottom-right panel. Hook both hands onto rigid chassis edges, load elbows and shoulders backward, shift her torso away from the wall, tilt the partly detached assembly toward her, and show strained cables, bent fasteners, cracked plaster, and restrained falling fragments. |
| Six-pass result | Fit-to-page hierarchy and all unchanged reference views pass. Full-resolution inspection confirms both hands take forceful purchase on the chassis. The wall-to-hands-to-elbows-to-shoulders vector, displaced housing, strained cables, and debris now communicate removal immediately. Identity, uniform, table-brace pose, label, materials, and other geometry remain stable. No prohibited content was observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ENV1 ART0 STY1` |
| Status | `Approved working authority`; author approved on `2026-09-01`. The action correction reads as angry removal rather than repair; the registered source remains unchanged pending final reconciliation. |

## PF1-004 - Thena Dedicated Continuity Candidate

| Field | Record |
|---|---|
| Source | `characters/thena/continuity-sheet.png`, SHA-256 `BE4223E8B08BE4D77AAA127D82135320D658208F7C07E9D2F615F6BF09B795F6`, `1672x941` |
| Generated evidence | `characters/thena/continuity-sheet-phase1-refinement-v1.png`, `1671x941`, SHA-256 `56BD0F5BAB4AE4C7D4DA4FB4FEE686340A7BD00AB14BCF528FCA208D935F788F` |
| Review candidate | `characters/thena/continuity-sheet-phase1-refinement-v1-canvas-normalized.png`, `1672x941`, SHA-256 `EFFCB518EF38722489F73B615B7F52C5F3068D8DCEAF93667E2B5A5E1A7BBF23` |
| Authorities | Source controls identity, layout, patched gear, armor, scarf, holster, pistol, repair device, and action intent. Approved PF1-001 controls craft. The Korin study controls fine human detail only. |
| Prompt summary | Separate real grime, dampness, edge wear, and repairs from the shared surface artifact; distinguish cloth, leather, armor, metal, hair, and skin; stabilize Thena's face; correct repair-tool contacts, pistol grip, and the grounded crouch's support arm, palm, balance, and joint chain. |
| Canvas note | The review candidate duplicates the generated image's final outer-edge column once. No illustrated content was rescaled or regenerated. |
| Pass 1 - fit-to-page | Pass. Label, view hierarchy, silhouettes, gear readability, and action studies remain intact. |
| Pass 2 - full-resolution human inspection | Watch. Face, damp hair, skin, hands, glove construction, and nails remain specific and consistent. |
| Pass 3 - anatomy and movement | Watch. The crouch forms a credible planted-foot/grounded-knee/support-palm tripod; shoulder, elbow, wrist, and palm align; the pistol hand maintains a full low-ready grip. Repair hands engage separate components. |
| Pass 4 - continuity and geometry | Pass. Patched equipment, armor, straps, holster, scarf, pouches, torn cloth, pistol, repair device, and label `THENA` remain stable. |
| Pass 5 - material, light, and environment | Watch. Meaningful dirt, dampness, chipped edges, and repairs remain localized; cloth, leather, plate, metal, skin, and hair no longer share one decorative pattern. |
| Pass 6 - artifact and content sweep | Pass. No new text, symbols, logos, insignia, watermarks, fused digits, missing equipment, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ART0 STY1` |
| Status | `Approved working authority`; author approved on `2026-09-01`. Eligible for Phase 1 dependent-page propagation; the registered source remains unchanged pending final reconciliation. |

## PF1-005 - Young Gor Dedicated Continuity Candidate

### v1 - Superseded Anatomy Candidate

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-young-phase1-refinement-v1.png` |
| SHA-256 | `366922450583329561708D0F7A04990742C25083EC0F8F53971CFA3F90196293` |
| Dimensions | `1024x1536` |
| Result | Corrected hand/foot scale, open-palm joint chain, and lower training/recovery contact, but retained broad faceted tonal islands across the pale trousers. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA1 KIN1 CNT1 STY1` |
| Status | `Superseded`; retained as anatomy-correction evidence only. |

### v2 - Candidate Review

| Field | Record |
|---|---|
| Source | `characters/gor-of-almelah/continuity-sheet-young.png`, SHA-256 `991F03A1F1EACBD1723FCA4368C3A8C9DE26841F7CF488FA91718D9059D33C4D`, `1024x1536` |
| Asset | `characters/gor-of-almelah/continuity-sheet-young-phase1-refinement-v2.png` |
| SHA-256 | `39CB3EC6C8BC74C21C10A6220B1CE465BC07F0C227F4679D2BF6366191D73183` |
| Dimensions | `1024x1536` |
| Authorities | Source controls identity, layout, rotation/expression inventory, garments, and action intent. v1 controls corrected anatomy/contact. Approved PF1-001 controls craft. The Korin study controls fine human detail only. |
| Prompt summary | Preserve v1's corrected geometry and interaction pixel-close while removing broad faceted/marbled patterning from pale trousers, dark wrap tops, and skin; retain only construction-, fold-, contact-, anatomy-, and light-caused variation. |
| Pass 1 - fit-to-page | Pass. Five rotations, four portraits, three lower studies, scale, hierarchy, and silhouettes remain intact. |
| Pass 2 - full-resolution human inspection | Watch. One identity persists; hands, bare feet, toes, nails, stubble, hair, and skin retain restrained specificity. |
| Pass 3 - anatomy and movement | Watch. Raised palm and guarding hand follow credible joint chains over a grounded wide base. The lower standing figure takes a clear forearm support while the seated figure braces through a hand and planted foot. Crossed arms remain distinct. |
| Pass 4 - continuity and geometry | Pass. Build, garments, view inventory, border, and action placements remain stable. |
| Pass 5 - material, light, and environment | Watch. Dark wrap, pale trousers, hair, and skin are materially distinct; remaining variation follows folds, overlap, contact, anatomy, and directional light. |
| Pass 6 - artifact and content sweep | Pass. No text, symbols, logos, insignia, watermarks, extra figures, fused limbs, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 STY1 ART0` |
| Status | `Approved working authority`; author approved on `2026-09-01`. This unlocks `PF1-006`; the registered source remains unchanged pending final reconciliation. |

## PF1-006 - Augmented Gor Dedicated Continuity Candidate

### v1-v2 - Superseded Material Iterations

| Field | Record |
|---|---|
| Immutable source | `characters/gor-of-almelah/continuity-sheet.png`, SHA-256 `EBFF2C25481771565F88365C323C805F09BC179D2F93772F79929B403CA4C97C`, `1024x1536` |
| v1 | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v1.png`, SHA-256 `4DD005DFD79F503012B0F5B8341AF9A8EC2FBDF71A0D10CCD031567D1D7DCCE7`, `1024x1536` |
| v2 | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v2.png`, SHA-256 `4D564D29AD00F73E566F382ADD02A0A96CBFFFD1D6E2A18A28C9D2595206A8B2`, `1024x1536` |
| Result | Sheet geometry, armor, identity, raised palm, carried-body support, knife grip, and ready mechanics remained stable, but broad angular texture persisted across dark cloth, pale armor, and skin. |
| Status | `Superseded`; retained as correction evidence only. |

### v3 - Rejected Facial-Material Iteration

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v3.png` |
| SHA-256 | `A579A7D57336BB5BC3A47FDD7819501C2490461E794B7BEED122F04564358B93` |
| Dimensions | `1024x1536` |
| Result | Dark cloth, armor plates, sensor weave, rain behavior, and scar closeup became materially quieter while the corrected action mechanics remained intact. |
| Author finding | Six prominent faces still showed broad marble-like tonal islands, including the upper rotation and all five expression studies. |
| Status | `Focused rework`; rejected as the final authority after author annotation on `2026-09-01`. |

### v4 - Face-Corrected Environmental-Rework Predecessor

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v4.png` |
| SHA-256 | `709CCBCDE03F61AFF78E8ADEF8FD7A71B9A68F0273596E807BABF81F2E47723D` |
| Dimensions | `1024x1536` |
| Authorities | Source controls sheet geometry, armor, rain state, blade, scars, and action inventory. Approved young-Gor v2 controls identity and anatomy. Approved PF1-001 controls craft. The protected Korin study supplies discrete pores, follicles, stubble, fine lines, brows, lashes, and grouped hair only; its exposure and broad etched fields are explicitly excluded. |
| Prompt summary | Preserve v3 outside exposed facial skin and hair boundaries; replace the author-marked marble fields with continuous anatomical shading, sparse individual pores and follicles, natural stubble, fine expression lines, subtle asymmetry, and grouped curls across all visible faces. |
| Pass 1 - fit-to-page | Pass. Four rotations, rain panel, five expression studies, three action studies, four detail panels, hierarchy, border, and silhouettes remain intact. |
| Pass 2 - full-resolution human inspection | Watch. The six marked faces now use continuous facial planes with localized pores, stubble, fine lines, brows, lashes, and grouped hair instead of map-like patches. All remain recognizably the same Gor. |
| Pass 3 - anatomy and movement | Watch. Raised palm, carried-body support, shared center of mass, knife grip, and ready advance remain physically legible and recoverable. |
| Pass 4 - continuity and geometry | Pass. Pale composite geometry remains consistent across rotations; sensor weave, rain state, scars, knife, sheath, panel inventory, and relative scale remain stable. |
| Pass 5 - material, light, and environment | Watch. Armor, weave, cloth, skin, hair, scar tissue, rain, metal, and sheath are distinct. Remaining variation follows construction, anatomy, contact, wear, water, and light. |
| Pass 6 - artifact and content sweep | Pass. No text, letters, numbers, logos, insignia, watermarks, extra views, missing figures, fused digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ART0 STY1` |
| Author finding | The rain-state industrial background still contained wavy, warped generated linework behind and below Gor, centered near `32.9%` width and `62.9%` height. |
| Status | `Superseded`; facial correction retained, but the annotated rain background required focused rework. |

### v5 - Face And Rain-Background Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v5.png` |
| SHA-256 | `DE960B710A5099F3FC92905579FA3D247EA76E8FAEC24CC22BC876CAB73CBE42` |
| Dimensions | `1024x1536` |
| Authorities | v4 controls the corrected faces and all non-rain-panel content. The immutable source controls Gor's rain-state identity and wet industrial intent. Approved PF1-001 controls rectilinear environment edges and restrained grayscale craft. |
| Prompt summary | Preserve v4 pixel-close outside the rain-state background; replace the marked wavy/melted pseudo-structure with straight vertical supports, coherent parallel edges, a level wet floor, near-vertical rain, gravity-led runoff, restrained puddle reflections, and sparse readable distance detail. |
| Pass 1 - fit-to-page | Pass. Full sheet hierarchy, figure scale, border, panel divisions, rotations, expressions, actions, and closeups remain intact. |
| Pass 2 - full-resolution human inspection | Watch. v4's corrected continuous facial planes, discrete pores, stubble, fine lines, brows, lashes, and grouped hair remain stable. |
| Pass 3 - anatomy and movement | Watch. Raised palm, carried-body support, shared center of mass, knife grip, and ready advance remain unchanged and physically legible. |
| Pass 4 - continuity and geometry | Pass. Armor, sensor weave, rain-state figure, scars, blade, sheath, panel inventory, and relative scale remain stable. The rain background now uses straight supports and a coherent ground plane. |
| Pass 5 - material, light, and environment | Watch. Armor, weave, cloth, skin, hair, rain, metal, wet floor, and architecture are distinct. Rain and runoff follow gravity; reflections follow the corrected floor and structure. |
| Pass 6 - artifact and content sweep | Pass. The marked wavy background artifact is removed. No text, letters, numbers, logos, insignia, watermarks, extra views, missing figures, fused digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ENV1 ART0 STY1` |
| Status | `Candidate review`; internally acceptance-compliant and awaiting explicit author approval. `PF1-014` remains gated. |

### v6 - Author-Bias Identity And Hair Iteration

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v6.png` |
| SHA-256 | `2F693621382F31F688BCD3A15BF361AEE6EED6855B7EFED24B69033003E57CC7` |
| Dimensions | `1024x1536` |
| Author bias | `D4 H4 C4 F3 A1 M4`: several corrections; medium-brown tight curls; clearly distinct facial identity; preserve successful anatomy; correct distracting material artifact. |
| Authorities | v5 controls layout, armor, action anatomy, rain geometry, blade, scars, and all object placement. Approved young-Gor v2 controls identity continuity. The protected Korin partial-face study controls human microdetail only; approved Chapter 1 craft controls restrained line-and-paint finish. |
| Prompt summary | Preserve v5's sheet and anatomy while giving Gor consistent medium-brown tight curls, increasing non-glamorous facial specificity, and removing shared surface pattern from armor, weave, cloth, skin, rain, and background. |
| Result | Hair color and curl target succeeded; facial identity became more specific; sheet geometry and action anatomy remained stable. Faceted crackle remained visible on armor and skin, especially in the bottom closeups and several facial studies. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ENV1 ART0 STY1` |
| Status | `Superseded iteration`; retained as evidence. The material gate required one narrower pass. |

### v7 - Author-Bias Material-Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v7.png` |
| SHA-256 | `E3A568E8EE714A3F11F884A173687A95DAF8D01D0909EDC7BF6CD8BDFEC0B6FB` |
| Dimensions | `1024x1536` |
| Authorities | v6 controls the author-selected medium-brown tight curls, facial-identity direction, layout, figures, anatomy, armor geometry, rain panel, knife, sheath, and detail inventory. The Korin study controls human microdetail only; Chapter 1 controls page finish. |
| Prompt summary | Change only the residual material rendering: remove polygon cells, cracked-earth tracery, marble veins, faceted wedges, map-like boundaries, cloudy camouflage patches, embossed squiggles, and broad mottling. Replace them with smooth matte composite, quiet construction-bound weave, causal cloth folds, continuous living skin, and gravity-driven rain. |
| Pass 1 - fit-to-page | Pass. Portrait hierarchy, rotations, rain figure, expressions, actions, detail studies, silhouettes, and relative scale remain readable. |
| Pass 2 - full-resolution human inspection | Watch. One consistent Gor retains medium-brown tight curls, specific facial asymmetry, pores, fine lines, uneven stubble, scars, brows, ears, neck transitions, hands, and nails without broad stone-like segmentation. |
| Pass 3 - anatomy and movement | Watch. v5's raised palm, carried-body support, knife grip, ready advance, joint chains, five-digit hands, balance, and center of mass remain physically legible. |
| Pass 4 - continuity and geometry | Pass. Pale armor geometry, black weave, clothing cut, rain state, scars, blade, sheath, crops, panel divisions, and figure/object inventory remain stable. |
| Pass 5 - material, light, and environment | Watch. Pale armor is smooth hard matte composite; black weave is quiet and directional; dark cloth follows seams and gravity; skin variation is anatomical and localized; rain and wet reflections remain causal. No material carries the v6 cellular crackle at page-reading scale. |
| Pass 6 - artifact and content sweep | Pass. No letters, numbers, labels, logos, insignia, watermarks, extra or missing figures, fused digits, gore, neon, or unintended generated symbols were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 ENV1 ART0 STY1` |
| Status | `Candidate review`; internally acceptance-compliant and awaiting explicit author approval. `PF1-014` remains gated until that approval. |

## PF1-007 - Korin Dedicated Continuity Candidate

| Field | Record |
|---|---|
| Source | `characters/korin-tal/continuity-sheet.png`, SHA-256 `33D86EAE66DCF30C3A0997113A2028F28F20C4BC94D3D00ACC4CC6E19F53ADBB`, `1672x941` |
| Asset | `characters/korin-tal/continuity-sheet-phase1-refinement-v1.png` |
| SHA-256 | `0626673E306EA40F9287B5CF9F50767F7AA388A9388ADA9D0C93BF281256338D` |
| Dimensions | `1672x941` |
| Authorities | Source controls identity, layout, suit, posture, label, observer, and schematic purpose. Approved PF1-001 controls craft. The protected Korin study supplies fine human detail without its crop or dark exposure. |
| Prompt summary | Remove suit/skin patterning; preserve Korin's identity and tailored slate suit; refine visible and behind-back hands; retain the angled schematic's geometry and purpose while replacing all generated microtext with text-free rings, axes, callout lines, node dots, blank bands, and unnumbered ticks. |
| Pass 1 - fit-to-page | Pass. Four rotations, four portraits, observer, schematic, hierarchy, and negative space remain stable. |
| Pass 2 - full-resolution human inspection | Watch. Identity, fine lines, restrained stubble, hair grouping, hands, and nails remain specific without adopting the protected study's dark photographic treatment. |
| Pass 3 - anatomy and movement | Pass. Static rotations remain proportionate; the observer's hands overlap cleanly behind his back. |
| Pass 4 - continuity and geometry | Pass. Suit cut, insert, shoes, label, observer, display perspective, and central ring/axis construction remain intact. |
| Pass 5 - material, light, and environment | Watch. Slate suit, lighter insert, skin, hair, shoes, and pale display are materially distinct and coherently lit. |
| Pass 6 - artifact and content sweep | Pass. The only readable text is `KORIN TAL`. Former microtext is replaced by nonlinguistic horizontal bars, callout geometry, ring axes, nodes, blank bands, and unnumbered ticks. No logos, insignia, watermarks, accidental glyphs, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ART0 STY1` |
| Status | `Approved working authority`; author approved on `2026-09-01`. Eligible for Phase 1 dependent-page propagation; the registered source remains unchanged pending final reconciliation. |

## PF1-008 - Broken-Clinic Leader And Guard Candidate

### v1 - Rejected Hand Iteration

| Field | Record |
|---|---|
| Asset | `characters/broken-clinic-leader-and-guard/continuity-sheet-phase1-refinement-v1.png` |
| SHA-256 | `4D947EE098834B341DA12F7DBE628D64FF8A31B13070A243EF4FF7086E70E49D` |
| Dimensions | `1024x1536` |
| Result | Improved identity separation and material behavior, but the med-kit hands remained oversized, elongated, and weakly attached to the case. |
| Residual scores | `MAT1 FAC1 DET1 HND2 ANA1 CNT2 CST1 STY1` |
| Status | `Focused rework`; not eligible for propagation. |

### v2 - Candidate Review

| Field | Record |
|---|---|
| Source | `characters/broken-clinic-leader-and-guard/continuity-sheet.png`, SHA-256 `0C1B1990FE3058924B7A8EC09472D3B954E6C612A55735048711CE200F5322FB`, `1024x1536` |
| Asset | `characters/broken-clinic-leader-and-guard/continuity-sheet-phase1-refinement-v2.png` |
| SHA-256 | `5312794B2018C04E6302AC78A32F74A46F33785ABF81C57E6ED9AD047C7EF5AA` |
| Dimensions | `1024x1536` |
| Authorities | Source controls leader/guard identity, layout, clothing, med-kit, doorway, lamp, and clinic. v1 controls the improved identity/material direction. The Korin study controls hand microdetail only. |
| Prompt summary | Preserve v1 outside the med-kit hands. Reduce both hands about 15–20 percent, give the upper hand a four-finger/opposing-thumb lid-rim clamp, and give the near hand a thumb-on-rim/fingers-around-corner grip with aligned wrists and explicit metal contact. |
| Pass 1 - fit-to-page | Pass. Leader, guard, panel hierarchy, med-kit, doorway, and shared scene remain legible. |
| Pass 2 - full-resolution human inspection | Watch. The older heavier leader and leaner uncertain guard remain distinct; faces, hair, stubble, hands, and nails retain specificity. |
| Pass 3 - anatomy and movement | Watch. Neutral and doorway poses remain supported. Both med-kit wrists align; the left hand clamps the lid rim and the right wraps the case corner at natural scale. |
| Pass 4 - continuity and geometry | Pass. Clothing, case, hinge, latch, bandage, packet, syringe, table, doorway, pipes, lamp, and clinic geometry remain stable. |
| Pass 5 - material, light, and environment | Watch. Work fabrics, skin, hair, rusted metal, medical contents, walls, pipes, and lamp glass remain distinct; wear is localized and causal. |
| Pass 6 - artifact and content sweep | Pass. No text, logos, insignia, watermarks, fused digits, missing contents, extra people, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 CNT1 CST1 STY1 ART0` |
| Status | `Approved working authority`; author approved on `2026-09-01`. Eligible for Phase 1 dependent-page propagation; the registered source remains unchanged pending final reconciliation. |

## PF1-009 - Below-the-Map Escort Group Candidate

| Field | Record |
|---|---|
| Source | `characters/below-the-map-escort/continuity-sheet.png`, SHA-256 `547703ECBAACFEECECA79C67BBF4DF2810926D93614CE37D850E12C799F19F5D`, `1024x1536` |
| Asset | `characters/below-the-map-escort/continuity-sheet-phase1-refinement-v1.png` |
| SHA-256 | `B78DB564CD7AA4AAA4A2B339A176E6FBBB37A89D618100682F774172937718BA` |
| Dimensions | `1024x1536` |
| Authorities | Source controls group identities, layout, masks, clothing, equipment, gestures, formation, and ruined setting. Approved PF1-001 controls craft. The Korin study controls fine human detail only. |
| Prompt summary | Preserve the older leader, masked watcher, route-cloth carrier, runner, wrench bearer, and rod bearer as distinct recurring roles; separate skin, masks, damp cloth, leather, metal, tools, and wet ground; clarify the leader's stop palm and every rifle, cloth, wrench, rod, and formation contact. |
| Pass 1 - fit-to-page | Pass. Role hierarchy, view inventory, silhouettes, equipment, and bottom formation remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Faces/masks, hair, stop palm, small hands, glove construction, and route-cloth fingers remain role-specific. |
| Pass 3 - anatomy and movement | Watch. Stop arm and palm align; rifles retain two-point grips and continuous barrels; cloth and tool contacts are explicit; bottom figures contact the wet ground. |
| Pass 4 - continuity and geometry | Pass. Role identities, relative heights, masks, goggles, satchels, pouches, scarves, rifles, wrench, rods, route cloth, and formation order remain stable. |
| Pass 5 - material, light, and environment | Watch. Dampness, mud, abrasion, fraying, rust, and oil remain causal; skin, woven masks, cloth, leather, goggles, weapon/tool materials, boots, and wet ground are distinguishable. |
| Pass 6 - artifact and content sweep | Pass. No text, symbols, logos, insignia, watermarks, fused digits, bent barrels, duplicated roles, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 STY1 ART0` |
| Status | `Approved working authority`; author approved on `2026-09-01`. Eligible for Phase 1 dependent-page propagation; the registered source remains unchanged pending final reconciliation. |

## PF1-010 - Almelah Dojo Master Refinement v3

### v3 Pass 1 - Rejected Material Iteration

| Field | Record |
|---|---|
| Retained material pilot v1 | `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot.png`, `1024x1536`, SHA-256 `D3F71AAFEF17DEAD3D031E62FC88AB536F5AB7846506CD8771B93BEEB2B0065D` |
| Retained material pilot v2 | `characters/almelah-dojo-master/continuity-sheet-material-refinement-pilot-v2.png`, `1024x1536`, SHA-256 `1FEE6AAB02394C55282ABA43DEC73481AF2D5B55F5375698EF8EA6B0A7A5E657` |
| Asset | `characters/almelah-dojo-master/continuity-sheet-material-refinement-v3-pass1.png` |
| SHA-256 | `8F0ED3F7800D87DF9391AE88923AFE108E210EE15C898EE420D80746FE124E50` |
| Dimensions | `1024x1536` |
| Result | Restored age, identity, hair, skin, hand, and foot specificity, but retained broad angular tonal islands across the pale trousers. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA1 STY1` |
| Status | `Focused rework`; retained as synthesis evidence only. |

### Final v3 - Candidate Review

| Field | Record |
|---|---|
| Sources | `characters/almelah-dojo-master/continuity-sheet.png` (`A11`) controls identity/geometry; `continuity-sheet-material-refinement-pilot-v2.png` (`A13`) supplies the cleaner material direction; the Korin partial-face study (`A16`) supplies human-detail behavior; approved PF1-001 controls craft. |
| Asset | `characters/almelah-dojo-master/continuity-sheet-material-refinement-v3.png` |
| SHA-256 | `0B4332BA9E9217D3D8CAAB611B9EFF96C1DC2698A5EFB9BD4CFF129D8EB2AC6C` |
| Dimensions | `1024x1536` |
| Prompt summary | Preserve pass1's restored identity and anatomy pixel-close; remove all remaining faceted/polygonal pattern from pale trousers, dark wrap, and skin; retain only garment construction, true folds, contact, anatomy, age, and light. |
| Pass 1 - fit-to-page | Pass. Four rotations, four portraits, three lower poses, hierarchy, scale, border, and silhouettes remain intact. |
| Pass 2 - full-resolution human inspection | Watch. Older lean identity, pores, fine lines, gray hair grouping, restrained stubble, hand tendons, nails, toe joints, and natural asymmetry remain visible without photographic drift. |
| Pass 3 - anatomy and movement | Watch. Neutral rotations, cross-legged seat, upright teaching palm, guarding hand, walking pose, wrists, ankles, hands, and bare feet remain credible and supported. |
| Pass 4 - continuity and geometry | Pass. Identity, wrap construction, cuffs, undershirt, trousers, view inventory, and pose placements remain stable. |
| Pass 5 - material, light, and environment | Watch. Pale trousers now read as quiet woven cloth; dark wrap, skin, gray hair, and bare feet remain distinct with only causal folds, anatomy, contact, and light. |
| Pass 6 - artifact and content sweep | Pass. No text, symbols, logos, insignia, watermarks, extra views, fused digits, cartoon flattening, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 STY1 ART0` |
| Status | `Approved working authority`; author approved on `2026-09-01`. The registered source and prior pilots remain unchanged pending final reconciliation. |

## PF1-011 - Chapter 1 Page 01 Candidate

### v1-v3 - Retained Focused Iterations

| Field | Record |
|---|---|
| Immutable source | `chapter_01_wakeup/page-01.png`, SHA-256 `262D68A9573013A87DF586F42331A4255A8ED7EAF31EFBEDD8F2CB031304BB4B`, `1024x1536` |
| v1 | `chapter_01_wakeup/page-01-phase1-refinement-v1.png`, SHA-256 `6323848EE20DF6621C3D285858E3C492D1CF71C68BDEC31CD12B26938EC7FB08` |
| v2 | `chapter_01_wakeup/page-01-phase1-refinement-v2.png`, SHA-256 `D7E5D1FF711A995DA2877AC6B0B55020A9B23B29AC1282B188B36556CAC08248` |
| v3 | `chapter_01_wakeup/page-01-phase1-refinement-v3.png`, SHA-256 `A5611356B3EE3346C05C180E6D2C4FA5E7629284E82379FCAE53D944D665A263` |
| Result | v1 corrected the final reach, hand scale, five-digit structure, and knife contact while preserving all lettering. v2-v3 reduced cloth and skin pattern density, but connected closeup skin marks remained too visible for promotion. |
| Status | `Iteration evidence`; preserved and superseded by v4. |

### v4 - Candidate Review

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-01-phase1-refinement-v4.png` |
| SHA-256 | `044E950A3EA2B5B26632A7348847370AF6CC21E1B1AEA2C6B081FD4C839FBE56` |
| Dimensions | `1024x1536` |
| Authorities | Source controls panel geometry, equipment, room, story order, captions, and timing. Approved PF1-001 controls Chapter 1 craft. Approved PF1-002 controls Cassian identity, anatomy, scrubs, hands, and restrained movement. |
| Prompt summary | Preserve all non-skin content and lettering pixel-close; keep the corrected final reach/contact; reduce closeup skin pattern to quiet anatomical values with only tiny isolated pores, individual stubble, fine eyelid/knuckle lines, subtle veins, tendons, and natural nail beds. |
| Pass 1 - fit-to-page | Pass. Five panels, captions, hierarchy, crops, timing, room, attendants, tray, tool, knife, and bed remain intact. |
| Pass 2 - full-resolution human inspection | Watch. Cassian remains one identity across ear, eye, and final action views. Fine connected skin marks remain visible on close inspection but no longer dominate the page-fit read. |
| Pass 3 - anatomy and movement | Watch. Final reach uses modest elbow flex, shoulder loading, a continuous arm/wrist chain, proportionate five-digit hand, and explicit index/middle fingertip contact with the knife handle/tang. |
| Pass 4 - continuity and geometry | Pass. Panel count, room geometry, attendants, visor, interface tool, knife, tray, bed, crops, and lighting sequence remain stable. |
| Pass 5 - material, light, and environment | Watch. Scrubs, trousers, uniforms, gloves, bedding, skin, metal, hair, and visors are distinguishable. Residual closeup skin texture is recorded as a later polish item rather than a Phase 1 blocker. |
| Pass 6 - artifact and content sweep | Pass. All seven approved captions remain verbatim and in place. No new text, symbols, logos, insignia, watermarks, extra figures, fused digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Candidate review`; acceptance-compliant at the Phase 1 severity threshold and awaiting author review. The registered source remains unchanged. |

### v5 - Author-Bias Expression And Material Iteration

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-01-phase1-refinement-v5.png` |
| SHA-256 | `53C7817170A34D3009D95FF7837D1D3D966BCEBDAE4DD9E6498E5CC9AF7952A0` |
| Dimensions | `1024x1536` |
| Author bias | `D3 E2 R1 K1 S4 T1`: one focused correction; restrained final-panel tension mainly in Cassian's eyes; preserve reach, first knife contact, and exact text; correct distracting shared surface artifact. |
| Authorities | v4 controls all page content, anatomy, geometry, action, captions, and timing. Approved Cassian v2 controls identity. The protected Korin study controls human microdetail only. |
| Prompt summary | Preserve v4 while carrying the preceding shocked-eye tension into Cassian's final gaze and removing cellular/marble texture from skin, scrubs, uniforms, gloves, bedding, metal, and room surfaces. |
| Result | All seven captions, the reach, and the knife contact remained intact; the final gaze gained restrained tension. Cellular texture remained visible on Cassian's skin and dark scrubs. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Superseded iteration`; retained as evidence. A material-only pass was required. |

### v6 - Author-Bias Material-Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-01-phase1-refinement-v6.png` |
| SHA-256 | `917729B007473E1DF2F1F923D7C3DBDF6D1A39CA37EC73A9911DA1302B27C951` |
| Dimensions | `1024x1536` |
| Authorities | v5 controls the score-E2 final expression, exact lettering, action, room, and page geometry. Augmented-Gor v7 supplies clean material behavior only; the Korin study supplies human microdetail only. |
| Prompt summary | Remove residual interconnected cells, marble veins, map-like tracery, engraved loops, cloudy camouflage, and repeated tonal islands without changing any page content. |
| Pass 1 - fit-to-page | Pass. Five-panel hierarchy, blur, ear contact, eye reaction, final reach, tray/bed relationship, and all captions remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian remains one identity with localized pores, stubble, fine lines, hair roots, eyes, ear, hand tendons, nails, and restrained final tension. |
| Pass 3 - anatomy and movement | Watch. Shoulder-to-fingertip reach, elbow flex, wrist, five-digit hand, bed support, body weight, and first knife contact remain physically legible. |
| Pass 4 - continuity and geometry | Pass. Room, attendants, visors, interface tool, tray, knife, bed, crops, light sequence, and object positions remain stable. |
| Pass 5 - material, light, and environment | Watch. Skin, scrubs, white uniforms, gloves, bedding, stainless metal, visors, walls and equipment now use distinct physically caused texture without a dominant shared cellular field. |
| Pass 6 - artifact and content sweep | Pass. All seven captions remain verbatim and in place. No generated microtext, logos, insignia, watermark, extra limbs/digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Candidate review`; internally acceptance-compliant and awaiting explicit author approval. The registered source remains unchanged. |

## PF1-012 - Chapter 1 Page 02 Candidate

| Field | Record |
|---|---|
| Source | `chapter_01_wakeup/page-02.png`, SHA-256 `DCE5D20749102A0834DE731A5721D1E2B1BEB94D2D18114999E6CC7B14A30ED9`, `1024x1536` |
| Asset | `chapter_01_wakeup/page-02-phase1-refinement-v1.png` |
| SHA-256 | `833889DBA56A16100AE255F442CEEB05F137A549C97DA4BE97D5AC54977B87BA` |
| Dimensions | `1024x1536` |
| Authorities | Source controls the four-panel page, captions, alien-language balloon, room, attendants, tools, pulse effect, story order, and timing. Approved PF1-001 controls Chapter 1 craft. Approved PF1-002 controls Cassian identity, anatomy, scrubs, hands, stance, and defensive intent. |
| Prompt summary | Preserve all lettering and alien glyphs; correct the two-person restraint's shoulders, elbows, wrists, contacts, stance, and reaction force; correct the knife grip and non-penetrating collar/neck contact; reduce the POV hand to natural scale with a five-digit interface-tool grip; reduce broad cross-material patterning without chasing minor surface variance. |
| Pass 1 - fit-to-page | Pass. Four panels, captions, alien balloon, room, attendants, tray, bed, door, control panel, pulse effect, and repeated tableau remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian and both attendants remain consistent; faces, hair, skin, gloved hands, visor edges, and tool/knife contacts are legible. Residual fine skin and uniform texture is deferred. |
| Pass 3 - anatomy and movement | Watch. Cassian's restraint and knife arms form continuous shoulder-to-hand chains; the female attendant receives force against the wall and contacts his forearm; the male attendant reacts through neck, shoulder, raised hand, and stance. The POV hand has natural scale and one explicit five-digit grip. |
| Pass 4 - continuity and geometry | Pass. Panel geometry, repeated tableau, character identities, visors, room, bed, door, tray, tools, pulse position, and camera sequence remain stable. |
| Pass 5 - material, light, and environment | Watch. Skin, scrubs, pale uniforms, gloves, transparent visors, metal, bedding, wall panels, and pulse light remain distinguishable. Residual cross-material texture does not dominate the page-fit read. |
| Pass 6 - artifact and content sweep | Pass. All approved English captions remain verbatim and in place; the alien-language balloon and glyph sequence remain visually intact. No new text, logos, insignia, watermarks, extra figures, fused digits, penetration, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Candidate review`; acceptance-compliant at the Phase 1 severity threshold and awaiting author review. The registered source remains unchanged. |

### v2-v3 - Author-Bias Rebuild Iterations

| Field | Record |
|---|---|
| Author bias | `D5 O5 A5 K5 T1 S2`: rebuild the restraint choreography and knife interaction; preserve text; retain only minor surface correction. |
| v2 | `chapter_01_wakeup/page-02-phase1-refinement-v2.png`, SHA-256 `790EB651386A262D6A5D73E8446665AD543E096B0EFD4FC758C7A90EFA3AFB95`, `1024x1536`. Corrected the pulse source to the standing attendant's wrist, but retained the choke-loop, a probe-like panel-3 object, and lost final collar contact. |
| v3 | `chapter_01_wakeup/page-02-phase1-refinement-v3.png`, SHA-256 `C4E73BA0E00BA51647AEFD82AF6127AA3C6BA3D80E89AA8DB331708C82969719`, `1024x1536`. Restored a broad food knife and clearer hand ownership, but reversed the left-arm pin so the fist rather than elbow supplied contact; final knife contact remained open. |
| Status | `Rejected iteration evidence`; both preserve all approved captions and the alien-language balloon but fail the action gate. |

### v4 - Strongest Author-Bias Rebuild, Unresolved

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-02-phase1-refinement-v4.png` |
| SHA-256 | `E0CF76E10DC52932D0746BAB52A07D4917A251A94408633E114BAB5F5384F0D1` |
| Dimensions | `1024x1536` |
| Authorities | v1 controls page layout, exact English captions, alien-language balloon, room, figures, and timing. Page-01 v6 controls the broad food knife. Approved Cassian v2 controls identity and anatomy. The manuscript controls the elbow pin, knife restraint, and wrist-interface pulse. |
| Prompt summary | Rebuild the repeated restraint so Cassian's left back-elbow pins the nearest attendant, his fist returns toward his sternum, his right hand holds the broad food knife, panel 3 shows that same knife rather than a probe, and the last panel carries a wrist-origin harmonic pulse. |
| Pass 1 - fit-to-page | Watch. Four panels, room, captions, alien balloon, two-attendant restraint, first-person knife beat, and wrist pulse read in the intended order. |
| Pass 2 - full-resolution human inspection | Watch. Identities, faces, visors, hands, knife grip, and alert reactions remain readable; residual shared texture is secondary to the action failure. |
| Pass 3 - anatomy and movement | Focused rework. Panels 1 and 4 show a materially clearer left back-elbow/fist relationship and all hands have owners. Panel 2 still substitutes Cassian's fist as the pinned-attendant contact. Panel 4 leaves a visible gap between the knife and collar. |
| Pass 4 - continuity and geometry | Watch. Room, bed, tray, door, figures, screen direction, broad knife, wrist interface and pulse source remain stable. Panel-2 restraint contact and panel-4 knife contact do not match the wide action precisely. |
| Pass 5 - material, light, and environment | Watch. Materials remain distinguishable; connected pattern remains a later concern after action is solved. |
| Pass 6 - artifact and content sweep | Pass. Approved captions and alien-language balloon remain intact. No new text, logos, insignia, watermark, extra figure, penetration, gore, or unintended color was observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN2 CNT2 CST1 PNL2 ART0 STY1` |
| Status | `Unresolved`; strongest retained rebuild but not acceptance-compliant and not ready for author approval. |

### v5-v6 - Rejected Localization Attempts

| Field | Record |
|---|---|
| v5 | `chapter_01_wakeup/page-02-phase1-refinement-v5.png`, SHA-256 `6F04D7AC1FD377D27EFF7251FA2098477DC4884CF81C515E3FB234F695B790F5`, `1024x1536`. Regressed the wide left-arm poses to a forearm wrap while preserving the broad knife and wrist pulse. |
| v6 | `chapter_01_wakeup/page-02-phase1-refinement-v6.png`, SHA-256 `C2D854505DC9FC1F4505AB32B50A066E5CDE5597EFB3CB26D5844932B013CD28`, `1024x1536`. Removed the visible panel-2 fist but produced another forearm bar and did not close the panel-4 knife/collar gap. |
| Status | `Rejected iteration evidence`; v4 remains the strongest current Page 02 rebuild. |

### v7-v8 - Clean Full Rebuild And Knife-Only Iteration

| Field | Record |
|---|---|
| v7 | `chapter_01_wakeup/page-02-phase1-refinement-v7.png`, SHA-256 `D06A9E33788C01509C8429D217EC7212B08AE03AF732BF1CE1003F05CF91D0D5`, `1024x1536`. New four-panel construction from the approved Page 01, combined Chapter 1, and Cassian authorities rather than the inherited faulty pose. Panel 2 isolates the pinned attendant and Cassian's elbow contact, eliminating crossed arm chains; panel 3 shows the broad food knife; panel 4 uses the attendant's wrist-interface pulse. English captions are exact, materials are quiet, and wide-view blades read edge-on. The alien glyph sequence was newly generated rather than preserved. |
| v8 | `chapter_01_wakeup/page-02-phase1-refinement-v8.png`, SHA-256 `83599C3488C1F0E52B69FAF4747AE71C0B6959DB0E652D5122A69F9638EDD2F4`, `1024x1536`. Knife-only attempt left the wide edge-on views materially unchanged; the action remained stable. |
| Status | `Iteration evidence`; v7 supplies the accepted rebuild geometry, but the alien-language balloon required restoration. |

### v9 - Author-Bias Full-Rebuild Candidate Review

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-02-phase1-refinement-v9.png` |
| SHA-256 | `61F28E4BF38D83071D2EEE67F1191DFBFEC66103A983033C9899955F08E34735` |
| Dimensions | `1024x1536` |
| Authorities | v7 controls the clean four-panel rebuild, identities, room, action, materials, English captions and wrist pulse. v1 controls the approved alien-language balloon and glyph sequence. Page-01 v6 and approved Cassian v2 remain identity, knife and craft authorities. |
| Prompt summary | Restore only v1's approved alien-language balloon and glyph sequence into v7 while locking the clean rebuild, elbow pin, broad/edge-on food-knife views, wrist-interface action, room and all English captions. |
| Pass 1 - fit-to-page | Pass. Four panels read as simultaneous restraint, pinned-attendant speech, first-person knife weight and wrist-interface translation. |
| Pass 2 - full-resolution human inspection | Watch. Cassian and both attendants remain consistent; faces, visors, skin, hair, gloves, hands and expressions remain observed and restrained. |
| Pass 3 - anatomy and movement | Watch. Cassian's left elbow contact has no orphan fist or crossed competing chain; his planted stance and right arm are traceable. The same broad food knife is face-on in panel 3 and plausibly edge-on at the collar in wide panels. Exactly two arms/hands belong to each wide-view figure. |
| Pass 4 - continuity and geometry | Pass. Room, bed, tray, door, equipment, figures, screen direction, restraint, knife, wrist interface and wrist-origin pulse are continuous. The simplified panel-2 crop intentionally isolates one contact rather than repeating two overlapping restraints. |
| Pass 5 - material, light, and environment | Watch. Skin, dark scrubs, pale uniforms, gloves, visors, bedding, knife, tray and room panels are distinct and materially quiet without a dominant shared cellular field. |
| Pass 6 - artifact and content sweep | Pass. All five English caption groups remain exact and in place; the approved alien-language balloon/glyph sequence is restored. No generated microtext elsewhere, logos, insignia, watermark, orphan hands, extra/fused digits, penetration, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Candidate review`; internally acceptance-compliant and awaiting explicit author approval. The registered source remains unchanged. |

## PF1-013 - Chapter 1 Page 03 Candidate

### v1 - Annotated Sequence Candidate

| Field | Record |
|---|---|
| Source | `chapter_01_wakeup/page-03.png`, SHA-256 `471173EB59C9B39AA8EDE03095494DE33F7EB8859DEA3CD1C884E78ADBA3FBC8`, `1024x1536` |
| Asset | `chapter_01_wakeup/page-03-phase1-refinement-v1.png` |
| SHA-256 | `3E04BCD92AFD719FB2F9E1CBA646A8B78E2DC4C57B1165AABAE29419992D02B8` |
| Dimensions | `1024x1536` |
| Authorities | Source controls the five-panel page, every caption and speech balloon, room, attendants, visors, knife/tool, pulse rings, warm-light transition, story order, emotional restraint, and dropped-knife ending. Approved PF1-001 controls Chapter 1 craft. Approved PF1-002 controls Cassian identity, anatomy, scrubs, hands, release, and kneeling mechanics. |
| Prompt summary | Preserve all lettering and story geometry; correct knife grip/contact, repeated restraint continuity, release path and weight shift, open hand, floor-support palm, kneeling hands/knees, and dropped-knife separation; reduce broad cross-material patterning without chasing minor surface variance. |
| Pass 1 - fit-to-page | Pass. Five panels, captions/balloons, pulse and warm-light progression, room, attendants, knife/tool, tray, bed, and dropped-knife ending remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian and both attendants remain consistent; faces, hair, stubble, skin, hands, gloves, visor edges, and expressions remain specific. Residual fine surface texture is deferred. |
| Pass 3 - anatomy and movement | Watch. Knife hand and collar contact align; the repeated tableau remains continuous; the release reads as withdrawal with lowering knife arm and weight shift; the open hand is proportionate; the final support palm, knees, attendant hands/knees, and dropped knife are distinct and grounded. |
| Pass 4 - continuity and geometry | Pass. Panel sequence, room, attendants, visors, tools, pulse rings, warm transition, crops, body positions, and dropped knife remain stable. |
| Pass 5 - material, light, and environment | Watch. Skin, scrubs, uniforms, gloves, visors, bedding, metal, walls, floor, pulse and warm practical light remain distinguishable. Residual cross-material texture does not dominate the page-fit read. |
| Pass 6 - artifact and content sweep | Pass. Every approved caption and speech balloon remains verbatim and in place. No new text, logos, insignia, watermarks, extra figures, fused limbs, penetration, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Author finding | The restraint-arm overlap around `26.4%` width / `37.3%` height was not mechanically traceable, and the hand around `78.1%` width / `27.4%` height read as an orphan with no clear owner. |
| Status | `Superseded`; release and kneeling mechanics retained, but the two marked ownership failures required focused correction. |

### v2-v4 - Retained Limb-Ownership Iterations

| Field | Record |
|---|---|
| v2 | `chapter_01_wakeup/page-03-phase1-refinement-v2.png`, SHA-256 `61A8A781EE509C8A766AE57B88057DEF463C3D4F18DA4F97ACEC7437981F98E3` |
| v3 | `chapter_01_wakeup/page-03-phase1-refinement-v3.png`, SHA-256 `FE44DF4870FB733E1AF7AE195C5A173608B3127982860BB29D1FB2D411D018D2` |
| v4 | `chapter_01_wakeup/page-03-phase1-refinement-v4.png`, SHA-256 `E9D5391E32F44193F2530FE38C8BD05FA4F5AC9376C8A4A2AE909E0DB3405A66` |
| Result | v2 clarified the panel-3 Cassian/attendant arm chains but left panel 2's hand orphaned. v3 still could not prove that hand's origin. v4 removed the ambiguous limb from panel 2 but also removed the required knife arm from panel 1. |
| Status | `Iteration evidence`; retained and superseded by v5. |

### v5 - Limb-Ownership Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-03-phase1-refinement-v5.png` |
| SHA-256 | `03751BC0B75A64A83DF6BEF2360BEFF8C52DCDF3778A32D2587458D57C9F8D41` |
| Dimensions | `1024x1536` |
| Authorities | v4 controls the clean panel-2 reaction closeup and all lower panels. v2 and PF1-012 control panel-1 knife-arm ownership and direction. Approved PF1-001 and PF1-002 remain the Chapter 1 craft and Cassian authorities. |
| Prompt summary | Restore only panel 1's connected Cassian right arm, aligned wrist, five-digit knife grip, and controlled collar contact while preserving panel 2 as a reaction closeup with no arm, hand, knife, tool, or disconnected body part. Retain panel 3's clarified restraint-arm ownership and all v1 release/kneeling improvements. |
| Pass 1 - fit-to-page | Pass. Five panels, captions/balloons, story order, pulse/warm transition, action, release, kneeling sequence, and dropped knife remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian and attendants remain consistent; faces, eyes, hair, stubble, skin, gloves, visor edges, hands, and expressions remain specific. Residual fine surface texture is deferred. |
| Pass 3 - anatomy and movement | Watch. Panel 1's knife arm visibly belongs to Cassian and ends in controlled contact. Panel 2 contains no orphan limb. Panel 3's Cassian restraint arm and the attendant's exactly two gloved arms are traceable through shoulders, elbows, cuffs, wrists, and hands. Release, floor palm, knees, attendant support, and dropped-knife separation remain intact. |
| Pass 4 - continuity and geometry | Pass. Panel sequence, room, attendants, visors, tools, pulse rings, warm transition, crops, body positions, and dropped knife remain stable. Panel 2's reaction-only crop is an intentional continuity clarification. |
| Pass 5 - material, light, and environment | Watch. Skin, scrubs, uniforms, gloves, visors, bedding, metal, walls, floor, pulse and warm practical light remain distinguishable. Residual cross-material texture does not dominate the page-fit read. |
| Pass 6 - artifact and content sweep | Pass. Every approved caption and speech balloon remains verbatim and in place. No orphan limb, new text, logos, insignia, watermarks, extra figures, fused limbs, penetration, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Candidate review`; acceptance-compliant at the Phase 1 severity threshold and awaiting author review. The registered source remains unchanged. |

### v6 - Author-Bias Narrative And Dialogue Rebuild

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-03-phase1-refinement-v6.png` |
| SHA-256 | `A5CB276CB49B72B5BD82986752370279A8F1D3E8A12866D548F6E5000A18EC75` |
| Dimensions | `1024x1536` |
| Author bias | `D5 O5 R1 E2 K1 T5 S5`: rebuild ownership and lettering; preserve release/kneeling and dropped-knife mechanics; keep emotion controlled; remove dominant surface artifacts. Author note: the existing dialogue did not make sense. |
| Source reconciliation | The redundant panel-4 question `Where am I?` followed the already explicit statement `You're on Earth. Hive Spindle 9. You've returned.` The adaptation candidate removes that one redundant balloon without inventing new dialogue. The manuscript remains unchanged. |
| Prompt summary | Preserve the five-panel story while clarifying the panel-1 knife hand, keeping panel 2 reaction-only, making panel-3 ownership readable, removing the redundant panel-4 balloon, and preserving the release, collapse, support and dropped knife. |
| Result | Narrative and dialogue order became coherent; `Where am I?` is absent; the reaction-to-release transition remains restrained. Dominant cellular texture still covered skin, scrubs and pale uniforms. |
| Residual scores | `MAT2 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART0 STY1` |
| Status | `Superseded iteration`; narrative rebuild retained, material gate required a narrower pass. |

### v7 - Author-Bias Material-Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `chapter_01_wakeup/page-03-phase1-refinement-v7.png` |
| SHA-256 | `D53DAE6BF2109477A8056890E08D5E5487E5654199E1B4E42F4509C427162C7D` |
| Dimensions | `1024x1536` |
| Authorities | v6 controls narrative, dialogue correction, page geometry, figures, action and warm transition. Augmented-Gor v7 supplies clean material behavior only; the protected Korin study supplies human microdetail only. |
| Prompt summary | Remove cellular boundaries, marble veins, stone facets, reptile-scale patches, etched loops, camouflage fields and repeated tonal islands while preserving every figure, action, panel and text decision. |
| Pass 1 - fit-to-page | Pass. Five-panel progression from translated statement through reaction, explanation, release and collapse remains coherent and readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian and both attendants remain consistent; skin, hair, stubble, eyes, brows, hands, nails, visors and gloves are observed rather than stone-carved. Emotion remains tense and controlled. |
| Pass 3 - anatomy and movement | Watch. Panel-1 knife hand belongs to Cassian; panel 2 contains no orphan limb; panel-3 hands have visible owners; release, lowered knife, open hand, floor palm, both knees, attendant support and dropped knife remain grounded. |
| Pass 4 - continuity and geometry | Pass. Room, bed, tray, door, monitors, attendants, visors, crops, action order and cool-to-muted-amber transition remain stable. |
| Pass 5 - material, light, and environment | Watch. Skin, dark scrubs, pale uniforms, gloves, visors, bedding, knife, tray, walls, door and floor are materially distinct and substantially free of the prior shared cellular field. |
| Pass 6 - artifact and content sweep | Watch. The redundant `Where am I?` balloon remains absent; no new dialogue or generated microtext appears. The panel-3 translated explanation uses three periods instead of the requested single ellipsis character, recorded as a lettering watch item. No logos, insignia, watermark, extra figure, fused limb, gore or unintended color was observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 CST1 PNL1 ART1 STY1` |
| Status | `Candidate review`; internally acceptance-compliant at the Phase 1 severity threshold and awaiting explicit author approval. The manuscript and registered source remain unchanged. |

## PF1-014 - Chapter 13 Contextual Candidate - Gated

### Pre-Gate Source Lineage

| Field | Record |
|---|---|
| Earlier material-refinement test | `experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-test.png`, SHA-256 `8626E28EA7470E4A47D355F974432AF44799EAB9A5E03EA1D28DE7F5C9B817F5`, `1024x1536` |
| Immutable Phase 1 source (`A17`) | `experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-perspective-v2.png`, SHA-256 `6B2EAF4107ED86E4AD76AA57A2A063CFA7F4613AF6E3F05682C5547E4AB46CB8`, `1024x1536` |
| Source role | A17 preserves the corrected first-panel Thena scale, doorway depth, rain, lightning, breach geometry, panel layout, and contextual contrast. It remains the immutable input for the later correction. |
| Provisional source scores | `MAT2 FAC3 DET2 HND2 ANA3 KIN3 CNT3 PER2 CST3 PNL2 STY2` |
| Remaining failures | Second-row Cassian face remains chunky and etched; raised palm, grapple, impact contact, and final airborne pose require hand/anatomy/movement correction; Cassian's short sleeves and Gor's bulky pre-v7 armor/hair treatment remain continuity drift. |
| Required authorities | Approved `PF1-001` craft, approved `PF1-002` Cassian, approved `PF1-004` Thena, and explicit author approval of augmented-Gor `PF1-006` v7. |
| Status | `Gated`; no correction candidate has been generated. Both source files are preserved, hash-recorded, dimension-verified, and prospectively routed through Git LFS. |

## PF1-015 - Chapter 14 Contextual Candidate

### v1 - Annotated Treatment-Anatomy Candidate

| Field | Record |
|---|---|
| Source | `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-material-refinement-test.png`, SHA-256 `6228C00772174071036D910AADEFD486C70231B118BD0BCCC720E7D26714C97D`, `1024x1536` |
| Asset | `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-phase1-refinement-v1.png` |
| SHA-256 | `DE7EA112FCD158C7B947CFC1A276463F75D1F9CA853E8B076D3765CDB3F9EC3E` |
| Dimensions | `1024x1536` |
| Authorities | Source controls the six-panel page, corridor/clinic geography, population, beds, med-kit, practical lamps, low exposure, and narrative sequence. Approved PF1-002, PF1-004, and PF1-008 control Cassian, Thena, and the clinic leader. |
| Prompt summary | Preserve the page and low practical lighting; reduce the leader's hands to natural scale; separate support and treatment functions across two five-digit hands; align wrists/forearms; make explicit bandage contact continuous across the bottom panels; separate meaningful clinic grime from cross-material mottling. |
| Pass 1 - fit-to-page | Pass. Six-panel hierarchy, corridor depth, clinic population, beds, characters, practical lights, and treatment sequence remain readable. |
| Pass 2 - full-resolution human inspection | Watch. Cassian, Thena, and the leader remain consistent with their approved working authorities; faces, hair, bandage, hands, and nails remain specific in the low light. |
| Pass 3 - anatomy and movement | Watch. One leader hand supports Thena's wrist from below while the other manipulates the bandage; hand scale, digits, wrists, elbows, shoulders, and torso lean now form a continuous treatment chain across both bottom panels. |
| Pass 4 - continuity and geometry | Pass. Corridor, clinic, population, beds, med-kit, table, lamps, pipes, patched surfaces, panel order, relative scale, and character blocking remain stable. |
| Pass 5 - material, light, and environment | Watch. Skin, worn cloth, Thena's patched gear, bandage, leather, metal, glass, walls, bedding, pipes, and wet surfaces are distinct. Localized grime and wear remain causal. |
| Pass 6 - artifact and content sweep | Pass. No text, letters, numbers, logos, insignia, watermarks, new characters, missing patients, fused digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 PER1 CST1 ENV1 ART0 STY1` |
| Author finding | Thena's metal around `9.1%` width / `66.9%` height and the clinic leader's shoulder material around `82%` width / `66.1%` height retained the shared cloudy/faceted artifact. |
| Status | `Superseded`; treatment anatomy retained, but the two marked material regions required focused correction. |

### v2 - Material-Corrected Candidate Review

| Field | Record |
|---|---|
| Asset | `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-phase1-refinement-v2.png` |
| SHA-256 | `D9519EED1709336488C5FEC4241CD7340898A9F3745869C38766FAEC6C9034E4` |
| Dimensions | `1024x1536` |
| Authorities | v1 controls corrected treatment anatomy and all non-material content. Approved PF1-004 controls Thena's metal, straps, leather, cloth, dampness, and wear. Approved PF1-008 controls the leader's work coat and material behavior. |
| Prompt summary | Preserve v1 pixel-close outside the marked surfaces; render Thena's plate as stable hard worn metal with crisp edges, fasteners, directional scratches, restrained chips, and lamp-caused highlights; render the leader's shoulder as quiet heavy cloth with seams, causal folds, abrasion, and localized stains. Apply those behaviors consistently to the same recurring garments. |
| Pass 1 - fit-to-page | Pass. Six-panel hierarchy, characters, clinic geography, population, practical lights, treatment sequence, and low exposure remain intact. |
| Pass 2 - full-resolution human inspection | Watch. Faces, hair, skin, hands, nails, bandage, and role identities remain stable. |
| Pass 3 - anatomy and movement | Watch. v1's natural-scale treatment hands, below-wrist support, bandage manipulation, aligned wrists, elbows, shoulders, and continuous action remain unchanged. |
| Pass 4 - continuity and geometry | Pass. Panel boundaries, crops, corridor, clinic, patients, beds, med-kit, table, lamps, pipes, and character blocking remain stable. |
| Pass 5 - material, light, and environment | Watch. The marked plate now reads as hard metal and the marked shoulder as heavy cloth; matching garments remain consistent elsewhere. Clinic grime, dampness, abrasion, rust, and repairs remain localized and causal. |
| Pass 6 - artifact and content sweep | Pass. The two author-marked shared-material artifacts are removed. No text, letters, numbers, logos, insignia, watermarks, new characters, missing patients, fused digits, gore, or unintended color were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 PER1 CST1 ENV1 ART0 STY1` |
| Status | `Candidate review`; acceptance-compliant at the Phase 1 severity threshold and awaiting author review. The registered source remains unchanged. |

### v3 - Author-Bias Grime And Exposure Candidate Review

| Field | Record |
|---|---|
| Asset | `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-phase1-refinement-v3.png` |
| SHA-256 | `0B98BF4CE93F90CB39AD64E8692FE7D27738EEB731ECDFBB9BA2D50DBCCF35CB` |
| Dimensions | `1024x1536` |
| Author bias | `D4 H1 M1 G4 L1 P1`, plus the author note to darken by approximately `10%`: preserve treatment anatomy, material separation, population and geometry; reduce grime toward mostly clean; keep dark treatment readability while lowering exposure. |
| Authorities | v2 controls every panel, figure, hand, treatment contact, material identity, population, room, lamp and object. No identity, pose, geometry or material redesign is authorized. |
| Prompt summary | Remove pervasive grime overlays and retain only localized causal abrasion, rust, dampness and contact stains; darken the full page approximately ten percent while preserving all practical sources and readable silhouettes. |
| Pass 1 - fit-to-page | Pass. Six-panel hierarchy, corridor depth, clinic population, treatment sequence, faces, hands and silhouettes remain readable at the darker exposure. |
| Pass 2 - full-resolution human inspection | Watch. Cassian, Thena, the leader, patients and background workers remain consistent; faces, hair, hands, nails and bandage detail remain specific. |
| Pass 3 - anatomy and movement | Watch. v2's natural hand scale, below-wrist support, bandage manipulation, five-digit contact, aligned wrists/elbows/shoulders and continuous treatment chain remain unchanged. |
| Pass 4 - continuity and geometry | Pass. Population, corridor, clinic, beds, patients, med-kit, table, curtains, lamps, pipes, wet floor, panel boundaries, cameras and blocking remain stable. |
| Pass 5 - material, light, and environment | Watch. Thena's hard metal and the leader's heavy cloth remain distinct; grime is localized to wear, leaks, joins, damp floor and handled surfaces. Exposure is approximately ten percent darker without crushed treatment action or lost population. |
| Pass 6 - artifact and content sweep | Pass. No text, letters, numbers, logos, insignia, watermark, new/missing figures, broken treatment contact, fused digits, gore, neon or unintended generated symbols were observed. |
| Residual scores | `MAT1 FAC1 DET1 HND1 ANA1 KIN1 CNT1 PER1 CST1 ENV1 LGT1 ART0 STY1` |
| Status | `Candidate review`; internally acceptance-compliant and awaiting explicit author approval. The registered source remains unchanged. |

## Pre-Approval Dependency Recheck - 2026-09-01

This is a read-only dependency check. It does not promote a candidate, update the registry, or authorize proof regeneration.

| Authority / chain | Dependents inspected | Finding | Status |
|---|---|---|---|
| Approved `PF1-001` Chapter 1 craft | Page 01 v6, Page 02 v9, Page 03 v7 | Portrait hierarchy, white gutters, restrained grayscale line-and-paint, clean-room geometry, controlled amber accents, caption treatment, and readable silhouettes remain within the working Chapter 1 language. | Pass |
| Approved `PF1-002` Cassian | Page 01 v6, Page 02 v9, Page 03 v7 | Lean build, dark scrubs, black hair, stubble, face, hands, defensive restraint, release, and collapse remain recognizably one Cassian. Expression moves from alarm to controlled disbelief and physical fade without identity drift. | Watch; author approval pending |
| Chapter 1 sequential chain | Page 01 v6 -> Page 02 v9 -> Page 03 v7 | Two attendants, sterile visors, pale uniforms, room, bed, tray, ordinary food knife, linguistic contact, restraint, wrist-origin pulse, translated statement, release, and dropped-knife collapse remain narratively continuous. The knife is broad-face in the Page 02 POV and edge-on in restraint views. Page 03's explanation uses three periods rather than the requested single ellipsis character. | Watch; no severity `2` or `3` finding |
| Approved `PF1-004` Thena | Chapter 14 contextual v3 | Face, dark hair, patched armor, straps, scarf, bandaged wrist, hard metal, guarded posture, and role-specific wear remain consistent; the darker page does not erase her silhouette or treatment contact. | Watch; author approval pending |
| Approved `PF1-008` clinic leader | Chapter 14 contextual v3 | Older broad face, receding dark hair, stubble, heavy work coat, practical hands, below-wrist support, bandage manipulation, and restrained authority remain consistent with the working pair sheet. | Watch; author approval pending |
| Augmented Gor v7 candidate | Chapter 13 contextual `A17` | The existing contextual page still uses the pre-v7 dark-hair/shared-surface treatment and retains the already recorded face, clothing, grapple, impact, and airborne-pose failures. It cannot inherit medium-brown tight curls, the more specific face, or the cleaned material system until v7 is explicitly approved. | Gated; `PF1-014` unchanged |
| Proof layer | Affected Volume 01 reproductions | Not inspected or regenerated because the completion gate requires source-candidate approval first. | Correctly deferred |

## Technical Validation Snapshot - 2026-09-01

- All `18/18` immutable Phase 1 inputs (`A01-A18`) resolve, retain their recorded dimensions, and match the SHA-256 fingerprints in `PROPOSED_FIXES_PHASE_1_2026-09-01.md`.
- All `14/14` current Phase 1 authority/page review selections (`PF1-001` through `PF1-013`, excluding gated `PF1-014`, plus `PF1-015`) resolve, retain their recorded dimensions, and match the SHA-256 fingerprints in this log. All `14/14` are internally acceptance-compliant; author approvals remain pending for `PF1-006`, `PF1-011`, `PF1-012`, `PF1-013`, and `PF1-015`.
- All `14/14` current review selections resolve to the Git LFS `filter=lfs` rule. This verifies prospective routing; pointer and object integrity remain final staging/commit validation tasks.
- All `55/55` untracked Phase 1 PNGs—including immutable gated inputs, superseded candidates, and rejected iterations—open successfully, resolve to the Git LFS rule, and have both their project-relative path and SHA-256 recovery fingerprint recorded in this log.
- All `69/69` unique PNG paths referenced by this review log resolve under `art/graphic_novel/`.
- Prospective Git LFS pointer generation succeeds for all `55/55` untracked Phase 1 PNGs: each produces the canonical three-line version/OID/size structure. Index-pointer validation remains a later staging check; staged-file count is intentionally zero.
- All `86/86` unique paths extracted from the `114` `Available` or `Style Reference` registry rows resolve relative to `art/graphic_novel/`.
- Active branch is `codex/phase-1-artwork-fixes`; staged-file count is `0`.
- No changed path is under `docs/canonical_md/`, `docs/lore_registry.md`, or an Obsidian mirror path.
- `git diff --check` passes. Reported LF-to-CRLF notices are working-tree conversion warnings, not whitespace errors.
- `PF1-014` remains intentionally absent from this candidate count because its stated prerequisite, explicit author approval of augmented-Gor `PF1-006` v7, has not yet been recorded.

## Reset Candidate Record - 2026-09-07

Author decisions `PF1-006`, `PF1-011`, `PF1-012`, `PF1-013`, and `PF1-015` are recorded as `D4`. The following files are new, non-promoted sibling candidates. They do not update the asset registry, proof layer, working authority, or `PF1-014` gate.

| Candidate | SHA-256 | Dimensions | Role / retained review note |
|---|---|---:|---|
| `chapter_01_wakeup/asset-pack-phase1-reset/macro-ward-geometry-v1.png` | `CBFECE3DDFD9876017B957FF7DB0B1AD8858421220C0AE8CA17880941191E3E7` | `1536x1024` | Macro room geometry: cot, tray, door, lighting, and camera grammar. |
| `chapter_01_wakeup/asset-pack-phase1-reset/meso-characters-blocking-v1.png` | `C23A8863B7F6A1B97DC1F614FD0F9EC87C92B96DC001B4768C93AA19FFABF9E0` | `1536x1024` | Baseline character/blocking reference. Tray meal clutter is a watch item; do not use it as prop authority. |
| `chapter_01_wakeup/asset-pack-phase1-reset/meso-restraint-release-v1.png` | `374995F515F93D7E74ADA4293ED607F652E44AEA26F53C95F74CE61F59AC1F70` | `1536x1024` | Retained iteration evidence; superseded because both attendants resolved male. |
| `chapter_01_wakeup/asset-pack-phase1-reset/meso-restraint-release-v2.png` | `FB07F957629D172261100F9C0EB86C6123A1AFE7BE48A30B5B2C953157A1927F` | `1536x1024` | Candidate action authority for female/male attendant distinction, restraint, wrist pulse, release, and dropped knife. |
| `chapter_01_wakeup/asset-pack-phase1-reset/micro-knife-interface-materials-v1.png` | `1553D4157B845F359A5A421BEFBD14A3EDDD0AE4E3C6CF8B0BDE25FCD0490B8F` | `1536x1024` | Candidate reusable ordinary food-knife, interface, pulse, contact, and material authority. |
| `chapter_01_wakeup/candidates/phase1-reset/page-01-art-only-v1-canvas-normalized.png` | `693CB29DA9C3368B9699804382F41E3B457FFF3B406AD3B6F2C11FBFF6564B24` | `1024x1536` | Art-only wake-up/page-one candidate; normalized without cropping onto the standard portrait page canvas. Raw render `page-01-art-only-v1.png` retained as source evidence. |
| `chapter_01_wakeup/candidates/phase1-reset/page-02-art-only-v1-canvas-normalized.png` | `E43F0EE84506BE12D370AC37B6AA40307EC15BFFD1AD1F679DDEF00B06F6D9EC` | `1024x1536` | Art-only restraint/pulse candidate; normalized without cropping onto the standard portrait page canvas. Raw render `page-02-art-only-v1.png` retained as source evidence. |
| `chapter_01_wakeup/candidates/phase1-reset/page-03-art-only-v1-canvas-normalized.png` | `FBCF4CD1EDCE61324A1EF44739D4C52098383E9FAF9252B7EB327CAC16AB63FF` | `1024x1536` | Art-only release/collapse candidate; normalized without cropping onto the standard portrait page canvas. Raw render `page-03-art-only-v1.png` retained as source evidence. |
| `characters/gor-of-almelah/candidates/phase1-reset/continuity-sheet-face-material-v8.png` | `0EEDBF88846A08B74FC04994DA6473F268A417918E9D47EE5DB8A61777581E7D` | `1024x1536` | Targeted v7-derived Gor face/material candidate; review grid-like facial-skin artifact at full resolution. |
| `experiments/visual-language-hierarchy/assets/candidates/phase1-reset/chapter_14_broken_clinic-page-01-contextual-focused-v4.png` | `293285EB48B20751F28A2E4C1AAFF65EF58504E4FDBB39065659A6646EC2BB52` | `1024x1536` | Focused clinic v3-derived treatment-contact candidate; retain armor/fabric/character separation while reviewing hand scale and wrap contact. |

The Chapter 1 asset pack is a production dependency for the three replacement pages. Its micro knife plate is the prop authority for subsequent revisions; the earlier page candidates do not control the new art-only sequence. The three page candidates intentionally remain unlettered. Exact captions and dialogue are deferred until their composition is approved.
