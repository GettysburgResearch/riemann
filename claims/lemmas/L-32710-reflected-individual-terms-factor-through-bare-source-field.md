# L-32710 — Source-convolved reflected individual terms factor through the bare source field

Claim ID: `L-32710`  
Title: After atomized carry localization, each individual term in the source-convolved independent-frequency Selberg identity is exactly a physical cross-inner-product with the bare inverse-source field  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC/PLANCHEREL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #302 `L-28013`; PR #241 `L-9518`; atomized carry window `L-29001`  
Scope: arbitrary invertible Dirichlet system and, in particular, the Q=4 Euler–Blaschke source; no energy closure or RH claim

## 1. General Dirichlet system

Let

\[
 A(s)=\sum_{n\ge1}a(n)n^{-s},
 \qquad
 B(s)=A(s)^{-1}=\sum_{n\ge1}b(n)n^{-s},
\]

and write

\[
 L(s)=-{A'(s)\over A(s)},
 \qquad
 C(s)=L(s)^2-L'(s).
\]

At coefficient level,

\[
 \Lambda=b*(a\log),
 \qquad
 C=\Lambda\log+\Lambda*\Lambda,
 \qquad
 q=b*\Lambda=-b\log.
\]

For independent real twists `t,u`, use the usual notation

\[
 B_t(s)=B(s+it),
 \qquad C_t(s)=C(s+it),
\]

and similarly for `-u`.

PR #302 `L-28013` gives exactly

\[
 (b_t*b_{-u})*(C_{t,-u}-C_t-C_{-u})
 =2q_t*q_{-u}.
 \tag{L-32710.1}
\]

The purpose of this lemma is to identify the two **individual** terms in the
same physical normalization as the right-hand current square.

## 2. Atomized physical localization

Let the fixed carry-position window have Mellin multiplier

\[
 H_\theta(s)=\zeta(s)N_\theta(s),
\]

as in `L-29001`. For any Dirichlet multiplier `F`, define its physical field by

\[
 \boxed{
 \widehat{\mathcal P_F}(t,\theta)
 =\zeta(\sigma+it)N_\theta(\sigma+it)F(\sigma+it)
 }
 \tag{L-32710.2}
\]

on a fixed admissible vertical line, with the usual compact logarithmic block
cutoff. The exact Fourier convention and block normalization are those of
`L-9518`; they cancel from every identity below.

For two multipliers `F,G`, Plancherel gives the exact block bilinear form

\[
 \boxed{
 \mathfrak B_J(F,G)
 =\int_J\!\int_I
 \mathcal P_F(x,\theta)
 \overline{\mathcal P_G(x,\theta)}\,d\theta\,dx.
 }
 \tag{L-32710.3}
\]

Equivalently its two-frequency kernel is the product of the two factors in
(L-32710.2), with the block Fourier kernel depending only on `t-u`.

## 3. Exact factorization of the first individual term

The Dirichlet multiplier of the first source-convolved individual Selberg term
is

\[
 B_t(s)B_{-u}(s)C_t(s).
\]

After multiplication by the two carry-window factors from physical
localization, it becomes exactly

\[
 \begin{aligned}
 &\zeta(s+it)N_\theta(s+it)
   B(s+it)C(s+it)\\
 &\qquad\times
 \zeta(s-iu)N_\theta(s-iu)B(s-iu).
 \end{aligned}
 \tag{L-32710.4}
\]

This is separable in `t` and `u`. Therefore its complete localized
independent-frequency contribution is

\[
 \boxed{
 \mathfrak B_J(BC,B).
 }
 \tag{L-32710.5}
\]

No diagonal restriction, source-cone lift, or rowwise approximation is used.

The reflected second individual term is similarly

\[
 \boxed{
 \mathfrak B_J(B,BC)
 =\overline{\mathfrak B_J(BC,B)}
 }
 \tag{L-32710.6}
\]

on the Hermitian diagonal.

Thus the sum of the two individual terms is exactly

\[
 \boxed{
 2\operatorname{Re}\mathfrak B_J(BC,B).
 }
 \tag{L-32710.7}
\]

## 4. The current square has the same normalization

Because

\[
 q=b*\Lambda
\]

has multiplier `BL`, the right side of (L-32710.1), under the same physical
localization, is

\[
 \boxed{
 2\mathfrak B_J(BL,BL)
 =2\int_J\!\int_I|\mathcal P_{BL}|^2.
 }
 \tag{L-32710.8}
\]

Therefore (L-32710.1) becomes, after physical localization, the exact identity

\[
 \boxed{
 \mathfrak P_J
 -2\operatorname{Re}\mathfrak B_J(BC,B)
 =2\|\mathcal P_{BL}\|_{J,I}^2,
 }
 \tag{L-32710.9}
\]

where `mathfrak P_J` denotes only the localized **product-source** term
`(b_t*b_-u)*C_(t,-u)`.

This isolates the source accounting sharply: the two individual pieces are no
longer an unidentified part of the product block.

## 5. Q=4 consequence

For the Q=4 Euler–Blaschke source,

\[
 B_4(s)=E_4(s)/\zeta(s).
\]

Hence the bare physical field has multiplier

\[
 \zeta(s)N_\theta(s)B_4(s)=E_4(s)N_\theta(s).
 \tag{L-32710.10}
\]

PR #337 `L-32709` proves directly in physical coordinates that this field is
deterministic/polylogarithmic:

\[
 \boxed{
 \|\mathcal P_{B_4}\|_{J,I}^2
 \ll(1+J)^2
 }
 \tag{L-32710.11}
\]

for every fixed balanced carry-position interval.

Consequently Cauchy--Schwarz in the exact factorization gives

\[
 \boxed{
 |\mathfrak B_J(B_4C_4,B_4)|
 \ll(1+J)\,\|\mathcal P_{B_4C_4}\|_{J,I}.
 }
 \tag{L-32710.12}
\]

Thus **both individual source-convolved reflected terms contain only one
RH-sensitive leg**. The second leg is the already-closed bare Q=4 source.

This is strictly stronger than saying that the unweighted source has a small
carry norm: it is the exact independent-frequency placement of that source in
the reflected identity.

## 6. What remains

Equation (L-32710.9) reduces the Q=4 reflected accounting problem to two
objects:

1. the product-source block `mathfrak P_J`;
2. the single higher-current field `mathcal P_(B_4 C_4)`.

The unweighted/bare source no longer appears as an unidentified two-frequency
boundary term. In particular, the negative fifteen-contact collar of
`L-32706/L-32707` and the deterministic bare carry theorem `L-32709` now have a
precise physical slot.

A completion may proceed by either:

- placing `mathfrak P_J` into the Q=4 Kummer reserve and absorbing the
  `B_4C_4` cross term; or
- resumming the `B_4C_4` hierarchy by a finite Jordan deformation before taking
  the reflected square.

Neither step is asserted here.

## 7. Proof boundary

Closed exactly, subject to review:

1. physical localization of both source-convolved individual Selberg terms;
2. their exact factorization through the bare source field;
3. the identical normalization of the RH-sensitive current square;
4. reduction of the entire individual-term contribution to one cross-inner-product;
5. Q=4 insertion of the deterministic/polylog bare field.

Still open:

1. product-source block positivity/reserve placement;
2. control or resummation of the `B_4C_4` leg;
3. the coefficient-one neutral recurrence;
4. RH.
