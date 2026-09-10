# Execution contract and boundaries

The new verifier uses Python's standard library only. Algebra is exact rational
arithmetic in formal prime-log variables. Clearing log(2) denominators lets the
two jets, squared coefficients, convolution formulas and null directions be
checked without floating-point equality. Ordinary logarithms are separately
enclosed using range-reduced atanh series with explicit tails and outward
144-bit dyadics. Prime logs are formal algebra variables, not an assertion
that they are algebraically independent.

The reconstructed result has 1,055 bounded checks in 13 named groups. These
include 512 independent sieve-versus-trial-factor comparisons, 231 proxy
coefficient equalities, 46 jet checks, and small norm, harmonic, lattice and
source checks. These counts are finite fixtures, not distinct infinite
mathematical theorems. The largest native scalar fixture is m=5, with all
prime powers through 100; the proxy support fixtures reach n=128. The
Möbius/trial-factor comparison reaches 512. Correction constants are enclosed
for Y=2,...,24, not for an unbounded range by computation. The all-Y results
have analytic proofs in PROOF.md.

Final commands:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

Both verification modes reconstruct the same mathematical JSON. Each rejection
driver first accepts a pristine copy, then runs eight actual CLI corruptions:
false RH status, false count-saving status, Boolean alias for an integer count,
duplicate JSON, changed proof bytes, altered authenticated parent, extra file,
and missing checksum. Semantic JSON mutations are resealed so the result
comparison rather than merely the file checksum must reject them. Proof-file
mutation tests integrity, not machine verification of its analytic contents.

The exact eight-file inventory and seven-entry manifest are checked, as is the
consumed parent manuscript at Git blob
046a12cd9233aa7d8a9a3a5d4d4c64a67d4207be and SHA-256
036e9d3d7b429e9ac8d850e81910c53addfa1d9654050732cfc3dc8bcc4e47c7.
No parent code is executed. The local parent file was supplied in the
conversation and its identities agree with the published source tree at the
verified PR head. A full repository checkout is not claimed.

The delivery contains an add-only patch and the authenticated parent proof as
minimal replay context. The patch roundtrip is tested in a temporary Git
repository, preserves an unrelated sentinel, and reproduces the packet bytes.
That is not a full repository build or remote CI execution.

No numerical zeta value, derivative, zero ordinate, or critical-line contour is
computed. The classical convexity bound, operator mean-value argument, infinite
contour passage, asymptotic Riemann sums, and all-scale Möbius estimates are
paper proofs or explicitly named analytic dependencies, not finite-test
conclusions. Their constants have not been turned into a certified numerical
contour engine. No new positive range, failure-count upper bound, RH proof,
formal build, external producer replay, or independent referee acceptance is
claimed. The mathematical completion achieved is the bounded-coefficient
source and high-frequency tail, not the remaining low-frequency signed bound.
