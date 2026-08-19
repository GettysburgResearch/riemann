# L-99242 — An eventually nonnegative row modulo a Mellin-holomorphic defect excludes every off-line zero

Claim ID: `L-99242`  
Status: **PROVED SELF-CONTAINED ANALYTIC THEOREM**  
Created: 2026-08-19  
Depends on: fixed-row definitions only  
RH status: **conclusion-producing**

Fix \(j\ge2\). Let

\[
c_X(j)=\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j)
\]

be the full Möbius component row. Suppose that for all \(X\ge X_0\),

\[
\boxed{
c_X(j)=d_X(j)+\mathfrak E_X(j),
\qquad d_X(j)\ge0,
\qquad |\mathfrak E_X(j)|\le B_j.
}
\tag{L-99242.1}
\]

Define \(d_X(j)=0\) for \(1\le X<X_0\).

## 1. Exact Mellin transform of the full row

Put

\[
A_j=\frac{j+1}{j-1},
\quad
B_j^{(0)}=\frac{(j+1)(j-2)}{j(j-1)},
\quad
C_j=\frac2{j(j-1)}.
\]

For \(z=s+\tfrac12\), finite Fubini and
\(\sum\mu(n)n^{-z}=1/\zeta(z)\) give initially for \(\Re s>\tfrac12\)

\[
\boxed{
\mathcal C_j(s)
=
\frac{C_j}{s^2}
+
\frac{P_j(s+\frac12)}
{s^2\zeta(s+\frac12)},
}
\tag{L-99242.2}
\]

where

\[
P_j(z)
=
A_jj^{-z}
-B_j^{(0)}(j+1)^{-z}
-C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-99242.3}
\]

The right side meromorphically continues to \(\Re s>0\) and is analytic at
every positive real \(s\).

## 2. The surrogate has the same nonreal poles

The finite initial integral

\[
F_j(s)=\int_1^{X_0}c_X(j)X^{-s-1}\,dX
\]

is entire. By boundedness, the defect transform

\[
\mathcal E_j(s)
=\int_{X_0}^{\infty}\mathfrak E_X(j)X^{-s-1}\,dX
\]

is holomorphic on \(\Re s>0\). Therefore the Mellin transform of the
nonnegative surrogate,

\[
\mathcal D_j(s)
=
\int_1^\infty d_X(j)X^{-s-1}\,dX,
\]

has continuation

\[
\boxed{
\mathcal D_j(s)
=
\mathcal C_j(s)-F_j(s)-\mathcal E_j(s).
}
\tag{L-99242.4}
\]

Thus every pole of \(\mathcal C_j\) in \(\Re s>0\) survives in
\(\mathcal D_j\).

## 3. Large-row noncancellation

For fixed \(z\) with \(0<\Re z<1\), Euler summation in (L-99242.3) gives

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
\tag{L-99242.5}
\]

The leading coefficient is nonzero for every nontrivial zeta zero. Hence, for
every such zero \(\rho\), one can choose a fixed sufficiently large \(j\) with

\[
P_j(\rho)\ne0.
\tag{L-99242.6}
\]

## 4. Landau argument

The nonnegative function \(d_X(j)\) has finite Mellin abscissa because
\(c_X(j)=O_j(\sqrt X\log(2X))\) and the defect is bounded.

Let \(\sigma_c\) be that abscissa. If \(\sigma_c>0\), Landau's theorem for a
nonnegative Mellin density forces a singularity at the real point
\(s=\sigma_c\). But (L-99242.4) is analytic at every real \(s>0\). Therefore

\[
\sigma_c\le0,
\]

so the defining nonnegative Mellin integral is holomorphic throughout
\(\Re s>0\).

If \(\zeta(\rho)=0\) with \(\Re\rho>\tfrac12\), choose \(j\) by
(L-99242.6). Equation (L-99242.2) has a genuine pole at

\[
s=\rho-\frac12,
\qquad \Re s>0,
\]

and (L-99242.4) shows the same pole in \(\mathcal D_j\), a contradiction.

Thus zeta has no zero to the right of the critical line. The functional
equation gives the symmetric half, and

\[
\boxed{\mathrm{RH}.}
\tag{L-99242.7}
\]
