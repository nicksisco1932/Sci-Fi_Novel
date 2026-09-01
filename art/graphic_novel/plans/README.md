# Graphic Novel Plan Backups

The **Plan** entry in the Codex sidebar is a conversation artifact produced by a Plan-mode turn. It is not a file in this repository and does not automatically synchronize with these Markdown copies.

## Files

- `render-hive-earth-continuity-set.original.md`: exact backup of the original sidebar plan. Do not edit it.
- `render-hive-earth-continuity-set.experiment.md`: editable copy for controlled tests.

## How To Experiment

1. Edit one row in the experiment file's `Experiment Controls` table.
2. Start a new Codex turn with Plan mode enabled.
3. Use the `Test Prompt` at the bottom of the experiment file.
4. Compare the new proposed plan with the original backup.
5. Implement only after the revised plan matches the intended behavior.

Changing the experiment file affects a future run only when Codex is explicitly told to read it. It does not alter the existing sidebar plan or previous task history.

## Lowest-Risk Controls

- Canvas and orientation.
- Number and type of deliverables.
- Reference ordering.
- Composition and scale language.
- Documentation targets.
- QA checks.

Keep canon strictness and the no-manuscript-edit boundary unchanged during visual experiments.
