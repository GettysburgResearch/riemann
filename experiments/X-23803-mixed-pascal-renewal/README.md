# X-23803 — Mixed Pascal renewal reconnaissance

This directory supports the alternative producer `L-23815`.

## Files

- `verify.py` performs a directed `Decimal` interval check at the fixed endpoint
  `X=4096` for the frozen branching law
  
  ```text
  31/32 at max(1,floor(n/3))
   1/32 at floor(n/2).
  ```

- `scan_large.cpp` is a fast standard-library reconnaissance scanner. It uses
  floating-point arithmetic and is not a proof object.

- `results/directed-verification.json` records the finite directed verdict.

- `results/large-reconnaissance.txt` records only the tested endpoints and sign
  outcome of the floating-point scan.

## Exact status

The directed verifier certifies one finite recurrence and the exact node-balance
interface at that endpoint. It does **not** prove the cofinal sign theorem MPR,
BCT/BTF, or RH.

The large scanner is exploratory only. Its purpose is to locate counterexamples
and compare frozen branching laws; no conclusion may be extrapolated beyond the
listed endpoints.
