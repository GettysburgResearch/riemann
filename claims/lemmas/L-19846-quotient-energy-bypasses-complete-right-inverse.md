# L-19846 — Quotient energy bypasses a complete quantitative right inverse

Claim ID: `L-19846`  
Status: **PROPOSED EXACT FINITE-DIMENSIONAL REPAIR**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Scope: adversarial correction to source-frame theorem 1; proves that a lower singular-value bound for the complete source map is not required for the signed target/gap transfer

## 1. Setup

Let `(U,G)` be a finite-dimensional source coefficient space, let `D>=0` be
the complete ordinary tail form in that same source metric, and let

\[
 S:U\longrightarrow V
 \tag{L-19846.1}
\]

be a surjective arithmetic localization/periodization map into the complete
finite CCM space `(V,H)`.

Define the induced quotient energy on `V` by

\[
 \mathfrak D(v)
 :=\min_{Su=v}\langle u,Du\rangle.
 \tag{L-19846.2}
\]

The minimum exists after quotienting the zero-energy kernel. Equivalently, if

\[
 U_0=(\ker S)^{\perp_D},
 \tag{L-19846.3}
\]

then `S:U_0->V` is an isomorphism and

\[
 \mathfrak D=S^{-*}D|_{U_0}S^{-1}.
 \tag{L-19846.4}
\]

A small singular value of `S` makes the corresponding quotient energy large.
It is not a low-energy obstruction.

## 2. Source hierarchy

Assume there is a normalized source target `u_*` such that

\[
 \langle u_*,Du_*\rangle\le a_Rd_4\|u_*\|_G^2,
 \tag{L-19846.5}
\]

and the source tail form has at most one eigenvalue below the signed scale:

\[
 \dim\mathbf1_{[0,b_Rd_6)}(G^{-1/2}DG^{-1/2})\le1.
 \tag{L-19846.6}
\]

Here

\[
 a_R=R^{o(1)},
 \qquad
 b_R=R^{-o(1)},
 \qquad
 d_4/d_6=R^{-2+o(1)}.
 \tag{L-19846.7}
\]

Assume only an **upper** source-map bound

\[
 S^*HS\preceq K_RG,
 \qquad
 K_R=R^{o(1)},
 \tag{L-19846.8}
\]

and target nondegeneracy

\[
 \|Su_*\|_H^2\ge k_R\|u_*\|_G^2,
 \qquad
 k_R=R^{-o(1)}.
 \tag{L-19846.9}
\]

No lower bound for `S` on the complete source space is assumed.

## 3. Target upper bound

Let `v_*=Su_*`. The minimizing definition gives

\[
 \mathfrak D(v_*)
 \le\langle u_*,Du_*\rangle.
 \tag{L-19846.10}
\]

Therefore

\[
 \boxed{
 \frac{\mathfrak D(v_*)}{\|v_*\|_H^2}
 \le\frac{a_R}{k_R}d_4.}
 \tag{L-19846.11}
\]

Only the target line needs a lower image bound.

## 4. Counting low quotient directions

Put

\[
 \alpha_R=\frac{b_R}{2K_R}d_6.
 \tag{L-19846.12}
\]

Suppose, toward a contradiction, that the quotient form has two linearly
independent vectors `v_1,v_2` with Rayleigh quotient below `alpha_R`. Choose
their `D`-minimal lifts `u_1,u_2 in U_0`. Their span is two-dimensional because
`S` is injective on `U_0`.

Let `E_<` be the source spectral subspace below `b_Rd_6`; by (L-19846.6) it has
dimension at most one. Some nonzero combination

\[
 u=c_1u_1+c_2u_2
 \tag{L-19846.13}
\]

is `G`-orthogonal to `E_<`. Hence

\[
 \langle u,Du\rangle\ge b_Rd_6\|u\|_G^2.
 \tag{L-19846.14}
\]

On the other hand, the two-dimensional restriction of the quotient form below
`alpha_R H` gives

\[
 \langle u,Du\rangle
 =\mathfrak D(Su)
 <\alpha_R\|Su\|_H^2
 \le\alpha_RK_R\|u\|_G^2
 =\frac12b_Rd_6\|u\|_G^2,
 \tag{L-19846.15}
\]

a contradiction. Thus

\[
 \boxed{
 \dim\mathbf1_{[0,\alpha_R)}
 (H^{-1/2}\mathfrak DH^{-1/2})\le1.}
 \tag{L-19846.16}
\]

Equivalently, the second quotient eigenvalue satisfies

\[
 \boxed{
 \theta_2(\mathfrak D,H)
 \ge\frac{b_R}{2K_R}d_6.}
 \tag{L-19846.17}
\]

## 5. Target/gap ratio

Combining (L-19846.11) and (L-19846.17),

\[
 \frac{\theta_1(\mathfrak D,H)}
      {\theta_2(\mathfrak D,H)}
 \le
 \frac{2a_RK_R}{b_Rk_R}\frac{d_4}{d_6}
 =R^{-2+o(1)}\longrightarrow0.
 \tag{L-19846.18}
\]

Thus projective target selection survives every complete source-map singular
value, however small, provided the source tail itself has only one direction
below the signed `d_6` scale.

## 6. Why the reviewer’s `sigma_min` gate is overstrong

A complete lower singular-value estimate would bound the norm of an arbitrary
right inverse. The quotient argument never uses such an inverse. It uses:

1. qualitative surjectivity;
2. an upper map bound;
3. one target-line lower bound;
4. the low-index count of the complete source tail form.

If `S` nearly kills a high source direction, then representing its normalized
output requires a large source and therefore a large quotient tail energy. That
direction is safely above the target, not below it.

Accordingly, the superalgebraic small singular directions in `R-19843` do not
by themselves kill the positive route. They kill the specific congruence
argument in `T-19807`, but the correct quotient-energy composition remains
available.

## 7. Exact remaining analytic obligation

The theorem moves the genuine common-frame frontier to:

\[
 \boxed{
 \dim\mathbf1_{[0,R^{-o(1)}d_6)}
 (G^{-1/2}D_{\rm complete}G^{-1/2})\le1}
 \tag{L-19846.19}
\]

on a **surjective complete source reservoir**, together with

\[
 S^*HS\preceq R^{o(1)}G
 \tag{L-19846.20}
\]

and target nondegeneracy. This is a high-reservoir alias/coercivity theorem, not
a quantitative right-inverse theorem.

`L-19841/L-19844/L-19845` prove (L-19846.19) for the declared growing low
prolate packet. They do not yet prove that this packet is surjective, nor do
they cover an arbitrary high-mode reservoir added to obtain surjectivity.

## 8. Proof boundary

The finite-dimensional quotient theorem is exact. It does not prove the
remaining complete-reservoir analytic inequality (L-19846.19). It shows that
the reviewer correctly rejected the claimed congruence, but that the specific
polylogarithmic `sigma_min` replacement proposed in the review is not logically
minimal.

No RH conclusion is claimed.
