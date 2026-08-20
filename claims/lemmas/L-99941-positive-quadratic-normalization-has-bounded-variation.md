# L-99941 — The positive quadratic normalization has finite ordinary variation and a positive limit

Claim ID: `L-99941`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: `L-99939`, `L-99940`  
RH status: **not assumed**

Let

\[
G_2(u)=e^{-u}\mathfrak H_2(e^u).
\]

Then:

1. `G_2(u)>0` for every `u>=0`;
2. `G_2` has finite total variation on `[0,infinity)`;
3.

\[
\boxed{
\lim_{u\to\infty}G_2(u)
=16\frac{1-67^{-3/2}}{\zeta(3/2)}>0.
}
\]

## Variation

The atomic variation is finite because

\[
\sum_n\frac{|\beta(n)|}{n^{3/2}}<\infty.
\]

Also `0<=T(y)<=4sqrt(y)` for `y>=1`, so

\[
|\mathfrak H_1(x)|
\le8\sqrt x\sum_{n\le x}\frac1n
\le8\sqrt x(1+\log x).
\]

By `L-99940`, the continuous variation is bounded by

\[
3\int_1^\infty|\mathfrak H_1(x)|\frac{dx}{x^2}<\infty.
\]

## Limit

Expanding `T^2` gives

\[
\frac{\mathfrak H_2(x)}x
=16\sum_{n\le x}\frac{\beta(n)}{n^{3/2}}
 -\frac{24}{\sqrt x}\sum_{n\le x}\frac{\beta(n)}n
 +\frac9x\sum_{n\le x}\frac{\beta(n)}{\sqrt n}.
\]

The first sum converges absolutely to

\[
16\frac{1-67^{-3/2}}{\zeta(3/2)}.
\]

The second and third terms tend to zero by the elementary bounds
`sum_(n<=x)1/n=O(log x)` and `sum_(n<=x)n^(-1/2)=O(sqrt x)`.
