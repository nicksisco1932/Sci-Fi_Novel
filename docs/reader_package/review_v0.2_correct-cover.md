# Reader Package Verification — correct cover and author credit

Current PDF: `beta_readers/packages/v0.2_2026-10-08_correct-cover/Hive_Earth_Beta_Reader_Package.pdf`.

PDF SHA-256: `2be1d9559f12fc170387b5282842f2cad595f7e63c7207a462e61d9e57592849`.

The author explicitly identified https://chatgpt.com/s/m_6ac879705640819197192fd67afe9899 as the correct book cover. The original 1024-by-1536 PNG was retrieved through the browser's media download and preserved as `beta_readers/assets/hive-book-cover.png`. SHA-256: `66f4756b2305afd1c057fac6f944c3b5846b7403933e16f91dc65c8221ad56f8`. This replaces the earlier city render as the default cover; earlier editions remain preserved.

The author credit is **Nicholas J. Sisco** on the artwork, title page, PDF metadata, combined Markdown, configuration, and manifest. The cover is displayed whole at its original aspect ratio without cropping, added lettering, or regeneration.

## Checks and review

- All pinned manuscript, supporting-source, and artwork hashes validated before package generation.
- 213 pages, one foreword, 28 chapters, and three appendices. All 32 source sections pass the extracted-token fidelity checks.
- Source section spans and text checks are unchanged from the previous illustrated edition.
- All 211 pages after the title page are pixel-identical to the preceding illustrated edition. The cover and author credit are the only reader-facing changes.
- Inspected rendered cover and title page at full size: artwork and embedded lettering remain intact; corrected credit is legible, with no overlap or clipping.
- Verified author metadata and title-page extraction explicitly.
- Earlier illustrated package still matches its recorded PDF hash.
- `git diff --check` and whitespace checks on the new package and Copy Editor files pass. The inherited v0.1 ledger's two Markdown hard-break spaces remain preserved, as documented in the preceding review record.

The Copy Editor role, style sheet, and preparation tool are saved separately. Its `v0.2_first-review` run has 32 pending sections with validated source and guidance hashes; no copyedit findings have been assessed yet.

No manuscript prose, canon terms, or supporting snapshots were changed. No continuity conflict was resolved, no sync was performed, and no commit or push was created.
