# L-105490 — The bounded derivative-outer density has a different exact Mellin symbol

Claim ID: `L-105490`

Status: **PROVED EXACT KERNEL/SYMBOL CORRECTION**

Created: 2026-08-26

Depends on: `L-102701`, corrected `L-102866`, `L-102880`, `L-103070--L-103071`

RH status: **not assumed**

Let \(D=y\,d/dy\), and let the bounded derivative-outer density be

\[
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-105490.1}
\]

Use the Mellin convention

\[
\widehat f(s)=\int_0^\infty f(y)y^{-s}\frac{dy}{y}.
\]

## 1. Direct symbol

Integrating the three affine-in-\(\sqrt y\) pieces gives, first for generic
\(s\) and then by removable continuation,

\[
\boxed{
\widehat K_L(s)=
\frac{
4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})
}{
s(s-\tfrac12)
}.
}
\tag{L-105490.2}
\]

This formula agrees with the zero logarithmic moment
\(\widehat K_L(0)=0\), interpreted by continuation.

Let

\[
\widehat A(s)=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-\tfrac12)}
\tag{L-105490.3}
\]

be the positive ratio-four half-kernel, and put

\[
P(s)=\frac12s(s-1)(5s+\tfrac32)(2s-1).
\tag{L-105490.4}
\]

Then

\[
P(s)\widehat A(s)^2
=
\frac{
(s-1)(5s+\tfrac32)(1-2^{-s})^2
(1-\sqrt2\,2^{-s})^2
}{
s(s-\tfrac12)
}.
\tag{L-105490.5}
\]

Equations (L-105490.2) and (L-105490.5) are not equal.

## 2. Exact bridge

Their exact relation is

\[
\boxed{
(5s+\tfrac32)(1-\sqrt2\,2^{-s})\widehat K_L(s)
=
4P(s)\widehat A(s)^2.
}
\tag{L-105490.6}
\]

Let \((\mathsf Sf)(y)=f(y/2)\). Since \(\mathsf S\) has Mellin multiplier
\(2^{-s}\), (L-105490.6) is the compact-distribution identity

\[
\boxed{
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)K_L
=
4P(D)(A*_M A).
}
\tag{L-105490.7}
\]

No boundary convention changes the missing factor:
it is a genuine dyadic/differential bridge.

## 3. Sourcewise form

For any finite coefficient source \(b=(b_n)\), put

\[
H_b(X)=\sum_n b_nK_L(X/n),
\qquad
J_b(X)=\sum_n b_n(A*_MA)(X/n).
\]

Finite Mellin Fubini gives coefficientwise

\[
\boxed{
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)H_b
=
4P(D)J_b.
}
\tag{L-105490.8}
\]

For the canonical Boolean source, the exact Wick version uses the
normal-ordered half-source square. Replacing it by the ordinary completion
adds the already-declared repeated-label contraction ledger, but does not
remove the operator in (L-105490.8).

## Binding disposition

The historical identities

```text
H_K = P(D) J_U
H_K = -2 P(D) O_U
```

are therefore superseded. The reflection identities for \(J_U\) and
\(P(D)J_U\) remain exact. Their transfer to the bounded density \(H_K\)
must pass through (L-105490.8).
