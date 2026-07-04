# AGENTS.md - Sci-Fi Novel Operating Guide

## Project Type
This repository contains a prose fiction manuscript and supporting worldbuilding documents.

Treat manuscript files as literary source material, not generic text to optimize.

The primary goal is preservation of authorial voice, continuity, narrative texture, and canon stability.

## Source of Truth
The active manuscript source is:

`docs/canonical_md/`

Archived LaTeX, exported files, PDFs, old drafts, and Obsidian copies are not the active source unless explicitly stated.

Obsidian vault files are a mirror/sync target unless a task explicitly says otherwise.

Do not assume that a repo-relative path exists inside the Obsidian vault.

Repo paths and Obsidian paths must be treated as distinct unless verified.

When adding or updating lore references, distinguish between:

* repo source path
* Obsidian mirror path
* Obsidian wikilink, if applicable

If a lore registry entry points to a file, verify that the referenced file exists in the intended location. If the repo file exists but the Obsidian mirror does not, report that as a sync issue rather than silently treating the path as valid.

Treat archived LaTeX files under `Legacy/latex_artifacts/` as artifact snapshots, not the working source of truth.

Do not edit or recreate a LaTeX export unless explicitly asked to synchronize or export the canonical markdown drafts into LaTeX.

If archived LaTeX and `docs/canonical_md/` differ, edit `docs/canonical_md/` and note that LaTeX sync is pending.

## Prime Directive
Do not rewrite manuscript prose unless explicitly asked.

When asked to add, insert, repair, or lightly revise, make the smallest effective change.

Preserve existing paragraphs, cadence, diction, ambiguity, emotional subtext, and character dynamics wherever possible.

A good edit should feel like the author wrote it.

## Manuscript Preservation Rules
1. Prefer additive edits over replacement.
2. Do not rewrite surrounding prose for style unless the task specifically requests a rewrite.
3. Do not "smooth," "polish," "clarify," or "improve" functioning prose unless asked.
4. Do not convert subtext into explanation.
5. Do not summarize a character's emotional state if the scene already implies it.
6. Do not add interpretive sentence fragments that explain the moment.
7. Do not simplify morally ambiguous material into clear conclusions.
8. Do not change character dynamics unless explicitly requested.
9. Do not change terminology, proper nouns, or setting language without checking canon.
10. Do not add exposition where a brief implication will work.
11. Preserve paragraph breaks unless a change is necessary.
12. Preserve line rhythm and silence. Do not fill every pause with explanation.
13. Do not alter character motivations or thematic intent.
14. Prefer surgical edits over rewrites.
15. Never add new plot points or expand lore unless explicitly requested.

## Forbidden AI-Prose Tendencies
Avoid inserting generic dramatic interpretation such as:

* "A revised estimate."
* "There was respect in it. And caution."
* "Something had changed."
* "Not fear. Recognition."
* "He understood then."
* "For the first time, she saw him."
* "The silence said everything."
* "It was not X. It was Y."
* "And that made all the difference."
* "He realized he had underestimated her."
* "She was beginning to understand."
* "The weight of it settled over them."
* "Neither of them said what they both knew."

These patterns often sound generic, overdetermined, or mechanically dramatic. They flatten prose by telling the reader how to interpret the beat.

## Character Interiority Rules
Do not state a character's internal conclusion unless the point of view and scene already support it.

When revising a look, gesture, pause, silence, or shift in attention, preserve ambiguity.

Characters should not become transparent to the narrator unless the manuscript already uses that mode.

Bad:

"The look she gave him had changed.

There was respect in it.

And caution.

A revised estimate."

Better principle:

Keep the beat embodied, specific, and unresolved. Preserve the original line whenever possible. If repair is necessary, make the smallest change that restores tension without explaining the emotion.

Do not insert the example automatically.

## House Style
The manuscript favors:

* restrained intensity
* precise but not sterile prose
* controlled ambiguity
* concrete physical detail
* pressure under the surface
* morally complicated history
* worldbuilding through residue, not exposition
* characters who reveal themselves indirectly
* brief lore references that imply larger systems
* high-stakes scenes without melodramatic summary
* tight verbs and minimal adverbs
* dialogue tags that default to "said" or are omitted

Avoid:

* generic cinematic phrasing
* therapy-speak
* YA-style realization beats
* tidy moral summaries
* excessive sentence fragments
* mechanical dramatic cadence
* exposition dumps
* explaining what a look, silence, or pause "means"
* replacing authorial texture with clean summary
* melodrama and filler
* unnecessary filter words, unless the filter is intentional

## Lore and Canon Rules
Before adding or changing lore, search existing files with `rg`.

Check at minimum:

* `docs/lore_registry.md`
* `docs/canonical_md/Current Timeline Summary.md`
* relevant chapter files in `docs/canonical_md/`
* relevant character dossiers, if they exist
* relevant appendix/backmatter files, if they exist

Do not rename canon terms unless explicitly instructed.

Respect distinctions between:

* geographic/canon setting terms
* local slang
* historical labels
* artistic or memory traditions
* ancient political names
* current active factions

If a term is ancient history, characters should usually treat it as familiar cultural residue, not shocking revelation.

Before editing any proper noun or lore detail, consult `docs/lore_registry.md`; if absent, create or update it first only when the task allows that change.

If canon conflicts arise, stop and report a continuity alert instead of forcing a conflicting edit.

## Current Canon Source Rules
Use `docs/canonical_md/` as the active manuscript source.

Chapter filenames serve as chapter titles unless existing convention shows otherwise.

Do not add inline chapter title headings inside manuscript chapter files unless explicitly requested.

Chapter files should use blank-line-separated paragraphs.

Preserve Obsidian-compatible paragraph formatting.

## Appendix and Backmatter Rules
Appendix material may contain fuller exposition than the manuscript.

Main manuscript references should remain brief unless the task explicitly asks for an exposition scene.

When adding appendix lore:

* distinguish confirmed history from rumor
* keep ancient history feeling old and culturally worn
* avoid forcing current characters to explain background material
* update the lore registry only when requested or when canon requires it
* verify both repo and Obsidian paths if sync is part of the task

## Obsidian Sync Rules
Do not edit Obsidian vault files unless the task explicitly requests Obsidian sync.

When syncing to Obsidian:

* keep repo manuscript and Obsidian manuscript copies identical
* sync lore registry updates to the Obsidian Lore folder
* sync appendix/backmatter files to the appropriate Obsidian location
* if no appropriate Obsidian folder exists, report the issue before inventing a new structure unless the user authorized creation
* add a short workflow sync note only when requested

Do not place repo-relative paths in Obsidian-facing notes unless they are clearly labeled as repo paths.

Prefer Obsidian wikilinks for Obsidian-facing references when the target file exists in the vault.

## Manuscript Editing Workflow
Before editing manuscript prose:

1. Read `AGENTS.md`.
2. Read `docs/lore_registry.md`.
3. Read `docs/canonical_md/Current Timeline Summary.md`.
4. Read relevant character dossiers, if applicable.
5. Identify the exact file and scene.
6. Read enough surrounding text to understand voice and context.
7. Make the smallest change that satisfies the request.
8. Preserve existing paragraph breaks unless there is a clear reason.
9. Avoid changing adjacent prose.
10. Review the diff for unnecessary rewrites.
11. Revert incidental style changes not required by the task.

If a required file is missing, search likely candidates such as `*continuity*`, `*registry*`, `*timeline*`, and `*Timeline Summary*`.

If the search yields multiple plausible candidates, list the candidates and stop with a `% TODO:` in output; do not guess.

## Continuity Alerts
If a proposed edit conflicts with established continuity, do not apply the edit.

Instead, output a `Continuity Alert` with:

* File
* Location, by line or section
* What would be changed
* Why it conflicts
* Suggested resolution path

Continuity conflicts include proper nouns, timeline facts, event ordering, character motivations, technology limits, faction definitions, setting terminology, and established lore.

## Diff Discipline
A manuscript edit is too broad if it:

* rewrites entire paragraphs unnecessarily
* changes the emotional meaning of a scene
* changes the rhythm of dialogue without reason
* replaces concrete prose with interpretive summary
* adds explanation where implication was sufficient
* makes the prose sound more generic
* changes canon terms without need
* edits sync targets when only source files were requested

If a task requires major rewriting, state that clearly in the final report.

When edits are made, include or summarize the relevant unified diff in the final response if requested by the user or existing repo rules.

## LaTeX Constraints
Do not alter LaTeX document structure such as `\chapter`, `\section`, or `\input` unless explicitly requested.

Do not reformat LaTeX indentation or whitespace unless necessary for clarity.

Do not modify preamble or compilation settings unless explicitly requested.

Preserve custom macros and commands exactly as written.

Do not change quotation style, dashes, or typographic conventions unless incorrect.

## Required Checks
After edits, run:

```bash
git diff --check
```

When lore or canon terms are touched, run targeted `rg` checks for the relevant proper nouns and terminology.

For manuscript edits, inspect the diff manually and remove unnecessary rewrites before finalizing.

For source/sync tasks, verify that repo paths and Obsidian paths both exist before claiming they are synced.

## Commit and Push Rules
Commit only when explicitly requested.

Use clear commit messages.

Do not push unless explicitly instructed and authentication is confirmed.

If the user did not ask for a commit, leave changes uncommitted and report that no commit was created.

## Final Response Requirements
After completing a task, report:

* files changed
* summary of edits
* any canon terms added or changed
* checks run
* commit status
* push status
* any continuity alerts or source/sync path issues discovered

Do not claim broader rewriting, cleanup, sync, or validation was performed unless it actually was.
