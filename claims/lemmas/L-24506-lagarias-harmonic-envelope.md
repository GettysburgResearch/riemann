# L-24506 — Lagarias harmonic envelope around the Robin scale

Claim ID: `L-24506`  
Status: `IMPORTED AND REPROVED — elementary`  
Scope: harmonic-number estimates used by `T-24502`  
Issue: #245  
Source: Lagarias, arXiv:math/0008177v2, Lemmas 3.1 and 3.2.

Let

\[
H_n=\sum_{j=1}^n\frac1j.
\]

## 1. Exact fractional-part representation

For every integer `n>=1`,

\[
\boxed{
H_n=\log n+\gamma+\int_n^\infty\frac{\{t\}}{t^2}\,dt.
}
\tag{L-24506.1}
\]

Indeed,

\[
\int_1^n\frac{\lfloor t\rfloor}{t^2}\,dt=H_n-1
\]

after splitting at the integer intervals through `n`, and rearrangement yields

\[
H_n=\log n+1-\int_1^n\frac{\{t\}}{t^2}\,dt.
\]

Letting `n` tend to infinity identifies

\[
\gamma=1-\int_1^\infty\frac{\{t\}}{t^2}\,dt
\]

and gives (L-24506.1).

Consequently

\[
\log n+\gamma<H_n\le\log n+\gamma+\frac1n.
\tag{L-24506.2}
\]

## 2. Lower harmonic envelope

For `n>=3`, (L-24506.2) gives

\[
e^{H_n}\ge e^\gamma n.
\]

Also `H_n>=log n`, hence `log H_n>=log log n>0`. Therefore

\[
\boxed{
e^{H_n}\log H_n\ge e^\gamma n\log\log n
\qquad(n\ge3).}
\tag{L-24506.3}
\]

## 3. Upper harmonic envelope

For `n>=3`, the elementary bound `H_n<=log n+1` implies

\[
\log H_n
\le
\log(\log n+1)
\le
\log\log n+\frac1{\log n}.
\tag{L-24506.4}
\]

The upper side of (L-24506.2) gives

\[
e^{H_n}\le e^\gamma n e^{1/n}.
\]

Since `e^x<=1+2x` on `0<=x<=1`,

\[
\boxed{
e^{H_n}\le e^\gamma n\left(1+\frac2n\right).}
\tag{L-24506.5}
\]

Combining (L-24506.4) and (L-24506.5), and using the elementary numerical inequalities recorded by Lagarias, yields for `n>=10`

\[
e^{H_n}\log H_n
\le
 e^\gamma n\log\log n+\frac{6n}{\log n}.
\tag{L-24506.6}
\]

Finally `H_n<=log n+1<=n/log n` for `n>=20`, so

\[
\boxed{
H_n+e^{H_n}\log H_n
\le
 e^\gamma n\log\log n+\frac{7n}{\log n}
\qquad(n\ge20).}
\tag{L-24506.7}
\]

## 4. Quantitative significance

The Lagarias threshold differs from the Robin main term by at most `O(n/log n)`. Under false RH, Robin supplies infinitely many excesses of size

\[
\frac{n\log\log n}{(\log n)^\beta},
\qquad 0<\beta<\frac12,
\]

which dominate `n/log n`. This scale separation is the entire converse mechanism.

## Review boundary

All statements in this file are elementary. The only finite numerical checks needed are the displayed inequalities at the declared thresholds. The RH content enters only through the imported Robin theorems in `T-24502`.
