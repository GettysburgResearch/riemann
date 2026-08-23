# Formalization registry

`FORMALIZATION_MAP.tsv` is generated deterministically from `../../canonical/2026-08-22/claims.tsv`.
It contains one row for every canonical semantic claim and keeps scientific and formal statuses separate.

Reviewers update only their owned sparse delta:

```text
deltas/A.tsv
deltas/B.tsv
deltas/C.tsv
```

A later reconciliation pass merges approved deltas into the generated map. The bootstrap generator never guesses proof status from the scientific verdict.
