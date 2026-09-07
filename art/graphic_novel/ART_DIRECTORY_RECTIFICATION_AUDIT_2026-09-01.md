# Graphic-Novel Art Directory Rectification Audit - 2026-09-01

Status: inventory and migration proposal only. Do not move, rename, deduplicate, delete, or redirect assets until Phase 1 corrections are complete, committed, and separately approved for path migration.

Purpose: make visual authorities, candidates, experiments, concepts, scene sources, and derived proofs easier to find without breaking registry entries, study notes, experiment reports, LFS pointers, or historical review evidence.

## Current Snapshot

The read-only inventory on `2026-09-01` found:

| Metric | Count |
|---|---:|
| All files under `art/graphic_novel/` | `304` |
| PNG files | `258` |
| Markdown files | `42` |
| PDF files | `1` |
| Exact duplicate PNG hash groups | `5` |
| Files participating in exact duplicate groups | `11` |

Top-level distribution at the time of the audit:

| Directory | Files | PNG | Markdown | PDF |
|---|---:|---:|---:|---:|
| `chapter_01_wakeup/` | `6` | `6` | `0` | `0` |
| `characters/` | `27` | `27` | `0` | `0` |
| `concept_sketches/` | `82` | `82` | `0` | `0` |
| `experiments/` | `17` | `11` | `5` | `0` |
| `locations/` | `16` | `14` | `2` | `0` |
| `lore/` | `16` | `15` | `1` | `0` |
| `motifs/` | `5` | `5` | `0` | `0` |
| `plans/` | `4` | `0` | `4` | `0` |
| `proofs/` | `56` | `50` | `3` | `1` |
| `scenes/` | `62` | `46` | `16` | `0` |
| `style_refs/` | `1` | `1` | `0` | `0` |
| `tech/` | `1` | `1` | `0` | `0` |

Phase 1 candidates created after the snapshot will increase the working count. The table is a dated baseline, not a permanent registry total.

## Discoverability Findings

### Generic Basename Collisions

The same filename is reused across many unrelated subjects:

| Basename | Occurrences |
|---|---:|
| `concept-a.png` | `41` |
| `concept-b.png` | `41` |
| `page-01.png` | `21` |
| `page-02.png` | `15` |
| `landscape-reference.png` | `13` |
| `continuity-sheet.png` | `9` |
| `page-03.png` | `8` |
| `reference.png` | `6` |

These names are safe only when the full path is already known. Search results, generated-image prompts, review notes, and human conversation become ambiguous when paths are shortened.

### Mixed Lifecycle States

Several subject directories currently place immutable sources, refinement pilots, rejected iterations, review candidates, and eventual authorities beside one another. Filename suffixes carry most of the lifecycle meaning, and that meaning is not consistent across older and newer work.

### Cross-Category Copies

Five groups are byte-identical while serving different semantic roles:

| SHA-256 prefix | Paths |
|---|---|
| `BB721D92...` | `lore/voss/voss-lore-continuity-sheet.png`; `motifs/maribel-voss-mural/reference.png`; `motifs/under-hive-memory-mural-style/reference.png` |
| `029093C2...` | `locations/broken-clinic/landscape-reference.png`; `locations/lower-grid-lanes-between-signals/landscape-reference.png` |
| `14585A38...` | `motifs/hive-amber-alert-state/reference.png`; `tech/cognitive-pattern-testing-interface/reference.png` |
| `EBFF2C25...` | `characters/gor-of-almelah/continuity-sheet.png`; `motifs/almelah-oath-augmentation-contrast/reference.png` |
| `EF95C4B4...` | `locations/surface-age-stack-field/landscape-reference.png`; `lore/voss/surface-age-stacks-landscape.png` |

These may be intentional semantic mirrors. Do not deduplicate them automatically. First designate one canonical visual authority and record whether each additional path is a deliberate role-specific mirror, a generated derivative, or an obsolete duplicate.

### Authority Leakage From Experiments

Some experiment outputs now supply approved narrow style or detail behavior. Their production role is documented, but their paths remain under `experiments/`, making them easy to overlook or misclassify.

## Recommended Organization Model

The existing top-level subject categories are useful and should not be replaced wholesale. Apply lifecycle grouping inside each subject directory instead:

```text
art/graphic_novel/
  characters/<subject>/
    source/
    candidates/<phase-or-study>/
    approved/
    archive/
  chapters/<chapter>/
    source/
    candidates/<phase-or-study>/
    approved/
  scenes/<chapter-or-sequence>/<scene>/
    source/
    candidates/
    approved/
  locations/<subject>/
  lore/<subject>/
  motifs/<subject>/
  development/
    concept-sketches/
    experiments/
    style-references/
  outputs/
    proofs/
  catalog/
    asset-registry.md
    authority-map.md
    migration-map.md
```

This is a conceptual target. Exact casing, hyphenation, and whether `chapter_01_wakeup/` becomes `chapters/chapter-01/` require a separate approval because those decisions affect many established paths.

## Naming Rules Proposed For Migration

1. Keep the subject slug in every filename that may appear outside its directory, such as `cassian-rho-continuity-source.png` or `chapter-01-page-01-approved.png`.
2. Encode lifecycle in the directory, not only in long suffixes.
3. Keep iteration numbers inside `candidates/<phase>/`; do not overwrite or silently promote.
4. Reserve `approved/` for author-approved production authorities and pages.
5. Keep rejected but informative generations under `archive/<phase>/` with their hashes and rejection reason.
6. Keep derived proofs under `outputs/proofs/`; never treat them as editable sources.
7. Give each intentional semantic mirror a registry record pointing to its canonical authority hash.
8. Keep concept sketches isolated from production-quality acceptance counts.

## Safe Migration Sequence

1. Finish and commit Phase 1 at stable paths.
2. Freeze a complete path, SHA-256, dimensions, LFS, registry-status, and reference manifest.
3. Assign every image one lifecycle role: source, candidate, approved, archived iteration, experiment, concept, style reference, semantic mirror, or derived proof.
4. Draft an explicit old-path to new-path migration table; review it before moving files.
5. Move one category at a time with Git-aware moves after resolving absolute targets.
6. Update `asset_registry.md`, study notes, experiment reports, visual briefs, plans, proof notes, and prompt references in the same change unit.
7. Search the entire repository for every old path and ambiguous basename.
8. Validate dimensions and SHA-256 continuity after moves; moving must not alter image bytes.
9. Run `git diff --check`, `git lfs fsck`, registry path checks, and a manual documentation diff.
10. Commit organization separately from artwork correction and keep the old commit history recoverable.

## Explicit Non-Actions During Phase 1

- No source, candidate, experiment, concept, proof, or reference path is moved.
- No exact duplicate is deleted or replaced by a link.
- No registered status is changed merely because a file appears redundant.
- No manuscript, lore canon, or Obsidian path is changed.
- No migration commit is mixed with the artwork-correction commit set.
