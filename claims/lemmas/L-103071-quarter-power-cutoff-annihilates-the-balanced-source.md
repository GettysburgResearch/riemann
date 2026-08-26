# L-103071 — The quarter-power cutoff makes the balanced equal-pair source support-empty

Claim ID: `L-103071`  
Status: **PROVED EXACT SUPPORT THEOREM**  
Created: 2026-08-26  
Depends on: `L-106080`, `L-106132`, `L-106133`; fixed support of `K_L`  
RH status: **not assumed**

Retain the dyadic physical and owner-product blocks

\[
Y\le X<2Y,
\qquad
A\le P<2A,
\]

and the cutoff

\[
V=V_{Y,A}
=
\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

## 1. Literal balanced-core support

The Boolean Vaughan defect is

\[
a_V=\varepsilon-\mu_V\star\mathbf1_{\rm sf}.
\]

Every nonzero factor in

\[
a_V\star a_V\star\mu_{\rm sf}
\]

has two disjoint factors

\[
r>V,
\qquad
s>V.
\]

Thus every balanced physical core `a` satisfies

\[
\boxed{
a\ge rs\ge(V+1)^2.
}
\tag{L-103071.1}
\]

Equivalently, in the canonical half-source square of `L-106132--L-106133`,
each half-core is larger than `V`, so their product obeys the same lower
bound.

## 2. Physical support contradiction

A balanced completed physical atom is

\[
N=P a^2.
\]

By (L-103071.1),

\[
a^2\ge(V+1)^4
>
\frac{2Y}{A}.
\]

Since `P>=A`,

\[
\boxed{
N=P a^2>2Y.
}
\tag{L-103071.2}
\]

But the derivative kernel is supported in `[1,8]`. A term

\[
K_L(X/N)
\]

can be nonzero only when `N<=X`. On the complete dyadic block,
`X<2Y`, contradicting (L-103071.2).

Therefore

\[
\boxed{
\mathcal O_{K_L}
\left[\mathcal B_{V,\rm sf}^{\rm equal\ pair}\right](X)
=0
\qquad(Y\le X<2Y).
}
\tag{L-103071.3}
\]

The same statement holds for every fixed differential image of the common
mother, because differentiation does not enlarge multiplicative support.

## 3. Scope

The theorem is coefficientwise and does not use cancellation. The two labelled
copies of `67` cause no exception: owner labels are distinct in the Boolean
source, and their physical product is larger, not smaller.

The cutoff is fixed on a disjoint source block. No source is copied and no
owner pair is selected after observation.
