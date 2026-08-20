# L-99581 — Every off-line zero forces two-sided IHR67 oscillation

Claim ID: `L-99581`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: `L-99261/L-99262` for the exact scalar transform  
RH status: **not assumed**

Put `z=s+1/2`. The exact Mellin transform is

\[
\boxed{
\int_1^\infty \mathfrak H_{67}(X)X^{-s-1}\,dX
=
\frac{1-67^{-z}}{s^2}
\left[
 6-\frac{3(2^{-z}-1)(2^{-z}-2)}{\zeta(z)}
\right].
}
\tag{L-99581.1}
\]

This holds initially for `Re(s)>1/2` and continues meromorphically to
`Re(s)>0`. The continued expression is analytic at every positive real `s`:

- at `z=1`, the reciprocal-zeta term vanishes;
- on `(1,infinity)`, the Euler product has no zero;
- on `(1/2,1)`, the alternating eta representation shows that zeta is real and
  nonzero.

Let `rho` be a nontrivial zero with `Re(rho)>1/2`. None of the explicit
multipliers vanishes there:

\[
|67^{-\rho}|<1,
\]

\[
2^{-\rho}=1\Longrightarrow\Re\rho=0,
\qquad
2^{-\rho}=2\Longrightarrow\Re\rho=-1.
\]

Thus (L-99581.1) has a genuine pole at

\[
s_0=\rho-\frac12,
\qquad \Re s_0>0,
\]

with the same multiplicity as the zeta zero.

The arithmetic definition gives
`mathfrak H_67(X)=O(sqrt(X)log(2X))`, so its Mellin integral has finite
abscissa of convergence. If `mathfrak H_67` were eventually nonnegative,
Landau's one-sign theorem would force a singularity at a positive real
abscissa. The continued expression has no such singularity. Applying the same
argument to `-mathfrak H_67` excludes eventual nonpositivity.

Therefore

\[
\boxed{
\zeta(\rho)=0,\ \Re\rho>\tfrac12
\Longrightarrow
\mathfrak H_{67}(X)>0\text{ and }\mathfrak H_{67}(X)<0
\text{ for arbitrarily large }X.
}
\tag{L-99581.2}
\]

Finite verification, however large, cannot replace the global source-specific
transport or cancellation theorem.
