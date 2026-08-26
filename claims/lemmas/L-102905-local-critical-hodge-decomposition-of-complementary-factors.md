# L-102905 — Local critical Hodge decomposition of every complementary factorization

Claim ID: `L-102905`  
Status: **PROVED EXACT LOCAL TENSOR DECOMPOSITION**  
Created: 2026-08-25  
Depends on: `L-102901--L-102904`  
RH status: **not assumed**

Work in one labelled-prime Euler algebra with variable

\[
x=p^{-1/2}U_p.
\]

Let

\[
E=1-x,
\qquad
C=1-x^2,
\]

and let

\[
F_t=(1-x)(1+x)^t,
\qquad
G_t=(1-x)(1+x)^{1-t}.
\]

Then

\[
F_tG_t=EC
\]

for every real or complex temperature `t`.

Put

\[
M={E+C\over2}=1-{x\over2}-{x^2\over2},
\qquad
\Omega=x\otimes1-1\otimes x.
\]

Let `pi` denote arithmetic multiplication from the two-factor tensor algebra to the local Euler algebra.

## 1. Exact critical-order decomposition

The first coefficients are

\[
F_t=1+(t-1)x+O(x^2),
\qquad
G_t=1-tx+O(x^2),
\]

whereas

\[
M=1-{x\over2}+O(x^2).
\]

Consequently there is an exact tensor `V_t` such that

\[
\boxed{
F_t\otimes G_t
=
M\otimes M
+
\left(t-{1\over2}\right)\Omega
+
V_t,
}
\tag{L-102905.1}
\]

with

\[
\boxed{
\pi(\Omega)=0,
\qquad
\pi(V_t)\in x^2\mathbf C[[x]].
}
\tag{L-102905.2}
\]

Indeed the root and first-order tensor coefficients agree after subtracting the displayed antisymmetric term, while

\[
\pi(V_t)=EC-M^2=-{1\over4}x^2(1-x)^2.
\tag{L-102905.3}
\]

Thus every complementary temperature differs from the arithmetic midpoint by exactly two kinds of directions:

```text
an antisymmetric flat-gauge direction killed by convolution;
a squared/higher-prime-power direction.
```

No other critical local coordinate exists.

## 2. Orthogonal Hodge energy

Write the two first-chaos coefficients as

\[
a=t-1,
\qquad
b=-t.
\]

They satisfy

\[
a+b=-1.
\]

The decomposition

\[
(a,b)
=
\left(-{1\over2},-{1\over2}\right)
+
\left(t-{1\over2}\right)(1,-1)
\]

is orthogonal in the Euclidean tensor metric. Hence

\[
\boxed{
|a|^2+|b|^2
=
{1\over2}
+2\left|t-{1\over2}\right|^2.
}
\tag{L-102905.4}
\]

The midpoint is therefore the unique minimum-energy lift of the fixed first-chaos target.

## 3. Quotient formulation

Modulo the sum of

```text
ker(pi);
preimages of x^2 C[[x]],
```

the normalized complementary-factor space has one affine critical class, represented by

\[
\boxed{M\otimes M.}
\tag{L-102905.5}
\]

The class is independent of temperature, endpoint color, complex phase, or factor ordering.

This is a Hodge decomposition in the literal sense used here:

```text
harmonic part:       M tensor M;
exact/gauge part:    multiple of Omega;
subcritical part:    V_t.
```

It is a source identity, not a physical sign theorem.
