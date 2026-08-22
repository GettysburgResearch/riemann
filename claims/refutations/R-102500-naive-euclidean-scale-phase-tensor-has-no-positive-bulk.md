# R-102500 — The naive Euclidean scale–phase tensor has no positive bulk

Claim ID: `R-102500`  
Status: **PROVED METHOD REFUTATION / REDESIGN FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102501`  
RH status: **unproved**

Consider one labelled mode

\[
F_\lambda(u,\theta)=\phi(u-\lambda)e^{-i\lambda\theta}.
\]

The ordinary Euclidean wave/Laplace residual is

\[
(\partial_u^2+\partial_\theta^2)F_\lambda
=
(\phi''(u-\lambda)-\lambda^2\phi(u-\lambda))e^{-i\lambda\theta}.
\]

The frequency `lambda=log(n)` is unbounded, while the compact mother changes
sign. The residual has no source-independent sign and no uniform positive bulk
decomposition.

Consequently the standard stress tensor formed from
`(partial_u,partial_theta)` cannot supply the programme's determinant reserve.

The correct replacement is

\[
Q=u-i\sum_\ell(\log p_\ell)\partial_{\vartheta_\ell},
\]

which acts by `u-log(n)` on each source atom and satisfies the exact Heisenberg
commutator of `L-102501`.
