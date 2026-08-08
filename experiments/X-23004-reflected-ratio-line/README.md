# X-23004 — Reflected ratio-line algebra

This standard-library exact regression checks the finite source algebra behind
`R-23006`.

It verifies:

- for a squarefree product with `k` primes, the double inverse coefficient is
  the product of `k` same-sign two-orientation **sums**;
- the value at the identity orientation is `(-2)^k`, hence nonzero;
- the basic reflected ratio numerator is `X+X^-1`;
- after clearing one monomial, `X^2+1` is not divisible by the candidate
  difference denominator `1-X^2`;
- the semiprime Hermitian ratio pair has equal positive coefficients in the two
  orientations.

This is finite formal Laurent-polynomial algebra only. It does not assert that
no enlarged source identity can repair the ratio sector, and it proves no
statement about RH.
