# X-27201 — Exact ternary-fragmentation replay

The checker verifies, using only integers and `fractions.Fraction`:

- the deterministic `ceil(n/3)+floor(2n/3)` divergence recurrence;
- exact reconstruction of arbitrary rational carry targets;
- the scalar tail-renewal identity;
- the continuum ternary carry minus divisibility-boundary formula;
- the base-three digit-sum endpoint identity;
- a wrong-rounding mutation.

Run:

```bash
python verify.py
python -m unittest discover -s tests -v
```

It does not test or certify positivity of the actual logarithmic target,
Ternary Fragmentation Positivity, MFT, or RH.
