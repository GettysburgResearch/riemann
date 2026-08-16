# L-93301 — The complete cubic Q4 scalar is one large-prime scale-four shell plus a square-root-safe tower term

Claim ID: `L-93301`  
Status: **UNCONDITIONAL EXACT REDUCTION**  
Created: 2026-08-16  
Depends on: `L-93300`; elementary prime-power bookkeeping  
RH status: **unproved**

## 1. Scale-four cubic wavelet

Let

\[
 K(x)=\frac{x(1-x)(2x-1)}3
\]

for \(0\le x\le1\), and extend it by zero outside that interval.  Define

\[
 \boxed{
 F(x)=K(x)-4K(4x)\mathbf1_{0\le x\le1/4}.
 }
\]

Then explicitly

\[
 \boxed{
 F(x)=
 \begin{cases}
 170x^3-63x^2+5x,&0\le x\le1/4,\\[1mm]
 \dfrac{-2x^3+3x^2-x}{3},&1/4<x\le1,\\[1mm]
 0,&\text{otherwise}.
 \end{cases}
 }
\]

The two formulas agree at \(x=1/4\), where \(F(1/4)=-1/32\).
A safe pointwise bound is

\[
 |F(x)|\le1,
 \qquad
 |F(x)|\le5x
 \quad(0\le x\le1).
\]

## 2. Exact source reorganization

The cubic scalar of PR #498 satisfies

\[
 \begin{aligned}
 \mathcal A_\circ(N)
 ={}&
 \sum_{n\le N}\Lambda(n)F(n/N)
 \\
 &+
 3(\log4)\sum_{4^r\le N}K(4^r/N).
 \end{aligned}
 \tag{L-93301.1}
\]

This is obtained by substituting \(m=4n\) in the contracted source term.
No approximation is used.

Equivalently, for every odd prime \(p\),

\[
 Z_{p,N}
 =(\log p)\sum_{k:p^k\le N}F(p^k/N),
 \tag{L-93301.2}
\]

while the \(p=2\) block has the same scale-four sum plus the displayed
four-adic gauge.

## 3. Complete same-prime geometric formula

Let

\[
 K_p=\max\{k:p^k\le N\},
 \qquad
 H_p=\max\{k:4p^k\le N\},
\]

with an empty sum interpreted as zero.  If

\[
 G_r(p,M)=\sum_{k=1}^{M}p^{rk}
 =\frac{p^r(p^{rM}-1)}{p^r-1},
\]

and

\[
 a_1=-\frac13,\qquad a_2=1,\qquad a_3=-\frac23,
\]

then for every odd prime

\[
 \boxed{
 \frac{Z_{p,N}}{\log p}
 =
 \sum_{r=1}^3
 a_rN^{-r}
 \left[
 G_r(p,K_p)-4^{r+1}G_r(p,H_p)
 \right].
 }
 \tag{L-93301.3}
\]

Thus every power and every contracted appearance of one Euler factor is already
summed in a closed finite geometric expression.

## 4. Small prime bases are square-root safe

If \(p\le\sqrt N\), then

\[
 (\log p)\#\{k:p^k\le N\}\le\log N.
\]

Using \(|F|\le1\),

\[
 \sum_{p\le\sqrt N}
 (\log p)\left|
 \sum_{k:p^k\le N}F(p^k/N)
 \right|
 \le\sqrt N\log N.
 \tag{L-93301.4}
\]

The four-adic gauge contains \(O(\log N)\) terms, each bounded by
\(3(\log4)\|K\|_\infty\).  It is therefore \(O(\log N)\).

## 5. The exact large-prime shell

For \(p>\sqrt N\), only \(p^1\le N\) occurs.  Hence

\[
 \boxed{
 \mathcal A_\circ(N)
 =
 \sum_{\sqrt N<p\le N}
 (\log p)F(p/N)
 +O(\sqrt N\log N).
 }
 \tag{L-93301.5}
\]

The implied constant is absolute and can be replaced by the explicit
small-base sum in (L-93301.4) plus the finite four-adic gauge.

This eliminates:

```text
all higher prime powers;
all same-prime tower interference;
the four-adic gauge;
and every prime base at most sqrt(N)
```

from the RH-bearing arithmetic producer.

## 6. Prime-discrepancy form

Let

\[
 \vartheta(x)=\sum_{p\le x}\log p.
\]

Because `L-93302` proves \(\int_0^1F=0\), and because \(F(x)=O(x)\) at
the origin,

\[
 N\int_{1/\sqrt N}^{1}F(x)\,dx=O(1).
\]

Therefore the hard shell is exactly a scale-wavelet of the prime discrepancy:

\[
 \boxed{
 \sum_{\sqrt N<p\le N}(\log p)F(p/N)
 =
 \int_{\sqrt N}^{N}F(t/N)\,d[\vartheta(t)-t]
 +O(1).
 }
 \tag{L-93301.6}
\]

No prime number theorem estimate is used in this identity.

## 7. Consequence

A bound

\[
 \left|
 \sum_{\sqrt N<p\le N}(\log p)F(p/N)
 \right|
 \ll\sqrt N(\log N)^B
\]

would close the centered cubic criterion.  The reduction itself is
unconditional; the displayed shell estimate remains RH-bearing.

## 8. Boundary

```text
complete prime-tower formula                    exact
small prime bases                               O(sqrt(N) log N)
four-adic gauge                                 O(log N)
large-prime shell                               exact remaining object
prime discrepancy form                         exact
large-prime shell square-root bound             open / RH-bearing
Riemann Hypothesis                              unproved
```
