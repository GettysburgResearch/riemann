# L-21704 — Exact line-zero convex-order budget and martingale completion target

Claim ID: `L-21704`  
Title: Every cosine-bell line-zero factor is convex-order dominated by its uniform annihilator factor, with exact variance budget `2/gamma^2`  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — finite and infinite convex-order theorem proved; Brownian completion coupling open**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Dependencies: `T-21702`, `T-21703`; elementary one-dimensional convex order  
Scope: the sharp probability coupling interface for the final saturation

## 1. One line-zero factor

Fix `gamma>0` and put

\[
a=\frac\pi\gamma.
\tag{L-21704.1}
\]

Let `U_gamma` be uniform on `[-a,a]`, and let `C_gamma` have density

\[
f_C(x)=\frac1{2a}
\left(1+\cos\frac{\pi x}{a}\right)
\mathbf1_{|x|\le a}.
\tag{L-21704.2}
\]

Both variables are symmetric and centered. Their characteristic functions are

\[
\varphi_U(t)=\frac{\sin(at)}{at},
\tag{L-21704.3}
\]

\[
\varphi_C(t)=
\frac{\sin(at)}{at(1-a^2t^2/\pi^2)},
\tag{L-21704.4}
\]

with removable values at the apparent poles. Therefore

\[
\varphi_U(t)=
\left(1-\frac{t^2}{\gamma^2}\right)
\varphi_C(t).
\tag{L-21704.5}
\]

## 2. Exact peakedness order

For `0<=r<=a`,

\[
\mathbb P(|U_\gamma|>r)=1-\frac ra,
\tag{L-21704.6}
\]

whereas

\[
\begin{aligned}
\mathbb P(|C_\gamma|>r)
&=1-\frac1a\int_0^r
 \left(1+\cos\frac{\pi x}{a}\right)dx\\
&=1-\frac ra-
 \frac1\pi\sin\frac{\pi r}{a}.
\end{aligned}
\tag{L-21704.7}
\]

Hence

\[
\boxed{|C_\gamma|\preceq_{\rm st}|U_\gamma|.}
\tag{L-21704.8}
\]

For any convex function `Phi`, symmetrize it by

\[
\overline\Phi(x)=\frac12(\Phi(x)+\Phi(-x)).
\]

The function `overline Phi` is even, convex, and nondecreasing on `[0,infinity)`.
Using symmetry and (L-21704.8),

\[
\mathbb E\Phi(C_\gamma)
=\mathbb E\overline\Phi(C_\gamma)
\le
\mathbb E\overline\Phi(U_\gamma)
=\mathbb E\Phi(U_\gamma).
\]

Therefore

\[
\boxed{C_\gamma\preceq_{\rm cx}U_\gamma.}
\tag{L-21704.9}
\]

This is stronger than a variance comparison.

## 3. Exact variance budget

Direct integration gives

\[
\operatorname{Var}(U_\gamma)=\frac{a^2}{3}
 =\frac{\pi^2}{3\gamma^2},
\tag{L-21704.10}
\]

\[
\operatorname{Var}(C_\gamma)
 =\frac{a^2}{3}-\frac{2a^2}{\pi^2}
 =\frac{\pi^2/3-2}{\gamma^2}.
\tag{L-21704.11}
\]

Thus

\[
\boxed{
\operatorname{Var}(U_\gamma)
-
\operatorname{Var}(C_\gamma)
=\frac2{\gamma^2}.}
\tag{L-21704.12}
\]

By Strassen's theorem, (L-21704.9) admits a martingale coupling. For any such
coupling,

\[
\mathbb E[U_\gamma\mid C_\gamma]=C_\gamma
\tag{L-21704.13}
\]

and

\[
\mathbb E[(U_\gamma-C_\gamma)^2]=\frac2{\gamma^2}.
\tag{L-21704.14}
\]

Each line zero therefore supplies an exact martingale-variance budget.

## 4. Infinite line-zero sum

Take `m_gamma` independent copies for each actual critical-line ordinate. Since

\[
\sum_\gamma\frac{m_\gamma}{\gamma^2}<\infty,
\tag{L-21704.15}
\]

the partial sums converge in `L2`. Let

\[
C=\sum_{\gamma,j}C_{\gamma,j},
\qquad
U=\sum_{\gamma,j}U_{\gamma,j}.
\tag{L-21704.16}
\]

Convex order is preserved under independent convolution and under these
uniformly square-integrable weak limits. Hence

\[
\boxed{C\preceq_{\rm cx}U.}
\tag{L-21704.17}
\]

Moreover

\[
\boxed{
\operatorname{Var}(U)-\operatorname{Var}(C)
=2\sum_\gamma\frac{m_\gamma}{\gamma^2}.}
\tag{L-21704.18}
\]

Taking independent factorwise martingale couplings produces a global coupling
with

\[
\boxed{\mathbb E[U\mid C]=C}
\tag{L-21704.19}
\]

and total martingale increment variance equal to the right side of
(L-21704.18).

## 5. Brownian completion target

Let `Z` be the half-size-biased Brownian log-range variable of `L-21703`,
independent of `C`. The saturation inequality is exactly

\[
\operatorname{Var}(Z)
\le
\operatorname{Var}(U)-\operatorname{Var}(C).
\tag{L-21704.20}
\]

A stronger sufficient theorem is

\[
\boxed{Z+C\preceq_{\rm cx}U.}
\tag{L-21704.21}
\]

By `T-21703`, (L-21704.21) is actually equivalent to RH: it gives the reverse
variance inequality, while the positive quartet defect gives the opposite
variance inequality, so equality and RH follow. Under RH the two laws are equal.

Equivalently, the final proof may construct a coupling satisfying

\[
\boxed{
\mathbb E[U\mid Z+C]=Z+C.}
\tag{L-21704.22}
\]

The line-zero factors already provide a canonical martingale reservoir through
(L-21704.13)--(L-21704.19). The only missing probability theorem is to embed the
specific Brownian log-range displacement `Z` into this reservoir without
exceeding its exact variance budget.

## 6. Stop-loss formulation

For centered square-integrable real variables, (L-21704.21) is equivalent to

\[
\boxed{
\mathbb E[(Z+C-r)_+]
\le
\mathbb E[(U-r)_+]
\quad\text{for every real }r.}
\tag{L-21704.23}
\]

This gives a one-parameter verification target. A Brownian-path proof may seek a
direct stopping-time or martingale transport whose terminal stop-loss transform
is bounded by the explicit infinite uniform sum.

## 7. Proof boundary

The factorwise peakedness, convex order, infinite convolution, and exact variance
budget are proved above. They do not imply the Brownian completion
(L-21704.21). Adding an independent nondegenerate `Z` makes a law less, not more,
concentrated in convex order.

Therefore the existence of the line-zero martingale reservoir is genuine new
structure but is not itself a proof of saturation. The load-bearing theorem is
the specific coupling (L-21704.22), or any weaker independent argument proving
only (L-21704.20).