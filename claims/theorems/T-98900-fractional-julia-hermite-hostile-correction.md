# T-98900 — Hostile correction of the fractional Julia–Tao–Hermite candidate

Claim ID: `T-98900`  
Status: **EXACT DOWNGRADE; FRACTIONAL HEAT PRODUCER OPEN**  
Created: 2026-08-18  
Depends on: `R-98900--R-98902`, `L-98900`  
RH status: **unproved**

The algebraic fractional-chaos theorem `L-98700`, the atomwise finite Tao Gram
`L-98701` at its stated scope, and the local analytic pole audit of `L-98702`
are retained subject to their own reviews.  The load-bearing energy estimate
`L-98703.1` is **not proved by the published argument**.

Three exact interfaces fail or were omitted:

1. Weyl displacement changes parity:
   \[
   W(f)^*\Pi W(f)=W(-2f)\Pi.
   \]
2. Weyl displacement changes the logarithmic heat generator:
   \[
   W(f)^*d\Gamma(h)W(f)
   =d\Gamma(h)+a^*(hf)+a(hf)+\langle f,hf\rangle.
   \]
3. If the heat is conjugated correctly, the positive diagonal used by a
   Schur/Cauchy payment is invariant under the unitary change of coordinates;
   its one-prime sector already grows like `exp((1/4-o(1))T)`, so positivity
   alone cannot supply the tunable `exp(96 theta T+o(T))` rate for all small
   `theta`.

The exact compensated centered representation must retain both

```text
Pi_f = W(2f) Pi;
H_(T,f) = W(f)^* exp(-A^2/(4T)) W(f).
```

A repaired proof would therefore require a new signed estimate for the joint
compensated matrix coefficient.  Denote this missing theorem by `CFHE98900`.
It is not implied by the positive finite Tao Gram and is presently open.

```text
fractional positive chaos                 RETAINED
finite atomwise Tao Gram                  RETAINED AT LOCAL SCOPE
local pole-growth audit                   RETAINED / SEPARATE REVIEW
Weyl-parity invariance                    FALSE
free-heat invariance under centering      FALSE
positivity-only tunable trace exponent    REFUTED AS A METHOD
CFHE98900 compensated heat estimate       OPEN / RH-BEARING
L-98703 / T-98700 conclusion              UNESTABLISHED
Riemann Hypothesis                        UNPROVEN
```
