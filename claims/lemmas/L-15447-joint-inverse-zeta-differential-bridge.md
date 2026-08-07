# L-15447 — Joint inverse-zeta differential bridge

Claim ID: `L-15447`  
Title: The dyadic prime signal times the analytic-totient carrier is one safe first-order differential image  
Status: **PROPOSED — EXACT TRANSFORM IDENTITY; LOCAL TRACE ESTIMATE SEPARATE**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15445`; PR #226 `L-9512/T-9506`; `T-15412`  
Cross-route connections: PRs #158, #202, #208, #216, #218, #219, #222, #224, #226  
Scope: exact arithmetic/analytic bridge; no zero-free hypothesis and no RH conclusion are used in the identity

## 1. The inverse-zeta carrier

Let

\[
 U(s)
 :=\mathcal T(s)-{3/\pi^2\over s-2}
 =-{\zeta(s-1)\over s(s-1)\zeta(s)},
 \tag{L-15447.1}
\]

where `mathcal T` is the Mellin transform of the analytic summatory-totient
error in `L-15445`. Initially (L-15447.1) holds for `Re s>2`, and then by
meromorphic continuation.

Put

\[
 \boxed{
 A(s)={\zeta'\over\zeta}(s-1)-{1\over s}-{1\over s-1}.}
 \tag{L-15447.2}
\]

Logarithmic differentiation of (L-15447.1) gives the exact identity

\[
 {U'(s)\over U(s)}
 =A(s)-{\zeta'\over\zeta}(s).
 \tag{L-15447.3}
\]

Equivalently,

\[
 \boxed{
 U'(s)-A(s)U(s)
 =-{\zeta'\over\zeta}(s)U(s).}
 \tag{L-15447.4}
\]

No division by `U` is needed in (L-15447.4).

## 2. The dyadic prime signal

Let

\[
 Q_\diamond(\log Y)
 ={\psi(Y)-4\psi(Y/4)\over\sqrt Y}
 \tag{L-15447.5}
\]

be the dyadic Chebyshev signal of `T-15412`. In the same `s` coordinate its
Laplace/Mellin transform is

\[
 \boxed{
 \mathcal Q(s)
 =-{1-4^{1-s}\over s}{\zeta'\over\zeta}(s).}
 \tag{L-15447.6}
\]

Multiplying (L-15447.4) by `(1-4^(1-s))/s` yields

\[
 \boxed{
 \mathcal Q(s)U(s)
 ={1-4^{1-s}\over s}
 \bigl[U'(s)-A(s)U(s)\bigr].}
 \tag{L-15447.7}
\]

This is the exact joint prime–totient identity. The left side is the transform
product of the RH-sensitive prime ray and the inverse-zeta carrier. The right
side is a first-order differential operator with a coefficient that is safe in
the open critical strip.

## 3. Why the coefficient is safe

On

\[
 {1\over2}<\Re s<1,
 \tag{L-15447.8}
\]

one has `-1/2<Re(s-1)<0`. The functional equation expresses
`zeta(s-1)` as a nonzero elementary factor times `zeta(2-s)`, and
`Re(2-s)>1`. Hence

\[
 \zeta(s-1)\ne0
 \qquad(1/2<\Re s<1).
 \tag{L-15447.9}
\]

Therefore `A(s)` is holomorphic in the entire open strip. On every closed
substrip it has at most polynomial vertical growth, obtained from the functional
equation, Stirling's formula, and the absolutely convergent Euler series for
`zeta'/zeta(2-s)`.

The factor `1-4^(1-s)` has zeros only on `Re s=1`; the rational factor `1/s` is
regular on the open strip. Thus (L-15447.7) introduces no new RH-sensitive
divisor.

## 4. Multiplicity ledger at a hypothetical zero

Suppose `rho` is a nontrivial zero with

\[
 {1\over2}<\Re\rho<1
\]

and multiplicity `m>=1`. Since `zeta(rho-1)`, `rho`, and `rho-1` are nonzero,
`U` has a pole of exact order `m` at `rho`. The coefficient `A` is regular
there, and

\[
 U'-AU
\]

has a pole of exact order `m+1`. Equivalently, the right side of
(L-15447.4) is the product of a simple logarithmic-derivative pole and the
order-`m` inverse-zeta pole.

Consequently

\[
 \boxed{
 \mathcal Q(s)U(s)
 \text{ has an uncancelled pole of order }m+1\text{ at }s=\rho.}
 \tag{L-15447.10}
\]

This strengthens the pole exposure: the joint source cannot hide an off-line
zero by multiplicity or by a zero of the dyadic multiplier.

## 5. Physical interpretation

Products of Mellin transforms are multiplicative convolutions. After matching
the harmless normalization shifts used in `L-15445`, (L-15447.7) says:

```text
(dyadic centered prime ray) Mellin-convolved with
(analytic totient inverse-zeta carrier)

    =

safe first-order logarithmic differential operator applied to
(the same analytic totient carrier).
```

Thus the prime Type-II problem and the Möbius/Farey local-to-Bohr problem are not
merely RH-equivalent. They are two realizations of one differential source.

The coefficient-side Selberg gauge in `L-15443` removes `zeta` by multiplication.
Equation (L-15447.7) describes the complementary physical operation: division
by `zeta` is carried by `U`, while the prime numerator is an explicit safe
differential image.

## 6. Norm consequence

Fix a closed strip

\[
 {1\over2}+\delta\le\Re s\le1-\delta.
\]

Because `A` has polynomial vertical growth, any local Sobolev estimate controlling
both `U` and `U'` on that strip controls the joint source `mathcal Q U` through
(L-15447.7). Conversely, an off-line zero makes every such estimate fail at its
horizontal coordinate by (L-15447.10).

The required estimate is therefore a **local trace estimate for one inverse-zeta
carrier**, not two independent prime and Möbius cancellation theorems.

## 7. Relationship to the proposed completion

`L-15448` supplies the proposed critical local-to-Bohr estimate for the complete
Möbius–Bernoulli realization of `U`. `T-15414` consumes that estimate through
PR #226's Mellin theorem and obtains RH. Equation (L-15447.7) then gives an
independent replay through the dyadic prime/Selberg route.

## 8. Proof boundary

Closed exactly:

- the logarithmic derivative calculation;
- the joint identity (L-15447.7);
- open-strip safety of `A`;
- the pole-order and multiplicity ledger;
- the identification of the common inverse-zeta source.

Not supplied by this lemma:

- a critical local Sobolev/second-moment estimate for `U`;
- the determinant cancellation theorem of `L-15448`;
- RH.
