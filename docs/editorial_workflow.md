# Editorial Workflow

## Current Stage

On 2026-10-09 the author accepted the current v0.2 beta manuscript as the most polished version and the working baseline. Its 28 chapter files were promoted exactly into `docs/canonical_md/`. Start future development there. See `docs/working_baseline.md` for source hashes, recovery, and acceptance scope.

The next editorial milestone is a proposal-only Copy Editor review. Preserve the accepted voice and rhythm; further developmental changes require the author's requested scope. The author has accepted the baseline, not claimed that copyediting is complete.

## Source of Truth
- Primary working draft: `docs/canonical_md/`
- Continuity reference: `docs/lore_registry.md`
- Timeline reference: `docs/canonical_md/Current Timeline Summary.md`
- Supporting character references: relevant files in `docs/character_dossiers/`
- Opening-specific edit guidance: `OPENING_EDIT_AGENT.md`
- Non-authoritative LaTeX artifact: `Legacy/latex_artifacts/main_artifact_snapshot.tex`

## Opening Chapter Source Selection
- Use `docs/canonical_md/Chapter 1 – The Return.md` as the active merged opening chapter.
- Treat `Legacy/canonical_md_superseded/opening_chapters_pre_merge_2026-07-02/` as the archive for the former standalone Chapters 1-3.
- Treat `Legacy/canonical_md_superseded/Chapter 1 – Scene 1- The Return.md` as an older superseded composite snapshot.
- Do not edit superseded snapshots unless the task is explicitly to reconcile or restore archived material into a new canonical form.
- Treat chapter filenames as chapter titles; active chapter markdown files should begin directly with prose rather than duplicating the title as an inline heading or plain first line.
- Keep chapter prose as blank-line-separated Markdown paragraphs so Obsidian renders each paragraph as its own block.

## Book 1 Boundary

Current working baseline, approved 2026-10-09: use the merged Chapter 1 and Chapters 4–30, plus the three selected appendices. The Chapter 15 stopping point below describes the historical release/graphic-novel v1 boundary and must not truncate the current beta manuscript. See `beta_readers/README.md` for the verified edition, source checkpoint, and superseded exports. The expanded Gor appendix retains its developmental status and disclosed differences from Chapter 15.

- Author-confirmed titles, 2026-09-26: Book 1 is **Hive: Earth**; Book 2 is **Hive: Dyson**.
- Author decision, 2026-09-26: prose Book 1 ends at the same narrative stopping point as graphic-novel Volume One: the end of `Chapter 15 – The Night the Oath Broke.md`, including Gor's rain epilogue and the final sentence, "The rain took his footsteps."
- Book 1 comprises the active merged Chapter 1 followed by Chapters 4–15: thirteen canonical source files. Do not restore archived Chapters 2–3 or renumber source files to assemble this book.
- Chapter 16, `Dead Relay`, and subsequent chapters fall outside Book 1. Their source files remain in place; this boundary does not decide the next book's ending.
- Author-approved web release, 2026-09-26: publish the complete Book 1 as an exploratory draft, subject to revision, with all rights reserved and free website reading only. No download edition or republication/adaptation permission is granted. See `docs/website_publication_plan.md` for implementation and release status.
- Author-directed beta integration, 2026-10-06: for the current beta-draft revision, integrate the post-Gor / biomechanic / handshake arc into Book 1 through the new ending in Chapter 30. This supersedes the 2026-09-26 Book 1 boundary for this working draft only; it does not authorize changing the existing public web release. Keep the merged Chapter 1 and source-file numbering; archived Chapters 2–3 are superseded material already represented in the merged opening.

## Per-Chapter Process
1. Read `AGENTS.md`.
2. Read `docs/lore_registry.md`.
3. Read `docs/canonical_md/Current Timeline Summary.md`.
4. Read `OPENING_EDIT_AGENT.md` for opening-chapter stabilization passes.
5. Read the target chapter in `docs/canonical_md/`.
6. Read any relevant character or world reference files, including `docs/character_dossiers/`, if the scene depends on them.
7. Apply surgical prose edits that improve humanity, clarity, and specificity without changing lore or intent.
8. Update `docs/lore_registry.md` first if a proper noun or lore detail must change.
9. If an edit would break continuity, stop and issue a `Continuity Alert` instead of forcing the change.
10. Leave archived LaTeX artifacts alone unless the task is specifically to sync or export the canonical markdown back into LaTeX.

## Archived LaTeX Status
`Legacy/latex_artifacts/main_artifact_snapshot.tex` is currently a manuscript artifact, not the active prose source.

For now:
- keep it as a reference or compilation snapshot if it is still useful
- do not use it as the editing baseline
- do not assume it matches the current state of `docs/canonical_md/`
- treat any future markdown-to-LaTeX reconciliation as a separate sync pass

## Practical Rule
If the same chapter exists in both `docs/canonical_md/` and an archived LaTeX artifact, edit the markdown chapter unless the task explicitly says to update LaTeX.

## Reader Package

Requests for a package, share copy, or beta-reader edition mean one combined PDF with the agreed Hive artwork as its front cover, selected author's note/foreword, complete manuscript, and appendices. Follow `docs/reader_package/README.md` and the pinned source and cover selection in `docs/reader_package/package.json`. Preserve previous dated editions and retain any developmental appendix notices. The current package selects the author-approved v0.2 working manuscript in `docs/canonical_md/`. The original style-trial and earlier packages remain frozen comparison editions.

## Copy Editor

For mechanical and consistency review, use `COPY_EDITOR_AGENT.md` and `docs/copy_editor/README.md`. The author's first-pass choice is proposed corrections for review. Pin the selected package inputs, prepare a versioned coverage ledger, and record exact proposals and author queries. A prepared run is not a completed review. Apply accepted corrections only after the author's instruction, preserving completed manuscript and package versions.
