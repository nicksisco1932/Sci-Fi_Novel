# Chapter Diff Audit

## File Map
- `main.tex` (source for extracted chapter blocks)
- `chapters/ch1.tex`
- `chapters/ch2.tex`
- `chapters/ch3.tex`

Extracted ranges in `main.tex`:
- CHAPTER 1: lines 23-57
- CHAPTER 2: lines 58-90
- CHAPTER 3: lines 91-126

## Chapter 1
- Result: **DIVERGENT**
- First mismatch: main.tex:~23 (chapter-block line ~1) vs chapters/ch1.tex:~1
- Diff excerpt (first mismatch window):
```diff
- % ============================================================
- % CHAPTER 1
- % ============================================================
- 
- \chapter{The Return}
- 
- The first thing Cassian heard was the beeping.
- Steady. Mechanical. Familiar. It ticked like a metronome through the static of his mindâ€”too clean, too precise. His body lay somewhere beyond the sound, distant, heavy, but the rhythm called him back.
- Voices murmured. Calm, professional. Not quite his language, but close enough to stir something old in him. Training? Memory?
- A soft hiss. Footsteps.
+ \chapter{The Return}
+ 
+ The first thing Cassian heard was the beeping.
+ 
+ Steady. Mechanical. Familiar. It ticked like a metronome through the static of his mindâ€”too clean, too precise. His body lay somewhere beyond the sound, distant, heavy, but the rhythm called him back.
+ 
+ Voices murmured. Calm, professional. Not quite his language, but close enough to stir something old in him. Training? Memory?
+ 
+ A soft hiss. Footsteps.
+ 
```
- Classification: divergent

## Chapter 2
- Result: **DIVERGENT**
- First mismatch: main.tex:~58 (chapter-block line ~1) vs chapters/ch2.tex:~1
- Diff excerpt (first mismatch window):
```diff
- % ============================================================
- % CHAPTER 2
- % ============================================================
- 
- \chapter{Before the Jump}
- 
- The sky above Earth was still blue back then.
- Cassian sat on the edge of the launch padâ€™s pre-departure station, legs dangling over the polished composite ledge, watching clouds drift over the Pacific Array. Launch towers bristled in the distance like needles against the curve of the Earth. The sun glinted off the ocean, fractured into gold and platinum waves.
- He took a long breath. The air was sharp, sea-salted. Real.
- A technician approached from behind, smiling warmly, retinal calibration lenses hiding her eyes.
+ \chapter{Before the Jump}
+ 
+ The sky above Earth was still blue back then.
+ 
+ Cassian sat at the edge of the launch padâ€™s pre-departure station, watching clouds shift over the Pacific Array. Launch towers bristled like metallic needles against the curvature of the planet.
+ 
+ A technician approached. â€œYouâ€™re cleared for Phase Three. Vitals optimal. Neural mesh stable.â€
+ 
+ He smirked. â€œOnly matters if I come back.â€
+ 
```
- Classification: divergent

## Chapter 3
- Result: **DIVERGENT**
- First mismatch: main.tex:~91 (chapter-block line ~1) vs chapters/ch3.tex:~1
- Diff excerpt (first mismatch window):
```diff
- % ============================================================
- % CHAPTER 3
- % ============================================================
- 
- \chapter{A Flaw in the Pattern}
- 
- Korin Tal did not like anomalies.
- Not because they were dangerousâ€”though some wereâ€”but because they meant something had slipped. A variable unaccounted for. A prediction failed.
- He stood motionless in the atrium of the Central Cognition Sector, eyes fixed on the data pillar. Light streamed down the length of the towerâ€”white, orderlyâ€”until it pulsed red at the base.
- Red wasnâ€™t supposed to happen.
+ \chapter{A Flaw in the Pattern}
+ 
+ Korin Tal did not like anomalies.
+ 
+ Not because they were dangerous, but because they meant something had slippedâ€”an unaccounted variable.
+ 
+ Now one stood recorded before him: a human who should have been dust.
+ 
+ â€œUnscheduled biological signature. Temporal mismatch,â€ the pillar reported.
+ 
```
- Classification: divergent

Phase 1 complete. No files modified during Phase 1.

