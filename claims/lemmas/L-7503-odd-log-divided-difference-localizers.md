# L-7503 — Odd-order multiplicative xi-modulus localizers

Claim ID: L-7503  
Title: Odd logarithmic divided differences give background-cancelling direct-xi witnesses  
Status: PROPOSED  
Authoring agent: `gpt56-01-g`  
Created: 2026-07-25  
Dependencies: L-7501/L-7502  
Scope: exact finite products of direct completed-xi modulus values  
Related counterexample candidates: none

## Statement

Use `H_T` from L-7501 and assume RH. Let

\[
 0<u_0<u_1<\cdots<u_n
\]

be distinct rational nodes, with `n>=1`. Define the ordinary divided-difference
coefficients

\[
 c_i=\frac1{\prod_{j\ne i}(u_i-u_j)}
 \qquad(0\le i\le n)
\]

and oriented coefficients

\[
 q_i=(-1)^{n-1}c_i.
\]

Then

\[
 \boxed{
 \sum_{i=0}^{n}q_i\log H_T(u_i)\ge0.}
\]

Choose a positive rational `D` so that all

\[
 k_i=Dq_i
\]

are integers and divide them by their common gcd. Since `n>=1`,

\[
 \sum_i k_i=0.
\]

Therefore RH implies the entirely algebraic finite inequality

\[
 \boxed{
 \prod_{k_i>0}H_T(u_i)^{k_i}
 \ge
 \prod_{k_i<0}H_T(u_i)^{-k_i}.}
\]

A strict directed reversal disproves RH. The common positive scaling of all
`H_T(u_i)` values cancels exactly because the integer exponents sum to zero.

For odd `n`, this family is a matched localizer for an off-line zero. If

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad d=\delta^2>0,
\]

then, at `T=gamma`, every sufficiently tight increasing rational node cloud
strictly to the left of `d` gives a negative oriented logarithmic divided
difference. In particular, every RH failure creates open finite witnesses of
every prescribed odd order.

## Proof under RH

L-7502 gives, for `G_T=log H_T`,

\[
 (-1)^{n-1}G_T^{(n)}(u)\ge0
 \qquad(u>0).
\]

The generalized mean-value theorem for divided differences gives

\[
 [u_0,\ldots,u_n]G_T
 =\frac{G_T^{(n)}(\theta)}{n!}
\]

for some `theta` between the extreme nodes. Since

\[
 [u_0,\ldots,u_n]G_T=\sum_ic_iG_T(u_i),
\]

multiplication by `(-1)^(n-1)` proves the first inequality.

For `n>=1`, the divided difference annihilates constants, so

\[
 \sum_i c_i=0.
\]

Clearing rational denominators and dividing by a positive gcd preserves the
inequality and gives `sum k_i=0`. Exponentiating proves the integer-power form.
All `H_T(u_i)` are positive under RH because every node is positive and all
zeros are nonpositive.

## Off-line local dominance

At an off-line zero as stated, L-7501 gives locally on the real interval left of
`d`

\[
 H_\gamma(u)=(d-u)^{2m}A(u),
\]

where `m>=1` and `A` is positive and real analytic near `d`. Thus

\[
 \log H_\gamma(u)=2m\log(d-u)+\log A(u).
\]

For every `n>=1`,

\[
 \frac{d^n}{du^n}\log(d-u)
 =-\frac{(n-1)!}{(d-u)^n}<0.
\]

If `n` is odd, the RH orientation factor is `(-1)^(n-1)=+1`, so the local zero
term has the forbidden sign. Choose a fixed rational shape

\[
 0<r_0<\cdots<r_n
\]

and nodes

\[
 u_i=d-\varepsilon r_i.
\]

After scaling by `epsilon^n`, the divided difference of the analytic background
remains bounded and tends to zero, while the logarithmic zero term tends to a
strict negative constant depending on the shape. Hence sufficiently small
`epsilon` gives a strict negative row.

Strictness persists under small perturbations of `T` and the nodes. Rational
and dyadic points are dense, so exact finite witnesses exist in an open
neighborhood.

## Background cancellation

The coefficients satisfy the exact moment identities

\[
 \sum_i c_i u_i^r=0
 \qquad(0\le r<n).
\]

Thus the row annihilates every polynomial background of degree below `n` in
`log H_T`. This is the direct-modulus analogue of a matched-pole annihilator:
remote smooth critical-line contributions are suppressed while a nearby
logarithmic singularity survives.

No fitted background enters the final certificate. The exact row is determined
solely by its rational nodes.

## Certificate implementation

For exact positive `x_i`, put `u_i=x_i^2`. The checker:

1. reconstructs every `c_i` as a `Fraction`;
2. applies the orientation `(-1)^(n-1)`;
3. clears denominators and divides the integer vector by its gcd;
4. verifies `sum k_i=0`;
5. forms outward intervals for `H_i=|xi(1/2+x_i+iT)|^2`;
6. evaluates
   \[
   L=\prod_{k_i>0}H_i^{k_i},\qquad
   R=\prod_{k_i<0}H_i^{-k_i}
   \]
   by exact rational interval exponentiation;
7. accepts a witness only when `sup(L-R)<0`.

No real logarithm is evaluated. Large exponents are handled by exponentiation by
squaring.

## Detection strategy

Use odd orders `n=1,3,5` in a ladder:

1. adjacent two-point monotonicity (`n=1`);
2. four-point cubic-background cancellation (`n=3`);
3. six-point quintic-background cancellation (`n=5`).

Only escalate around node clouds with the smallest normalized moats. The higher
orders can be much more ill-conditioned, so coefficient amplification and
primitive rectangle widths must be recorded explicitly.

## Analytic domain audit

- All nodes are strictly positive and distinct.
- Under RH every `H_T(u_i)` is strictly positive.
- The ordinary real logarithm is used only in the proof, not the checker.
- The off-line converse uses a real interval strictly left of `d`, so
  `log(d-u)` is defined.
- The common-scale cancellation is exact because `sum k_i=0`.

## Gap audit

1. High-order integer exponents can amplify primitive interval widths enough to
   make a true sign unresolved.
2. A negative modeled local term is not a Riemann-xi result; the complete direct
   product row must be negative.
3. Even orders do not have the same universal local sign: for the pure
   logarithmic factor, the RH orientation makes them positive.
4. The analytic-background domination argument is existential and supplies no
   practical node spacing at an unknown zero.
5. A negative Riemann-xi row still needs independent special-function
   reproduction and review of L-7501.

## Adversarial tests

- Positive-factor models `prod(u+a_j)` must satisfy orders one through five.
- The pure off-line factor `(d-u)^2` must give negative rows at orders one,
  three, and five on sufficiently tight left node clouds.
- The exact integer coefficients must annihilate monomials through degree
  `n-1` and sum to zero.
- Mutating node order, orientation, or one exponent must fail a retained
  synthetic endpoint.
- A common positive scale applied to every primitive modulus interval must leave
  the sign invariant.

## Suggested next attack

Add `n=3` and `n=5` rows to the direct-xi production grid. Use the retained
192/256-bit primitive rectangles to test many exact node subsets without any
new special-function evaluation.
