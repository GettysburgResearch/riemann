# T-99000 — Corrected frontier of the fractional Julia–Tao–Hermite route

Claim ID: `T-99000`  
Status: **COMPLETE DOWNGRADE AND EXACT REDUCTION**  
Created: 2026-08-18  
Frozen parent: PR #613 at `6809d8509f031f7f783ef20e2250ff2735e32924`

The original `L-98703` heat bound and the RH conclusion of `T-98700` are false
as a proof chain:

1. `R-99000` proves the stated uniform bound is analytically false at the real
   carrier for every `theta<1/192`.
2. `R-99001` proves number parity does not reflect logarithmic energy.
3. `R-99002` proves every uniform-center replacement retains an antipodal
   Liouville vertical limit of exponential energy type `1/2`.
4. `R-99003` proves positive continuum pole-centering cannot cancel the prime
   heat diagonal.
5. `L-99001` proves fractional intensity changes only polynomial prefactors;
   the heat exponent is fixed by the singularity location.

What survives is:

```text
fractional positive Euler chaos             exact
finite local Tao atom decomposition         exact at its declared scope
local off-line branch heat lower bound      exact
pole-centered mixed source                  exact
signed first-chaos current                  exact
```

The corrected conclusion-producing theorem is:

> **PCSCHE** — Pole-Centered Signed Cross-Scale Heat Estimate.  For the exact
> mixed source in `L-99000`, prove at every fixed center `tau_0` a subexponential
> critical heat-energy bound, preserving the continuum-prime cross terms and
> the cross-scale source labels before any positive trace.

A proof of PCSCHE would exclude every off-line zero by the local Hankel lower
bound.  Conversely, its first-chaos content is a reciprocal-zeta/prime-error
estimate at the RH scale.  PCSCHE is not proved in this packet.

```text
L-98703 uniform heat estimate              FALSE
T-98700 complete RH claim                  WITHDRAWN
pole centering at s=1                      CLOSED EXACTLY
positive-trace centering                   REFUTED
PCSCHE                                     OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
