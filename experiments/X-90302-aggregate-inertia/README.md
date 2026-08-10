# X-90302 — Aggregate inertia elimination

This experiment verifies the exact Fraction algebra in `L-90304`.

It checks:

- the aggregate determinant-defect inequality;
- the source-only bound after eliminating the unknown current;
- a sharp equality case;
- a mutation witness showing that the factor `A/(A-F)` cannot be removed.

It does **not** verify:

- any Q4 analytic estimate;
- physical/carry normalization;
- the reflected recurrence;
- RH.

Run:

```bash
python verify.py > results/verification.json
```

Expected classification:

```text
PASS_EXACT_AGGREGATE_INERTIA_ELIMINATION
```

Retained proof-object SHA-256:

```text
11dd103d5c25fe22dc9dfbe81bd9e85a85f200ad1e066a2b02b2e0868aec171a
```
