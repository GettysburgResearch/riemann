# L-19859 — The exact alias-corrected periodized tail preserves the signed hierarchy

Claim ID: `L-19859`  
Status: **PROVED TRANSFER THEOREM — FOLD-SYNTHESIS BOUND OPEN**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: exact periodized residual `L-19820`; exact Fourier containment `L-19858`; signed ordinary-tail hierarchy `L-19841`; quotient min--max `L-19846`  
Scope: finite-periodized alternative to the continuous theorem `T-19811`

## 1. Exact corrected tail

Let `U` be a finite source space and let

\[
 t:U\to H_{\rm out}
\]

be the ordinary omitted-support tail. Let

\[
 \mathfrak F_Lt:U\to H_{\rm in}
\]

be its complete multiplicative fold into the fundamental interval. Assume the periodized source vector already lies exactly in the finite Fourier space, as supplied by `L-19858`. Then the projection term in `L-19820` vanishes and the exact residual is

\[
 \boxed{Wu=t(u)-\iota_L\mathfrak F_Lt(u).}
\tag{L-19859.1}
\]

Because its two components have disjoint physical support,

\[
 \boxed{
 D_W:=W^*W
 =D_t+D_F,}
\tag{L-19859.2}
\]

where

\[
 D_t=t^*t,
 \qquad
 D_F=(\mathfrak F_Lt)^*(\mathfrak F_Lt)\succeq0.
\]

The finite localized Weil matrix is exactly

\[
 A_{\rm fin}=W^*Q_WW.
\tag{L-19859.3}
\]

## 2. Complete lower hierarchy is automatic

Assume the ordinary tail has at most one eigenvalue below `bd_6`:

\[
 \dim\mathbf1_{[0,bd_6)}
 (G^{-1/2}D_tG^{-1/2})\le1.
\tag{L-19859.4}
\]

Since `D_W>=D_t`,

\[
 \boxed{
 \dim\mathbf1_{[0,bd_6)}
 (G^{-1/2}D_WG^{-1/2})\le1.}
\tag{L-19859.5}
\]

Thus folded alias energy cannot create another low direction. No smallness of the fold is needed for the complete complement gap.

## 3. Target upper bound

Let `u_*` be the signed source target and suppose

\[
 \langle u_*,D_tu_*\rangle
 \le a d_4\|u_*\|_G^2.
\tag{L-19859.6}
\]

Assume only the target-line fold estimate

\[
 \boxed{
 \|\mathfrak F_Lt(u_*)\|^2
 \le K_F\langle u_*,D_tu_*\rangle.}
\tag{L-19859.7}
\]

Then

\[
 \boxed{
 \langle u_*,D_Wu_*\rangle
 \le(1+K_F)a d_4\|u_*\|_G^2.}
\tag{L-19859.8}
\]

A subpolynomial fold loss `K_F=R^{o(1)}` is harmless because `d_4/d_6=R^{-2+o(1)}`.

## 4. Quotient transfer to the exact finite Fourier space

Let

\[
 S:U\to E_N(L),
 \qquad
 S u=\Sigma_\mu E(u),
\]

be onto, and suppose

\[
 S^*HS\preceq K_SG,
\tag{L-19859.9}
\]

while the target is nondegenerate:

\[
 \|Su_*\|_H^2\ge k_*\|u_*\|_G^2.
\tag{L-19859.10}
\]

Define the quotient corrected-tail form

\[
 \overline D_W(v)
 =\min_{Su=v}\langle u,D_Wu\rangle.
\]

`L-19846`, with the sharp two-dimensional min--max proof, gives

\[
 \boxed{
 \theta_2(\overline D_W,H)
 \ge\frac b{K_S}d_6,}
\tag{L-19859.11}
\]

and

\[
 \boxed{
 R_{\overline D_W}(Su_*)
 \le\frac{(1+K_F)a}{k_*}d_4.}
\tag{L-19859.12}
\]

Therefore

\[
 \boxed{
 \frac{R_{\overline D_W}(Su_*)}
      {\theta_2(\overline D_W,H)}
 \le
 \frac{K_S(1+K_F)a}{bk_*}
 \frac{d_4}{d_6}.}
\tag{L-19859.13}
\]

Every complete source-map lower singular value disappears.

## 5. Exact finite local-Weyl target

The finite proof now needs a relative estimate for the same corrected residual:

\[
 \boxed{
 \frac1{\log R}
 \left\|
 \overline D_W^{-1/2}
 [A_{\rm fin}-(\log R)\overline D_W]
 \overline D_W^{-1/2}
 \right\|
 \longrightarrow0.}
\tag{L-19859.14}
\]

This is the correct replacement for both the false omitted-tail congruence of `T-19810` and the stronger-than-necessary whole-packet condition `D_q=o(D_t)`.

## 6. Analytic fold bound

For radial exact-radical sources, `mathfrak F_Lt` is a sum over multiplicative translates of the same normalized exterior profile. The natural sufficient estimate is

\[
 \|\mathfrak F_Lt\|^2
 \le R^{o(1)}\|t\|^2
\tag{L-19859.15}
\]

on the target line, obtained by:

1. retaining the leading `1/k` endpoint channel collectively;
2. using the Parseval identities of `L-19850`;
3. treating every stationary first-versus-`k` contribution by `L-19853`;
4. summing all higher endpoint jets absolutely.

This analytic estimate is proposed, not proved by the abstract transfer above.

## 7. Proof boundary

- The exact residual, positivity, low-index monotonicity, and quotient transfer are proved.
- Exact finite Fourier containment follows from `L-19858` at non-zeta-cycle supports.
- The target fold estimate (L-19859.7)/(L-19859.15) and the corrected-residual local-Weyl estimate (L-19859.14) remain analytic review targets.
- No RH conclusion is claimed here.
