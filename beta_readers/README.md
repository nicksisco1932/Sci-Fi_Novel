# Hive Earth beta release index

## Current reading edition

**2026-10-07 v2** is the corrected private beta edition. Read [the combined PDF](../output/pdf/Hive_Earth_Beta_Reader_2026-10-07-v2.pdf).

The verified reading copy has **166 pages** and 32 navigation bookmarks. Its SHA-256 is `5862984250b5693c357d150a669912df22aff5f8eaefc79a180bd5bd8e2f6cf2`. Beta PDFs have a scoped Git binary attribute so checkout line-ending conversion cannot alter their bytes.

It contains the existing reader note, the complete merged Chapter 1 and Chapters 4–30 (28 chapter files), and these appendices in order:

1. Figures of the Turning Time.
2. The Voss Conquest.
3. Gor of Almelah, including the complete expanded text and its developmental notice.

Chapters 2–3 are superseded opening material already represented in Chapter 1. Elias Verran and the Verran lineage retain their existing manuscript terminology. No separate Verran appendix exists or has been invented.

The Gor appendix discloses unresolved differences from Chapter 15. This edition preserves that disclosure and includes the text for review without reconciling those differences or promoting the appendix to canon.

## Provenance and recovery

- Active branch: `codex/beta-reader-rectification`.
- Manuscript source checkpoint: `c41140b00b9fe348f546ada77a9143413ae5894e`.
- [Edition manifest](editions/2026-10-07-v2.json): ordered source files and hashes, preserved cover, exact output path, reader note, and superseded exports.
- [Verification record](editions/2026-10-07-v2.verification.json): PDF hash, page count, content comparison, navigation, and source-preservation results.
- [Delivery record](editions/2026-10-07-v2.delivery.json): recipient, attachment hash, sent-message ID, and mailbox confirmation after delivery.

The source checkpoint is recoverable through Git. The PDF and its manifest identify the exact reading edition. Working source files may have newer author changes, so do not call a later file authoritative based only on its timestamp. Compare it against the source checkpoint and manifest.

The current Codex worktree is `C:/Users/nicks/.codex/worktrees/a83b/Sci-Fi_Novel`. The main checkout is `C:/Users/nicks/Documents/GitHub/Sci-Fi_Novel`. They are separate working directories. This branch is backed up to the existing GitHub repository; these notes do not claim that the main checkout has been switched, merged, or synchronized.

## Check, build, and verify

The builder locates the repository from its own file. It uses Python, ReportLab, pypdf, and the installed Georgia font family. This machine's bundled runtime already provides the packages; no new environment or dependency installation is required.

From the repository root in PowerShell:

```powershell
& 'C:/Users/nicks/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B beta_readers/build_beta.py check beta_readers/editions/2026-10-07-v2.json
& 'C:/Users/nicks/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B beta_readers/build_beta.py verify beta_readers/editions/2026-10-07-v2.json
```

`check` verifies the complete source inventory and hashes. `verify` checks the existing reading copy against those sources and its output record. On a checkout where the edition has not yet been built, use `build` in place of `verify`. It refuses to overwrite an existing PDF or verification record.

To prepare a later edition, create a new edition manifest with a new dated version and output path, checkpoint the intended sources, then build and verify that edition. Never repurpose the v2 manifest or overwrite a completed reading copy. Preserve source punctuation, emphasis, paragraphs, and scene breaks; Markdown links use their visible display text.

## Superseded package components

These files remain unchanged and are retained for recovery. They are not the complete current reading package.

| Artifact | Why it is superseded |
| --- | --- |
| [October 6 DOCX](Hive_Earth_Beta_Reader_Draft_2026-10-06.docx) | Chapter text matches the verified manuscript, but no appendices are included. |
| [October 6 manuscript PDF](../output/pdf/Hive_Earth_Beta_Reader_Draft_2026-10-06.pdf) | Separate earlier manuscript export; its renderer replaced source dashes. |
| [October 7 supplement PDF](../output/pdf/Hive_Earth_Beta_Reader_Supplement_2026-10-07.pdf) | Contains the two Voss appendices and reader note, but omits the expanded Gor appendix. |

The old temporary renderer is historical export evidence and is not the supported rebuild command. The Chapter 15 public-release and graphic-novel v1 materials remain historical editions; they do not limit the current private beta manuscript.
