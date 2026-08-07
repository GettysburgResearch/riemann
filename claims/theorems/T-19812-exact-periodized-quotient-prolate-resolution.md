# T-19812 — Exact-periodized quotient-prolate resolution theorem

Claim ID: `T-19812`  
Status: **PROPOSED FULL FINITE RESOLUTION COMPOSITION — FOLDED-TAIL ANALYTICS REQUIRE REVIEW**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: exact Fourier containment `L-19858`; exact corrected tail `L-19820`; corrected-tail hierarchy `L-19859`; stationary alias ledger `L-19853`; target identity `L-19849`; finite Rayleigh criterion `T-15103`; CCM finite real-zero and transform-limit interfaces  
Supersedes: the rejected omitted-tail congruence in `T-19810`  
Scope: finite-matrix alternative to the continuous theorem `T-19811`

## 1. Exact finite source realization

Let

\[
 L=2\log\lambda,
 \qquad
 E_N(L)=\operatorname{span}\{e_k:|k|\le N\}.
\]

Choose a support which is not a zeta cycle. By `L-19858`,

\[
 \boxed{E_N(L)\subset\Sigma_\mu E(\mathcal S_0^{\rm ev}).}
\tag{T-19812.1}
\]

Thus every finite CCM vector is the exact periodization of a global arithmetic-radical source. No high Fourier projection residual occurs on the periodized side.

Choose a finite source reservoir `U_(L,N)` and an onto map

\[
 S_{L,N}:U_{L,N}\to E_N(L),
 \qquad
 S_{L,N}u=\Sigma_\mu E(u).
\tag{T-19812.2}
\]

No lower singular-value estimate is assumed.

## 2. Exact corrected residual

For a source `u`, let `t_u` be the ordinary exterior tail and let `mathfrak F_Lt_u` be its complete fold into the fundamental interval. Since the periodized vector already lies in `E_N`, the exact residual of `L-19820` is

\[
 \boxed{
 W_{L,N}u=t_u-\iota_L\mathfrak F_Lt_u.}
\tag{T-19812.3}
\]

The finite localized Weil matrix satisfies exactly

\[
 \boxed{
 A_{L,N}
 =W_{L,N}^*Q_WW_{L,N}.}
\tag{T-19812.4}
\]

Define the positive corrected-tail Gram

\[
 D_{L,N}=W_{L,N}^*W_{L,N}.
\tag{T-19812.5}
\]

## 3. Quotient hierarchy hypotheses

Assume that on a positive-measure set of supports in every sufficiently large radial block:

1. the complete source corrected-tail form has at most one direction below the signed scale,
   \[
   \dim\mathbf1_{[0,b_Rd_6)}
   (G_R^{-1/2}D_{L,N}G_R^{-1/2})\le1;
   \tag{T-19812.6}
   \]
2. an inversion-even source target `u_R` satisfies
   \[
   \langle u_R,D_{L,N}u_R\rangle
   \le a_Rd_4\|u_R\|_{G_R}^2;
   \tag{T-19812.7}
   \]
3. the source map has only an upper bound and target-line lower bound,
   \[
   S_R^*H_RS_R\preceq K_RG_R,
   \qquad
   \|S_Ru_R\|_{H_R}^2\ge k_R\|u_R\|_{G_R}^2;
   \tag{T-19812.8}
   \]
4. the losses satisfy
   \[
   a_R,K_R,k_R^{-1},b_R^{-1}=R^{o(1)}.
   \tag{T-19812.9}
   \]

`L-19859` supplies the exact transfer from the ordinary signed tail once the target fold synthesis is `R^(o(1))`.

Let `overline D_(L,N)` be the quotient corrected-tail form on `E_N(L)`. Then

\[
 \boxed{
 R_{\overline D}(v_R)
 \le\frac{a_R}{k_R}d_4,}
\tag{T-19812.10}
\]

and

\[
 \boxed{
 \theta_2(\overline D,H_R)
 \ge\frac{b_R}{K_R}d_6,}
\tag{T-19812.11}
\]

where `v_R=S_Ru_R`. Hence

\[
 \frac{R_{\overline D}(v_R)}
      {\theta_2(\overline D,H_R)}
 =R^{-2+o(1)}\to0.
\tag{T-19812.12}
\]

## 4. Relative corrected-tail local-Weyl hypothesis

Assume the exact finite matrix is relatively scalar in the same quotient metric:

\[
 \boxed{
 (1-\eta_R)(\log R)\overline D_{L,N}
 \preceq A_{L,N}
 \preceq
 (1+\eta_R)(\log R)\overline D_{L,N},
 \qquad
 \eta_R\to0.}
\tag{T-19812.13}
\]

The required analytic ledger is the corrected one:

```text
ordinary exterior tail;
complete multiplicative fold;
Bessel radial endpoint;
one stationary point for every later alias;
Mellin Airy fold;
collective leading endpoint series;
off-line oscillatory support averaging.
```

No term is discarded by a finite-projection approximation.

## 5. Finite ground line

Equations (T-19812.10)--(T-19812.13) imply:

\[
 A_{L,N}\succeq0,
\]

\[
 \mu_R(v_R)
 \le(1+\eta_R)(\log R)(a_R/k_R)d_4,
\]

and

\[
 \lambda_2(A_{L,N})
 \ge(1-\eta_R)(\log R)(b_R/K_R)d_6.
\]

Thus the target excess divided by the complete finite gap tends to zero. The exact finite ground line is eventually simple and inversion-even and converges projectively to `v_R`.

## 6. Target and Hurwitz

Assume, in the moving Hardy norm,

\[
 \|c_Rv_R-k_R^\Xi\|_{\lambda,\tau_R}\to0,
 \qquad
 \tau_R\nearrow1/2,
\tag{T-19812.14}
\]

with nonzero real `c_R`. The exact Hermite limit satisfies

\[
 \mathcal M(Ep_+)=2C_H\xi,
\]

and the signed correction is `O(d_4/d_6)`.

The finite Rayleigh-floor theorem gives the same moving-Hardy convergence for the exact finite ground states. CCM's finite real-zero theorem then says that every finite ground-state transform has only real zeros. Local-uniform convergence to `Xi` and Hurwitz exclude every nonreal centered zero.

Therefore the hypotheses above imply

\[
 \boxed{\mathrm{RH}.}
\tag{T-19812.15}
\]

## 7. Relationship to the second review

The review correctly rejects

\[
 A^V=S^{-*}A^US^{-1}
\]

when `A^U` is the ordinary omitted-support tail form. The present theorem never makes that identification. It uses the exact alias-corrected residual `W_(L,N)` furnished by periodization.

The high-Fourier residual `q` from `L-19832` belongs to the direct-restriction realization. Exact rotation projection on the periodized source range makes the periodized Fourier residual zero; the complete fold is retained instead.

## 8. Exact remaining review frontier

Independent review must verify:

1. the rotation/source Bochner integral and exact containment in `L-19858` in the precise CCM periodization normalization;
2. the complete folded-tail target bound and low-index hierarchy in `L-19859`;
3. the corrected Bessel/stationary-alias/Airy ledger for the folded residual;
4. the relative finite local-Weyl estimate (T-19812.13);
5. the moving-Hardy target normalization (T-19812.14).

Until those pass:

```text
exact-periodized full proposal: PROPOSED
accepted proof of RH:           NO
```
