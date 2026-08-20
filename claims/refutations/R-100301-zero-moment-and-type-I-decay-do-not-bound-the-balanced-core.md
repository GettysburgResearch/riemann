# R-100301 — Zero moment and Type-I decay do not sign the balanced Vaughan core

Claim ID: `R-100301`  
Status: **EXACT INTERFACE FIREWALL**  
Created: 2026-08-20

The estimate in `L-100310` is an estimate for the complete lattice variable

\[
\sum_m m^{-1/2}K_1(Y/m).
\]

After Vaughan decomposition, the remaining coefficient is

\[
a_U(r)a_U(s)\mu(m),
\]

with \(r,s>U\). The zero moment has already been spent in the
\(\mathbf1\)-convolution term \(\mathcal T_U\); it does not act again on
\(\mathcal B_U\).

This distinction is algebraic. For \(U=3\),

\[
a_U(5)=-1,\qquad a_U(6)=1,
\]

and the Dirichlet convolution \(a_U*a_U\) already has the negative coefficient

\[
(a_U*a_U)(30)=-2.
\]

Thus \(a_U*a_U\) is not a positive completion, and a source-blind Schur,
Cauchy--Schwarz, or lattice-quadrature estimate cannot orient the balanced
trilinear.

The valid remaining theorem must retain all three coefficient families in
(L-100311.5), before taking absolute values.
