# L-9802 — Critical-point certificates for rational cross-height portfolios

Claim ID: `L-9802`  
Title: A low-degree derivative numerator and rigorous critical-value bounds certify rational cross-height logarithmic direct-`xi` portfolios  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-7501`; the standard completed-`xi` normalization and symmetries  
Scope: cross-height direct completed-`xi` portfolios with rational coefficients  
Related counterexample candidates: `O-9802` and the `X-9802` sharp PR #105 response

## Motivation

`L-9801` proves a cross-height direct-`xi` product inequality by clearing all
integer exponents into one polynomial `A-B`. That is ideal for small exponent
vectors. It becomes inefficient when a valid response consists of one nearly
boundary same-height row plus tiny rational repairs from other heights: clearing
denominators can create a polynomial of enormous degree even though the
underlying logarithmic response has only a few distinct quadratic factors.

This lemma replaces exponent clearing by a critical-point certificate. With `m`
distinct sampled height/node pairs, the derivative numerator has degree at most
`2m-1`, independent of coefficient denominators or magnitudes.

## Statement

For exact real heights `T_r`, positive rational nodes `u_{rj}>0`, and exact
rational coefficients `beta_{rj}`, suppose

\[
 \boxed{\sum_j\beta_{rj}=0\qquad\text{for every height }r.}
\tag{L-9802.1}
\]

Put

\[
 Q_{rj}(x)=(x-T_r)^2+u_{rj}>0,
\]

and define the one-zero response

\[
 \phi_\beta(x)=
 \sum_{r,j}\beta_{rj}\log Q_{rj}(x).
\tag{L-9802.2}
\]

Let the product range only over the distinct pairs with nonzero coefficient:

\[
 D(x)=\prod_{r,j}Q_{rj}(x)>0,
\]

and define the exact rational derivative numerator

\[
 \boxed{
 P_\beta(x)=
 D(x)\phi_\beta'(x)
 =\sum_{r,j}
  2\beta_{rj}(x-T_r)
  \prod_{(a,b)\ne(r,j)}Q_{ab}(x).}
\tag{L-9802.3}
\]

Suppose either `P_beta` is identically zero, or an exact certificate supplies
pairwise-disjoint rational intervals

\[
 I_1,\ldots,I_s
\]

such that:

1. each `I_k` contains exactly one distinct real root of `P_beta`;
2. the intervals account for every distinct real root of `P_beta`;
3. directed rational logarithm arithmetic proves
   \[
      \inf_{x\in I_k}\phi_\beta(x)\ge0
      \qquad(1\le k\le s).
   \]

Then

\[
 \boxed{\phi_\beta(x)\ge0\qquad(x\in\mathbb R).}
\tag{L-9802.4}
\]

For real `T`, write

\[
 H_T(u)=
 \left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2.
\]

Under RH, (L-9802.4) implies the finite logarithmic portfolio inequality

\[
 \boxed{
 R_\beta:=
 \sum_{r,j}\beta_{rj}\log H_{T_r}(u_{rj})\ge0.}
\tag{L-9802.5}
\]

Thus a strict directed interval with upper endpoint below zero is a finite
RH-disproof witness, subject to independent direct-`xi`, normalization, and
analytic review.

## Proof of the global response criterion

Every `Q_{rj}` is strictly positive on the real line, so `phi_beta` is smooth and

\[
 \phi_\beta'(x)=\frac{P_\beta(x)}{D(x)}.
\]

Condition (L-9802.1) gives

\[
 \phi_\beta(x)\longrightarrow0
 \qquad(x\to+\infty\text{ or }x\to-\infty).
\tag{L-9802.6}
\]

Indeed, at each fixed height,

\[
 \log((x-T)^2+u)=2\log|x|+O(x^{-1}),
\]

and the common `2 log|x|` term cancels. If `P_beta` is identically zero, then
`phi_beta` is constant; (L-9802.6) forces it to be zero.

Otherwise, between consecutive real roots of `P_beta`, the derivative has a
constant sign because `D>0`. Hence `phi_beta` is monotone on every such
component. Its minimum on the compactified real line is therefore attained at a
real critical point or at one of the two infinities. The critical-point lower
bounds and (L-9802.6) prove (L-9802.4).

## Proof of the direct-`xi` consequence

Under RH, `L-7501` gives, up to one additive constant `C_r` at every height,

\[
 \log H_{T_r}(u)
 =C_r+\sum_\gamma m_\gamma
  \log\bigl((T_r-\gamma)^2+u\bigr).
\]

The constant `C_r` vanishes after contraction by (L-9802.1). The resulting zero
sum is absolutely convergent: the per-height zero-sum condition cancels the
constant logarithmic term, leaving `O(gamma^-2)` after the complete sum over
heights. Therefore

\[
 R_\beta
 =\sum_\gamma m_\gamma\phi_\beta(\gamma)\ge0,
\]

which proves (L-9802.5). QED.

## Exact critical-point proof object

The `X-9802` checker requires:

```text
exact origin, heights, positive nodes and rational coefficients
one zero-sum identity per height
exact coefficients of P_beta, reconstructed rather than trusted
pairwise-disjoint rational root intervals
an exact Sturm count of one root in every interval
an exact Sturm count proving the intervals exhaust all real roots
positive rational enclosures of every Q_rj over every root interval
self-contained rational logarithm enclosures
strict or nonnegative lower bounds for every critical response
```

The Sturm sequence counts distinct roots, so repeated stationary points are
included once. Root-interval endpoints are rejected if they are themselves
roots.

For a rational interval `[a,b]`, the checker obtains the exact range of

\[
 (x-T)^2+u
\]

by testing the two endpoints and the vertex `x=T` when it lies in the interval.
The logarithm is enclosed by power-of-two range reduction and the positive
atanh series

\[
 \log y=2\sum_{k=0}^{M-1}
 \frac{z^{2k+1}}{2k+1}+E_M,
 \qquad z=\frac{y-1}{y+1},
\]

with an explicit geometric tail.

## Sharp exact PR #105 response

Use only the center and upper member of the exact PR #105 symmetric triple:

\[
 T_0=rac{20225875608341108140435}{2^{32}},
 \qquad T_+=T_0+\frac5{16},
\]

and nodes

\[
 u_1=2^{-20},\qquad u_2=2^{-12},\qquad u_3=2^{-10}.
\]

Take the integer coefficient vectors

\[
 \beta_0=(-23,46,-23),
\]

\[
 \beta_+=(-750746,1000000,-249254).
\tag{L-9802.7}
\]

Both sums are zero. The derivative numerator has degree nine and exactly five
real roots. `X-9802` isolates all five in dyadic intervals of width `3*2^-80`.
With 64 positive atanh terms, the directed critical response lower endpoints
are approximately

```text
+2.28114181033643
+0.413720542806542
+105.043422397344
+5.61061546295551
+3817480.25682095
```

in the integer normalization. Hence the one-zero response is strictly positive
on the entire real line.

The ordinary p256 midpoint contraction of the direct-`xi` data is

```text
integer row      +5.823585906012185...
normalized row   +5.823585906012185e-6
```

where normalization divides by `10^6`. This is positive and is not a
counterexample. It is, however, over six orders tighter than the first small
integer `L-9801` controls and is a useful boundary candidate for asymmetric
height/node continuation.

## Structural interpretation

The dominant upper-height vector is extremely close to the exact Jensen row

\[
 (-256,341,-85),
\]

because

\[
 2^{-12}=\frac{256}{341}2^{-20}
          +\frac{85}{341}2^{-10}.
\]

Concavity of `log(y+u)` makes that same-height row nonnegative. The small center
repair and small displacement from the Jensen weights reduce the observed
finite margin while preserving the full shared-zero response. This explains
why an unconstrained cross-height linear program found a near-null rather than
a robust negative.

## Relation to `L-9801`

When all coefficients have a small common denominator, multiplying through and
using `L-9801` is often the simplest certificate. `L-9802` is strictly more
practical for large denominator repairs: its derivative degree depends only on
the number of distinct height/node pairs, whereas the cleared product degree
depends on the total positive exponent.

`L-9802` does not enlarge the mathematical response cone beyond exact rational
logarithmic portfolios with globally nonnegative one-zero response. It enlarges
the tractable proof-object class.

## Analytic domain audit

- All logarithm arguments in the response are positive real quadratics.
- Every direct-`xi` node has `u>0`; no denominator or zero exclusion is used.
- The height-dependent canonical-product constant cancels separately at every
  height.
- Rational coefficients are permitted because (L-9802.5) is a linear logarithmic
  inequality; no branch of a rational power is formed.
- A common numerical scale at one height cancels only when it is point-independent
  and the exact coefficient sum there is zero.

## Gap audit

- A dense response grid is not a global certificate.
- Approximate derivative roots are not root isolators.
- Every distinct real derivative root must be accounted for, including repeated
  roots that do not change sign.
- A root interval whose response enclosure crosses zero is unresolved, not
  positive by its midpoint.
- The atanh truncation tail and power-of-two range reduction must be outward.
- A negative ordinary direct-`xi` contraction is not a witness.
- The sharp PR #105 row is positive; it is a boundary control and search seed.

## Suggested next attack

Search the complete rational tangent cone around the Jensen boundary row using
an exchange algorithm. Freeze the smallest candidates to dyadic coefficients,
run the exact derivative-root/critical-value checker, and then contract the
existing p192/p256 PR #105 primitives. Repeat on asymmetric height triples and
on the ordinates with the smallest normalized rows in PR #105.
