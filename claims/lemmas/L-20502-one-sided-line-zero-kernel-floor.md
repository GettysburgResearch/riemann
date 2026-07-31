# L-20502 — One-sided line-zero deflation closes the Schur-corrected kernel

Claim ID: `L-20502`  
Title: The complete kernel needs only a lower residual LMI after a conditional simple-line frame; positive omitted mass is free  
Status: `PROPOSED — COMPLETE FINITE SCHUR PROOF; COFINAL RESIDUAL MOAT OPEN`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`; `L-19701`; the centered polarized Weil zero-sum formula  
Scope: final selected-real-zero kernel after the positive ambient complement has been isolated  
Related counterexample candidates: none

## 1. Kernel and selected positive line mass

Use the graph basis

\[
J_Z:R\longrightarrow K_Z\subset U
\]

and metric \(G_K=J_Z^*G_UJ_Z\) from `L-20501`.

Let \(Y\) be a finite proof-grade simple critical-line block and let

\[
S=S_{Y\mid Z}=V_YJ_Z.
\]

Its positive Weil contribution is

\[
\boxed{
Q_Y^K=S^*M_YS.
}
\tag{L-20502.1}
\]

Assume

\[
Q_Y^K\succeq\sigma^2G_K,
\qquad
\sigma^2>0.
\tag{L-20502.2}
\]

## 2. One-sided residual

Write the complete Weil form as

\[
Q_W=Q_Y+Q_{\mathrm{rem},Y},
\tag{L-20502.3}
\]

where \(Q_Y\) is the finite positive line-zero form and
\(Q_{\mathrm{rem},Y}\) contains every unselected zero and every remaining
term in the declared exact normalization.

The only residual hypothesis needed for a lower floor is

\[
\boxed{
J_Z^*Q_{\mathrm{rem},Y}J_Z
\succeq
-\omega G_K,
\qquad
\omega\ge0.
}
\tag{L-20502.4}
\]

There is no upper bound. Arbitrarily large positive unselected line-zero mass is
harmless.

Combining (L-20502.1)--(L-20502.4) gives

\[
\boxed{
J_Z^*Q_WJ_Z
\succeq
(\sigma^2-\omega)G_K.
}
\tag{L-20502.5}
\]

## 3. Positive-complement Schur correction

Let \(C\succ0\) be the already-isolated ambient complement, and let
\(Z_K:K_Z\to E\) be the kernel-to-complement cross map. In graph coordinates,
assume the exact upper LMI

\[
\boxed{
J_Z^*Z_K^*C^{-1}Z_KJ_Z
\preceq
\chi G_K,
\qquad
\chi\ge0.
}
\tag{L-20502.6}
\]

The Schur-corrected kernel is

\[
S_K
=
J_Z^*Q_WJ_Z
-
J_Z^*Z_K^*C^{-1}Z_KJ_Z.
\tag{L-20502.7}
\]

Therefore

\[
\boxed{
S_K
\succeq
(\sigma^2-\omega-\chi)G_K.
}
\tag{L-20502.8}
\]

This is the final finite-kernel floor.

In particular,

\[
\boxed{
\sigma^2>\omega+\chi
\Longrightarrow
S_K\succ0.
}
\tag{L-20502.9}
\]

More generally, if

\[
\sigma^2-\omega-\chi\ge-\varepsilon,
\]

then

\[
S_K\succeq-\varepsilon G_K.
\tag{L-20502.10}
\]

## 4. Exact proof

For every graph coordinate \(r\),

\[
\begin{aligned}
\langle S_Kr,r\rangle
={}&
\langle S^*M_YSr,r\rangle\\
&+
Q_{\mathrm{rem},Y}(J_Zr,J_Zr)\\
&-
\|C^{-1/2}Z_KJ_Zr\|^2.
\end{aligned}
\]

Apply (L-20502.2), (L-20502.4), and (L-20502.6) term by term. QED.

No absolute value, triangle inequality, or dimension estimate is used.

## 5. Möbius-tail formulation

Let

\[
\mathcal R_N=J_Z+T_N
\]

be any exact global-radical extension of the complete kernel, including the
Möbius extension of `L-20301/L-20302`.

At every zeta zero,

\[
\widehat{T_Nr}(\rho)
=
-\widehat{J_Zr}(\rho).
\tag{L-20502.11}
\]

Hence, by the zero-side formula,

\[
\boxed{
Q_W(T_Nr,T_Ns)
=
Q_W(J_Zr,J_Zs).
}
\tag{L-20502.12}
\]

The selected positive part is separately invariant:

\[
\boxed{
Q_Y(T_Nr,T_Ns)
=
Q_Y(J_Zr,J_Zs).
}
\tag{L-20502.13}
\]

Subtracting gives the stronger residual identity

\[
\boxed{
Q_{\mathrm{rem},Y}(T_Nr,T_Ns)
=
Q_{\mathrm{rem},Y}(J_Zr,J_Zs).
}
\tag{L-20502.14}
\]

Thus the free Dirichlet-polynomial coefficients of `L-20303` cannot change
\(\omega\). They may improve the Hardy realization and the Schur cross
\(\chi\), but the one-sided Weil residual is immutable.

## 6. The corrected Möbius target

The sufficient condition in `T-20301` used

\[
|Q_W(T_Nr,T_Nr)|
+
\|C^{-1/2}Z_KJ_Zr\|^2
\le
\eta\|J_Zr\|_{G_K}^2.
\tag{L-20502.15}
\]

That condition is valid but unnecessarily strong.

The exact replacement is:

\[
\boxed{
Q_{\mathrm{rem},Y}(T_Nr,T_Nr)
\ge
-\omega\|J_Zr\|_{G_K}^2,
}
\tag{L-20502.16}
\]

together with

\[
\boxed{
\|C^{-1/2}Z_KJ_Zr\|^2
\le
\chi\|J_Zr\|_{G_K}^2
}
\tag{L-20502.17}
\]

and the conditional selected-line frame (L-20502.2).

Positive residual directions are not charged.

## 7. Optimized finite moat

For fixed first frame \(Z\), define

\[
\boxed{
\mathfrak K_Z
=
\sup_Y
\left[
\sigma_{Y\mid Z}^2-\omega_{Y\mid Z}
\right],
}
\tag{L-20502.18}
\]

where \(Y\) runs over finite proof-grade simple-line blocks and
\(\omega_{Y\mid Z}\) is any directed lower endpoint satisfying
(L-20502.4) for the complete residual after subtracting \(Y\).

Then every number \(m<\mathfrak K_Z-\chi\) is a certified lower floor for
the corrected kernel whenever the corresponding finite proof object is
available.

The exact positive gate is

\[
\boxed{
\mathfrak K_Z>\chi.
}
\tag{L-20502.19}
\]

Optimizing over admissible first frames gives

\[
\mathfrak K
=
\sup_Z(\mathfrak K_Z-\chi_Z).
\tag{L-20502.20}
\]

A cofinal lower bound \(\mathfrak K_\lambda\ge-o(1)\) is sufficient for the
positive program.

## 8. False-RH alternative

Suppose RH is false and the finite kernel hierarchy captures a supported
off-line Xi-cardinal difference. Its complete Weil value stays below a fixed
negative constant after Schur elimination by `L-19701`.

Every finite simple-line form \(Q_Y\) vanishes on the limiting global cardinal
difference. Consequently the residual in (L-20502.3) retains the fixed negative
signature. On a capturing hierarchy, either

- the conditional frame \(\sigma_{Y\mid Z}^2\) collapses;
- the one-sided residual endpoint \(\omega\) dominates it;
- the Schur cross retains a negative moat;
- or the finite capture/normalization hypotheses fail.

Thus the cofinal positivity of (L-20502.8) is RH-bearing, but the finite theorem
does not hide where the sign lives.

## 9. Proof boundary

- The finite selected-line, residual, and Schur composition is exact.
- The theorem removes the absolute-tail overestimate.
- It does not prove a cofinal lower LMI for the unselected-zero residual.
- Production must retain one complete residual object; selected positive masses
  may not be subtracted twice.
- No RH proof is claimed until the directed moat
  \(\sigma^2-\omega-\chi\ge-o(1)\) is established cofinally.
