# L-19821 — Critical-strip growth still closes the support average

Claim ID: `L-19821`  
Title: The full off-line horizontal displacement costs at most a quarter power of the radial scale, which the support large sieve still defeats  
Status: **PROPOSED — COMPLETE LARGE-SIEVE REPAIR; PROFILE INTERFACE IMPORTED FROM PR #164**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the normalized tail-profile representation of `T-16202`; the uniform shrinking-strip profile bounds of `L-16216/L-16219/L-16222`; Riemann–von Mangoldt unit-window counts  
Scope: the horizontal-zero-displacement gate in `L-16226/T-16205`

## 1. The issue

The support-average theorem `L-16226` is written with a polylogarithmic amplitude envelope. A centered off-line zero

\[
 s_\rho=\gamma+i\delta,
 \qquad
 \delta=\beta-\frac12,
 \qquad |δ|<\frac12,
\]

also meets the support-translation factor in the normalized omitted-tail transform. That factor is not uniformly bounded. The correct unconditional growth is a quarter power of the radial scale.

The point of this lemma is that this larger envelope is still comfortably below the critical large-sieve threshold. No RH assumption, zero-density estimate, or zero-free strip is needed.

## 2. Normalized tail profile

Retain the PR #164 radial normalization

\[
 \widehat T_{n,R}(s)
 =\sqrt{\frac{d_n(R)}{R}}
  e^{-isx_R}\Phi_{n,R}\!\left(\frac{s}{R}\right),
 \tag{L-19821.1}
\]

where

\[
 R=2\pi\lambda^2,
 \qquad
 x_R=\log\lambda
 =\frac12\log\frac{R}{2\pi}.
 \tag{L-19821.2}
\]

Let the mode window satisfy

\[
 0\le n\le H_R,
 \qquad H_R=O((\log R)^2).
 \tag{L-19821.3}
\]

The uniform Dunster/Fuchs interface needed below is the following shrinking-strip bound: for each fixed compact frequency-ratio band

\[
 0<a\le |u|\le b<\infty,
\]

there are constants `A,C` such that

\[
 \sup_{\substack{n\le H_R\\a\le|u|\le b\\|v|\le1/(2R)}}
 \left(
  \|\Phi_{n,R}(u+iv)\|
 +\|\partial_u\Phi_{n,R}(u+iv)\|
 +R\|\partial_R\Phi_{n,R}(u+iv)\|
 \right)
 \le C(\log R)^A.
 \tag{L-19821.4}
\]

For a finite packet, the norms in (L-19821.4) may be operator, Hilbert–Schmidt, or Euclidean packet norms. Polynomial packet-dimension losses are absorbed into the exponent `A` because of (L-19821.3).

## 3. Exact critical-strip envelope

For every nontrivial zeta zero, the classical zero-free boundary gives

\[
 0<\beta<1,
 \qquad |δ|<\frac12.
 \tag{L-19821.5}
\]

Therefore

\[
 \left|e^{-is_\rho x_R}\right|
 =e^{\delta x_R}
 \le e^{|\delta|x_R}
 \le\lambda^{1/2}
 =\left(\frac{R}{2\pi}\right)^{1/4}
 \le R^{1/4}.
 \tag{L-19821.6}
\]

Since

\[
 \operatorname{Im}\frac{s_\rho}{R}=\frac\delta R,
 \qquad
 \left|\operatorname{Im}\frac{s_\rho}{R}\right|<\frac1{2R},
\]

(L-19821.4) applies throughout the full open critical strip. Consequently the normalized amplitude occurring in the support-average packet obeys

\[
 \boxed{
 \|A_\rho(R)\|
 \le C R^{1/4}(\log R)^A.}
 \tag{L-19821.7}
\]

The same estimate holds for one support derivative. Indeed,

\[
 \partial_R
 \left[e^{-isx_R}\Phi_R(s/R)\right]
 =e^{-isx_R}
 \left[
  -isx_R'\Phi_R(s/R)
  +\partial_R\Phi_R(s/R)
  -\frac{s}{R^2}\partial_u\Phi_R(s/R)
 \right].
 \tag{L-19821.8}
\]

On a band `|gamma| asymp R`,

\[
 |s x_R'|=\frac{|s|}{2R}=O(1),
 \qquad
 \frac{|s|}{R^2}=O(R^{-1}),
\]

so (L-19821.4) gives

\[
 \boxed{
 \|A_\rho(R)\|+\|A_\rho'(R)\|
 \le C R^{1/4}(\log R)^A.}
 \tag{L-19821.9}
\]

This quarter-power factor is the complete cost of allowing every possible horizontal displacement in the critical strip.

## 4. Hilbert-valued support large sieve with polynomial amplitude

Let `T` be large and let the zero band satisfy

\[
 aT\le|\gamma_\rho|\le bT.
\]

Assume the standard unit-window count

\[
 N(t+1)-N(t)\le C\log(2+t)
 \tag{L-19821.10}
\]

with multiplicity. Let

\[
 Z_T(R)
 =\frac1R
  \sum_{\rho\in\mathcal Z_T}
  A_\rho(R)e^{i\gamma_\rho\phi(R)},
 \qquad T\le R\le2T,
 \tag{L-19821.11}
\]

where

\[
 0<c\le|\phi'(R)|\le C,
 \qquad
 |φ''(R)|\le C/T.
 \tag{L-19821.12}
\]

Put

\[
 B_T=C T^{1/4}(\log T)^A,
 \qquad L_T=C\log T.
\]

Expanding the Hilbert–Schmidt square and grouping ordinates into unit bins gives the same near/far decomposition as `L-16226`:

- same and adjacent bins contribute `O(B_T^2 L_T^2/T)` to the support average;
- bins at distance `m>=1` contribute `O(B_T^2/(Tm))` per pair after one integration by parts;
- summing the harmonic bin separation gives one further `log T`.

Hence

\[
 \boxed{
 \frac1T\int_T^{2T}\|Z_T(R)\|_{\rm HS}^2\,dR
 \le
 C B_T^2L_T^2\frac{\log T}{T}.}
 \tag{L-19821.13}
\]

Substituting the critical-strip envelope yields

\[
 \boxed{
 \frac1T\int_T^{2T}\|Z_T(R)\|_{\rm HS}^2\,dR
 \le
 C T^{-1/2}(\log T)^{2A+3}
 \longrightarrow0.}
 \tag{L-19821.14}
\]

Thus the support average remains vanishing even after paying for the worst possible off-line horizontal displacement.

## 5. Simultaneous good supports

Suppose the complete frame generates at most

\[
 F_T=O((\log T)^B)
\]

horizontal, reflected-branch, Airy, endpoint, and line-centered oscillatory families. Choose the common threshold

\[
 \eta_T=T^{-1/16}.
 \tag{L-19821.15}
\]

For one family, Markov and (L-19821.14) give a bad-support fraction

\[
 O\!\left(
  T^{-3/8}(\log T)^{2A+3}
 \right).
\]

After the union bound over all `F_T` families, the total bad fraction still tends to zero. Since `eta_T -> 0`, every oscillatory family is simultaneously `o(1)` on a positive-measure subset of `[T,2T]`.

Removing finitely many deterministic transition intervals and the countable set of exact zeta-cycle lengths leaves a nonempty good-support set for every sufficiently large block.

## 6. Consequence for the PR #164 wrapper

The support-averaging step does not require the polylogarithmic amplitude sentence in `L-16226`. It remains valid under the much larger and unconditional envelope

\[
 B_T=O\!\left(T^{1/4}(\log T)^A\right).
\]

Therefore a hypothetical off-line zero cannot defeat the support average merely through the factor `exp(delta log lambda)`. The large-sieve reserve is a full half power of `T`, while the complete critical-strip continuation consumes only a quarter power before squaring.

This closes the horizontal-displacement growth mismatch in the growing prolate-frame programme.

## 7. Proof boundary

- The quarter-power estimate is exact once the normalized profile formula (L-19821.1) is fixed.
- The large-sieve estimate uses only the unconditional unit-window zero count and finite packet regularity.
- The shrinking-strip profile bound (L-19821.4) is the imported PSWF interface; it must be audited in the exact CCM/Dunster normalization.
- This lemma does not by itself prove the growing arithmetic-tail Gram floor or the finite CCM real-zero theorem.
- No accepted proof of RH is claimed by this lemma alone.
