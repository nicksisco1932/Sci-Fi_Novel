# Manuscript Style Trial v0.2 — Analysis

## Scope and method

This experiment compares the frozen baseline, completed v0.1, and v0.2 across Chapter 1 and Chapters 4–30 (28 files). Exact unchanged lines anchor chapter-level alignments; the JSON file records per-chapter anchor counts and sentence-length contours. Paragraph joins/splits and operation labels are manually reviewed in the ledger.

Tokens are Unicode word runs, retaining internal apostrophes and hyphens. Sentence boundaries are approximate at `.`, `!`, and `?`; abbreviations, decimals, ellipses, fragments, and dialogue complicate automatic segmentation. Counts describe structure, not reading speed or sophistication.

## Aggregate structural counts

| Measure | Baseline | v0.1 | v0.2 |
|---|---:|---:|---:|
| Word tokens | 33123 | 33173 | 33193 |
| Paragraphs | 3217 | 3156 | 3163 |
| Approx. sentences | 4851 | 4754 | 4765 |
| Sentences at most 6 tokens | 2880 | 2778 | 2788 |

## What changed between baseline and v0.1

The frozen v0.1 ledger records joins and recasts chiefly in narration: waking perception, recovery, inference chains, environmental scans, and infrastructure description. It also records purposeful retention of tactical beats, interrupted exchanges, countdowns, and interface messages. Previously suitable passages were not treated as evidence that every other passage should be expanded. v0.1’s Chapter 20 recast compressed a spatial inventory, while Chapter 21 compressed the bright-thread clue and added an interpretive phrase.

## Aligned examples

### Chapter 20 — spatial reveal

**Baseline:** “The corridor widened after two turns into a chamber hidden behind the false wall of the buried street. The architecture changed immediately. Not civic fiction anymore. Survival, layered over ruins.”

**v0.1:** The corridor description became one joined paragraph describing the architecture as shifting from civic remnants to survival, then compressed the chamber inventory into a list.

**v0.2:** “After two turns, the corridor widened into a chamber hidden behind the false wall of the buried street. The architecture changed immediately: not civic fiction anymore, but survival layered over ruins. The chamber held…” The remaining list retains the v0.1 detail.

The revision reconnects movement and architecture while restoring the requested distinction and adding no setting detail.

### Chapter 1 — interruption in recovery

**v0.2:** “Darkness. Silence. / Awareness. Extreme darkness. Brief, faint flashes in the distance. / Should I go to it? / Snap. Extreme pain.” The uncertain perception and question break before the existing dislocated-second sentence; “Then again” adds the second interruption before the translation-device hiss.

### Chapter 21 — clue, then inference

**Baseline and v0.1 order:** the runner reports the deepened cut; Cassian sees the bright thread; the group discusses who should notice it; later Cassian states that the hunter left the mark usable “on purpose.” v0.1 preserved that order but compressed the bright-thread observation and added “a deliberate bid for attention.” v0.2 restores the observed detail and short beats while keeping the dialogue at its existing position.

## Rhythm and development model

Sentence contours, approximate length distributions, and paragraph changes are recorded per chapter in `measurements_v0.2.json`. The broad v0.1 pattern is retained in chapters where connected attention was already working; short action, silence, dialogue, and signal beats remain where they carry scene function. v0.2 develops the Chapter 1 recovery interruption, restores the Chapter 20 distinction, and restores the Chapter 21 clue presentation. Chapter 16 remains byte-identical and serves as a profile of connected attention, not a target statistic.

The scene-mode labels are sustained observation, immediate action, contested exchange, recollection/recovery, and signal/countdown. They describe changing demands, not prescribed rhythms.

## Editorial dimensions

- **Word choice:** selective precision; no decorative synonym replacement. Chapter 20 restores a phrase with an established contrast.
- **Sentence structure and cadence:** connected syntax for linked movement and perception; short beats retained for actual turns, interruptions, and danger.
- **Paragraph development:** group only details belonging to a shared moment or spatial field; do not turn every detail into a continuous inventory.
- **Operation:** Chapter 1 additive interruption; Chapter 20 recast; Chapter 21 clue-presentation restoration; all other passages reviewed and retained. Narration, dialogue, and interface forms remain distinct.

## Limitations

Automatic alignment cannot infer viewpoint, scene mode, subtext, or editorial intent. Counts can mis-segment punctuation and fragments. Human review is recorded in the chapter ledger; no metric is a quality score.

## Frozen v0.2 principle

**Let related perceptions develop through sentences rather than compressing them into inventories.**

Next action: the author reads v0.2 beside v0.1 and judges whether the prose has gained the desired development.
