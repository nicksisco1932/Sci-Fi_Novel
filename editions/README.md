# Edition lifecycle (no duplicate working manuscripts)

**Working prose lives only in `docs/canonical_md/`**; appendices live in `docs/appendices/`. This directory is for **immutable production editions**, not editable chapters.

- [`beta/`](beta/) — author/beta-reader editions; non-public drafts.
- [`proofs/`](proofs/) — typeset/copyedit proofs pending publication decision.
- [`published/`](published/) — final, expressly released copies.

For future editions use `<stage>/hive-earth/<edition-id>/` with an ordered source manifest, a unique PDF or DOCX, a validation sidecar, and a checkpoint commit. Do not overwrite a released edition, rename its files, or overwrite its manifest.

**Historical exception:** The verified **2026-10-07 v2** beta remains, byte-for-byte, at `output/pdf/Hive_Earth_Beta_Reader_2026-10-07-v2.pdf` with its manifests under `beta_readers/editions/`. We intentionally did not relocate that evidence.

See [source-of-truth protocol](../docs/SOURCE_OF_TRUTH.md). The existing `beta_readers/build_beta.py` produces 28 chapter files and three appendices and now permits new beta PDF destinations under `editions/beta/`. It does not yet include the in-development author's note.
