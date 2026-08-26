# L-105404 — The primitive F1 Hodge energy is exactly the orthogonal activation–slope energy

Claim ID: `L-105404`

Status: **PROVED EXACT ORTHOGONAL DECOMPOSITION**

Retain the full filtered SHARP disk of PR #719 in centered coordinate

\[
P(w)=P_0+2B\operatorname{Re}w+A|w|^2,
\qquad |w|\le\frac12,
\]

where

\[
B=G-A.
\]

The three real rays are `w=-1/2,0,1/2`, and `L-105402` gives the primitive
Hodge energy

\[
\mathcal H_{\rm prim}(A,G)
=
\frac{49A^2-96AG+48G^2}{24}.
\]

Substituting `G=A+B` gives the exact orthogonal factorization

\[
\boxed{
\mathcal H_{\rm prim}(A,G)
=
\frac{A^2}{24}+2B^2.
}
\tag{L-105404.1}
\]

Thus the finite Hodge norm has two and only two primitive coordinates:

```text
A / sqrt(24)       radial activation curvature;
sqrt(2) B          filtered-disk scale/phase slope.
```

The conclusion-facing outer-ray/Lorentz current is

\[
5A-G=4A-B.
\tag{L-105404.2}
\]

Cauchy in the orthogonal coordinates gives

\[
\boxed{
(4A-B)^2
\le
\frac{769}{2}
\left(\frac{A^2}{24}+2B^2\right).
}
\tag{L-105404.3}
\]

The constant is optimal, and the exact residual is

\[
\boxed{
\frac{769}{2}\mathcal H_{\rm prim}-(4A-B)^2
=
\frac{(A+192B)^2}{48}.
}
\tag{L-105404.4}
\]

## Exact conjunctive equivalence

For any measurable source region `Omega`,

\[
\int_\Omega\sqrt{\mathcal H_{\rm prim}}
\le
\frac1{\sqrt{24}}\int_\Omega|A|
+
\sqrt2\int_\Omega|B|,
\tag{L-105404.5}
\]

while

\[
\int_\Omega|A|
\le\sqrt{24}\int_\Omega\sqrt{\mathcal H_{\rm prim}},
\]

\[
\int_\Omega|B|
\le\frac1{\sqrt2}\int_\Omega\sqrt{\mathcal H_{\rm prim}}.
\tag{L-105404.6}
\]

Therefore the cofinal primitive-energy theorem is equivalent, up to fixed
constants, to the conjunction of the activation-curvature and disk-slope
estimates on the same source partition. Neither coordinate may be proved on a
different normalization and then combined after physical collapse.

This is the exact `F1` explanation for why the reviewed `CV` and `XD` middle
classes recur together.
