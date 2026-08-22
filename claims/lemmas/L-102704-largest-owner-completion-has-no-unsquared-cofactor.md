# L-102704 — A square-root cofactor completion leaves no unsquared cofactor prime

Claim ID: `L-102704`  
Status: **PROVED EXACT COMBINATORIAL CORRECTION**  
Created: 2026-08-22  
Depends on: PR #691 `L-100600`; largest-prime ownership  
RH status: **not assumed**

In a largest-prime wavelet occurrence write

\[
n=pm,
\qquad
p=P^+(n),
\qquad
P^+(m)<p,
\qquad
pm\le X.
\]

Let \(q\mid m\) be any prime factor of the cofactor. Then

\[
q<p
\]

and

\[
pq\le pm\le X.
\]

Since \(p>q\),

\[
\boxed{q^2<pq\le X,\qquad q<\sqrt X.}
\tag{L-102704.1}
\]

Therefore a source-faithful cofactor completion at

\[
Z_X=\sqrt X
\]

squares **every** cofactor prime. There is no optional unsquared cofactor label
above \(\sqrt X\).

The completed largest-owner packet has the exact physical form

\[
\boxed{n=p a^2,}
\tag{L-102704.2}
\]

where every prime divisor of the squarefree label product \(a\) is strictly
smaller than \(p\). The sole unsquared label is the greatest owner \(p\).

## Same-product injectivity

Suppose

\[
p a^2=q b^2
\]

with

\[
p>P^+(a),
\qquad
q>P^+(b).
\]

If \(p\ne q\), assume \(p>q\). The left side has odd \(p\)-adic valuation.
Thus \(p\mid b\), contradicting \(P^+(b)<q<p\). Hence \(p=q\), and then
\(a=b\).

Therefore

\[
\boxed{
(p,a)\longmapsto p a^2
\text{ is injective on the completed largest-owner source.}
}
\tag{L-102704.3}
\]

This removes both the alleged depth-one cofactor sector and every same-product
collision between distinct owner/core pairs.

## Remaining scope

PR #715 `L-102505` gives polylogarithmic collapse for the full squared core.
After (L-102704.3), the only occupancy problem is overlap of **distinct**
products

\[
p a^2\ne q b^2
\]

inside the compact multiplicative observation window. No owner or factor-pair
multiplicity remains.
