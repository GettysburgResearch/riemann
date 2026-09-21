# MHB32 execution and assurance boundary

## Mathematical status

All new infinite arguments are proposed proofs, requiring independent review.
The code does not prove the Müntz identity, the oscillatory symbol estimates,
the imported Patel–Yang theorem, an unbounded native gain, or RH.
A finite source/covariance calculation is not promoted to an all-scale result.

## Completed prior-publication verification

The MCB31 companion was extracted and its mathematical proof, checker,
arithmetic module, receipt, and tests matched their live GitHub blob identities
at `aaea3f9605a430600bea0189397d93ca315b5f98`. Publisher-only documentation
was intentionally reconciled upstream and is not represented as unchanged.
No re-upload of that already landed work was needed.

Fresh complete MCB31 reconstruction/receipt verification passed normally and
optimized, reproducing full report SHA-256
`825800dd0f0759d787944daa23fe6cb31e5df7275b23a418e3d961e238c3c4d9`.
Both 12-method MCB31 suites passed on this Linux host, including symlink
refusal. This does not rewrite the publisher's Windows permission error.

## New authoritative finite calculation

Run from this directory:

```
python -S -B check.py --check results.json
python -O -S -B check.py --check results.json
python -S -B test_check.py
python -O -S -B test_check.py
```

Both full default reconstructions and both 12-method suites passed, with no
skips. The ordinary and optimized reconstructed report has SHA-256
`9f34a2c4db6ac9a93cd5b55913fc92b84ccff1ca423cf01ccfd37e07a8c7b8d3`.
The final timed optimized run completed in 31.45 seconds on this host; this
is one observed run, not a performance guarantee.

Coverage is two complete native observation blocks: [128,255] and [512,1023],
640 cells in all, largest native endpoint 1023. All native Newton coefficients
through the respective endpoints are checked: 1278 comparisons counting
overlaps. Three and four successive smooth bands respectively are evaluated.
Their exact rational weights are differenced BEFORE independent band-shell
calculation. Every cross term between shells and the remaining complement is
retained (six and ten cross terms, respectively). The largest complete band is
also evaluated directly and compared against the sum of its shells.

The complement is obtained by exact subtraction from the fully checked native
output, NOT a second exhaustive summation over all unselected denominators.
All spectral modes retain their logarithmic centering constants. No future
native coefficient is an input to the short-source Newton producer; the
separate finite sieve intentionally computes them for cross-checking.

Other controls include 120 exact polynomial source/centering/difference
fixtures, the nonzero rank-one value 1/5, exact exponent identities, integer
roots and 32 outward rational-power controls, smooth-cutoff endpoint algebra,
and direct versus rotated elementary phases. Finite budget comparisons use a
LOWER rational enclosure for H^(191/82), not an upward-rounded value silently
substituted for the theorem's right side.

Each 12-method suite includes one pristine actual CLI acceptance and one
actual altered-report CLI refusal on the explicitly smaller quick corpus.
Type-alias, duplicate-key and symlink cases are separate in-process tests;
they are not claimed to be many full numerical subprocess campaigns.

## Arithmetic and the wider-band repair

The authoritative computations use exact Python integers/Fraction and the
SHA-locked inherited 144-bit outward elementary backend. No mpmath, zeta
oracle, sampled root table, machine-float quadrature or random signs enter
acceptance. The inherited backend and same-author implementations are not
independent mathematical validation.

An initial wider-band attempt used the old uninterrupted sine/cosine rotation.
At y=31, H=8, those valid intervals expanded enough to fail the finite budget
check. The failure was not hidden, reclassified as a pass, or used to change
the source. The new evaluator reseeds from exact rational phases every 32
steps, checks agreement, and intersects the two valid enclosures. Its final
bounds remain fully outward. The old module is preserved unchanged.

Some combined/short-budget orchestration attempts timed out before all their
commands completed. Completed separate runs, including the final timed
optimized reconstruction, supply the receipts above. No success is inferred
from an interrupted run. A request for an unsupported streaming container
session failed before running code and was replaced by ordinary execution.

## Optional scout, excluded from acceptance

`mellin_scout.py` was executed with mpmath at 25 decimal working digits and
limit 64. For the polynomial control it gave centered value approximately
0.05781247713719914777, compared with exact 37/640. Its analytic omitted-tail
ceiling is stated, but its finite quadrature error is UNKNOWN. It is an
ordinary numerical sanity check, NOT a Mellin integral certificate.
`mellin_scout.json` remains separately labelled and is not imported by the
accepting checker or tests.

## Environment, delivery and exclusions

Observed host: Linux, Python 3.13.5, GCC 14.2.0 build. The optional numerical
scout uses installed mpmath; no clean dependency installation was performed.

Source files, manifest, exact local Git subtree, add-only patch application,
and fresh-archive replay are checked again for publication; their final remote
commit/tree identities are recorded in the PR receipt rather than invented
in this file. A minimal local Git fixture is not a full Riemann checkout.

No full-repository validator, remote CI result, Lean build, Windows/macOS run,
complete old DSE27/NCG28/ATC29/NCL29 numerical campaign, independent referee
acceptance, new zero-free region, or full remaining-gap closure is claimed.
