# Validation and remaining review obligations

Status: finite exact diagnostics and same-author mathematical reconstruction. This document is not an independent review receipt.

## What was run

From this directory:

```sh
python check.py > validation.json
python -O check.py > validation.optimized.json
cmp validation.json validation.optimized.json
```

Both final runs returned PASS and the files were byte-identical. The checker uses only the Python standard library, with Fraction arithmetic in Q(omega), omega^2+omega+1=0. It raises RuntimeError on a failed predicate; optimization does not disable the checks. There are 30,634 counted predicates per run. Several predicates test a finite vector of coefficients at once; the count is not a count of independent theorems or asymptotic cases.

## Exact coverage

Local formal Euler algebra is checked through prime-power degree six, for biases 0, 1/3, 1/2 and 1, signs +/-1, every sixth root of unity, and the zero phase. It checks f=m*h, h*g=1, f*g=m, the inverse square correction, and the expectations of the noise coefficients. Degenerate zero-probability sign values are included in the algebraic checks but have zero weight in expectations.

Actual residue characters are constructed at the two ideals above 7 (omega roots 2,4), the two above 13 (roots 3,9), and the inert ideal above 5 of norm 25. Their complete residue fields have the correct literal zero and six equal nonzero character fibers.

The row test enumerates all 54 nonzero elements a+b*omega with norm a^2-ab+b^2<=13. The column test uses the 13 nonunit squarefree products of the FIVE stated prime ideals with norm at most 196. It is NOT the full native column family below 196, and its sharp finite support is NOT a simulation of the fixed smooth Mellin detector. Exclusion cases are none, the first ideal above 7, and the inert ideal above 5. Even moment orders 2,4,6,8 are tested.

All partial-freezing conditional expectations are enumerated exactly. The tests compare each odd-binomial increment against the literal change of moment, verify the fourth-moment coefficient -4, and telescope to the exact Möbius endpoint. The 3,240 row/order/mask increments include 1,058 negative, 1,084 positive and 1,098 zero values. This rules out a monotonicity shortcut on these actual-character polynomials; it proves no asymptotic covariance theorem.

A separate bounded example with repeated prime powers checks centered hypercontractivity after radical grouping. The prime-power p^2 computation explicitly detects the false substitution of an independent inverse-noise copy. No floating-point approximation or OCR is used in the checker.

## Same-author reconstruction, not external approval

The written proofs were checked against the following failure points before publication:

1. The centered-sign argument is obtained by independent-copy symmetrization, not a false hypercontractivity constant for rare normalized signs. Grouping by radical explicitly bounds repeated-prime multiplicities.
2. The inverse-noise coefficient is not centered at even prime powers. Its square-ideal correction is retained before Minkowski is used. No independence between convolution factors is inferred.
3. Uniform finite bias-profile estimates are separated from almost-sure analyticity for one fixed infinite profile. No uncountable full-probability event for changing profiles is claimed.
4. Growing-prime constants do not hide a fixed exceptional set. The threshold for an arbitrary little-o growth function can depend on that function; the displayed log-squared corollary has its own explicit rate.
5. The arbitrary-coefficient obstruction changes the coefficients and is not a counterexample to the native Möbius statement. Its prime ideal theorem input is named and is unnecessary for the positive freezing bound.
6. The signed flux uses the exact cofactor at D/Np, the moving p-exclusion, and the same physical row range. Complete-residue cancellation is not transferred to a norm ball. TARGET-4 and TARGET-k are expressly unproved.
7. The analytic shifted-zero mechanism is credited to Aymone--Sidoravicius. No priority claim is made for the classical factorization or standard sign inequalities.

An independent mathematical reviewer still needs to check the two proof notes, especially Theorem 3.1 and Corollary 3.2 in NOISE_MULTIPLIERS.md and the growth quantifiers and one-sided return in PRIME_FREEZING.md. There was no subagent review, independent rerun by another person, Lean build, or upstream CI run in this pass.

## Integrity

MANIFEST.json records byte lengths, SHA-256 and Git blob SHA-1 for the seven other files. It does not hash itself and is not an analytic certificate. The two validation outputs are intentionally duplicated to preserve the ordinary/optimized pair. A matching source hash authenticates bytes, not the correctness of a mathematical assertion.
