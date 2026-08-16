# L-93300 — A zero-safe endpoint-order family with arbitrarily deep hyperbola localization

Claim ID: `L-93300`  
Status: **PROVED EXACT FINITE / MELLIN THEOREM**  
Created: 2026-08-16  
Depends on: the endpoint-field summation used in frozen `L-93250`  
RH status: **unproved**

## 1. The kernel family

For an integer \(r\ge1\), define

\[
G_r(x)
=
x^r(1-x)^r(2x-1)\mathbf 1_{0\le x\le1}
\]

and

\[
w_r(x)=\frac12G_r'(x).
\]

Then

\[
G_r(1-x)=-G_r(x),
\qquad
w_r(1-x)=w_r(x),
\qquad
\int_0^1w_r(x)\,dx=0.
\]

The finite positive number

\[
C_r=\int_0^1w_r(x)^2\,dx
\]

is completely explicit.  In the first two cases,

\[
C_1=\frac1{20},
\qquad
C_2=\frac1{630}.
\]

The frozen cubic kernel is \(K=G_1/3\), so its norm \(1/180\) is recovered.

## 2. Exact endpoint projection

For the complete centered Q4 field, put

\[
\mathcal A_r(N)
=
\int_0^1w_r(\theta)Q_{\circ,N}(\theta)\,d\theta.
\]

The same finite-prefix reversal as in `L-93250` gives

\[
\boxed{
\mathcal A_r(N)
=
\sum_{m\le N}c_\circ(m)G_r(m/N).
}
\tag{L-93300.1}
\]

Because \(w_r\) has mean zero,

\[
\boxed{
|\mathcal A_r(N)|^2
\le
NC_r\,\mathscr V_\circ(N).
}
\tag{L-93300.2}
\]

Thus every member of the family is controlled by the same centered endpoint
energy.

## 3. Mellin multiplier

A beta-integral gives, for \(\Re s>-r\),

\[
\boxed{
\widehat G_r(s)
=
\int_0^1G_r(x)x^{s-1}\,dx
=
\frac{r!(s-1)}
{\displaystyle\prod_{j=r}^{2r+1}(s+j)}.
}
\tag{L-93300.3}
\]

The only numerator zero is \(s=1\).  Hence \(\widehat G_r\) is nonzero at every
point in the open critical strip.

The factor-four transfer kernel is

\[
\Phi_r(x)=G_r(x)-4G_r(4x),
\]

with \(G_r(4x)=0\) for \(x>1/4\).  Its Mellin transform is

\[
\boxed{
\widehat\Phi_r(s)
=
(1-4^{1-s})\widehat G_r(s).
}
\tag{L-93300.4}
\]

Both factors vanish at \(s=1\), so the principal pole is killed to second
order.  Neither factor vanishes at a nontrivial zero in the open strip.

## 4. Complete Q4 transform

For real \(X\ge1\),

\[
\int_1^\infty
\mathcal A_r(X)X^{-s-1}\,dX
=
\widehat G_r(s)
\left[
(1-4^{1-s})
\left(-\frac{\zeta'}{\zeta}(s)\right)
+
3(\log4)\frac{4^{-s}}{1-4^{-s}}
\right]
\]

initially in \(\Re s>1\), with meromorphic continuation supplied by the
displayed right side.

Every open-strip zero survives.  Consequently, for any fixed \(r\),

\[
\mathcal A_r(N)\ll \sqrt N\,\log^B(2N)
\quad(N\ge2)
\]

for some fixed \(B\) is an RH-sufficient estimate.  Under RH, summation by
parts and von Koch give such an estimate.  No member of the family makes the
arithmetic estimate automatic.

## 5. The quintic companion

For \(r=2\),

\[
G_2(x)=2x^5-5x^4+4x^3-x^2,
\]

\[
w_2(x)=5x^4-10x^3+6x^2-x,
\qquad
\int_0^1w_2^2=\frac1{630},
\]

and

\[
\boxed{
\widehat G_2(s)
=
\frac{2(s-1)}
{(s+2)(s+3)(s+4)(s+5)}.
}
\tag{L-93300.5}
\]

Moreover,

\[
\max_{0\le x\le1}|G_2(x)|
=
\frac{\sqrt5}{125},
\qquad
\max G_2(x)^2=\frac1{3125}.
\]

Unlike the cubic transfer, \(\Phi_2\) is continuously differentiable at
\(x=1/4\).  This removes one full order of quadrature boundary loss and is the
first concrete redesigned observable used below.

## 6. Exact boundary

```text
finite endpoint identity for every r             exact
centered-energy Cauchy bridge                    exact
zero-safe Mellin multiplier                      exact
factor-four double cancellation at s=1           exact
quintic companion                                exact
square-root arithmetic estimate                  not assumed
Riemann Hypothesis                               unproved
```
