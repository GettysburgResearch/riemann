# T-93851 — Heat-resolvent prime-block decorrelation would imply CPBD and RH

Claim ID: `T-93851`  
Status: **PROPOSED CONDITIONAL PRODUCER — OPEN**  
Created: 2026-08-15  
Depends on: `L-93850`; PR #498 `T-93255`  
RH status: **unproved**

Define the distinct-prime heat-resolvent correlation

\[
\mathfrak H_{\ne p}(N)
=\sum_{p<r}\int_0^\infty
 e^t h_{p,N}(t)h_{r,N}(t)dt.
\]

The proposed Heat-Resolvent Prime-Block Decorrelation theorem (`HRPBD`) is:

\[
\boxed{
|\mathfrak H_{\ne p}(N)|
\ll N\log^B N
}
\tag{T-93851.1}
\]

for one fixed `B`, uniformly in `N`.

Expanding the total heat energy gives

\[
\int_0^\infty e^t|h_N(t)|^2dt
=
\sum_p\int_0^\infty e^t|h_{p,N}(t)|^2dt
+2\mathfrak H_{\ne p}(N).
\]

The left side is nonnegative. `L-93850` bounds the diagonal by

\[
8960N\log(2N).
\]

Therefore HRPBD implies

\[
\int_0^\infty e^t|h_N(t)|^2dt
\ll N\log^{B'}N.
\]

By the weighted Cauchy bridge,

\[
|\mathcal A_\circ(N)|^2
\ll N\log^{B'}N.
\]

This is CPBD, so the zero-safe cubic Mellin theorem of PR #498 gives RH.

The new proposed gate is not claimed proved. Its value is structural:

```text
static CPBD obstruction
-> integrated heat-time cross-prime correlation
-> safe complete-tower diagonal
-> explicit positive resolvent kernel
```

It offers a direct meeting point with the First-Hermite heat lane without
claiming that the two arithmetic block families are identical.
