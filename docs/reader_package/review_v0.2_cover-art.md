# Reader Package Verification — v0.2 with agreed cover

Edition: October 8, 2026, cover-art revision. PDF: `beta_readers/packages/v0.2_2026-10-08_cover-art/Hive_Earth_Beta_Reader_Package.pdf`.

PDF SHA-256: `204f67fa8c3dde01bc4948474379448fc712c7f561dfcdf2deb28a4301d54cd4`.

## Cover provenance and presentation

The front cover uses the author's previously selected Hive render, preserved byte-for-byte from `C:/Users/nicks/.codex/worktrees/a83b/Sci-Fi_Novel/beta_readers/assets/hive-earth-cover.jpg`. The earlier edition manifest `beta_readers/editions/2026-10-07-v2.json` in that worktree pins the same SHA-256: `d213517710ada706680a5eac4c116d88367915b7f4be6ec19b26bfdade71492e`.

The selection was recovered from **Review AI Artifact Hunter (3)** (`01a11467-e3a1-7532-9145-270a9aef970f`), where the author requested the praised Hive image as the book cover. The author's current request confirms its reuse for this package. The image is displayed uncropped at its original aspect ratio on page 1, with title and edition information on page 2. No artwork was regenerated or edited.

## Completeness and fidelity

- 213 pages; 32 source sections: one foreword, 28 chapters, three appendices.
- All manuscript, supporting-snapshot, and cover hashes validated before writing outputs.
- Every source section passed the existing extracted-token fidelity check.
- Combined Markdown is byte-identical to the preceding 212-page package.
- The source provenance is identical, with one additional cover asset.
- Every source section starts and ends exactly one page later. The Chapter 1 addition is on page 12; the Gor developmental notice is on page 200.
- All 209 content pages, from the foreword through the final appendix, were rendered and compared with the preceding edition: pixel-identical above the footer. Footer page numbers increased by one.
- The preceding PDF still matches its recorded hash. Its saved `package_config.json` matches its original configuration hash, allowing later reproduction.
- `git diff --check` passes. All new package, configuration, workflow, and tool text files pass the trailing-whitespace scan. A scan of all 122 untracked text files found only two inherited Markdown hard-break spaces in the preserved v0.1 `review_ledger.md` (lines 3–4); that completed-version record was retained unchanged.
- A second builder invocation validates input and artifact hashes and reuses the package successfully.

## Visual review

Inspected the new cover and title page at full size and the opening and final contact sheets. The whole artwork remains visible, with no overlaid text or cropping. The title page has no repeated running header. Contents and appendix transitions remain consistent. The previous edition's full visual review remains applicable to the identical content-page layouts; the render comparison above verifies that relationship.

## Saved workflow and source status

The pinned cover and default output path are recorded in `package.json`; `README.md`, `SHARE_PACKAGE.md`, and the project instructions identify this as the current package. The builder validates cover hashes before output writes and saves each new edition's exact configuration. The renderer selects the new package automatically.

No manuscript prose, canon terms, or supporting-source text changed. Existing developmental notices remain visible. No Obsidian sync, LaTeX export, commit, or push was performed.
