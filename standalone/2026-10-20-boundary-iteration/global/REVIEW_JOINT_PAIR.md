# Review of the joint pair and comparison with the supplied completed mean

20 October 2026. Independent review of the new joint absorption and its
source comparison; the quadratic convention bridge is the reviewer's own
work. No new zero-free boundary is certified here.

Reviewed `mixed/JOINT_PAIR_UNEQUAL_CUTOFFS.md` at SHA256
`36277fce41d0c5d425b534b885cd08cd3444a33fbeb49dfa45303f1c13d195c7`.
The inherited finite-profile reflection and analytic large sieves remain
explicit imported inputs, rather than being re-proved by this review.

## Arithmetic and absorption checks

The quadratic orientation is exactly the kernel checked in
[QUADRATIC_LARGE_SIEVE_SOURCE_AUDIT.md](QUADRATIC_LARGE_SIEVE_SOURCE_AUDIT.md).
For each fixed cubic row and bad-place ray sector, its column coefficient
is independent of the quadratic row. The sextic partner has digit one,
not digit five, and must use the sextic sieve separately. Finite cusp
corrections depend only on fixed bad-place classes, so a finite partition
precedes either sieve.

The cube character remains the quadratic character in both partners.
At each fixed cube ideal its value is a row phase with the original zero;
removing the phase retains the positive coprimality restriction. The
cube coefficient on the right line has modulus `Nd^(-1-3 delta)`.
Minkowski is convergent for positive delta, including all four displayed
nonnegative column exponents. No coprimality between the squarefree and
cube columns is needed or inserted.

The reflection interchanges the two partners, preserves the quadratic
conductor, and replaces the cubic row only by divisors. Its squared
conductor factor and the weighted divisor sum agree with the earlier
exact pair. Every displayed power of the cubic row bound in either
normalization exceeds `2 delta`. Partial summation therefore has the
claimed cost. Both finite conductor truncations close. Polynomial strip
growth makes the height-normalized suprema finite before absorption;
the Gaussian convolution has a finite weighted norm. Enlarging both
cutoffs by the common fixed constant makes the two normalized maps
strict contractions. The expressions for `c0`, `c2`, and the balanced
exponents are algebraically consistent.

**Verdict on the argument:** no new arithmetic or closure gap found,
conditional on its stated upstream analytic inputs.

## The balanced exponent is already available from a supplied input

There is a stronger comparison than summing the fixed-conductor bound.
[rStation paper 5, equations (11.1)--(11.4)](https://rstation.ai/problems/riemann_hypothesis/papers/5)
gives a completed smooth dyadic bound. Substituting its row bound `H`
and fourth-power label length `R`, and undoing its normalized label
average, gives

\[
 E_2(D)\ll (RHD)^\epsilon\{RH+R^2H^2/D\}.                 \tag{1}
\]

The digit-one partner is the required positive sextic family. The
fixed cusp profiles can first be expanded into their finite good-column
ray characters; their ramified geometric factors are absolutely
convergent on the present line. Cube completion has precisely the
quadratic twist prescribed by the source's multiplicative character
cubed. Restricting its positive row and label averages to squarefree
coprime pairs is legitimate.

A second estimate for the same completed dyad is the elementary sextic
bound, obtained with the same cube Minkowski argument:

\[
 E_2(D)\ll(RHD)^\epsilon
 \{RH+RD+RH^{5/6}D^{1/3}+RH^{1/3}D^{5/6}\}.             \tag{2}
\]

To evaluate the continued completed series on `Re s=1/2+delta`, its
normalized dyad is multiplied by `D^(-delta-it)`. Use (2) on `D<=V`
and (1) on `D>V`, for the value of `V` in the reviewed note. Minkowski
in the joint row-label Hilbert space, with preliminary epsilon smaller
than delta, gives

\[
 \begin{split}
 \mathcal M_2\ll(RH)^\epsilon\{RH
 &+RV^{1-2\delta}+RH^{5/6}V^{1/3-2\delta}\\
 &+RH^{1/3}V^{5/6-2\delta}
 +R^2H^2V^{-1-2\delta}\}.                              \tag{3}
 \end{split}
\]

Every short-column exponent is positive because `delta<1/6`.
The long-column floor is summable: its dyadic norm is bounded by
`(RH)^(1/2) D^(-delta+epsilon)`. Thus no convergence on the central
line is assumed. First use the identity where the series converges
absolutely, then local uniform Hilbert-space convergence and analytic
continuation. Equation (3) is no larger than the proposed `F2`; it
even omits its extra positive term `c2 RH`.

With this right-line `F2` estimate already established, one quadratic
free split at `W` gives

\[
 \mathcal M_0\ll O_0(W)+c_0F_2\ll F_0
\]

by the same exact reflection and divisor partial summation. This step
uses neither a left-line Dirichlet-series expansion nor circular
self-absorption.

Consequently the proposed `28/11` balanced exponent improves the sum
of the earlier fixed-conductor estimates, but is also recoverable from
the supplied recursive completed mean plus the ordinary sextic sieve.
The unequal-cutoff proof is a distinct derivation from a smaller input
set; its numerical exponent should not be described as a new best
estimate relative to all supplied work. No strict detector improvement
follows from either derivation.

## Final-version additions

The reviewed final version now includes the source-overlap calculation
above in its own Section 5, with the appropriate reduced-dependency
scope. Its added Section 6 is also valid: Gauss multiplicativity removes
the outer row factors, the right-line cube reciprocal is bounded by
absolute Euler convergence, and Cauchy in the actual row pairs gives
`A^(1/2+delta) (RH Fj)^(1/2)` for the stated smooth free column.
Substitution at equal lengths gives exactly the exponents in JQ17 and
the limiting `59/22` and `89/33` powers. Its jointly dependent outer
coefficients are permissible. The explicit exclusion of prime inner
support and arbitrary inner arithmetic multipliers is necessary and
retained. No additional analytic or consumer gap was found.
