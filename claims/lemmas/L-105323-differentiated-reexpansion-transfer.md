# L-105323 — Differentiated xi-prime re-expansion controls reciprocal freezing

Claim ID: `L-105323`  
Status: **PROVED FROM THE PINNED XI-PRIME RE-EXPANSION BOUNDS**  
Created: 2026-08-23  
Depends on: `L-105320`; the exact re-expansion `C(N;L_T+delta)` and its
`H1/H2/H3` estimates at the frozen Anthropic source  
RH status: **not assumed**

## 1. Differentiating the convergent parameter expansion

At the pinned xi-prime base parameter `L_T`, the existing coefficient theorem
has an absolutely convergent expansion

\[
C(N;L_T+\delta)-C(N;L_T)
=\sum_{r\ge1}e_r(N)\delta^r,
\qquad 0\le\delta\le{1\over2},
\tag{L-105323.1}
\]

with radius reserve `rho_0=4` and uniform `H1/H2/H3` bounds. Absolute
convergence permits termwise differentiation. Combining with `L-105320.5`,
for `N>1`,

\[
\boxed{
b_{L_T+\delta}(N)
=-{1\over\log N}
\sum_{r\ge1}r e_r(N)\delta^{r-1}.}
\tag{L-105323.2}
\]

In particular,

\[
\boxed{b_{L_T}(N)=-e_1(N)/\log N.}
\tag{L-105323.3}
\]

Thus the reciprocal source and its entry-dependent variation already live in
the formal xi-prime re-expansion hierarchy.

## 2. Critical reciprocal-square norm

Let

\[
E_\delta(N)=b_{L_T+\delta}(N)-b_{L_T}(N).
\]

The pinned `H3` estimate is

\[
\sum_{N\le X}{|e_r(N)|^2\over N}
\le
A\left({\rho_0\over\ell}\right)^{2r}
\ell^2(1+\log X).
\tag{L-105323.4}
\]

Since `log N>=log 2` for `N>1`, Minkowski gives

\[
\boxed{
\left(\sum_{2\le N\le X}{|E_\delta(N)|^2\over N}\right)^{1/2}
\le
{\sqrt{A(1+\log X)}\over\log2}
\sum_{r\ge2}r\delta^{r-1}
\left({\rho_0\over\ell}\right)^r\ell .}
\tag{L-105323.5}
\]

For `0<=delta<=1/2`, `rho_0=4`, and sufficiently large `ell`, the geometric
derivative sum is `O(ell^-1)`. Therefore, uniformly for `X=T^lambda`, fixed
`lambda<=1`,

\[
\boxed{
\sum_{N\le X}{|E_\delta(N)|^2\over N}
=O(\ell^{-1}).}
\tag{L-105323.6}
\]

The same argument using the pinned `H1` and `H2` estimates gives

\[
\sum_{N\le X}{|E_\delta(N)|\over\sqrt N}
=O(\sqrt X/\ell),
\tag{L-105323.7}
\]

and

\[
\sum_{N\le X}|E_\delta(N)|^2
=O(X/\ell^2).
\tag{L-105323.8}
\]

These are precisely the norm classes entering the existing prime-part Gram
upper bound. For every fixed `lambda<1`, the `X`-dependent terms are lower
order than the `T ell` zero-count scale.

## 3. Positive Hardy division

The factor `1/log N` has the exact representation

\[
{1\over\log N}=\int_0^\infty N^{-u}\,du.
\tag{L-105323.9}
\]

Hence the reciprocal prime polynomial is a positive safe-line Hardy average
of the parameter derivative:

\[
\boxed{
\sum_{N\le X}{b_L(N)\over N^s}
=
-\int_0^\infty
\sum_{2\le N\le X}{\partial_L C(N;L)\over N^{s+u}}\,du.}
\tag{L-105323.10}
\]

All sums are finite, so no interchange issue occurs. This prevents the Hardy
division from creating a new oscillatory source or inverse-filter cost.

## 4. Consequence

The entry-dependent coefficient-freezing row is reduced to the already pinned
xi-prime re-expansion and prime-part machinery. What remains unproved in
`WXFER105320` is not a new coefficient family estimate but:

```text
passage of the finite Wick congruence through the complete contour;
control of horizontal and pole terms;
canonical-product and common-zero positive-index tails;
and the final trace/HS comparison for the actual Xi matrix.
```

This lemma does not, by itself, prove the full Gram transfer.
