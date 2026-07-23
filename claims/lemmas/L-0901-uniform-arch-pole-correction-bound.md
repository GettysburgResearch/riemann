# L-0901 — Uniform high-carrier archimedean and pole correction bound

Claim ID: L-0901  
Title: Uniform operator bound for the exact D-0801 archimedean and pole corrections  
Status: PROPOSED  
Authoring agent: `gpt56-01-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0702's compact archimedean formula and the inherited Guinand--Weil normalization  
Scope: the equal-cell piecewise autocorrelation carrier family  
Related counterexample candidates: none

## Statement

Fix `c>=2`, put

\[
 L=\log c,\qquad \Delta=\frac{L}{2\pi},\qquad h=\frac{\Delta}{K},
\]

and use the `K`-cell D-0801 family at a carrier `T>0`. Normalize coefficient
vectors by

\[
 \|v\|_2=1.
\]

Then the Gram value is `h`, and the normalized exact matrix can be written

\[
 \widetilde Q_{\rm exact}(T,c,K)
 =\frac{\log(T/(2\pi))}{2\pi}I-S_K(T,c)+E_{\rm arch}+E_{\rm pole},
\]

where `S_K` is the complete finite prime Toeplitz matrix of L-0801. Conditional
on the exact block formulas and signs, the omitted correction obeys

\[
 \|E_{\rm arch}+E_{\rm pole}\|_{\rm op}
 \le B_{\rm arch}(T,c,K)+B_{\rm pole}(T,c,K),
\]

with

\[
 B_{\rm arch}
 =\frac1{\pi T}\left[
   \frac K L(\log K+2)+6K+5+\frac1L
 \right]
\]

and

\[
 B_{\rm pole}
 =\frac{4\sqrt c\,K^2}{\pi L T^2}.
\]

Consequently every exact normalized eigenvalue lies within the displayed total
bound of the corresponding complete-prime leading eigenvalue.

At the X-0901 endpoint

\[
 c=10^{11},\quad K=1024,\quad T=4709203636353.65,
\]

the ordinary decimal evaluation is

\[
 B_{\rm arch}<4.400401\times10^{-10},\qquad
 B_{\rm pole}<7.517\times10^{-16},
\]

so the total is below `4.401e-10`. This is more than `6.1e5` times smaller than
the reported complete-prime leading margin `2.6896626427e-4`.

This comparison does **not** certify that leading margin: the prime phases,
accumulation, and eigensolve in X-0901 remain ordinary numerical arithmetic.
It does show that the exact archimedean and pole blocks are not a plausible
source of a sign reversal at this carrier if the leading matrix is reproduced.

## Normalized autocorrelation

For `0<=d<K`, define

\[
 c_d=\sum_{j=0}^{K-1-d}v_{j+d}\overline{v_j},
 \qquad c_K=0.
\]

Then `c_0=1` and Cauchy--Schwarz gives `|c_d|<=1`. Put

\[
 H=\frac{2L}{K}.
\]

For `t in [dH,(d+1)H]`, with `theta=(t-dH)/H`, define

\[
 r_v(t)=(1-\theta)c_d+\theta c_{d+1}.
\]

The normalized Fourier weight at `xi=t/(4*pi)` is

\[
 \frac{\widehat g_{T,v}(t/(4\pi))}{h}
 =\operatorname{Re}\left(e^{-iTt/2}r_v(t)\right).
\]

The elementary bounds used below are

\[
 |r_v(t)|\le1,
 \qquad
 \operatorname{Var}(r_v)\le2K,
 \qquad
 |r_v'(t)|\le\frac2H
\]

on each open cell.

## Exact archimedean residual

Let

\[
 a(t)=\frac{e^{-t/4}}{1-e^{-t}},
 \qquad
 b(t)=a(t)-\frac1t,
 \qquad \omega=\frac T2.
\]

The compact formula inherited from L-0702 gives the normalized archimedean
quadratic value

\[
 \frac{A(v)}h=\frac1{2\pi}\left[
 \int_0^{2L}\left(
 \frac{e^{-t}}t-a(t)\operatorname{Re}(e^{-i\omega t}r_v(t))
 \right)dt+E_1(2L)-\log\pi
 \right],
\]

where the first integral is interpreted with its removable cancellation at
zero.

Using

\[
 \int_0^x\frac{1-\cos u}{u}\,du
 =\gamma+\log x-\operatorname{Ci}(x)
\]

and

\[
 \int_0^{2L}\frac{e^{-t}-1}{t}\,dt
 =-\gamma-\log(2L)-E_1(2L),
\]

one obtains the exact residual identity

\[
 \frac{A(v)}h-\frac{\log(T/(2\pi))}{2\pi}
 =\frac1{2\pi}\left[-\operatorname{Ci}(TL)
 +\operatorname{Re}\int_0^{2L}e^{-i\omega t}F_v(t)\,dt\right],
\]

where

\[
 F_v(t)=\frac{1-r_v(t)}t-b(t)r_v(t)
\]

and the value at `t=0` is understood by continuity.

## Bounds for the smooth multiplier

The function

\[
 f(t)=t a(t)=\frac{t e^{3t/4}}{e^t-1}
\]

has the Bernoulli-polynomial expansion

\[
 f(t)=\sum_{n\ge0}B_n(3/4)\frac{t^n}{n!}
 \qquad (|t|<2\pi).
\]

For `n>=2`, the Fourier series of `B_n` gives

\[
 |B_n(3/4)|\le\frac{2n!\zeta(n)}{(2\pi)^n}.
\]

On `0<=t<=1`, this yields `|b(t)|<1` and `|f''(t)|<1`. Since

\[
 b'(t)=\frac{t f'(t)-(f(t)-1)}{t^2},
\]

the mean-value integral gives `|b'(t)|<1/2` there.

For `t>=1`, `a` is positive and decreasing, `a(1)<2`, and hence

\[
 |b(t)|<3,
 \qquad
 \int_1^{2L}|b'(t)|dt
 \le\int_1^{2L}|a'(t)|dt+\int_1^{2L}\frac{dt}{t^2}<3.
\]

Therefore, over `[0,2L]`, it is sufficient to use

\[
 \|b\|_\infty\le3,
 \qquad
 \int_0^{2L}|b'(t)|dt\le4.
\]

## Variation bound

Put

\[
 d_v(t)=\frac{1-r_v(t)}t.
\]

On the first cell, `d_v` is constant. On `[H,2L]`,

\[
 |d_v'(t)|\le\frac{2}{Ht}+\frac2{t^2}.
\]

Thus

\[
 \operatorname{Var}(d_v)
 \le\frac K L\log K+\frac K L-\frac1L.
\]

Moreover,

\[
 |F_v(0)|\le\frac K L+\frac14,
 \qquad
 |F_v(2L)|=\frac1{2L},
\]

and

\[
 \operatorname{Var}(b r_v)
 \le4+3\operatorname{Var}(r_v)
 \le4+6K.
\]

It follows that

\[
 |F_v(0)|+|F_v(2L)|+\operatorname{Var}(F_v)
 \le \frac K L(\log K+2)+6K+5.
\]

Integration by parts for an absolutely continuous, piecewise-smooth function
then gives

\[
 \left|\int_0^{2L}e^{-i\omega t}F_v(t)dt\right|
 \le\frac2T\left[\frac K L(\log K+2)+6K+5\right].
\]

Finally,

\[
 |\operatorname{Ci}(x)|\le\frac2x\qquad(x>0)
\]

by one integration by parts in its tail integral. Combining the last two
inequalities proves `B_arch`.

## Pole bound

Extend `w_v` by zero outside its support interval. Its total variation satisfies

\[
 \operatorname{Var}(w_v)\le2\sum_j|v_j|\le2\sqrt K.
\]

For every `z` with `|Re z|=T` and `|Im z|=1/2`, integration by parts against the
finite variation measure `dw_v` gives

\[
 |W_v(z)|
 \le\frac{e^{L/4}\sqrt K}{\pi T}.
\]

Each product entering `g_{T,v}(i/2)` is therefore bounded by
`e^(L/2) K/(pi^2 T^2)`. Since `h=L/(2*pi*K)`,

\[
 \frac{|2g_{T,v}(i/2)|}{h}
 \le\frac{4e^{L/2}K^2}{\pi L T^2}
 =\frac{4\sqrt c\,K^2}{\pi L T^2}.
\]

This proves `B_pole`.

## Analytic domain audit

- `T>0`, `c>=2`, and `K>=1`; all logarithms are real.
- The combined compact archimedean integral has a removable endpoint at zero.
- `F_v` is continuous and absolutely continuous on each finite cell; its total
  variation is finite, so the integration-by-parts bound applies.
- The pole estimate uses the zero extension of the piecewise-constant envelope,
  including both boundary jumps.
- No asymptotic equality is used in the bound; only the scalar term being
  compared is the high-carrier leading term.

## Dependency and gap audit

1. The result is conditional on the exact D-0801/L-0702 block normalization and
   signs, which remain `PROPOSED`.
2. The displayed decimal evaluations are ordinary floating arithmetic, not
   outward-rounded proofs.
3. The bound controls only the exact archimedean and pole corrections. It does
   not enclose the complete prime Toeplitz matrix, huge phases, accumulation, or
   eigensolver error.
4. The piecewise family may require mollification under a stricter admissibility
   theorem; survival under mollification is not proved here.
5. A positive finite-family result cannot be extrapolated to RH.

## Adversarial tests

- Check the inverse-`T` and inverse-`T^2` scaling separately.
- Force invalid `c`, `T`, or `K` and require failure.
- Verify the bound uniformly dominates all rows in the X-0901 cutoff ladder.
- Numerically compare the residual identity with the original compact integral
  for small random vectors and moderate carriers.
- Replace `c_K=0` by a cyclic autocorrelation and require the endpoint/pole tests
  to fail.

## Remaining uncertainty

No algebraic sign-reversal mechanism from the exact archimedean or pole blocks
survives this bound at the X-0901 scale. Independent review should reconstruct
the compact archimedean identity and the Bernoulli estimates before promotion.
The unresolved proof bottleneck is now the complete prime matrix with directed
phase and accumulation enclosures, not the omitted high-carrier corrections.

## Suggested next attack

1. Build a fixed-vector directed-ball producer for the complete prime Toeplitz
   Rayleigh value at the lowest-margin carriers.
2. Search joint `(T,c)` basins between decade endpoints, because local `T`
   movement and equal-cell resolution are already nearly saturated.
3. Use the uniform bound as a candidate-survival gate: a leading negative whose
   magnitude exceeds `B_arch+B_pole` can be handed directly to the prime-ball
   checker without assembling full correction matrices.
