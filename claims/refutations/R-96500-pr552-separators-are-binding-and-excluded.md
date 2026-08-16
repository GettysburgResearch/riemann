# R-96500 — The PR #552 fixed-product and rough-reservoir separators are binding

Claim ID: `R-96500`  
Status: **PROVED EXACT FIREWALL / ROUTE EXCLUSION**  
Created: 2026-08-17  
Frozen source: PR #552 at `81df9c3f507aba0e5f21187044583a0d6fb90db9`

## 1. Fixed-product scope

For one physical product `n=dm`, every factorization has logarithmic knot

\[
\log d+\log m=\log n.
\]

Hence a divisor cube at fixed `n` may cancel equal-knot atoms, but it cannot
produce a nontrivial convex packet supported at `a<b<c`. Any proof that invokes
three-knot convexity while claiming never to mix physical products is invalid.

## 2. Rough-reservoir counterexample

The proposed lower bound

\[
\sum_{\substack{u\le m<pu\\(m,P)=1}}m^{-1/2}
\ge 2\sqrt u(\sqrt p-1)
\tag{R-96500.1}
\]

is false. At

\[
P=30,\qquad p=5,\qquad u=2,
\]

the only integer in `[2,10)` coprime to 30 is 7. Thus the left side is
`1/sqrt(7)<1/2`, while

\[
2\sqrt2(\sqrt5-1)
>2\cdot {4\over3}\cdot {6\over5}
={16\over5}>3.
\]

No averaged density heuristic repairs this pointwise failure.

## 3. Binding exclusion

`T-96500` is invalid if it uses either:

```text
fixed-product cross-knot convexity;
rough-prefix density or a rough-block lower bound;
positive realization of an oriented child row;
physical Y4 slack as the complete arithmetic gap.
```

The successor uses none of them. Its only rough-prime inequality is the local
coefficient identity

\[
\sum_i\alpha_i<67^{-1/2}<1/8,
\]

which follows from ordered scalar weights and not from the population of rough
integers.
