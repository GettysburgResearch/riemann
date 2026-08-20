# L-100210 — One extra half-order notch gives a true zero moment and power-decaying Type-I sums

Claim ID: `L-100210`  
Status: **PROVED EXACT ANALYTIC REDUCTION**  
Created: 2026-08-20  
Base: PRs #674--#675  
RH status: **not assumed**

Let \(K_0\) be the minimal ratio-eight ordinary-Möbius wavelet of PR #674.
Its Mellin transform is

\[
\widehat K_0(s)
=
(1-\sqrt2\,2^{-s})(1-2^{-s})^2
\frac{s+\frac32}{s^2(s-\frac12)}.
\tag{L-100210.1}
\]

The zero of the first finite factor cancels the displayed removable
half-order pole. Define one additional notch

\[
\boxed{
K_1=(I-\sqrt2 S_2)K_0.
}
\tag{L-100210.2}
\]

Then

\[
\operatorname{supp}K_1\subset[1,16]
\]

and

\[
\widehat K_1(s)
=
(1-\sqrt2\,2^{-s})\widehat K_0(s).
\tag{L-100210.3}
\]

Thus

\[
\boxed{\widehat K_1(1/2)=0.}
\tag{L-100210.4}
\]

The new zeros lie on \(\Re s=1/2\); no reciprocal-zeta pole
\(s=\rho-\frac12\) with \(1/2<\Re\rho<1\) is cancelled.

Put

\[
k(x)=x^{-1/2}K_1(1/x),
\qquad
\operatorname{supp}k\subset[1/16,1].
\tag{L-100210.5}
\]

Then

\[
\int_{\mathbb R}k(x)\,dx
=
\int_1^{16}K_1(y)y^{-3/2}\,dy
=
\widehat K_1(1/2)
=
0.
\tag{L-100210.6}
\]

The explicit three-band formulas of PR #674 show that \(K_1\) is continuous,
vanishes at both support endpoints, is piecewise smooth, and that the
distributional derivative \(k'\) has finite total variation. Let

\[
V_1=\operatorname{Var}(k')<\infty.
\]

The composite trapezoid formula with the periodic Bernoulli kernel gives, for
every \(Y\ge1\),

\[
\left|
\frac1Y\sum_{m\in\mathbb Z}k(m/Y)-\int k
\right|
\le
\frac{V_1}{12Y^2}.
\tag{L-100210.7}
\]

Consequently

\[
\boxed{
\left|
\sum_{m\ge1}\frac1{\sqrt m}K_1(Y/m)
\right|
\le
\frac{V_1}{12}\,Y^{-3/2}.
}
\tag{L-100210.8}
\]

This is a genuine power-decaying Type-I estimate. It is unavailable for
\(K_0\), whose half-order zero is spent only removing the original carrier
pole rather than creating a zero moment.

Finally define

\[
\mathcal W_1(X)
=
\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}K_1(X/n).
\tag{L-100210.9}
\]

Its Mellin transform is \(\widehat K_1(s)/\zeta(s+1/2)\). Therefore subpower
logarithmic negative mass of \(\mathcal W_1\) implies RH by the same
Mellin--Landau argument as PR #674.
