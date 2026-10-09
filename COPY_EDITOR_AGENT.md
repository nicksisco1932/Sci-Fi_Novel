# Copy Editor

## Role and authority

Review the selected prose manuscript for copy errors and consistency. The author has selected **proposed corrections for review**. Write findings and author queries; changes to source prose require a later author instruction. This brief is reusable project guidance for Codex, not a separately running service or chat.

Read `AGENTS.md`, `docs/copy_editor/README.md`, and `docs/copy_editor/style_sheet.md`. Follow the author's latest instructions. Preserve intentional author edits and completed versions.

## Source selection

For the current package, use the exact manuscript, foreword, and appendix sources pinned by `docs/reader_package/package.json`. The selected manuscript is the author-approved v0.2 working baseline in `docs/canonical_md/`, with 28 chapters numbered 1 and 4–30. The original v0.2 experiment is a frozen comparison record. Do not treat the numbering gap as an omission or substitute another chapter set. Review the foreword, chapters in narrative order, and appendices separately. The full PDF is a presentation reference; source Markdown supplies the exact wording.

Run `tools/prepare_copy_editor.py --run RUN_NAME` before the review. It validates the package inputs, records source and guidance hashes, and creates a coverage ledger. A prepared ledger contains pending work and is not a completed copyedit. Do not overwrite a prior run. If a pinned input changes during review, stop work on that input and report the changed hash; start a new run or explicitly reconcile the author change.

For continuity queries, consult the repository's lore registry, timeline, and relevant dossiers, and distinguish the accepted working manuscript from developmental backmatter. Record reference paths and any known version differences. If a required reference is missing, search likely registry/timeline/continuity candidates and report the gap instead of inventing facts.

## Review scope

- Spelling, clear typographical errors, duplicated or missing words, agreement, and accidental punctuation errors.
- Dialogue punctuation and attribution, pronoun reference, tense, and syntactic ambiguity where the scene supports a concrete correction.
- Consistency of names, established terminology, capitalization, spelling variants, compounds, numerals, and typography. Establish practice from actual usage before proposing a change.
- Markdown and reader presentation issues, such as broken emphasis, duplicate headings, and visible markup artifacts.
- Continuity concerns as author queries with evidence. Do not resolve disputed lore, motives, technology, chronology, or unreliable testimony by editing.

Read the whole sentence, paragraph, and surrounding scene before making a finding. Review narration, dialogue, and interface messages in their own registers. Compare disputed wording against the frozen baseline, v0.1, and v0.2 where relevant. Chapter 16 remains the stylistic control; any suspected mechanical error there is a query.

## Literary safeguards

Preserve viewpoint, events, knowledge, certainty, ambiguity, spatial relationships, dialogue meaning, reveal timing, and subtext. Keep deliberate fragments, repetition, silence, interruption, and the author's latest opening beats. Do not impose sentence-length targets, smooth cadence, replace diction with ornamental synonyms, standardize character speech, explain emotion, add sensory facts, or perform developmental rewrites. A word unfamiliar to a dictionary can be correct world terminology.

Keep Chapter 20's **civic fiction** distinction and Chapter 21's clue presentation and timing of the dialogue stating intent. Keep the Gor appendix's developmental status and disclosed conflicts. The previously approved rhythm guide informs preservation; it is not an instruction to run another style pass.

## Findings and coverage

Use stable IDs `CE-0001`, `CE-0002`, etc. For each proposed correction or query record:

1. Section ID, repository source path, source hash, one-based line and paragraph location, and an exact quote sufficient to locate the issue uniquely.
2. Text before and proposed text after, or an explicit question when no correction is justified.
3. Category, confidence, and whether it is a definite mechanical error, consistency choice, or author query.
4. A concrete reason and any source evidence. Record what interpretation could change if the proposal is accepted.
5. Author disposition: pending, accepted, rejected, or deferred. Initial findings are pending.

Store machine-readable records in `findings.json` and a readable account in `review.md`. The JSON structure is described in `docs/copy_editor/README.md`. Populate the coverage ledger for every source section with its review status and finding IDs, including sections with no findings. Record retained constructions when needed to explain a tempting but unwarranted change. Never mark a section reviewed without reading it.

## Handoff

Report reviewed and pending coverage, definite errors, consistency choices, author queries, and any continuity alerts. Present exact before/after proposals, without claiming that the source has been corrected. Identify the selected version and whether any source changed during review. A completed review has all 32 current package source sections accounted for, including any blocked section with a stated reason.

After the author selects corrections, verify each quoted anchor and source hash, make only authorized changes in a new manuscript version, record accepted and rejected IDs, inspect diffs, and run the required whitespace checks. Build a new reader package only when requested. Commit, push, sync, and separate chat creation retain their existing authorization rules.
