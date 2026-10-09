# Accepted working baseline

**Author:** Nicholas J. Sisco. **Decision date:** October 9, 2026.

The author selected the current v0.2 beta manuscript as the most polished version and the starting point for all further development. The active working manuscript is **`docs/canonical_md/`**, with the merged Chapter 1 followed by Chapters 4–30. All 28 chapter files were copied byte-for-byte from the selected beta inputs. No new prose was composed during promotion.

## Records and recovery

- `working_baseline.json` identifies the accepted version, source locations, chapter order, selected package, and approval scope.
- `manuscript_baselines/2026-10-09_v0.2/manifest.json` and `chapters.sha256` freeze the acceptance record and all 28 accepted chapter hashes.
- `manuscript_baselines/2026-10-09_pre_promotion/` preserves the 28 previous working chapter files, timeline, foreword, and three appendices, with a 33-file hash manifest.
- GitHub's preceding `main` checkpoint was `26a569044fc6abd2054f9b6cb481c77aeab56296`. The promotion branch includes that history, rather than replacing it.
- `developmental/manuscript_style_tests/v0.2/` remains the untouched comparison edition. The baseline, v0.1, guides, ledgers, and earlier packages are also retained.

The approved reading edition was `beta_readers/packages/v0.2_2026-10-08_correct-cover/`. Its PDF SHA-256 is `2be1d9559f12fc170387b5282842f2cad595f7e63c7207a462e61d9e57592849`. The working-baseline package is `beta_readers/packages/v0.2_working_2026-10-09/`, with the same text and correct HIVE cover; its title-page date identifies the promotion edition.

## Future work

Edit the canonical working files when the author requests changes. Preserve the accepted voice, plot, ambiguity, dialogue meaning, and reveal timing. Frozen chapters, review records, and dated packages remain historical evidence; authorized future working edits do not need to match the initial accepted hashes forever. New exports must pin the new input bytes and use new dated output directories. Do not silently regenerate an older package with newer prose.

The Copy Editor remains in proposed-corrections mode. Its current canonical review is prepared under `docs/copy_editor/runs/v0.2_working_first-review/`; no copyedit has been performed yet. The earlier experimental review setup remains historical.

## Supporting text and scope

The selected author's foreword is `docs/developmental/Author’s Foreword – What the Record Loses.md`; the three selected appendices are in `docs/appendices/`. Their text matches the accepted package's supporting snapshots. The foreword's editorial status line is still omitted only in reader presentation.

Gor's appendix retains its explicit developmental notice and disclosed differences from Chapter 15. Accepting the manuscript as the working baseline does not resolve those conflicts or establish its conflicting history as canon. The storyline and established terminology otherwise pass through unchanged from the selected beta.

The existing public website and graphic-novel editions keep their historical release boundaries. Obsidian and archived LaTeX are separate sync/export targets and were not updated by this promotion. The main checkout and this Codex worktree share Git history but remain distinct working directories.
