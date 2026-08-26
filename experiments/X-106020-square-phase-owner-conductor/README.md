# X-106020 — Square-phase owner-conductor family replay

Standard-library exact replay for `L-106020--L-106022`, `R-106020`, and the
finite algebra in `T-106020`.

It checks:

```text
Hilbert-valued nonzero square-phase energy by exact Ramanujan orthogonality;
pair-quotient formula p I - J;
strict principal contraction (p-1)/(p+1);
two-modulus tensor identity and contraction;
principal/quadratic two-root fibre of the square map on characters;
strict algebraic improvement over phase-cardinality Cauchy.
```

The vectors use exact Gaussian-integer coordinates. No floating-point roots of
unity are evaluated.

Run:

```bash
python3 verify.py --output /tmp/x106020.json
cmp /tmp/x106020.json results/verification.json
```

Expected verdict:

```text
PASS_X_106020_SQUARE_PHASE_OWNER_CONDUCTOR_FAMILY
```

The replay does not evaluate a Dirichlet `L`-function, prove the coherent
short-core moment `SOCM106020`, prove `HBCQDSP102888`, or prove RH.