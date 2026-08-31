# 4. Primary Target G — source-admissible infinite observation

## 4.1 Product observation classification

For a prime \(p\), let \(U_p\) be the two-dimensional local source
space spanned by \(A(z)=\sqrt{1-z^2}\) and \(C(z)=\sqrt{1-z}\). The
local bilinear tensor space \(U_p\otimes U_p\) has dimension four.

For a shift \(\beta\ge1\), define the local observation row

\[
K_p[\beta,(i,j)]
=
\sum_{k\ge0}p^{-k}f_{i,k}f_{j,k+\beta},
\qquad i,j\in\{A,C\}.
\tag{G.1}
\]

Let \(B_p\) be a finite shift set and \(K_{p,B_p}\) the matrix with
those rows.

### Theorem G1

For a Cartesian product of shift sets \(B_2\times B_3\times B_5\),
the infinite observation matrix is

\[
\boxed{
R_\infty
=
K_{2,B_2}\otimes K_{3,B_3}\otimes K_{5,B_5}.
}
\tag{G.2}
\]

It is injective on the 64-dimensional tensor space if and only if each
local matrix has rank four. For four shifts at each prime this is
equivalent to

\[
\det K_{p,B_p}\ne0,\qquad p=2,3,5.
\tag{G.3}
\]

For Euclidean singular values,

\[
\sigma_{\min}(R_\infty)
=
\prod_{p=2,3,5}\sigma_{\min}(K_{p,B_p}),
\]

\[
\kappa_2(R_\infty)
=
\prod_{p=2,3,5}\kappa_2(K_{p,B_p}).
\tag{G.4}
\]

Thus the design and conditioning problem for a product observation
reduces exactly to three four-dimensional local problems.

A product observation needs at least four local rows at each prime,
hence at least \(4^3=64\) rows, to recover the full tensor space.
This does not exclude a smaller non-product family on the
20-dimensional curvature subspace.

## 4.2 Explicit lower frame bound

Use the committed shifts \(B_p=\{1,2,3,4\}\). Let

\[
B=483\,723\,248,\qquad
L_3=\frac{39375}{64}.
\]

### Theorem G2

For every integer \(H\ge H_3\) and every \(x\in\mathbb C^{64}\),

\[
\boxed{
\|R_Hx\|_2
\ge
\frac1{16B}\|x\|_2
=
\frac1{7\,739\,571\,968}\|x\|_2.
}
\tag{G.5}
\]

The known physical row scaling is
\(D=\operatorname{diag}(b^{-1/2})\), with
\(30\le b\le810000=900^2\). Therefore

\[
\boxed{
\|DR_Hx\|_2
\ge
\frac1{14400B}\|x\|_2
=
\frac1{6\,965\,614\,771\,200}\|x\|_2.
}
\tag{G.6}
\]

An explicit upper bound is

\[
\|R_Hx\|_2\le125\|x\|_2,\qquad
\|DR_Hx\|_2\le\frac{125}{\sqrt{30}}\|x\|_2.
\tag{G.7}
\]

Hence the 64 physical rows form a uniform finite-horizon frame for all
\(H\ge H_3\), not merely an injective family.

### Proof

From the inverse bound,

\[
\|R_\infty x\|_\infty\ge B^{-1}\|x\|_\infty.
\]

The tail estimate gives

\[
\|R_Hx\|_\infty
\ge
\left(B^{-1}-L_3H^{-1/2}\right)\|x\|_\infty.
\]

The definition of \(H_3\) makes \(L_3H^{-1/2}<1/(2B)\), so

\[
\|R_Hx\|_\infty\ge\frac1{2B}\|x\|_\infty.
\]

Since \(\|x\|_\infty\ge\|x\|_2/8\) and
\(\|R_Hx\|_2\ge\|R_Hx\|_\infty\), (G.5) follows. The smallest physical
row scale is \(1/900\), giving (G.6).

For the upper bound, the source identities give

\[
\sum_d\|v_d\|_1=64.
\]

Every selected denominator has positive exponent at all three primes,
so

\[
\|v_{db}\|_1\le(5/8)^3.
\]

Thus each row has absolute \(\ell^1\)-norm at most

\[
64(5/8)^3=\frac{125}{8}.
\]

The Frobenius norm of a 64-row matrix is therefore at most
\(8(125/8)=125\). Physical scaling decreases it by at least the factor
\(1/\sqrt{30}\). ∎

## 4.3 Source-derived conditioning

Let

\[
W=R_\infty^{-1}
=
K_2^{-1}\otimes K_3^{-1}\otimes K_5^{-1}.
\tag{G.8}
\]

This is an authenticated tensor decoder built from the source rows. It
is an invertible post-observation coordinate change, not a projector
and not a claim that arbitrary tensor coordinates are path-attainable.

For \(H\ge H_3\),

\[
\|WR_H-I\|_\infty
\le
\frac{BL_3}{\sqrt H}<\frac12.
\tag{G.9}
\]

Consequently the conditioned observation has max-norm condition number
at most \(3\).

For a Euclidean condition number, use
\(\|M\|_2\le8\|M\|_\infty\). If

\[
H\ge H_{\mathrm{cond}}
:=
(16BL_3)^2+1
=
22673317603084772006250001,
\tag{G.10}
\]

then

\[
\|WR_H-I\|_2<\frac12.
\]

Hence every singular value of \(WR_H\) lies in \([1/2,3/2]\) and

\[
\boxed{\kappa_2(WR_H)\le3.}
\tag{G.11}
\]

For physical observations, first undo the known diagonal row scaling
and then apply \(W\):

\[
W D^{-1}(D R_H)=W R_H.
\]

This gives a quantitative, source-defined stable recovery theorem.

## 4.4 Representation-theoretic explanation of pure-prime collapse

At one prime, the local source coefficient vectors lie in a
two-dimensional space \(U_i\). The antisymmetric local current produced
by a shift \(\beta\) is

\[
D_{i,\beta}
=
\sum_{k\ge0}q_i^k
\bigl(c_{i,k}\wedge c_{i,k+\beta}\bigr)
\in\Lambda^2U_i.
\tag{G.12}
\]

But

\[
\dim\Lambda^2U_i=1.
\]

Equivalently, \(\Lambda^2U_i\) is the one-dimensional determinant
representation of \(GL(U_i)\). Therefore changing the pure-prime
power \(\beta\) can only change a scalar in this determinant line.

When the other two prime shifts are zero, their local antisymmetric
terms vanish termwise, and the complete curvature row has the form

\[
\Omega_{p_i^\beta}=D_{i,\beta}\,\Xi_i,
\tag{G.13}
\]

where \(\Xi_i\) is independent of \(\beta\). Hence all pure powers of
one prime occupy one representation line. The selected eight
pure-prime rows occupy at most the three lines \(\Xi_2,\Xi_3,\Xi_5\).

This collapse is not a numerical accident. It is forced by the
one-dimensional exterior square of a rank-two local source.

Full-support rows avoid this mechanism by probing a nonzero shift in
every local factor. Their infinite observations live in the full
tensor product of the four-dimensional local bilinear coefficient
spaces; injectivity is then exactly the local rank-four condition of
Theorem G1.

---

# 5. Auxiliary Target H consequence — what the current Epstein certificates already imply

This is not one of the three primary targets, but the current winding
certificate has an immediate analytic consequence.

## 5.1 Simple complex zero and local branch

Each complex rectangle has winding number \(1\) and contains no pole.
The total zero multiplicity in that rectangle is therefore one. The
unique zero \(\rho_*\) is simple:

\[
\partial_s\Lambda(\rho_*;x_*,y_*)\ne0.
\tag{H.1}
\]

The completed Epstein zeta is holomorphic in \(s\) and real-analytic in
the lattice parameters \((x,y)\), \(y>0\). The real-analytic implicit
function theorem therefore gives a unique local zero branch

\[
\rho=\rho(x,y)
\tag{H.2}
\]

through each certified complex zero. This conclusion is non-effective:
the current artifact does not give a numerical neighborhood or a
lower interval for \(|\Lambda_s|\).

For a tangent modulus direction \(v\),

\[
\partial_v\rho
=
-\frac{\partial_v\Lambda}{\partial_s\Lambda}.
\tag{H.3}
\]

For

\[
Q_{x,y}(m,n)=\frac{(m+nx)^2}{y}+n^2y,
\]

the elementary derivatives are

\[
\partial_xQ=\frac{2n(m+nx)}y,\qquad
\partial_yQ=n^2-\frac{(m+nx)^2}{y^2}.
\tag{H.4}
\]

These can be inserted into the existing incomplete-gamma
representation and differentiated with the same tail architecture.

## 5.2 Symmetry-collision lemma

The completed self-dual family satisfies

\[
\Lambda(s;x,y)=\Lambda(1-s;x,y),\qquad
\Lambda(\overline s;x,y)=\overline{\Lambda(s;x,y)}.
\]

An off-line zero \(\rho\) has the partner
\(1-\overline\rho\). Suppose a continuous off-line pair reaches
\(\Re s=1/2\). At the meeting point the two partners coincide.

### Lemma H1

An off-line pair cannot cross the critical line through a simple zero.
Every boundary point where the two symmetry partners coalesce lies in

\[
\boxed{\Lambda=0,\qquad \Lambda_s=0.}
\tag{H.5}
\]

### Proof

If the common zero were simple, the implicit-function theorem would
give a unique nearby zero branch in a small \(s\)-disc. Symmetry would
produce a second nearby branch \(1-\overline\rho\). Off the wall the
two are distinct, contradicting uniqueness. ∎

Thus the actual island boundary is a discriminant wall, not a regular
simple-zero crossing wall.

At a generic wall point with

\[
\Lambda=\Lambda_s=0,\qquad
\Lambda_{ss}\ne0,\qquad
\partial_v\Lambda\ne0,
\]

Weierstrass preparation gives the local square-root law

\[
(s-s_0)^2
=
-\,2\frac{\partial_v\Lambda}{\Lambda_{ss}}
(v-v_0)
+\text{higher terms}.
\tag{H.6}
\]

The ratio in (H.6), not \(-\Lambda_v/\Lambda_s\), determines the
off-line side and crossing direction at the wall.

## 5.3 What remains uncertified

The complex winding certificates qualitatively establish
\(\Lambda_s\ne0\) at their off-line zeros. They do not certify:

* a numerical lower bound for \(|\Lambda_s|\);
* any nonzero modulus derivative;
* continuation from the certified point to a critical-line
  discriminant point;
* \(\Lambda_{ss}\ne0\) and a transverse modulus derivative at that
  discriminant;
* whether the observed islands belong to one connected discriminant
  component.

The real sign-change certificate does not even establish simplicity.

---
