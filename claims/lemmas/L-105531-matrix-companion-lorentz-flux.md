# L-105531 — Matrix-valued companion Lorentz flux

Claim ID: `L-105531`  
Status: **PROVED EXACT AT FINITE REGULAR-COLLAR SCOPE**  
Created: 2026-08-24  
Depends on: `L-105240` on PR #731; residue theorem  
RH status: **not assumed**

## 1. Derivative chain and observation map

Let `F_(k-1),F_k,F_(k+1)` be real entire functions with

\[
F_{k-1}'=F_k,
\qquad
F_k'=F_{k+1}.
\]

Fix `delta>0`, `lambda>=0`, and put

\[
p=F_k,
\qquad
E=F_{k+1}+i\delta F_k,
\qquad
H=F_{k+1}+\lambda F_{k-1}.
\tag{L-105531.1}
\]

Let

\[
\Phi(z)=(\phi_1(z),\ldots,\phi_d(z))^{\mathsf T}
\]

be holomorphic near a lower toothed rectangle, real on the real axis, and
fixed before the critical signs are observed.  Define the matrix-valued
meromorphic field

\[
\boxed{
\mathscr T_\Phi(z)
=
\frac{H(z)^2}{p(z)E(z)}
\Phi(z)\Phi(z)^{\mathsf T}.
}
\tag{L-105531.2}
\]

## 2. Residues

At a simple real zero `c` of `p`, put

\[
\rho_c=\frac{F_{k-1}(c)}{F_{k+1}(c)}.
\]

Then

\[
\boxed{
\operatorname{Res}_{z=c}\mathscr T_\Phi
=(1+\lambda\rho_c)^2
\Phi(c)\Phi(c)^{\mathsf T}\succeq0.
}
\tag{L-105531.3}
\]

At a simple companion zero `zeta` of `E`,

\[
\operatorname{Res}_{z=\zeta}\mathscr T_\Phi
=
\frac{H(\zeta)^2}{p(\zeta)E'(\zeta)}
\Phi(\zeta)\Phi(\zeta)^{\mathsf T}.
\tag{L-105531.4}
\]

Confluent blocks are obtained by the complete principal part and must not be
replaced by simple residues.

## 3. Exact matrix identity

Assume the collar contains no nonreal zero of `p`, no boundary pole, and only
simple real `p`-zeros.  Let

\[
D_\Phi
=
\sum_{p(c)=0,\ c\in(-T,T)}
(1+\lambda\rho_c)^2
\Phi(c)\Phi(c)^{\mathsf T}.
\tag{L-105531.5}
\]

Let `P_Phi` be the sum of the companion residues (L-105531.4) in the collar,
and let `O_Phi` be `(2 pi i)^(-1)` times the integral of `mathscr T_Phi`
over the bottom and two vertical sides.  Entrywise residue calculus and the
upper semicircle half-residues give

\[
\boxed{
D_\Phi
=Q_\Phi+2\Re O_\Phi-2\Re P_\Phi,
}
\tag{L-105531.6}
\]

where

\[
\boxed{
Q_\Phi
=\frac{\delta}{\pi}
\int_{-T}^{T}
\frac{H(x)^2}
 {F_{k+1}(x)^2+\delta^2F_k(x)^2}
\Phi(x)\Phi(x)^{\mathsf T}\,dx
\succeq0.
}
\tag{L-105531.7}
\]

This is the exact matrix polarization of the scalar Lorentz-energy identity.

## 4. Link to the real Pick residue block

For `lambda>0`, define

\[
G_\Phi=\sum_c\Phi(c)\Phi(c)^{\mathsf T},
\quad
S_\Phi=\sum_c\rho_c^2\Phi(c)\Phi(c)^{\mathsf T},
\quad
R_\Phi=\sum_c(-\rho_c)\Phi(c)\Phi(c)^{\mathsf T}.
\]

The scalar identity

\[
-\rho
=\frac{1+\lambda^2\rho^2-(1+\lambda\rho)^2}{2\lambda}
\]

gives the exact matrix relation

\[
\boxed{
R_\Phi
=\frac1{2\lambda}
\left(G_\Phi+\lambda^2S_\Phi-D_\Phi\right)
\succeq
\frac1{2\lambda}(G_\Phi-D_\Phi).
}
\tag{L-105531.8}
\]

Thus the companion defect is the literal matrix debt against a positive Pick
anchor; it is not merely a scalar count.

## 5. Scope

The theorem is finite and exact.  A wide Xi strip may contain nonreal and
confluent `F_k` zeros; their complete hyperbolic pole-jet blocks, the strip
partial indices, and the outer endpoint flux remain conclusion-bearing.  The
required asymptotic negative-trace estimate is `MATRIXLERC105531`, which is
not proved here.
