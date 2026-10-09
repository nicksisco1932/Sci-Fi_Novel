# Hive repository — source of truth and release protocol

**Effective 2026-10-08.** This protocol distinguishes mutable narrative source from frozen reading artifacts. It does not assert that any local Windows worktree has been synced.

## Authority, in priority order

1. **Working manuscript:** `main:docs/canonical_md/*.md` (merged Chapter 1 and Chapters 4–30). Edit only these files for prose. Consult `docs/lore_registry.md` and `docs/canonical_md/Current Timeline Summary.md` for canon.
2. **Working back matter:** `main:docs/appendices/*.md`. Source appendix status may be developmental; inclusion in a beta does not automatically canonize it.
3. **Non-canonical exploration:** `docs/developmental/`. The 2026-10-08 author-note revision is saved here as v0.2. Foreword/afterword placement is **unresolved**, so it is not part of a reading edition.
4. **Superseded source:** `Legacy/`. The old `docs/canonical/` contained 17 DOCX files whose Git blob identities matched `Legacy/` exactly. Those duplicated tracked paths were removed, but the original DOCX bytes remain archived and recoverable through Git history.
5. **Exports:** PDFs, DOCX beta copies, website and graphic-novel adaptations never become narrative source by virtue of a newer modification date.

## Git branches and worktrees

- `main` is the integrated, evolving prose source; task branches may contribute to it after review and verification.
- The frozen October 7 v2 reading edition came from source commit `c41140b00b9fe348f546ada77a9143413ae5894e`, not from an arbitrary branch head or today's checkout.
- On 2026-10-08, `main` was fast-forwarded from `dbb3954e57703a776e3d0a6cc9acc703e81139ad` to `26a569044fc6abd2054f9b6cb481c77aeab56296`. The former tip is backed up on `archive/main-before-consolidation-2026-10-08`.
- Two Windows worktrees are known: `C:/Users/nicks/Documents/GitHub/Sci-Fi_Novel` and `C:/Users/nicks/.codex/worktrees/a83b/Sci-Fi_Novel`. Their uncommitted contents cannot be inferred from GitHub. Read `git worktree list`, `git branch --show-current`, `git status --short --untracked-files=all`, and `git diff` (including staged changes) **in each** before fetching, changing branches, pulling, or removing files. Preserve, commit, or carefully stash local author changes before integration. Do not force-reset or clean them.

## Immutable production stages

| Stage | Meaning | Paths |
| --- | --- | --- |
| **Working** | Ongoing editorial changes | `docs/canonical_md/`, `docs/appendices/` |
| **Beta** | Reviewable reader copy with provenance | New: `editions/beta/<book>/<edition-id>/`; legacy v2: `beta_readers/editions/` and `output/pdf/` |
| **Proof** | Final typesetting/copyedit, **not yet public** | `editions/proofs/<book>/<edition-id>/` |
| **Published** | Explicitly approved distribution package | `editions/published/<book>/<edition-id>/` |
| **Archive** | Superseded snapshots and recovered sources | `Legacy/` and Git history |

An edition ID is immutable. Each new edition requires its own manifest, ordered source inventory, exact source commit, file hashes, verification record, and export. Never overwrite a prior PDF or reuse its edition ID. A beta is not published merely because a file exists on GitHub. If a reading edition includes a proposed foreword or afterword, place it in its new manifest explicitly and update/test the builder to support that role before release.

The existing beta builder validates **28 chapters + three appendices**. The output destination supports the older `output/pdf/` layout and new `editions/beta/` layout. It does not yet incorporate optional author-note source roles. Do not silently concatenate front or back matter or alter the verified 2026-10-07 v2 package.

## Before any future beta/proof/publication

1. Reconcile each relevant local worktree; confirm which edits are committed.
2. Work from the integrated `main` source or an explicitly identified revision branch, and review the diff.
3. Inventory the exact chapter order and included front/back matter; resolve known continuity alerts.
4. Checkpoint the source in Git. Generate a **new** edition manifest referencing that full commit and hashes.
5. Export to a fresh stage/edition path. Validate text completeness, source hashes, bookmark order, output digest, and all rendered pages; publish the verification evidence.
6. Only after explicit authorization, promote a proof to `published/`. Historical beta, proof, and published packages remain byte-for-byte immutable.

Use `python tools/verify_source_tree.py` to check the source hierarchy and legacy beta evidence without changing files.
