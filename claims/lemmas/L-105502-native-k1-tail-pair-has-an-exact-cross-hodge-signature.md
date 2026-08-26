# L-105502 — The native tail pair has an exact cross-Hodge mismatch signature

Claim ID: `L-105502`

Status: **PROVED EXACT SOURCE/KERNEL AND REFLECTION-HODGE FACTORIZATION**

Created: 2026-08-27

Depends on: `L-102500`, `L-102701`, `L-105501`

RH status: **not assumed**

Let \(A\) be the positive ratio-four half-kernel with

\[
\widehat A(s)
=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-\frac12)}.
\]

Let \(K_1\) be the corrected same-\(K_1\) ordinary-Möbius wavelet of
`L-100310`.

## 1. Exact half-kernel factorization

Write

\[
Q(D)=(D+\tfrac32)(D-\tfrac12).
\]

The multipliers satisfy

\[
\begin{aligned}
Q(s)\widehat A(s)^2
&=
(s+\tfrac32)(s-\tfrac12)
\frac{(1-2^{-s})^2(1-\sqrt2\,2^{-s})^2}
{s^2(s-\frac12)^2}\\
&=
\widehat K_1(s).
\end{aligned}
\]

Therefore

\[
\boxed{K_1=Q(D)(A*_M A).}
\tag{L-105502.1}
\]

This identity is on the native detector and contains no owner/core completion.

## 2. Native colored fields

For a prime coloring \(\chi\), define

\[
F_{U,\chi}^\pm(X)
=
\sum_n
\frac{f_{U,\chi}^\pm(n)}{\sqrt n}
A(X/n),
\]

where \(f_{U,\chi}^\pm\) are from `L-105501`.  Finite Mellin Fubini and
(L-105501.6) give

\[
\boxed{
\mathcal B_U^{K_1}
=
Q(D)\bigl(F_{U,\chi}^+*_M F_{U,\chi}^-\bigr).
}
\tag{L-105502.2}
\]

The left side is the literal balanced Vaughan current on the same \(K_1\)
detector.  It is independent of \(\chi\).

In the extreme tail gauge,

\[
F_{U,+}=\mathcal O_A[\nu_U],
\qquad
F_{U,-}=\mathcal O_A[a_U].
\tag{L-105502.3}
\]

## 3. Cross-Hodge polarization

Freeze a finite source horizon and put, on logarithmic coordinates,

\[
f_\chi(u)=F_{U,\chi}^+(e^u),
\qquad
g_\chi(u)=F_{U,\chi}^-(e^u).
\]

Let

\[
(R_xg)(u)=g(x-u).
\]

Define the alignment and mismatch energies

\[
\boxed{
\mathcal A_\chi(x)
=
\frac14\|f_\chi+R_xg_\chi\|_2^2,
\qquad
\mathcal D_\chi(x)
=
\frac14\|f_\chi-R_xg_\chi\|_2^2.
}
\tag{L-105502.4}
\]

Both are nonnegative.  Polarization gives

\[
\boxed{
(F_{U,\chi}^+*_MF_{U,\chi}^-)(e^x)
=
\mathcal A_\chi(x)-\mathcal D_\chi(x).
}
\tag{L-105502.5}
\]

Moreover,

\[
\boxed{
\mathcal A_\chi(x)+\mathcal D_\chi(x)
=
\frac12(\|f_\chi\|_2^2+\|g_\chi\|_2^2),
}
\tag{L-105502.6}
\]

which is independent of \(x\).

The cross-convolution in (L-105502.5) is the same source for every coloring.
Therefore, for two colorings \(\chi,\chi'\),

\[
\boxed{
\mathcal D_\chi(x)-\mathcal D_{\chi'}(x)
=
\frac14\left(
\|f_\chi\|_2^2+\|g_\chi\|_2^2
-\|f_{\chi'}\|_2^2-\|g_{\chi'}\|_2^2
\right).
}
\tag{L-105502.7}
\]

Thus prime color is a flat Hodge gauge: it changes the mismatch baseline but
not any differential conclusion-facing current.

## 4. The derivative current is one mismatch variation

Put

\[
K_2=DK_1,
\qquad
L(D)=DQ(D)=D(D+\tfrac32)(D-\tfrac12).
\]

Since \(L(D)\) annihilates the constant in (L-105502.6),

\[
\boxed{
\mathcal B_U^{K_2}(e^x)
=
2L(D)\mathcal A_\chi(x)
=
-2L(D)\mathcal D_\chi(x).
}
\tag{L-105502.8}
\]

Consequently,

\[
\boxed{
(\mathcal B_U^{K_2})_-
=
2\bigl(L(D)\mathcal D_\chi\bigr)_+.
}
\tag{L-105502.9}
\]

This is an exact one-sided identity, not a Cauchy majorant.

## 5. Native F1 meaning

The live ordinary-Möbius terminal packet is the differential variation of one
nonnegative reflected mismatch between two long source fields.  There are:

```text
no imposed owner/core square completion;
no Wick-to-ordinary contraction correction;
no semiprime completion mode;
no owner-pair physical collapse.
```

Natural repeated prime powers in the ordinary Vaughan convolution are retained
with their literal coefficients; they are not discarded as contractions.

The remaining estimate is the source-specific variation of
\(\mathcal D_\chi\).  Positivity of \(\mathcal D_\chi\) alone does not control
the sign of its third-order differential image.
