# L-21902 — Uniform Gaussian tails for the differential-Hermite completion

Claim ID: `L-21902`  
Title: Polynomially many dilation derivatives of the exact Xi source retain a super-Gaussian multiplicative support tail  
Status: **PROPOSED — COMPLETE ELEMENTARY TAIL ESTIMATE; INTERPOLATION-PROJECTION TAIL SEPARATE**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-15101`; `L-21901`  
Scope: physical exterior/fold part of the exact source-frame tail

## 1. Polynomial form of the source ladder

Put

\[
 y=\pi x^2,
 \qquad
 h(x)=p_0(y)e^{-y},
 \qquad
 p_0(y)=y^2-\frac32y.
 \tag{L-21902.1}
\]

For

\[
 \mathcal D=x\partial_x+\frac12
 =2y\partial_y+\frac12,
 \tag{L-21902.2}
\]

one has

\[
 \mathcal D[p(y)e^{-y}]
 =(Tp)(y)e^{-y},
 \tag{L-21902.3}
\]

where

\[
 \boxed{
 Tp=2yp'(y)+\left(\frac12-2y\right)p(y).
 }
 \tag{L-21902.4}
\]

If `deg p<=d` and `||p||_1` denotes the sum of the absolute values of its
coefficients, then

\[
 \boxed{
 \|Tp\|_1
 \le\left(2d+\frac52\right)\|p\|_1.
 }
 \tag{L-21902.5}
\]

Indeed the three terms in (L-21902.4) cost at most `2d`, `1/2`, and `2`
times the coefficient norm.

After `r` applications, the degree is at most `r+2`, so

\[
 \boxed{
 \|T^rp_0\|_1
 \le\frac52\,7^r r!.
 }
 \tag{L-21902.6}
\]

The constant `7` is deliberately nonoptimal; it follows from
`2(r+2)+5/2<=7(r+1)`.

## 2. A polynomial source bound

Let

\[
 P(X)=\sum_{m=0}^Mp_mX^m
 \tag{L-21902.7}
\]

and define

\[
 f_P=P(-\mathcal D^2)h.
 \tag{L-21902.8}
\]

Then

\[
 f_P(x)=q_P(\pi x^2)e^{-\pi x^2},
 \qquad
 \deg q_P\le2M+2,
 \tag{L-21902.9}
\]

and

\[
 \boxed{
 \|q_P\|_1
 \le C_M\|P\|_1,
 \qquad
 C_M={5\over2}7^{2M}(2M)!.
 }
 \tag{L-21902.10}
\]

Consequently, for `x>=1`,

\[
 \boxed{
 |f_P(x)|
 \le C_M\|P\|_1
 (\pi x^2)^{2M+2}e^{-\pi x^2}.
 }
 \tag{L-21902.11}
\]

## 3. Arithmetic image on the upper multiplicative ray

Let

\[
 K_P(u)=E(f_P)(u)
 =u^{1/2}\sum_{n\ge1}f_P(nu).
 \tag{L-21902.12}
\]

For `u>=1`, put `q=e^{-pi u^2}`.  Since `n^2>=n`,

\[
 e^{-\pi n^2u^2}\le q^n.
 \tag{L-21902.13}
\]

For every integer `r>=0`,

\[
 n^r\le r!{n+r-1\choose r},
 \tag{L-21902.14}
\]

and hence

\[
 \sum_{n\ge1}n^rq^n
 \le {r!q\over(1-q)^{r+1}}.
 \tag{L-21902.15}
\]

Applying this with `r=4M+4` to (L-21902.11) gives

\[
 \boxed{
 |K_P(u)|
 \le \mathcal C_M\|P\|_1
 u^{4M+9/2}e^{-\pi u^2},
 \qquad u\ge1,
 }
 \tag{L-21902.16}
\]

where the completely explicit constant

\[
 \boxed{
 \mathcal C_M
 ={5\over2}7^{2M}(2M)!\pi^{2M+2}
 {(4M+4)!\over(1-e^{-\pi})^{4M+5}}
 }
 \tag{L-21902.17}
\]

may be replaced by any directed rational upper enclosure.

## 4. The lower ray is identical

Equation `L-21901.16` gives

\[
 \mathcal F\mathcal D=-\mathcal D\mathcal F.
 \]

Therefore `-mathcal D^2` commutes with Fourier transform. Since `h` is
self-Fourier, every `f_P` is self-Fourier.  The two source cancellations permit
Poisson summation exactly as in `L-15101`, giving

\[
 \boxed{K_P(u)=K_P(1/u).}
 \tag{L-21902.18}
\]

Thus the upper and lower multiplicative support tails have the same weighted
norm.

## 5. Explicit weighted support-tail bound

For `0<=tau<1/2`, use

\[
 \|g\|_{\tau,\mathrm{glob}}^2
 =\int_0^\infty|g(u)|^2
 (u^{2\tau}+u^{-2\tau}){du\over u}.
 \tag{L-21902.19}
\]

Let `P_lambda` restrict to `[lambda^-1,lambda]`. For `lambda>=1`, equations
(L-21902.16)--(L-21902.18) give

\[
 \|(I-P_\lambda)K_P\|_{\tau,\mathrm{glob}}^2
 \le4\mathcal C_M^2\|P\|_1^2
 \int_\lambda^\infty
 u^{8M+8+2\tau}e^{-2\pi u^2}\,du.
 \tag{L-21902.20}
\]

For

\[
 b=8M+8+2\tau,
 \tag{L-21902.21}
\]

integration by parts and

\[
 \int_\lambda^\infty u^{b-2}e^{-2\pi u^2}du
 \le\lambda^{-2}
 \int_\lambda^\infty u^be^{-2\pi u^2}du
 \tag{L-21902.22}
\]

yield, whenever the denominator is positive,

\[
 \boxed{
 \|(I-P_\lambda)K_P\|_{\tau,\mathrm{glob}}^2
 \le
 {4\mathcal C_M^2\|P\|_1^2
  \lambda^{8M+7+2\tau}e^{-2\pi\lambda^2}
  \over
  4\pi-(8M+7+2\tau)/\lambda^2}.
 }
 \tag{L-21902.23}
\]

This is a direct growing-degree extension of the fixed-source estimate in
`L-15101`.

## 6. Quadratic-log source frames remain super-Gaussian

Put

\[
 \ell=\log\lambda.
 \tag{L-21902.24}
\]

Suppose

\[
 M\le C\ell^2
 \tag{L-21902.25}
\]

and

\[
 \log(2+\|P\|_1)
 =O(\ell^2\log(2+\ell)).
 \tag{L-21902.26}
\]

Then the logarithm of every factor in the numerator of (L-21902.23), except
the Gaussian, is

\[
 O(\ell^3+\ell^2\log\ell),
 \tag{L-21902.27}
\]

whereas

\[
 2\pi\lambda^2=2\pi e^{2\ell}.
 \tag{L-21902.28}
\]

Therefore, uniformly on such a packet,

\[
 \boxed{
 \|(I-P_\lambda)K_P\|_{\tau,\mathrm{glob}}
 =\exp[-\pi\lambda^2+O(\ell^3)]
 \longrightarrow0
 }
 \tag{L-21902.29}
\]

faster than every exponential in `ell`.

The explicit Lagrange inverse of `L-21901` satisfies (L-21902.26) whenever the
finite zeta diagonal has subexponential inverse.  Indeed

\[
 \|L_k\|_1
 \le{\prod_{j\ne k}(1+x_j)
       \over\prod_{j\ne k}|x_k-x_j|}
 \tag{L-21902.30}
\]

and the denominator is given exactly by `L-21901.32`--`L-21901.33`; the crude
bound already gives `log ||L_k||_1=O(N log(N+ell))`.

## 7. Consequence for the source bridge

For the exact differential-Hermite inverse:

```text
ordinary physical exterior tail
+ every literal periodization fold
```

is super-Gaussian on the quadratic-log packet.  Thus these terms cannot be the
load-bearing obstruction in the complete corrected tail.

The only potentially non-super-Gaussian component is the discarded high
Fourier part of the smooth periodization.  That component is isolated exactly
in `L-21903`.

## 8. Proof boundary

- The polynomial recurrence, coefficient estimate, Gaussian power-sum bound,
  self-Fourier identity, and weighted tail integration are elementary.
- Constants are intentionally conservative and should be independently
  replayed before production use.
- The theorem controls physical exterior and fold tails.  It does not prove
  that the high Fourier projection residual has the prolate `d_4/d_8`
  hierarchy, nor does it prove local-Weyl scalarization or RH.
