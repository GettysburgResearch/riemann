# L-105646 — Every convex upper-height moment decreases under differentiation

Claim ID: `L-105646`  
Status: **PROVED EXACT FINITE-POLYNOMIAL MAJORIZATION THEOREM**  
Created: 2026-08-25  
Depends on: the root-compression identity underlying `L-105320`; Schur--Horn and Cauchy interlacing, proved in-line at statement-to-use scope  
RH status: **not assumed**

## 1. Statement

Let

\[
p(z)=\prod_{j=1}^{n}(z-\rho_j)
\]

be monic, with arbitrary complex roots counted with multiplicity, and let

\[
c_1,\ldots,c_{n-1}
\]

be the zeros of `p'`, also counted with multiplicity.  Put

\[
y_j=\operatorname{Im}\rho_j,
\qquad
\gamma_k=\operatorname{Im}c_k.
\]

Then for every convex nondecreasing function

\[
\varphi:\mathbb R\to[0,\infty)
\]

one has

\[
\boxed{
\sum_{k=1}^{n-1}\varphi(\gamma_k)
\le
\sum_{j=1}^{n}\varphi(y_j).
}
\tag{L-105646.1}
\]

In particular, for every horizontal level `H` and every real `q>=1`,

\[
\boxed{
\sum_{p'(c)=0}
(\operatorname{Im}c-H)_+^q
\le
\sum_{p(\rho)=0}
(\operatorname{Im}\rho-H)_+^q.
}
\tag{L-105646.2}
\]

Thus every positive upper-height moment is nonincreasing under
differentiation.

## 2. Root compression

Let

\[
D=\operatorname{diag}(\rho_1,\ldots,\rho_n),
\qquad
e={1\over\sqrt n}(1,\ldots,1)^T,
\]

and let `P=I-ee^*`.  On `e^perp`, define

\[
C=PDP|_{e^\perp}.
\]

The matrix determinant lemma, or the resolvent identity

\[
e^*(zI-D)^{-1}e={1\over n}{p'(z)\over p(z)},
\]

gives

\[
\boxed{
\det(zI_{e^\perp}-C)={p'(z)\over n}.
}
\tag{L-105646.3}
\]

Hence the eigenvalues of `C` are exactly the critical points `c_k`.

## 3. Imaginary-part Schur majorization

Let

\[
Y={D-D^*\over2i}
=\operatorname{diag}(y_1,\ldots,y_n).
\]

The Hermitian imaginary part of `C` is

\[
\boxed{
\operatorname{Im}C
={C-C^*\over2i}
=PYP|_{e^\perp}.
}
\tag{L-105646.4}
\]

Take a unitary Schur decomposition

\[
Q^*CQ=T,
\]

where `T` is upper triangular with diagonal `c_1,...,c_(n-1)`.  Then

\[
Q^*(\operatorname{Im}C)Q
={T-T^*\over2i}
\]

is Hermitian and has diagonal

\[
(\gamma_1,\ldots,\gamma_{n-1}).
\]

If

\[
\mu_1\ge\cdots\ge\mu_{n-1}
\]

are the eigenvalues of `Im C`, the finite-dimensional Schur--Horn theorem says
that the diagonal vector is majorized by the eigenvalue vector.  Equivalently,
for every convex `varphi`,

\[
\boxed{
\sum_{k=1}^{n-1}\varphi(\gamma_k)
\le
\sum_{k=1}^{n-1}\varphi(\mu_k).
}
\tag{L-105646.5}
\]

For completeness, the only consequence used here follows by expressing the
diagonal as `S mu`, where

\[
S_{jk}=|Q_{kj}|^2
\]

is doubly stochastic, and applying Jensen row by row.

## 4. Compression interlacing

Reorder the root heights so that

\[
y_1\ge\cdots\ge y_n.
\]

Since `Im C` is a codimension-one compression of the Hermitian diagonal matrix
`Y`, the min--max principle gives Cauchy interlacing:

\[
\boxed{
y_j\ge\mu_j\ge y_{j+1}
\qquad(1\le j<n).}
\tag{L-105646.6}
\]

Because `varphi` is nondecreasing and nonnegative,

\[
\sum_{j=1}^{n-1}\varphi(\mu_j)
\le
\sum_{j=1}^{n-1}\varphi(y_j)
\le
\sum_{j=1}^{n}\varphi(y_j).
\tag{L-105646.7}
\]

Combining (L-105646.5)--(L-105646.7) proves (L-105646.1).

## 5. Concrete consequences

Taking

\[
\varphi(t)=(t-H)_+^q
\]

proves (L-105646.2).  At `q=1`,

\[
\boxed{
\sum_{p'(c)=0}(\operatorname{Im}c-H)_+
\le
\sum_{p(\rho)=0}(\operatorname{Im}\rho-H)_+.
}
\tag{L-105646.8}
\]

Taking `varphi(t)=exp(lambda(t-H))`, `lambda>0`, gives

\[
\boxed{
\sum_{p'(c)=0}e^{\lambda(\operatorname{Im}c-H)}
\le
\sum_{p(\rho)=0}e^{\lambda(\operatorname{Im}\rho-H)}.
}
\tag{L-105646.9}
\]

Letting `q` tend to infinity in the finite set recovers

\[
\max_k\operatorname{Im}c_k
\le
\max_j\operatorname{Im}\rho_j,
\]

the horizontal Gauss--Lucas height inequality, but (L-105646.2) is strictly
stronger: it controls the complete penetration distribution, not only the top
zero.

## 6. Xi-packet interpretation

For every finite symmetric canonical-product packet approximating Xi on a
regular rectangle, (L-105646.2) applies exactly.  At `q=1`, the aggregate depth
of derivative zeros above a moving horizontal line is paid by the aggregate
depth of parent zeros above that line.

Combining with the simple-factor current charge bound of `L-105641`, one gets
for total analytic height `H_a=b+h` and boundary level `H_0`:

\[
\boxed{
\sum_{p'(c)=0}
\mathfrak q_{b,h}
\bigl((\operatorname{Im}c-H_0)_+\bigr)
\le
{2h\over H_a^2}
\sum_{p(\rho)=0}
(\operatorname{Im}\rho-H_0)_+,
}
\tag{L-105646.10}
\]

where

\[
\mathfrak q_{b,h}(d)
=2d\int_0^\infty r_{b,h}(\xi)e^{-2d\xi}d\xi
\le {2h\over H_a^2}d.
\]

This is an exact finite-packet parent-to-derivative source budget.

## 7. Scope

Passage from finite canonical packets to a cofinal Xi rectangle must retain
horizontal endpoints, omitted zeros and the canonical exponential factor.  The
theorem does not control the **number** of arbitrarily shallow derivative
zeros, does not compare nonorthogonal model-space traces by scalar addition,
and does not prove the pointwise microscope sign.  It supplies a new
unconditional Lyapunov family for the microscopic collar.  RH remains
unproved.
