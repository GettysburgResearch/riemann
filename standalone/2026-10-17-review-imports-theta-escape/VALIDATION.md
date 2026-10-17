# Validation and what it establishes

## Fresh checker, not a rerun of the author's checker

`verify.py` was written from the formulas inspected during this review. It does not import #959's verifier, outputs or manifests. Normal and optimized Python produced byte-identical `CHECKS.json`. The 427 predicates include 188 domain guards, 88 density-term checks, 88 finite extremal probability examples, exact polynomial identities, source-indexing guards and the retuned budgets. These counts include related/repeated finite cases; they are not independent analytic theorems.

Polynomials in e use Fraction coefficients. Their nonnegativity on the WHOLE interval [0,1/100000] is established by nonnegative Bernstein coefficients. Strict contour conditions are checked on 0<e<=1/100000, allowing zero margins only at the excluded endpoint. Convexity of the correction domain then covers connecting contour segments. This is a sufficient exact certificate, not a floating fit or a sampled parameter optimization.

The checker reproduces all four #959 central exponents, the two principal remainders, the small and large ranges, the Mellin normalization and the three-way tie. The modified first threshold is also substituted into all ten norm/height terms of de Faveri's detector. The fixed positive e and all ordinary arbitrary losses remain part of the written analytic argument, not a test-generated premise.

## Actually executed negative controls

`run_mutations.py` launches separate optimized Python processes with six corrupted models:

1. Restore the individual-convexity numerator loss.
2. Leave the old principal z remainder in the purported improved comparison.
3. Set the legal support slack M-1 to zero.
4. Claim twice the available high-powerful saving after Cauchy.
5. Pretend one Mobius convolution produces a reciprocal rather than cancelling zeta.
6. Omit the factor two in FSW's log-log discriminant exponent.

Every corrupted process is required to exit unsuccessfully. `MUTATIONS.json` records the actual first failed guard. Exceptions, not Python assertions, implement the tests.

## Publication and replay

The local payload is frozen by `MANIFEST.json`, which lists every other payload file's byte count, SHA-256 and Git blob SHA-1. `verify_manifest.py` rejects missing, altered or additional payload files (ignoring only generated `__pycache__` directories). Publication uses a separate additive branch; remote tree entries are compared with this local inventory. A receipt outside the payload records the resulting commit/PR and read-back scope. The downloadable ZIP is tested after extraction; no success of unexecuted remote CI is claimed.

## Mathematical boundary

These checks do NOT prove the CT metaplectic construction, identify characters by actual computations in a number field, certify the BGL infinite AFE manipulations, establish a reciprocal-L moment, or prove OPEN-L/OPEN-G. No actual L-values or zero census are computed. No Lean build, repository-wide validation, upstream transitive axiom audit, independent human referee, or separately commissioned review agent ran here.

The analytic source-interface review and the new written component arguments are distinct from the finite checker. All new component proofs remain proposed until independently examined. In particular 2747/3000 is a conditional implication, not a newly established zero-free theorem. The review's finding of no fatal error at the inspected interfaces is not an assertion that every possible gap in #959 has been excluded.
