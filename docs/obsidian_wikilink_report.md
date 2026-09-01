# Obsidian Wikilink Audit Report

Date: 2026-08-31

## Scope and Result

- Source edited: repository canonical Markdown only.
- Documents linked: 20 active chapters in `docs/canonical_md/` and 2 appendices in `docs/appendices/`.
- Total wikilinks inserted: 62.
- Continuity registry updated: No.
- Canon terms added or changed: None.
- Vault sync performed: No.
- Commit or push performed: No.

## Linked Entities and Destinations

| Class | Entity | Destination | Links | Display forms / aliases | Source documents |
|---|---|---|---:|---|---|
| Character | Cassian Rho | `Cassian Rho` | 22 | `Cassian Rho`, `Cassian` | All 20 active chapters; both appendices |
| Character | Korin Tal | `Korin Tal` | 5 | `Korin Tal`, `Korin` | Chapters 1, 5, 6, and 11; *Appendix – Figures of the Turning Time* |
| Character | Alyen Ithra | `Alyen Ithra` | 5 | `Alyen Ithra`, `Alyen`, `ALYEN` | Chapters 6, 7, 9, 11, and 17 |
| Character | Gor of Almelah | `Gor of Almelah` | 6 | `Gor`, `GOR` | Chapters 15–19 and 21 |
| Location / system | Hive Earth / Hive | `Hive Spindle World Document` | 20 | `Hive`, `HIVE`, `Hive Earth`, `Hive Spindle 9`, `Spindle 9` | Chapters 1, 4–7, 9–21; both appendices |
| Historical figure | Maribel Voss | `Appendix – Figures of the Turning Time#Maribel Voss` | 2 | `Maribel Voss` | Chapter 22; *Appendix - The Voss Conquest* |
| Event / concept | The Voss Effect | `Appendix – Figures of the Turning Time#Administration and the Voss Effect` | 1 | `The Voss Effect` | Chapter 22 |
| Event / concept | Voss Conquest | `Appendix - The Voss Conquest#The Voss Conquest` | 1 | `Voss Conquest` | *Appendix – Figures of the Turning Time* |

Each eligible entity is linked only at its first meaningful occurrence in a document. Later repetitions remain unlinked.

## Important Entities Lacking Dedicated Notes

These entities appear in the selected documents but do not have exact, dedicated destination notes in the active project.

### Character

- Thena.

### Location

- Pacific Array.
- Hive Spindle 9 as a dedicated location note; current links use the broader Hive world document.
- Spindle 1, Spindle 22, and Spindle 31.
- Lower Grid; the related phrase *Lanes Between Signals* is also used as a chapter title.
- Below the Map.
- Helios Drift.
- Arkline Arcologies.
- Polar Grids.
- Equatorial Core Belts.
- Almelah.

### Faction / Institution

- Reversionist / Reversionists; the text uses the label for both a hidden actor and a broader dissident identity.
- Human Continuity Archive.
- The Great Union.
- Coalition of the Willing.
- States of the Great Angel.
- Minority World-State.

### Technology / System

- Linguistic interface / translation device.
- Helion-class scoutcraft and the Helion mission/training tradition.
- Quantum entanglement relay.
- Hyperspace gate.
- Passive filament tracker; the manuscript reveals it through `filament` and `tracker` wording rather than the full registry label.
- Cryo-capable modification / augmentation.

### Event / Concept

- Harmony.
- Surface Age.
- Turning Time.
- Great Sorrow.
- Proto-Under Hive.
- Under-Hive memory.

## Intentionally Not Linked

- Ordinary nouns, generic objects, unnamed attendants, watchers, residents, and other transient scene figures.
- Pronouns, epithets, and unnamed references such as `the hunter`, `the old figure`, or `the hidden source`.
- Later repetitions of an already linked entity in the same document.
- Plain `Earth` in pre-Hive memory, where redirecting it to the Hive world document would collapse an important historical distinction.
- Specific locations such as Spindle 22, Almelah, and Below the Map were not redirected to the broad Hive document.
- Generic or potentially ambiguous uses of `system`, `architecture`, `consensus`, `AI`, `relay`, `spindle`, and `harmony`.
- Appendix headings were not self-linked.
- Missing-note entities were left as plain manuscript text rather than linked to the lore registry or to semantically loose substitutes.

## Ambiguous Cases for Review

- **Broad Hive destination:** `Hive Spindle World Document` is the only existing durable world note for Hive Earth. It is used for contextual `Hive`, `Hive Earth`, `Hive Spindle 9`, and `Spindle 9` links, but it is not a dedicated note for Spindle 9.
- **Reversionist identity:** singular references may indicate the hidden individual, while plural or institutional usage can indicate the dissident thread. A future note structure should preserve that distinction.
- **Lower Grid / Lanes Between Signals:** the manuscript uses overlapping geographic language, but the canonical relationship should be settled before creating separate notes or aliases.
- **Proto-Under Hive / Under-Hive memory:** these are canonically distinct cultural concepts and should not be collapsed into the current geography of Below the Map.
- **Voss material:** Maribel Voss and The Voss Effect currently resolve to sections in a broader figures appendix rather than standalone notes.

## Vault and Sync Warnings

- Active project mirror: `B:\nicks\Documents\Obsidian_vault\02_Projects\Sci-Fi Novel`.
- Obsolete duplicate tree: `B:\nicks\Documents\Obsidian_vault\Sci-Fi Novel`; it was inspected but not used or modified.
- The following active mirror files differed from the repository before this pass even after existing wikilinks were stripped:
  - Chapter 1 – The Return
  - Chapter 10 – Signal to Noise
  - Chapter 11 – Contingencies
  - Chapter 12 – The Lanes Between Signals
  - Chapter 13 – The Soft Edge
  - Chapter 14 – The Broken Clinic
  - Chapter 15 – The Night the Oath Broke
  - Chapter 16 – Dead Relay
  - Chapter 19 – Below the Map
- Do not sync the repository over those files until their vault-only prose differences have been reconciled and reviewed.

## Verification

- All 22 edited documents passed exact byte comparison after inserted wikilink syntax was removed: 22/22.
- Existing mixed LF/CRLF line-ending patterns and Unicode punctuation were preserved.
- Total inserted links: 62.
- Duplicate destination within the same document: 0.
- All seven destination note basenames are unique across the full vault.
- All three appendix heading anchors exist exactly once in the active vault project.
- No missing-note candidate was linked.
- The lore registry and timeline summary were not modified.
