# Reader Package

When the author asks for a **package**, **share copy**, or **beta-reader edition**, build one combined PDF containing:

1. The agreed Hive artwork on the front cover, followed by a title page and linked contents.
2. The selected author's note or foreword.
3. The complete selected manuscript in its established chapter order.
4. The appendices after the manuscript.

The current selection is the v0.2 style-trial manuscript, including the author's latest Chapter 1 transition addition, the foreword **What the Record Loses**, and the Figures of the Turning Time, Voss Conquest, and Gor appendices. This package selection does not promote the experimental manuscript or developmental appendix to canonical status.

## Share file

The current shareable edition is:

`beta_readers/packages/v0.2_2026-10-08_correct-cover/Hive_Earth_Beta_Reader_Package.pdf`

A combined Markdown copy and `package_manifest.json` accompany the PDF for reproducibility. The PDF alone contains the entire reader edition; recipients do not need the source files or manifest.

## Agreed cover

Use `beta_readers/assets/hive-book-cover.png` as the front cover for future packages. The author explicitly identified the artwork at https://chatgpt.com/s/m_6ac879705640819197192fd67afe9899 as the correct book cover. It is the dark HIVE design with golden light and the embedded **Nicholas J. Sisco** credit.

SHA-256: `66f4756b2305afd1c057fac6f944c3b5846b7403933e16f91dc65c8221ad56f8`. The retrieved original is 1024 by 1536 pixels. Keep the complete image at its original aspect ratio, without cropping, regeneration, or additional text over the artwork. Title and edition information remain on the following page. `package.json` pins the image path, hash, and share-link provenance; the builder validates it before writing outputs.

This choice supersedes the earlier city render `beta_readers/assets/hive-earth-cover.jpg`. The earlier packages and artwork remain preserved for recovery. The author credit in all new packages and metadata is **Nicholas J. Sisco**. Cover selection does not establish visual lore as canon.

## Build

Run from the repository root using the existing Python runtime:

```powershell
& 'C:/Users/nicks/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' tools/build_reader_package.py
```

`package.json` selects the manuscript folder, chapter order, hash manifest, foreword, appendices, date, and output directory. All input hashes and completeness checks run before output writes. The PDF uses Georgia at 10.8 points with 15-point leading on 6-by-9-inch pages. It includes page numbers, linked contents, and bookmarks. Obsidian links display their visible text; Markdown emphasis and scene breaks are rendered for reading.

If the selected inputs and existing artifacts still match their hashes, the command reuses the verified package immediately. Use `--rebuild` only when regeneration of the identical edition is needed. PDFs use deterministic metadata, so identical inputs reproduce the same artifact.

The foreword's editorial development-status line is omitted from the reader presentation. Its full source snapshot remains preserved. The Gor appendix's developmental status and specific unresolved Chapter 15 conflicts remain visible to readers. No prose or lore is rewritten while packaging.

## Future editions

Update the selected source snapshots and SHA-256 values only when an author-approved source changes. Set a new version/date/output directory for changed inputs. The builder refuses to replace an existing edition with different inputs. Earlier packages must remain available. Chapter 16 and other source-preservation requirements still apply to manuscript revisions.

The supporting snapshots were copied from the main checkout; `supporting_sources.json` records their original locations and hashes. Their paths are repository snapshot paths, not Obsidian mirror paths.

Each new edition also saves its exact `package_config.json`. The earlier plain-cover October 8 edition is preserved in `beta_readers/packages/v0.2_2026-10-08/`. To reproduce it, pass its saved configuration using `--config` and `--rebuild`.

After building, verify the text-fidelity results in the manifest and render the PDF for visual review, including all-page contact sheets and full-size cover, contents, changed passage, frontmatter, appendix transitions, and final page. A successful extraction check does not replace visual review.

```powershell
& 'C:/Users/nicks/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' tools/render_reader_package.py
```

Use `--pages 11,12` to include additional changed pages. Renders go to `tmp/pdfs/reader_package/`. The renderer checks the PDF hash, makes contact sheets for all pages, and selects the cover, contents, foreword, opening edit, appendix starts, and final page automatically. Inspect them, record the final PDF hash and review results, then remove only those temporary renders.

## Start here next time

1. Read this workflow and `package.json`; the author credit is Nicholas J. Sisco, the current share format is a single PDF with the agreed Hive artwork as its front cover, and the existing serif design can be reused.
2. Use the selected manuscript version; do not substitute this worktree's canonical chapter set for an explicitly selected experiment. The current experiment has 28 files numbered 1 and 4–30.
3. Locate any newly requested supporting revision using the original-source paths in `supporting_sources.json`. Read and snapshot it with Python's `pathlib` and UTF-8; preserve the bytes and hash them. Non-ASCII filenames can look wrong in Windows console output, so verify bytes and code points before claiming corruption or trying to reconstruct sources from a diff.
4. Choose a new dated output directory when inputs change. Run the existing builder, which validates the pinned sources before writing. Skip reconstruction of earlier manuscript trials.
5. Reuse the package if nothing changed. For a new edition, run the renderer, inspect the new layout and changed passages, record verification, and give the author the PDF link.

This records the successful local workflow. It requires no new models, dependencies, LaTeX export, or Obsidian sync.
