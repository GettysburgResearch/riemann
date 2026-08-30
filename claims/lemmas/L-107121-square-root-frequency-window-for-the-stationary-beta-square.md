# L-107121 — The stationary beta square has an unconditional square-root frequency frontier

**Claim ID:** `L-107121`  
**Status:** proved from the classical Dirichlet-polynomial mean-value theorem  
**Date:** 2026-08-31  
**RH:** not assumed

Retain `q=67`, `L=log q`, and put

\[
D_Y(t)=\sum_{\substack{n\le Y\\q\nmid n}}
\frac{\mu(n)}{n^{1/2+it}}.
\tag{1}
\]

The Fourier transform of

\[
\Lambda_q(v)=\left(1-\frac{|v|}{L}\right)_+
\]

is

\[
\widehat\Lambda_q(t)
=L\left(\frac{\sin(tL/2)}{tL/2}\right)^2.
\tag{2}
\]

Consequently Fourier inversion and finite summation give the exact positive
spectral identity

\[
\boxed{
\mathcal Q_q(Y)
=\frac{L}{2\pi}\int_{\mathbb R}
\left(\frac{\sin(tL/2)}{tL/2}\right)^2
|D_Y(t)|^2\,dt.
}
\tag{3}
\]

## 1. Classical mean-value input

For `U>=1`, the standard Hilbert-inequality proof of the mean-value theorem
for Dirichlet polynomials gives

\[
\int_U^{2U}|D_Y(t)|^2dt
\ll (U+Y)\sum_{n\le Y}\frac{\mu_q(n)^2}{n}
\ll (U+Y)\log(2Y).
\tag{4}
\]

No zero-free region is used in (4).

## 2. High-frequency tail

For `|t|>=1`, the multiplier in (3) is `O_L(t^{-2})`. Dyadically applying
(4) therefore yields, uniformly for `T>=1`,

\[
\boxed{
\int_{|t|>T}
\widehat\Lambda_q(t)|D_Y(t)|^2dt
\ll_L
\log(2Y)\left(\frac1T+\frac{Y}{T^2}\right).
}
\tag{5}
\]

Fix `B>1/2` and define

\[
T_B(Y)=Y^{1/2}(\log(2Y))^B.
\tag{6}
\]

Then (5) is polylogarithmic, indeed

\[
\ll_L
Y^{-1/2}(\log(2Y))^{1-B}
+(\log(2Y))^{1-2B}.
\tag{7}
\]

Thus frequencies beyond the square-root threshold contribute only a
subpower error.

## 3. Truncated quantitative detector

Define

\[
\mathcal Q_q^{(B)}(Y)
=\frac{L}{2\pi}
\int_{|t|\le T_B(Y)}
\left(\frac{\sin(tL/2)}{tL/2}\right)^2
|D_Y(t)|^2dt,
\]

and

\[
\mathfrak Q_q^{(B)}(X)=\max_{2\le Y\le X}\mathcal Q_q^{(B)}(Y).
\tag{8}
\]

Equations (5)--(7) and `T-107110` imply

\[
\boxed{
\limsup_{X\to\infty}
\frac{\log(1+\mathfrak Q_q^{(B)}(X))}{\log X}
=2\Theta-1.
}
\tag{9}
\]

Hence

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathfrak Q_q^{(B)}(X)=X^{o(1)}.
}
\tag{10}
\]

This is a fixed compact causal detector with a source-blind spectral window of
size `Y^(1/2+o(1))`. The much smaller hyperbolic window on PR #779 is obtained
only after paying noncompact physical tails; the two theorems therefore meet
at the repository's causal localization barrier.

## 4. Firewall

The same mean-value theorem applied to the retained low-frequency window gives
only `O(Y log Y)` at source-blind strength. Paying the tail is not an estimate
of the surviving window. Any fixed power saving there would, by (9), prove a
new zero-free half-plane.
