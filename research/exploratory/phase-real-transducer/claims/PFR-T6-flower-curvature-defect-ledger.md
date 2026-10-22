# PFR-T6 — Flower turning and curvature-defect ledger

Status: **AUTHOR-PROVED EXACT GEOMETRIC THEOREM; REVIEW PENDING**
Scope: fixed-sign angular petals with simple endpoint zeros
RH status: **unproved**

For

\[
\Gamma(\phi)=r(\phi)e^{-i\phi},
\qquad r(\alpha)=r(\beta)=0,
\qquad L=\beta-\alpha,
\]

with `r` of fixed nonzero sign in the open interval:

1. the petal is simple away from the origin exactly when `L<=2*pi`;
2. for every `k>=1` with `2*pi*k<L`, there is a forced self-intersection with
   parameter separation `2*pi*k`;
3. the open-arc signed tangent turn is exactly `-(L+pi)`;
4. a simple closed petal has total signed turn `-2*pi`;
5. its total absolute curvature satisfies

\[
K_{abs}\ge2\pi+2(L-\pi)_+.
\]

Therefore, for `M` simple Hardy petals between consecutive simple
critical-line zeros,

\[
M\ge
\frac{\vartheta(\gamma_M)-\vartheta(\gamma_0)}{\pi}
-\frac1{2\pi}\sum_j(K_j-2\pi).
\]

The local clockwise-curvature numerator is the entirely real expression

\[
\mathfrak C_H=
\vartheta'^2Z^2+2(Z')^2-ZZ''+
(\vartheta''/\vartheta')ZZ'.
\]

With `D_H=vartheta'^2 Z^2+(Z')^2`, the open-petal turn and positive
back-turning mass are exactly

\[
\int_a^b\frac{\vartheta'\mathfrak C_H}{D_H}\,dt=L+\pi,
\qquad
P_{\rm open}=\int_a^b
\frac{\vartheta'(\mathfrak C_H)_-}{D_H}\,dt,
\]

and

\[
K_{abs}-2\pi=2\bigl(P_{\rm open}+(L-\pi)_+\bigr).
\]

Thus missing petal count is paid by an explicit real normalized nonconvexity
budget plus the positive origin-corner turn.  No bound on that budget is
proved here.

Full proof: `FLOWER_CURVATURE_108260.md`.
