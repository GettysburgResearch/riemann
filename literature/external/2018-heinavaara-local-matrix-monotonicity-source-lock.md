# External source lock — local characterisation of finite-order matrix monotonicity

Source: Otte Heinävaara, **Local characterizations for the matrix
monotonicity and convexity of fixed order**, Proc. Amer. Math. Soc. 146
(2018), no. 9, 3791–3799; arXiv:1608.07516; DOI
`10.1090/proc/13674`.

Status: **PUBLISHED EXTERNAL THEOREM / NOT REPROVED HERE**  
Created: 2026-08-14  
RH status: **unproved**

## Imported statement

For an open real interval `(a,b)`, an integer `n>=2`, and a
`C^(2n-1)` function `f`, the following are equivalent:

1. `f` is matrix monotone of order `n` on `(a,b)`;
2. every `n x n` Loewner matrix of `f` is positive semidefinite;
3. for every `t in (a,b)`, the local Hankel matrix

\[
 \boxed{
 M_n(t,f)
 =\left(
 \frac{f^{(i+j-1)}(t)}{(i+j-1)!}
 \right)_{1\le i,j\le n}
 \succeq0.
 }
\]

Heinävaara gives an integral representation of each Loewner matrix as an
integral of congruences of the local Hankel matrices, with a nonnegative
Peano/B-spline weight.  The result is the Dobsch–Donoghue local
characterisation in a form suited to the present programme.

## Use in this branch

`L-92204` identifies `M_n(t,Z)` by an exact invertible Toeplitz congruence
with the adjacent Stieltjes-Hankel matrix of the safe Xi admittance

\[
 p(t)=1/Z(t).
\]

Thus finite-order matrix monotonicity of the Xi impedance is exactly a finite
Hankel-moment problem.

## Trust boundary

The published theorem is imported.  The reciprocal Toeplitz congruence and
the zeta-specific positivity claims are new and remain subject to independent
review.
