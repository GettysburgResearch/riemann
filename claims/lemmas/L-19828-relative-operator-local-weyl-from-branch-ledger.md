# L-19828 — The complete branch ledger implies source-tail relative local Weyl

Claim ID: `L-19828`  
Status: **PROVED CONDITIONAL SOURCE-TAIL COMPOSITION; FINITE CCM PROJECTION REQUIRES L-19832**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Corrected: 2026-08-07 after the finite-projection residual audit  
Dependencies: complete branch/alias ledger `L-19827/L-19829`; support large sieve `L-16226`; arithmetic tail floor `L-19826`; Riemann--von Mangoldt  
Scope: relative local-Weyl theorem for the localized exact-radical source form, not yet the finite CCM Fourier projection

## 1. Statement

Let `S_R` be a finite signed packet of exact arithmetic sources. For every source
let

\[
 J=E(f),
 \qquad
 g=P_\lambda J,
 \qquad
 t=(I-P_\lambda)J.
 \tag{L-19828.1}
\]

Let

\[
 D_R=(\langle t_j,t_k\rangle)
 \tag{L-19828.2}
\]

be the complete ordinary omitted-tail Gram and let

\[
 A_R=Z(t,t)=Q_W(g,g)
 \tag{L-19828.3}
\]

be the exact localized source Weil matrix furnished by `L-16206`.

Assume the complete normalized profile conclusions of `L-19827/L-19829` and the
positive signed tail floor of `L-19826`. Then, in every sufficiently large
dyadic radial block `[T,2T]`, there is a set `G_T` of relative measure `1-o(1)`
such that for every `R in G_T`,

\[
 \boxed{
 {\left\|
 D_R^{-1/2}
 \left[A_R-(\log R)D_R\right]
 D_R^{-1/2}
 \right\|_{\rm op}
 \over\log R}
 \longrightarrow0.}
 \tag{L-19828.4}
\]

Hypothetical off-line zeros are included. The support translation has cancelled
and is never charged.

This theorem does **not** identify `A_R` with the finite CCM matrix on
`P_Ng`. The exact residual identity `L-19832` shows that the latter is the
zero-side form of `t+(I-P_N)g` and therefore has an additional projection gate.

## 2. Exact zero-side normalization

On one dyadic ordinate band,

\[
 A_R^{\rm band}
 ={1\over R}
 \sum_{\rho:\,aR\le|\gamma_\rho|\le bR}
 K_R\!\left({\gamma_\rho+i\delta_\rho\over R}
 \right),
 \tag{L-19828.5}
\]

where

\[
 \rho={1\over2}+\delta_\rho+i\gamma_\rho,
 \qquad |\delta_\rho|<1/2,
\]

and `K_R` is the polarized complete tail-profile kernel. The full source form is
a finite sum of such bands plus low- and high-frequency tails governed by the
same normalized endpoint estimates.

## 3. Slow phase-diagonal kernel

Use `L-19827/L-19829` to decompose

```text
K_R = K_R^diag + K_R^osc + K_R^fold + K_R^end.
```

The diagonal part contains every equal extracted phase, including the positive
self-Grams of higher aliases. In the whitened `D_R` metric,

\[
 \sup_x\|K_R^{\rm diag}(x)\|
 +\int_a^b\|\partial_xK_R^{\rm diag}(x)\|dx
 \le(\log R)^C.
 \tag{L-19828.6}
\]

Holomorphic Taylor expansion in the shrinking strip gives

\[
 \left\|
 K_R^{\rm diag}(x+i\delta/R)-K_R^{\rm diag}(x)
 \right\|
 \le { (\log R)^C\over R}.
 \tag{L-19828.7}
\]

Since the band contains `O(R log R)` zeros with multiplicity, the external
`1/R` normalization makes the complete diagonal horizontal replacement
`O((log R)^(C+1)/R)`.

## 4. Stieltjes local Weyl law for the slow kernel

Write

\[
 N(t)=M(t)+S(t),
 \qquad
 M'(t)=c_0\log t+c_1+O(t^{-1}),
 \qquad
 S(t)=O(\log(t+2)).
 \tag{L-19828.8}
\]

The normalization constant `c_0` is absorbed into `D_R`. The main density gives

\[
 {1\over R}\int_{aR}^{bR}K_R^{\rm diag}(t/R)dM(t)
 = (\log R)D_R^{\rm diag}+O(D_R^{\rm diag}).
 \tag{L-19828.9}
\]

For the remainder, Stieltjes integration by parts gives

\[
\begin{aligned}
 {1\over R}\int K_R^{\rm diag}(t/R)dS(t)
 ={}&{1\over R}[K_R^{\rm diag}(t/R)S(t)]_{aR}^{bR}\\
 &-{1\over R^2}\int_{aR}^{bR}S(t)
   \partial_xK_R^{\rm diag}(t/R)dt.
\end{aligned}
 \tag{L-19828.10}
\]

Using (L-19828.6) and (L-19828.8),

\[
 \left\|
 {1\over R}\int K_R^{\rm diag}(t/R)dS(t)
 \right\|
 \le { (\log R)^C\over R}.
 \tag{L-19828.11}
\]

Thus

\[
 A_R^{\rm diag}
 = (\log R)D_R^{\rm diag}+O(D_R^{\rm diag})
 +O_D((\log R)^C/R).
 \tag{L-19828.12}
\]

## 5. Oscillatory branch families

Every unequal-phase branch family has the form

\[
 Z_T(R)
 ={1\over R}
 \sum_{\gamma\in\Gamma_T}
 e^{iR\Delta S(\gamma/R)}A_\gamma(R),
 \qquad T\le R\le2T,
 \tag{L-19828.13}
\]

with

\[
 \|A_\gamma(R)\|+R\|A_\gamma'(R)\|
 \le(\log T)^C
 \tag{L-19828.14}
\]

by `L-19827/L-19829`. The phase partition has the separation required by
`L-16226`, so

\[
 {1\over T}\int_T^{2T}\|Z_T(R)\|_{\rm HS}^2dR
 \le { (\log T)^C\over T}.
 \tag{L-19828.15}
\]

With threshold `T^-1/8`, Markov and a union bound over the polylogarithmic family
count leave a relative-measure `1-o(1)` set on which every compact oscillatory
family is `o(1)` simultaneously.

For off-line zeros, the shrinking-strip expansion contributes the bounded
factor `exp[-delta S'(x)]`; the extracted amplitudes still satisfy
(L-19828.14). No zero-density estimate and no smallness of `delta` are used.

## 6. Fold, endpoint, and infinite-alias families

The Airy/fold contribution is

\[
 O(R^{-1/3}(\log R)^C),
 \tag{L-19828.16}
\]

or may be bounded through its `O(R^-2/3)` frequency width and the unit-window
zero count.

For the first endpoint channel, the alias Gram uses the collectively summed
`L2` logarithmic function of `L-19829`. For support averaging, retain the
individual aliases: the `k`-th coefficient is `O(k^-1)` and one integration by
parts in its `k`-dependent support phase supplies a second `k^-1`. Hence the
complete endpoint support ledger is majorized by

\[
 \sum_{k=2}^\infty k^{-2}<\infty.
 \tag{L-19828.17}
\]

Higher channels and the retained radial remainder are absolutely summable.
Thus all fold, endpoint, and infinite-alias errors are `o(1)` simultaneously on
the common good-support set.

## 7. Reassembly with the exact continuous tail Gram

The continuous source-tail Gram has the same branch decomposition. The
stationary, fold, and collective endpoint estimates give

\[
 \left\|
 D_R^{-1/2}(D_R-D_R^{\rm diag})D_R^{-1/2}
 \right\|
 \le R^{-1/3}(\log R)^C.
 \tag{L-19828.18}
\]

Therefore replacing `(log R)D_R^diag` by `(log R)D_R` costs `o(log R)` in the
whitened metric. Combining Sections 3--6 proves (L-19828.4).

## 8. What this theorem supplies

On the good-support sequence,

\[
 (1-\eta_R)(\log R)D_R
 \preceq A_R\preceq
 (1+\eta_R)(\log R)D_R,
 \qquad \eta_R\to0.
 \tag{L-19828.19}
\]

Together with `L-19826`, this proves the source-localized target scale and
complete signed `d_6` gap. It also proves positivity of the localized source
form.

## 9. What it does not supply

Let

\[
 v=P_Ng,
 \qquad q=(I-P_N)g.
\]

The finite CCM matrix is

\[
 A_{\rm CCM}=Z(t+q,t+q),
\]

not `Z(t,t)`. To promote (L-19828.19) to the exact finite CCM space, one must
prove either

\[
 \|D_t^{-1/2}D_qD_t^{-1/2}\|\to0
 \tag{L-19828.20}
\]

and extend the branch ledger to the cross and self terms involving `q`, or use
the local Möbius extension `L-20301` and prove an equivalent signed hierarchy
and scalarization for its explicit lower tail.

The absolute quadratic-log target approximation of `L-16213` is not sufficient
for (L-19828.20), because the prolate tail scales are exponentially smaller.

## 10. Proof boundary

- The Stieltjes, support-large-sieve, fold, endpoint, and diagonal-selection
  arguments are complete conditional on the explicit normalized radial theorem
  `L-19827/L-19829`.
- The theorem is correctly scoped to the exact localized source form.
- The finite CCM Fourier-projection assembly remains open as `L-19832`.
- No RH conclusion follows from this theorem alone.
