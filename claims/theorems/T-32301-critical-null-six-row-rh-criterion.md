# T-32301 — Critical-null six-row carry criterion for RH

Claim ID: `T-32301`  
Title: One explicit six-row carry combination with the real critical mode removed is sufficient for RH  
Status: **PROPOSED COMPLETE CONDITIONAL CRITERION — THE SIX-ROW ESTIMATE IS OPEN**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32302`; exact triangular carry inversion; Landau one-sign/abscissa principle in the form already used elsewhere in the repository  
Scope: full RH criterion; no unconditional estimate is claimed

## 1. Exact finite scalar

Let `c_X(n)` be the unique triangular inverse coefficients satisfying, for `2<=q<=X`,

\[
w_X(q)=q^{-1/2}\log(X/q)
=\sum_{n=q}^Xc_X(n)\beta_{nq}.
\tag{T-32301.1}
\]

Define

\[
\begin{aligned}
\mathcal C_\dagger(X)={}&
-\left({5\over6}+{\sqrt2\over3}\right)c_X(2)
-{1\over2}c_X(3)\\
&+{11\sqrt2\over10}c_X(4)
 +{5\sqrt2\over6}c_X(5)
 +{9\sqrt2\over14}c_X(6)
 +{\sqrt2\over2}c_X(7).
\end{aligned}
\tag{T-32301.2}
\]

By `L-32302.14--15` and exact carry inversion,

\[
\boxed{
\mathcal C_\dagger(X)
=\sum_{2\le q\le X}\omega_\dagger(q)q^{-1/2}\log(X/q).
}
\tag{T-32301.3}
\]

The lower limit `q=2` is load bearing: the carry system has no `q=1` column, while `omega_dagger(1)=1`. Thus the complete Dirichlet Riesz source differs from the six-row carry scalar by exactly `log X`.

No averaged carry row `n>=8` occurs.

## 2. Mellin transform

For `Re z` initially large, the elementary Riesz integral gives

\[
\boxed{
\int_1^\infty \mathcal C_\dagger(X)X^{-z-1}\,dX
={1\over z^2}
\left[
{P_\dagger(2^{-z-1/2})\over\zeta(z+1/2)}-1
\right].
}
\tag{T-32301.4}
\]

The `-1` is the omitted unit source `q=1`. At `z=0`,

\[
P_\dagger(2^{-1/2})=0,
\]

so the bracket tends to `-1`; the six-row scalar therefore retains the elementary real `-log X` mode. This normalization is consistent with direct finite evaluation.

At every point

\[
z=\rho-{1\over2}
\]

coming from a zeta zero with `Re rho>1/2`, the finite numerator is nonzero by `L-32302.5`; subtracting `1` does not remove the pole. Hence every hypothetical off-line zero remains an uncancelled singularity of (T-32301.4).

For every positive real `z`, the right side has no zeta-zero singularity. The zeta pole at `z=1/2` contributes a finite value to the bracket, not a pole.

## 3. Two sufficient closing statements

Either of the following is sufficient for RH.

### Critical-null subpower bound

\[
\boxed{
\forall\varepsilon>0,
\qquad
|\mathcal C_\dagger(X)|=O_\varepsilon(X^\varepsilon).
}
\tag{CNSB}
\]

Then the Mellin transform is holomorphic in `Re z>0`. An off-line zero would create an uncancelled pole there, contradiction.

### Eventual one-sign form

It is also sufficient to prove that `mathcal C_dagger(X)` has one sign for all sufficiently large `X`. If its convergence abscissa were positive, Landau's theorem would force a singularity at a positive real point. Equation (T-32301.4) has none. Hence the abscissa is at most zero; the pole at `z=0` is compatible with the elementary logarithmic mode, while every hypothetical off-line pole has positive real part and is excluded.

## 4. Why this criterion is different from the five-adic quotient

The finite numerator annihilates the **real square-root critical source mode** before any residue quotient is taken:

\[
P_\dagger(2^{-1/2})=0.
\]

The remaining `-log X` term is not that arithmetic mode; it is the explicit omitted unit carry column. It has been retained exactly rather than hidden inside the source normalization.

At the same time the numerator retains all nonreal critical-line modes except the discrete dyadic lattice where the finite factor itself vanishes, and it retains every off-line zero.

Therefore a future finite transition theorem may legitimately work in a critical-null source space without silently deleting the PR #277 half-moment.

## 5. Review-facing target

A claimed unconditional completion must prove, not assume, one of:

```text
CNSB for the exact six-row scalar;
eventual one-sign of the exact six-row scalar;
a source-specific reflected/carry estimate which implies CNSB.
```

The present branch does not supply that final estimate.

## 6. Exact status

```text
critical-null source/filter algebra       PROPOSED COMPLETE
positive inverse/generalized primes       PROPOSED COMPLETE
factor-eight pointwise carry image        PROPOSED COMPLETE
six-row averaged collapse                 PROPOSED COMPLETE
q=1 normalization                         CORRECTED EXACTLY
six-row Mellin transform                  PROPOSED COMPLETE
CNSB / eventual one-sign                  OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVEN
```
