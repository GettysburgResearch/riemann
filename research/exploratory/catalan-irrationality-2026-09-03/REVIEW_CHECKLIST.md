# Review checklist

Attach reviewer, date, exact source version, and evidence path to every checked
item.

## A. Provenance

- [ ] Attached PDF SHA256 equals the source lock.
- [ ] PDF has 20 pages and expected metadata.
- [ ] All pages were rendered and visually inspected independently.
- [ ] Current arXiv version is checked for revisions or errata.
- [ ] A companion source/code repository is searched for again.
- [ ] Any later source is pinned by immutable commit and license.

## B. Definitions and dimensions

- [ ] `T_m`, `u_m`, and the recurrence are exact.
- [ ] `Pi_i` uses the correct `B` consecutive odd factors.
- [ ] The residual row and column ranges are exact.
- [ ] Section 3 explicitly defines `D=2B`.
- [ ] `D+S+3=N`.
- [ ] `F_B=product_{r=0}^{2B-1} r!`.
- [ ] The three auxiliary columns correspond exactly to the omitted rows.

## C. Full-rank argument

- [ ] Polynomial defect degree is at most `2B-3`.
- [ ] The finite differences annihilate exactly the required range.
- [ ] `lambda -> P_lambda^*` is injective.
- [ ] `D_lambda` is nonzero and has degree at most `2B-1`.
- [ ] The zero sets of `K` and `G_0` are disjoint as claimed.
- [ ] The rational-difference no-solution proof handles the polynomial case.
- [ ] Every pole-shift argument counts multiplicities correctly.

## D. Determinant factorization

- [ ] Newton transform determinant is `+-1`.
- [ ] Reference pivots are the stated factorials.
- [ ] Auxiliary columns become the three exact unit vectors.
- [ ] Cauchy-Binet index and sign conventions are correct.
- [ ] Lemma 4.1 factorial normalization is correct.
- [ ] `Psi_A(I)` is an integer.
- [ ] Uniform degree and coefficient-height bounds for `Psi_A(I)` are proved.
- [ ] Cauchy determinant contributes the second `V(I)`.
- [ ] All powers of two are tracked.

## E. Local valuation layer

- [ ] Formula (5.7) matches every factor in (4.5).
- [ ] Tail denominator bound (5.11) is correct.
- [ ] Taking the minimum after the p-adic triangle inequality is legal.
- [ ] The sum over prime-power layers is finite.
- [ ] Theorem 5.1 states `S<=B/20`.
- [ ] Balanced occupancy really minimizes the collision number.
- [ ] Inequality (5.21) is proved for all intended `B,S,Q`.
- [ ] The prime-2 positive-part argument is independent of odd-prime formulas.

## F. Stability

- [ ] Actual and ideal upper row indices are correct.
- [ ] Every surplus-row exchange is explicit.
- [ ] Local base-cost change is bounded uniformly.
- [ ] Double-Vandermonde occupancy change is bounded uniformly.
- [ ] The support cutoff is proved; no unproved `5B` claim remains.
- [ ] Weighted sum of changes is `o(B^2)`.
- [ ] Real-place and `Psi_A` stability are included.

## G. Small-prime certificate

- [ ] Breakpoint set has exactly 238 raw cells.
- [ ] Merge to 178 cells preserves formulas.
- [ ] `K_v(n+v)` recurrence is proved, not only sampled.
- [ ] Every `Q_0(v)` piece is the claimed rational quadratic.
- [ ] Antiderivative (6.26) differentiates correctly.
- [ ] Argument shifts by 64 are exact.
- [ ] Bernoulli remainder bounds and signs are correct.
- [ ] Logarithm and `log(2pi)` enclosures are directed.
- [ ] Final interval for `I_odd` is reproduced from clean bytes.

## H. Middle-prime certificate

- [ ] Six affine boundaries are complete.
- [ ] Floor-change values are complete.
- [ ] All ordering-crossing events are included.
- [ ] Lowest-`rho` marginal selection is correct on every cell.
- [ ] There are exactly 235 affine cells.
- [ ] Exact integration recovers the displayed rational.
- [ ] Decimal bounds follow by rational arithmetic.

## I. Large-prime range

- [ ] Seven pieces in (8.1) are derived from exact local minima.
- [ ] Their endpoint conventions do not lose mass.
- [ ] Integral (8.2) is correct.
- [ ] Raw baseline (8.3) is derived.
- [ ] Higher powers contribute `o(B^2)` with explicit support.

## J. Proposition 9.5

- [ ] One master finite ledger is written.
- [ ] Every `B^2 log B` coefficient cancels visibly.
- [ ] Raw `4rho-2rho^2` coefficient is derived.
- [ ] Prime 2 is included exactly once.
- [ ] Odd small, middle, and large ranges have correct signs.
- [ ] `Psi_A(I)` contributes only `o(B^2)`.
- [ ] Number of subsets contributes only `o(B^2)`.
- [ ] Stirling errors are uniform in `A` and `I`.
- [ ] Floor errors and surplus rows are uniform.
- [ ] PNT partial summation applies to the exact piecewise functions.
- [ ] Fixed `q^S` contributes only `o(B^2)`.

## K. Final theorem

- [ ] Conservative margin is strictly positive.
- [ ] `H_B^min` is the denominator of the same nonzero scalar.
- [ ] `q^S H_B^min qhat_B` is a nonzero integer.
- [ ] The asymptotic upper bound is eventually negative.
- [ ] No implicit dependence of `A` invalidates uniformity.

## L. Riemann boundary

- [ ] No RH implication is claimed.
- [ ] PNT is not described as RH-strength.
- [ ] Special-value irrationality is separated from zero distribution.
- [ ] Numerical diagnostics are not described as certificates.
- [ ] No source theorem is entered in `canonical/` before review.
