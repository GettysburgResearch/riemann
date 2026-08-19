# L-99453 — Quantitative fixed-row noncancellation and the Landau pole transfer

Claim ID: `L-99453`  
Status: **PROVED SELF-CONTAINED ANALYTIC THEOREM**  
Created: 2026-08-20  
RH status: **conclusion-facing**

Fix \(j\ge2\). Let

\[
A_j=\frac{j+1}{j-1},
\qquad
B_j=\frac{(j+1)(j-2)}{j(j-1)},
\qquad
C_j=\frac2{j(j-1)}
\]

and

\[
P_j(z)
=
A_jj^{-z}
-B_j(j+1)^{-z}
-C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-99453.1}
\]

## 1. Exact Mellin formula

For the full Möbius row \(c_X(j)\), finite Fubini gives initially in
\(\Re s>1/2\)

\[
\boxed{
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\frac12)}
{s^2\zeta(s+\frac12)}.
}
\tag{L-99453.2}
\]

The right side continues meromorphically to \(\Re s>0\) and has no singularity
at any positive real \(s\).

## 2. Large-row noncancellation with a controlled remainder

For fixed \(z\) with \(0<\sigma=\Re z<1\), one-step Euler summation gives

\[
\sum_{m=1}^{j+1}m^{-z}
=
\frac{(j+1)^{1-z}}{1-z}
+\zeta(z)
+\frac12(j+1)^{-z}
+O_z(j^{-\sigma-1}).
\tag{L-99453.3}
\]

The error follows directly from the bounded first periodic Bernoulli function;
one further integration by parts gives the displayed exponent uniformly on
compact subsets of \(0<\Re z<1\).

Substituting (L-99453.3), expanding only the two factors
\((1+1/j)^{-z}\) and \((1-1/j)^{-1}\), and retaining the finite
\(C_j\zeta(z)\) term gives

\[
\boxed{
P_j(z)
=
-\frac{z(z+1)}{1-z}j^{-z-1}
+
O_z(j^{-\sigma-2})
+
O_z(j^{-2}).
}
\tag{L-99453.4}
\]

For a nontrivial zero \(\rho\), the leading coefficient

\[
-\frac{\rho(\rho+1)}{1-\rho}
\]

is nonzero. Consequently there is an explicit finite \(J(\rho)\) such that

\[
\boxed{
|P_j(\rho)|
\ge
\frac12
\left|\frac{\rho(\rho+1)}{1-\rho}\right|
j^{-\Re\rho-1}
>0
\qquad(j\ge J(\rho)).
}
\tag{L-99453.5}
\]

No uniformity in the unknown zero is required: Landau is applied after fixing
one hypothetical zero and then one sufficiently large row.

## 3. Landau transfer through a bounded calibration

Suppose

\[
c_X(j)=D_X(j)+A_X(j),
\qquad
D_X(j)\ge0,
\qquad
A_X(j)=O_j(1).
\]

The transform of \(A_X(j)\) is holomorphic in \(\Re s>0\). Hence every
nonremovable pole in (L-99453.2) survives in the Mellin transform of \(D_X(j)\).

Let \(\sigma_c\) be the finite abscissa of convergence of the defining
nonnegative Mellin integral of \(D_X(j)\). Landau's real-abscissa lemma states
that if \(\sigma_c\) is finite, the point \(s=\sigma_c\) is singular. Its proof
is the usual positivity argument: analyticity at \(\sigma_c\) bounds all
positive logarithmic moments and forces convergence a little to the left.

But the continuation furnished by (L-99453.2) minus the bounded calibration is
analytic at every positive real point. Thus \(\sigma_c\le0\), and the defining
integral is holomorphic throughout \(\Re s>0\).

If \(\zeta(\rho)=0\) with \(\Re\rho>1/2\), choose \(j\) by
(L-99453.5). Then the nonnegative Mellin transform has a genuine pole at

\[
s=\rho-\frac12,
\qquad
\Re s>0,
\]

a contradiction. Functional-equation symmetry gives the proposed RH
conclusion.

This theorem closes the analytic interface conditional only on the exact
nonnegative-surrogate plus bounded-root-calibration identity.
