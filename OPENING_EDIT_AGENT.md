# Opening Edit Agent

## Scope
Use this guide for opening-stabilization edits over the active canonical markdown chapters, especially `Chapter 1 – The Return.md` and the early Hive/Lower Grid sequence that follows.

The goal is to absorb the author's Obsidian notes and draft additions into the manuscript without importing rough wording, typos, casual phrasing, or continuity drift.

## Required Reads
Before editing narrative prose, read:
- `AGENTS.md`
- `OPENING_EDIT_AGENT.md`
- `docs/lore_registry.md`
- `docs/canonical_md/Current Timeline Summary.md`
- Relevant files in `docs/character_dossiers/`

## Source Handling
- Treat `docs/canonical_md/` as the canonical source.
- Treat Obsidian `Manuscript/` edits as author intent notes unless the wording already fits the house style.
- Archive Obsidian drafts before overwriting them during sync.
- Do not edit archived snapshots unless explicitly restoring or reconciling material.

## Editorial Rules
- Preserve canon, motivations, event order, proper nouns, and established technology limits.
- Keep the voice precise, restrained, and high-stakes.
- Prefer implication over explanation.
- Keep lore light and embodied in action, setting, or procedural language.
- Remove filter wording unless the filter is the point.
- Remove typos, duplicated words, casual modernisms, and over-explained anatomy or tactics.
- Preserve blank-line-separated paragraphs for Obsidian readability.
- Preserve chapter filenames as titles; do not add inline chapter headings.

## Opening Pass Priorities
- Chapter 1: strengthen Hive Earth and Korin texture without front-loading a lore dump.
- Chapters 4-6: sharpen Cassian's suspicion and Korin/Alyen pressure while keeping their roles distinct.
- Chapter 7: make the escape feel like a calculated risk, not an easy rescue.
- Chapter 8: deepen physical jeopardy and the alien combat memory without turning it into a technical fight manual.
- Chapters 9-11: clarify Thena, the lanes, and neglected Hive sectors without making them a formal resistance.

## Continuity Behavior
- Update `docs/lore_registry.md` before changing a proper noun, timeline fact, faction definition, or technology rule.
- If an author note conflicts with established continuity, do not import it. Mention it in the edit summary as a continuity concern.
- If uncertain, leave a `% TODO:` note rather than guessing.

## Output Expectations
Every implementation pass should report:
- Changed files
- Whether the continuity registry changed
- Vault sync status
- Verification performed
- A short unified diff excerpt
