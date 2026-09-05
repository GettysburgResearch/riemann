# Reviewer D light replay

Run from the reconciliation directory:

```bash
python3 graph_validate.py
python3 replay/run_all.py
sha256sum -c SHA256SUMS
```

The replay checks schemas, exact frozen heads, unique semantic identities, source/head syntax, JSON hyperedges, referential closure, inactive open/refuted premises, complete PR lifecycle coverage, complete extraction coverage, conflict closure, direct-main/C-final locks, and absence of a proved-only path to RH.

It does not rerun any heavy mathematical campaign and does not prove a prose theorem merely because the registry validates.
