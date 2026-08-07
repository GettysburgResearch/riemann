# L-22302 — One-dimensional semiprime Sobolev sufficient condition

Claim ID: `L-22302`  
Title: Two weighted L2 estimates for explicit one-dimensional semiprime signals imply the critical H1 condition and RH  
Status: `PROPOSED — COMPLETE FOURIER-SOBOLEV TRANSFER; SEMIPRIME ESTIMATES OPEN`  
Authoring agent: `gpt56-pro-19`  
Created: 2026-08-07  
Issue: #223  
Dependencies: `T-22301`; `L-22301`; elementary Fourier Sobolev inequality

## 1. Critical convolution signal

Let

\[
 C=Q*Q
\]

be the one-dimensional product-scale signal of `L-22301`, and for `sigma>0`
put

\[
 c_\sigma(x)=e^{-\sigma x}C(x).
 \tag{L-22302.1}
\]

Then

\[
 \widehat{c_\sigma}(t)
 =\widehat H(\sigma+it)^2
  P_1(1/2+\sigma+it)^2.
 \tag{L-22302.2}
\]

## 2. Fourier L1 from one derivative

Use the Fourier convention

\[
 \widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}dx.
\]

For every `f in W^(1,2)(R)`, Cauchy--Schwarz and Plancherel give

\[
\begin{aligned}
 \|\widehat f\|_1
 &\le
 \left(\int\frac{dt}{1+t^2}\right)^{1/2}
 \left(\int(1+t^2)|\widehat f(t)|^2dt\right)^{1/2}\\
 &\le
 \boxed{
 \pi\sqrt2\,
 \bigl(\|f\|_2^2+\|f'\|_2^2\bigr)^{1/2}.}
\end{aligned}
\tag{L-22302.3}
\]

Therefore

\[
 c_\sigma\in W^{1,2}(\mathbb R)
 \quad\Longrightarrow\quad
 \widehat{c_\sigma}\in L^1(\mathbb R).
 \tag{L-22302.4}
\]

By `T-22301`, proving (L-22302.4) for every `sigma>0` proves RH, subject to the
parent prime-only transfer.

## 3. Explicit arithmetic form

Let

\[
 W=H*H.
\]

Then

\[
 C(x)=\sum_n\frac{b_{\mathbb P,2}(n)}{\sqrt n}
 W(x-\log n),
 \tag{L-22302.5}
\]

and

\[
 C'(x)=\sum_n\frac{b_{\mathbb P,2}(n)}{\sqrt n}
 W'(x-\log n).
 \tag{L-22302.6}
\]

Thus

\[
 c_\sigma'(x)
 =e^{-\sigma x}
 \sum_n\frac{b_{\mathbb P,2}(n)}{\sqrt n}
 \bigl[W'-\sigma W\bigr](x-\log n).
 \tag{L-22302.7}
\]

The complete sufficient arithmetic theorem is the pair

\[
\boxed{
\begin{aligned}
&\int e^{-2\sigma x}
 \left|
  \sum_n\frac{b_{\mathbb P,2}(n)}{\sqrt n}
  W(x-\log n)
 \right|^2dx<\infty,\\
&\int e^{-2\sigma x}
 \left|
  \sum_n\frac{b_{\mathbb P,2}(n)}{\sqrt n}
  [W'-\sigma W](x-\log n)
 \right|^2dx<\infty,
\end{aligned}}
\tag{L-22302.8}
\]

for every `sigma>0`.

Both are one-dimensional squarefree-semiprime/prime-square mean-square
estimates with fixed compact piecewise-polynomial windows. The factor-ratio
cells of PR #222 are absent.

## 4. Why this may be more attackable

The target is stronger than the exact `H^1` condition, but it has three useful
features:

1. it is a standard weighted `L2` mean square rather than an `L1` Fourier norm;
2. the second signal differs only by the explicit window
   `W'-sigma W`;
3. direct pair enumeration and grouped product enumeration give independent
   arithmetic producers.

A Selberg/Heath--Brown decomposition can therefore be applied to one product
variable and retained through the final quadratic contraction.

## 5. Proof boundary

The Fourier-Sobolev transfer is exact. No estimate in (L-22302.8) is proved.
Those estimates remain strong enough to imply RH and cannot follow from an
entrywise absolute semiprime bound.
