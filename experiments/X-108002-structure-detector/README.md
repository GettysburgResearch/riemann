# X-108002 — battery verification of the structure detector (T-108002)

Run from the repository root:

```
python3 experiments/X-108002-structure-detector/verify.py
```

Expected banner: `PASS_108002_STRUCTURE_DETECTOR checks=10`.

This experiment intentionally exercises the deposited instrument
(`research/exploratory/2026-08-30-two-programme-pass/core/reconstruct.py`)
rather than reimplementing it: the instrument and its refusal semantics are
the claimed object. All arithmetic is `EXACT_RATIONAL`; the function-field
Mobius rows are computed by exhaustive exact Mobius over monic polynomials
(degrees < 7, q = 2 and 3), independent of the identity they confirm.
Writes `results/verification.json` with `"rh_established": false`.

Tests: `python3 -m unittest discover -s experiments/X-108002-structure-detector/tests`
