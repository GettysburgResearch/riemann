# L-105452 — Fixed clean Plücker packets have modulus-free phase normalization

Claim ID: `L-105452`

Status: **PROVED EXACT COMPOSITION OF FROZEN FIXED-PACKET THEOREMS**

Retain one clean owner quadruple

\[
P=\{p,q\},\qquad Q=\{r,s\},
\]

and square-core octaves

\[
A\le a<2A,
\qquad
B\le b<2B.
\]

By `L-105451`, its Plücker coefficient has two nontrivial augmentation
coordinates. Using all four owner phases, PR #719 `L-102864` gives

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
\left(1+\frac{rs}{A}\right)^{1/2}
\left(1+\frac{pq}{B}\right)^{1/2}.
}
\tag{L-105452.1}
\]

Every explicit owner factor cancels the dimension of its corresponding
augmentation representation. In the doubly long range

\[
A\ge rs,\qquad B\ge pq,
\]

one obtains

\[
\boxed{|\mathcal C_{P,Q}|\ll1.}
\tag{L-105452.2}
\]

The adaptive 15-choice selector of `L-102865` gives the exact long/short
interpolation for all other core regimes.

## Type-I removal

The centered outer kernel has the exact square-lattice moment

\[
\int_1^8R_L(y)\frac{dy}{y}=0.
\]

The Vaughan identity of `L-102867` therefore removes every complete-lattice
and Type-I core term with an integrable \(O(Y^{-1/6})\) error. The surviving
core variables satisfy

\[
r,s>Y^{1/6},
\qquad
m\ll Y^{1/6},
\qquad
rsm\asymp\sqrt Y.
\tag{L-105452.3}
\]

Thus the direct F1 trace contains none of the following:

```text
singleton carrier;
shared owner;
owner/core incidence;
equal product;
pair diagonal;
trivial augmentation character;
fixed-quadruple owner modulus;
complete square lattice;
Type-I core.
```

Only the signed coherent summation of the balanced packets remains.
