# L-102831 — Largest-two completion produces a unique semiprime squareclass

Claim ID: `L-102831`  
Status: **PROVED EXACT COMBINATORIAL/PHYSICAL THEOREM**  
Created: 2026-08-24  
Depends on: `L-102830`; `L-102704`; PR #715 squared-core completion  
RH status: **not assumed**

Work in the hard largest-two gauge of `L-102830`, after the joint occurrence of
the two labelled `67` copies has been placed in the closed repeated-physical-
prime diagonal. Every retained owner pair therefore consists of distinct
physical primes.

A squarefree hard occurrence has

\[
n=pq\,m,
\qquad p>q>P^+(m),
\qquad n\le16Y.
\]

Every prime `r|m` satisfies `r<q` and

\[
r^2<qr\le qm\le n\le16Y.
\]

Hence

\[
\boxed{r<4\sqrt Y.}
\tag{L-102831.1}

The source-faithful completion at `Z=4 sqrt(Y)` therefore squares every
cofactor prime. In the completed regional gauge the physical product is

\[
\boxed{N=pq\,a^2,}
\tag{L-102831.2}

where `a` is squarefree and every prime divisor of `a` is smaller than `q`.
The sole unsquared physical primes are the two largest owners.

## 1. Exact injectivity

Suppose

\[
pq\,a^2=rs\,b^2,
\]

with

\[
p>q>P^+(a),
\qquad r>s>P^+(b),
\]

and with `p,q` and `r,s` distinct inside each pair. The squarefree kernel of
the left side is `pq`; the squarefree kernel of the right side is `rs`. Thus
`{p,q}={r,s}`. The prescribed order gives `p=r`, `q=s`, and then `a=b`.

Therefore

\[
\boxed{
(p,q,a)\longmapsto pq\,a^2
\text{ is injective on the hard sector.}
}
\tag{L-102831.3}

The excluded double-`67` pair has squarefree kernel one and remains in the
already-closed squared diagonal; it is not silently treated as a semiprime.

## 2. Exact squareclass interpretation

For every retained completed occurrence,

\[
\operatorname{rad}(N)\bmod (\mathbb Q^\times)^2=pq.
\]

Thus the hard owner pair is exactly the semiprime squarefree kernel of the
physical integer, not an auxiliary label. The remaining physical restriction
is a correlation between distinct semiprime squareclasses.

The polylogarithmic gauge transfer back to the native Euler current is already
proved in `L-102706--L-102709`; no new source or reserve is introduced.