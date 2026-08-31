# L-105680 — Determinant-strength CTI and a spectral-flatness region

**Claim ID:** `L-105680`  
**Status:** proved exact all-rank finite-packet theorem  
**Date:** 2026-08-31  
**RH:** not assumed

Let

\[
G_s(i,j)=\frac1{\overline\lambda_i+\lambda_j+s},
\qquad \Re\lambda_j>0,
\]

and fix `H>0`. Define the normalized current and overlap matrices

\[
B_H=G_0^{-1/2}G_HG_0^{-1/2},
\]

\[
A_H=G_0^{-1/2}G_{2H}G_{4H}^{-1}G_{2H}G_0^{-1/2}.
\tag{1}
\]

Their traces are the current mass `mathcal T_H` and the Cauchy-translation
overlap `mathcal O_H`.

## 1. Exact determinant gain

For distinct nodes the Cauchy determinant is

\[
\det G_s=
\frac{\prod_{i<j}|\lambda_i-\lambda_j|^2}
{\prod_i(2\Re\lambda_i+s)
 \prod_{i<j}|\overline\lambda_i+\lambda_j+s|^2}.
\tag{2}
\]

Consequently

\[
\boxed{
\frac{\det A_H}{\det B_H}=\mathscr D_H,
}
\tag{3}
\]

where

\[
\boxed{
\begin{aligned}
\mathscr D_H
={}&\prod_i
\frac{(2\Re\lambda_i+H)(2\Re\lambda_i+4H)}
     {(2\Re\lambda_i+2H)^2}\\
&\times\prod_{i<j}
\left|
\frac{(\overline\lambda_i+\lambda_j+H)
      (\overline\lambda_i+\lambda_j+4H)}
     {(\overline\lambda_i+\lambda_j+2H)^2}
\right|^2.
\end{aligned}
}
\tag{4}
\]

Every factor is strictly larger than one. For a diagonal factor this follows
from

\[
(x+H)(x+4H)-(x+2H)^2=xH>0.
\]

For an off-diagonal pair, writing
`z=x+iy`, `x>0`, gives

\[
\boxed{
\begin{aligned}
&[(x+H)^2+y^2][(x+4H)^2+y^2]
-[(x+2H)^2+y^2]^2\\
&\qquad=H(8H^2x+9Hx^2+9Hy^2+2x^3+2xy^2)>0.
\end{aligned}
}
\tag{5}
\]

Hence

\[
\boxed{
\det A_H>\det B_H
}
\tag{6}
\]

for every nonempty distinct packet; confluent derivative packets follow by
continuity after the standard normalization.

This is the constant-one CTI at determinant/geometric-mean strength, valid at
every rank and height even though the stronger Loewner premise `MLC105656` is
false.

## 2. Spectral-flatness criterion for trace CTI

Let `alpha_i` and `beta_i` be the eigenvalues of `A_H` and `B_H`. AM--GM and
(3) give

\[
\mathcal O_H
=\sum_i\alpha_i
\ge n(\det A_H)^{1/n}
=n\mathscr D_H^{1/n}(\det B_H)^{1/n}.
\tag{7}
\]

Therefore

\[
\boxed{
\frac{\operatorname{tr}B_H}
     {n(\det B_H)^{1/n}}
\le\mathscr D_H^{1/n}
\Longrightarrow
\mathcal O_H\ge\mathcal T_H.
}
\tag{8}
\]

Thus CTI holds whenever the arithmetic-mean/geometric-mean dispersion of the
current spectrum is paid by the explicit Cauchy determinant gain.

A convenient stronger sufficient condition is

\[
\boxed{
\kappa(B_H)\le\mathscr D_H^{1/n},
}
\tag{9}
\]

because `AM/GM<=lambda_max/lambda_min`.

## 3. Scope

The determinant theorem does not imply the trace theorem for an arbitrary
spectrally dispersed packet. It gives a new all-rank closed region and an
explicit quantitative resource for the remaining intermediate-contact
problem. No Loewner order is asserted.
