# L-25603 — Rank-one meromorphic charge and the fixed-ratio anchor

Claim ID: `L-25603`  
Title: After all reciprocal-free finite-depth differences are removed, the balanced inverse hierarchy has one meromorphic charge per reflected side, represented by any fixed-ratio Mertens shell  
Status: **PROPOSED EXACT REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: `L-23007`, `L-23008`, `L-23401`; `L-25601`  
Scope: analytic charge rank and scalar anchor; no norm estimate

## 1. Finite inverse hierarchy

For a standard finite inverse put

\[
E_{K,V}(s)={R_V(s)^K\over\zeta(s)}.
\tag{L-25603.1}
\]

At every nontrivial zero `rho`, `L-23007` proves

\[
\operatorname{PP}_{\rho}E_{K,V}
=
\operatorname{PP}_{\rho}{1\over\zeta}.
\tag{L-25603.2}
\]

For finitely many pairs `(K_j,V_j)` and coefficients `c_j`,

\[
\boxed{
\operatorname{PP}_{\rho}
\left(\sum_jc_jE_{K_j,V_j}\right)
=\left(\sum_jc_j\right)
\operatorname{PP}_{\rho}{1\over\zeta}.}
\tag{L-25603.3}
\]

Thus every finite cross-order difference with `sum c_j=0` is reciprocal-free,
while every combination with nonzero total coefficient retains the same
meromorphic charge.

## 2. One-dimensional quotient

Let `P` be the finite linear span of the residuals `E_(K,V)` under
consideration, and let `H` be the subspace whose elements are holomorphic at
every nontrivial zero. The map

\[
\chi:\mathcal P\longrightarrow\mathbb C,
\qquad
\chi\left(\sum_jc_jE_{K_j,V_j}\right)=\sum_jc_j
\tag{L-25603.4}
\]

has kernel `P intersect H`. Therefore

\[
\boxed{
\dim\mathcal P/(\mathcal P\cap\mathcal H)=1.}
\tag{L-25603.5}
\]

The finite inverse hierarchy has exactly one nontrivial meromorphic quotient
class. The matrix depth lift `L-25601` gives a concrete finite representative
of all reciprocal-free depth differences and one anchor column for this class.

## 3. Reflected quotient rank

Apply the construction independently to the `+` and `-` reflected sides. The
meromorphic quotient of the double hierarchy is the tensor product of two
one-dimensional quotient classes. Hence the complete top reflected charge has

\[
\boxed{
\text{analytic quotient rank }1.}
\tag{L-25603.6}
\]

Every other depth-color combination is reciprocal-free in at least one leg and
belongs to the finite complete-lattice/error grammar.

This is a genuine bounded-charge theorem at the level of analytic quotient
rank.

## 4. Physical representative: a fixed-ratio Möbius shell

For fixed `0<c<1`, define

\[
Q_c(t)=e^{-t/2}\bigl[M(e^t)-M(ce^t)\bigr].
\tag{L-25603.7}
\]

Its Laplace transform is

\[
\boxed{
\widehat Q_c(z)
={1-c^{z+1/2}\over
 (z+1/2)\zeta(z+1/2)}.}
\tag{L-25603.8}
\]

The numerator is nonzero at every hypothetical zero with real part greater
than `1/2`. Thus `Q_c` is a physical representative of the unique meromorphic
charge.

Moreover, `L-23008` gives mutually inverse causal `ell^1` filters between every
two fixed ratios. Therefore all `Q_c` have the same cumulative-energy and
Hardy exponents. One may choose the dyadic shell `c=1/2` or the first Farey-cell
ratio `c=2/3` without changing the obstruction.

## 5. Why quotient rank one is not an exponent `1/K`

The anchor `Q_c` is one scalar coordinate, but its coefficient support at block
`J` occupies the full shell

\[
ce^J<n\le e^J.
\]

Its multiplicative range is of scale `X=e^J`, not `V=e^(J/K)`. Hence the
following inference is false:

```text
one meromorphic charge
=> one V-sized paid coordinate
=> energy exponent 1/K.
```

The correct conclusion is only

```text
all reciprocal-free depth directions are bookkeeping/complete-lattice terms;
one full-scale fixed-ratio Möbius anchor remains.
```

A bound

\[
\int_J^{J+B}|Q_c(t)|^2dt=e^{o(J)}
\tag{L-25603.9}
\]

for one fixed `B>0` is exactly the source-specific coercivity theorem still
needed. By `L-23401` and its transfer theorem, it is RH-bearing.

## 6. Corrected charge ledger

The top reflected packet may therefore be compressed to:

1. a finite reciprocal-free depth/incidence ledger;
2. complete-lattice rows closed by Euler/contour shift;
3. strict lower-scale rows;
4. one full-scale scalar anchor `Q_c` and its reflected normal Gram.

This is stronger and more precise than counting all divisor coordinates. It
also proves that no bounded face vocabulary can finish the proof unless it
supplies a genuine estimate for the scalar anchor.

## 7. Proof boundary

Closed exactly here:

- one-dimensionality of the finite meromorphic quotient;
- rank-one reflected quotient;
- exact fixed-ratio physical representative;
- equivalence of all fixed ratios;
- the distinction between analytic rank and logarithmic support scale.

Open:

- subexponential anchor energy;
- `BTP(K)`/`RBC(K)` in its arithmetic sense;
- RH.
