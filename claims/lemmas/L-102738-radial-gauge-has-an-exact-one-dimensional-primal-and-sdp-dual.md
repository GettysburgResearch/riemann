# L-102738 — The centered radial gauge has an exact one-dimensional primal and compact SDP dual

Claim ID: `L-102738`  
Status: **PROVED EXACT CONVEX-ALGEBRA THEOREM**  
Created: 2026-08-22  
Depends on: `L-102731`, `L-102733`  
RH status: **not assumed**

Retain the centered filtered-disk coordinates

\[
P(w)=C+2B\,\Re w+A|w|^2,
\qquad |w|\le\frac12,
\]

and the radial cost of `L-102733`,

\[
\mathfrak R(A,B,C)
=
\inf_{\lambda,\eta\ge0}
\left[
\frac{255}{64}\lambda+rac1{16}(C+\eta)
\right],
\tag{L-102738.1}
\]

subject to

\[
\begin{pmatrix}
A+\lambda&B\\
B&C+\eta-\lambda/4
\end{pmatrix}\succeq0.
\tag{L-102738.2}
\]

## 1. Exact one-dimensional primal

Put

\[
x=A+\lambda,
\qquad
y=C+\eta-\lambda/4.
\]

Then the constraints are

\[
x\ge\max\{A,0\},
\qquad
y\ge0,
\qquad xy\ge B^2,
\]

and

\[
y\ge C+\frac{A-x}{4}.
\]

The objective simplifies exactly because

\[
\frac{255}{64}+\frac1{64}=4:
\]

\[
\frac{255}{64}(x-A)+\frac1{16}
\left[y+\frac{x-A}{4}\right]
=
4(x-A)+\frac y{16}.
\]

Consequently

\[
\boxed{
\mathfrak R(A,B,C)
=
\inf_{x\ge\max\{A,0\}}
\left\{
4(x-A)
+
\frac1{16}
\max\left(
\frac{B^2}{x},
C+\frac{A-x}{4},
0
\right)
\right\}.
}
\tag{L-102738.3}
\]

At `x=0`, the term `B^2/x` is interpreted as `0` when `B=0` and `+infinity`
otherwise.

Thus the matrix optimization in the conclusion-facing gauge is one real
convex minimization.  No hidden row, reserve, or matrix variable remains.

## 2. Exact compact dual

Let

\[
Z=
\begin{pmatrix}u&v\\v&w\end{pmatrix}\succeq0.
\]

Lagrange duality gives

\[
\boxed{
\mathfrak R(A,B,C)
=
\sup
\left\{
-uA-2vB+\left(\frac1{16}-w\right)C
\right\},
}
\tag{L-102738.4
\]

where the supremum is over

\[
0\le w\le\frac1{16},
\qquad
0\le u\le\frac{255}{64}+\frac w4,
\qquad
v^2\le uw.
\tag{L-102738.5}
\]

The equality is strong: a strictly feasible primal point is obtained by taking
`lambda` and `eta` sufficiently large.

The dual set is compact.  Hence `mathfrak R` is a supremum of a fixed compact
family of linear source functionals.  This is the precise form needed for
source partitions and logarithmic integration.

## 3. Rank-one ray interpretation

For a rank-one dual matrix

\[
Z=(a,b)^{\mathsf T}(a,b),
\]

put `theta=b^2` and, when `b` is nonzero, `t=a/b`.  Then

\[
-uA-2vB+\left(\frac1{16}-w\right)C
=
\frac C{16}-\theta P(t).
\tag{L-102738.6}
\]

The admissibility conditions become

\[
0\le\theta\le\frac1{16},
\qquad
\theta\left(t^2-\frac14\right)\le\frac{255}{64}.
\tag{L-102738.7}
\]

Thus the centered radial gauge is an exact extrapolation envelope for the
filtered SHARP polynomial: it prices how far the disk-positive polynomial can
fall along a compact family of outer rays.

The distinguished extreme ray is identified in `L-102739`.