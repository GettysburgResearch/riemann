# L-19828 — The complete branch ledger implies the relative operator local-Weyl theorem

Claim ID: `L-19828`  
Status: **PROVED CONDITIONAL COMPOSITION FROM L-19827/L-19829 AND L-16226; SPECIAL-FUNCTION STATUS INHERITED**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Corrected: 2026-08-07 to remove a redundant source-inverse assumption  
Dependencies: complete branch/alias ledger `L-19827/L-19829`; support large sieve `L-16226`; arithmetic tail floor `L-19826`; Riemann--von Mangoldt; source necessity theorem `L-19831`  
Scope: the fourth theorem requested by the independent review

## 1. Statement

Let `S_R` be a complete finite signed source packet with the same dimension as
the finite CCM space `V_R`. Let

\[
 T_R:S_R\to V_R
\]

be its projected source map, not assumed injective in advance. Let `D_R` be the
complete arithmetic omitted-tail Gram on `S_R`, and let

\[
 A_R=T_R^*A_{V,R}T_R
\]

be the exact pulled-back localized zero-side/Weil matrix. Assume the complete
profile conclusions of `L-19827/L-19829` and the positive tail floor of
`L-19826`.

Then, in every sufficiently large dyadic radial block `[T,2T]`, there is a set
`G_T` of relative measure `1-o(1)` such that for every `R in G_T`,

\[
 \boxed{
 {\left\|
 D_R^{-1/2}
 \left[A_R-(\log R)D_R\right]
 D_R^{-1/2}
 \right\|_{\rm op}
 \over\log R}
 \longrightarrow0.}
 \tag{L-19828.1}
\]

At every sufficiently large good support, `L-19831` then implies that `T_R` is
injective and hence bijective. Thus source injectivity is a consequence of the
local-Weyl theorem, not an input to its proof.

The theorem is unconditional with respect to the location of zeta zeros;
hypothetical off-line zeros are included.

## 2. Exact zero-side normalization

On one dyadic ordinate band, the normalized zero-side matrix has the form

\[
 A_R^{\rm band}
 ={1\over R}
 \sum_{\rho:\,aR\le|\gamma_\rho|\le bR}
 K_R\!\left({\gamma_\rho+i\delta_\rho\over R}
 \right),
 \tag{L-19828.2}
\]

where

\[
 \rho={1\over2}+\delta_\rho+i\gamma_\rho,
 \qquad |\delta_\rho|<1/2,
\]

and `K_R` is the polarized complete tail-profile kernel. The support translation
has cancelled exactly by `R-19805`.

The full matrix is a finite sum of such bands plus low- and high-frequency tails.
The latter are controlled by the same endpoint and profile bounds; adding them
does not change the argument.

## 3. Slow phase-diagonal kernel

Use `L-19827/L-19829` to decompose the profile kernel into

```text
K_R = K_R^diag + K_R^osc + K_R^fold + K_R^end.
```

Here `K_R^diag` contains every pair of equal extracted phase, including the
positive self-Grams of all higher aliases. It is not restricted to the first
alias. In the whitened `D_R` metric,

\[
 \sup_x\|K_R^{\rm diag}(x)\|
 +\int_a^b\|\partial_xK_R^{\rm diag}(x)\|dx
 \le(\log R)^C.
 \tag{L-19828.3}
\]

Holomorphic Taylor expansion in the shrinking strip gives

\[
 \left\|
 K_R^{\rm diag}(x+i\delta/R)-K_R^{\rm diag}(x)
 \right\|
 \le { (\log R)^C\over R}
 \tag{L-19828.4}
\]

uniformly for `|delta|<=1/2`.

The number of zeros in the band is `O(R log R)`, so after the external `1/R`
normalization the complete diagonal horizontal replacement costs

\[
 O((\log R)^{C+1}/R)
 \tag{L-19828.5}
\]

in the whitened metric.

## 4. Stieltjes local Weyl law for the slow kernel

Let `N(t)` count nontrivial zeros with multiplicity. Riemann--von Mangoldt gives

\[
 N(t)=M(t)+S(t),
 \qquad
 M'(t)=c_0\log t+c_1+O(t^{-1}),
 \qquad
 S(t)=O(\log(t+2)).
 \tag{L-19828.6}
\]

The normalization constant `c_0` is absorbed into the definition of `D_R`.
Equivalently one may retain `c_0 log R` throughout and rescale at the end.

For the line-centered slow kernel,

\[
 {1\over R}
 \int_{aR}^{bR}K_R^{\rm diag}(t/R)dN(t)
 \tag{L-19828.7}
\]

is evaluated by Stieltjes integration. The main density gives

\[
 (\log R)D_R^{\rm diag}+O(D_R^{\rm diag}),
 \tag{L-19828.8}
\]

because `log(t)=log R+log(t/R)` and `log(t/R)` is bounded on `[aR,bR]`.

For the remainder,

\[
\begin{aligned}
 {1\over R}\int K_R^{\rm diag}(t/R)dS(t)
 ={}&{1\over R}[K_R^{\rm diag}(t/R)S(t)]_{aR}^{bR}\\
 &-{1\over R^2}
   \int_{aR}^{bR}S(t)
   \partial_xK_R^{\rm diag}(t/R)dt.
\end{aligned}
 \tag{L-19828.9}
\]

Using (L-19828.3) and (L-19828.6),

\[
 \boxed{
 \left\|
 {1\over R}\int K_R^{\rm diag}(t/R)dS(t)
 \right\|
 \le { (\log R)^C\over R}.}
 \tag{L-19828.10}
\]

The decisive factor is the external `1/R` in the zero-side matrix. Thus no
strong pointwise estimate for `S(t)` and no unproved Selberg moment is needed for
the slow phase-diagonal part.

Equations (L-19828.4)--(L-19828.10) yield

\[
 A_R^{\rm diag}
 = (\log R)D_R^{\rm diag}+O(D_R^{\rm diag})
 +O_D((\log R)^C/R).
 \tag{L-19828.11}
\]

After division by `log R`, the bounded `O(D)` term is already negligible.

## 5. Oscillatory branch families

Every unequal-phase branch family has the form

\[
 Z_T(R)
 ={1\over R}
 \sum_{\gamma\in\Gamma_T}
 e^{iR\Delta S(\gamma/R)}A_\gamma(R),
 \qquad T\le R\le2T,
 \tag{L-19828.12}
\]

with

\[
 \|A_\gamma(R)\|+R\|A_\gamma'(R)\|
 \le(\log T)^C
 \tag{L-19828.13}
\]

by `L-19827/L-19829`. The phase partition has the genuine separation required by
`L-16226`. Hence

\[
 {1\over T}\int_T^{2T}\|Z_T(R)\|_{\rm HS}^2dR
 \le { (\log T)^C\over T}.
 \tag{L-19828.14}
\]

Choose `q_T=T^-1/8`. Markov's inequality gives a bad-support fraction

\[
 O(T^{-3/4}(\log T)^C).
 \tag{L-19828.15}
\]

The number of mode, branch, reflected, and compact-alias families is
polylogarithmic. A union bound therefore leaves a relative-measure `1-o(1)` set
on which every compact oscillatory family is `o(1)` simultaneously.

The same argument applies to off-line branch amplitudes. Their horizontal
multipliers are bounded, and their correctly extracted amplitudes still satisfy
(L-19828.13). No smallness of `delta_rho` is assumed.

## 6. Fold families

By `L-19827`, either the Airy normal form gives a complete operator contribution

\[
 O(R^{-1/3}(\log R)^C),
\]

or the fold frequency box is treated as exceptional. Its width is `O(R^-2/3)`;
the unit-window zero count and external normalization give

\[
 O(R^{-2/3}(\log R)^C).
 \tag{L-19828.16}
\]

Both are `o(1)` in the whitened metric.

## 7. Endpoint and infinite-alias families

For the alias Gram, the first endpoint channel has already been summed as the
`L2` logarithmic function of `L-19829`; higher channels and the retained
remainder are absolutely summable.

For support averaging, keep the first endpoint channel termwise. The `k`-th
coefficient is `O(k^-1)`, while integration by parts in its `k`-dependent support
phase supplies another `k^-1`. Therefore the complete endpoint support ledger is
majorized by

\[
 \sum_{k=2}^\infty k^{-2}<\infty.
 \tag{L-19828.17}
\]

The coefficient support derivative satisfies the `R A'` hypothesis. Applying
the same zero-bin argument and summing (L-19828.17) gives an endpoint bad
fraction tending to zero. The absolutely summable higher channels are easier.

Thus all endpoint and infinite-alias errors are `o(1)` simultaneously on a
relative-measure `1-o(1)` support set.

## 8. Reassembly with the exact continuous Gram

The continuous complete tail Gram has the same phase decomposition:

\[
 D_R=D_R^{\rm diag}+D_R^{\rm osc}
     +D_R^{\rm fold}+D_R^{\rm end}.
\]

Stationary phase, cubic van der Corput, and the collective endpoint theorem give

\[
 \left\|
 D_R^{-1/2}
 (D_R-D_R^{\rm diag})
 D_R^{-1/2}
 \right\|
 \le R^{-1/3}(\log R)^C.
 \tag{L-19828.18}
\]

Hence replacing `(log R)D_R^diag` in (L-19828.11) by `(log R)D_R` costs

\[
 o(\log R)
 \tag{L-19828.19}
\]

in the whitened metric. `L-19826` supplies the complete signed Gram floor, so
every whitening operation above is legitimate.

## 9. Final estimate and source injectivity

On the common good-support set, combine

```text
slow Stieltjes error              O_D(1)+O(polylog/R),
compact oscillatory zero sum      o(1),
off-line branch replacement       o(1),
fold contribution                 o(1),
endpoint/infinite aliases         o(1),
continuous cross-Gram replacement o(1).
```

Therefore

\[
 \left\|
 D_R^{-1/2}
 [A_R-(\log R)D_R]
 D_R^{-1/2}
 \right\|
 =o(\log R),
 \tag{L-19828.20}
\]

which is (L-19828.1).

For all sufficiently large good supports, the relative error is less than
`(1/2)log R`. Thus

\[
 A_R\succeq {1\over2}(\log R)D_R\succ0.
\]

Since `A_R=T_R^*A_{V,R}T_R`, `L-19831` gives

\[
 \ker T_R=\{0\}.
\]

Equal dimensions then give bijectivity. Exact and near source-cycle supports are
therefore excluded by the analytic good-support estimate itself; no quantitative
right inverse is assumed.

## 10. Ground-state consequence

Define

\[
 \eta_R
 ={\|D_R^{-1/2}[A_R-(\log R)D_R]D_R^{-1/2}\|
   \over\log R}.
\]

Then `eta_R->0` on the selected sequence. Together with `L-19826`,
`L-19830`, and the elementary upper pullback metric bound, the exact finite
matrix has

\[
 \mu_R=O((1+B_R)(\log R)d_4),
\]

while its second generalized scale is at least

\[
 c(\log R)d_6/K_R.
\]

Since

\[
 K_R(1+B_R)d_4/d_6\to0,
\]

the target excess divided by the complete gap tends to zero.

## 11. Proof boundary

- The Stieltjes, large-sieve, fold-measure, endpoint summation, diagonal
  selection, and source-injectivity consequences are proved here.
- The special-function profile and alias hypotheses are those in
  `L-19827/L-19829`; this theorem inherits their independent-review status.
- The false fixed polylogarithmic singular-value gate of `R-19806` is not used.
- No RH conclusion is claimed until the complete packet/target identification
  and imported CCM finite real-zero interfaces are composed and independently
  audited.
