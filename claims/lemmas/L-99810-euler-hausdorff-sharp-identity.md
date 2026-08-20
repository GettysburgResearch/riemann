# L-99810 — The scalar SHARP defect is exactly a duplicate-67 Euler–Hausdorff exceedance

Claim ID: `L-99810`  
Status: **PROVED EXACT IDENTITY**  
Created: 2026-08-20  
Depends on: the scalar of PR #653; the Euler–Hurwitz identities of PR #615  
RH status: **not assumed**

Fix `p=67` and put

\[
 \beta(n)=\mu(n)-\mathbf1_{p\mid n}\mu(n/p).
\tag{L-99810.1}
\]

Let

\[
 S(y)=\sum_{m\le y}m^{-1/2},
 \qquad
 T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

and define the positive Euler discrepancy

\[
 \boxed{E(y)=2S(y)-T(y).}
\tag{L-99810.2}
\]

The scalar SHARP Harnack defect is

\[
 h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\tag{L-99810.3}
\]

## 1. Exact convolution

The Dirichlet series of `beta` is

\[
 \sum_{n\ge1}\frac{\beta(n)}{n^z}
 =\frac{1-p^{-z}}{\zeta(z)}.
\]

Consequently

\[
 \boxed{\beta*\mathbf1=\delta_1-\delta_p.}
\tag{L-99810.4}
\]

Using `T=2S-E` and finite divisor switching,

\[
\begin{aligned}
 \sum_{n\le x}\frac{\beta(n)}{\sqrt n}
  2S(x/n)
 &=2\sum_{nm\le x}\frac{\beta(n)}{\sqrt{nm}}\\
 &=2\sum_{k\le x}\frac{(\beta*\mathbf1)(k)}{\sqrt k}\\
 &=2\left(1-p^{-1/2}\mathbf1_{x\ge p}\right).
\end{aligned}
\]

Therefore

\[
 \boxed{
 h(x)=2\left(1-p^{-1/2}\mathbf1_{x\ge p}\right)
 -\sum_{n\le x}\frac{\beta(n)}{\sqrt n}E(x/n).
 }
\tag{L-99810.5}
\]

For `x>=67`, define

\[
 \mathcal Q_E(x)=
 \sum_{n\le x}\frac{\beta(n)}{\sqrt n}E(x/n).
\]

Then

\[
 \boxed{
 h(x)<0
 \iff
 \mathcal Q_E(x)>2(1-67^{-1/2}).
 }
\tag{L-99810.6}
\]

Thus the negative-mass condition of PRs #653/#656 is exactly

\[
 \boxed{
 \int_{67}^{X}
 \left[\mathcal Q_E(t)-2(1-67^{-1/2})\right]_+
 \frac{dt}{t}=X^{o(1)}.
 }
\tag{L-99810.7}
\]

By PR #656, (L-99810.7) is equivalent to RH.

## 2. Hausdorff and Hurwitz structure

At integer `N`, PR #615 proves that

\[
 E(N)=e_\infty+\int_0^1u^N\,d\nu(u),
 \qquad
 e_\infty=3+2\zeta(1/2)>0,
 \qquad d\nu\ge0.
\tag{L-99810.8}
\]

Hence the integer Euler discrepancy is a strict Hausdorff moment sequence.
For real `y`, write `N=floor(y)` and

\[
 \mathscr E(y)=3+2\zeta(1/2)-2\zeta(1/2,y+1)-4\sqrt y.
\]

The exact fractional-cell reset is

\[
 \boxed{
 E(y)=\mathscr E(y)-D(y),
 \qquad
 D(y)=\int_N^y\zeta(3/2,u+1)\,du,
 }
\tag{L-99810.9}
\]

with

\[
 D(N)=0,
 \qquad
 0<D(y)<\frac2{\sqrt{N+1}}
 \quad(N<y<N+1).
\tag{L-99810.10}
\]

Equations (L-99810.5)–(L-99810.10) separate the last scalar obstruction into a
positive completely monotone storage term and one explicit positive activation
reset.  They do not sign the Möbius projection; that projection is the
remaining RH-equivalent correlation.
