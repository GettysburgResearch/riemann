# T-92910 — A bounded native deficit forces RH by a reconstructed prime-square and Mellin–Landau chain

Claim ID: `T-92910`  
Status: **PROPOSED COMPLETE ENDPOINT THEOREM — INDEPENDENT REVIEW REQUIRED**  
RH status: **unproved pending reconstruction**

Assume the rows of `L-92911`–`L-92913` exist for every integer \(X\ge10^{12}\). Their ordinary feasibility gives
\[
\mathcal H(d_X)=\sum_q\Lambda(q)C_{d_X}(q)
\le
P_\Lambda(X)=\sum_q\Lambda(q)w_X(q).
\]
Therefore
\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X)<55000.
\]

By `L-92914`,
\[
A(X)=F_\Lambda(X)-\frac{C_{\square}}4\log^2X+o(\log^2X)<0
\]
for all sufficiently large \(X\).

## Mellin–Landau exclusion

Put \(a(t)=A(e^t)\). The exact prime-endpoint Mellin calculation, physically imported with this packet, gives a meromorphic Laplace transform whose only possible singularities in \(\Re z>0\) come from nontrivial zeta zeros \(\rho\) with \(\Re\rho>1/2\). At such a zero,
\[
\operatorname*{Res}_{z=\rho-1/2}\widehat a(z)
=\frac{m_\rho}{(\rho-1/2)^2}\ne0.
\]
All real positive candidate singularities are explicitly absent.

Since \(-a(t)\ge0\) eventually, Landau's theorem for Laplace transforms of eventually nonnegative functions says that its finite abscissa of convergence, if positive, is a singularity on the positive real axis. The exact symbol has no such singularity, so the abscissa is at most zero. Hence the transform is analytic throughout \(\Re z>0\), contradicting any pole \(z=\rho-1/2\) there.

There is therefore no nontrivial zero with \(\Re\rho>1/2\). The functional equation reflects every zero with \(\Re\rho<1/2\) to one with real part greater than one half. Thus every nontrivial zero lies on the critical line:
\[
\boxed{\mathrm{RH}.}
\]
The compact initial interval contributes an entire transform and does not affect the argument.
