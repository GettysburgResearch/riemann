# L-7502 — Multiplicative xi-modulus hierarchy

Claim ID: L-7502  
Title: Under RH, the logarithm of the horizontal xi modulus has completely monotone derivative  
Status: PROPOSED  
Authoring agent: `gpt56-01-g`  
Created: 2026-07-25  
Dependencies: L-7501  
Scope: finite multiplicative completed-xi witnesses  
Related counterexample candidates: none

## Statement

Use `H_T` from L-7501. Assume RH. For every real `T` and `u>0`, put

\[
 G_T(u)=\log H_T(u).
\]

Then, for every integer `n>=1`,

\[
 \boxed{
 (-1)^{n-1}G_T^{(n)}(u)\ge0.}
\]

Equivalently, `G_T'` is completely monotone. Thus `G_T` is increasing and
concave, and its finite divided differences satisfy

\[
 (-1)^{n-1}[u_0,\ldots,u_n]G_T\ge0
\]

for every strictly increasing positive node list.

In particular, for

\[
 0<u_0<u_1<u_2,
\]

logarithmic concavity gives

\[
 (u_2-u_0)\log H_T(u_1)
 \ge
 (u_2-u_1)\log H_T(u_0)
 +(u_1-u_0)\log H_T(u_2).
\]

If the nodes are rational, choose a positive integer `D` such that

\[
 A=D(u_2-u_0),\quad
 B=D(u_2-u_1),\quad
 C=D(u_1-u_0)
\]

are positive integers. Then `A=B+C` and RH implies the entirely algebraic
multiplicative inequality

\[
 \boxed{
 H_T(u_1)^A\ge H_T(u_0)^B H_T(u_2)^C.}
\]

A rigorous strict reversal is a finite RH-disproof witness using three direct
completed-xi values and no logarithm in the final checker.

## Proof

Under RH, L-7501 gives

\[
 H_T(u)=C_Tu^{m_T}
 \prod_j\left(1+\frac{u}{a_j}\right)^{m_j},
 \qquad a_j>0.
\]

For `u>0`, logarithmic differentiation yields the absolutely and locally
uniformly convergent series

\[
 G_T'(u)=\frac{m_T}{u}+
 \sum_j\frac{m_j}{u+a_j}.
\]

Repeated differentiation gives

\[
 (-1)^{n-1}G_T^{(n)}(u)
 =(n-1)!\left\{
 \frac{m_T}{u^n}+
 \sum_j\frac{m_j}{(u+a_j)^n}
 \right\}\ge0.
\]

The divided-difference signs follow from the generalized mean-value theorem.
The three-point inequality is ordinary concavity. Exponentiating is legitimate
because every `H_T(u_j)` is strictly positive for `u_j>0` under RH. Clearing the
rational node denominators gives the integer-power form.

## Why this can outperform monotonicity

A broad horizontal sample may remain increasing even when it contains a small
local deformation caused by an off-line zero. Concavity and higher alternating
divided differences constrain the entire shape, not only endpoint order.
The integer-power form retains direct completed-xi primitive data and avoids
`xi'/xi` division.

## Directed certificate

For three exact dyadic positive offsets `x_j`, set `u_j=x_j^2` exactly. A proof
checker may either:

1. form positive intervals for `H_T(u_j)=|xi|^2`, raise them to the exact integer
   powers `A,B,C`, and prove
   \[
   \sup H_1^A<\inf(H_0^BH_2^C);
   \]
   or
2. enclose each real logarithm after proving its modulus interval has positive
   lower endpoint, and contract the rational concavity row.

The first route has a smaller logical surface. Exponentiation uses repeated
squaring with outward rational interval multiplication.

A common positive normalization `S(T)` cancels because `A=B+C`:

\[
 (S H_1)^A<(S H_0)^B(S H_2)^C
 \iff H_1^A<H_0^BH_2^C.
\]

Thus an arbitrary rigorously positive scale depending only on the common
ordinate may be used to improve serialization and conditioning.

## Existential relationship

The two-point witness of L-7501 is already existentially complete. Therefore the
three-point hierarchy is not needed for completeness. Its purpose is detection:
it may expose a forbidden deformation before a sampled endpoint pair reverses.

Near an off-line positive zero `u=d`, `log H_T(u)` tends to negative infinity,
so concavity and higher divided-difference constraints necessarily fail on
suitable nearby rational node sets.

## Analytic domain audit

- Nodes satisfy `u_j>0`, so `H_T(u_j)>0` under RH.
- The logarithm is the ordinary real logarithm of a positive real value.
- The series is locally uniformly convergent away from `u=0`.
- Integer-power certificate arithmetic introduces no transcendental operation.

## Gap audit

1. Large cleared exponents can make raw rational powers huge. Exact checker code
   should reduce common factors and use exponentiation by squaring.
2. A complex xi rectangle that includes zero cannot justify a positive lower
   modulus bound for a logarithmic checker; the direct integer-power route may
   still produce only a nonnegative interval and should fail closed.
3. The scale-cancellation rule requires the same positive factor at all three
   horizontal points.
4. A negative synthetic or modeled-zero inequality is not a Riemann-xi result.

## Adversarial tests

- Products `prod(u+a_j)` with positive rational `a_j` must satisfy the exact
  multiplicative inequality.
- The off-line dip model `(u-d)^2(u+a)` must violate a suitable node triple.
- Mutating `A=B+C` must make common-scale cancellation unavailable.
- An interval whose lower endpoint is zero must never be passed to a logarithm.

## Suggested next attack

For every direct-xi horizontal block, check in order:

1. two-point monotonicity from L-7501;
2. adjacent three-point integer-power log concavity;
3. higher alternating divided differences only around the smallest retained
   moats.
