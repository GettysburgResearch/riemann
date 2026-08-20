# L-99614 — Subpower logarithmic negative mass of the SHARP Harnack defect implies RH

Claim ID: `L-99614`  
Status: **PROVED COMPLETE CONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: PR #653 `L-99270`, `L-99272`  
RH status: **the arithmetic negative-mass hypothesis is open**

Let

\[
\mathcal N_{67}(X)
=
\int_1^X\mathfrak H_{67}(x)^-\frac{dx}{x}.
\]

Assume that for some `theta>=0` and every `epsilon>0`,

\[
\mathcal N_{67}(X)
=O_\epsilon(X^{\theta+\epsilon}).
\tag{L-99614.1}
\]

Then the Mellin transform of the negative part is holomorphic in
`Re s>theta`.  Adding it to the exact transform of `L-99251` gives the Mellin
transform of the nonnegative positive part.  Landau's theorem forces its
abscissa of convergence to be at most `theta`, because the exact continuation

\[
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}
\]

has no singularity on the real interval `s>theta`.

Hence the full transform is holomorphic in `Re s>theta`.  A zeta zero `rho`
with

\[
\operatorname{Re}\rho>\frac12+\theta
\]

would give a nonremovable pole at `s=rho-1/2`; the factor
`1-67^{-rho}` is nonzero.  Therefore no such zero exists.

In particular,

\[
\boxed{
\mathcal N_{67}(X)=X^{o(1)}
\quad\Longrightarrow\quad RH.
}
\tag{L-99614.2}
\]

This is strictly weaker than the pointwise global Harnack sign requested by
PR #653.
