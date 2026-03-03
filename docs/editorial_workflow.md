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
- Supporting character references: relevant files in `docs/canonical_md/`
- Non-authoritative artifact: `main.tex`

## Per-Chapter Process
1. Read `AGENTS.md`.
2. Read `docs/lore_registry.md`.
3. Read `docs/canonical_md/Current Timeline Summary.md`.
4. Read the target chapter in `docs/canonical_md/`.
5. Read any relevant character or world reference files if the scene depends on them.
6. Apply surgical prose edits that improve humanity, clarity, and specificity without changing lore or intent.
7. Update `docs/lore_registry.md` first if a proper noun or lore detail must change.
8. If an edit would break continuity, stop and issue a `Continuity Alert` instead of forcing the change.
9. Leave `main.tex` alone unless the task is specifically to sync or export the canonical markdown back into LaTeX.

## `main.tex` Status
`main.tex` is currently a manuscript artifact, not the active prose source.

For now:
- keep it as a reference or compilation snapshot if it is still useful
- do not use it as the editing baseline
- do not assume it matches the current state of `docs/canonical_md/`
- treat any future markdown-to-LaTeX reconciliation as a separate sync pass

## Practical Rule
If the same chapter exists in both `docs/canonical_md/` and `main.tex`, edit the markdown chapter unless the task explicitly says to update LaTeX.

