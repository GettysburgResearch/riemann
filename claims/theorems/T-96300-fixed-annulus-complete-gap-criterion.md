# T-96300 — One fixed-annulus complete-gap bound implies the Riemann Hypothesis

Claim ID: `T-96300`  
Status: **PROPOSED COMPLETE CONDITIONAL IMPLICATION — PRODUCER OPEN**  
Created: 2026-08-17  
Depends on: `L-96300`; the exact complete-gap Mellin pole theorem in PRs #352/#353  
RH status: **unproved because the producer is open**

Fix `h>0`. Assume that for some finite `B`,

\[
\boxed{
\mathfrak A_h(X)
=F_\Lambda(X)-2F_\Lambda(e^{-h}X)+F_\Lambda(e^{-2h}X)
=O(\log^B(2X)).
}
\tag{T-96300.1}
\]

Then its Mellin integral converges and is holomorphic throughout `Re(s)>0`. By `L-96300`,

\[
\widehat{\mathfrak A_h}(s)
=(1-e^{-hs})^2\widehat{F_\Lambda}(s).
\]

The multiplier is nonzero in `Re(s)>0`. Every zero `rho` of zeta with `Re(rho)>1/2` gives a nonremovable pole of the exact complete-gap transform at

\[
s=\rho-\frac12.
\]

This contradicts holomorphy. Hence there is no zero to the right of the critical line. The functional equation excludes zeros to its left, and RH follows.

The open producer is:

```text
ACTQ_h — Annular Complete-Tail Quadrature

For one fixed h>0, prove the bound (T-96300.1), equivalently a
polylogarithmic bound for the compact discrepancy in L-96300.6.
```

Unlike the former affine–Volterra endpoint composition, `ACTQ_h` contains no physical-packing normalization and no `J/P` ambiguity. It attacks the complete arithmetic gap directly.
