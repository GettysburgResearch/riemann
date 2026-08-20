# M-99900 — Next attack on the corrected half-order frontier

The exact source is now narrow enough for a fail-closed attack.

1. Work with the literal coefficient
   `a_n=beta(n)/sqrt(n)`; never replace it by `mu(n)`.
2. Use `L-99901` to express every Poisson square through cumulative coefficient
   tails before applying Cauchy--Schwarz.
3. Use `L-99902` to decompose each multiplicative block into diagonal,
   near-ratio, large-gcd, and separated coprime sectors.
4. The diagonal and bounded-ratio source-free terms are elementary. The
   remaining separated sector is the same phase-sensitive half-order Type-II
   geometry already isolated by SACF/C4MBI, now with the exact duplicate-67
   three-band coefficients.
5. Any claimed proof must retain both off-diagonal signs and the activation
   overlap length. A source-blind PSD or unweighted Mertens estimate is not a
   substitute.

A useful next theorem would be a one-sided Type-II estimate directly for

\[
\sum_{m\ne n}
\frac{\beta(m)\beta(n)}{\sqrt{mn}}
\ell_{U,V;67}(m,n)
\]

with the exact filtered coefficient packet. A subpower upper bound, combined
with the already subpower diagonal, would prove `GPMOC99800`.
