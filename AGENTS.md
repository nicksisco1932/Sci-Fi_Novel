# AGENTS.md - Sci-Fi Novel Refinement Rules

## Objective
Improve clarity, pacing, and voice while preserving plot, lore, and character intent.

## Current Draft Workflow
- Treat `docs/canonical_md/` as the active source for chapter-by-chapter narrative refinement.
- At this stage, the job is to make each chapter read more human, expand selectively where clarity, tension, or character depth need it, and sharpen concrete detail while preserving canon and continuity.
- Use the continuity files and relevant character material before changing narrative content.
- Treat `main.tex` as an artifact snapshot, not the working source of truth.
- Do not edit `main.tex` unless explicitly asked to synchronize or export the canonical markdown drafts into LaTeX.
- If `main.tex` and `docs/canonical_md/` differ, edit `docs/canonical_md/` and note that LaTeX sync is pending.

## Non-Negotiables
- Do not change proper nouns, timeline facts, or established lore unless explicitly asked.
- Do not alter character motivations or thematic intent.
- Keep tone: precise, restrained, high-stakes. Avoid melodrama and filler.
- Prefer surgical edits over rewrites.
- Preserve paragraph breaks unless they are demonstrably harming flow.
- Never add new plot points or expand lore unless explicitly requested.

## Lore and Continuity Integrity

### Required pre-edit reading (for narrative/prose edits)
- Before editing narrative text, read `AGENTS.md`.
- Read the continuity registry file: `docs/lore_registry.md`.
- Read the timeline summary file: `docs/canonical_md/Current Timeline Summary.md`.
- If a required file is missing, search likely candidates (`*continuity*`, `*registry*`, `*timeline*`, `*Timeline Summary*`).
- If the search yields multiple plausible candidates, list the candidates and STOP with a `% TODO:` in output; do not guess.

### Continuity deviation alerts (fail-safe behavior)
- If a proposed edit conflicts with established continuity (proper nouns, timeline facts, event ordering, character motivations, technology limits), DO NOT apply the edit.
- Instead, output a `Continuity Alert` with:
- `File`
- `Location` (line or section)
- `What would be changed`
- `Why it conflicts`
- `Suggested resolution path`

## LaTeX Constraints
- Do not alter document structure (`\chapter`, `\section`, `\input`, etc.).
- Do not reformat indentation or whitespace unless necessary for clarity.
- Do not modify preamble or compilation settings.
- Preserve custom macros and commands exactly as written.
- Do not change quotation style, dashes, or typographic conventions unless incorrect.

## Output Requirements
- Always provide a short summary of changes.
- Always produce a unified diff when edits are made.
- When uncertain, insert a `% TODO:` comment instead of guessing.
- Flag continuity issues separately from prose edits.
- If no edits are made, explicitly state: "No manuscript changes recommended."

## House Style
- Tight verbs, minimal adverbs.
- Remove redundancy and weak qualifiers.
- Avoid filter words (he felt, she noticed) unless intentional.
- Dialogue tags default to "said" or omitted.
- Trust implication over explanation.

## Why This Version Is Better
- It prevents Codex from "cleaning up" LaTeX formatting.
- It prevents macro corruption.
- It forces explicit no-edit acknowledgment.
- It enforces structural discipline.

Before editing any proper noun or lore detail, consult lore_registry.md; if absent, create/update it first.



