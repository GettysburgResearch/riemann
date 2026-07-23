# L-4702 — Derivative-free complete-Bernstein divided differences for xi

Claim ID: L-4702  
Title: Under RH every finite divided difference of the horizontal xi response has an alternating sign  
Status: PROPOSED  
Authoring agent: `gpt56-05-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-3201; L-4701  
Scope: finite value-only xi inequalities at one height  
Related counterexample candidates: none

## Statement

Use the notation of L-4701. For fixed real `T`, define

\[
 J_T(u)=\sqrt u\,\operatorname{Re}F\!\left(\frac12+\sqrt u+iT\right),
 \qquad u>0.
\]

For pairwise distinct positive nodes `u_0,...,u_n`, let
`[u_0,...,u_n]J_T` denote the ordinary divided difference. If RH holds, then
for every `n>=1`,

\[
 \boxed{
 (-1)^{n-1}[u_0,\ldots,u_n]J_T
 =\sum_\gamma
 \frac{(T-\gamma)^2}
 {\prod_{k=0}^{n}\{u_k+(T-\gamma)^2\}}
 \ge0.
 }
\]

Thus any exact finite node set and rigorous value enclosures proving the
opposite strict sign give a finite unconditional counterexample witness to RH.
No derivative of `xi`, `zeta`, or `F` is needed.

The first cases are:

1. **Monotonicity** (`n=1`): for `u_0<u_1`,
   \[
   J_T(u_1)\ge J_T(u_0).
   \]
2. **Concavity** (`n=2`): for `u_0<u_1<u_2`,
   \[
   [u_0,u_1,u_2]J_T\le0.
   \]
   Equivalently, consecutive secant slopes decrease after the appropriate
   unequal-step normalization.
3. **Third-order sign** (`n=3`):
   \[
   [u_0,u_1,u_2,u_3]J_T\ge0.
   \]

When all nodes coalesce to `u`, the hierarchy becomes

\[
 (-1)^{n-1}J_T^{(n)}(u)\ge0.
\]

In particular, the `n=1` confluent inequality is exactly half of the L-4101
right-side differential inequality.

## Definitions

Divided differences are defined recursively by

\[
 [u_0]f=f(u_0),
\]

and

\[
 [u_0,\ldots,u_n]f
 =\frac{[u_1,\ldots,u_n]f-[u_0,\ldots,u_{n-1}]f}
 {u_n-u_0}.
\]

For distinct nodes the value is symmetric in the nodes, although a certificate
should store them in increasing order to make its sign convention auditable.

## Motivation

The two-point witness of L-4701 is existentially complete, but a coarse grid can
miss a narrow interval on which `J_T` actually decreases. Higher finite
differences can expose curvature or higher-order oscillation while every
sampled first secant remains positive.

The hierarchy is also a derivative-free consistency ladder for the Stieltjes
moment matrices in L-4102. It lets a high-height implementation begin with only
repeated value evaluations and add expensive jets later.

## Proof

Assume RH. L-4701 gives

\[
 J_T(u)=\sum_\gamma f_{a_\gamma}(u),
 \qquad
 f_a(u)=\frac{u}{u+a},
 \qquad
 a_\gamma=(T-\gamma)^2\ge0.
\]

For `n>=1`, write

\[
 f_a(u)=1-\frac{a}{u+a}.
\]

The constant has zero divided differences of positive order. The reciprocal
kernel has the elementary identity

\[
 [u_0,\ldots,u_n]\frac1{u+a}
 =\frac{(-1)^n}{\prod_{k=0}^{n}(u_k+a)}.
\]

This may be proved by induction from the recursive definition or by the partial
fraction formula for divided differences. Therefore

\[
 [u_0,\ldots,u_n]f_a
 =\frac{(-1)^{n-1}a}{\prod_{k=0}^{n}(u_k+a)}.
\]

Apply this to `a=a_gamma` and sum. For `n=1`, the summand is
`O((T-gamma)^-2)`; for larger `n` it decays still faster. Hence the series is
absolutely convergent, and the identity follows either term by term or by
passing to the limit from finite symmetric zero truncations. Every term on the
right after multiplication by `(-1)^(n-1)` is nonnegative.

The confluent form follows from the standard limit

\[
 \lim_{u_0,\ldots,u_n\to u}[u_0,\ldots,u_n]f
 =\frac{f^{(n)}(u)}{n!}.
\]

The positive factor `n!` does not affect the sign.

## Exact certificate reduction

Choose exact positive dyadic offsets `x_k` and put `u_k=x_k^2`. A producer
computes balls

\[
 R_k\ni\operatorname{Re}F\!\left(\frac12+x_k+iT\right)
\]

and therefore

\[
 J_k=x_kR_k.
\]

Every divided difference is a fixed rational linear combination

\[
 [u_0,\ldots,u_n]J_T
 =\sum_{k=0}^{n}
 \frac{J_T(u_k)}{\prod_{r\ne k}(u_k-u_r)}.
\]

The independent checker reconstructs these exact rational coefficients and
performs outward interval addition. It accepts a counterexample witness only
when the interval for

\[
 (-1)^{n-1}[u_0,\ldots,u_n]J_T
\]

has upper endpoint strictly below zero.

## Analytic domain audit

- Every point lies in `Re(s)>1/2` and is separately proved zero-free before
  evaluating `F`.
- All nodes `u_k` are positive real numbers; the positive square root is used.
- Nodes must be distinct. Repeated nodes belong to a confluent jet certificate,
  not the value-only schema.
- The RH proof uses an absolutely convergent zero-resolvent sum after one or
  more divided differences.
- No branch cut, contour, or numerical differentiation occurs.

## Dependency audit

- D-3201 fixes the completed xi normalization.
- L-4701 supplies the RH representation of `J_T` and proves the first-order
  case and the off-line local geometry.
- The only new algebra is the exact divided difference of `(u+a)^-1`.

## Gap audit

1. The RH sign is `(-1)^(n-1)`, not `(-1)^n`.
2. The nodes are squared horizontal offsets; applying the same formula directly
   in `x` is incorrect.
3. Unequal node spacing requires true divided differences, not an unnormalized
   finite-difference stencil.
4. Alternating interval coefficients create cancellation; precision must be
   escalated until the final sign separates or the result remains unresolved.
5. A high-order violation in a surrogate or truncated zero list is not a xi
   certificate.
6. This hierarchy does not assert that any predetermined finite grid detects
   every RH failure. Existential completeness comes from its `n=1` member.

## Adversarial tests

1. For finite on-line zero multisets, compare every order through at least four
   against the explicit positive sum in the statement.
2. Use nonuniform nodes and verify the barycentric and recursive formulas agree
   exactly.
3. Reverse two nodes in serialized data and require rejection rather than an
   implicit sort.
4. Use the off-line synthetic quartet from X-4701 and require positive scalar
   values but a second divided difference with the forbidden positive sign.
5. Coalesce nodes at increasing precision and compare with the L-4101/L-4102
   jet formulas.
6. Widen one input ball until the alternating sum overlaps zero and require
   `UNRESOLVED`.

## Remaining uncertainty

No algebraic gap is known. Practical conditioning worsens rapidly when nodes
are close or the order is high; low orders should be attempted before generic
large divided-difference searches.

## Suggested next attack

Add orders one through three to the Issue #39 value-only Arb producer. Search
adaptively in `u`: monotonicity first, concavity second, and only then higher
orders. Store exact barycentric coefficients so an independent checker never
trusts the producer's finite-difference implementation.
