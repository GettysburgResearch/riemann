# L-21502 — Finite prime-pair Gram energy

Claim ID: `L-21502`  
Title: Every terminal-prime Hardy energy is one explicit finite positive-semidefinite multiplicative prime-pair form, with a polynomial diagonal and all RH obstruction off diagonal  
Status: `PROPOSED — COMPLETE FINITE IDENTITY AND GLOBAL EXPONENT SPLIT`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: `L-21501`; `T-21501` for the rightmost-zero interpretation

## 1. Truncated energy

Let `G` be the explicit window of `L-21501`, supported in

\[
 [a,b]=[1,3+\log4],
\]

and put

\[
 q(x)=Q_G(x)
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}G(x-\log n).
\]

For real `X`, define

\[
 \mathcal E_G(X)=\int_{-\infty}^{X}|q(x)|^2\,dx.
 \tag{L-21502.1}
\]

Only prime powers satisfying

\[
 \log n\le X-a
\]

can occur. Hence every sum below is finite.

## 2. Exact Gram expansion

For real `u,v`, define

\[
 \boxed{
 K_X(u,v)
 =\int_{-\infty}^{X}G(x-u)G(x-v)\,dx.}
 \tag{L-21502.2}
\]

Expanding the finite sum and interchanging it with the integral gives

\[
 \boxed{
 \mathcal E_G(X)
 =\sum_{m,n\le e^{X-a}}
   \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
   K_X(\log m,\log n).}
 \tag{L-21502.3}
\]

The kernel is positive semidefinite. Indeed, for arbitrary complex numbers
`c_1,...,c_r` and real locations `u_1,...,u_r`,

\[
 \sum_{i,j}\overline{c_i}c_jK_X(u_i,u_j)
 =\int_{-\infty}^{X}
  \left|\sum_ic_iG(x-u_i)\right|^2dx
 \ge0.
 \tag{L-21502.4}
\]

Thus every finite level is one exact Gram form. There is no spectral ansatz,
zero truncation, or omitted prime tail.

## 3. Interior autocorrelation

If

\[
 X\ge\max(u,v)+b,
\]

then both translated windows are completely included and

\[
 K_X(u,v)=C_G(u-v),
 \tag{L-21502.5}
\]

where

\[
 C_G(t)=5C_\phi(t)-2C_\phi(t-\log4)-2C_\phi(t+\log4)
\]

and `C_phi` is the explicit cubic spline of `L-21501`.

Since `C_phi` is supported on `[-2,2]`,

\[
 C_G(t)=0
 \qquad\text{when}\qquad
 |t|>2+\log4.
 \tag{L-21502.6}
\]

Therefore the interior prime-pair form couples only bounded multiplicative
ratios:

\[
 e^{-(2+\log4)}
 \le\frac mn\le
 e^{2+\log4}.
 \tag{L-21502.7}
\]

The global RH obstruction is a coherent local-ratio prime correlation, not an
interaction between arbitrarily separated scales.

## 4. Diagonal is automatically subexponential

Split

\[
 \mathcal E_G(X)=\mathcal D_G(X)+\mathcal O_G(X),
 \tag{L-21502.8}
\]

where

\[
 \mathcal D_G(X)
 =\sum_{n\le e^{X-a}}
   \frac{\Lambda(n)^2}{n}K_X(\log n,\log n)
 \tag{L-21502.9}
\]

is the diagonal and `O_G` contains all `m!=n` terms.

Because

\[
 0\le K_X(u,u)\le\|G\|_2^2
\]

and

\[
 \|G\|_2\le3\|\phi\|_2,
 \qquad
 \|\phi\|_2^2=\frac23,
\]

one has

\[
 K_X(u,u)\le6.
\]

Using `Lambda(n)<=log n`, the elementary integral comparison gives

\[
\begin{aligned}
 \mathcal D_G(X)
 &\le6\sum_{n\le e^{X-a}}\frac{(\log n)^2}{n}\\
 &\le C(1+X)^3.
\end{aligned}
\tag{L-21502.10}
\]

Consequently

\[
 \limsup_{X\to\infty}
 \frac{\log(1+\mathcal D_G(X))}{2X}=0.
 \tag{L-21502.11}
\]

No prime number theorem is needed.

## 5. The entire rightmost-zero exponent is off diagonal

Let

\[
 \mathcal O_G^+(X)=\max\{\mathcal O_G(X),0\}.
\]

Then

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
  \frac{\log(1+\mathcal O_G^+(X))}{2X}.}
 \tag{L-21502.12}
\]

### Proof

Since `E_G>=0` and `D_G>=0`,

\[
 \mathcal O_G^+(X)\le\mathcal E_G(X),
\]

so the exponent on the right is at most `Theta_zeta` by `T-21501`.

Conversely,

\[
 \mathcal E_G(X)
 =\mathcal D_G(X)+\mathcal O_G(X)
 \le\mathcal D_G(X)+\mathcal O_G^+(X).
\]

The diagonal has exponent zero. Therefore any positive exponential exponent of
`E_G` must be carried by `O_G^+`; if the common exponent is zero the equality is
automatic. This proves (L-21502.12).

Thus

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal O_G^+(X)=\exp(o(X)).}
 \tag{L-21502.13}
\]

This is the exact arithmetic target of the global attack.

## 6. Unit-block version

Define

\[
 \mathcal B_G(j)
 =\int_j^{j+1}|Q_G(x)|^2dx.
 \tag{L-21502.14}
\]

Each block again has an exact finite Gram representation, now with kernel

\[
 K_j^{\rm block}(u,v)
 =\int_j^{j+1}G(x-u)G(x-v)dx.
\]

Since

\[
 \mathcal E_G(J)=\sum_{j<J}\mathcal B_G(j)+O(1),
\]

RH is equivalently

\[
 \boxed{
 \mathcal B_G(j)=\exp(o(j)).}
 \tag{L-21502.15}
\]

in the upper-envelope sense

\[
 \limsup_{j\to\infty}\frac{\log(1+\mathcal B_G(j))}{2j}=0.
\]

This block form is the natural interface for dyadic decomposition, bilinear
forms, and multiplicative dispersion estimates.

## 7. Proof-production interface

A finite exact certificate at `X` contains:

1. the complete duplicate-free prime-power manifest through `e^(X-a)`;
2. exact or outward-enclosed logarithmic locations;
3. the finite piecewise-polynomial kernel `K_X`;
4. the exact positive-semidefinite Gram contraction;
5. separate diagonal and off-diagonal ledgers;
6. a source digest for `G` and the prime manifest.

Unlike a sign certificate for one scalar level, the global programme must prove
a uniform subexponential upper envelope for this sequence of finite energies.

## 8. Proof boundary

Closed here:

- exact finite prime-pair expansion;
- positive-semidefinite Gram structure;
- bounded-ratio localization;
- polynomial diagonal bound;
- equality of the off-diagonal positive exponent with `Theta_zeta`.

Open:

\[
 \boxed{
 \mathcal O_G^+(X)=\exp(o(X)).}
\]

The open statement is no smaller than RH, but it is now a direct multiplicative
prime-pair coherence estimate with no hidden spectral or limiting object.
