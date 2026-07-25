# L-2816 — Segment-centered algebraic enclosure of `q^{-1/2}`

Claim ID: L-2816  
Title: One square root per integer segment suffices for every prime amplitude in that segment  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: binomial series; L-2815; L-2806 fixed-vector scalarization  
Scope: high-cutoff complete directed carrier prime sums  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Let `m,q>0`, put

\[
 y=\frac{q-m}{m},
\]

and suppose `|y|<=beta<1`. Define

\[
 c_k=(-1)^k\frac{\binom{2k}{k}}{4^k}
\]

and

\[
 S_J(y)=\sum_{k=0}^{J}c_k y^k.
\]

Then

\[
 \boxed{
 \frac1{\sqrt q}
 =\frac1{\sqrt m}\left(S_J(y)+E_J(y)\right)
 }
\]

with the elementary enclosure

\[
 \boxed{
 |E_J(y)|\le\frac{\beta^{J+1}}{1-\beta}.
 }
\]

Consequently, one directed enclosure of `m^{-1/2}` per integer segment, followed by algebraic interval evaluation of `S_J`, encloses every `q^{-1/2}` in the segment without evaluating a square root at `q`.

## Target specialization

For the unfinished PR #65 ranges `2000:4900`, use segment size

\[
 H=20{,}000{,}000
\]

and the integer midpoint `m` of each segment. Since every such segment lies above `4*10^10`,

\[
 |y|<\frac1{4000}.
\]

With `J=5`,

\[
 \boxed{
 |E_5(y)|
 <\frac{1}{4000^6(1-1/4000)}.
 }
\]

Because `m>4*10^10`, one has `m^{-1/2}<1/200000`. Thus the absolute reciprocal-square-root truncation is below

\[
 \frac{1}{200000\,4000^6(1-1/4000)}.
\]

For the target fixed vector, use the safe bounds

\[
 |\rho_q|<2,
 \qquad
 \frac{\log q}{\pi}<9,
 \qquad
 \#\{q\le10^{11}\}<10^{11}.
\]

Even if this high-segment approximation were pessimistically charged to every integer below the cutoff, the total resulting prime-Rayleigh uncertainty would be less than

\[
 \boxed{10^{-14}.}
\]

The actual missing ordinary-prime count is far smaller, so this is deliberately loose.

## Proof

The binomial series gives, for `|y|<1`,

\[
 (1+y)^{-1/2}
 =\sum_{k=0}^{\infty}
 (-1)^k\frac{\binom{2k}{k}}{4^k}y^k.
\]

The central-binomial estimate

\[
 \binom{2k}{k}\le4^k
\]

implies `|c_k|<=1`. Therefore

\[
 |E_J(y)|
 \le\sum_{k=J+1}^{\infty}|y|^k
 \le\frac{\beta^{J+1}}{1-\beta}.
\]

Since `q=m(1+y)`, multiplication by `m^{-1/2}` proves the first statement.

For the target segments, `|q-m|<=10^7` and `m>4*10^10`, so `|y|<1/4000`. Substituting `J=5` proves the displayed local bound. The total fixed-vector contribution from a reciprocal-square-root perturbation `epsilon_q` is at most

\[
 \sum_q \frac{\log q}{\pi}|\rho_q||\epsilon_q|.
\]

Applying the stated crude target bounds yields

\[
 10^{11}\cdot9\cdot2\cdot
 \frac{1}{200000\,4000^6(1-1/4000)}
 <10^{-14},
\]

verified by exact integer cross multiplication in X-2815.

## Combined amplitude enclosure

For ordinary primes in the unfinished ranges,

\[
 b_q=\frac{\log q}{\pi\sqrt q}.
\]

A producer combines:

1. L-2815's directed segment-centered interval for `log(q)`;
2. this lemma's directed interval for `q^{-1/2}`;
3. one directed enclosure of `pi^{-1}` shared by the shard.

Outward interval multiplication directly encloses `b_q`; no separate first-order error linearization is permitted or needed.

## Gap audit

- The coefficients must be represented exactly or outwardly enclosed.
- The precomputed `m^{-1/2}` must itself be directed.
- The coarse geometric remainder is valid on both sides of the midpoint; an alternating-series one-sided shortcut is not used.
- Higher prime powers use `log(p)` rather than `log(q)` in the amplitude. They are already contained in the completed direct shard and are outside this specialization.
- This lemma does not control phase-grid Taylor truncation; L-2813 supplies that separate budget.

## Adversarial tests

1. Test positive and negative `y` at the segment endpoints.
2. Compare against direct high-precision square roots for random target integers.
3. Mutate `J=5` to `J=4` and require the claimed target `10^-14` aggregate moat to fail if its exact inequality no longer holds.
4. Deliberately use `m<=4*10^10` and require the target specialization to reject it.
5. Widen the midpoint-square-root interval and verify inclusion remains monotone.

## Suggested next attack

Implement L-2815 and L-2816 in one drop-in algebraic evaluator. Retain the direct MPFR evaluator as a fallback for phase-bin or deposition-knot ambiguity and as an independent complete-small-cutoff control.