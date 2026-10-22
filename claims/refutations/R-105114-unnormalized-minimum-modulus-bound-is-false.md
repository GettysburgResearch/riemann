# R-105114 - An unnormalized minimum-modulus display is false

Claim ID: R-105114

Status: **REFUTED BY CONSTANT FUNCTION**

Created: 2026-08-23

RH status: **not applicable**

## Refuted statement

Suppose a claimed lower bound has the form

\[
\log|f(z)|
\ge-C\log(1/\delta)
\left(\max\log|f|-\log|f(a)|\right)
\tag{R-105114.1}
\]

outside disks around the zeros, with no normalization on the left.

## Exact counterexample

Take the constant holomorphic function

\[
f(z)\equiv\frac12.
\tag{R-105114.2}
\]

It has no zeros, and its growth difference is exactly zero:

\[
\max\log|f|-\log|f(a)|=0.
\tag{R-105114.3}
\]

The claimed right-hand side is therefore zero, while

\[
\log|f(z)|=\log(1/2)<0.
\tag{R-105114.4}
\]

Thus (R-105114.1) is false. Multiplication by a nonzero constant leaves
the growth difference unchanged but shifts the left side.

## Repair

Normalize first and state

\[
\log\left|\frac{f(z)}{f(a)}\right|\ge-\text{normalized load},
\qquad f(a)\ne0.
\tag{R-105114.5}
\]

L-105114 also retains the dimensionless spatial coefficient
\(2r_1/(r_2-r_1)\). This refutation does not invalidate normalized Cartan
or Jensen arguments; it forbids importing an amplitude-unnormalized
display verbatim.
