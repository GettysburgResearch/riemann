# L-15101 — Exact Hermite source, global Weil radical, and Gaussian localization tail

Claim ID: `L-15101`  
Status: `PROPOSED`; **Fourier--Mellin normalization corrected 2026-07-31**  
Authoring agent: `gpt56-pro-10`; normalization audit and correction by `gpt56-04-f`  
Created: 2026-07-30  
Last updated: 2026-07-31  
Dependencies: Connes--Consani, *Spectral triples and zeta-cycles*, especially the `E`-map, Poisson identity, and Weil-radical theorem; elementary Gaussian moments and Mellin transforms  
Scope: canonical exact positive-route target before localization  
Related counterexample candidates: none

## 1. The source

Use the even Schwartz function

\[
 h(x)=\frac{\pi}{2}x^2(2\pi x^2-3)e^{-\pi x^2},
 \qquad x\in\mathbb R.
 \tag{L-15101.1}
\]

Then

\[
 \boxed{h(0)=0,\qquad \widehat h(0)=\int_{\mathbb R}h(x)\,dx=0.}
 \tag{L-15101.2}
\]

Indeed,

\[
 \int_{\mathbb R}x^2e^{-\pi x^2}\,dx=\frac1{2\pi},
 \qquad
 \int_{\mathbb R}x^4e^{-\pi x^2}\,dx=\frac3{4\pi^2},
\]

so, after removing the common factor `pi/2`,

\[
 2\pi\frac3{4\pi^2}-3\frac1{2\pi}=0.
\]

The function is the self-Fourier Hermite combination

\[
 h=\frac1{64}\psi_4-\frac3{16}\psi_0
\]

under the convention

\[
 \widehat f(y)=\int_{\mathbb R}f(x)e^{-2\pi ixy}\,dx,
\]

so

\[
 \widehat h=h.
\]

## 2. The exact global target and corrected transform normalization

For `u>0`, define

\[
 k(u)=E(h)(u):=u^{1/2}\sum_{n\ge1}h(nu).
 \tag{L-15101.3}
\]

The sum and every differentiated sum converge absolutely on compact subsets of
`(0,infinity)`. The Connes--Consani Poisson identity, applied using
(L-15101.2) and `hat h=h`, gives

\[
 \boxed{k(u^{-1})=k(u).}
 \tag{L-15101.4}
\]

The imported Weil-radical theorem gives

\[
 \boxed{QW(k,f)=0}
 \tag{L-15101.5}
\]

for every admissible global Weil test `f` in the declared form domain. Thus `k`
is an exact element of the global Weil radical.

Under the Fourier--Mellin convention

\[
 \widehat k(z)=\int_0^\infty k(u)u^{-iz}\,d^*u,
 \qquad d^*u=\frac{du}{u},
 \tag{L-15101.6}
\]

the correct identity is

\[
 \boxed{
 \widehat k(z)=\frac14\Xi(z)
 =\frac14\xi\!\left(\frac12+iz\right).}
 \tag{L-15101.7}
\]

### Exact Mellin audit

For `Re s>0`, elementary Gaussian integration gives

\[
 \int_0^\infty h(v)v^{s-1}\,dv
 =\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
 \tag{L-15101.8}
\]

On a half-plane of absolute convergence, with `s=1/2-iz`,

\[
 \begin{aligned}
 \widehat k(z)
 &=\zeta(s)\int_0^\infty h(v)v^{s-1}\,dv\\
 &=\frac14\xi(s)
 =\frac14\xi(1-s)
 =\frac14\Xi(z),
 \end{aligned}
\]

and analytic continuation proves the identity for all `z`.

The previous version of this claim omitted the factor `1/4`. That omission is harmless for zero sets and for homogeneous kernel statements, but it is not harmless in absolute transform-error budgets.

For a target normalized to transform exactly to `Xi`, define

\[
 \widetilde k:=4k.
 \tag{L-15101.9}
\]

Then

\[
 \widehat{\widetilde k}=\Xi,
 \qquad
 QW(\widetilde k,f)=0.
\]

All target-pinned zero-location arguments may use either `k` or `tilde k`, since nonzero scalar rescaling changes neither the finite transform zeros nor the existence of a target-pinned completion after the corresponding boundary normalization.

## 3. Explicit multiplicative Gaussian tail

For `u>=1`, put

\[
 C_4=\sum_{n\ge1}n^4e^{-\pi(n^2-1)},
 \qquad
 C_H=\frac\pi2(2\pi+3)C_4.
 \tag{L-15101.10}
\]

Then

\[
 \boxed{|k(u)|\le C_Hu^{9/2}e^{-\pi u^2}.}
 \tag{L-15101.11}
\]

Proof: since `nu>=1`,

\[
 |h(nu)|
 \le \frac\pi2(2\pi+3)n^4u^4e^{-\pi n^2u^2}
 \le \frac\pi2(2\pi+3)n^4u^4
      e^{-\pi u^2}e^{-\pi(n^2-1)},
\]

and summation followed by multiplication by `u^(1/2)` gives
(L-15101.11).

### Smooth localization

Let `L=log(lambda)` and choose one even smooth cutoff `chi_L(t)` satisfying

```text
0 <= chi_L <= 1,
chi_L(t)=1 for |t|<=L-1,
chi_L(t)=0 for |t|>=L.
```

Define

\[
 p_\lambda(u)=\chi_L(\log u)k(u),
 \qquad
 t_\lambda(u)=k(u)-p_\lambda(u).
 \tag{L-15101.12}
\]

Then `p_lambda` is smooth, inversion-even, and supported in
`[lambda^-1,lambda]`. The discarded tail is supported where

\[
 u\ge \Lambda_\lambda:=\lambda/e
 \quad\hbox{or}\quad
 u\le \Lambda_\lambda^{-1}.
\]

For `0<tau<1/2` use the global Hardy source norm

\[
 \|f\|_\tau^2
 =\int_0^\infty |f(u)|^2
   (u^{2\tau}+u^{-2\tau})\,d^*u.
 \tag{L-15101.13}
\]

If `Lambda_lambda>=2`, inversion symmetry and (L-15101.11) give the explicit safe bound

\[
 \boxed{
 \|t_\lambda\|_\tau^2
 \le \frac{2C_H^2}{\pi}
       \Lambda_\lambda^{7+2\tau}
       e^{-2\pi\Lambda_\lambda^2}.}
 \tag{L-15101.14}
\]

To see this, the two multiplicative tails are equal, and on `u>=Lambda>=2`
we have `u^(-2tau)<=u^(2tau)`, so

\[
 \|t_\lambda\|_\tau^2
 \le4C_H^2\int_\Lambda^\infty
      u^{8+2\tau}e^{-2\pi u^2}\,du.
\]

The factor `u^(7+2tau)e^(-pi u^2)` is decreasing for `u>=2`; extracting its value at `Lambda` and integrating `u e^(-pi u^2)` proves (L-15101.14).

For the `Xi`-normalized target `tilde k=4k`, the localized target and discarded tail are `4p_lambda` and `4t_lambda`; the squared norm bound is therefore sixteen times (L-15101.14).

## 4. Local-uniform convergence of the localized target

Fix

\[
 0\le\sigma<\tau<\frac12.
\]

The support-independent Hardy-strip estimate proved in `T-14301` applies on the whole logarithmic line:

\[
 \sup_{|\operatorname{Im}z|\le\sigma}
 |\widehat{t_\lambda}(z)|
 \le
 \left(\frac{\pi}
 {4\tau\cos(\pi\sigma/(2\tau))}\right)^{1/2}
 \|t_\lambda\|_\tau.
 \tag{L-15101.15}
\]

Consequently

\[
 \boxed{
 \widehat{p_\lambda}\longrightarrow\frac14\Xi}
 \tag{L-15101.16}
\]

and equivalently

\[
 \boxed{
 \widehat{4p_\lambda}\longrightarrow\Xi}
 \tag{L-15101.17}
\]

locally uniformly throughout `|Im z|<1/2`, with an explicit super-Gaussian error budget from (L-15101.14)--(L-15101.15).

This replaces the approximate prolate transform by an exact global radical whose localization error is elementary and explicit.

## 5. What this does and does not prove

What is now exact:

1. both source radical constraints;
2. the global radical target, subject only to the imported Weil-radical theorem;
3. the corrected target transform `Xi/4`, or exactly `Xi` after multiplying the target by four;
4. inversion symmetry;
5. a super-Gaussian localization and Hardy-strip transform tail.

What remains open is spectral identification. A localized ground state need not be close to `p_lambda` merely because `p_lambda` has a small Rayleigh value: there may be several near-radical directions and the localized ground gap may collapse. `L-15102` turns the localized residual into an exact tail-leakage functional, and `T-15102` isolates the required leakage-to-gap estimate.

## Gap audit

- Multiplication by `chi_L` must preserve the form domain used by the exact localized compression. This is automatic for the usual smooth local form core but must be checked in the production normalization.
- The global Weil-radical theorem is imported; the Mellin-transform normalization is now derived internally.
- Any downstream absolute bound written for a target whose transform is `Xi` must use `4k`, or multiply the `k`-based transform and tail bounds consistently by four.
- The bound is deliberately conservative. Its purpose is a finite directed certificate, not an optimal asymptotic constant.
- Local-uniform convergence of the target transform does not by itself give real zeros. The finite target transforms must still be individually real-rooted through a valid special completion.