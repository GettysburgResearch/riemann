# R-102100 — The \(17/16\) one-prime Harnack cone is not invariant under a second interior prime

Claim ID: `R-102100`  
Status: **REFUTED EXACTLY BY DIRECTED RATIONAL INTERVALS**  
Created: 2026-08-21  
Depends on: `L-102101`  
RH status: **unproved**

For an interior label `ell`, define

\[
H_\ell={17\over16\ell}I-\ell^{-1/2}U_\ell.
\]

`L-102101` proves `H_ell K_(p,q)>=0` for one insertion. It is tempting to iterate these operators. That is false.

Take

\[
(p,q,\ell_1,\ell_2,y)=(73,277,103,199,7519).
\]

Outward rational square-root enclosures give

\[
\boxed{(H_{103}H_{199}K_{73,277})(7519)<-{339\over1000}.}
\tag{R-102100.1}
\]

The replay computes every branch of `Psi` with exact rational interval arithmetic; no floating-point sign decision is used.

Therefore the gain in `L-102102` is a complete Euler-level theorem, not an invariant-cone theorem. It closes intervals while the total reciprocal budget is below one, but cannot be concatenated across successive bands without the full parity sum.
