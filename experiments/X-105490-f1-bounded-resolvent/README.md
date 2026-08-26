# X-105490 — F1 bounded detector / critical resolvent replay

Run:

```bash
python experiments/X-105490-f1-bounded-resolvent/verify.py
```

The replay checks:

```text
direct Mellin integration of the bounded K_L density;
the exact dyadic/differential multiplier bridge;
failure of the historical direct equality;
positivity and H^-1 decay of the corrected critical weight;
nondecay of the withdrawn unregularized weight;
the stable anti-causal dyadic inverse;
critical conjugated multiplier lower bounds;
Beta Cauchy for normal-ordered slice amplitudes;
positive mean square of nonzero finite Dirichlet polynomials;
hostile mutation rejection.
```

It authenticates finite algebra and analytic identities. It does not prove any
open source-specific estimate or RH.
