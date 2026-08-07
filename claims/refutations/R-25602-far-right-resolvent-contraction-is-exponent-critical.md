# R-25602 — Far-right finite-resolvent contraction is exponent-critical

Claim ID: `R-25602`  
Title: Absolute contraction of the residual on a far-right vertical line is exactly canceled by physical-block deweighting and cannot yield a subcritical Möbius exponent  
Status: **PROPOSED EXACT SCOPE BARRIER PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: `L-9518`; `L-23201`; weighted Young inequality  
Scope: proofs using only absolute residual multiplier norms

## 1. Normalized additive residual operator

Let `r_V` be the standard finite-resolvent residual and let

\[
(T_{r_V}f)(x)
=\sum_{n\ge1}{r_V(n)\over\sqrt n}
 f(x-\log n).
\tag{R-25602.1}
\]

For `alpha>1/2`, put

\[
\sigma=\alpha+\frac12>1,
\qquad
\|f\|_{2,\alpha}=\|e^{-\alpha x}f(x)\|_{L^2(\mathbb R)}.
\]

Translation gives the exact weighted identity

\[
e^{-\alpha x}(T_{r_V}f)(x)
=\sum_n{r_V(n)\over n^\sigma}
[e^{-\alpha(\,x-\log n\,)}f(x-\log n)].
\]

Hence weighted Young gives

\[
\boxed{
\|T_{r_V}f\|_{2,\alpha}
\le A_{V,\sigma}\|f\|_{2,\alpha},
\qquad
A_{V,\sigma}=\sum_n{|r_V(n)|\over n^\sigma}.}
\tag{R-25602.2}
\]

## 2. Absolute tail size

The residual vanishes through `V`, and for `n>V`

\[
|r_V(n)|
\le\sum_{d\mid n}1=d(n).
\]

For every fixed `sigma>1`, elementary Dirichlet-hyperbola or integral bounds
give

\[
\boxed{
A_{V,\sigma}
\le C_\sigma V^{1-\sigma}\log(2V).}
\tag{R-25602.3}
\]

Thus the residual is a strict contraction on a sufficiently far-right weighted
all-line space.

## 3. K-fold depth cost

Iterating (R-25602.2),

\[
\|T_{r_V}^{K-1}f\|_{2,\alpha}
\le
[C_\sigma V^{1-\sigma}\log(2V)]^{K-1}
\|f\|_{2,\alpha}.
\tag{R-25602.4}
\]

At the finite-resolvent endpoint

\[
V=X^{1/K+o_K(1)},
\]

this gain has leading scale

\[
X^{-(\sigma-1)(1-1/K)+o_K(1)}.
\tag{R-25602.5}
\]

If the final depth is written with `K` residual-scale factors rather than
`K-1`, the corresponding leading scale is exactly

\[
X^{1-\sigma+o_K(1)}.
\tag{R-25602.6}
\]

The distinction is an `O(1/K)` endpoint convention and does not alter the
critical conclusion below.

## 4. Physical-block deweighting

On a physical block `x in [J,J+1]`, with `X=e^J`,

\[
\|f\|_{L^2(J,J+1)}
\le e^{\alpha(J+1)}\|f\|_{2,\alpha}.
\tag{R-25602.7}
\]

Since `alpha=sigma-1/2`, the `K`-depth absolute estimate combines
(R-25602.6) and (R-25602.7) into

\[
\boxed{
X^{1-\sigma}X^{\sigma-1/2}
=X^{1/2}.}
\tag{R-25602.8}
\]

The choice of vertical line cancels out exactly. Moving farther right makes the
residual multiplier smaller by precisely the amount by which physical-block
Fourier inversion becomes more expensive.

In energy, the corresponding absolute estimate is of scale `X^(1+o(1))`, the
critical unsigned square-root barrier.

## 5. Consequence

The following proposed shortcut is invalid:

```text
choose sigma>>1;
R_V is small on Re s=sigma;
therefore the top depth has a vanishing physical exponent.
```

Absolute far-right contraction proves only the classical square-root-sized
bound.  Any subcritical result must retain signed arithmetic cancellation not
visible in `A_(V,sigma)`.

This is the vertical-line form of the meromorphic charge conservation theorem
`L-25602`: the gain in the residual half-plane cannot destroy the off-line pole
response of the physical source.

## 6. Permitted stronger input

A useful estimate must improve on absolute Young by a source-specific signed
statement, for example

\[
\|T_{r_V}f_{\rm arithmetic}\|_{2,\alpha}
\le
V^{1-\sigma-\eta_K+o(1)}
\|f_{\rm arithmetic}\|,
\tag{R-25602.9}
\]

or an equivalent reflected lower-scale recurrence.  Any fixed positive
`eta_K` would survive deweighting; proving it on the fixed-ratio Möbius source
is the balanced Type-II theorem.

## 7. Proof boundary

Closed here:

- the exact weighted residual operator;
- its absolute norm;
- the far-right tail bound;
- exact cancellation of the vertical-line gain under deweighting.

Not ruled out:

- signed source-specific contraction;
- reflected dispersion using actual Möbius correlations;
- RH.
