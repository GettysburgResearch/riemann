# L-105653 — Critical points plus the centroid are doubly stochastic barycenters of the roots

Claim ID: `L-105653`  
Status: **PROVED EXACT FOR FINITE POLYNOMIALS**  
Created: 2026-08-25  
Depends on: `L-105320`, `L-105651`; Schur triangularization  
RH status: **not assumed**

## 1. Exact barycentric coupling

Let `p` be monic of degree `n>=2`, with roots

\[
z_1,\ldots,z_n
\]

and critical points

\[
c_1,\ldots,c_{n-1},
\]

counted with multiplicity.  Put

\[
\overline z={1\over n}\sum_{j=1}^n z_j,
\qquad
D=\operatorname{diag}(z_1,\ldots,z_n),
\qquad
e=n^{-1/2}(1,\ldots,1)^T.
\]

Choose an isometry

\[
Q:\mathbb C^{n-1}\longrightarrow e^\perp\subset\mathbb C^n
\]

such that the compression

\[
Q^*DQ
\]

is upper triangular.  This is possible by taking a Schur basis of the root
compression.  `L-105320` gives

\[
\det(wI-Q^*DQ)={p'(w)\over n},
\]

so the diagonal entries of `Q^*DQ` are the critical points `c_k`.

For `1<=k<=n-1` and `1<=j<=n`, define

\[
\boxed{s_{kj}=|Q_{jk}|^2.}
\tag{L-105653.1}

Then

\[
\boxed{
c_k=\sum_{j=1}^n s_{kj}z_j.}
\tag{L-105653.2}

Each row sums to one because every column of `Q` is a unit vector:

\[
\sum_j s_{kj}=1.
\]

The column sums satisfy

\[
\sum_{k=1}^{n-1}s_{kj}
=(QQ^*)_{jj}
=(I-ee^*)_{jj}
=1-{1\over n}.
\tag{L-105653.3}

Append the final row

\[
\boxed{s_{nj}={1\over n}.}
\tag{L-105653.4}

The resulting `n by n` matrix `S=(s_(kj))` is doubly stochastic and

\[
\boxed{
\begin{pmatrix}
c_1\\
\vdots\\
c_{n-1}\\
\overline z
\end{pmatrix}
=
S
\begin{pmatrix}
z_1\\
\vdots\\z_n
\end{pmatrix}.
}
\tag{L-105653.5}

This is a literal complex barycentric coupling, not only a family of projected
majorization inequalities.

## 2. Every convex planar observable decreases

Identify `C` with `R^2`.  Let

\[
\Psi:\mathbb C\longrightarrow\mathbb R
\]

be convex.  Applying Jensen to each row of `S`, then using the column sums,
gives

\[
\boxed{
\sum_{k=1}^{n-1}\Psi(c_k)
+
\Psi(\overline z)
\le
\sum_{j=1}^n\Psi(z_j).
}
\tag{L-105653.6}

Thus the critical divisor plus one centroid atom is below the parent divisor
in complex convex order.

`L-105651` follows by taking

\[
\Psi(z)=\varphi(\operatorname{Re}(e^{-i\theta}z)).
\]

The present theorem is strictly stronger because the test need not factor
through one real projection.

## 3. Radial and disk-escape hierarchies

For every center `w in C` and every `q>=1`, the function

\[
\Psi_{w,q}(z)=|z-w|^q
\]

is convex.  Hence

\[
\boxed{
\sum_{k=1}^{n-1}|c_k-w|^q
+|\overline z-w|^q
\le
\sum_{j=1}^n|z_j-w|^q.
}
\tag{L-105653.7}

More generally, for `R>=0`,

\[
\Psi_{w,R,q}(z)=(|z-w|-R)_+^q
\]

is convex because `t -> (t-R)_+^q` is convex and nondecreasing on
`[0,infinity)`.  Therefore

\[
\boxed{
\begin{aligned}
&\sum_{k=1}^{n-1}(|c_k-w|-R)_+^q
+(|\overline z-w|-R)_+^q\\
&\qquad\le
\sum_{j=1}^n(|z_j-w|-R)_+^q.
\end{aligned}
}
\tag{L-105653.8}

Every convex disk-escape moment decreases under differentiation after the
centroid atom is retained.

## 4. Equality and concentration

Equality in (L-105653.6) for a strictly convex `Psi` forces every row of `S`
with nontrivial support to be concentrated on parent roots at a common point.
Consequently broad parent-root dispersion creates a strict convex-order loss,
whereas multiple roots and degenerate clusters are represented without a
separation assumption.

No claim is made that a small convex-order loss forces real-rootedness.  A
conjugate pair can approach the real axis while retaining its full integer
multiplicity and arbitrarily small radial or vertical escape moment.

## 5. Xi relevance

Applied to finite real canonical-product packets of the Xi derivative ladder,
(L-105653.8) simultaneously controls:

```text
upper-height penetration;
lower-height penetration;
Jensen-disk escape;
off-center complex windows;
all q-th convex distance moments.
```

This unifies the earlier height-majorization, Jensen-disk attraction and
critical-residue compression coordinates.  It supplies an exact geometric
consumer for a reviewed fixed-width terminal derivative theorem, with only the
cofinal packet and endpoint ledger left before entire-function use.

## 6. Scope

The theorem is finite-dimensional.  The existence of the doubly stochastic
coupling does not reverse differentiation, does not control nonconvex
indicators or clipped degree, and does not identify the degree-zero all-pass
phase energy.  Cofinal Xi passage, pointwise phase localization and RH remain
open.
