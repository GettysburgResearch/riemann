# R-101100 — Positive completed collar does not desmooth to the fixed CV scalar

Claim ID: `R-101100`  
Status: **PROVED EXACT STATEMENT-TO-USE REFUTATION**  
Created: 2026-08-21  
Depends on: `L-101100`; PRs #677, #684, #686  
RH status: **unproved**

For a finite small-prime set `P_Z`, put

\[
\mathscr A_Z=\prod_{p\in\mathcal P_Z}(I+p^{-1/2}S_p).
\]

For any fixed source scalar `F`,

\[
\boxed{
\mathscr A_ZF
=F+\sum_{\varnothing\ne A\subseteq\mathcal P_Z}
p_A^{-1/2}S_AF.
}
\tag{R-101100.1}
\]

Thus

\[
F=\mathscr A_ZF-
\sum_{\varnothing\ne A}p_A^{-1/2}S_AF.
\tag{R-101100.2}
\]

The correction is signed. Its coefficientwise inverse is alternating, not
positive.

## Exact two-state counterexample

Let `U(x_0,x_1)=(x_1,0)`, let `r=1/2`, and take

\[
F=(-1,3).
\]

Then

\[
(I+rU)F=(1/2,3)\ge0
\]

coordinatewise, while `F_0=-1<0`. Hence even global positivity of a finite
completion does not imply positivity, bounded negative mass, or one-sided
variation control for the original scalar.

## Dynamic-cutoff firewall

In `L-101100`, `Z=X^(9/10)`. Therefore the multiplier `A_(Z(X))` changes with
`X`. Landau's theorem applies to one fixed Mellin density; it cannot consume a
diagonal family of different completed densities.

Consequently the implication

```text
completed squared-core collar has zero negative variation
    -> fixed critical scalar has subpower negative variation
```

is false without an additional source-faithful signed desmoothing theorem.

This is precisely the remaining CV interface.
