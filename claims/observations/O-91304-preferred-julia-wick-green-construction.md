# O-91304 — Current preferred construction after identifying the inverse as a Julia all-detail Wick corner

Observation ID: `O-91304`  
Status: **CURRENT HANDOFF**  
Created: 2026-08-12

The prime source and its signed inverse are now both explicit parts of one
local lossless geometry:

```text
forward source       scalar Julia ports;
global inverse       normalized all-detail Julia corner;
all generations      increasing Poisson/Fock chaos;
critical completion  Green/theta Wick renormalization.
```

The immediate production target is no longer an arbitrary source/model
intertwiner. It is `JWGR_omega`, a renormalized map on one explicitly given
generalized Wick vector.

Recommended attack:

1. express each finite-prime all-detail corner in log-delay coordinates;
2. apply the exact Suzuki Green primitive before removing the Julia
   normalizations;
3. derive the gamma/theta counterterm by Mellin integration by parts;
4. prove cutoff-uniform graph-norm bounds;
5. identify the limit with the causal Hardy vector;
6. retain the coupled Brownian and p=2 boundary traces;
7. prove dyadic cocycle compatibility.
