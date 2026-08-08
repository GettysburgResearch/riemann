# X-21703 — Brownian gamma / logarithmic Nörlund experiments

## Exact layer

```bash
python verify.py
```

The verifier uses only Python's standard library and `fractions.Fraction`. It checks:

- double-pole partial fractions;
- the harmonic endpoint collapse;
- exact Laplace reconstruction;
- normalization;
- gamma-sum moments by two independent methods;
- the finite Mellin/Dirichlet polynomial;
- logarithmic Nörlund coefficient aggregation;
- four mutations.

Retained verdict:

```text
PASS_EXACT_BROWNIAN_GAMMA_NORLUND_ALGEBRA
```

It proves no zero theorem.

## Reconnaissance layer

`recon.py` requires NumPy and SciPy. It evaluates the gamma-stripped finite function, compares critical-line sign changes with an argument-principle winding count, and can reproduce the raw `N=75` mutation and selected Nörlund scans.

Example:

```bash
python recon.py raw 75 120 0.03
python recon.py norlund 500 300 0.05
```

All output from `recon.py` is ordinary floating-point reconnaissance. Matching counts at one finite height are not a zero certificate and do not imply BLNRZ.
