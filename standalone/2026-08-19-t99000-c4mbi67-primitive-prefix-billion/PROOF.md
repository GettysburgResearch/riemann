# Primitive-prefix reconstruction of T-97701/C4MBI67

This file is the concise proof map. The complete proofs, including the
specialized Landau theorem, theta/Poisson functional equation, exact rational
scanner argument, and hostile boundary audit, are in `main.tex` and the
canonical PDF.

## 1. Arithmetic dictionary

Let `q(1)=0`, `q(2)=15`, `q(4)=3`, and `q(n)=6` otherwise. With `a=q*mu`,

\[
a(n)=6\mathbf 1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)-3\mathbf1_{4\mid n}\mu(n/4).
\]

For

\[
R_X=\sum_n {a(n)\over\sqrt n}\log(X/n)_+,
\qquad A_X=R_X-R_{X/4},
\]
put

\[
C(t)=\sum_{n\le t}{a(n)\over\sqrt n}.
\]

Finite Fubini gives the decisive identity

\[
\boxed{A_X=\int_{X/4}^{X}C(t){dt\over t}.}
\]

Thus the pointwise theorem `C(t)>=0` is a strictly stronger sufficient
producer for C4MBI67.

## 2. Three-band and four-band forms

Writing `B(t)=sum_(n<=t) mu(n)/sqrt(n)`, one has

\[
C(t)=6-\left(6B(t)-{9\over\sqrt2}B(t/2)+{3\over2}B(t/4)\right).
\]

A second finite Fubini step recovers exactly the four-band T-97701 boundary.
No asymptotic estimate enters either identity.

## 3. Source ownership

For squarefree `n>1`,

\[
\mu(n)\log n=-\sum_{p\mid n}\mu(n/p)\log p.
\]

Dividing by `log n` and reindexing gives the exact prime–Möbius owner
decomposition. Every source atom is spent once through weights
`log p/log n`.

## 4. Weighted threshold complex

Introduce three dyadic labels of cost `2` and activities
`2^{-1/2},2^{-1/2},2^{-3/2}`, plus one label of cost `p` and activity
`p^{-1/2}` for each odd prime. Then

\[
{C(t)\over6}
=\sum_{\varnothing\ne S,\,P(S)\le t}(-1)^{|S|+1}r(S),
\]

the expected Euler characteristic of the induced multiplicative-threshold
complex. Adding one label `(p,r)` obeys exactly

\[
G_{V\cup\{p\}}(X)=G_V(X)+r\{H_X(p)-G_V(X/p)\}.
\]

This is the complete source-faithful Bellman recurrence. A literal finite
fixture at threshold `26` is negative, so independent pointwise PSD/Schur ports
do not compose; future-prime correlation is essential.

## 5. Analytic consumer

For `z=s+1/2`,

\[
\int_1^\infty A_X X^{-s-1}dX
={1-4^{-s}\over s^2}
\left[6-{3(1-2^{-z})(2-2^{-z})\over\zeta(z)}\right].
\]

The manuscript proves, rather than imports, the needed nonnegative-density
Landau theorem and derives the zeta functional equation from Poisson summation
for the Gaussian. Consequently eventual `A_X>=0` excludes every zeta zero with
real part greater than `1/2`; reflection excludes every zero with real part
less than `1/2`.

## 6. Exact finite theorem

The scanner sets `S=2^40` and computes the exact integer `q_n` satisfying

\[
q_n^2n\le S^2<(q_n+1)^2n.
\]

Each signed term is rounded outward. The complete run through `10^9` gives

```text
minimum lower numerator: 1226685126915
scale:                   1099511627776
minimum endpoint:        48433
```

so `C(t)>=0` for every real `1<=t<1,000,000,001` and therefore `A_X>=0` on the
same range.

## 7. Exact boundary

The all-scale statement

\[
\boxed{C(t)\ge0\quad(t\ge1)}
\]

has not been proved. It is the sole remaining line in this strengthened route.
Accordingly C4MBI67 and RH remain open in this packet.
