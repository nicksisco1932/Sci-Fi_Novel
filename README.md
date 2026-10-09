# Hive — source and release index

**Single active working manuscript:** [`docs/canonical_md/`](docs/canonical_md/) on the integrated `main` branch. The merged Chapter 1 and Chapters 4–30 are the working prose; [`docs/appendices/`](docs/appendices/) contains source appendices. Read [the source-of-truth protocol](docs/SOURCE_OF_TRUTH.md) before modifying or exporting the book.

## Current private reader edition (immutable)

**Hive: Earth — 2026-10-07 v2**, verified 166-page PDF, 28 chapter files and three appendices.

- [Beta edition and recovery index](beta_readers/README.md)
- [Reading PDF](output/pdf/Hive_Earth_Beta_Reader_2026-10-07-v2.pdf)
- [Frozen manifest](beta_readers/editions/2026-10-07-v2.json)
- [Verification record](beta_readers/editions/2026-10-07-v2.verification.json)
- Manuscript source checkpoint: `c41140b00b9fe348f546ada77a9143413ae5894e`

This is a release snapshot, **not** the current working tree. Never modify or overwrite its PDF, manifest, verification, or delivery record.

## Directory roles

| Location | Status |
| --- | --- |
| `docs/canonical_md/` | **Only active prose manuscript source** |
| `docs/appendices/` | Working appendix sources |
| `docs/developmental/` | Non-canonical exploration; includes author note v0.2 |
| `docs/character_dossiers/`, `docs/lore_registry.md` | Character and continuity references |
| `Legacy/` | Historical DOCX and superseded artifacts, never an editing baseline |
| `beta_readers/` | Existing beta builder, legacy edition manifests, tests |
| `output/pdf/` | Frozen legacy PDF exports |
| `editions/beta/` | New immutable beta editions and their manifests |
| `editions/proofs/` | Typeset proofs after editorial lock |
| `editions/published/` | Final, intentionally approved publications |
| `art/` | Artwork and graphic-novel workstreams; not manuscript authority |

The redundant `docs/canonical/` folder was removed after all 17 DOCX blobs were verified identical to their archived copies in `Legacy/`. Do not recreate it or edit the DOCX copies as if they were current.

The revised *What the Record Loses* author note is a **developmental draft**, not included in the frozen October 7 edition; foreword versus afterword placement remains open.

## Safe startup (multiple Windows worktrees)

The local checkout at `C:/Users/nicks/Documents/GitHub/Sci-Fi_Novel` and the Codex worktree at `C:/Users/nicks/.codex/worktrees/a83b/Sci-Fi_Novel` are separate. Before editing or synchronizing either, inspect `git status --short --untracked-files=all`, `git branch --show-current`, `git rev-parse HEAD`, and `git worktree list`. **Do not reset, clean, checkout, or pull over uncommitted author work.**

The older Chapter 15 stopping point is historical public/graphic-novel release context; it does not truncate the current 30-chapter private beta draft.
