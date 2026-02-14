# AGENTS.md - Sci-Fi Novel Refinement Rules

## Objective
Improve clarity, pacing, and voice while preserving plot, lore, and character intent.

## Non-Negotiables
- Do not change proper nouns, timeline facts, or established lore unless explicitly asked.
- Do not alter character motivations or thematic intent.
- Keep tone: precise, restrained, high-stakes. Avoid melodrama and filler.
- Prefer surgical edits over rewrites.
- Preserve paragraph breaks unless they are demonstrably harming flow.
- Never add new plot points or expand lore unless explicitly requested.

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