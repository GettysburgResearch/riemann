# Execution, trust boundaries and delivery

Date: 2026-09-10. All new mathematical statements remain proposed pending independent review.

## Executed accepting arithmetic

Both commands reconstructed the complete retained exact-algebra receipt:

    python -I -S -B check.py --check checks.json
    python -I -S -B -O check.py --check checks.json

Fresh producer-mode output in both modes is byte-identical to checks.json. Producer mode is not itself acceptance. The checks cover complete finite Laplace numerator identities and all local pole coefficients for N=1,...,12, the corresponding boundary jets and moments through degree eight, every coefficient of the next gamma differential step, the specified finite tail-product identities, and the exact flow symbols. Finite products test the telescoping algebra; they do not replace the written infinite-tail argument.

The exact coverage record is:

```json
{
  "boundary_derivatives": 156,
  "cascade_coefficient_identities": 90,
  "continuous_flow_symbols": 80,
  "convolution_moments": 108,
  "density_cutoffs": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12
  ],
  "finite_tail_products": 96,
  "local_partial_fractions": 78,
  "normalizer_and_strip_constant_controls": 7
}
```

Six unittest methods passed in each Python mode, with no skips. They include one pristine actual CLI acceptance and twelve altered-receipt CLI refusals per mode. Duplicate keys, Boolean/integer and float/integer aliases, wrong arithmetic, reduced coverage, missing/extra fields and false proof-status flags reject. The tests also independently check the harmonic-number form of the density coefficients through N=20. Repeated runs and overlapping identities are not independent mathematical reviews or separate theorems.

The checker is Python standard-library only and uses exact integers/Fractions. It does not import an author module from another research packet. It verifies its bounded algebra, not the infinite analytic arguments, the Bessel theorem or RH. SHA256SUMS authenticates packet bytes when checked separately; check.py does not claim to authenticate the external literature or to validate every sentence of this manuscript.

## Exploratory calculation (not an accepting certificate)

    python -B scout.py --output scout.json

This completed with mpmath 1.3.0 at 90 decimal digits. The two N=4 defining-integral quadrature grids are one 160-node Gauss–Legendre rule and a 12-by-32 composite rule, each on [0,3]. The apparent nonreal roots differ by approximately 5.13e-53. Five selected first-real-root tracks also completed using the recorded grids/seeds. These are not zero censuses.

No outward primitive/rounding bounds or complete quadrature/Rouche count were assembled. The paper supplies an analytic tail envelope, but the numerical output is deliberately NOT a certified zero. Agreement between two grids sharing one arithmetic backend is not an independent numerical proof. Earlier exploratory Hankel and raw-Mellin scans informed the choice of target but are not used as evidence for a theorem here.

One initial scout execution failed because the broad real-root starting guesses did not converge at the requested tolerance. The code was changed to use explicit nearby scouting seeds; the subsequent full output completed. This was a numerical search adjustment, not a mathematical repair or a successful first execution.

## Source and repository boundaries

AGENTS.md was read. Main was read back at f99d9e3908dde4865377c75d9ca051c1f545bf4f. The six latest PR descriptions supplied orientation only, not a new review of their proofs. No theorem from those new branches is imported. A final PR #842 read found it had advanced to 8f1f457b0b92e76a0a75bd3d8a8921c205fa75b0 with connected/collective-limit work; only that updated description was read, and its new arguments are not imported. The Biane–Pitman–Yor representation and finite-Mellin-approximation context were read in the primary source, including the stated PDF images; the standard Bessel equations/asymptotics were checked in NIST DLMF. No exhaustive originality audit is claimed.

The current GitHub connector exposes read actions but no write actions. Plugin discovery found the existing GitHub connector, not a second available writer. An actual direct git ls-remote request failed with “Could not resolve host: github.com”. No remote research branch, PR, commit, main update or integration-candidate change is claimed.

## Delivery checks

The separate delivery receipt records the exact ten-file local subtree, hashes, clean-archive extraction and add-only patch roundtrip. Those are checks of local artifacts, not full repository checkout verification. The patch affects only standalone/2026-09-10-reciprocal-gamma-cascade/. It preserves unrelated/earlier source files in the temporary test repositories.

No complete repository build/validator, external zero computation, finite-parameter collision census, native Windows run, Lean proof, remote CI run or independent mathematical acceptance was performed. The spectral confinement target and any global real-rootedness of later approximants remain unproved.
