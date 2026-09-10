# Validation and assurance boundary

Date: 2026-09-10. Environment: CPython 3.13.5. No third-party library is required by the retained checker or tests. Exploratory mpmath/SymPy scripts were used during derivation but are not trusted or included as proof producers.

Executed successfully:

```sh
python check.py --out checks.json
python -O check.py --verify checks.json
python -m unittest -v test_check
python -O -m unittest -v test_check
python -m py_compile check.py test_check.py
```

Five test methods passed in each interpreter mode. Each mode included complete receipt recomputation, three altered-receipt refusals (RH flag, interval endpoint, rational defect constant), arithmetic-domain refusal checks, and a comparison of the complete N=320 and N=400 series enclosures.

The produced phase interval is outwardly enclosed by

`[-0.012270544269418342, -0.011449778905716176]`.

It proves only the negative phase derivative of the specified second-level gamma approximant at one point, conditional on the explicitly reconstructed special-function formulas and Binet remainder. It is not a zero certificate.

## Arithmetic contract

The trusted numerical primitives are Python arbitrary-precision integers, exact Fraction arithmetic, and integer square root. Dyadic interval operations explicitly use floor and ceiling. Series truncations include their analytic infinite tails. Machin's formula and the atanh logarithm series generate pi and logarithms rather than trusting floating libraries. A complex denominator must be enclosed away from zero before division. Python assertions are not used for acceptance, so optimized mode does not disable the checker.

## Not executed or established

No exhaustive repository audit, whole-repository test suite, Lean build, independent analytic proof review, all-height zero census, all-order phase certificate, or RH proof was performed. Normal/optimized runs share one producer implementation and are not independent numerical algorithms. A reviewer must separately examine the mathematical identities, domains and source imports.
