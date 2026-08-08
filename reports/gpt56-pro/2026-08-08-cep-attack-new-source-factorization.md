# CEP attack — complete endpoint source factorization

## Status

This is a research direction note. It does not prove CEP or RH.

The current canonical endpoint scalar is

\[
A_\Lambda(X)=
\sum_{m\le X}2\sqrt m(1-\sqrt{m/X})\log(m/(m-1))
-\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
\]

The remaining theorem is

\[
A_\Lambda(X)=o(\log X).
\]

## New attack: differentiate before estimating

The endpoint kernel is smoother than the scalar itself. Define

\[
K_X(m)=2\sqrt m(1-\sqrt{m/X})\log(m/(m-1)).
\]

Instead of bounding the discrepancy directly, study the logarithmic derivative

\[
\frac{d}{d\log X}A_\Lambda(X).
\]

The benchmark derivative has the exact form

\[
\partial_{\log X}K_X(m)=
\sqrt{m/X}
\log(m/(m-1)).
\]

The arithmetic derivative is controlled by the endpoint insertion of the Chebyshev measure. The conjectural closing identity is therefore not a direct cancellation of \(\Lambda\), but a monotonicity statement for the derivative discrepancy.

## Proposed factorization

Let

\[
\Psi(X)=\sum_{n\le X}\Lambda(n)/\sqrt n.
\]

The endpoint scalar is a smoothed comparison between \(\Psi(X)\) and a fractional integral of the counting measure. A promising route is to rewrite

\[
A_\Lambda(X)=\int_1^X W_X(t)d(\psi(t)-t)
\]

with a positive endpoint-adapted kernel \(W_X\) whose Mellin transform is exactly the CEP firewall factor.

The desired theorem becomes:

\[
\left|\int_1^X W_X(t)d(\psi(t)-t)\right|=o(\log X).
\]

This preserves cancellation before absolute values, unlike prime-only tail estimates.

## Prime-square reserve interaction

The earlier prime-square reserve shows the ordinary-prime reduction should be delayed. The correct order is:

1. prove complete-source cancellation;
2. use prime powers as reserve;
3. descend to ordinary primes.

Removing squares first destroys the natural Selberg square structure.

## Concrete next lemma target

Prove an endpoint Selberg identity of the form

\[
A_\Lambda(X)=B(X)+Q(X),
\]

where

- \(B(X)\) is an explicit boundary term with \(B(X)=o(\log X)\);
- \(Q(X)\) is a positive/negative Hermitian square defect with a nonnegative majorant.

The target is a scalar analogue of the reflected physical blocks already developed elsewhere in the repository.

## Failure conditions

This route must not:

- replace the complete von Mangoldt source by ordinary primes;
- take absolute values before Selberg recombination;
- assume a one-sided sign for \(A_\Lambda\);
- infer cofinal bounds from finite computations.

## Current honest boundary

Known:

- CEP has a direct Mellin consumer;
- prime squares create an ordinary-prime reserve;
- the endpoint scalar is the correct complete source.

Unknown:

- an unconditional sublogarithmic estimate for CEP.
