# L-9702 — Support-gap Hausdorff witnesses after complete slab deflation

Claim ID: `L-9702`  
Title: A completely deflated zero slab forces a Hausdorff moment cone and a three-value support-gap inequality for the residual direct-`xi` logarithmic modulus  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-7501`; the complete slab-isolation interface of `L-9701`; standard completed-`xi` symmetries  
Scope: support-aware finite RH witnesses after all critical-line zeros in one exact ordinate slab have been removed  
Related counterexample candidates: none

## Namespace note

This theorem was initially drafted as `L-9307`. Concurrent PR #103 had already
allocated that identifier. The mathematics is unchanged; `L-9702` is the stable
identifier.

## Statement

Fix exact real numbers

\[
 a<T<b
\]

such that the slab endpoints are not zero ordinates. Suppose a proof-grade,
multiplicity-aware total count together with proof-grade critical-line
isolation has certified the complete multiset `J` of all nontrivial zeros whose
ordinates lie in `(a,b)`. For `u>=0`, put

\[
 H_T(u)=\left|\xi\!\left(\frac12+\sqrt u+iT\right)\right|^2
\]

and define

\[
 R_T(u)=\log H_T(u)
 -\sum_{\gamma\in J}m_\gamma
  \log\!\left(u+(T-\gamma)^2\right).
\tag{L-9702.1}
\]

Set

\[
 A=\min\{(T-a)^2,(b-T)^2\}>0.
\tag{L-9702.2}
\]

Assume RH. Then every remaining zero ordinate satisfies

\[
 (T-\gamma)^2\ge A.
\]

The following hold.

### 1. Support-gap representation

Up to an additive real constant,

\[
 R_T(u)=C+\sum_{\gamma\notin J}m_\gamma
 \log\!\left(u+(T-\gamma)^2\right),
\tag{L-9702.3}
\]

where every squared distance in the sum is at least `A`.

### 2. Three-value support-gap chord

For

\[
 0\le u_0<u_1<u_2,
\]

put

\[
 S=u_0+A,
 \qquad
 L_j=\log\!\left(1+\frac{u_j-u_0}{S}\right),
 \quad j=1,2.
\]

Then

\[
 \boxed{
 L_1\bigl(R_T(u_2)-R_T(u_0)\bigr)
 -L_2\bigl(R_T(u_1)-R_T(u_0)\bigr)
 \ge0.}
\tag{L-9702.4}
\]

This uses three residual values and no derivative or division by `xi`.

### 3. Hausdorff moment hierarchy

Fix `u_0>=0` and put `S=u_0+A`. For `n>=1`, define

\[
 M_n(u_0)=\frac{(-1)^{n+1}}{(n-1)!}R_T^{(n)}(u_0),
 \qquad
 B_n(u_0)=S^nM_n(u_0).
\tag{L-9702.5}
\]

There is a finite positive measure `nu` on `[0,1]` such that

\[
 B_{r+1}(u_0)=\int_0^1q^r\,d\nu(q),
 \qquad r\ge0.
\tag{L-9702.6}
\]

Consequently, for every `r,k>=0`,

\[
 \boxed{
 \sum_{j=0}^{k}(-1)^j\binom{k}{j}B_{r+1+j}(u_0)\ge0,}
\tag{L-9702.7}
\]

and for every finite real vector `c=(c_0,...,c_d)`,

\[
 \boxed{
 \sum_{i,j=0}^{d}c_ic_jB_{r+1+i+j}(u_0)\ge0,}
\tag{L-9702.8}
\]

\[
 \boxed{
 \sum_{i,j=0}^{d}c_ic_j
 \left(B_{r+1+i+j}(u_0)-B_{r+2+i+j}(u_0)\right)\ge0.}
\tag{L-9702.9}
\]

The first support ratio is

\[
 \boxed{
 (-1)^{n+1}
 \left(nR_T^{(n)}(u_0)+(u_0+A)R_T^{(n+1)}(u_0)\right)
 \ge0.}
\tag{L-9702.10}
\]

A strict directed violation of any displayed inequality is a finite RH-disproof
witness after the complete-slab, selected-factor, normalization, and
independent-reproduction gates.

## Proof of the support representation

Under RH, `L-7501` supplies, up to an additive constant,

\[
 \log H_T(u)=C+\sum_\gamma m_\gamma
 \log\!\left(u+(T-\gamma)^2\right).
\]

Subtracting every factor whose ordinate lies in `(a,b)` gives (L-9702.3). Every
remaining ordinate satisfies `gamma<=a` or `gamma>=b`, so

\[
 |T-\gamma|\ge\min\{T-a,b-T\},
\]

which proves the support lower bound.

## Proof of the chord inequality

Fix one residual squared distance `y>=A`. Put

\[
 p=u_1-u_0,
 \qquad
 q=u_2-u_0,
 \qquad0<p<q.
\]

For `x>0`, define

\[
 r(x)=\frac{\log(1+px)}{\log(1+qx)}.
\]

Its derivative has the sign of

\[
 p(1+qx)\log(1+qx)-q(1+px)\log(1+px).
\]

Let

\[
 F(z)=\frac{(1+z)\log(1+z)}z.
\]

Since

\[
 F'(z)=\frac{z-\log(1+z)}{z^2}>0,
\]

the derivative numerator equals

\[
 pqx\bigl(F(qx)-F(px)\bigr)>0.
\]

Thus `r` is increasing. Taking

\[
 x=\frac1{u_0+y}\le\frac1{u_0+A}
\]

gives

\[
 \frac{\log(1+p/(u_0+y))}{\log(1+q/(u_0+y))}
 \le\frac{L_1}{L_2}.
\]

After clearing positive denominators, the contribution of this factor to
(L-9702.4) is nonnegative. Summing over all residual factors proves the chord
inequality.

## Proof of the Hausdorff hierarchy

Differentiating (L-9702.3) gives

\[
 M_n(u_0)=\sum_{\gamma\notin J}
 \frac{m_\gamma}{(u_0+(T-\gamma)^2)^n}.
\]

For every remaining zero define

\[
 q_\gamma=\frac{u_0+A}{u_0+(T-\gamma)^2}\in(0,1].
\]

Then

\[
 B_n(u_0)=\sum_{\gamma\notin J}m_\gamma q_\gamma^n.
\]

The finite positive measure

\[
 \nu=\sum_{\gamma\notin J}m_\gamma q_\gamma\,\delta_{q_\gamma}
\]

satisfies (L-9702.6). Hence

\[
 \sum_{j=0}^k(-1)^j\binom{k}{j}B_{r+1+j}
 =\int_0^1q^r(1-q)^k\,d\nu(q)\ge0,
\]

and

\[
 \sum_{i,j}c_ic_jB_{r+1+i+j}
 =\int_0^1q^r\left|\sum_i c_iq^i\right|^2d\nu(q)\ge0.
\]

Multiplying the integrand by `1-q` proves (L-9702.9). The scalar case
`B_n-B_{n+1}>=0` is equivalent to (L-9702.10). QED.

## Strict separation from ordinary Stieltjes positivity

Take

\[
 A=1,
 \qquad
 R(u)=\log\!\left(u+\frac12\right).
\]

This is an ordinary positive Stieltjes logarithmic factor, but its mass lies at
`1/2<A`. At `(u_0,u_1,u_2)=(0,1,2)`,

\[
 \log2\log5-(\log3)^2<0.
\]

Also `B_n=2^n`, so `B_1-B_2=-2`, while the ordinary Hankel moment matrix is
rank-one positive semidefinite. Thus the support-aware cone is strictly smaller
than the ordinary Stieltjes cone.

## Certificate architecture

A value-only certificate carries

```text
exact slab endpoints and target
complete slab count/isolation digests
support lower bound A
exact nodes
residual logarithm intervals
outward L1 and L2 intervals
final chord interval.
```

A derivative certificate additionally carries the directed logarithmic jet and
exact rational Rayleigh vectors. Shared primitive uncertainty must remain shared
through every contraction.

## Analytic domain audit

- `xi` is entire with the standard normalization.
- Selected factors have positive real arguments at all declared nodes.
- The slab count is multiplicity-aware and every slab factor is removed exactly
  once.
- No division by `xi`, complex logarithm branch, contour deformation, or
  numerical zero assumption occurs in the finite checker.

## Dependency audit

- `L-7501` supplies the RH-conditional genus-zero product.
- `L-9701` supplies one route to a complete slab factor table.
- The support chord and Hausdorff proofs are contained here.

## Gap audit

- A partial zero list does not justify the support bound.
- Approximate ordinates are not proof-grade factors.
- `A` must be a proved lower bound; rounding it upward is unsound.
- Negative rows under partial deflation are expected and are not counterexamples.
- Wide selected-factor intervals may make a correct row unresolved.
- Positive finite tables prove no global statement.

## Adversarial tests

1. A factor at `y=A` gives zero chord response.
2. A factor at `y>A` gives positive response.
3. A factor at `0<y<A` violates the support chord while ordinary Stieltjes
   positivity passes.
4. Missing or duplicated slab factors invalidate the complete-support gate.
5. Any derivative interval crossing zero remains unresolved.

## Remaining uncertainty

No directed Riemann-`xi` support-residual row has yet been preserved. Ordinary
natural-scale PR71 reconnaissance is positive.

## Suggested next attack

The cheaper `L-9703` count-only chord should be run first on every exact slab.
Use complete factor removal and the Hausdorff hierarchy only for slabs whose
count-only margin is unusually small.