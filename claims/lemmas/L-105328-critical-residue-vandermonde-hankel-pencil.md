# L-105328 — The complete critical-residue sign ledger is one Vandermonde–Hankel pencil

Claim ID: `L-105328`  
Status: **PROVED EXACT AT FINITE REGULAR-WINDOW SCOPE; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105214`, `L-105218`, `L-105300`, and the finite-window Hermite trace form on PR #726  
RH status: **not assumed**

## 1. Regular critical window

Let `F` be entire and real on the real axis. Let `Omega` be a bounded,
conjugation-symmetric Jordan domain such that `F'` has no zero on
`partial Omega`. Assume that the zeros

\[
c_1,\ldots,c_M
\]

of `F'` in `Omega` are distinct and are not zeros of `F`. Put

\[
\rho_j={F(c_j)\over F''(c_j)}.
\tag{L-105328.1}
\]

Conjugate critical points and residues occur in conjugate pairs. Define two
real symmetric Hankel matrices, indexed by `0<=r,s<M`, by

\[
\boxed{
\begin{aligned}
\mathsf P_{rs}(F;\Omega)
&=-{1\over2\pi i}\int_{\partial\Omega}
 {F(z)\over F'(z)}z^{r+s}\,dz,\\
\mathsf G_{rs}(F;\Omega)
&={1\over2\pi i}\int_{\partial\Omega}
 {F''(z)\over F'(z)}z^{r+s}\,dz.
\end{aligned}
}
\tag{L-105328.2}
\]

The first matrix is the complete critical-residue trace form. The second is
the unweighted critical-point count form.

## 2. Exact Vandermonde factorization

Let

\[
V_{jr}=c_j^r,
\qquad
D=\operatorname{diag}(-\rho_1,\ldots,-\rho_M).
\]

The residue theorem gives

\[
\boxed{
\mathsf P=V^T D V,
\qquad
\mathsf G=V^T V.
}
\tag{L-105328.3}
\]

Since the critical points are distinct, `V` is invertible. Therefore

\[
\det\mathsf G
=\prod_{1\le i<j\le M}(c_j-c_i)^2\ne0.
\tag{L-105328.4}
\]

Over the real evaluation algebra, every real critical point contributes the
one-dimensional form `[-rho_j]`; every nonreal conjugate pair contributes a
real two-dimensional hyperbolic block. Consequently,

\[
\boxed{
\operatorname{inertia}(\mathsf P)
=(G+C,E+C),
}
\tag{L-105328.5}
\]

where `G` is the number of real negative residues, `E` the number of real
positive residues, and `C` the number of nonreal conjugate critical pairs.

In particular, on the simple noncommon stratum,

\[
\boxed{
\mathsf P\succ0
\quad\Longleftrightarrow\quad
C=0\ \text{and}\ \rho_j<0\ \text{for every }j.
}
\tag{L-105328.6}
\]

Thus one contour-moment positive-definiteness test simultaneously
certifies the pointwise residue sign and excludes the nonreal-critical
correction. By Sylvester's criterion this is equivalent to positivity of the
`M` leading principal determinants of `mathsf P`.

## 3. Exact generalized characteristic polynomial

The entire critical-residue spectrum is the generalized spectrum of the
pencil `(mathsf P,mathsf G)`:

\[
\boxed{
{\det(\mathsf P+t\mathsf G)\over\det\mathsf G}
=\prod_{j=1}^{M}(t-\rho_j).
}
\tag{L-105328.7}
\]

Hence the residue signs can be recovered without locating a critical point.
For a monic polynomial `p` of degree `n`, with squarefree derivative, the
quotient-algebra operator `U_p` of `L-105300` has eigenvalues `rho_j`, and

\[
\boxed{
{\det(\mathsf P+t\mathsf G)\over\det\mathsf G}
=\det(tI-U_p)
={\operatorname{Res}_z(p',tp''-p)
 \over n^2\operatorname{Res}_z(p',p'')}.
}
\tag{L-105328.8}
\]

This identifies the Hermite trace form, the quotient-algebra spectrum and the
Bezoutian residue pivots as three presentations of one finite object.

## 4. Exterior/Vandermonde determinant hierarchy

Put

\[
a_\ell
=-{1\over2\pi i}\int_{\partial\Omega}
 {F(z)\over F'(z)}z^\ell\,dz
=-\sum_j\rho_jc_j^\ell.
\]

For `1<=k<=M`, let

\[
D_k^{\rm crit}(F;\Omega)
=\det[a_{r+s}]_{r,s=0}^{k-1}.
\tag{L-105328.9}
\]

Cauchy–Binet gives the exact atomic expansion

\[
\boxed{
D_k^{\rm crit}
=\sum_{\substack{S\subset\{1,\ldots,M\}\\|S|=k}}
\left(\prod_{j\in S}(-\rho_j)\right)
\prod_{\substack{i<j\\i,j\in S}}(c_j-c_i)^2.
}
\tag{L-105328.10}
\]

Equivalently, Andreief's identity gives the root-free multiple-contour form

\[
\boxed{
D_k^{\rm crit}
={(-1)^k\over k!(2\pi i)^k}
\int_{(\partial\Omega)^k}
\Delta(z_1,\ldots,z_k)^2
\prod_{a=1}^{k}{F(z_a)\over F'(z_a)}\,dz_a.
}
\tag{L-105328.11}
\]

The hierarchy is sharp rather than coherence-like:

```text
D_k^crit > 0 for every 1<=k<=M
    iff
all critical points in the window are real and every residue is negative.
```

The previously frozen five-real-root counterexample to subunit coherence has
all four determinants strictly positive. Thus the complete hierarchy accepts
benign real-rooted functions that the overstrong scalar coherence gate
rejects.

## 5. Exact bridge to the parent Bezoutian split

At the critical packet, the parent Bezoutian matrix is diagonal with entries

\[
-\rho_jF''(c_j)^2.
\]

The matrix `mathsf P` is its interpolation pullback through the invertible
Vandermonde map, with the nonzero curvature factors removed by congruence.
Therefore

\[
\boxed{
\mathsf P\succ0
\quad\Longleftrightarrow\quad
\text{the complete critical block of the Bezoutian is positive definite}.
}
\tag{L-105328.12}
\]

Combined with the exact Schur complement `L-105218`, the only remaining
negative squares then lie in the boundary Cauchy–Loewner remainder.

## 6. Xi specialization

For `F=Xi^(k)` in a regular symmetric rectangle, define `mathsf P_k` and
`mathsf G_k` by (L-105328.2). The finite-window gate

```text
CRVH105330:
  every leading determinant D_j^crit is positive through the complete
  critical count in every window of the canonical exhaustion.
```

is exactly the strict simple/noncommon version of

```text
PRES105220 plus absence of nonreal critical points.
```

It is a finite family of scalar contour determinants at each window. It is
not proved for a fixed low Xi derivative.

## 7. Scope

The theorem assumes simple noncommon critical points. Confluent critical jets
require the already separated multiplicity ledger. The determinant identities
supply no favorable Xi estimate and do not prove cofinal passage. They replace
pointwise unknown critical signs by one exact scalar contour hierarchy; they
do not establish that hierarchy.
