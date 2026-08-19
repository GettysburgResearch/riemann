# R-99000 — The fractional Julia heat bound is false at the real carrier

Claim ID: `R-99000`  
Status: **COMPLETE ANALYTIC REFUTATION**  
Created: 2026-08-18  
Frozen input: PR #613 at `6809d8509f031f7f783ef20e2250ff2735e32924`  
RH status: **not assumed**

Let

\[
 B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\]

and, for fixed non-integral `0<theta<1`, let `B_theta=B_diamond^theta` be the
branch positive on the real line `s>1`.  Write

\[
 B_\theta(s)=\sum_{n\ge1}b_\theta(n)n^{-s}
\qquad(\Re s>1)
\]

and

\[
 \mathscr B_{\theta,T}(\tau)
 =\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
  e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\]

PR #613 asserted the uniform energy estimate

\[
 \int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \sqrt{T/\pi}e^{-T(\tau-\tau_0)^2}\,d\tau
 \le (1+T)^{O(1)}e^{96\theta T+O(T^{3/4}\log^2T)}.
\tag{R-99000.1}
\]

We prove that (R-99000.1) is false for every `theta<1/192`, already at
`tau_0=0`.

## 1. Local branch at one

The Laurent expansion

\[
 \zeta(s)=\frac1{s-1}+\gamma+O(s-1)
\]

gives

\[
 \boxed{
 B_\diamond(s)=\frac38(s-1)(1+O(s-1)).
 }
\tag{R-99000.2}
\]

Hence

\[
 B_\theta(s)=(3/8)^\theta(s-1)^\theta(1+O_\theta(s-1)).
\tag{R-99000.3}
\]

## 2. Gaussian Mellin representation and a purely local contour shift

For every `c>1`, Gaussian Mellin inversion and absolute convergence of the
Dirichlet series give

\[
 \boxed{
 \mathscr B_{\theta,T}(\tau)
 =2\sqrt{\pi T}\,\frac1{2\pi i}
 \int_{c-i\infty}^{c+i\infty}
 B_\theta(s)e^{T(s-1/2-i\tau)^2}\,ds.
 }
\tag{R-99000.4}
\]

No global zero-free region is needed.  Meromorphic continuation at one gives a
radius `r_0>0` on which

\[
 B_\theta(s)=(3/8)^\theta(s-1)^\theta H_\theta(s),
 \qquad H_\theta(1)=1,
\]

with `H_theta` holomorphic and nonzero.  Choose `c=1+eta`, where
`eta>0` is so small that

\[
 (1/2+\eta)^2-r_0^2<1/4-\eta.
\]

On the portions of the original contour with `|Im s|>=r_0`, the Gaussian is
`O(exp((1/4-eta)T))`; absolute convergence bounds `B_theta` there.  On the
central finite segment, deform inside the zero-free local disk to a vertical
line left of one, with a Hankel loop around the cut `s=1-r`, `0<r<r_0`.
Every new segment away from the cut also has exponential rate strictly below
`1/4`.

The two banks of the cut differ by

\[
 (s-1)^\theta\big|_+-(s-1)^\theta\big|_-
 =2i\sin(\pi\theta)r^\theta.
\]

For `|tau|<=T^{-1/2}`, the Hankel contribution is therefore

\[
 2\sqrt{\pi T}\,\frac{(3/8)^\theta\sin(\pi\theta)}\pi
 e^{T(1/2-i\tau)^2}
 \int_0^{r_0}r^\theta H_\theta(1-r)
 e^{-T(1-2i\tau)r+Tr^2}\,dr.
\tag{R-99000.5}
\]

Set `r=u/T`.  Dominated convergence on `u<=T r_0/2`, followed by the
exponentially small tail, gives

\[
 \int_0^{r_0}\cdots dr
 =T^{-\theta-1}\Gamma(\theta+1)
 (1-2i\tau)^{-\theta-1}
 (1+O_\theta(T^{-1/2})).
\]

Using

\[
 \Gamma(-\theta)\Gamma(\theta+1)
 =-\frac\pi{\sin(\pi\theta)},
\]

we obtain, up to the orientation sign of the Hankel loop,

\[
 \boxed{
 \mathscr B_{\theta,T}(\tau)
 =\frac{2\sqrt\pi(3/8)^\theta}{\Gamma(-\theta)}
  T^{-\theta-1/2}(1-2i\tau)^{-\theta-1}
  e^{T(1/2-i\tau)^2}
  (1+O_\theta(T^{-1/2})).
 }
\tag{R-99000.6}
\]

The sign is irrelevant below; the coefficient is nonzero.  This derivation is
local at `s=1` and uses neither RH nor any asymptotic theorem for the
coefficients.

## 4. Energy asymptotic and contradiction

Since

\[
 |e^{T(1/2-i\tau)^2}|^2=e^{T/2-2T\tau^2},
\]

multiplying by the averaging Gaussian contributes `e^{-T tau^2}`.  Therefore

\[
 \boxed{
 \int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \sqrt{T/\pi}e^{-T\tau^2}\,d\tau
 \sim
 \frac{4\pi(3/8)^{2\theta}}
 {\sqrt3\,|\Gamma(-\theta)|^2}
 T^{-2\theta-1}e^{T/2}.
 }
\tag{R-99000.7}
\]

The exponential rate is `1/2`, independent of `theta`.  If `theta<1/192`, then
`96 theta<1/2`; the right side of (R-99000.1) has strictly smaller exponential
rate.  This proves the refutation.

The obstruction is the deterministic real carrier at `s=1`; it exists whether
or not RH is true.
