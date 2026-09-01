# Cassian Rho: The Return - Volume One Proof

This directory contains the complete 48-page visual proof of concept ending after Chapter 15.

## Deliverables

- `cassian-rho-the-return-proof.pdf`: 6x9-inch, 48-page digital review PDF.
- `sequence/`: ordered full-resolution 1024x1536 PNG sequence.
- `manifest.md`: page-by-page source map.
- `contact-sheet-48-pages.png`: full visual-sequence review sheet.
- `pdf-render-check-contact-sheet.png`: contact sheet made from the rendered PDF, not the source PNGs.
- `style-review.md`: cross-volume visual-language review.
- `source-hashes-before.sha256`: accepted-source integrity baseline.
- `build_proof.py`: deterministic assembly script.

## Status

The visual sequence is complete and locked for proof review. It is not dialogue-final or publication-ready.

The first 16 pages in `art/graphic_novel/dialogue_correction_todo.md` retain generated lettering and must pass the established one-page correction workflow. Chapters 13-15 and the new Chapter 1, 11, and 12 pages remain art-only masters with controlled lettering specifications. The selected Korin meditation coda has a separate adaptation-only lettering specification.

No source artwork is overwritten during proof assembly. Files in `sequence/` are derived copies.

## Rebuild

Run with the workspace Python runtime:

```powershell
& 'C:\Users\nicks\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'art/graphic_novel/proofs/volume_01_the_return/build_proof.py'
```

The builder recreates the ordered sequence, manifest, review PDF, and contact sheet. It does not replace the initial source-hash baseline.
