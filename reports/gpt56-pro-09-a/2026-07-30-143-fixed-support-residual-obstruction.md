# Fixed-support residual obstruction on the positive Hardy--prolate route

Agent: `gpt56-pro-09-a`  
Date: 2026-07-30  
Issue: #143  
PR: #150

## Result

The remaining numerator in the audited L-14302/L-14303 certificate has a
fixed-support ambient limit. Under graph convergence of the Fourier projections,

\[
 \mathcal R_{W_\tau}(z_N;p_N)
 \longrightarrow
 \mathcal R_{W_\tau}((A_\lambda-\mu_\lambda I)k_\lambda;k_\lambda).
\]

The limiting quantity is the reciprocal-Hardy distance of
`A_lambda k_lambda` from the line spanned by `k_lambda`. It vanishes exactly if
the prolate target is an exact eigenvector of the ambient Weil operator.

This prevents a misleading computational strategy: increasing `N` at one fixed
support cannot erase a genuine ambient prolate defect. It can only remove the
finite-section error.

## Source-level consistency

The source paper states that the main unresolved analytic step is precisely to
show that the explicit prolate candidate `k_lambda` accurately approximates a
scalar multiple of the lowest Weil eigenfunction. It also identifies the trace
formula relating the Weil form, the projections, and the map `E` as the
structural bridge. Thus L-14307 does not manufacture a new obstacle; it gives a
finite/ambient decomposition of the obstacle already stated by the authors.

The ambient Weil operator is unbounded, so ordinary `L2` Fourier convergence is
not enough. The correct hypothesis is graph convergence

```text
||P_N k-k|| + ||A P_N k-Ak|| -> 0.
```

This domain issue is now explicit rather than hidden inside a finite matrix
limit.

## Corrected finite objective

Every production table should separate:

```text
1. target projection tail;
2. operator graph-tail / finite-section error;
3. ambient reciprocal-Hardy prolate residual;
4. weighted even-complement coercivity h;
5. ambient residual divided by h.
```

Only item 3 can be attacked by the Weil--prolate trace relation. Items 1 and 2
are approximation/certification layers. Item 4 is a spectral separation layer.

## Strategic narrowing

The next theorem worth pursuing is not another finite Ritz estimate. It is an
ambient estimate of the form

\[
 \inf_c\|(A_\lambda-cI)k_\lambda\|_{W_{\tau}^{-1}}
 \leq \varepsilon_\lambda h_\lambda\|k_\lambda\|,
 \qquad \varepsilon_\lambda\to0,
\]

or a form-dual analogue if `k_lambda` is not yet known to lie in `D(A_lambda)`.
The trace formula should be rewritten directly as a residual identity or
inequality for `E(h_lambda)`, with the prolate concentration defect
`1-chi(lambda)` exposed as the expected small parameter.

## Audit note

The first draft of L-14307 contained an overcompressed quantitative Rayleigh
constant depending only on the Rayleigh quotient. Self-review caught that this
must instead involve `||A k||`. That draft was deleted before use and replaced
by the corrected bound in commit `5eceb5971617926981d3d86a0359ad13042db59a`.
The qualitative theorem was unchanged.

## Status

- L-14307: `PROPOSED`.
- No production graph-tail certificate exists yet.
- No ambient residual decay theorem exists yet.
- No RH proof is claimed.