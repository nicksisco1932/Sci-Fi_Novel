# Graphic-Novel Asset Ecosystem Map — 2026-09-04

Status: documentation-only working-tree snapshot and migration proposal. This document does not promote, move, rename, delete, deduplicate, regenerate, or canonize an asset.

Companion inventory: `art/graphic_novel/ASSET_INVENTORY_AND_MIGRATION_MAP_2026-09-04.csv`.

Historical baseline: `art/graphic_novel/ART_DIRECTORY_RECTIFICATION_AUDIT_2026-09-01.md`. That audit remains intact and should be read as a dated predecessor, not as the current file count.

## Snapshot Boundary

The inventory freezes the working tree before this map and its CSV were added.

| Field | Value |
|---|---|
| Snapshot date | `2026-09-04` |
| Git HEAD | `b24f2b55140833b0a1d56d54c2c1d46fcf479972` |
| Existing files represented | `344` |
| Additional planned-asset records | `21` |
| Total CSV records | `365` |
| Mapping outputs excluded from baseline | `2` |
| Expected files under `art/graphic_novel/` after this task | `346` |

The snapshot includes all tracked, modified, and untracked files under `art/graphic_novel/`. It excludes `art/music/`, manuscript files, lore documents outside the art tree, Obsidian mirrors, and the two mapping outputs. Manuscript and lore paths appear only as dependencies or source locators.

The working tree was already dirty. Existing modifications and untracked Phase 1 material are treated as intentional project state and were not altered.

## Physical Inventory

### Files by format

| Format | Existing files |
|---|---:|
| PNG | `295` |
| Markdown | `45` |
| SHA-256 manifest | `2` |
| PDF | `1` |
| Python proof builder | `1` |
| **Total** | **`344`** |

All `295` PNG files opened successfully during the snapshot. No corrupt PNG was found.

### Files by production domain

| Domain | Existing files | Current function |
|---|---:|---|
| Scene art | `90` | Chapter pages, sequence records, lettering specifications, and the outlying Chapter 1 wake-up set. |
| Concept development | `88` | The 82-image A/B wishlist, five Hive Earth systems sheets, and their index. |
| Proof outputs | `56` | A rebuildable 48-page sequence, contact sheets, PDF, manifest, review, hashes, and builder. |
| Characters | `34` | Registered continuity authorities and Phase 1 identity/material iterations. |
| Experiments | `20` | Korin material studies and the layered visual-language experiment. |
| Locations | `16` | Approved environmental references and visual briefs. |
| Lore art | `16` | Voss studies, murals, Surface Age material, and historical plates. |
| Governance | `13` | SOPs, registries, audits, catalogues, milestone records, and review entry points. |
| Motifs | `5` | Registered thematic or interface mirrors and references. |
| Plans | `4` | Preserved production and experiment plans. |
| Style references | `1` | Surface Age stack-field contextual style reference. |
| Technology | `1` | Cognitive-pattern testing interface authority. |

### Git state

| Git state | Existing files |
|---|---:|
| Tracked and clean | `272` |
| Tracked and modified | `5` |
| Untracked | `67` |

The untracked set contains `60` PNGs and `7` Markdown records. The PNGs comprise the `55` Phase 1 images documented by the Phase 1 review log and the five Hive Earth systems sheets. Their untracked state is storage state, not an authority judgment.

### Canvas inventory

| Dimensions | PNGs |
|---|---:|
| `1024×1536` | `174` |
| `1536×1024` | `81` |
| `1672×941` | `22` |
| `1122×1402` | `6` |
| `1086×1448` | `3` |
| `1671×941` | `2` |
| `971×1619` | `2` |
| `1032×1136` | `1` |
| `1264×2672` | `1` |
| `1535×1024` | `1` |
| `1670×941` | `1` |
| `972×1619` | `1` |

Nonstandard canvases are recorded rather than automatically rejected. Some are documented generated evidence, normalized predecessors, contact sheets, or deliberately deferred concept sources.

## Identification Model

The CSV separates a durable logical asset from each physical realization.

- `logical_asset_id` identifies the enduring subject or deliverable. It intentionally repeats across versions and manifestations.
- `artifact_id` identifies one physical realization and is unique. It combines a semantic identifier, preserved version or role information, and a short SHA-256 prefix.
- Promotion or migration does not change either identifier.
- Planned assets receive deterministic `PLANNED` artifact IDs based on their declared paths.

For example, the registered Cassian continuity sheet and its Phase 1 refinements share the logical family `GN-CHAR-CASSIAN-RHO-CONTINUITY-SHEET`; each file has its own artifact ID.

Logical-ID repetition is valid only when the records are versions, normalized manifestations, mirrors, derivatives, or otherwise documented realizations of the same logical asset. Current paths and artifact IDs must remain unique.

## Classification Model

The map does not use a single status field to answer several different questions.

### Lifecycle

`approved`, `approved-working`, `candidate`, `concept`, `experiment`, `superseded`, `rejected`, or `planned`.

Lifecycle describes where the artifact stands in its own history. It does not establish the scope in which another generation may rely on it.

### Artifact roles

`primary`, `semantic-mirror`, `derived-output`, `production-reference`, `governing-document`, `record`, `source`, or `other`.

Roles are semicolon-delimited because they can coexist. An approved image may be both a primary artifact and a production reference. An experimental image may be a protected source for a later candidate without becoming an approved visual authority.

### Authority scope

`foundational-craft`, `identity`, `contextual-environment`, `narrow-detail`, or `none`.

Authority is scoped rather than global. The conflict rule remains:

1. Manuscript and lore canon govern what exists, chronology, character facts, technology, and narrative events.
2. Identity authorities govern stable faces, bodies, costume, equipment, augmentation geometry, and injury state.
3. Foundational visual authority governs rendering discipline, anatomy, materials, perspective, physical plausibility, and finish.
4. Contextual authorities govern environment, weather, palette, local camera language, contrast, and scene rhythm.
5. Narrow references govern only their documented detail, such as human skin behavior or one interface family.
6. Scene adaptation may vary lower-level presentation but cannot override a higher authority within that authority's scope.

Accepted art is an **approved visual authority**. It is constrained by canon but does not become prose-level canon merely through visual approval.

### Decision and canon state

Decision state records whether classification is `settled`, `author-review-required`, `phase1-reconciliation-required`, `dependency-blocked`, or `deferred`.

Canon status records whether something is a `canon-source`, `canon-constrained`, `non-canon`, or `not-applicable` artifact. No generated image in this inventory is treated as a canon source.

## Authority Findings

### Foundational craft

`chapter_01_wakeup/continuity-sheet.png` remains the registered foundational visual authority. `chapter_01_wakeup/continuity-sheet-phase1-refinement-v2.png` is the author-approved Phase 1 working authority. The refinement may govern Phase 1 propagation, but it does not replace the registered source until `PF1-016` reconciliation.

The Korin partial-face study at `experiments/korin-office-meditation/assets/study-02-partial-face.png` is an approved narrow-detail reference. It controls restrained human microdetail only; it does not control identity, composition, palette, location, costume, or scene continuity.

### Approved Phase 1 working authorities

Nine files have explicit author approval for Phase 1 propagation while the registered sources remain unchanged:

| Scope | Working authority |
|---|---|
| Foundational craft | `chapter_01_wakeup/continuity-sheet-phase1-refinement-v2.png` |
| Cassian identity | `characters/cassian-rho/continuity-sheet-phase1-refinement-v2.png` |
| Alyen identity/action | `characters/alyen-ithra/continuity-sheet-phase1-refinement-v2.png` |
| Thena identity/equipment | `characters/thena/continuity-sheet-phase1-refinement-v1-canvas-normalized.png` |
| Young Gor identity | `characters/gor-of-almelah/continuity-sheet-young-phase1-refinement-v2.png` |
| Korin identity | `characters/korin-tal/continuity-sheet-phase1-refinement-v1.png` |
| Clinic leader and guard | `characters/broken-clinic-leader-and-guard/continuity-sheet-phase1-refinement-v2.png` |
| Below-the-Map escort | `characters/below-the-map-escort/continuity-sheet-phase1-refinement-v1.png` |
| Almelah dojo master | `characters/almelah-dojo-master/continuity-sheet-material-refinement-v3.png` |

These remain `approved-working`, not `approved`, in the map. Their proposed action is promotion only after Phase 1 reconciliation.

### Author decisions still required

Five current finalists are internally acceptance-compliant but still await explicit author review:

- `characters/gor-of-almelah/continuity-sheet-phase1-refinement-v7.png`
- `chapter_01_wakeup/page-01-phase1-refinement-v6.png`
- `chapter_01_wakeup/page-02-phase1-refinement-v9.png`
- `chapter_01_wakeup/page-03-phase1-refinement-v7.png`
- `experiments/visual-language-hierarchy/assets/chapter_14_broken_clinic-page-01-contextual-phase1-refinement-v3.png`

They remain candidates. Filename recency, internal QA, or inclusion in a review sheet does not promote them.

### Gated work

`PF1-014` has no generated correction candidate. Its immutable experimental input is:

`experiments/visual-language-hierarchy/assets/chapter_13_soft_edge-page-01-contextual-material-refinement-perspective-v2.png`

It remains an experiment and protected source, with `dependency-blocked` decision state. Its gate is explicit approval of augmented-Gor `PF1-006` v7 followed by generation and review of the actual `PF1-014` correction.

`PF1-016` remains incomplete. No affected Phase 1 source, working authority, candidate, or retained iteration should be physically reorganized before that reconciliation.

### Registry gap

`scenes/chapter_01_korin_office/page-01.png` is used by the Volume One proof and appears in the dialogue queue, but it has no generated-asset row in `asset_registry.md`. The map classifies it conservatively as `approved-working` with `phase1-reconciliation-required`, rather than inferring approval from proof inclusion.

### Planned assets

The registry declares `21` PNG destinations that do not exist. They remain planned records, not corrupt or missing-file failures. These include unresolved character sheets, location references, technology references, and motifs. `Canon Check Needed` produces a dependency block; other unrendered destinations remain deferred until scheduled production need.

## Exact Duplicate And Mirror Map

Five SHA-256 groups contain eleven physical files. Each group has one proposed primary authority and one or more semantic mirrors. No physical deduplication is authorized.

| Group | Proposed primary | Semantic mirror or mirrors |
|---|---|---|
| `DUP-001` | `locations/broken-clinic/landscape-reference.png` | `locations/lower-grid-lanes-between-signals/landscape-reference.png` |
| `DUP-002` | `tech/cognitive-pattern-testing-interface/reference.png` | `motifs/hive-amber-alert-state/reference.png` |
| `DUP-003` | `lore/voss/voss-lore-continuity-sheet.png` | `motifs/maribel-voss-mural/reference.png`; `motifs/under-hive-memory-mural-style/reference.png` |
| `DUP-004` | `characters/gor-of-almelah/continuity-sheet.png` | `motifs/almelah-oath-augmentation-contrast/reference.png` |
| `DUP-005` | `locations/surface-age-stack-field/landscape-reference.png` | `lore/voss/surface-age-stacks-landscape.png` |

The primary designation identifies the semantic owner of the image bytes. A mirror retains its own role and lookup path. The copies should remain physical until a later catalogue can resolve aliases without breaking prompts, notes, proof builders, or human navigation.

## Dependency Map

The CSV records path-level `depends_on`, `derived_from`, `mirrors`, and `used_by` relationships. The principal chains are:

### Chapter 1 and foundational grammar

```text
Chapter 1 manuscript
  → wake-up combined continuity authority
    → dedicated Cassian and other character authorities
      → Chapter 1 page candidates
        → dialogue review
          → Volume One proof sequence
```

The Phase 1 foundational refinement is a working authority inside this chain, not a registered replacement.

### Gor and Chapters 13–15

```text
young Gor authority + Almelah dojo/master references
  → augmented Gor authority and Phase 1 refinements
    → Chapter 13 pursuit
    → Chapter 15 memory, fall, recognition, and rain sequences
```

Approval of augmented-Gor v7 is also a direct prerequisite for `PF1-014`.

### Hive Earth

```text
manuscript and lore constraints
  → Hive city, Spindle, integration-map, Lower Grid, and Voss-era references
    → chapter scene pages
    → exploratory macro/meso/micro systems sheets
```

The five Hive Earth systems sheets remain non-canon concepts. They have production-reference value without governing later images:

| Sheet | Authority scope | Decision state | Action |
|---|---|---|---|
| Class differences | Contextual environment | Author review required | Leave |
| Mind link | Narrow detail | Author review required | Leave |
| Blade technology | Narrow detail | Author review required | Leave |
| Scavenger projectile technology | Narrow detail | Author review required | Leave |
| Hive Earth scarred recovery | Contextual environment | Author review required | Leave |

Their printed filenames and current paths should remain stable during this mapping phase.

### Voss and Chapter 22

```text
Voss lore and appendix constraints
  → Voss lore continuity sheet
    → mural and Under-Hive semantic mirrors
      → Chapter 22 runoff route and mural staging
```

The dark Voss drafts remain deferred style-rerender candidates. The river-city sequence remains adaptation-only historical study material even where it is visually useful.

### Proof outputs

The Volume One `manifest.md` maps source pages into a deterministic 48-page sequence. Sequence files, contact sheets, and the PDF are `derived-output` artifacts with no authority scope. The proof's use of an image does not approve that image or supersede its source classification. After any authorized path migration, proof artifacts must be rebuilt from the updated manifest rather than treated as editable masters.

## Metadata Coverage

Prompt preservation is uneven:

- `5` PNGs have a full prompt record in the layered visual-language experiment.
- `145` PNGs have prompt summaries, chiefly Phase 1 and concept-development material.
- `145` PNGs have no retained prompt record discoverable in the repository.

The map records absence without reconstructing lost instructions. `classification_basis` states why each classification was assigned. Where `manual-inference` appears, `classification_notes` explains the filesystem or document evidence used.

## Friction Points

1. **Lifecycle mixing.** Registered sources, approved working authorities, pending candidates, rejected attempts, and normalized evidence often occupy one subject directory.
2. **Generic basenames.** `concept-a.png`, `concept-b.png`, `page-01.png`, `landscape-reference.png`, `continuity-sheet.png`, and `reference.png` are understandable only with their full paths.
3. **Split authority records.** The registry describes production sources while newer working authority lives in Phase 1 logs and author-review records.
4. **Experiment leakage.** Some experiments supply valuable narrow references or appear in a proof while retaining experimental lifecycle.
5. **Physical semantic copies.** Exact duplicate images serve different lookup roles without a first-class alias model.
6. **Incomplete prompt provenance.** Many accepted assets preserve outcome and usage but not the exact generation instruction.
7. **Derived-output visibility.** Fifty-one PNG/PDF proof artifacts inflate image totals even though they are rebuildable and non-authoritative.
8. **One structural outlier.** `chapter_01_wakeup/` performs the same production role as directories under `scenes/` but sits beside the category tree.

## Proposed Target Architecture

Keep the existing subject categories. Add lifecycle directories inside subjects only after Phase 1 is reconciled and a migration is separately authorized.

```text
art/graphic_novel/
  characters/<subject>/
    approved/
    candidates/<batch>/
    archive/<batch>/
  locations/<subject>/
    approved/
    candidates/<batch>/
    archive/<batch>/
  tech|motifs|lore/<subject>/
    approved/
    candidates/<batch>/
    archive/<batch>/
  scenes/<chapter-scene>/
    approved/
    candidates/<batch>/
    archive/<batch>/
```

Use `source/` only when an immutable external visual input is neither a candidate nor an approved production asset. Do not copy canonical manuscript prose into the art tree.

Concept sketches, experiments, proofs, plans, and governing documents should remain in their functional domains. Their lifecycle and role are made explicit through the inventory rather than by forcing them into an `approved` tree.

The outlying `chapter_01_wakeup/` directory should eventually become `scenes/chapter_01_wakeup/`. That move is gated on Phase 1 reconciliation because it contains registered sources and the largest concentration of active candidates.

## Naming Policy

Lifecycle belongs in directories. Filenames should carry subject, asset role, and only versions that are already supported by provenance.

Examples:

- `characters/cassian-rho/approved/cassian-rho-continuity-sheet.png`
- `characters/cassian-rho/candidates/phase-1/cassian-rho-continuity-sheet-phase1-refinement-v2.png`
- `scenes/chapter_01_wakeup/approved/chapter_01_wakeup-page-01.png`
- `concept_sketches/locations/hive-earth/hive-earth-concept-a.png`

Do not assign invented maturity versions to legacy unversioned authorities. Existing `v0.1`, Phase 1, pilot, normalization, and pass identifiers remain part of their lineage.

## Per-Artifact Migration Decisions

Every CSV record has one proposed action and destination:

| Action | Records | Meaning |
|---|---:|---|
| Rename | `82` | Add the subject slug to generic A/B concept filenames without changing their development domain. |
| Move | `70` | Place settled authorities in lifecycle directories when migration is authorized. |
| Leave | `67` | Preserve functional governance, experiment, concept-system, or source paths. |
| Rebuild derived output | `51` | Recreate proof artifacts after source-path migration. |
| Defer | `33` | Wait for canon, production, rerender, or scheduling decisions. |
| Archive | `32` | Preserve explicitly rejected or superseded evidence under its batch archive. |
| Promote after approval | `24` | Keep in candidates until author review or `PF1-016` permits promotion. |
| Retain as mirror | `6` | Preserve an intentional cross-category physical copy and point it to its primary hash authority. |

These are recommendations, not executed operations. `proposed_path` is populated even when the proposed action is `leave`, allowing a later migration tool to compare current and intended state without guessing.

## Safe Migration Sequence

1. Resolve the five author decisions, generate and review `PF1-014`, and complete `PF1-016`.
2. Adopt the logical and artifact IDs in a durable catalogue without moving files.
3. Rename the low-risk A/B concept assets and verify every wishlist reference.
4. Migrate reusable character, location, technology, motif, lore, and style authorities one subject at a time.
5. Migrate scene sources, candidates, archives, and the Chapter 1 wake-up outlier.
6. Update the proof manifest and rebuild all derived proof outputs.
7. Recheck every old path, dependency edge, SHA-256, dimension, LFS attribute, and registry reference.

Organization changes should be committed separately from artwork correction. No migration should delete historical generations; rejected work remains recoverable evidence.

## CSV Field Guide

| Field group | Fields |
|---|---|
| Snapshot | `snapshot_date`, `snapshot_git_head`, `record_kind` |
| Identity | `logical_asset_id`, `artifact_id`, `current_path`, `filename`, `domain`, `subject`, `asset_type`, `version`, `batch_id` |
| Integrity | `exists`, `extension`, `byte_size`, `sha256`, `width`, `height`, `duplicate_group`, `git_state`, `lfs_policy` |
| Classification | `lifecycle`, `artifact_roles`, `authority_scope`, `canon_status`, `review_status`, `decision_state`, `prompt_record` |
| Provenance | `classification_basis`, `classification_notes`, `evidence_source`, `source_locator` |
| Relationships | `depends_on`, `derived_from`, `supersedes`, `mirrors`, `used_by` |
| Migration | `metadata_gaps`, `proposed_action`, `proposed_path`, `migration_gate`, `notes` |

Semicolon-delimited fields contain controlled multiple values. Paths are repository-relative beneath `art/graphic_novel/` unless a field explicitly names an external repo source.

## Validation State

- The CSV contains `344` unique existing-file paths and `21` unique planned-asset paths.
- All artifact IDs are unique.
- Repeated logical IDs are used for documented manifestations rather than accidental identifier collision.
- All `295` PNG records have readable dimensions and SHA-256 values.
- Five exact duplicate hash groups containing eleven files are reproduced.
- Pending Phase 1 candidates remain candidates.
- Nine approved working authorities remain distinct from registered approved sources.
- The gated `PF1-014` input remains an experiment and dependency-blocked source.
- Planned assets are not classified as corrupt files.
- Proof pages, contact sheets, and PDF are non-authoritative derivatives.
- No manuscript, lore, registry, artwork, Phase 1 record, directory, or Obsidian file was changed by this mapping task.

