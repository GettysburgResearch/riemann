# X-20203 — Curvature-corrected prime transport

This exact standard-library regression checks the primal/dual/Bregman identity,
the strong-convexity square gate, and the quantile-transport recurrence for a
strictly convex quadratic barrier.

It is synthetic algebra only. It evaluates no zeta, prime stream, Selberg sum,
or cofinal RH predicate.

Run:

```bash
python verify.py certificates/synthetic.json
python -m unittest discover -s tests -v
```
