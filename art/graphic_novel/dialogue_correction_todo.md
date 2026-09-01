# Graphic Novel Dialogue Correction Todo

Purpose: audit and correct visible dialogue, captions, labels, and sound text on the initial graphic-novel pages one page at a time.

This is an art-production tracker, not canon. The exact wording and scene order must come from `docs/canonical_md/`. Do not use text already present in a generated image as the source of truth.

## Status Key

- `Pending`: page has not been compared against the manuscript.
- `Awaiting Lettering`: accepted art-only page has an exact manuscript lettering map but no visible text yet.
- `Auditing`: every visible text element is being transcribed and checked.
- `Correction Rendered`: a non-destructive corrected version exists and needs review.
- `Needs Rerender`: a targeted text edit could not preserve layout, art, or speaker order.
- `Approved`: wording, attribution, placement, and art continuity have passed review.

## One-Page Workflow

1. Read the exact scene in `docs/canonical_md/`.
2. Inspect the full-resolution page and transcribe every visible text element in reading order.
3. Create a correction spec containing panel location, current text, required manuscript text, speaker or caption type, and required action.
4. Check wording, punctuation, capitalization, apostrophes, dashes, speaker attribution, chronology, balloon tails, and caption placement.
5. Correct one page only. Preserve all accepted artwork, panel geometry, character identity, lighting, and gutters.
6. Save the first correction non-destructively as `page-##-dialogue-v2.png`. Keep the current page until the corrected version is approved.
7. Compare the corrected page against both the manuscript and the original art at full resolution.
8. Mark the page `Approved` only when no extra, missing, paraphrased, misspelled, misattributed, or chronologically displaced text remains.
9. After approval, update `asset_registry.md` and retain the superseded page as a clearly named production draft.

If a text-only edit changes faces, hands, clothing, props, staging, or panel layout, reject it and mark the page `Needs Rerender`.

## Correction Queue

Work strictly from top to bottom unless a specific page is requested.

| Order | Status | Source | Page | Audit Notes |
|---:|---|---|---|---|
| 1 | Pending | `docs/canonical_md/Chapter 1 – The Return.md` | `chapter_01_wakeup/page-01.png` | Opening wake-up dialogue/caption audit. |
| 2 | Pending | `docs/canonical_md/Chapter 1 – The Return.md` | `chapter_01_wakeup/page-02.png` | Confrontation and translation-interface audit. |
| 3 | Pending | `docs/canonical_md/Chapter 1 – The Return.md` | `chapter_01_wakeup/page-03.png` | Earth/Spindle reveal, question, reassurance, and caption audit. |
| 4 | Pending | `docs/canonical_md/Chapter 1 – The Return.md` | `scenes/chapter_01_launch_anomaly/page-01.png` | Launch-memory dialogue, labels, and caption audit. |
| 5 | Pending | `docs/canonical_md/Chapter 1 – The Return.md` | `scenes/chapter_01_launch_anomaly/page-02.png` | AI warning, anomaly phrasing, and return-transition audit. |
| 6 | Pending | `docs/canonical_md/Chapter 4 – The Walk.md` | `scenes/chapter_04_the_walk/page-01.png` | Attendant dialogue and generated narrative captions. |
| 7 | Pending | `docs/canonical_md/Chapter 5 – The Opening Move.md` | `scenes/chapter_05_opening_move/page-01.png` | Korin/Cassian wording, speaker tails, and exchange order. |
| 8 | Pending | `docs/canonical_md/Chapter 5 – The Opening Move.md` | `scenes/chapter_05_opening_move/page-02.png` | Four-century reveal, assimilation exchange, and memory statement. |
| 9 | Pending | `docs/canonical_md/Chapter 6 – Controlled Variables.md` | `scenes/chapter_06_controlled_variables/page-01.png` | Sequence 7 dialogue and caption/speaker attribution. |
| 10 | Pending | `docs/canonical_md/Chapter 7 – The Seam.md` | `scenes/chapter_07_the_seam/page-01.png` | Escape-slate wording, timer relationship, and captions. |
| 11 | Pending | `docs/canonical_md/Chapter 7 – The Seam.md` | `scenes/chapter_07_the_seam/page-02.png` | Corridor captions and Alyen lockdown dialogue. |
| 12 | Pending | `docs/canonical_md/Chapter 8 – The Drop.md` | `scenes/chapter_08_the_drop/page-01.png` | Fall captions and chronological placement. |
| 13 | Pending | `docs/canonical_md/Chapter 8 – The Drop.md` | `scenes/chapter_08_the_drop/page-02.png` | Drone line, telepathic warning, and omitted/extra captions. |
| 14 | Pending | `docs/canonical_md/Chapter 9 – Fractures in the Core.md` | `scenes/chapter_09_fractures_in_the_core/page-01.png` | Cassian/Thena dialogue, speaker attribution, and omissions. |
| 15 | Pending | `docs/canonical_md/Chapter 10 – Signal to Noise.md` | `scenes/chapter_10_signal_to_noise/page-01.png` | Pre-ambush dialogue wording and chronological placement. |
| 16 | Pending | `docs/canonical_md/Chapter 10 – Signal to Noise.md` | `scenes/chapter_10_signal_to_noise/page-02.png` | Confirm intentionally silent action page contains no generated text. |
| 17 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_safehouse_recognition/page-01.png` | Chapter page 1; manuscript captions plus one clearly marked adaptation caption. |
| 18 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_dojo/page-01.png` | Chapter page 2; first exchange and shared-grammar caption. |
| 19 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_dojo/page-02.png` | Chapter page 3; rematch, bow, banter, and private oath. |
| 20 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_dojo/page-03.png` | Chapter page 4; late-red-light departure and closing captions. |
| 21 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_augmentation_offer/page-01.png` | Chapter page 5; offer, oath, refusal, and functionary exchange. |
| 22 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_augmentation_offer/page-02.png` | Chapter page 6; master approval, review-to-action, and safehouse transition. |
| 23 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_fall/page-01.png` | Chapter page 7; ridge, return, controlled purge, and dojo reveal. |
| 24 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_fall/page-02.png` | Chapter page 8; Gor/master confrontation through the span exchange. |
| 25 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_almelah_fall/page-03.png` | Chapter page 9; yield, final judgment, non-graphic cutaway, and oath inversion. |
| 26 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_safehouse_conclusion/page-01.png` | Chapter page 10; identification and clean-win explanation. |
| 27 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_safehouse_conclusion/page-02.png` | Chapter page 11; includes the two clearly marked adaptation dialogue lines. |
| 28 | Awaiting Lettering | `docs/canonical_md/Chapter 15 – The Night the Oath Broke.md` | `scenes/chapter_15_gor_in_rain/page-01.png` | Chapter page 12; cryo rhythm, harsher rule, and final spoken lines. |
| 29 | Awaiting Lettering | `docs/canonical_md/Chapter 13 – The Soft Edge.md` | `scenes/chapter_13_soft_edge/page-01.png` | Chapter page 1; real-rain stillness, warning footfalls, and first impact. |
| 30 | Awaiting Lettering | `docs/canonical_md/Chapter 13 – The Soft Edge.md` | `scenes/chapter_13_soft_edge/page-02.png` | Chapter page 2; Gor's recognition, controlled violence, and challenge. |
| 31 | Awaiting Lettering | `docs/canonical_md/Chapter 13 – The Soft Edge.md` | `scenes/chapter_13_soft_edge/page-03.png` | Chapter page 3; tactical escape, patient pursuit, and closing hunt captions. |
| 32 | Awaiting Lettering | `docs/canonical_md/Chapter 14 – The Broken Clinic.md` | `scenes/chapter_14_broken_clinic/page-01.png` | Chapter page 1; clinic approach, guard evaluation, and price exchange. |
| 33 | Awaiting Lettering | `docs/canonical_md/Chapter 14 – The Broken Clinic.md` | `scenes/chapter_14_broken_clinic/page-02.png` | Chapter page 2; treatment, boundary-setting, and exit. |
| 34 | Awaiting Lettering | `docs/canonical_md/Chapter 14 – The Broken Clinic.md` | `scenes/chapter_14_broken_clinic/page-03.png` | Chapter page 3; clinic analysis, Gor's deliberate distance, and absence captions. |
| 35 | Awaiting Lettering | `docs/canonical_md/Chapter 22 – The Runoff Cut.md` | `scenes/chapter_22_runoff_cut/page-01.png` | Chapter page 1; conditional escort, Voss mural, and canonical environmental lettering. |
| 36 | Awaiting Lettering | `docs/canonical_md/Chapter 22 – The Runoff Cut.md` | `scenes/chapter_22_runoff_cut/page-02.png` | Chapter page 2; route cloth, three-cut comparison, and dark-lantern stop. |
| 37 | Awaiting Lettering | `docs/canonical_md/Chapter 22 – The Runoff Cut.md` | `scenes/chapter_22_runoff_cut/page-03.png` | Chapter page 3; runoff reveal, diagonal addition, and invitation. |

## Acceptance Gate

A page is not dialogue-approved until all answers are yes:

- Is every word drawn from the correct manuscript scene?
- Is punctuation preserved or changed only for necessary balloon legibility without changing meaning?
- Is each line assigned to the correct speaker or caption type?
- Does the page preserve the manuscript's event and dialogue order?
- Are there no invented captions, labels, sound effects, or explanatory summaries?
- Is all lettering readable at full page size?
- Did the correction preserve the accepted art and continuity references?

## Production Hold

Do not treat Chapters 1 and 4-10 as dialogue-final, export them for publication, or assemble them into a final book until every row above is `Approved`.
