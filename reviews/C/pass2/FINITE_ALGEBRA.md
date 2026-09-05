# Reviewer C — independent finite algebra and its exact scope

These arguments use no research producer implementation or analytic prime estimate. The accompanying `scripts/independent_finite_algebra.py` provides bounded independent coefficient checks; the universal finite identity follows from the proof below, not extrapolation from those checks.

## 1. Largest-owner telescoping for every finite commuting family

Let `D_1,...,D_n` be commuting linear operators on one vector space and put

\[
F_0=I,\qquad F_j=\prod_{i=1}^j(I-D_i).
\]

Commutativity gives `F_j−F_{j−1}=−D_j F_{j−1}`. Summing these differences proves, for every nonnegative integer `n`,

\[
\boxed{\prod_{j=1}^n(I-D_j)
=I-\sum_{j=1}^nD_j\prod_{i<j}(I-D_i).}
\]

The same identity follows by expanding the left product: each nonempty squarefree monomial has a unique largest index `j`; choosing its smaller indices supplies precisely the term indexed by `j` on the right. Thus the identity has a complete all-finite proof independent of the numerical tests.

Weighted dilation operators `D_p f(X)=p^{-1} f(X/p)` commute. Applying the identity to a specified finite list of these operators and to a fixed small-prime base gives the finite largest-prime telescope. Equality with a particular native arithmetic source, its zero-extension/cutoff convention and its all-scale estimates remain additional source/analytic obligations; this abstract identity does not supply them.

The independent checker expands one side by polynomial multiplication and the other by largest-index subset ownership for ranks 0 through 8, checking 511 coefficient positions in total. It neither imports the #599 code nor treats these nine ranks as a proof of an asymptotic estimate.

## 2. Fixed 5:3 row algebra

Let

\[
P_2=2a-1-b,\qquad 3P_3=5b-a-1-3a^2.
\]

Direct collection of independent coefficients gives

\[
5P_2+3P_3=-3a^2+9a-6=-3(a-1)(a-2).
\]

For complex `a` with `|a|<1`, neither factor vanishes, so the scalar is nonzero and the two rows cannot both vanish. The checker independently collects the coefficients on the left and multiplies the two factors on the right; it does not compare two copies of an asserted coefficient tuple.

This is finite numerator algebra. Identifying a with the correct exponential coordinate and binding the numerator to one fixed native detector's Mellin transform are separate source/analytic statements. No negative-mass estimate or RH conclusion is proved here.

## 3. Error-bound sign control

For real `M,E,R` and `B≥0`, the hypotheses `|E|≤B` and `R≥−M+B` give

\[
M+E+R\ge M-B-M+B=0.
\]

Using instead `R≥−M−B` is insufficient: `M=2`, `B=1`, `E=−1`, `R=−3` satisfies those weaker inequalities but has total `−2`. Keeping the actual signed error permits the exact condition `R≥−M−E`. This clarifies sufficient error budgeting for downstream source adapters; it is not a claim that a cited source explicitly asserts the wrong condition.

## 4. What the replays do not establish

The finite identities do not prove PNT, Mertens, uniformity in growing cutoff parameters, an imported interval endpoint, a signed boundary remainder, an individual-zeta detector estimate, or a source-coverage theorem. The separate #568/#599 author replays authenticate and reproduce only their declared finite fixtures and floating/Decimal calculations. Their optimization-sensitive assertions are documented by temporary-copy mutations, not by altering the retained research sources.
