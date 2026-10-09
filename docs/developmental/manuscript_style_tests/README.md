# Manuscript Style Experiments

This directory tracks isolated prose experiments. The canonical manuscript remains `docs/canonical_md/`.

## Versions

| Version | Basis | Status |
|---|---|---|
| Source snapshot | Copy of the canonical chapter files at experiment start | Preserved as the comparison baseline |
| v0.1 | Separate working copy evaluated against frozen `style_guide_v0.1.md` | Complete experimental trial; pending author review; non-canon |

## Scope and safeguards

- The experiment covers every active chapter file present at setup. The merged Chapter 1 and Chapters 4–30 are included; superseded Chapters 2–3 are not.
- Chapter 16 is the sole source for style observations in version 0.1. Its full paragraphs provide positive examples; its short beats and fragments are not universal patterns. Other chapters are test material, not additional authorities for expanding the guide.
- Keep the source snapshot unchanged. Make all trial revisions in `v0.1/` and leave `docs/canonical_md/` untouched.
- Preserve plot, canon, character intent, and point of view. This is a prose-style experiment, not permission to add scenes or lore.
- Treat the guide as a hypothesis. A rule may be marked unsuitable for a passage rather than forced where it damages pace, tension, or silence.
- Record per-chapter outcomes in `review_ledger.md`. Record prose edits in `comparison_v0.1.diff` and the dated log below.
- Regenerate the baseline and v0.1 Markdown reading copies and unified diff with `assemble_reading_copies.py`. It verifies chapter order and the source snapshot hashes, displays wikilinks by their visible text, and records the frozen guide hash.
- Record meaningful revisions and author feedback here before creating a later version.

## Revision log

| Date | Version | Change |
|---|---|---|
| 2026-10-08 | Setup | Created the baseline snapshot, v0.1 working copy, and Chapter 16-derived style guide. |
| 2026-10-08 | v0.1 | Refined and froze the guide around connected attention, physical detail, evidence before inference, and varied rhythm. No guide changes during the v0.1 prose pass. |
| 2026-10-08 | v0.1 | Completed a selective style pass across all active chapters; Chapter 16 remains the unchanged control. Per-chapter decisions are in `review_ledger.md`. |

## Author acceptance — 2026-10-09

The author selected the completed v0.2 beta as the most polished version and the working baseline. Its exact chapter bytes now occupy `docs/canonical_md/`. Future development starts with those canonical files. This acceptance supersedes the experiment's pending/non-canon status for the selected manuscript text; it does not authorize modifying the frozen trial directories, infer approval of every experimental editing rule, or reconcile the developmental Gor appendix. See `docs/working_baseline.md`.
