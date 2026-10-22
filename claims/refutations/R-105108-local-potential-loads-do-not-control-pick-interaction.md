# R-105108 — Local potential loads do not control Pick interaction

Claim ID: R-105108

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105107; L-105108

RH status: **unproved**

## Refuted inference 1: magnitudes determine the optimum

The following implication is false:

> Once every targetwise Green load \(|y_c|\) and every target location are
> known, their magnitudes determine the multipoint selector norm.

Use target nodes \(-1/2,1/2\) in the unit disk.  Their normalized Gram
matrix is

\[
G=
\begin{pmatrix}
1&3/5\\
3/5&1
\end{pmatrix},
\qquad
\kappa_2(G)=4.
\tag{R-105108.1}
\]

For values \((2,2)\), the constant interpolant gives

\[
\tau_{+}=2.
\tag{R-105108.2}
\]

For values \((-2,2)\), the unique extremal is \(H(z)=4z\), so

\[
\tau_{-}=4=2\sqrt{\kappa_2(G)}.
\tag{R-105108.3}
\]

The nodes, conformal radii, Green distances, product separations, and value
magnitudes are identical.  Only the phases differ.  Scalar potential loads
therefore do not determine the full Pick optimum.

## Selector-compatible collision

This phase debt occurs inside the exact L-105107 residue-selector class.
Take targets \(\pm\varepsilon\), both of order one with \(\gamma=1\), and
a simple nontarget at zero.  The forced inner function is \(I_0(z)=z\), so

\[
y_{-\varepsilon}=-\varepsilon^{-1},
\qquad
y_{\varepsilon}=\varepsilon^{-1}.
\tag{R-105108.4}
\]

The optimal interpolant and selector are

\[
H_*(z)=z/\varepsilon^2,
\qquad
W_*(z)=z^2/\varepsilon^2,
\qquad
\tau=\varepsilon^{-2}.
\tag{R-105108.5}
\]

At \(\varepsilon=1/5\), the local load is only \(Y=5\), while
\(\tau=25\).  The normalized Gram condition number is \(25\), and the
upper bound \(Y\sqrt\kappa\) is sharp.  The uncentred target-cardinal
envelope is \(26\).

## Refuted inference 2: every pair test is enough

The implication

> all one- and two-target Pick restrictions are feasible at norm \(u\), so
> the full target problem is feasible at norm \(u\)

is also false.  Take nodes and values

\[
c=(-1/2,0,1/2),
\qquad
y=(-1,1,-1).
\tag{R-105108.6}
\]

The two adjacent restrictions have optimum \(2+\sqrt3\), and the endpoint
restriction has optimum one.  But the complete determinant is

\[
\det(sK-D_yKD_y^*)
=\frac{16}{225}(s-1)(s^2-62s+1).
\tag{R-105108.7}
\]

Consequently

\[
\tau_{\rm full}
=\sqrt{31+8\sqrt{15}}
=4+\sqrt{15}
>2+\sqrt3.
\tag{R-105108.8}
\]

Every two-by-two principal Pick matrix can therefore be positive
semidefinite while the full matrix remains indefinite.

## Refuted inference 3: smooth fixed geometry removes separation debt

In the unchanged unit disk, take target zero of order one with \(\gamma=1\)
and one nontarget \(a=1/n\) of fixed order \(m\), for integers
\(n\ge2\), \(m\ge1\).  The exact one-target normalization is

\[
\beta=(-1/n)^m,
\qquad
\tau=n^m.
\tag{R-105108.9}
\]

Thus smooth boundary, conformal radius one, fixed target data, and fixed
total multiplicity do not yield a separation-free norm bound.

## Consequence

Finite potential sums, target separation, and Gram conditioning give useful
authenticated envelopes.  A cofinal Xi estimate must still control the
full-event values \(y_c\), their phases, the joint normalized-Gram operator,
and the quotient edge norm.  No RCMV104530 or RH conclusion follows.
