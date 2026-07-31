# X-14313 — Exact separated-zero Hardy-frame floor

This checker verifies the scalar directed interface of `L-14320` with Python
integers and `fractions.Fraction` only.

Given safe rational bounds

```text
d_lower <= pi/(4 tau),
r_upper >= 2 sum_(n>=1) sech(pi D n/(4 tau)),
epsilon_upper >= exp(-2 tau L)/tau,
```

and a finite zero count `m`, it certifies

```text
sigma^2 = d_lower(1-r_upper)-m epsilon_upper.
```

The synthetic packet proves `147/100`; six adversarial tests pass. Production
use requires a typed analytic gate binding the exact separated certified-zero
set and all directed transcendental evaluations.
