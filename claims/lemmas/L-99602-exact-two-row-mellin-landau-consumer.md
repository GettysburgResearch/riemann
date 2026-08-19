# L-99602 — Two exact rows give a complete noncancellation and Mellin--Landau consumer

Claim ID: `L-99602`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: nonnegativity, or a nonnegative witness modulo Mellin-holomorphic
error, for rows `2` and `3`  
RH status: **not assumed**

## 1. Fixed-row transforms

For

\[
c_X(j)=\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
\]

finite Fubini in the initial half-plane gives

\[
\mathcal C_j(s)
=
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+1/2)}
{s^2\zeta(s+1/2)}.
\tag{L-99602.1}
\]

The right side is meromorphic in `Re(s)>0` and analytic at every positive real
point.

For `j=2,3`, put \(z=s+1/2\). The numerators are

\[
P_2(z)=2\,2^{-z}-1-3^{-z},
\tag{L-99602.2}
\]

\[
3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.
\tag{L-99602.3}
\]

## 2. Exact common-zero elimination

Put

\[
a=2^{-z},\qquad b=3^{-z}.
\]

If \(P_2(z)=0\), then

\[
b=2a-1.
\]

Substitution in (L-99602.3) gives exactly

\[
\boxed{
3P_3(z)=-3(a-1)(a-2).
}
\tag{L-99602.4}
\]

When `Re(z)>0`,

\[
|a|=2^{-\Re z}<1,
\]

so \(a\ne1,2\). Hence

\[
\boxed{
P_2(z)\ \text{and}\ P_3(z)
\ \text{have no common zero in }\Re z>0.
}
\tag{L-99602.5}
\]

No large-row limit or Euler--Maclaurin remainder is needed.

## 3. Exact-positive-row version

Assume

\[
c_X(2)\ge0,\qquad c_X(3)\ge0.
\]

Each row has finite Mellin abscissa. If a zeta zero \(\rho\) satisfies
\(\Re\rho>1/2\), at least one numerator in (L-99602.2)--(L-99602.3) is nonzero.
The corresponding meromorphic continuation has a pole at

\[
s=\rho-\frac12,\qquad\Re s>0.
\]

If the defining nonnegative Mellin integral did not converge throughout
`Re(s)>0`, Landau forces a singularity at its positive real abscissa. But
(L-99602.1) is analytic at every positive real point. This contradiction
excludes the zero. Functional-equation symmetry gives RH.

## 4. Holomorphic-defect version

It is enough to construct, for `j=2,3`,

\[
c_X(j)=D_X(j)+E_X(j),
\qquad D_X(j)\ge0,
\tag{L-99602.6}
\]

where

\[
\int_1^\infty E_X(j)X^{-s-1}\,dX
\]

is holomorphic in `Re(s)>0`. The pole of the full row survives in the Mellin
transform of \(D_X(j)\), and the same Landau argument applies.

Thus the analytic conclusion-facing interface is completely closed once the
two arithmetic witnesses are supplied.

## 5. Consequence

The candidate no longer needs the large-\(j\) asymptotic

\[
P_j(z)\sim-\frac{z(z+1)}{1-z}j^{-z-1}.
\]

That asymptotic remains useful as redundancy, but it is removed from the
minimal proof graph.
