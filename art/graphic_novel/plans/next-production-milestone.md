# Next Graphic Novel Production Milestone

## Baseline

- Preserved milestone commit: `dbb3954` (`Preserve Volume One graphic novel milestone`).
- Planning branch: `codex/next-production-milestone`.
- The milestone contains the 48-page Volume One visual proof, 42 monochrome concept studies across 21 complete A/B subjects, and accepted scene/reference work through Chapter 15 plus Chapter 22.
- The existing proof is visually assembled but is not dialogue-final or publication-ready.

This branch must preserve the accepted milestone non-destructively. Do not overwrite accepted source art, proof pages, continuity sheets, manuscript canon, or lore while carrying out the work below.

## Rectification Status — 2026-09-01

- All 82 requested concept files are present on the milestone branch or in its current rectification worktree.
- 79 files meet the current canvas acceptance rules. Three event plates are preserved as `Deferred` source work because their canvases do not conform: Great Sorrow Concept B (`1535x1024`) and Under-Hive Memory Concepts A and B (`1672x941`).
- The accepted corpus therefore contains 39 complete A/B pairs, one partially accepted pair, and one fully deferred pair.
- Phase 2 selection remains pending. No subject has yet been frozen through a recorded `A`, `B`, `combine`, or `defer` review decision and explicit user approval.

## Definition Of Done

The next production milestone is complete when:

1. The art registry, remaining-scene catalogue, and dialogue queue reflect the assets that actually exist.
2. All 41 concept subjects have complete A/B pairs, for exactly 82 concept images.
3. Every A/B pair has a recorded `A`, `B`, `combine`, or `defer` review decision, with no automatic canon or continuity promotion.
4. The user has reviewed the completed concept corpus and explicitly approved a visual baseline for preservation.
5. The Volume One dialogue queue has been processed one page at a time and the 48-page proof has been rebuilt from approved lettering assets.
6. Chapters 16-21 have approved dependency references and a page-production plan; rendering beyond those approvals remains a separate execution decision.
7. Focused validation passes and the branch is clean at its milestone commit.

## Phase 0: Reconcile Production Trackers

Recommended compute: `MEDIUM`.

The current remaining-scene catalogue predates the new Chapter 11-12 assets and still reports some completed dependencies as missing. Update documentation before generating more work.

- Mark the Central Cognition, Spindle 31 checkpoint, and Lower Grid market references available.
- Mark the three Chapter 11 and three Chapter 12 art-only pages rendered and awaiting lettering.
- Recalculate the remaining chapter count. After reconciliation, Chapters 16-21 are the six unrendered chapters in the active catalogue.
- Record 21 of 41 subjects and 42 of 82 images as the committed baseline, then recalculate live progress so any valid post-baseline A/B pairs are preserved rather than regenerated.
- Confirm the dialogue tracker reports 16 `Pending` pages and 29 `Awaiting Lettering` pages.
- Do not promote exploratory concept sketches into the asset registry during bookkeeping.

Focused tests:

- Every documented `Available` or `Rendered` path exists.
- Tracker counts agree with filesystem counts.
- `rg` finds no stale `Needs Landscape Render` status for the three newly accepted Chapter 11-12 references.
- `git diff --check` passes and no file under `docs/canonical_md/` changes.

## Phase 1: Complete The Concept Corpus

Recommended compute: `HIGH` for visual interpretation; `MEDIUM` for count and tracker updates.

At the committed baseline, 20 subjects and 40 individual images remain. Subtract any complete post-baseline A/B pairs confirmed during Phase 0, then render only the incomplete items. Use one image-generation call per asset and complete each A/B pair before moving to the next subject.

### Batch 1: Production-Critical Systems

Render the six technology subjects first because several are direct dependencies for Chapters 16-18:

- Linguistic Interface / Translation Device.
- Helion-Class Scoutcraft.
- Quantum Entanglement Relay.
- Hyperspace Gate.
- Passive Filament Tracker.
- Cryo-Capable Modification / Augmentation.

### Batch 2: Institutions And Historical Authorities

Render all six institution subjects without inventing insignia, uniforms, slogans, or fixed identities:

- Reversionists.
- Human Continuity Archive.
- The Great Union.
- Coalition of the Willing.
- States of the Great Angel.
- Minority World-State.

### Batch 3: Events And Durable Concepts

Render all eight concept subjects while preserving ambiguity and avoiding illustrative exposition:

- The Voss Effect.
- Voss Conquest.
- Harmony.
- Surface Age.
- Turning Time.
- Great Sorrow.
- Proto-Under Hive.
- Under-Hive Memory.

Focused tests for every pair:

- `concept-a.png` and `concept-b.png` both exist in the required subject directory.
- Each remaining non-character image is `1536x1024` and uses the required landscape/reference-board orientation.
- A and B are materially different concepts, not camera-angle duplicates.
- Images remain monochrome in visual review. A pixel scan may flag strong channel divergence for review, but should not reject subtle warm-paper variation automatically.
- No generated dialogue, labels, slogans, insignia, or explanatory text appears in the art.
- Hidden or disputed identities remain unresolved where the wishlist requires ambiguity.
- No accepted continuity or scene asset is overwritten.
- The wishlist is updated only after both images exist and pass review.

Corpus acceptance tests:

```text
subject directories: 41
concept images:       82
complete A/B pairs:   41
missing A/B files:     0
```

## Phase 2: Review And Freeze The Visual Baseline

Recommended compute: `MAXIMUM AVAILABLE` for the cross-corpus investigation; `MEDIUM` for recording decisions and hashes.

This is an evaluation phase, not a generation phase.

- Build contact sheets by category and one full-corpus index.
- Record `A`, `B`, `combine`, or `defer` for each of the 41 subjects.
- Identify stable Chapter 1 craft invariants: line discipline, anatomy, materials, perspective, physical credibility, and finish.
- Identify contextual authorities that may legitimately vary: location, era, weather, lighting, texture, camera, contrast, and panel rhythm.
- Separate adaptation design decisions from manuscript canon.
- Require explicit user approval before promoting any concept into a continuity sheet, location plate, motif, or style-guide rule.
- Hash the approved baseline and preserve its exact generation prompts, references, dimensions, and review decisions.

Focused tests:

- All 41 subjects have one explicit review decision.
- No `defer` result is promoted.
- Every promoted element cites its source concept and governing canon/reference files.
- Accepted milestone hashes remain unchanged.
- The user approval gate is recorded before any baseline-freeze commit.

## Phase 3: Finish Volume One Dialogue And Lettering

Recommended compute: `HIGH` for manuscript-to-panel judgment; `MEDIUM` for deterministic rendering and proof QA.

Follow `dialogue_correction_todo.md` strictly from top to bottom unless the user selects a specific page.

### Pass A: Existing Generated Text

- Audit the first 16 `Pending` pages one page at a time.
- Transcribe all visible text before correcting it.
- Save corrections non-destructively as `page-##-dialogue-v2.png`.
- Reject any correction that changes faces, hands, clothing, props, staging, gutters, or lighting.

### Pass B: Art-Only Masters

- Letter the 29 `Awaiting Lettering` pages from their controlled specifications.
- Distinguish manuscript dialogue, manuscript narration, environmental text, remembered voice, oath text, and adaptation additions.
- Use deterministic lettering. Do not use generated image text.

### Pass C: Rebuild The Proof

- Rebuild the ordered 48-page sequence and PDF only after individual pages are approved.
- Preserve superseded proof artifacts as clearly named production drafts.

Focused tests:

- Every visible line matches the active canonical source or is explicitly tagged `Adaptation Addition`.
- Speaker attribution, chronology, punctuation, capitalization, and balloon tails are correct.
- Lettering does not cover faces, hands, action geometry, evidence props, or required environmental information.
- All sequence PNGs remain `1024x1536`.
- The rebuilt PDF has exactly 48 pages with a `6x9`-inch media box.
- Fonts are embedded, gutters are readable, and no balloons or captions are cropped.
- Rendering the PDF back to images produces the same page order as the manifest.

## Phase 4: Prepare Chapters 16-21

Recommended compute: `HIGH`.

Do not begin broad page rendering until Phase 3 is complete or the user explicitly reprioritizes the publication hold.

### Chapter 16-18 Dependency Set

- Hive pursuit operators continuity sheet.
- Reversionist terminal and guide-light motif.
- Dead relay and east shaft landscape.
- Reservoir bridge and watch station landscape.
- Passive filament tracker reference.
- West descent, pumpworks, and floodgate landscape.
- Transit-shell technology and interior reference.

### Chapter 19-21 Dependency Set

- Below-the-Map buried street landscape.
- Enclave and boundary-corridor landscape.
- Manual route-cut and boundary-signal motif.
- Evidence prop sheet: coat, route cloth, snapped blade, and failed lantern.

For each chapter, create a source-anchored page map and lettering specification before page generation. Keep art-only masters text-free and generate one asset per image call.

Focused tests:

- Every page cites an exact source span in `docs/canonical_md/`.
- Required character, location, technology, and motif references are available before page production.
- Page masters are exactly `1024x1536` and text-free.
- Character identity, wounds, clothing, props, route geometry, and environmental state remain continuous.
- No page introduces canon, symbols, dialogue, or explanatory imagery absent from the source or an approved adaptation specification.

## Separate Approval-Gated Tracks

These tasks remain in the project TODO but must not be mixed into this production branch without an explicit user decision:

1. **Reasoning-effort checkpoint:** implement the project-wide rule in `AGENTS.md` with a concise graphic-novel application note in `art/graphic_novel/SOP.md`. Use a separate branch from the preserved baseline because this changes agent-governance policy.
2. **Silo engineering and canon reconciliation:** resolve the Type I geothermal vent/silo function, scale, distribution, and terminology before changing manuscript or lore. Treat the existing sketches as adaptation exploration only.
3. **Controlled visual-language experiments:** the isolated hierarchy experiment has been explicitly approved for recovery onto this branch as evaluation material only. It uses derived copies, does not overwrite accepted assets, and cannot promote a visual rule before the corpus review gate.

## Focused Validation Commands

Use the bundled workspace Python runtime for image and PDF inspection. Keep validation read-only except for intentionally generated contact sheets or reports.

```powershell
git diff --check
git status --short
git lfs ls-files
rg -n "Pending|Awaiting Lettering|Correction Rendered|Approved" art/graphic_novel/dialogue_correction_todo.md
rg -n "Needs Continuity Sheet|Needs Landscape Render|Needs Tech Render|Needs Motif Render" art/graphic_novel/remaining_scene_catalogue.md
```

The image validator should report:

- concept subject, A/B completeness, dimensions, and orientation;
- proof sequence count and dimensions;
- scene-master count and dimensions;
- accepted-asset hash changes;
- files containing unexpected embedded text metadata, while leaving visual text review manual.

The PDF validator should report:

- page count;
- media-box dimensions;
- font embedding;
- manifest order;
- rendered-page dimensions and crop boundaries.

## Commit Boundaries

Keep commits reviewable and reversible:

1. Reconcile production trackers.
2. Complete each concept category or other small reviewed batch.
3. Record corpus-selection decisions and baseline hashes.
4. Correct and approve dialogue in small page batches.
5. Rebuild and validate the proof.
6. Add approved Chapter 16-21 references and page plans.

Do not push, merge, sync Obsidian, or modify canon unless separately requested.
