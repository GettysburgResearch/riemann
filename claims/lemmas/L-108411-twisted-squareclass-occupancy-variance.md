# L-108411 — Twisted squareclass pushforward diagonalizes the occupancy variance

Claim ID: `L-108411`  
Status: **PROVED EXACT FINITE SOURCE THEOREM**  
Created: 2026-08-31  
Depends on: `L-108410`; PR #771 `L-107304`  
RH/GRH status: **not assumed**

Let `X` be a finite abelian group. For nonnegative functions `A,B` define

\[
(A\star_2B)(r)
=
\sum_{xy^2=r}A(x)B(y).
\tag{L-108411.1}
\]

Put

\[
A_0=\sum_xA(x),
\qquad
B_0=\sum_yB(y),
\qquad
n=A\star_2B,
\qquad
N=A_0B_0.
\]

PR #771 proves the exact Fourier identity

\[
\boxed{
\widehat n(\chi)
=
\widehat A(\chi)\widehat B(\chi^2).
}
\tag{L-108411.2}
\]

Combining this with `L-108410` gives

\[
\boxed{
{H_X(n)^2\over N}
\le
\mathcal V_2(A,B)
:={1\over A_0^2B_0^2}
\sum_{\chi\ne1}
|\widehat A(\chi)|^2
|\widehat B(\chi^2)|^2.
}
\tag{L-108411.3}
\]

This is the exact character-energy coordinate of the physical occupancy
fluctuation.

## 1. Explicit resonance split

Let `R` be any declared exceptional character set, in particular the
quadratic/constant channels isolated on PR #771. Then

\[
\boxed{
\mathcal V_2
=
\mathcal V_2^{\rm nr}
+
\mathcal V_2^{\rm res},
}
\tag{L-108411.4}
\]

where the two terms are the same sum restricted to `chi notin R` and
`chi in R`. No triangle inequality or family-size factor is used in this
separation.

The reduced Kummer object and twisted Plancherel theorem of PR #771 control
the complete deep nonresonant multiplier at their stated function-field
scope. The explicit resonance term remains part of `QRESBIND107300`.

## 2. A useful pointwise sufficient bound

If

\[
|\widehat A(\chi)|
\le
\epsilon_A{A_0\over\sqrt{|X|}},
\qquad
|\widehat B(\chi^2)|
\le
\epsilon_B{B_0\over\sqrt{|X|}}
\]

for every nonexceptional `chi`, then

\[
\boxed{
\mathcal V_2^{\rm nr}
\le
\epsilon_A^2\epsilon_B^2.
}
\tag{L-108411.5}
\]

The normalization is load-bearing: a max-coefficient estimate without the
`|X|^{-1/2}` scale does not control the sum over characters.

## Scope

This theorem makes the physical occupancy map exactly diagonal in character
space. It does not prove the live mask completion, the number-field twisted
energy estimate, or the quadratic/principal binding.
