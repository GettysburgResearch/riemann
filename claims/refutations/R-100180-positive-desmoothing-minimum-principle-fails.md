# R-100180 — Finite-completion positivity does not positively desmooth by a minimum principle

Claim ID: `R-100180`  
Status: **PROVED INTERFACE FIREWALL**  
Created: 2026-08-20  
RH status: **unproved**

For one prime let

\[
G(X)=(I+rS_p)F(X)=F(X)+rF(X/p),\qquad r=p^{-1/2}>0.
\]

Even pointwise positivity `G(X)>=0` does not imply `F(X)>=0`. A positive inverse would require

\[
(I+rS_p)^{-1}=\sum_{k\ge0}(-r)^kS_p^k,
\]

whose coefficients alternate.

A proposed cutoff-minimum principle would need endpoint monotonicity in the direction `F(X/p)<=F(X)`, because then `G(X)<=(1+r)F(X)`. The critical Bernstein kernel `kappa_(m,m-1)(sqrt(Q/X))` has the opposite elementary shape: `kappa_(m,m-1)(t)` is increasing in `t>0`, hence each positive kernel atom decreases with `X`.

Therefore adaptive finite Euler squaring crosses the prime-harmonic owner wall, but that theorem cannot be transferred back to the original critical observable by a source-blind monotonicity or positive-inverse argument. Any valid closure must use additional source-specific information linking adjacent completed states, or bypass desmoothing entirely.
