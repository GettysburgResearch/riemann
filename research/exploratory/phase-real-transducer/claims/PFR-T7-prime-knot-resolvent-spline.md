# PFR-T7 — the actual-Xi Gamma resolvent is a prime-knot spline

Claim ID: `PFR-T7`  
Status: **PROVED EXACT ANALYTIC / DISTRIBUTIONAL THEOREM**  
Depends on: `PFR-T4`, `PFR-T5`  
RH status: **unproved**

For `a>1/2`, integer `m>=2`, let

\[
R_{a,m}(t)=\sum_\rho
\frac{e^{(\rho-1/2)t}}{(a+1/2-\rho)^m}.
\]

Then `R_(a,m)` is `C^(m-2)` and is analytic away from the points `log n`
with `Lambda(n) != 0`.  At every prime power,

\[
R_{a,m}^{(m-1)}((\log n)^+)
-R_{a,m}^{(m-1)}((\log n)^-)
=(-1)^{m+1}\frac{\Lambda(n)}{\sqrt n}.
\]

The jump is independent of `a`.  Distributionally, with `D=d/dt`,

\[
(a-D)^mR_{a,m}=\mathscr Z,
\]

where `mathscr Z` is the critical explicit-formula distribution, and

\[
(a-D)R_{a,m}=R_{a,m-1},
\qquad
\partial_aR_{a,m}=-mR_{a,m+1}.
\]

Thus one real function contains the prime powers as local derivative jumps and
the supremal zero displacement as its global exponential/energy abscissa from
`PFR-T5`.  No bound on that response is proved.

Full proof: `CONTINUATION_108320.md`.
