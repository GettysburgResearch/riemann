# L-105491 — The missing dyadic bridge has a stable anti-causal resolvent

Claim ID: `L-105491`

Status: **PROVED EXACT RESOLVENT AND ONE-WAY VARIATION TRANSFER**

Created: 2026-08-26

Depends on: `L-105490`, corrected `L-105463`, `L-106134--L-106135`

RH status: **not assumed**

Write \(x=\log X\), \(L=\log2\), and let

\[
(\tau_Lh)(x)=h(x-L).
\]

The sourcewise bridge of `L-105490` becomes

\[
(5\partial_x+\tfrac32)(I-\sqrt2\,\tau_L)H
=
4G,
\tag{L-105491.1}
\]

where \(H(x)\) is the bounded derivative-outer current and
\(G=P(\partial_x)J\) is the differential reflection/analytic-square current,
modulo the inherited closed field.

## 1. The dyadic inverse is anti-causal and bounded

Because \(\sqrt2>1\),

\[
\boxed{
(I-\sqrt2\,\tau_L)^{-1}
=
-\sum_{j\ge1}2^{-j/2}\tau_L^{-j}.
}
\tag{L-105491.2}
\]

The series converges in every translation-invariant \(L^p(\mathbb R)\),
\(1\le p\le\infty\), and

\[
\boxed{
\|(I-\sqrt2\,\tau_L)^{-1}\|_{L^p\to L^p}
\le \frac1{\sqrt2-1}.
}
\tag{L-105491.3}
\]

For compact packets it is pointwise finite at every fixed \(x\).
The forward geometric series
\(\sum_{j\ge0}2^{j/2}\tau_L^j\) is the wrong inverse branch.

## 2. Differential resolvent

The causal inverse is

\[
\boxed{
[(5\partial_x+\tfrac32)^{-1}g](x)
=
\frac15\int_{-\infty}^x
e^{-3(x-y)/10}g(y)\,dy.
}
\tag{L-105491.4}
\]

It is positive and has \(L^p\)-norm at most \(2/3\).
Consequently

\[
\boxed{
\|H\|_{L^p}
\le
\frac{8}{3(\sqrt2-1)}\,\|G\|_{L^p},
\qquad 1\le p\le\infty,
}
\tag{L-105491.5}
\]

whenever \(G\) is an \(L^p\) function. The same inequality holds for finite
signed measures with total variation on the right.

Thus the reflection gate

```text
F1VAR105460 = REFSIG106150 = SFSC106150:
  subpower total variation of G
```

is a valid sufficient condition for subpower logarithmic \(L^1\) mass of the
bounded current \(H\).

The converse is not asserted: differentiation is not bounded on \(L^1\), and
bounded variation of \(H\) does not follow from its \(L^1\) norm.

## 3. Critical conjugation

Let

\[
(C_{1/4}H)(x)=e^{-x/4}H(x).
\]

Then

\[
C_{1/4}(5\partial_x+\tfrac32)C_{1/4}^{-1}
=5\partial_x+\frac{11}{4},
\]

and

\[
C_{1/4}(I-\sqrt2\,\tau_L)C_{1/4}^{-1}
=I-2^{1/4}\tau_L.
\tag{L-105491.6}
\]

Hence

\[
\boxed{
(I-2^{1/4}\tau_L)^{-1}
=
-\sum_{j\ge1}2^{-j/4}\tau_L^{-j},
}
\tag{L-105491.7}
\]

with norm at most \(1/(2^{1/4}-1)\), while

\[
\|(5\partial_x+\tfrac{11}{4})^{-1}\|_{L^p\to L^p}
\le\frac4{11}.
\tag{L-105491.8}
\]

The critical bridge is therefore stable after the correct inverse branch is
chosen. Its role is nevertheless essential: it supplies exactly one
high-frequency smoothing factor missing from the historical unregularized
analytic-square norm.
