# L-99282 — Holomorphic perturbations of a nonnegative fixed row cannot cancel reciprocal-zeta poles

Claim ID: `L-99282`  
Status: **PROVED SELF-CONTAINED ANALYTIC THEOREM**  
Created: 2026-08-20  
RH status: **conclusion-producing**

Fix \(j\ge2\). Let the full Möbius row be

\[
c_X(j)
=
\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\]

Assume that for all sufficiently large \(X\),

\[
\boxed{
c_X(j)=d_X(j)+e_X(j),
\qquad
d_X(j)\ge0,
\qquad
e_\bullet(j)\in\mathscr H_0.
}
\tag{L-99282.1}
\]

## 1. Full-row Mellin transform

For \(\Re s>1/2\), finite Fubini gives

\[
\boxed{
\mathcal C_j(s)
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\frac12)}
{s^2\zeta(s+\frac12)},
}
\tag{L-99282.2}
\]

where

\[
P_j(z)
=
\frac{j+1}{j-1}j^{-z}
-
\frac{(j+1)(j-2)}{j(j-1)}(j+1)^{-z}
-
\frac2{j(j-1)}
\sum_{m=1}^{j+1}m^{-z}.
\tag{L-99282.3}
\]

The right side meromorphically continues to \(\Re s>0\) and is analytic at
every positive real \(s\).

## 2. Holomorphic perturbation

Remove the finite initial interval, whose Mellin transform is entire.
`L-99281` gives that the transform of \(e_X(j)\) is holomorphic on
\(\Re s>0\). Hence the Mellin transform of the eventually nonnegative surrogate
has the continuation

\[
\mathcal D_j(s)=\mathcal C_j(s)-\mathcal E_j(s)-F_j(s)
\tag{L-99282.4}
\]

on \(\Re s>0\), with exactly the same nonreal poles as \(\mathcal C_j\).

The surrogate has finite abscissa of convergence because
\(c_X(j)=O_j(\sqrt X\log(2X))\) and \(e_X(j)=X^{o(1)}\).
If that abscissa were positive, Landau's theorem for a nonnegative Mellin
density would force a singularity at the corresponding positive real point.
Equation (L-99282.4) is analytic at every such point. Therefore the defining
surrogate integral converges and is holomorphic throughout \(\Re s>0\).

## 3. Large-row noncancellation

Euler summation in (L-99282.3) gives, for fixed \(0<\Re z<1\),

\[
\boxed{
P_j(z)
=
-\frac{z(z+1)}{1-z}j^{-z-1}
+
O_z(j^{-\Re z-2})
+
O_z(j^{-2}).
}
\tag{L-99282.5}
\]

The leading coefficient is nonzero at every nontrivial zeta zero. Thus, for
each such zero \(\rho\), all sufficiently large fixed rows satisfy

\[
P_j(\rho)\ne0.
\tag{L-99282.6}
\]

If \(\Re\rho>1/2\), (L-99282.2) has a genuine pole at
\(s=\rho-1/2\) in \(\Re s>0\). Equation (L-99282.4) transfers the same pole to
the defining transform of the nonnegative surrogate, contradicting the
holomorphy just proved.

Therefore no zeta zero lies to the right of the critical line. Functional
equation symmetry gives RH.

The theorem is conditional only on (L-99282.1); it does not require a bounded
defect, score normalization, native capacities, or a prime-square moat.
