# L-21503 — Rephased critical-strip support sieve

Claim ID: `L-21503`  
Title: Endpoint rephasing restores the scaled derivative hypothesis in critical-strip support averaging  
Status: **PROPOSED — COMPLETE REPHASING AND ABSTRACT LARGE-SIEVE REPAIR; SOURCE-PROFILE LMIs AND FINITE STATIONARY LEDGER REMAIN**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: the abstract support large sieve of `L-16226`; the two-branch radial action of `L-16224`; a source-specific shrinking-strip profile bound in the exact CCM normalization  
Scope: repair of `L-19821-critical-strip-growth-closes-support-average.md` on PR #202

## 1. Scope correction

The parent support large sieve requires an amplitude family satisfying

\[
 \|A_\gamma(R)\|+T\|\partial_R A_\gamma(R)\|\le B_T,
 \qquad T\le R\le2T.
 \tag{L-21503.1}
\]

The endpoint translation in the normalized omitted-tail transform is

\[
 e^{-isx_R},
 \qquad
 x_R={1\over2}\log {R\over2\pi},
 \qquad
 s=\gamma+i\delta.
 \tag{L-21503.2}
\]

If the full factor is left inside the amplitude, differentiating its real
oscillation gives

\[
 R\partial_R e^{-i\gamma x_R}=-{i\gamma\over2}e^{-i\gamma x_R},
 \tag{L-21503.3}
\]

which has size `Theta(T)` on a band `gamma asymp T`.  Consequently the bound

\[
 \|A_\gamma\|+\|\partial_R A_\gamma\|
 \ll T^{1/4}\operatorname{polylog}T
\]

does **not** imply (L-21503.1).  The real endpoint oscillation must be moved
into the support phase before the large sieve is applied.

## 2. Exact rephasing

Assume one radial branch has the form

\[
 e^{i\varepsilon R S(\gamma/R)}
 e^{-i\gamma x_R+\delta x_R}
 a_{\varepsilon,R}\!\left({\gamma+i\delta\over R}\right),
 \qquad \varepsilon\in\{+1,-1\}.
 \tag{L-21503.4}
\]

Define the rephased real support phase and amplitude by

\[
 \Theta_{\varepsilon,\gamma}(R)
 =\varepsilon R S(\gamma/R)-\gamma x_R,
 \tag{L-21503.5}
\]

\[
 \widetilde A_{\varepsilon,\gamma,\delta}(R)
 =e^{\delta x_R}
 a_{\varepsilon,R}\!\left({\gamma+i\delta\over R}\right).
 \tag{L-21503.6}
\]

Then (L-21503.4) is exactly

\[
 e^{i\Theta_{\varepsilon,\gamma}(R)}
 \widetilde A_{\varepsilon,\gamma,\delta}(R).
 \tag{L-21503.7}
\]

No approximation and no zero-location hypothesis enters this factorization.

## 3. Restored scaled derivative bound

Fix a compact ratio band

\[
 0<a\le |u|\le b<\infty
\]

and suppose that, throughout

\[
 |v|\le {1\over2R},
 \qquad n\le C(\log R)^2,
\]

the source profile obeys

\[
 \boxed{
 \|a_R(u+iv)\|
 +\|\partial_u a_R(u+iv)\|
 +R\|\partial_Ra_R(u+iv)\|
 \le P_R.
 }
 \tag{L-21503.8}
\]

For every nontrivial zeta zero, `|delta|<1/2`, and therefore

\[
 e^{\delta x_R}\le e^{|\delta|x_R}\le R^{1/4}.
 \tag{L-21503.9}
\]

Using `R x_R'=1/2` and `s/R=O(1)` on the compact ratio band,

\[
\begin{aligned}
 R\partial_R\widetilde A
 =e^{\delta x_R}\left[
 {\delta\over2}a_R
 +R(\partial_Ra_R)_u
 -{\gamma+i\delta\over R}\partial_u a_R
 \right].
\end{aligned}
 \tag{L-21503.10}
\]

Hence

\[
 \boxed{
 \|\widetilde A\|+R\|\partial_R\widetilde A\|
 \le C R^{1/4}P_R.
 }
 \tag{L-21503.11}
\]

This is the derivative hypothesis actually required by `L-16226`.

## 4. Combined phase geometry

For the Dunster radial action, introduce the stationary parameter `y>0` by

\[
 \omega={\gamma\over R}=y+{1\over y}.
 \tag{L-21503.12}
\]

The Legendre identity of `L-16226/L-16224` is

\[
 S(\omega)-\omega S'(\omega)=y.
 \tag{L-21503.13}
\]

Therefore

\[
 \Theta_{\varepsilon,\gamma}'(R)
 =\varepsilon y-\frac\omega2.
 \tag{L-21503.14}
\]

For the `(+,-endpoint)` phase in (L-21503.5),

\[
 H_-(\omega)=y-\frac\omega2
 ={1\over2}\left(y-{1\over y}\right),
 \tag{L-21503.15}
\]

and

\[
 \boxed{
 {dH_-\over d\omega}
 ={y^2+1\over2(y^2-1)}.
 }
 \tag{L-21503.16}
\]

Thus

\[
 \left|{dH_-\over d\omega}\right|\ge{1\over2}
 \tag{L-21503.17}
\]

on both open branches away from the fold `y=1`.  The reflected sign gives the
negative of this function and has the same separation.

If the opposite endpoint sign occurs, the derivative map is

\[
 H_+(\omega)=y+\frac\omega2
 ={1\over2}\left(3y+{1\over y}\right),
 \tag{L-21503.18}
\]

with

\[
 {dH_+\over d\omega}
 ={3y^2-1\over2(y^2-1)}.
 \tag{L-21503.19}
\]

Besides the radial fold `y=1`, this has exactly one nondegenerate critical
ratio

\[
 y={1\over\sqrt3}.
 \tag{L-21503.20}
\]

Consequently the complete endpoint/radial phase family admits a fixed finite
partition into:

1. intervals on which the phase-derivative map is uniformly separated;
2. the ordinary radial fold near `y=1`;
3. at most one additional quadratic stationary neighborhood near
   `y=1/sqrt(3)` for the opposite endpoint sign.

The first family is covered directly by the parent large sieve.  The two finite
stationary neighborhoods require an Airy/van-der-Corput ledger and may not be
silently absorbed into a pointwise amplitude bound.

## 5. Cross-end mean-square bound

Let the zero ordinates in `[aT,bT]` satisfy the unconditional unit-bin count

\[
 \#\{\gamma\in[j,j+1)\}\ll\log T.
 \tag{L-21503.21}
\]

On every separated phase piece, `L-16226` and (L-21503.11) give

\[
 \boxed{
 {1\over T}\int_T^{2T}
 \|Z_T^{\rm cross}(R)\|_{\rm HS}^2\,dR
 \ll T^{-1/2}P_T^2(\log T)^3.
 }
 \tag{L-21503.22}
\]

In particular, if `P_T` is polylogarithmic, the right side tends to zero with a
full half-power reserve.

After the finite stationary neighborhoods are supplied with a vanishing total
ledger, Markov's inequality permits simultaneous selection for any
polylogarithmic number of phase families.

## 6. Same-end horizontal correction

The same-end channels contain no endpoint exponential after conjugate pairing.
Assume their holomorphic profile products satisfy the horizontal derivative
bound

\[
 \sup_{|v|\le1/(2R)}
 \left\|
 \partial_v\bigl[a_R(u-iv)^*a_R(u+iv)\bigr]
 \right\|
 \le P_R^2.
 \tag{L-21503.23}
\]

Since the actual imaginary ratio is `v=delta/R`, one zero contributes at most
`C P_R^2/R` beyond its line-centered value.  Summing
`O(R log R)` zeros in a fixed ratio band and retaining the outer `1/R`
normalization gives

\[
 \boxed{
 \|Z_R^{\rm same}-Z_R^{\rm same,line}\|
 \ll {P_R^2\log R\over R}.
 }
 \tag{L-21503.24}
\]

Thus the nonoscillatory same-end correction also vanishes when `P_R` is
polylogarithmic.  This channel is not proved by the support large sieve; it
requires the source-specific horizontal derivative bound (L-21503.23).

## 7. Corrected support-average theorem

Suppose one exact alias-corrected source profile satisfies:

1. the shrinking-strip graph bound (L-21503.8);
2. the same-end derivative bound (L-21503.23);
3. a finite radial/endpoint phase decomposition whose separated pieces obey
   (L-21503.16)--(L-21503.19);
4. vanishing ledgers for the radial fold, the additional stationary ratio,
   central pieces, endpoint polylogarithms, and the infinite alias remainder.

Then on a positive-measure subset of every sufficiently large dyadic support
block,

\[
 \boxed{
 \|A_R-A_R^{\rm line}\|=o(1),
 }
 \tag{L-21503.25}
\]

and therefore certainly `o(log R)`.

This is the corrected form of the horizontal-displacement step in the prolate
resolution proposal.

## 8. Proof boundary

- Equations (L-21503.5)--(L-21503.20) are exact rephasing and phase algebra.
- Equation (L-21503.22) is an application of the already abstract parent large
  sieve with its actual scaled derivative hypothesis restored.
- The original `L-19821` argument is not valid without this rephasing because it
  omits the factor `T` in the amplitude derivative gate.
- The complete source-profile LMIs, same-end horizontal derivative Gram, finite
  stationary ledgers, endpoint channels, and alias convergence are not proved
  here.
- This repair does not verify `T-19807` and does not prove RH.
