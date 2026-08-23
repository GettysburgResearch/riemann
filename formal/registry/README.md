# Formalization registry

`FORMALIZATION_MAP.tsv` is generated deterministically from `../../canonical/2026-08-22/claims.tsv` by:

```bash
python3 formal/scripts/generate_registry.py
python3 formal/scripts/validate_registry.py
```

It contains one row for every canonical semantic claim and keeps scientific and formal statuses separate. The joined report is intentionally ignored by Git: it is reproducible from the frozen scientific registry plus the sparse reviewer deltas, and avoiding one shared generated file prevents A/B/C merge conflicts.

At bootstrap, only the exact Mathlib-backed RH proposition is `STATED`. The `OpenCut` constructors in Lean are stable semantic metadata only; they do not become formal statements until an agent supplies the exact proposition and declaration through its owned delta.

Reviewers update only their owned sparse delta:

```text
deltas/A.tsv
deltas/B.tsv
deltas/C.tsv
```

A later reconciliation pass validates and snapshots the joined registry for `formal-v0.1`. The bootstrap generator never guesses proof status from the scientific verdict.
