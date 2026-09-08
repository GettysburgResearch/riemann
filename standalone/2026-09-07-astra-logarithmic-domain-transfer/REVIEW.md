# Independent review specification

The author requests review of these exact component proofs, not approval of RH.
Use the published head and packet byte inventory. The missing upper bound is
an OPEN claim, not an assigned proof obligation for the reviewer to fill.

1. Verify the canonical-log/outer assumptions and Poisson-Schwarz formula.
   In particular, (8) controls the absolute logarithm using a bounded SAFE
   value; a bounded signed mean alone would be inadequate. Check the minus
   sign and 1/pi in the differentiated Schwarz formula and the 1/sqrt(2)
   Hardy norm constant.
2. Check the explicit logarithmic derivative (13), including the removable
   value at s=1 and every prime power of an included base. Compare it to the
   native derivative before log X; the argument is initial-half-plane
   Laplace uniqueness plus local causality, not a boundary-integral shortcut.
3. Verify the shifted source domain is at alpha=b+sigma, not at b. The
   inward shift is essential; no constant remains uniform at sigma=0.
4. Reconstruct the multiplicity calculation (18)-(21). The target has exactly
   order m-1 at a denominator zero of order m. Thus the highest surviving
   delayed derivative has no powers of log X. Check the Laguerre norm and
   leading coefficient, and distinguish a hypothetical zero from an actual
   computed zero.
5. Check the conditional converse at b=1/2, especially the nonuniform
   prime-square part and the |y|>X tail. No inverse-zeta growth, zero
   simplicity or reciprocal-derivative conjecture is an input.
6. In Abel continuation, check the UNNORMALIZED cutoff weight. The scalar
   exponential must be (s+epsilon-1)zeta(s+epsilon), including its pole
   cancellation. The finite entropy moment, not a guessed log branch, is
   what makes its logarithm analytic in the new domain.
7. Confirm the unconditional PNT upper estimate does not pay epsilon<1-b.
   Neither the general positivity results nor a finite cost bound supplies
   the subpower subsequence. Read the failed attempts rather than silently
   treating this as a completed proof.

The bounded checker covers independent divisor/prime-power controls, complete
small Laguerre Grams, local jets, rational kernels, and constants. It does not
compute an actual off-line zero, an unbounded entropy estimate, or an infinite
operator norm. No external novelty claim or parent-wide review is requested.
