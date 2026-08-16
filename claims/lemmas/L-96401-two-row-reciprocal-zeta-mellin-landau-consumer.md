# L-96401 — Two fixed rows give an exact reciprocal-zeta Mellin--Landau consumer

Claim ID: `L-96401`  
Status: **UNCONDITIONAL EXACT ANALYTIC IMPLICATION**  
Created: 2026-08-17  
Builds on: PR #542's fixed-row transform; exact rows \(2,3\) noncancellation  
RH status: **conditional only on eventual nonnegativity of the two rows**

## 1. Fixed-row transforms

For \(j\ge2\), put
\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}
\]
and
\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
       -C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-96401.1}
\]
For \(\Re s>1/2\), finite Fubini and
\[
 \int_m^\infty\log(X/m)X^{-s-1}\,dX=\frac{m^{-s}}{s^2}
\]
give
\[
 \boxed{
 \int_1^\infty c_X(j)X^{-s-1}\,dX
 =
 \frac{C_j}{s^2}
 +
 \frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
 }
\tag{L-96401.2}
\]
The right side is meromorphic for \(\Re s>0\) and analytic at every positive
real \(s\).  The pole of \(\zeta\) at \(1\) becomes a zero of \(1/\zeta\).

## 2. Exact two-row noncancellation

The two numerators are
\[
 \boxed{P_2(z)=2\,2^{-z}-1-3^{-z}}
\tag{L-96401.3}
\]
and
\[
 \boxed{3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.}
\tag{L-96401.4}
\]
Let
\[
 x=2^{-z},\qquad y=3^{-z}.
\]
If \(P_2(z)=P_3(z)=0\), then
\[
 y=2x-1
\]
and
\[
 0=5y-x-1-3x^2=-3(x-1)(x-2).
\tag{L-96401.5}
\]
When \(\Re z>0\), \(|x|<1\), so neither \(x=1\) nor \(x=2\) is possible.
Therefore
\[
 \boxed{
 P_2(z)\ \text{and}\ P_3(z)
 \text{ have no common zero in }\Re z>0.
 }
\tag{L-96401.6}
\]
This replaces the large-\(j\) asymptotic noncancellation in PR #542 by an
exact two-row statement.

## 3. Landau implication

Assume that both \(c_X(2)\) and \(c_X(3)\) are nonnegative for every
sufficiently large real \(X\).  Subtracting the compact initial interval
changes each Mellin transform by an entire function.

Suppose
\[
 \rho=\beta+i\gamma,\qquad \beta>\frac12,
\]
is a nontrivial zeta zero.  Put \(s_\rho=\rho-\frac12\), so
\(\Re s_\rho>0\).  By (L-96401.6), at least one of
\(P_2(\rho),P_3(\rho)\) is nonzero.  The corresponding transform in
(L-96401.2) therefore has a genuine nonreal pole at \(s_\rho\), with the same
multiplicity as the zero.

For a nonnegative function, Landau's abscissa theorem says that a finite
abscissa of convergence is a singularity on the positive real axis.  But
(L-96401.2) is analytic at every positive real \(s\).  Hence the abscissa
cannot block the nonreal point \(s_\rho\), while holomorphy of the defining
integral to its right cannot contain that pole.  This contradiction excludes
every zero with real part greater than \(1/2\).  The functional equation gives
the other half.

Thus
\[
 \boxed{
 c_X(2)\ge0,\quad c_X(3)\ge0
 \quad\text{eventually}
 \Longrightarrow \mathrm{RH}.
 }
\tag{L-96401.7}
\]

No radix-four endpoint benchmark, prime-square moat, factor-\(67\) recursion,
Target--Lorenz tail, or finite-prime transport is used in this consumer.
