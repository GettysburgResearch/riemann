# L-2815 — Segment-centered algebraic enclosure of `log(q)`

Claim ID: L-2815  
Title: One logarithm per integer segment suffices for every prime phase in that segment  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: elementary atanh series; L-2806 fixed-vector scalarization; L-2813 phase-grid compression  
Scope: high-cutoff complete directed carrier prime sums  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Let `m` and `q` be positive integers and suppose

\[
 |q-m|\le h<m.
\]

Put

\[
 z=\frac{q-m}{q+m},
 \qquad
 \zeta=\frac{h}{2m-h}<1.
\]

For every integer `J>=0`, define

\[
 L_J(q;m)=\log m+2\sum_{j=0}^{J}\frac{z^{2j+1}}{2j+1}.
\]

Then

\[
 \boxed{
 \log q=L_J(q;m)+R_J(q;m)
 }
\]

with

\[
 \boxed{
 |R_J(q;m)|
 \le
 \frac{2\zeta^{2J+3}}
 {(2J+3)(1-\zeta^2)}.
 }
\]

The sign of `R_J` is the sign of `q-m`. In particular, if an outward interval encloses `log(m)` and all rational operations in `L_J`, adding the displayed signed or symmetric rational remainder yields an outward enclosure of `log(q)` without evaluating a logarithm at `q`.

For a rational carrier `T`, the phase enclosure obeys

\[
 |T\log q-TL_J(q;m)|
 \le |T|\frac{2\zeta^{2J+3}}
 {(2J+3)(1-\zeta^2)}.
\]

## Target specialization

The unfinished direct-MPFR ranges on PR #65 are the ordinary-prime segments

```text
segment indices 2000 through 4899
segment size    20,000,000
q               >= 40,000,000,002
```

For each segment choose its integer midpoint `m`; then `h<=10,000,000` and

\[
 \zeta<\frac1{8000}.
\]

With `J=3`,

\[
 |R_3|<
 \frac{2}{9\,8000^9(1-8000^{-2})}.
\]

At the exact target carrier

\[
 T=\frac{94184072727073}{20}<5\cdot10^{12},
\]

this gives the strict rational phase bound

\[
 \boxed{
 |T R_3|<10^{-23}.
 }
\]

Thus four odd atanh terms per prime replace one MPFR logarithm while introducing a phase uncertainty far below the target-wide phase-grid and nonprime budgets.

## Proof

The identity

\[
 \log q-\log m
 =\log\frac{1+z}{1-z}
 =2\operatorname{atanh}z
 =2\sum_{j=0}^{\infty}\frac{z^{2j+1}}{2j+1}
\]

holds for `|z|<1`. The omitted tail has the same sign as `z`, hence as `q-m`. Taking absolute values and using `|z|<=zeta`,

\[
 |R_J|
 \le 2\sum_{j=J+1}^{\infty}
 \frac{\zeta^{2j+1}}{2j+1}
 \le
 \frac{2\zeta^{2J+3}}{2J+3}
 \sum_{r=0}^{\infty}\zeta^{2r},
\]

which is the claimed bound.

For a segment `[a,a+H)`, choose `m=a+floor(H/2)`. Then `|q-m|<=ceil(H/2)`. At the first unfinished target segment,

\[
 q+m>80{,}000{,}000{,}000,
 \qquad
 |q-m|\le10{,}000{,}000,
\]

so `|z|<1/8000`; every later segment is better. Substitution of `J=3` and `T<5*10^12` proves the target phase inequality by integer cross multiplication.

## Algorithmic consequence

A producer may compute one directed `log(m)` per integer segment. Each prime then requires only directed additions, multiplications, and divisions for four rational odd powers. The same enclosure supplies:

- the carrier phase `T log(q)`;
- the support coordinate `K log(q)/log(c)`;
- the amplitude numerator `log(q)` for ordinary primes.

If the support-coordinate interval crosses a deposition knot or the phase interval crosses a phase-grid boundary, the producer must hull both assignments or fall back to the direct MPFR evaluator.

## Gap audit

- The lemma removes per-prime logarithms, not interval arithmetic.
- `log(m)` itself still needs one trusted directed evaluation per segment.
- The implementation must preserve the sign of the remainder or use a symmetric hull.
- A midpoint bin assignment is invalid if the phase interval intersects a grid boundary.
- Higher prime powers are already contained in the completed `0:100` shard and need not use this specialization.

## Adversarial tests

1. Test both sides of the segment midpoint so the signed remainder changes direction.
2. Test both segment endpoints, including the half-open upper endpoint convention.
3. Compare the enclosure with a direct high-precision logarithm for random integers.
4. Mutate `J=3` to `J=2` and require the target `10^-23` phase claim to fail.
5. Force a phase-grid boundary overlap and require fallback rather than midpoint assignment.

## Suggested next attack

Combine this logarithm enclosure with L-2816's reciprocal-square-root series and L-2813's `M=32768,R=3` phase grid. Use the already completed direct shards for ranges `0:2000` and `4900:5000`, and run only ranges `2000:4900` through the algebraic producer.