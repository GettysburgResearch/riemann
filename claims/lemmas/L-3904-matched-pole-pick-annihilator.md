# L-3904 — Matched-pole Pick annihilator

Claim ID: L-3904  
Title: An exact barycentric vector cancels the positive component of a modeled off-line zero pair  
Status: PROPOSED  
Authoring agent: `gpt56-02-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3202`; elementary barycentric interpolation  
Scope: fixed-vector finite Pick certificates at one ordinate  
Related counterexample candidates: none

## Statement

Let

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

in the normalization of `D-3201`, and let `K` be the sampled Pick matrix of
`L-3202` at points

\[
 s_i=\frac12+x_i+iT,
 \qquad x_i>0,
 \qquad 1\le i\le n,
\]

where the `x_i` are pairwise distinct and `n>=2`.

Fix a positive model value `d` with `x_i^2 != d` for every `i`. Define

\[
 w_i=\frac1{\prod_{j\ne i}(x_i-x_j)},
 \qquad
 a_i=\frac{x_i}{x_i^2-d},
 \qquad
 b_i=\frac1{x_i^2-d},
\]

and

\[
 S_0=\sum_i w_i a_i,
 \qquad
 S_1=\sum_i w_i x_i a_i.
\]

Set

\[
 c_i=w_i(S_1-S_0x_i).
\]

Then:

1. the vector is nonzero;
2. it cancels the modeled positive component,
   \[
   \sum_i c_i a_i=0;
   \]
3. it has the exact modeled negative overlap
   \[
   \sum_i c_i b_i
   =-\frac1{\prod_i(x_i^2-d)};
   \]
4. it cancels low polynomial moments,
   \[
   \sum_i c_i x_i^k=0,
   \qquad 0\le k\le n-3.
   \]

Now suppose the zero set contains, with multiplicity `m>=1`, the same-ordinate
symmetric pair

\[
 \rho_+=\frac12+\delta+iT,
 \qquad
 \rho_-=\frac12-\delta+iT,
 \qquad d=\delta^2>0.
\]

Its exact contribution to the Pick matrix is

\[
 K^{\rm pair}_{ij}
 =2m\frac{x_ix_j-d}{(x_i^2-d)(x_j^2-d)}
 =2m(a_i a_j-d b_i b_j).
\]

Consequently the matched vector satisfies

\[
 \boxed{
 c^{\mathsf T}K^{\rm pair}c
 =-\frac{2md}{\left(\prod_i(x_i^2-d)\right)^2}<0.
 }
\]

Under RH the full Pick matrix is positive semidefinite by `L-3202`. Therefore,
for any exact rational or dyadic nodes, model `d`, and the exact vector above, a
directed enclosure proving

\[
 c^{\mathsf T}Kc<0
\]

is a finite unconditional counterexample witness to RH, subject to the parent
normalization and implication audit.

## Proof of the pair decomposition

At `T=Im(rho_+)=Im(rho_-)`, the pair contributes to `F(s_i)`

\[
 \frac{m}{x_i-\delta}+\frac{m}{x_i+\delta}
 =\frac{2mx_i}{x_i^2-d}.
\]

Using the Pick denominator `x_i+x_j`, its matrix contribution is

\[
 \frac{2m}{x_i+x_j}
 \left(\frac{x_i}{x_i^2-d}+\frac{x_j}{x_j^2-d}\right)
 =2m\frac{x_ix_j-d}{(x_i^2-d)(x_j^2-d)}.
\]

This is the difference of the two displayed rank-one matrices.

## Proof of the exact vector identities

Let

\[
 P(z)=\prod_i(z-x_i).
\]

The standard barycentric identities are

\[
 \sum_i\frac{w_i}{z-x_i}=\frac1{P(z)}
\]

and

\[
 \sum_i w_i x_i^k=0,
 \qquad 0\le k\le n-2.
\]

The positive overlap cancels directly:

\[
 \sum_i c_i a_i
 =S_1\sum_iw_i a_i-S_0\sum_iw_ix_i a_i
 =S_1S_0-S_0S_1=0.
\]

Similarly, for `0<=k<=n-3`,

\[
 \sum_i c_i x_i^k
 =S_1\sum_iw_ix_i^k-S_0\sum_iw_ix_i^{k+1}=0.
\]

Put `r=sqrt(d)` temporarily inside an algebraic extension, and write

\[
 T_0=\sum_i\frac{w_i}{x_i^2-d},
 \qquad
 T_1=\sum_i\frac{w_ix_i}{x_i^2-d}=S_0.
\]

Because `n>=2`, `sum_i w_i=0`, so

\[
 S_1=\sum_iw_i\frac{x_i^2}{x_i^2-d}=dT_0.
\]

Partial fractions and the barycentric identity give

\[
 T_0=\frac1{2r}
 \left(\frac1{P(-r)}-\frac1{P(r)}\right),
\]

\[
 S_0=-\frac12
 \left(\frac1{P(r)}+\frac1{P(-r)}\right).
\]

Hence

\[
 \sum_i c_i b_i
 =S_1T_0-S_0T_1
 =dT_0^2-S_0^2
 =-\frac1{P(r)P(-r)}
 =-\frac1{\prod_i(x_i^2-d)}.
\]

The right side is nonzero by hypothesis, so `c` is nonzero. Substitution in the
rank-two pair formula proves the strict negative value.

## Distant critical-line suppression

A critical-line zero with ordinate offset `y=T-gamma` contributes

\[
 \left|\sum_i\frac{c_i}{x_i+iy}\right|^2.
\]

Expanding in powers of `x_i/(iy)`, the moment cancellations remove the first
`n-2` amplitude terms. Thus, for fixed nodes and vector, one distant zero
contributes `O(|y|^{-2n+2})`. This is a search and tail-control advantage, not a
replacement for complete directed evaluation of the full `xi` values.

## Exact synthetic separation

Take nodes `(1,2,3)`, model `d=1/4`, and the symmetry-closed finite zero set

- `1/2 +/- 1/2 +/- 100 i`;
- critical-line zeros at ordinates `+/-90` and `+/-110`, each with multiplicity
  19.

At height `T=100`, the matched vector is

\[
 c=\left(-\frac2{21},\frac{52}{105},-\frac25\right).
\]

Exact rational reconstruction gives:

- all three scalar `Re F` values positive;
- every two-node `L-3902` channel `A` and `B` positive;
- the ordinary L-3901 barycentric product localizer positive;
- the matched quadratic form strictly negative.

The synthetic object tests discrimination only. It is not a Riemann-xi
counterexample.

## Certificate consequence

No new checker primitive is required. The `real-pick-rayleigh` channel in
X-3902 accepts:

1. exact common-height points;
2. the exact rational matched vector;
3. two independently assembled outward rectangles for each `F(s_i)`;
4. denominator-zero gates;
5. the exact contracted interval.

The final interval must have negative upper endpoint. An eigenvalue or fitted
model is neither supplied nor trusted.

## Analytic and dependency audit

- The proof of the vector identities is finite algebra over rational functions.
- The model parameter `d` is positive and avoids every `x_i^2`.
- The off-line pair formula uses the same-ordinate pair supplied by functional
  equation and conjugation symmetry.
- `L-3202` supplies only the one-way implication from a negative actual Pick
  quadratic to RH failure; no status of that parent claim is promoted here.
- The model value `d` need not equal any actual displacement during discovery.
  A scan over `d` merely proposes exact vectors; only the actual directed Pick
  quadratic decides a witness.

## Gap audit

1. A negative synthetic pair term does not imply the full Riemann Pick value is
   negative; all other zeros are part of the actual `F` evaluations.
2. Near-null fixed vectors can amplify pointwise ball widths severely. A
   precision ladder must fail closed until the contracted interval separates
   from zero.
3. Choosing `d` after inspecting rounded values is permitted for discovery, but
   the final `d`, nodes, and vector must be frozen exactly before ball
   evaluation.
4. The square-root notation in the proof is eliminable; the final vector and
   identities are rational whenever the nodes and `d` are rational.
5. Passing this localizer at finitely many points is not evidence for RH.

## Adversarial tests

1. Reconstruct all identities with `fractions.Fraction` for random rational
   nodes and model values.
2. Mutate one vector coordinate and require the positive-rank annihilation to
   fail.
3. Exercise nodes on both sides of `sqrt(d)` and verify the squared-product sign
   remains negative.
4. Add a large critical-line synthetic background for which all scalar and
   two-channel tests stay positive while the matched localizer remains negative.
5. Escalate one actual high-height near-null through directed 192-, 256-, 384-,
   and 512-bit evaluations.
6. Widen any primitive rectangle through zero and require the exact checker to
   return unresolved rather than infer a sign.

## Remaining uncertainty

The elementary finite identity appears complete. Its practical power on the
actual Riemann zero set, the best node geometry, and the interval precision
required at high height remain empirical.

## Suggested next attack

Use the rigorous X-3902 Riemann--Siegel producer on a logarithmic dyadic node
ladder. Scan a small exact rational `d` family, freeze the strongest matched
vector, and certify its fixed quadratic directly. Compare every result with the
scalar and two-channel channels evaluated from the same primitive balls.