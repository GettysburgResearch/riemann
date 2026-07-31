# X-15605 — Exact phase-aware prime-bound checker

This experiment implements the final rational comparison in `T-15604`.
It performs no zeta, prime, logarithm, trigonometric, or window evaluation.
Those analytic values must already be supplied as directed rational intervals.

The checker verifies:

- ordered nonoverlapping ordinate shells;
- total shell-count upper bounds;
- exact subtraction of selected modeled multiplicities;
- the factor-two conjugate-zero shell budget;
- the high-zero and trivial-zero radii;
- exact interval subtraction;
- strict separation from the RH-valid band.

Run:

```bash
python verify.py certificates/synthetic.json \
  --output /tmp/verification.json
python -m unittest discover -s tests -v
```

The retained synthetic certificate has total RH-valid radius `43/100` and
residual interval `[10,101/10]`, so it returns a strict positive violation.
It tests the finite checker only; it is not a Riemann-zeta calculation.

Proof-object SHA-256:

```text
8ecafb5da1d9f31c2cfe638a7067ce25ab00b9d65dc5df90bfc62e60114ed774
```
