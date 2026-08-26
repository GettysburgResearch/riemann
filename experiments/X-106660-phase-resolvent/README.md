# X-106660 — Phase-optimized and resolvent scalar certificates

This lightweight replay checks the exact finite-dimensional algebra used in
`L-106660--L-106661` and `T-106660`.

Run:

```bash
python -B experiments/X-106660-phase-resolvent/verify.py
```

The replay uses `fractions.Fraction` only. It verifies:

- the corrected one-pole cross-Hankel calibration;
- strict two-channel phase dispersion;
- the scalar resolvent completion;
- a non-diagonal positive-contraction fixture;
- the square-root-free Cauchy-Gram coordinate formula.

It does not evaluate Xi, certify a mesoscopic asymptotic, prove ninety percent,
prove density one, or prove RH.
