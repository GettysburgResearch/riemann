# L-3901 — Barycentric Pick product localizers

Claim ID: L-3901  
Title: Exact barycentric fixed vectors turn sampled xi passivity into resolvent-product localizers  
Status: PROPOSED  
Authoring agent: `gpt56-02-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `D-3201`; `L-3201`; `L-3202`  
Scope: finite sampled `xi'/xi` witnesses in `Re(s)>1/2`  
Related counterexample candidates: none

## Statement

Let

\[
F(s)=\frac{\xi'(s)}{\xi(s)}
\]

in the normalization of `D-3201`. Fix a real ordinate `T` and pairwise distinct
positive real numbers

\[
x_0,\ldots,x_r>0,
\qquad
s_i=\frac12+x_i+iT.
\]

Assume none of the `s_i` is a zero of `xi`. Define the Pick matrix

\[
K_{ij}=\frac{F(s_i)+\overline{F(s_j)}}{x_i+x_j}
\]

and the barycentric vector

\[
c_i=\frac1{\prod_{j\ne i}(x_i-x_j)}.
\]

If RH holds, then

\[
\boxed{c^*Kc=\sum_\gamma\frac1{\prod_{i=0}^{r}(x_i^2+(T-\gamma)^2)}\ge0.}
\]

Here the ordinates `gamma` are counted with multiplicity. Consequently, exact
rational or dyadic `x_i`, the corresponding exact rational vector `c` up to a
nonzero common scale, and directed enclosures proving `c^*Kc<0` give a finite
unconditional counterexample witness to RH.

For a same-ordinate off-line symmetric pair

\[
\frac12+\delta+i\gamma,
\qquad
\frac12-\delta+i\gamma,
\qquad \delta>0,
\]

its contribution at `T=gamma` is exactly

\[
\boxed{\frac{2}{\prod_{i=0}^{r}(x_i^2-\delta^2)}.}
\]

In particular, for two offsets `0<x_-<x_+`, the two-point localizer is negative
whenever `x_-<delta<x_+`.

Every RH failure therefore creates an open negative basin for some exact
**two-point** barycentric Pick localizer: choose dyadic offsets bracketing the
horizontal displacement of a right-half-plane zero and sufficiently close to
it, then choose a rational or dyadic ordinate sufficiently close to its
ordinate.

## Fixed-vector evaluation and conditioning bound

For real `c_i`, the quadratic form is the real linear expression

\[
c^*Kc=\sum_i d_i\operatorname{Re}F(s_i),
\qquad
d_i=2c_i\sum_j\frac{c_j}{x_i+x_j}.
\]

Thus balls `Re F(s_i) in [a_i,b_i]` propagate by exact rational interval
arithmetic. If midpoint errors are bounded by `epsilon_i`, then

\[
|\Delta(c^*Kc)|\le\sum_i |d_i|\epsilon_i.
\]

The quantity `sum |d_i|` is an explicit conditioning diagnostic. It must be
recorded before a high-order localizer is interpreted numerically.

## Proof under RH

Under RH, the zero-resolvent expansion used in `L-3201` gives

\[
F(s_i)=\sum_\gamma\frac1{x_i+i(T-\gamma)}.
\]

For one ordinate offset `y=T-gamma`,

\[
\frac{(x_i+iy)^{-1}+(x_j-iy)^{-1}}{x_i+x_j}
=\frac1{(x_i+iy)(x_j-iy)}.
\]

Therefore

\[
K_{ij}=\sum_\gamma\frac1{(x_i+i(T-\gamma))(x_j-i(T-\gamma))}.
\]

For `P(z)=prod_i(z+x_i)`, partial fractions give

\[
\sum_i\frac{c_i}{z+x_i}=\frac{(-1)^r}{P(z)}.
\]

Hence

\[
\begin{aligned}
c^*Kc
&=\sum_\gamma\left|\sum_i\frac{c_i}{x_i+i(T-\gamma)}\right|^2\\
&=\sum_\gamma\frac1{\prod_i(x_i^2+(T-\gamma)^2)}\ge0.
\end{aligned}
\]

This proves the first formula.

## Off-line pair calculation

At `T=gamma`, the same-ordinate symmetric pair contributes to `F` the real
rational function

\[
f_\delta(x)=\frac1{x-\delta}+\frac1{x+\delta}=\frac{2x}{x^2-\delta^2}.
\]

Substituting `f_delta` into the Pick form and applying the same partial-fraction
identity at the two real poles `+/-delta` yields

\[
c^*K^{(\delta)}c=\frac{2}{\prod_i(x_i^2-\delta^2)}.
\]

For two points bracketing `delta`, exactly one factor is negative. The pair term
therefore tends to negative infinity as either bracket endpoint approaches
`delta`, while the contribution of every other zero is bounded on a sufficiently
small zero-free neighborhood. Continuity and density of dyadic points give an
exact finite two-point witness. ∎

## Analytic domain audit

- Every evaluation point is strictly in `Re(s)>1/2` and must be certified away
  from zeros of `xi`.
- The proof uses the same absolutely convergent half-plane resolvent interface as
  `L-3201` and `L-3202`.
- The barycentric nodes are pairwise distinct.
- No eigenvalue or limiting confluent matrix is needed for the counterexample
  implication.

## Dependency audit

- `D-3201` fixes the completed-xi normalization.
- `L-3201` supplies the zero-resolvent expansion and scalar implication.
- `L-3202` supplies the sampled Pick kernel and its RH-conditional positivity.
- The barycentric and off-line product identities are proved directly here.

## Gap audit

- A floating eigenvalue of a nearly singular Pick matrix is not a witness.
- Large barycentric weights can amplify pointwise evaluation errors by many
  orders of magnitude; `sum |d_i|` must be compared with the claimed margin.
- An interval containing zero is inconclusive even when its midpoint is negative.
- Reusing one inaccurate evaluator at several nominal precisions is not
  independent reproduction.
- The two-point existential statement gives no bound for the unknown zero height
  or horizontal displacement.

## Adversarial tests

1. Verify the product identity with exact rational arithmetic on finite
   critical-line zero models.
2. Verify the off-line symmetric-pair formula exactly and its bracket sign.
3. Mutate one barycentric sign and require the product identity to fail.
4. Reproduce a near-coalescent precision ladder and reject every sign that does
   not dominate the explicit linear amplification bound.
5. Freeze one integer-scaled vector before any rigorous complex-ball evaluation.

## Remaining uncertainty

The finite algebra is complete-looking. Its application to Riemann `xi` remains
conditional on review of the `D-3201`/`L-3201` normalization and on a future
ball-valued evaluator.

## Suggested next attack

Use a dyadic offset ladder and two-point localizers as the first reconnaissance
layer for Issue #39. Only points with a negative fixed-vector midpoint stable
under precision escalation should proceed to Arb.