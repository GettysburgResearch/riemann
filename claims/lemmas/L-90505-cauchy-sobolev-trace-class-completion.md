# L-90505 — A Cauchy–Sobolev completion gives an explicit trace-class zero kernel

Claim ID: `L-90505`  
Status: **PROPOSED COMPLETE FUNCTIONAL-ANALYTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: the centered Weil form; the global Xi-cardinal source theorem on PR #365; the classical local zero count  
Scope: an alternative fixed Hilbert completion with an explicit reproducing kernel; no positivity or RH conclusion by itself

## 1. Reverse-order exponential Sobolev map

Fix

\[
 \frac12<a<c,
 \qquad
 w_a(u)=e^{-a|u|},
 \qquad
 B_c=(c^2-\partial_u^2)^{-1}.
 \tag{L-90505.1}
\]

The resolvent kernel is

\[
 b_c(x)=\frac{e^{-c|x|}}{2c}.
 \tag{L-90505.2}
\]

Define

\[
 \boxed{J_{a,c}=B_cM_{w_a}:L^2(\mathbb R)\to L^2(\mathbb R).}
 \tag{L-90505.3}
\]

Its integral kernel is

\[
 K_J(x,u)=b_c(x-u)w_a(u).
\]

Hence

\[
 \|J_{a,c}\|_{\mathrm{HS}}^2
 =\|b_c\|_2^2\|w_a\|_2^2<\infty.
 \tag{L-90505.4}
\]

The order in (L-90505.3) is deliberate: the Fourier multiplier of `B_c` remains visible at complex evaluation points.

## 2. Exact evaluation kernel

Let `g in L^2` and `f=J_(a,c)g`. Since `w_a g in L^1` and `c>a`, Fubini gives, throughout `|Im z|<a`,

\[
 \widehat f(z)
 =\frac{\widehat{w_ag}(z)}{c^2+z^2}.
 \tag{L-90505.5}
\]

Thus evaluation at `z` is represented on coefficient space by

\[
 v_z(u)=
 \frac{e^{-a|u|}e^{-i\bar z u}}
      {c^2+\bar z^2}.
 \tag{L-90505.6}
\]

The reproducing kernel is therefore explicit:

\[
\begin{aligned}
 \mathcal K_{a,c}(z,w)
 &=\langle v_w,v_z\rangle\\
 &=\frac{1}{(c^2+z^2)(c^2+\bar w^2)}
   \int_{\mathbb R}e^{-2a|u|}e^{i(z-\bar w)u}\,du\\
 &=\boxed{
 \frac{4a}
 {(c^2+z^2)(c^2+\bar w^2)
  [4a^2+(z-\bar w)^2]} }.
\end{aligned}
 \tag{L-90505.7}
\]

For `z=x+iy`, `|y|<=1/2`,

\[
 \boxed{
 \mathcal K_{a,c}(z,z)
 =\frac{a}
 {(a^2-y^2)|c^2+z^2|^2}
 \ll_{a,c}(1+x^2)^{-2}.
 }
 \tag{L-90505.8}
\]

Consequently

\[
 \sum_\rho m_\rho\mathcal K_{a,c}(\gamma_\rho,\gamma_\rho)<\infty
 \tag{L-90505.9}
\]

by `N(t+1)-N(t)=O(log(t+3))`.

For distinct nodes in the strip, the Gram matrix is strictly positive: it is the Gram of the distinct exponential functions

\[
 u\mapsto
 \frac{e^{-a|u|}e^{-i\bar z_j u}}
      {c^2+\bar z_j^2},
\]

and a nontrivial exponential polynomial cannot vanish almost everywhere on either half-line.

## 3. Trace-class prime shifts

Let `T_y f(x)=f(x-y)`. Put

\[
 \phi_x(u)=w_a(u)b_c(x-u),
 \qquad
 F(x)=\|\phi_x\|_2.
\]

The operator has the nuclear representation

\[
 J_{a,c}^*T_yJ_{a,c}
 =\int_{\mathbb R}
   \phi_x\phi_{x-y}^*\,dx.
 \tag{L-90505.10}
\]

Because `c>a`,

\[
\begin{aligned}
 F(x)^2
 &=\frac1{4c^2}\int
   e^{-2a|u|}e^{-2c|x-u|}\,du\\
 &\le
 \frac{e^{-2a|x|}}{4c^2}
 \int e^{-2(c-a)|x-u|}\,du\\
 &=\frac{e^{-2a|x|}}
 {4c^2(c-a)}.
\end{aligned}
 \tag{L-90505.11}
\]

Therefore

\[
\begin{aligned}
 \|J_{a,c}^*T_yJ_{a,c}\|_1
 &\le\int F(x)F(x-y)\,dx\\
 &\le\boxed{
 \frac{e^{-a|y|}}
 {4c^2(c-a)}
 \left(|y|+\frac1a\right)}.
\end{aligned}
 \tag{L-90505.12}
\]

It follows that

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \|J_{a,c}^*(T_{\log n}+T_{-\log n})J_{a,c}\|_1<\infty.
 \tag{L-90505.13}
\]

Thus the zero side and the complete prime-power side both define trace-class operators, with no sharp support cutoff.

## 4. Global cardinal directions remain present

Let `q_omega` be any super-Gaussian Xi-cardinal source from PR #365. Set

\[
 g_\omega
 =w_a^{-1}(c^2-\partial_u^2)q_\omega.
 \tag{L-90505.14}
\]

Every derivative of `q_omega` decays faster than every Gaussian, so `g_omega in L^2` and

\[
 J_{a,c}g_\omega=q_\omega.
 \tag{L-90505.15}
\]

Hence this explicit Cauchy–Sobolev metric retains every fixed global cardinal witness.

## 5. Relation to `L-90501`

`L-90501` uses `M_w B` and obtains a smooth confinement with a robust abstract evaluation estimate. The present lemma uses `B_c M_w` and the cusp weight `e^{-a|u|}` to expose the exact strip kernel (L-90505.7). Both completions have the same zero-side Pontryagin index once global cardinals are included.

The explicit kernel is useful for:

- exact finite zero-Gram calculations;
- certified interpolation costs;
- pole-null projections;
- integrable/Cauchy determinant experiments.

## 6. Proof boundary

Proved here:

- an explicit Hilbert-Schmidt test map;
- the exact Cauchy–Sobolev evaluation kernel;
- fourth-power ordinate decay and trace-class zero summability;
- an explicit exponentially decaying prime-shift trace-norm bound;
- inclusion of every fixed Xi-cardinal source.

Not proved:

- positivity of the completed Weil operator;
- a stable determinant theorem for the Cauchy kernel;
- RH.
