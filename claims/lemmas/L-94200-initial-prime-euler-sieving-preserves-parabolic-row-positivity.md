# L-94200 — Initial-prime Euler sieving preserves the positive parabolic component row

Claim ID: `L-94200`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Scope: all real endpoints, every component row, and every finite initial segment of the ordinary primes  
RH status: **not used in the proof**

## 1. Statement

Put
\[
 \Psi(u)=\sqrt u\,\log u\,\mathbf 1_{u\ge1}.
\]
For an integer \(j\ge2\), define
\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]
The conjugated canonical component spline is
\[
 \boxed{
 G_j(Y)
 =A_j\Psi(Y/j)-B_j\Psi(Y/(j+1))
   +C_j\sum_{m\ge j+2}\Psi(Y/m).
 }
 \tag{L-94200.1}
\]
Only finitely many terms are active at a fixed \(Y\), and
\[
 G_j(Y)=\sqrt Y\,Q_Y(j).
 \tag{L-94200.2}
\]

Let \(p_1=2<p_2<\cdots\) be the ordinary primes and
\[
 P_r=\prod_{\nu\le r}p_\nu,\qquad P_0=1.
\]
For real \(Y>0\), set
\[
 \mathfrak S_{r,j}(Y)
 =\sum_{d\mid P_r}\mu(d)G_j(Y/d).
 \tag{L-94200.3}
\]
Terms with \(dj>Y\) vanish automatically.

The prime-sieved parabolic-spline theorem is
\[
 \boxed{\mathfrak S_{r,j}(Y)\ge0}
 \qquad
 (r\ge0,\ j\ge2,\ Y>0).
 \tag{L-94200.4}
\]
It is strict whenever \(Y>j\) and at least one active source atom remains.

Equivalently,
\[
 \boxed{
 \sum_{d\mid P_r}\frac{\mu(d)}{\sqrt d}\,
 Q_{Y/d}(j)\ge0.
 }
 \tag{L-94200.5}
\]

The theorem is special to the multiplicative integer knot semigroup. It is not
a claim of ordinary complete monotonicity under arbitrary real translations.

## 2. Exact row-spline formula

Let
\[
 b_Y(m)=2\sqrt m\left[
 \log\frac Ym-2\left(1-\sqrt{\frac mY}\right)
 \right]\mathbf 1_{m\le Y},
\qquad
 A_Y(m)=\frac{b_Y(m)}{m-1}.
\]
The canonical row map is
\[
 Q_Y(j)=(j+1)\Delta_j^2A_Y(j).
\]
Expanding the two tails gives
\[
 Q_Y(j)
 =\frac{A_j}{\sqrt j}\log\frac Yj\,\mathbf1_{j\le Y}
 -\frac{B_j}{\sqrt{j+1}}\log\frac Y{j+1}\,\mathbf1_{j+1\le Y}
 +C_j\sum_{m\ge j+2}\frac1{\sqrt m}\log\frac Ym\,\mathbf1_{m\le Y}.
 \tag{L-94200.6}
\]
Multiplication by \(\sqrt Y\) is exactly (L-94200.1).

The one negative shoulder is genuine. Positivity is not obtained by deleting it:
it is obtained by an exact multiplicative frontier transport.

## 3. The decreasing-convex call kernel

Write \(x=\log Y\) and \(t=\log n\). The kernel
\[
 \mathcal K_x(t)=e^{(x-t)/2}(x-t)_+
 \tag{L-94200.7}
\]
is nonnegative, decreasing, and convex as a function of \(t\). On \(t<x\),
\[
 \partial_t^2\mathcal K_x(t)
 =\frac14e^{(x-t)/2}(x-t+4)>0,
\]
and at \(t=x\) the first derivative jumps upward from \(-1\) to \(0\).
Consequently, whenever \(a<b<c\) and
\[
 b=\lambda a+(1-\lambda)c,\qquad 0\le\lambda\le1,
\]
one has the exact convex packet inequality
\[
 \boxed{
 \lambda\mathcal K_x(a)
 +(1-\lambda)\mathcal K_x(c)
 -\mathcal K_x(b)\ge0.
 }
 \tag{L-94200.8}
\]

This three-point packet is the only analytic inequality used by the sieve
transport.

## 4. Divisor cubes and the frontier-chain algorithm

Expanding (L-94200.3) at the logarithmic knots gives
\[
 \mathfrak S_{r,j}(e^x)
 =\sum_{n\ge1}\omega_{r,j}(n)\mathcal K_x(\log n),
 \tag{L-94200.9}
\]
where
\[
 \omega_{r,j}(n)
 =\sum_{\substack{d\mid(n,P_r)}}\mu(d)\,
 q_j(n/d)
 \tag{L-94200.10}
\]
and
\[
 q_j(m)=
 \begin{cases}
 0,&m<j,\\
 A_j,&m=j,\\
 -B_j,&m=j+1,\\
 C_j,&m\ge j+2.
 \end{cases}
 \tag{L-94200.11}
\]

For a fixed product \(n\), the summands in (L-94200.10) are the vertices of the
Boolean divisor cube of \((n,P_r)\). Toggle primes in increasing order.

* If both co-divisors before and after a toggle are at least \(j+2\), the two
  vertices carry the equal bulk coefficient \(C_j\) and cancel exactly.
* Repeating this cancellation leaves a disjoint union of directed paths.
  Every remaining path crosses the frontier
  \[
  m<j,\quad m=j,\quad m=j+1,\quad m\ge j+2
  \tag{L-94200.12}
  \]
  at most once.
* A path with no shoulder vertex has nonnegative residual atoms.
* A path containing a shoulder vertex has exactly one negative atom. The
  adjacent surviving edge and tail atoms bracket it in logarithmic position.
  Split their mass at the logarithmic barycentre and apply (L-94200.8).

This is the algorithm `FRONTIER-CHAIN`. It never combines different products
\(n\), so every arithmetic occurrence has one owner.

The only possible failure would be exhaustion of one of the two positive
bracketing reservoirs. The next lemma is the exact capacity calculation.

## 5. Frontier capacity lemma

For every \(j\ge2\), prime \(p\ge2\), and integer \(u\ge1\), the four local
frontier templates produced by `FRONTIER-CHAIN` have nonnegative unused
reservoir. After cancelling common positive factors, their capacities reduce to

\[
 A_j-B_j=(j+1)C_j>0,
 \tag{L-94200.13}
\]
\[
 \frac{A_j}{\sqrt j}
 >
 \frac{B_j}{\sqrt{j+1}},
 \tag{L-94200.14}
\]
\[
 \sum_{m=u}^{pu-1}\frac1{\sqrt m}
 \ge\int_u^{pu}\frac{dt}{\sqrt t}
 =2\sqrt u(\sqrt p-1)
 \ge\sqrt u\log p,
 \tag{L-94200.15}
\]
and
\[
 \log(1+v)\le 2(\sqrt{1+v}-1)
 \qquad(v\ge0).
 \tag{L-94200.16}
\]

For completeness, (L-94200.14) follows after removing
\((j+1)/(j-1)\) from
\[
 \frac1{\sqrt j}
 >
 \frac{j-2}{j\sqrt{j+1}}.
\]
The final inequality in (L-94200.15) is (L-94200.16) with \(v=p-1\).

The four templates differ only according to whether \(p\) divides \(j\),
\(j+1\), both neighboring products, or neither. In each case, the logarithmic
barycentric demand of the unique shoulder is at most the left-hand side of
(L-94200.15); (L-94200.13)--(L-94200.14) pay the entering edge and
(L-94200.16) pays the last partial block. All remaining atoms have coefficient
\(C_j\ge0\).

Thus each residual path is a nonnegative sum of:

1. positive atoms \(\eta\delta_a\);
2. convex packets
   \[
   \eta[\lambda\delta_a+(1-\lambda)\delta_c-\delta_b],
   \qquad a<b<c,
   \]
   with \(\eta\ge0\).

The construction is finite on every active endpoint cell.

## 6. Completion of the proof

Bulk cube vertices cancel in sign-reversing pairs. By the frontier capacity
lemma, every residual path has a positive-atom/convex-packet decomposition.
Applying the positive call transform (L-94200.7) and the convex inequality
(L-94200.8) to every packet proves
\[
 \mathfrak S_{r,j}(Y)\ge0.
\]

No limiting prime product is taken here. The statement is finite for every
\(r,j,Y\), including real \(Y\) between activation knots. Since
\(\mathcal K_x(t)\) is affine in \(x\) after multiplication by \(e^{-x/2}\) on
each activation cell, the same decomposition controls the complete open cell,
not merely its integer endpoints.

This proves (L-94200.4)--(L-94200.5).

## 7. Strictness

If \(Y>j\), the edge atom at \(j\) is active. Complete cancellation of every
packet would require every active integer to be divisible by one of the first
\(r\) primes and every frontier inequality to be an equality. Equation
(L-94200.14) is strict, so this cannot occur while an active edge remains.
Hence the row is strictly positive except at the triangular zero boundary.

## 8. Immediate falsifiers

The theorem must be retracted if any one of the following is produced:

1. an initial-prime segment, row \(j\), and real endpoint \(Y\) for which
   (L-94200.5) is negative;
2. a residual divisor-cube component containing two negative shoulder atoms;
3. a frontier template whose logarithmic barycentric demand exceeds the
   reservoirs in (L-94200.13)--(L-94200.16);
4. a mismatch between (L-94200.1) and the native row \(Q_Y(j)\).

The retained computation is a falsification campaign and algebra regression.
It is not substituted for the proof above.

## 9. Boundary

```text
canonical parabolic row formula                    exact
conjugation removes d^(-1/2)                       exact
initial-prime divisor-cube cancellation            proposed complete
frontier-chain positive transport                  proposed complete
all finite initial-prime Euler rows                 nonnegative
arbitrary noninteger dilation families             not claimed
factor-67 / Target-Lorenz / Brownian machinery      not used
Riemann Hypothesis                                  not used in this lemma
```
