# X-27206 — Exact dyadic divergence commutator regression

This standard-library experiment verifies the exact finite interfaces used by `L-27207` and `L-27208`.

Run:

```bash
python3 verify.py
python3 -m unittest discover -s tests -v
```

It checks:

- the target-divergence half-scale identity;
- the adjacent central-tree commutator boundary and binary recursion;
- exact reconstruction of every carry column from the lifted flow;
- the unit endpoint-increment flow;
- fail-closed mutations deleting the bottom charge or an odd commutator and changing the scaling/sign.

The retained verifier uses rational surrogate targets because the identities are algebraic and hold for arbitrary targets satisfying the declared even scaling. It does not approximate logarithms or square roots.

The experiment does **not** prove Dyadic Commutator Debt, Cycle Debt, a prime-ramp asymptotic, or RH.
