# R-9502 — The semicircle RH bound does not follow from an absolute contour shift

Claim ID: `R-9502`  
Title: The first proof sketch for the semicircle endpoint omitted a critical vertical-growth obstruction  
Status: `REFUTATION OF PROOF STEP; SEMICIRCLE THEOREM NOT REJECTED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `T-9501`; standard functional equation and Stirling estimates  
Scope: proof-status correction  
Related counterexample candidates: none

## Refuted step

`T-9501` initially stated that, under RH, one may shift

\[
\widehat k(z)\frac{\zeta(z)}{\zeta(z+1)}x^{z-1}
\]

to

\[
\Re z=-\frac12+\varepsilon
\]

and control the new vertical integral directly from

\[
\widehat k(\sigma+it)=O(|t|^{-3/2}).
\]

That is not an adequate absolute-convergence argument.

On this line the functional equation gives, at the level of absolute values,

\[
|\zeta(-1/2+\varepsilon+it)|
\asymp_{\varepsilon}
|t|^{1-\varepsilon}
|\zeta(3/2-\varepsilon-it)|.
\]

Even granting the standard RH-side subpolynomial bound for

\[
1/\zeta(1/2+\varepsilon+it),
\]

the absolute integrand is only of size approximately

\[
|t|^{-1/2-\varepsilon+o(1)},
\]

which is not integrable for small fixed `epsilon`.

Therefore the original sentence “standard zeta bounds control the shifted
integral” is incomplete. A correct proof would need an oscillatory functional-
equation/stationary-phase analysis, or an equivalent Bessel--Möbius transfer.

## What remains valid

The following parts of `T-9501` are unaffected:

1. the exact Mellin transform;
2. the main residue `3/pi`;
3. the genuine shifted-zero pole set `z=rho-1`;
4. the converse: an `O_epsilon(x^-3/2+epsilon)` bound excludes every off-line
   zero;
5. the exact bridge to the `s=1` Jordan/Volterra endpoint density.

The semicircle equivalence may still be true, but its RH-to-bound direction is
not promoted by the initial proof sketch.

## Rigorous repair

`T-9502` replaces the semicircle weight by

\[
(1-u^2)^2.
\]

Its Mellin transform is the rational function

\[
\frac8{z(z+2)(z+4)}=O(|t|^{-3}),
\]

and `L-9508` supplies an exact Bernoulli--Möbius decomposition. The classical
RH-equivalent Mertens estimate then gives the full

\[
x^{-3/2+\varepsilon}
\]

bound directly, without a delicate contour argument.

Thus `T-9502`, not the unreviewed RH direction of `T-9501`, is the proof-facing
global criterion.

## Status consequence

- Do not cite `T-9501` as a completed equivalence until the oscillatory transfer
  is independently supplied.
- The exact arithmetic and operator connection carried by its semicircle kernel
  remains useful.
- `T-9502` is the rigorous replacement for the full RH criterion.
