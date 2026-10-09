# Editorial Workflow

## Current Stage
The active manuscript pass is happening chapter by chapter in `docs/canonical_md/`.

At this stage, the editorial work is to:
- make the prose feel more human
- expand selectively where clarity, tension, pacing, or character depth need it
- sharpen concrete sensory and behavioral detail
- preserve canon, continuity, and character intent

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

Requests for a package, share copy, or beta-reader edition mean one combined PDF with the agreed Hive artwork as its front cover, selected author's note/foreword, complete manuscript, and appendices. Follow `docs/reader_package/README.md` and the pinned source and cover selection in `docs/reader_package/package.json`. Preserve previous dated editions and retain any developmental appendix notices. The current package uses the author-selected v0.2 style-trial manuscript; it does not replace the canonical source.

## Copy Editor

For mechanical and consistency review, use `COPY_EDITOR_AGENT.md` and `docs/copy_editor/README.md`. The author's first-pass choice is proposed corrections for review. Pin the selected package inputs, prepare a versioned coverage ledger, and record exact proposals and author queries. A prepared run is not a completed review. Apply accepted corrections only after the author's instruction, preserving completed manuscript and package versions.
