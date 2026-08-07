# O-9512 — The totient and Möbius local-moment criteria have the same critical loss

Claim ID: `O-9512`  
Title: Two independent all-moments reformulations converge to RH at the same rate  
Status: `PROPOSED CONNECTION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `T-9505`; Verjovsky, arXiv:2607.25002  
Scope: strategic connection, not an RH proof  
Related counterexample candidates: none

## Two variables

The repository's analytic-totient state is

\[
E^{\rm AN}(x)
=\frac12\left(1+\sum_{d>=1}\mu(d)\{x/d\}^2\right).
\]

Verjovsky's normalized Möbius polynomial is

\[
P_N(t)=N^{-1/2}\sum_{n<=N}\mu(n)e^{2\pi int}.
\]

`T-9505` proves that critical `2k`-th moments of `E^AN` on dyadic physical
intervals yield the pointwise exponent

\[
\frac12+\frac1{4k+2}.
\]

Verjovsky's local moment-to-point inequality for exponent `q` yields a Mertens
loss

\[
\frac1{2(q+1)}.
\]

At `q=2k`, the two losses coincide exactly:

\[
\boxed{
\frac1{2(q+1)}
=\frac1{4k+2}.}
\]

## Interpretation

The two moment ladders recover the same distinguished Möbius cancellation from
different coordinates:

1. local Fourier moments recover `M(N)` from a shrinking arc around `t=0`;
2. physical-scale moments recover `E^AN(x)` at an exceptional point through its
   logarithmic Lipschitz modulus;
3. `L-9512` transfers the critical exponent of `E^AN` back to the rightmost
   zeta zero.

The exact agreement of the finite-moment loss suggests seeking a direct
transference theorem between the two positive moment families. Such a theorem
could allow additive-Fourier tools and Farey/Green tools to be combined rather
than developed independently.

## Scope

The July 2026 paper explicitly describes its result as an equivalent
reformulation rather than a proof of RH. The present observation does the same.
Neither local moment family is presently bounded at all unbounded moment orders.

Primary source: A. Verjovsky, *Local Moments of Möbius Fourier Polynomials and
the Riemann Hypothesis*, arXiv:2607.25002.
