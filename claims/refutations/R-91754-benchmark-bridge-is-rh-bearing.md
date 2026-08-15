# R-91754 — The `J_Lambda-4sqrt(X)` bridge is RH-bearing and excluded

Claim ID: `R-91754`  
Status: **PROVED CIRCULARITY FIREWALL**  
Created: 2026-08-15  
Review source: PR #484  
RH status: **unproved**

Let

\[
D(X)=J_\Lambda(X)-4\sqrt X.
\]

For `Re z>1/2`, finite Mellin integration gives

\[
\widehat D(z)
 =\frac{-\zeta'/\zeta(z+1/2)}{z^2}
  -\frac4{z-1/2}.
\]

The positive-real pole at `z=1/2` cancels. Every zero

\[
\rho=\frac12+\delta+i\gamma,\qquad\delta>0,
\]

creates a genuine nonreal pole at `z=delta+i gamma`, while no positive-real
singularity remains.

If `D(X)<=C log X` eventually, alter a compact interval and put

\[
g(X)=C\log X-D(X)\ge0.
\]

The Mellin transform of `g` retains every off-line nonreal pole. If its
abscissa lies left of one such pole, the defining integral is holomorphic there.
If the abscissa is positive and lies at or to its right, Landau's theorem forces
a singularity at the real abscissa. Both alternatives contradict the pole
audit. Hence

\[
\boxed{D(X)=O_+(\log X)\Longrightarrow\mathrm{RH}.}
\]

No controlling theorem may use that estimate as a pre-RH input. Native cost is
computed only by the exact positive dual

\[
J_\Lambda(X)-\mathcal H(d)
 =\sum_qY_4(q)[\Omega_X(q)-\Xi_d(q)].
\]
