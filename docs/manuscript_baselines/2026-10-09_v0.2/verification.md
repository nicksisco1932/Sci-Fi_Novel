# Working-baseline promotion verification

Author decision: October 9, 2026. Selected beta: v0.2, correct HIVE cover, Nicholas J. Sisco credit.

## Source integrity

- GitHub authenticated as the configured author account; fetched `origin/main` at `26a569044fc6abd2054f9b6cb481c77aeab56296` before integrating.
- Preserved local beta work in commit `8d5f1fb`, then integrated that remote parent in commit `7392e39`.
- No pre-existing uncommitted canonical prose changes were present. Existing package and editorial work was preserved.
- All 28 promoted canonical chapter files match the selected v0.2 inputs byte-for-byte and match `chapters.sha256`.
- Compared against the preceding GitHub canonical text: 13 chapters have prose differences; 15 have identical text after accounting for original line endings. The promotion introduces no prose changes beyond those in the selected beta.
- Chapter 16 matches the frozen baseline, v0.1, and v0.2 exactly.
- All frozen baseline/v0.1/v0.2 parent hashes and both frozen guide hashes pass.
- All 33 pre-promotion recovery files pass their hash checks.
- Foreword and three appendix source texts match the selected package snapshots. Gor's developmental notice and disclosed conflicts remain unchanged.
- The timeline's status labels now identify the accepted working baseline; its event descriptions remain unchanged.

## Package verification

Current package: `beta_readers/packages/v0.2_working_2026-10-09/Hive_Earth_Beta_Reader_Package.pdf`.

PDF SHA-256: `7bc924b49a3e329a9fa13dbeaae0ffcada38f0c727aa18463bd1c0adb6bdda20`.

- 213 pages, one foreword, 28 chapters, three appendices.
- All input hashes were checked before writing package output; all 32 source sections pass extracted-token fidelity.
- All five preserved package editions pass their recorded PDF and Markdown hashes.
- All 212 pages outside the title page are pixel-identical to the accepted October 8 beta package. Only the title-page date changes to October 9.
- Inspected the new rendered title page at full size. The correct cover and previously reviewed interior layout are preserved.

## Review and scope

Manually inspected the chapter diff against the prior GitHub canonical text, confirming it reflects the selected beta. Checked chapter order, completeness, exact bytes, title handling, supporting text, and repository whitespace rules. Frozen historical Markdown breaks and unified-diff context/terminal lines use narrowly scoped whitespace attributes. The already-published asset audit's terminal blank line is preserved without rewriting that audit.

The new canonical Copy Editor run is prepared with all 32 sections pending and recorded source/guidance hashes. A copyedit has not been performed. No new canon term or lore explanation was authored during promotion. Existing Gor continuity disclosures remain open; no Obsidian, LaTeX, public-site, or other-checkout sync was performed.
