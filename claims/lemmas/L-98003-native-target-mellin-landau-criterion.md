# L-98003 — Native target capacity is itself a zero-safe Mellin–Landau criterion

Claim ID: `L-98003`  
Status: **PROVED COMPLETE CONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-18  
RH status: **the arithmetic target sign is not proved here**

Define the signed completed target

\[
H_X=T_E(X)-T_O(X)
=
\sum_{k\ge1}{\mu(k)\over\sqrt k}T(X/k),
\tag{L-98003.1}
\]

where `T(Y)=(4sqrt(Y)-3)1_(Y>=1)`. The sum is finite for every real `X`.

For `Re s>1/2`, absolute Fubini gives

\[
\begin{aligned}
\int_1^\infty H_X X^{-s-1}\,dX
&=
{1\over\zeta(s+1/2)}
\int_1^\infty(4\sqrt Y-3)Y^{-s-1}\,dY\\
&=
\boxed{
{s+3/2\over s(s-1/2)\zeta(s+1/2)}.
}
\end{aligned}
\tag{L-98003.2}
\]

The factor `k^(-s-1/2)` in the substitution `X=kY` is essential.

At `s=1/2`, the pole in `(s-1/2)^(-1)` is cancelled by the zero of
`1/zeta(s+1/2)` at the zeta pole. The continuation is analytic at every
positive real `s`: zeta has no positive real zero, and the remaining apparent
points are removable.

If `rho` is a nontrivial zeta zero with `Re rho>1/2`, then (L-98003.2) has a
nonremovable pole at

\[
s=\rho-1/2.
\]

The numerator there is `rho+1`, which is nonzero for every nontrivial zero.
Multiplicity is retained.

The elementary bound

\[
|H_X|\ll\sqrt X\log(2X)
\]

provides a finite Mellin abscissa. If `H_X>=0` for all sufficiently large real
`X`, discard the finite initial interval and apply Landau's theorem to
`H_(e^t)`. Since the continuation is analytic at every positive real point, its
abscissa is at most zero. A pole from an off-critical zero is impossible.
Functional-equation symmetry then gives RH.

Thus, with

> **Global Target Capacity 67 (`GTC67`).** `H_X>=0` for every sufficiently large
> real `X`,

we have

\[
\boxed{\mathrm{GTC}_{67}\Longrightarrow\mathrm{RH}.}
\tag{L-98003.3}
\]

This is a conditional analytic implication, not an unconditional proof of the
target sign. It explains why total target capacity cannot be dismissed as
routine bookkeeping after the Lorenz marginal collapses.