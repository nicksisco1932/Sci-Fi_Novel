# Surface Age Stack-Field Music

Original seamless ambient music inspired by the approved Surface Age stack-field visual reference. This is adaptation atmosphere, not a new canon location or lore entry.

## Preferred direction: Stack Field: Rainline

`stack-field-rainline-ambient-music-loop.mp3` is the slow ambient-music version. Its arrangement is built around sustained warm synth harmony, rounded bass, widely spaced electric-key tones, and four distant melodic swells. There is no beat, arpeggiator, broadband static, or recorded rain in the primary mix.

- **Length:** 96 seconds
- **Form:** four slowly crossfading harmonic fields
- **Layers:** sustained pad, warm bass, sparse keys, distant line, high pitched haze, stack resonance
- **Source material:** entirely procedural; no samples or borrowed recordings

`generate_slow_ambient_loop.py` deterministically recreates this version. Add `--stems` to export its six musical layers.

## Earlier music study: Stack Field: Afterlight

`stack-field-afterlight-music-loop.mp3` is a more active music study. It uses an audible D-minor/modal chord progression, warm bass, soft keys, a restrained arpeggio, tonal percussion, and a sparse answering melody. Its atmosphere is pitched and harmonic rather than broadband noise.

- **Length:** 80 seconds
- **Tempo:** 48 BPM
- **Form:** eight two-bar harmonic sections, resolving cleanly back to the opening
- **Layers:** pad, bass, keys, arpeggio, soft pulse, horizon melody, tonal air
- **Source material:** entirely procedural; no samples or borrowed recordings

`generate_music_loop.py` deterministically recreates this version. Add `--stems` to export its seven musical layers.

## Earlier atmosphere study: Stack Field: Low Weather

## Sound

- **Length:** 80 seconds
- **Tempo:** 48 BPM, expressed as pressure pulses rather than a conventional beat
- **Center:** D minor / modal, with a slow four-part harmonic drift
- **Layers:** storm mass, structural resonance, machinery pulse, distant signals, muted horizon warmth
- **Source material:** entirely procedural; no samples or borrowed recordings

This earlier mix is an environment-first study built around storm mass and structural noise. It remains here for reference, but `Afterlight` is the active musical direction.

## Files

- `stack-field-low-weather-loop.wav` — lossless stereo master
- `stack-field-low-weather-loop.mp3` — compact listening copy
- `generate_loop.py` — deterministic source; rerunning it recreates the composition

## Regenerate

From the repository root:

```powershell
& "C:\Users\nicks\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" art\music\surface_age_stacks\generate_loop.py
```

Add `--stems` to export the five constituent layers for remixing.

## Visual reference

The approved mood reference remains:

`art/graphic_novel/style_refs/surface-age-stacks-style-reference.png`

The phrase **Surface Age stack field** is an art-production label only, consistent with the graphic-novel asset registry.
