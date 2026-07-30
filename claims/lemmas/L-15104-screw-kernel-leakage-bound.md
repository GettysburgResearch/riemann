# L-15104 — Unconditional screw-kernel growth and double-exponential radical leakage

Claim ID: `L-15104`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-10`  
Created: 2026-07-30  
Dependencies: the exact screw normalization `D-9501`; Suzuki's identity `QW(v,w)=<GDv,Dw>` on the smooth core; `L-15101`; elementary bounds for the von Mangoldt sum and Lerch series  
Scope: close the numerator side of the exact radical leakage/gap criterion up to directed constants  
Related counterexample candidates: none

## 1. Logarithmic-coordinate target

Let `k=E(h)` be the exact target from `L-15101` and define

\[
 K(x)=k(e^x),
 \qquad x\in\mathbb R.
 \tag{L-15104.1}
\]

By multiplicative inversion, `K` is even. Put

\[
 \mathcal A_h(y)=\frac12h(y)+yh'(y).
\]

A direct differentiation of (L-15101.1) gives

\[
 \mathcal A_h(y)
 =\left(-2\pi^3y^6+\frac{15\pi^2}{2}y^4
               -\frac{15\pi}{4}y^2\right)e^{-\pi y^2}.
 \tag{L-15104.2}
\]

For `x>=0`,

\[
 K'(x)=e^{x/2}\sum_{n\ge1}\mathcal A_h(ne^x).
 \tag{L-15104.3}
\]

Define

\[
 C_6=\sum_{n\ge1}n^6e^{-\pi(n^2-1)},
\]

and

\[
 C_A=\left(2\pi^3+\frac{15\pi^2}{2}
                    +\frac{15\pi}{4}\right)C_6.
\]

Then, for `x>=0`,

\[
 \boxed{
 |K'(x)|\le C_Ae^{13x/2}e^{-\pi e^{2x}}.}
 \tag{L-15104.4}
\]

Together with `L-15101`, this gives explicit double-exponential bounds for both
`K` and `K'` on the two logarithmic tails.

## 2. Unconditional derivative bound for the screw kernel

Let `g=-Psi` be the zeta screw function in `D-9501`. There are explicit
constants `C_0,C_infinity>0` such that, away from the prime-power knots and with
one-sided values at knots,

\[
 \boxed{
 |g'(s)|\le C_0(1+|\log|s||),
 \qquad 0<|s|\le1,}
 \tag{L-15104.5}
\]

and

\[
 \boxed{
 |g'(s)|\le C_\infty(1+|s|)e^{|s|/2},
 \qquad |s|\ge1.}
 \tag{L-15104.6}
\]

These estimates are unconditional.

### Near zero

For `0<|s|<log 2`, the prime sum is empty. Differentiating the Lerch series gives
terms bounded by a constant multiple of

\[
 \sum_{m\ge1}\frac{e^{-2m|s|}}m
 =-\log(1-e^{-2|s|})
 =O(1+|\log|s||).
\]

All remaining terms have bounded derivative near zero.

### Away from zero

On a prime-knot cell, the derivative of the prime term has magnitude at most

\[
 \sum_{n\le e^{|s|}}\frac{\Lambda(n)}{\sqrt n}
 \le |s|\sum_{n\le e^{|s|}}n^{-1/2}
 \le2|s|e^{|s|/2}.
 \tag{L-15104.7}
\]

The elementary exponential terms have derivative `O(e^(|s|/2))`; the Lerch
term is exponentially bounded; and the linear term is constant. This proves
(L-15104.6). The derivative jumps at prime knots but remains locally bounded on
each side; no delta mass occurs in the first distributional derivative because
`g` itself is continuous.

## 3. Smooth tail and leakage convolution

Let `a>=2` and choose an even smooth cutoff `chi_a` with

```text
chi_a(x)=1 for |x|<=a-1,
chi_a(x)=0 for |x|>=a,
|chi_a'(x)|<=C_chi.
```

Put

\[
 p_a=\chi_aK,
 \qquad
 t_a=(1-\chi_a)K.
 \tag{L-15104.8}
\]

There is an explicit constant `C_T` such that

\[
 |t_a'(x)|
 \le C_Te^{13|x|/2}e^{-\pi e^{2|x|}}
 \quad(|x|\ge a-1).
 \tag{L-15104.9}
\]

Define, for `|y|<=a`,

\[
 F_a(y)=\int_{\mathbb R}g(y-x)t_a'(x)\,dx.
 \tag{L-15104.10}
\]

The integral and its first derivative converge absolutely. Splitting the
integral into `|x-y|<=1` and `|x-y|>1`, using respectively (L-15104.5) and
(L-15104.6), yields explicit constants `C_L>0` and an integer `m` such that

\[
 \boxed{
 \sup_{|y|\le a}|F_a'(y)|
 \le C_L(1+a)^m e^{15a/2}
       e^{-\pi e^{2(a-1)}}.}
 \tag{L-15104.11}
\]

One may take a deliberately nonoptimal fixed `m`, for example `m=3`, after
enlarging `C_L` on the compact range `2<=a<=a_0`. The proof uses only:

- integrability of `1+|log|s||` on `[-1,1]`;
- monotonic decrease of `e^(7x)e^(-pi e^(2x))` for sufficiently large `x`;
- symmetry of the two tails.

Every constant can be replaced by a directed rational upper enclosure in a
production certificate.

## 4. L2-dual localized residual

On the smooth core, Suzuki's identity is

\[
 QW(v,w)=\langle GDv,Dw\rangle.
 \tag{L-15104.12}
\]

For `w in H_0^1(-a,a)`, integration by parts gives

\[
 QW(t_a,w)
 =-\int_{-a}^{a}F_a'(y)\overline{w(y)}\,dy
 \tag{L-15104.13}
\]

up to the harmless fixed `i` factors in `D=i d/dx`. Therefore the ordinary
`L2` leakage norm obeys

\[
 \boxed{
 \ell_{2,a}:=
 \sup_{0\ne w\in H_0^1(-a,a)}
 \frac{|QW(t_a,w)|}{\|w\|_2}
 \le
 \sqrt{2a}\,C_L(1+a)^m e^{15a/2}
 e^{-\pi e^{2(a-1)}}.}
 \tag{L-15104.14}
\]

This is double-exponential decay in the logarithmic support `a`.

## 5. Spectral consequence

Suppose the exact localized complement gates of `L-15102` hold with ordinary
`L2` coercivity `g_a>0`. Then a suitable scalar multiple of the local ground
state satisfies

\[
 \|c_a\xi_a-p_a\|_2\le\frac{\ell_{2,a}}{g_a}.
 \tag{L-15104.15}
\]

For functions supported in `[-a,a]`,

\[
 \sup_{|\operatorname{Im}z|\le\sigma}|\widehat f(z)|
 \le\sqrt{2a}\,e^{\sigma a}\|f\|_2.
 \tag{L-15104.16}
\]

Consequently the exact radical route closes if, for every fixed
`0<=sigma<1/2`,

\[
 \sqrt{2a}\,e^{\sigma a}\frac{\ell_{2,a}}{g_a}\longrightarrow0.
 \tag{L-15104.17}
\]

By (L-15104.14), the following explicit growth condition is sufficient:

\[
 \boxed{
 \limsup_{a\to\infty}
 \frac{\log(g_a^{-1})}{e^{2a}}
 <\frac\pi{e^2}.}
 \tag{L-15104.18}
\]

In particular, any polynomial, ordinary exponential, stretched exponential, or
`exp(o(e^(2a)))` collapse of the continuum gap is harmless. Only a gap collapse
on the same `exp(-constant*e^(2a))` scale as the Gaussian source tail can defeat
this argument.

## Why this advances the blocker

Before this lemma, both numerator and denominator in the leakage/gap ratio were
open. The explicit screw formula and exact Hermite target make the numerator
structurally small without RH. The remaining positive-route question is now a
quantitative lower bound on the continuum simple-even separation `g_a`, or an
alternative no-crossing theorem that supplies the same effect.

## Gap audit

- The displayed constants are constructive but have not yet been instantiated
  by a directed checker. The asymptotic exponents, not their optimization, are
  the present theorem target.
- Equation (L-15104.12) and the precise sign/normalization of `G` remain imported
  from Suzuki and `D-9501`.
- Passing from the smooth core to the closed localized form requires the standard
  form-density argument and a verified common-domain cutoff approximation.
- The projection `P_a` onto zero-integral derivative data in Suzuki's `G_a`
  causes no change on `Dw` for `w in H_0^1`, but this must be retained in a
  production normalization audit.
- No lower bound for `g_a` is proved here. Therefore this lemma does not by itself
  prove RH.
