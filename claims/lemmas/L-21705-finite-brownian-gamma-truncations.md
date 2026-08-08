# L-21705 — Finite Brownian–gamma truncations and exact Mellin formula

Claim ID: `L-21705`  
Title: The Brownian-bridge range law has explicit finite gamma truncations whose Mellin transforms are finite Hermite divided differences  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: Biane–Pitman–Yor's Brownian-range/gamma-sum identity; finite partial fractions  
Scope: finite probability and complex analysis; no real-zero or RH conclusion

## 1. The finite variables

Let `Gamma_(2,n)` be independent gamma variables of shape two and unit rate, and put

\[
 S_N=\sum_{n=1}^N\frac{\Gamma_{2,n}}{n^2},
 \qquad
 Y_N=\sqrt{\frac{S_N}{\pi}}.
\tag{L-21705.1}
\]

The limiting variable satisfies

\[
Y_\infty
\overset d=
\sqrt{\frac2\pi}
\left(\max b-\min b\right)
\]

for a standard Brownian bridge `b`, and Biane–Pitman–Yor give

\[
\mathbb E[Y_\infty^s]=2\xi(s).
\tag{L-21705.2}
\]

For finite `N`, write

\[
m_N(s)=\mathbb E[Y_N^s].
\tag{L-21705.3}
\]

It is holomorphic for `Re(s)>-4N`, which contains the complete critical strip.

## 2. Laplace transform and partial fractions

The Laplace transform of `S_N` is

\[
\boxed{
 L_N(q)=\mathbb E[e^{-qS_N}]
 =\prod_{n=1}^N\left(\frac{n^2}{n^2+q}\right)^2.}
\tag{L-21705.4}
\]

It has the exact decomposition

\[
L_N(q)=\sum_{n=1}^N
\left(
 \frac{A_{N,n}}{q+n^2}
 +\frac{B_{N,n}}{(q+n^2)^2}
\right),
\tag{L-21705.5}
\]

where

\[
\boxed{
B_{N,n}
=4n^4\frac{(N!)^4}{(N-n)!^2(N+n)!^2}}
\tag{L-21705.6}
\]

and

\[
\boxed{
A_{N,n}
=-2B_{N,n}
 \sum_{\substack{1\le k\le N\\k\ne n}}
 \frac1{k^2-n^2}.}
\tag{L-21705.7}
\]

The finite harmonic collapse is

\[
\boxed{
\sum_{k\ne n}\frac1{k^2-n^2}
=\frac1{2n}
\left(
 H_{N-n}-H_{N+n}+\frac3{2n}
\right).}
\tag{L-21705.8}
\]

Consequently the density is the explicit phase-type spline

\[
\boxed{
f_N(x)=\sum_{n=1}^N(A_{N,n}+B_{N,n}x)e^{-n^2x}.}
\tag{L-21705.9}
\]

Although some displayed partial-fraction coefficients are signed, the complete density is nonnegative because it is the convolution density in (L-21705.1).

## 3. Exact Mellin transform

Set

\[
 C_{N,n}=4\frac{(N!)^4}{(N-n)!^2(N+n)!^2}.
\tag{L-21705.10}
\]

Integrating (L-21705.9) gives

\[
\boxed{
\begin{aligned}
m_N(s)
={}&\pi^{-s/2}\Gamma\left(1+\frac s2\right)D_N(s),\\
D_N(s)
={}&\sum_{n=1}^NC_{N,n}
\left[
 n(H_{N+n}-H_{N-n})+\frac{s-1}{2}
\right]n^{-s}.
\end{aligned}}
\tag{L-21705.11}
\]

For `N=1`, this reduces to

\[
m_1(s)=\pi^{-s/2}\Gamma\left(2+\frac s2\right),
\]

as required for one `Gamma(2,1)` variable.

## 4. Dirichlet-spline form

Let the knot list contain each number `n^(-2)` twice:

\[
\mathcal A_N=(1,1,2^{-2},2^{-2},\ldots,N^{-2},N^{-2}).
\]

Then the Hermite divided difference gives the compact formula

\[
\boxed{
 m_N(s)=
 \pi^{-s/2}\Gamma\left(1+\frac s2\right)
 [\mathcal A_N]\,x^{2N-1+s/2}.}
\tag{L-21705.12}
\]

One proof writes `S_N=G_(2N) Q_N`, where `G_(2N)` is gamma of shape `2N`, independent of the Dirichlet average

\[
Q_N=\sum_{n=1}^N\frac{W_n}{n^2},
\qquad
(W_1,\ldots,W_N)\sim\operatorname{Dirichlet}(2,\ldots,2),
\]

and applies the standard Dirichlet-average/divided-difference identity.

This representation nominates nonuniform B-splines and total positivity as possible finite real-zero mechanisms. It does not assert such a theorem.

## 5. Uniform truncation error in the critical strip

Write

\[
S_\infty=S_N+R_N,
\qquad
\mathbb E R_N=2\sum_{n>N}n^{-2}\le\frac2N.
\]

For `u=s/2`, `0<=Re(u)<=1/2`, and positive `a,r`,

\[
(a+r)^u-a^u
=u r\int_0^1(a+\theta r)^{u-1}d\theta.
\]

Since `S_N>=Gamma_(2,1)` and

\[
\mathbb E[\Gamma_{2,1}^{\operatorname{Re}u-1}]
=\Gamma(1+\operatorname{Re}u)\le1,
\]

independence gives

\[
\boxed{
|m_N(s)-2\xi(s)|\le\frac{|s|}{N}
\qquad(0\le\operatorname{Re}s\le1).}
\tag{L-21705.13}
\]

The bound is uniform on the closed strip and immediately implies local uniform convergence there.

## 6. Raw symmetrization and its danger

The finite functional-equation symmetrization

\[
X_N^{\rm raw}(s)=m_N(s)+m_N(1-s)
\tag{L-21705.14}
\]

satisfies

\[
X_N^{\rm raw}(s)=X_N^{\rm raw}(1-s)
\]

and converges locally uniformly to `4 xi(s)`. Functional equation and convergence do **not** imply that its finite zeros lie on the critical line. `O-21705` records high-precision off-line mutations for this raw producer.

## 7. Proof boundary

Closed here, subject to review:

- finite Brownian/gamma construction;
- rational partial fractions and density;
- exact Mellin/Dirichlet-polynomial formula;
- Dirichlet-spline representation;
- quantitative local uniform convergence.

Open:

- any finite real-zero theorem;
- RH.
