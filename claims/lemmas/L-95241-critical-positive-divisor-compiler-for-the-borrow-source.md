# L-95241 — The dyadic-borrow source has a positive inverse and nonnegative generalized primes

Claim ID: `L-95241`  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-95240`; elementary Euler products  
Scope: critical-normalized arithmetic source and divisor compiler; no physical-row positivity theorem

## 1. Critical source

Write \(s=z+1/2\) and

\[
y=2^{1/2-s}.
\]

The zero-safe source attached to `L-95240` is

\[
\boxed{
\Omega_\rho(s)
=
\frac{(1-y)(1+\rho y)}{\zeta(s)}.
}
\tag{L-95241.1}
\]

Its inverse is

\[
\boxed{
A_\rho(s)
=
\frac{\zeta(s)}{(1-y)(1+\rho y)}.
}
\tag{L-95241.2}
\]

The finite numerator cannot cancel a nontrivial zeta zero in \(\Re s>1/2\).

## 2. Positive inverse coefficients

At an odd prime, \(A_\rho\) has the ordinary zeta Euler factor. At \(2\), put \(x=2^{-s}=y/\sqrt2\). The local series is

\[
\frac1{(1-x)(1-y)(1+\rho y)}
=
\frac1{(1-y/\sqrt2)(1-y)(1+\rho y)}.
\tag{L-95241.3}
\]

Let

\[
b_e=\sum_{k=0}^{e}2^{-k/2},
\]

the coefficients of \([(1-y/\sqrt2)(1-y)]^{-1}\). If \(a_e\) denotes the full local coefficient, then

\[
a_{-1}=0,\qquad a_e=b_e-\rho a_{e-1}.
\tag{L-95241.4}
\]

Inductively, \(0<a_e\le b_e\): assuming \(a_{e-1}\le b_{e-1}\),

\[
a_e
\ge b_e-\rho b_{e-1}
> (1-\rho)b_{e-1}>0.
\]

Therefore every Dirichlet coefficient of \(A_\rho\) is strictly positive.

## 3. Nonnegative generalized primes

Define

\[
-\frac{A_\rho'}{A_\rho}(s)
=
\sum_{n\ge2}\frac{\Lambda_\rho(n)}{n^s}.
\]

For odd prime powers,

\[
\Lambda_\rho(p^r)=\log p.
\tag{L-95241.5}
\]

At \(2^r\),

\[
\boxed{
\frac{\Lambda_\rho(2^r)}{\log2}
=
1+2^{r/2}\bigl(1+(-1)^r\rho^r\bigr)>0.
}
\tag{L-95241.6}
\]

Thus

\[
\boxed{\Lambda_\rho(n)\ge0.}
\tag{L-95241.7}
\]

The logarithmic-derivative identity gives the coefficient-one positive divisor recursion

\[
\boxed{
a_\rho(n)\log n
=
\sum_{\substack{d\mid n\\d>1}}
\Lambda_\rho(d)a_\rho(n/d).
}
\tag{L-95241.8}
\]

After dividing by the left side, every \(n>1\) carries a genuine probability distribution on its proper divisor descents.

## 4. What this does and does not solve

`L-95241` supplies a source-specific positive arithmetic compiler rather than an abstract Farkas span. It preserves:

- one arithmetic coefficient per divisor occurrence;
- critical normalization;
- every dyadic orientation;
- nonnegative generalized-prime weights.

It does **not** prove that the packet's average-carry inverse is nonnegative. Positive inverse/generalized-prime data may not be promoted into a positive physical row without a source-to-row theorem.

## 5. Boundary

```text
positive inverse coefficients           PROPOSED COMPLETE EXACT
nonnegative generalized primes          PROPOSED COMPLETE EXACT
coefficient-one divisor compiler        PROPOSED COMPLETE EXACT
borrow-packet physical-row positivity   OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVED
```
