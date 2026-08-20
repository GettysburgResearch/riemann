# L-102005 — The centered cubic double-owner collar is exactly threshold-localized

Claim ID: `L-102005`  
Status: **PROVED EXACT SUPPORT/EXPANSION THEOREM**  
Created: 2026-08-21  
Depends on: PR #691 `L-100614`  
RH status: **not assumed**

Let

\[
\widetilde H_{ij}(X)=H_{ij}(X)-M_{ij}(X),
\]

with `H_(ij)` and the nonnegative deep carrier `M_(ij)` as in `L-100614`.
Write the finite interior label set as `I=(i,j)` and for `S subseteq I` put

\[
m_S=\prod_{h\in S}p_h,
\qquad
r_S=m_S^{-1/2}.
\]

Expand the interior Euler product. Then

\[
\boxed{
\widetilde H_{ij}(X)
=
\sum_{S\subseteq I}(-1)^{|S|}r_S\,
\widetilde K_{ij}\!\left({X\over m_S}\right),
}
\tag{L-102005.1}
\]

where

\[
\widetilde K_{ij}(Y)
=(I-U_{p_i})(I-U_{p_j})\Psi(Y)
-192\sqrt Y(1-p_i^{-1/2})(1-p_j^{-1/2}).
\tag{L-102005.2}
\]

The scalar kernel `widetilde K_(ij)` vanishes whenever all four endpoint-shifted arguments are on the deep branch. In particular,

\[
\boxed{
\widetilde K_{ij}(Y)=0
\qquad(Y\ge p_ip_j).
}
\tag{L-102005.3}
\]

Therefore every nonzero term in (L-102005.1) satisfies

\[
{X\over m_S}<p_ip_j,
\qquad	ext{i.e.}\qquad
\boxed{m_S>{X\over p_ip_j}.}
\tag{L-102005.4}
\]

Thus the centered collar is supported only on **large interior subset products**. The complete sum may be written exactly as

\[
\boxed{
\widetilde H_{ij}(X)
=
\sum_{\substack{S\subseteq I\\m_S>X/(p_ip_j)}}
(-1)^{|S|}m_S^{-1/2}
\widetilde K_{ij}(X/m_S).
}
\tag{L-102005.5}
\]

This is stronger than the qualitative partial-activation statement of `L-100614`: the threshold is explicit and multiplicative.

## Consequence for long intervals

If `p_j>p_i^A` and `p_ip_j<=X`, every harmful interior subset product must satisfy

\[
m_S>{X\over p_ip_j}.
\]

Hence, whenever `p_ip_j` is substantially below `X`, negativity can only come from high product-depth inside the interval. This is exactly the regime in which finite interior squaring and divisor renewal are available.

No sign estimate is claimed in this lemma. Its role is to force all possible negativity into a large-product tail before any absolute value is taken.