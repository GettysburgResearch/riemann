# L-15619 — Near-quadratic Gevrey radical packets

Claim ID: `L-15619`  
Title: Compact Gevrey atoms give rank `lambda^2/(log lambda)^p` exact-radical packets with superpolynomially small complete tails  
Status: `PROPOSED — COMPLETE SOURCE-PACKET PROOF; FORM NORMALIZATION INHERITED`  
Authoring agent: `gpt56-pro-09-f`  
Created: 2026-07-31  
Dependencies: `L-15616`, `L-15617`; existence of compact Gevrey atoms with stretched-exponential Fourier decay; the Connes--Consani Poisson/radical identity  
Scope: maximize the proof-grade capacity available to `L-15618`  
Related counterexample candidates: none

## 1. Purpose

`L-15616` obtains exact repaired packets of rank

\[
 d_\lambda\gg\lambda^{2-\delta}
\]

from a fixed Schwartz atom at spatial scale `lambda^(delta-1)`. A compact
Gevrey atom permits a polylogarithmic, rather than power, scale loss while its
Fourier tail still beats every inverse power of `lambda`.

## 2. Fixed Gevrey atom

Fix any real number

\[
 p>1.
 \tag{L-15619.1}
\]

Choose

\[
 \frac1p<\beta<1.
 \tag{L-15619.2}
\]

There exists a real function

\[
 \psi\in C_c^\infty(-1/4,1/4),
 \qquad
 \|\psi\|_2=1,
 \qquad
 \int\psi=0,
 \tag{L-15619.3}
\]

and constants `c,C>0` such that

\[
 \boxed{
 |\widehat\psi(\xi)|
 \le C\exp(-c|\xi|^\beta)
 \qquad(\xi\in\mathbb R).}
 \tag{L-15619.4}
\]

For example, differentiate and normalize a compact Gevrey bump of order
strictly below `p`. Differentiation enforces zero integral and preserves a
stretched-exponential estimate after changing the constants.

## 3. Packet scale and rank

Put

\[
 q_\lambda=(\log\lambda)^p,
 \qquad
 \ell_\lambda=\frac{q_\lambda}{\lambda}.
 \tag{L-15619.5}
\]

Inside

\[
 I_\lambda^+=\left(\frac58\lambda,\frac78\lambda\right)
\]

choose centers whose scaled supports are disjoint, exactly as in `L-15616`, and
define

\[
 b_{\lambda,k}(x)
 =\ell_\lambda^{-1/2}
 \psi\!\left(\frac{x-x_{\lambda,k}}{\ell_\lambda}\right),
 \tag{L-15619.6}
\]

\[
 f_{\lambda,k}(x)
 =2^{-1/2}
 \bigl(b_{\lambda,k}(x)+b_{\lambda,k}(-x)\bigr).
 \tag{L-15619.7}
\]

Then the family is orthonormal, real, even, compactly supported, vanishes at
zero, and has zero integral. Its size satisfies

\[
 \boxed{
 d_\lambda
 \ge c_0\frac{\lambda}{\ell_\lambda}-1
 =c_0\frac{\lambda^2}{(\log\lambda)^p}-1.}
 \tag{L-15619.8}
\]

Every coefficient combination is therefore an exact admissible source without
an external repair.

## 4. Dimension-free arithmetic Gram

Let

\[
 \mathcal F_\lambda c
 =\sum_{k=1}^{d_\lambda}c_kf_{\lambda,k},
 \qquad
 r_\lambda(c)=E(\mathcal F_\lambda c).
 \tag{L-15619.9}
\]

For `u in I_lambda^+`, all arithmetic summands with `n>=2` lie beyond the
source support. Hence

\[
 r_\lambda(c)(u)=u^{1/2}\mathcal F_\lambda c(u).
\]

Exactly as in `L-15616`, one obtains

\[
 \boxed{
 \|r_\lambda(c)\|_{L^2(d^*u)}^2
 \ge\frac12\|c\|_2^2.}
 \tag{L-15619.10}
\]

The global arithmetic Gram floor is independent of packet dimension.

## 5. Uniform stretched-exponential Fourier synthesis

Translation, reflection, and scaling in (L-15619.4), followed by
Cauchy--Schwarz over the packet, give for `||c||_2=1`

\[
\begin{aligned}
 |\widehat{\mathcal F_\lambda c}(\xi)|
 &\le
 C\sqrt{d_\lambda\ell_\lambda}
 \exp[-c(\ell_\lambda|\xi|)^\beta]\\
 &\le
 C'\lambda^{1/2}
 \exp[-c(\ell_\lambda|\xi|)^\beta].
\end{aligned}
 \tag{L-15619.11}
\]

For `v>=lambda`, `ell_lambda v>=q_lambda`. The elementary integral comparison

\[
 \sum_{n\ge1}e^{-c(yn)^\beta}
 \le C_\beta e^{-c' y^\beta}
 \qquad(y\ge1)
 \tag{L-15619.12}
\]

therefore gives

\[
 \boxed{
 \left|
 \sum_{n\ge1}
 \widehat{\mathcal F_\lambda c}(nv)
 \right|
 \le
 C\lambda^{1/2}
 \exp[-c'(\ell_\lambda v)^\beta].}
 \tag{L-15619.13}
\]

## 6. Complete exterior-tail estimate

The upper multiplicative tail is identically zero. On the lower tail, the exact
Poisson identity and `v=1/u` give

\[
\begin{aligned}
 \|1_{(0,1/\lambda)}r_\lambda(c)\|_2^2
 &=\int_\lambda^\infty
 \left|
 \sum_{n\ge1}
 \widehat{\mathcal F_\lambda c}(nv)
 \right|^2dv\\
 &\le
 C\lambda^2
 \exp[-c''q_\lambda^\beta].
\end{aligned}
 \tag{L-15619.14}
\]

Thus

\[
 \boxed{
 \|T_\lambda\|_{\ell^2\to L^2(d^*u)}
 \le
 C\lambda
 \exp[-c(\log\lambda)^{p\beta}].}
 \tag{L-15619.15}
\]

For every `0<=tau<1/2`, the multiplicative Hardy weight gives

\[
 \boxed{
 \|T_\lambda\|_{\ell^2\to X_{\lambda,\tau}}
 \le
 C_\tau\lambda^{1+\tau}
 \exp[-c(\log\lambda)^{p\beta}].}
 \tag{L-15619.16}
\]

A fixed finite number of logarithmic derivatives or polynomial weights changes
only the prefactor by a power of `lambda` and `log lambda`.

Because

\[
 p\beta>1,
\]

one has, for every `M>0`,

\[
 \boxed{
 \lambda^A(\log\lambda)^B
 e^{-c(\log\lambda)^{p\beta}}
 =O_M(\lambda^{-M})}
 \tag{L-15619.17}
\]

for all fixed `A,B`. Hence every declared finite tail/form seminorm is rapidly
decreasing uniformly over the whole growing packet.

## 7. Localized Gram and complete Weil residual

Let

\[
 J_\lambda
 =1_{[1/\lambda,\lambda]}E\mathcal F_\lambda.
\]

Equations (L-15619.10) and (L-15619.15) imply

\[
 \boxed{
 J_\lambda^*J_\lambda
 \succeq(1/2-o(1))I.}
 \tag{L-15619.18}
\]

The radical transport and componentwise explicit-formula proof of `L-15617`
then applies verbatim, with the stretched-exponential tail replacing its
Schwartz estimate. Provided the exact form-continuity constants have at most
polynomial support growth,

\[
 \boxed{
 \alpha_\lambda=O_M(\lambda^{-M}),
 \qquad
 \beta_\lambda=O_M(\lambda^{-M})}
 \tag{L-15619.19}
\]

for every `M`, uniformly at rank (L-15619.8).

## 8. Capacity consequence

For every fixed `p>1`, the exact near-radical capacity is now

\[
 \boxed{
 d_\lambda
 \gg_p\frac{\lambda^2}{(\log\lambda)^p},}
 \tag{L-15619.20}
\]

with complete compression and cross residual smaller than every inverse power.
Thus the threshold-clipped scalar target of `L-15618` reduces to

\[
 \boxed{
 \operatorname{Tr}
 \bigl(D_\lambda-(G_\lambda-\Gamma_\lambda)I\bigr)_+
 \le
 d_\lambda(\Gamma_\lambda-\alpha_\lambda).}
 \tag{L-15619.21}
\]

The source side is within an arbitrarily small polylogarithmic loss of the
natural one-dimensional time--frequency phase-space scale.

## 9. Why the logarithmic loss remains

A nonzero compactly supported function cannot have genuine exponential Fourier
decay. The Gevrey exponent must satisfy `beta<1`; consequently the simple fixed-
atom construction needs `q_lambda` larger than `log lambda` by a positive
power. Removing the remaining logarithmic loss requires a support-dependent
prolate/concentration packet rather than one fixed rescaled atom.

## 10. Proof boundary

- The compact Gevrey construction and stretched-exponential estimates are
  standard and unconditional.
- The arithmetic Gram floor is the exact local `n=1` identity and uses no zeta
  lower bound.
- The Poisson/radical and explicit-formula normalization are inherited from
  `L-15616/L-15617` and require the same independent convention audit.
- The theorem closes the near-radical capacity/rate side, not the complete
  arithmetic clipped-deficit estimate.
- No proof of RH is claimed.
