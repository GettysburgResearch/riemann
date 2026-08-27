# L-105651 — Critical points plus the centroid are directionally majorized by the roots

Claim ID: `L-105651`  
Status: **PROVED EXACT FOR FINITE POLYNOMIALS**  
Created: 2026-08-25  
Depends on: `L-105320`, `L-105646`; Schur--Horn and Hermitian pinching  
RH status: **not assumed**

## 1. Statement

Let `p` be a monic polynomial of degree `n>=2`, with zeros

\[
z_1,\ldots,z_n
\]

and critical points

\[
c_1,\ldots,c_{n-1},
\]

all counted with multiplicity.  Put

\[
\overline z={1\over n}\sum_{j=1}^n z_j.
\]

For a direction `theta`, define the real projection

\[
\pi_\theta(z)=\operatorname{Re}(e^{-i\theta}z).
\]

Then the `n`-vector

\[
\boxed{
\bigl(
\pi_\theta(c_1),\ldots,\pi_\theta(c_{n-1}),
\pi_\theta(\overline z)
\bigr)
}
\]

is majorized by

\[
\boxed{
\bigl(
\pi_\theta(z_1),\ldots,\pi_\theta(z_n)
\bigr).
}
\tag{L-105651.1}

Equivalently, for every convex function

\[
\varphi:\mathbb R\to\mathbb R
\]

for which the finite sums are defined,

\[
\boxed{
\sum_{k=1}^{n-1}\varphi(\pi_\theta(c_k))
+
\varphi(\pi_\theta(\overline z))
\le
\sum_{j=1}^{n}\varphi(\pi_\theta(z_j)).
}
\tag{L-105651.2}

No monotonicity assumption on `varphi` is required.

## 2. Compression proof

Let

\[
D=\operatorname{diag}(z_1,\ldots,z_n),
\qquad
e=n^{-1/2}(1,\ldots,1)^T.
\]

In the orthogonal decomposition

\[
\mathbb C^n=\mathbb Ce\oplus e^\perp,
\]

write

\[
D=
\begin{pmatrix}
\overline z & *\\
* & C
\end{pmatrix}.
\]

The root-compression identity of `L-105320` is

\[
\boxed{
\det(wI-C)={p'(w)\over n}.
}
\tag{L-105651.3}

Thus the eigenvalues of `C` are precisely `c_1,...,c_(n-1)`.

Fix `theta` and take the Hermitian directional part

\[
H=\operatorname{Re}(e^{-i\theta}D).
\]

Pinching `H` to the two blocks gives

\[
H_0=
\pi_\theta(\overline z)
\oplus
\operatorname{Re}(e^{-i\theta}C).
\]

Hermitian pinching is a unital trace-preserving positive map, so

\[
\lambda(H_0)\prec\lambda(H).
\tag{L-105651.4}

The eigenvalues of `H` are the projected root coordinates
`pi_theta(z_j)`.

Now take a Schur basis for `C`.  The diagonal of

\[
\operatorname{Re}(e^{-i\theta}C)
\]

in that basis is

\[
\pi_\theta(c_1),\ldots,\pi_\theta(c_{n-1}).
\]

Schur--Horn therefore gives

\[
\bigl(
\pi_\theta(\overline z),
\pi_\theta(c_1),\ldots,\pi_\theta(c_{n-1})
\bigr)
\prec\lambda(H_0).
\tag{L-105651.5}

Transitivity of majorization proves (L-105651.1), and Karamata proves
(L-105651.2).

## 3. Complete height-moment hierarchy

Take `theta=pi/2`, so that `pi_theta(z)=Im z`.  For every `H in R` and every
`q>=1`, the function

\[
\varphi_{H,q}(t)=(t-H)_+^q
\]

is convex.  Therefore

\[
\boxed{
\sum_{k=1}^{n-1}
(\operatorname{Im}c_k-H)_+^q
+
(\operatorname{Im}\overline z-H)_+^q
\le
\sum_{j=1}^{n}
(\operatorname{Im}z_j-H)_+^q.
}
\tag{L-105651.6}

For a real polynomial, `Im overline z=0`.  At every `H>=0`, the centroid term
vanishes and one recovers, now as part of a full convex hierarchy,

\[
\boxed{
\sum_k(\operatorname{Im}c_k-H)_+^q
\le
\sum_j(\operatorname{Im}z_j-H)_+^q.
}
\tag{L-105651.7}

This strengthens the earlier upper-height moment theorem from one chosen
family of convex increasing functions to **every convex directional test**.

## 4. Jessen absolute-distance inequality

For a real polynomial, choose

\[
\varphi_H(t)=|t-H|.
\]

Equation (L-105651.2) gives

\[
\boxed{
\sum_{j=1}^{n}|\operatorname{Im}z_j-H|
-
\sum_{k=1}^{n-1}|\operatorname{Im}c_k-H|
\ge |H|.
}
\tag{L-105651.8}

For `H>=0`, zero total imaginary sum rewrites the excess as

\[
\boxed{
\begin{aligned}
&\sum_j|\operatorname{Im}z_j-H|
-
\sum_k|\operatorname{Im}c_k-H|-H\\
&\qquad=
2\left[
\sum_j(\operatorname{Im}z_j-H)_+
-
\sum_k(\operatorname{Im}c_k-H)_+
\right]
\ge0.
\end{aligned}
}
\tag{L-105651.9}

The left side is the finite-polynomial horizontal logarithmic-potential
excess after removing the unavoidable one-degree carrier.  Thus the balanced
parent/derivative Jessen mean is unconditionally favorable at every height.

## 5. Relation to the adaptive logarithmic index

`L-105647` regularizes the signed all-pass index by sampling logarithmic modulus
on an interior horizontal line.  Equation (L-105651.8) proves that, after the
one-degree carrier is retained, the **parent-minus-derivative horizontal log
mean is already nonnegative for every finite polynomial packet**.

This is an integrated physical sign unavailable from the source-energy theorem
alone.  It does not imply the pointwise Turan quotient sign: horizontal
averaging can hide localized phase slips, exactly as the pointwise separator
`R-105630` warns.

## 6. Scope

The theorem is finite-dimensional and exact.  Cofinal passage to Xi requires
canonical-product regularization and the horizontal endpoint ledger.  Convex
majorization is one-way: a real-rooted high derivative does not force its
parent to be real-rooted.  The theorem proves a complete family of integrated
height inequalities, not `POINTID105630`, `D0PHASE105650`, or RH.
