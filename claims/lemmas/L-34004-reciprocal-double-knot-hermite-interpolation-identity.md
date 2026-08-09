# L-34004 — Reciprocal double-knot identity and Hermite interpolation bridge

Claim ID: `L-34004`

Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34001`, `L-34003`; elementary confluent divided differences

Scope: exact algebraic identification of the Brownian Dirichlet-mean factor with a reciprocal Hermite divided difference; no zero-free conclusion and no RH claim

## 1. General reciprocal confluent identity

Let `b_1,...,b_N` be distinct positive numbers and put

\[
a_i=b_i^{-1}.
\]

For a function `f`, write

\[
[a_1,a_1,\ldots,a_N,a_N]f
\]

for the confluent divided difference with each node repeated twice.  For every complex `z`,

\[
\boxed{
[a_1,a_1,\ldots,a_N,a_N]x^{z+2N-1}
=-\Bigl(\prod_{j=1}^N b_j^2\Bigr)
[b_1,b_1,\ldots,b_N,b_N]x^{-z-1}.
}
\tag{L-34004.1}
\]

### Proof

The repeated-knot residue formula gives

\[
\begin{aligned}
&[a_1,a_1,\ldots,a_N,a_N]x^{z+2N-1}\\
&=\sum_i
\frac{a_i^{z+2N-2}}
{\prod_{j\ne i}(a_i-a_j)^2}
\left[z+2N-1-2a_i\sum_{j\ne i}\frac1{a_i-a_j}\right].
\end{aligned}
\tag{L-34004.2}
\]

Since `a_i=1/b_i`,

\[
\frac{a_i^{z+2N-2}}
{\prod_{j\ne i}(a_i-a_j)^2}
=\Bigl(\prod_jb_j^2\Bigr)
\frac{b_i^{-z-2}}
{\prod_{j\ne i}(b_i-b_j)^2},
\tag{L-34004.3}
\]

and

\[
z+2N-1-2a_i\sum_{j\ne i}\frac1{a_i-a_j}
=z+1+2b_i\sum_{j\ne i}\frac1{b_i-b_j}.
\tag{L-34004.4}
\]

But the bracket in the repeated-knot formula for
`[b_1,b_1,...,b_N,b_N]x^(-z-1)` is

\[
-z-1-2b_i\sum_{j\ne i}\frac1{b_i-b_j},
\]

which is the negative of (L-34004.4).  Summing proves (L-34004.1).

The argument is an identity of meromorphic functions in `z`, hence extends through removable exceptional values.

## 2. Brownian reciprocal-square knots

For PR #343,

\[
a_i=i^{-2},\qquad b_i=i^2.
\]

Thus

\[
\boxed{
[1,1,1/4,1/4,\ldots,N^{-2},N^{-2}]x^{z+2N-1}
=-(N!)^4
[1,1,4,4,\ldots,N^2,N^2]x^{-z-1}.
}
\tag{L-34004.5}
\]

Combined with `L-34003`, the zero-bearing Brownian factor is therefore exactly a **Hermite/confluent interpolation functional at the squared equidistant nodes**

\[
1^2,2^2,\ldots,N^2.
\]

No probability approximation is needed for this identification.

## 3. Symmetric Hermite interpretation

Writing `u=y^2`, a repeated interpolation node `u=i^2` is equivalent to prescribing the value and first `u`-derivative, or equivalently the even Hermite data at the symmetric nodes `y=\pm i` after the usual even-variable reduction.

Therefore the PR #343 Dirichlet-average Mellin factor belongs to the same confluent squared-equidistant interpolation geometry used in the Hermite (`k=2`) zeta-interpolation literature.

This is an exact structural correspondence, not an assertion that a published asymptotic theorem has the same normalization or proves the desired half-plane stability.

## 4. Relation to the explicit numerator

Applying the repeated-knot formula on the right side of (L-34004.5), then differentiating the gamma interpolation of the squared-equidistant barycentric weights, recovers `L-34003`:

\[
H_N(z)
=\sum_{i=1}^N C_{N,i}i^{-2z}(z+\alpha_{N,i})
=-\frac12\sum_{i=1}^N
\left(C_N(x)x^{1-2z}\right)'_{x=i}.
\]

Thus the gamma-derivative formula and the Hermite reciprocal identity are two coordinates for the same finite object.

## 5. Literature bridge and normalization firewall

Ganzburg's Hermite interpolation framework treats multiplicity-two interpolation at symmetric real nodes and develops zeta asymptotics for polynomial families with equidistant zeros.  The present identity shows that the Brownian factor is naturally in that interpolation category after reciprocal transformation.

However, the affine relation between the Brownian Mellin exponent `z`, the reciprocal power `-z-1`, and the zeta parameter in a chosen Hermite normalization must be checked explicitly before importing any zero statement.  In particular, asymptotic convergence of interpolation errors to a zeta factor does **not** by itself imply that the finite interpolation errors are zero-free in the required half-plane.

This firewall is part of the theorem: `L-34004` supplies an exact algebraic bridge, not a black-box proof of raw Brownian stability.

## 6. New proof-facing target

The raw Brownian stability theorem may now be attacked equivalently in any of three exact coordinates:

1. the probability form `M_N(z)=E[Q_N^z]`;
2. the exponential numerator `H_N(z)` of `L-34003`;
3. the reciprocal Hermite divided difference
   \[
   [1^2,1^2,\ldots,N^2,N^2]x^{-z-1}.
   \]

The third coordinate makes available Hermite interpolation, Peano-kernel, and squared-equidistant-node techniques without changing the finite zero problem.

## 7. Proof boundary

Closed exactly:

1. the reciprocal confluent divided-difference identity;
2. specialization to reciprocal-square/squared-equidistant nodes;
3. equivalence with an even Hermite interpolation functional;
4. consistency with the explicit numerator of `L-34003`.

Open:

1. a cofinal zero-free theorem in `Re z>1/4`;
2. raw Brownian stability;
3. RH.
