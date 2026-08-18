# X-98010 — Zero-marginal Lorenz replay

Run

```bash
python3 experiments/X-98010-zero-marginal-lorenz/verify.py
```

Expected leading verdict:

```text
PASS_X_98010_ZERO_MARGINAL_LORENZ
```

The replay has two scopes.

1. Exact `fractions.Fraction` fixtures verify the finite convex theorem
   `lambda=0 is a global Lorenz minimizer iff T_E^+ <= T_O <= T_E`.
2. An 80-digit Decimal scan checks the cell derivative margin
   `B_N-c(N+1)A_N>0` through `N=100000` and checks finite source ordering.

The Decimal scans are hostile diagnostics, not the proof of the infinite theorem. The load-bearing proof is the elementary increasing-Riemann-sum argument in `L-98010`; it covers every cell and requires no numerical tail assumption.

The replay does not prove `ZMTS67`, `OSTP67`, `GPC67`, or RH.
