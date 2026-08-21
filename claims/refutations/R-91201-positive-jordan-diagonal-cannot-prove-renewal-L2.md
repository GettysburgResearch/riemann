# R-91201 — A positive-Jordan or diagonal argument cannot prove the critical renewal energy

Claim ID: `R-91201`  
Status: **EXACT METHOD FIREWALL**  
Created: 2026-08-12  
RH status: **unproved**

Write the factor-four output in reciprocal-scale coordinates as

\[
 \mathcal B_\omega(1/u)
 =\sum_{n\ge1}c_\omega(n)K_\omega(nu),
 \qquad
 c_\omega(n)=\frac{J_{2\omega}(n)}{n^\omega}>0,
\]

where `K_omega` is supported in `[0,1]`. Then

\[
 \mathcal I_\omega
 =\int_0^{1/4}\left|\sum_n c_\omega(n)K_\omega(nu)\right|^2du.
\]

For every `n>=4`, the diagonal term is

\[
 c_\omega(n)^2\int_0^{1/n}|K_\omega(nu)|^2du
 =\frac{c_\omega(n)^2}{n}\int_0^1|K_\omega(v)|^2dv.
\]

On primes,

\[
 c_\omega(p)=p^\omega(1-p^{-2\omega})\asymp p^\omega,
\]

so the sum of positive diagonal terms contains

\[
 \sum_p\frac{c_\omega(p)^2}{p}
 \asymp\sum_p p^{2\omega-1}=\infty
 \qquad(\omega>0).
\]

Thus every proof which takes absolute values, drops cross terms, or seeks a
Tonelli-positive decomposition in the native positive Jordan coordinates is
forced to diverge.  Finiteness, if true, comes from an infinite signed
cancellation between different arithmetic scales.

This is consistent with `T-91201`: one uncancelled off-line pole produces an
exponentially growing causal mode, while innerness makes the same boundary
transfer exactly isometric. The missing theorem cannot be a source-blind
coefficient estimate.
