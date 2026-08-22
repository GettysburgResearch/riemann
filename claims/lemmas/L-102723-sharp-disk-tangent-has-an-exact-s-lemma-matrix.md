# L-102723 — The completion tangent carries an exact SHARP-disk S-lemma matrix

Claim ID: `L-102723`  
Status: **PROVED EXACT LOCAL MATRIX THEOREM**  
Created: 2026-08-22  
Depends on: `L-102722`  
RH status: **not assumed**

Fix `tau` and `X`. For the tangent source `Sigma_tau` of `L-102722`, define

\[
a=\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}\mathbf1_{n\le X},
\]

\[
h=\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}T(X/n),
\qquad
q=\sum_n\frac{\Sigma_\tau(n)}{\sqrt n}T(X/n)^2,
\]

where `T(y)=(4sqrt(y)-3)1_(y>=1)`.

Then

\[
q_z=q+2(\Re z)h+|z|^2a
\]

is nonnegative throughout the exact PR #690 disk by `L-102722`.

Put

\[
z_0=4\sqrt2-5,
\qquad
R=8-4\sqrt2.
\]

The disk is `|z-z_0|<=R`. Writing `z=z_0+w`, one has

\[
q_z
=a|w|^2+2(h+z_0a)\Re w
+q+2z_0h+z_0^2a.
\tag{L-102723.1}
\]

## 1. Exact S-lemma certificate

The disk has strict interior. The real S-lemma therefore gives a scalar

\[
\lambda=\lambda(\tau,X)\ge0
\]

such that

\[
\boxed{
\mathsf M_{\tau,X}=
\begin{pmatrix}
 a+\lambda & h+z_0a\\
 h+z_0a & q+2z_0h+z_0^2a-\lambda R^2
\end{pmatrix}
\succeq0.
}
\tag{L-102723.2}
\]

Equivalently,

\[
a+\lambda\ge0,
\qquad
q+2z_0h+z_0^2a-\lambda R^2\ge0,
\]

and

\[
\boxed{
(a+\lambda)
(q+2z_0h+z_0^2a-\lambda R^2)
\ge
(h+z_0a)^2.
}
\tag{L-102723.3}
\]

The slack `lambda` is one source-owned reserve. It may not be spent again in a second diagonal inequality.

## 2. Boundary Lorentz inequality

Evaluating (L-102723.1) at the two real boundary points gives directly

\[
\boxed{
2R|h+z_0a|
\le
q+2z_0h+(z_0^2+R^2)a.
}
\tag{L-102723.4}
\]

Since

\[
R+z_0=3,
\qquad
R^2-z_0^2=39-24\sqrt2,
\]

whenever `h+z_0a<0`,

\[
\boxed{
-(h+z_0a)
\le
\frac{q+(39-24\sqrt2)a}{6}.
}
\tag{L-102723.5}
\]

The right-hand side is automatically nonnegative in that case.

## 3. One fixed five-to-one projection

The fixed point

\[
z_*=-\frac25+i\frac{4\sqrt6}{5}
\]

lies strictly inside the audited disk because

\[
(3+\tfrac25)^2+\frac{96}{25}
=
\frac{77}{5}
<
(16-8\sqrt2)\frac{17}{5}.
\]

At this point

\[
q_{z_*}=q-\frac45h+4a\ge0,
\]

so

\[
\boxed{
5a-h\ge-\frac54q.
}
\tag{L-102723.6}
\]

This is a fixed, source-faithful one-sided relation between the activation, critical-current and quadratic-current coordinates.

## Scope

The theorem supplies the exact local Perron/Pick-type matrix missing from the unfiltered completion current. It does not assert that the signed compact dyadic filter or the distinct-product physical collapse preserves the matrix cone.