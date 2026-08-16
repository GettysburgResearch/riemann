# L-96400 — The conclusion-producing rows have exact finite Riesz states and an integer-knot reduction

Claim ID: `L-96400`  
Status: **UNCONDITIONAL EXACT FINITE / MELLIN-ALGEBRA LEMMA**  
Created: 2026-08-17  
Depends on: the canonical component-spline formula; elementary Dirichlet convolution  
RH status: **not assumed**

## 1. The two full rows

For \(j\ge2\), let
\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]
Only rows \(j=2,3\) are needed by the direct Mellin--Landau consumer.

Put
\[
 F(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n}\log\frac xn,
 \qquad F(x)=0\quad(0<x<1).
\tag{L-96400.1}
\]
The constant-tail decomposition of the canonical row gives exactly
\[
 \boxed{
 c_X(2)
 =\log X-F(X)+\sqrt2\,F(X/2)-\frac1{\sqrt3}F(X/3)
 }
\tag{L-96400.2}
\]
and
\[
 \boxed{
 \begin{aligned}
 c_X(3)
 ={}&\frac13\log X-\frac13F(X)
 -\frac1{3\sqrt2}F(X/2)\\
 &+\frac5{3\sqrt3}F(X/3)-\frac12F(X/4).
 \end{aligned}
 }
\tag{L-96400.3}
\]
These are finite identities at every real \(X\); no Euler-product limit is
being taken.

## 2. Exact coefficient dictionaries

Write
\[
 c_X(j)=\sum_{n\le X}\frac{a_j(n)}{\sqrt n}\log\frac Xn.
\tag{L-96400.4}
\]
Then
\[
 \boxed{
 a_2(n)
 ={\bf1}_{n=1}-\mu(n)
 +2{\bf1}_{2\mid n}\mu(n/2)
 -{\bf1}_{3\mid n}\mu(n/3)
 }
\tag{L-96400.5}
\]
and
\[
 \boxed{
 \begin{aligned}
 3a_3(n)
 ={}&{\bf1}_{n=1}-\mu(n)
 -{\bf1}_{2\mid n}\mu(n/2)\\
 &+5{\bf1}_{3\mid n}\mu(n/3)
 -3{\bf1}_{4\mid n}\mu(n/4).
 \end{aligned}
 }
\tag{L-96400.6}
\]
As usual, a Möbius term with a noninteger argument is absent.

For a squarefree \(d>1\) with \((d,6)=1\), write
\(n=2^\alpha3^\beta d\).  Then
\[
 a_2(n)=\mu(d)r_2(\alpha,\beta),
 \qquad
 3a_3(n)=\mu(d)r_3(\alpha,\beta),
\tag{L-96400.7}
\]
where the nonzero entries are
\[
\begin{array}{c|r|r}
(\alpha,\beta)&r_2&r_3\\ \hline
(0,0)&-1&-1\\
(0,1)&0&6\\
(0,2)&1&-5\\
(1,0)&3&0\\
(1,1)&-2&-5\\
(1,2)&-1&5\\
(2,0)&-2&-2\\
(2,1)&2&2\\
(3,0)&0&3\\
(3,1)&0&-3.
\end{array}
\tag{L-96400.8}
\]
All other entries vanish.  The unit core \(d=1\) has the additional
\({\bf1}_{n=1}\) correction in (L-96400.5)--(L-96400.6).

Thus the complete problem is a large-prime squarefree Möbius sum against two
fixed finite \(2,3\)-scale kernels.  No vague rough reservoir is needed to
state the arithmetic object.

## 3. Integer-knot reduction

Define the two prefix states
\[
 M_j(N)=\sum_{n\le N}\frac{a_j(n)}{\sqrt n},
 \qquad
 L_j(N)=\sum_{n\le N}\frac{a_j(n)\log n}{\sqrt n}.
\tag{L-96400.9}
\]
For \(N\le X<N+1\),
\[
 \boxed{c_X(j)=M_j(N)\log X-L_j(N).}
\tag{L-96400.10}
\]
The newly entering term at an integer endpoint has logarithm zero, so
\(c_X(j)\) is continuous.  It is affine in \(\log X\) on every unit cell.
Consequently
\[
 \boxed{
 c_X(j)\ge0\ \text{for every real }X\ge X_0
 \iff
 c_N(j)\ge0\ \text{for every integer }N\ge\lceil X_0\rceil.
 }
\tag{L-96400.11}
\]

The exact state update is
\[
 M_j(N)=M_j(N-1)+\frac{a_j(N)}{\sqrt N},
\tag{L-96400.12}
\]
\[
 \boxed{
 c_{N+1}(j)
 =
 c_N(j)+M_j(N)\log\left(1+\frac1N\right).
 }
\tag{L-96400.13}
\]
This is the correct globally owned one-dimensional state.  A negative
\(M_j(N)\) is allowed; it consumes previously accumulated reserve through
(L-96400.13).  Treating every negative occurrence independently is stronger
than the actual theorem and leads to the reservoir overcounts isolated in
`R-96400`.

## 4. Exact renewal identity

The universal Riesz state satisfies
\[
 \boxed{
 F(x)+\sum_{m=2}^{\lfloor x\rfloor}\frac1{\sqrt m}F(x/m)=\log x.
 }
\tag{L-96400.14}
\]
Indeed, the coefficient of
\(n^{-1/2}\log(x/n)\) on the left is
\(\sum_{d\mid n}\mu(d)\), so only \(n=1\) remains.

Equations (L-96400.2)--(L-96400.14) replace the invalid local transport by an
exact finite state and expose the genuine remaining arithmetic sign problem.
