# L-97910 — The complete small-prime cube is positive below the quarter barrier

Claim ID: `L-97910`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Inputs: PR #576 `L-97400`; PR #590 largest-prime hardening at `223f1125...`  
RH status: **not assumed**

Let `b(Y)` be the complete `P_61` annular `5:3` scalar, extended by zero below
its support. The corrected directed theorem gives

\[
 b(Y)=a_*\sqrt Y+O(1),
 \qquad
 a_*=12\prod_{p\le61}(1-p^{-1})>0.
\tag{L-97910.1}
\]

The error in (L-97910.1) is globally bounded: the large-`Y` assertion is the
retained asymptotic theorem, and the remaining compact interval is bounded
because `b` is a finite continuous logarithmic-ramp sum.

Fix

\[
 0<\kappa<\frac12
\]

and put

\[
 \boxed{
 Z_\kappa(X)=\bigl(\kappa\log X\log\log X\bigr)^2.
 }
\tag{L-97910.2}
\]

For any least allowed rough prime `p_0>=67`, define the complete Euler cube

\[
 \mathcal B_{p_0,Z}(X)=
 \sum_{d\mid Q_{p_0,Z}}
 \frac{\mu(d)}{\sqrt d}\,b(X/d),
 \qquad
 Q_{p_0,Z}=\prod_{p_0\le p\le Z}p.
\tag{L-97910.3}
\]

No depth truncation is made. Divisors with inactive child endpoint contribute
zero in the original cube.

Then, uniformly in every `p_0>=67`,

\[
 \boxed{\mathcal B_{p_0,Z_\kappa(X)}(X)>0}
\tag{L-97910.4}
\]

for all sufficiently large `X`. More quantitatively,

\[
 \boxed{
 \frac{\mathcal B_{p_0,Z}(X)}{\sqrt X}
 =a_*\prod_{p_0\le p\le Z}(1-p^{-1})
 +O\!\left(X^{-1/2}
           \prod_{p_0\le p\le Z}(1+p^{-1/2})\right).
 }
\tag{L-97910.5}
\]

## Proof

Put

\[
 e(Y)=b(Y)-a_*\sqrt Y.
\]

There is a fixed `C_b` with `|e(Y)|<=C_b` for every `Y>0`. Substitution into
(L-97910.3) is exact, including inactive divisors, because their zero value is
encoded by `e(X/d)=-a_*sqrt(X/d)`:

\[
 \mathcal B_{p_0,Z}(X)
 =a_*\sqrt X\prod_{p_0\le p\le Z}(1-p^{-1})+E(X),
\]

where

\[
 |E(X)|\le C_b\prod_{p_0\le p\le Z}(1+p^{-1/2}).
\tag{L-97910.6}
\]

Removing initial primes increases the positive main product and decreases the
error product, so `p_0=67` is the worst case.

Mertens' theorem gives

\[
 \prod_{67\le p\le Z}(1-p^{-1})\gg(\log Z)^{-1}.
\tag{L-97910.7}
\]

The prime number theorem and partial summation give

\[
 \sum_{p\le Z}p^{-1/2}
 =(2+o(1))\frac{\sqrt Z}{\log Z}.
\tag{L-97910.8}
\]

For (L-97910.2),

\[
 (2+o(1))\frac{\sqrt Z}{\log Z}
 =(\kappa+o(1))\log X.
\tag{L-97910.9}
\]

Thus the error in (L-97910.5) is `X^{kappa-1/2+o(1)}` after normalization,
whereas the positive normalized main term is `gg 1/log Z`. Since
`kappa<1/2`, the ratio tends to zero.

## Scope and sharpness of this proof

Equivalently, the theorem closes every fixed cutoff

\[
 Z=c(\log X\log\log X)^2,
 \qquad c<\frac14.
\]

It closes all depths supported on those primes. It does not assert a sign for
the complementary large-prime debt. The constant `1/4` is the boundary of the
global bounded-remainder estimate: at `c=1/4`, its error loses the strict power
margin. This is a proof barrier, not a counterexample to a larger cube.
