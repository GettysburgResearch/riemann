# Diagnostic replays

Both scripts in this directory are **non-proof diagnostics**.

## Original constant/local replay

```text
catalan_audit_replay.py
replay.json
```

This lane checks selected formulas in arXiv:2609.04176v1, including the final
decimal subtraction, the small-prime constant, the middle-prime integral, the
finite reduced inequality (5.21), and the unsafe `5B` cutoff example.

It requires SciPy. The frozen output was generated with Python 3.13.5 and
SciPy 1.17.0.

## Hostile Proposition 9.5 replay

```text
catalan_height_hostile_replay.py
height_hostile_replay.json
```

This pure-standard-library lane evaluates a one-term lower bound on the
largest-summand majorant used by Proposition 9.5. It computes exact ideal local
minima and uses an explicit two-term alternating-tail lower bound.

The finite output corroborates the hostile review, but the proof-level result
is analytic. Read:

```text
../DEEP_HOSTILE_REVIEW.md
../HEIGHT_BOUND_COUNTERCHECK.md
```

The current verdict is:

```text
posted v1 proof: invalid as written
Catalan irrationality: not established by the preprint
Catalan rationality: not established either
```
