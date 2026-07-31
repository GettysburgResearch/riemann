# L-20503 — RKHS interpolation lower bound for every exact local radical tail

Claim ID: `L-20503`  
Title: A conditional simple-line frame gives an extension-independent Hardy lower bound; no fixed finite kernel admits a vanishing exact radical tail  
Status: `PROPOSED — COMPLETE RKHS PROJECTION PROOF`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`; `L-20301/L-20303`; the reciprocal-Hardy evaluation Gram of `L-14320`  
Scope: analytic realization of exact global-radical extensions of the complete finite kernel  
Related counterexample candidates: none

## 1. Reproducing-kernel setting

Let \(\mathcal H_\tau\) be the declared reciprocal-Hardy Hilbert space in which
evaluation at each real centered ordinate is bounded. For a finite set

\[
Y=\{\gamma_1,\ldots,\gamma_m\},
\]

let \(k_{\gamma_j}\in\mathcal H_\tau\) be the evaluation representers:

\[
\widehat q(\gamma_j)
=
\langle q,k_{\gamma_j}\rangle_\tau.
\tag{L-20503.1}
\]

Put

\[
H_Y=
\left(
\langle k_{\gamma_j},k_{\gamma_\ell}\rangle_\tau
\right)_{j,\ell}.
\tag{L-20503.2}
\]

For distinct real ordinates, \(H_Y\succ0\).

In the normalization of `L-14320`,

\[
\boxed{
(H_Y)_{j\ell}
=
\frac{\pi}{4\tau}
\operatorname{sech}
\left(
\frac{\pi(\gamma_j-\gamma_\ell)}{4\tau}
\right).
}
\tag{L-20503.3}
\]

The abstract theorem below needs only positivity of \(H_Y\).

## 2. Minimum norm for prescribed evaluations

Let

\[
\mathcal E_Yq
=
\bigl(
\widehat q(\gamma_1),\ldots,\widehat q(\gamma_m)
\bigr).
\]

For every \(q\in\mathcal H_\tau\),

\[
\boxed{
\|q\|_\tau^2
\ge
(\mathcal E_Yq)^*
H_Y^{-1}
(\mathcal E_Yq).
}
\tag{L-20503.4}
\]

### Proof

The orthogonal projection of \(q\) onto

\[
\operatorname{span}
\{k_{\gamma_1},\ldots,k_{\gamma_m}\}
\]

has the form

\[
p=\sum_jc_jk_{\gamma_j}.
\]

Its evaluation vector is \(H_Yc\). Requiring
\(\mathcal E_Yp=\mathcal E_Yq=v\) gives

\[
c=H_Y^{-1}v.
\]

Therefore

\[
\|p\|_\tau^2
=
c^*H_Yc
=
v^*H_Y^{-1}v.
\]

Since \(p\) is an orthogonal projection, \(\|q\|_\tau\ge\|p\|_\tau\). QED.

Equality holds for the minimum-norm interpolant.

## 3. Apply the bound to the graph kernel

Let \(K_Z=\operatorname{Ran}J_Z\) be the complete graph kernel of `L-20501`, and
let the second line block \(Y\) have conditional evaluation matrix

\[
S_{Y\mid Z}=V_YJ_Z.
\tag{L-20503.5}
\]

Let

\[
\mathcal R=J_Z+T
\tag{L-20503.6}
\]

be **any** exact global Weil-radical synthesis of this kernel. This includes
every Möbius extension and every free-coefficient extension of `L-20303`.

At every zeta zero,

\[
\widehat{Tc}(\gamma)
=
-\widehat{J_Zc}(\gamma).
\]

Hence

\[
\mathcal E_YTc
=
-S_{Y\mid Z}c.
\tag{L-20503.7}
\]

Substituting into (L-20503.4) yields

\[
\boxed{
\|Tc\|_\tau^2
\ge
c^*
S_{Y\mid Z}^*H_Y^{-1}S_{Y\mid Z}
c.
}
\tag{L-20503.8}
\]

In operator form,

\[
\boxed{
T^*G_\tau T
\succeq
S_{Y\mid Z}^*H_Y^{-1}S_{Y\mid Z}.
}
\tag{L-20503.9}
\]

This lower bound is independent of the Möbius cutoff, the correction bump, and
all free Dirichlet-polynomial coefficients.

## 4. Fixed-level no-go theorem

Let

\[
G_K=J_Z^*G_UJ_Z
\]

and define

\[
\boxed{
\vartheta_{Y\mid Z}^2
=
\lambda_{\min}
\left(
G_K^{-1/2}
S_{Y\mid Z}^*H_Y^{-1}S_{Y\mid Z}
G_K^{-1/2}
\right).
}
\tag{L-20503.10}
\]

If \(S_{Y\mid Z}\) is injective, then

\[
\vartheta_{Y\mid Z}^2>0.
\]

Equation (L-20503.9) gives

\[
\boxed{
\|Tc\|_\tau
\ge
\vartheta_{Y\mid Z}
\|J_Zc\|_{G_K}.
}
\tag{L-20503.11}
\]

Therefore:

\[
\boxed{
\text{At a fixed finite support, no exact global-radical extension of a
nonzero complete kernel can have uniformly vanishing Hardy tail.}
}
\tag{L-20503.12}
\]

This is not a defect of the Möbius construction. It is forced by interpolation
at actual critical-line zeros.

## 5. Necessary cofinal collapse

Suppose a cofinal synthesis program claims

\[
T_j^*G_{\tau_j}T_j
\preceq
\eta_j^2G_{K,j},
\qquad
\eta_j\to0.
\tag{L-20503.13}
\]

For every proof-grade conditional frame \(Y_j\),

\[
\boxed{
\vartheta_{Y_j\mid Z_j}^2
\le
\eta_j^2.
}
\tag{L-20503.14}
\]

Consequently a necessary condition is

\[
\boxed{
\sup_{Y_j}
\vartheta_{Y_j\mid Z_j}^2
\longrightarrow0.
}
\tag{L-20503.15}
\]

Thus a valid near-radical hierarchy must become nearly invisible, in the Hardy
interpolation metric, to every finite conditional line frame.

Under false RH, supported approximants to the global off-line cardinal
difference provide exactly such collapsing real-zero evaluations while
retaining a fixed negative Weil value. The theorem therefore explains why
Hardy-tail smallness alone cannot be obtained from qualitative finite framing.

## 6. Separation from the one-sided Weil criterion

`L-20502` does **not** require

\[
\|T_j\|_\tau\to0.
\]

It requires only a one-sided lower LMI for the residual Weil form and a Schur
cross bound. Positive Hardy mass and positive Weil mass are harmless.

Accordingly:

- (L-20503.11) refutes overstrong fixed-level small-tail claims;
- it does not refute the sharper one-sided selected-line criterion;
- a positive proof should avoid paying for the full Hardy norm whenever the
  residual has favorable sign.

## 7. Support-restricted strengthening

If a tail \(q\) is known to be supported in \((0,\rho]\), `L-20304` supplies
the scalar strengthening

\[
\|q\|_\tau
\ge
\sqrt{2\tau}\rho^{-\tau}
|\widehat q(\gamma)|
\]

at each real \(\gamma\).

The matrix theorem (L-20503.9) is different: it accounts for correlations among
many evaluations and is sharp in the full RKHS. A production checker should
retain both lower bounds and use the stronger one.

## 8. Proof boundary

- The RKHS projection argument is exact.
- The explicit sech Gram inherits the reciprocal-Hardy normalization audit.
- The theorem supplies a lower, not an upper, tail estimate.
- It shows that increasing the Möbius cutoff cannot force fixed-level Hardy
  convergence.
- No cofinal rate for the conditional interpolation floor is proved.
