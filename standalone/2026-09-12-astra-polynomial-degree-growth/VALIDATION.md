# DG26 validation receipt and limits

Status: PROPOSED mathematical components; the required subpower estimate and
RH remain OPEN. Date: 2026-09-12. All numerical acceptance is integer/Fraction
arithmetic with explicit outward rounding. This is same-author computation,
not independent mathematical review or a proof-assistant verification.

## Repository publication versus executable companion

The repository publication has EIGHT non-executable files. It does not contain
check.py. The connector blocked that code upload with an indeterminate safety
status. No encoded, split, or alternate-endpoint upload of it was attempted.
The mathematics and receipt are published separately; the full nine-file local
packet is supplied to the user as a downloadable artifact.

The commands below describe actual executions in that COMPLETE companion,
not commands executable from this documentation-only directory. Its original
manifest remains inside the companion. This publication's MANIFEST.sha256
instead authenticates its own seven non-manifest files; the two manifests
are intentionally different and must not be substituted for each other.

Companion checker:

    Git blob bd791e9484114dbf29f0ab4e0eb03d5c2b069bcc
    SHA256 976a09a38717d819d252104980c57ce9cb47acb043dd62b0f2e11677aa5be2dc

The complete written PROOF.md is byte-identical in both versions:

    Git blob c68170e2dacd23c188c9e71482e51fe63566b587
    SHA256 94bb449b4ec654f946d1085816e709a2c68486439acad8b8e3a44a0ee9411504

## Actual protocol in the complete companion

    python -B check.py --write results.json --self-test
    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

The complete expected payload is reconstructed from primitive definitions
before comparison. A valid digest alone is never accepted. The check modes
authenticate all eight manifest entries and the exact nine-file inventory.
The published receipt uses 160-bit outward endpoints of calculations performed
at 768 bits. Exact large rationals are compared BEFORE the smaller receipt is
encoded. All bounds include every cross term.

Canonical semantic SHA256:

    aedd7a58cdca28340370d44eb92c2fe1556c11eaf3f5ecf8df37afe1beea6f2e

The full internal payload has semantic digest
`630b3708187e562ead88cb2942a7dd60b1d58dc12d1fe84e6053ad9955ee25a9`.
The published compact receipt keeps counts, group hashes and all six norm
enclosures. It is reconstructed from the FULL internal payload on every run,
not accepted from those hashes. Add `--detail /tmp/dg26-detail.json` to emit
the detailed canonical record; its copy is also in the downloadable bundle.

## Coverage

* 64 Legendre coefficient lists (degrees0--63) from the three-term recurrence
  versus the factorial Rodrigues formula; 528 exact odd orthogonality entries.
* 256 rational Mellin coefficient identities from direct monomial integration
  versus the closed product. These real test parameters are NOT zeta zeros.
* 2048 Mobius values by sieve versus independent trial factorization.
* 32 odd even-zeta enclosures via Machin pi/Bernoulli versus Euler--Maclaurin
  at N=128,K=64, with its full periodic-Bernoulli remainder. The former uses
  220 terms for atan(1/5) and80 for atan(1/239), with alternating tails.
* 16 reciprocal-even-zeta comparisons against literal Mobius sums through
  2048, with the ENTIRE remaining Dirichlet tail bounded absolutely. No zero
  input or unseen analytic continuation is used to generate these primitives.
* Complete 32-by-32 output Gram construction from all even-zeta multipliers
  and exact interval integration. Its first8-by-8 lower triangle (36 entries)
  is reconstructed by a separate output-polynomial integration route using
  the second primitive path. This is not two separate full-size matrix codes.
* Six native all-vector certificates Lambda_N<4 for N=1,2,4,8,16,32, with
  63 interval LDL pivots in total. Each also has a complete trace upper bound
  and an integer-vector Rayleigh lower bound. They are not exact eigenvalues.
* 80 Bernstein moment/variance controls and six synthetic proof-exponent
  balances. These check bounded algebra, not the infinite analytic theorem.

The checker has no third-party or parent-module imports. Its two primitive
calculations share Fraction arithmetic and Bernoulli coefficients, and have
one author. They must not be called independent mathematical reviews.

## Adversarial tests

Every --self-test first accepts a pristine regenerated record, then changes and
RESEALS twelve distinct payloads. Alterations include false RH/growth status,
source pin, working precision, missing degree case, altered bound, changed
probe digest, changed native-primitive group digest, Boolean alias, enlarged degree scope,
wrong exponent-group count, and a changed entire-tail group digest. All must be refused by the
same acceptance function. A duplicate-key JSON control is also refused.
These are twelve calls to the acceptance function per mode, not twelve
separately launched CLI processes or twelve independent theorem reviews.

## Development history retained

A noncertifying mpmath scout at 150 decimal digits selected the integer
Rayleigh vectors and inspected dimensions through32. Its first displayed
maximum used an invalid negative-index convention and printed zero; correcting
the index exposed the actual values. That scouting output is not an input to
acceptance. Only the resulting explicit integer vectors are retained, and
all their Rayleigh inequalities are reconstructed by directed arithmetic.

The first exact run unnecessarily required one outward upper endpoint to
lie below another upper endpoint at N=1, where the true quantities are equal.
It correctly refused that overstrong interval comparison. The final checks
compare a genuine Rayleigh LOWER bound to the trace upper bound, and prove
both are below4. The original mathematical interval enclosures were not
changed to pass that test.

The next development run exceeded Python's integer-to-string limit because
an exact Mobius partial sum was serialized with its huge denominator. The
final calculation retains that exact rational internally, checks its entire
tail comparison, and emits its outward interval instead. No language guard
was disabled and no floating value replaced the rational calculation.

## Scope of fresh replay and publication

The complete companion addition-only patch is applied to a fresh local Git fixture containing
an unrelated sentinel. Every added file is compared byte-for-byte with the
tested packet; the sentinel is preserved. A clean ZIP extraction is also
replayed. These are packet fixtures, NOT a full authenticated repository
checkout. Direct git ls-remote failed DNS in this session. Connector publication
does not constitute a repository-wide validator run.

Not executed: whole-repository scientific audit, full tools validator, Lean or
other proof assistant, parent accepting suites, other agents' numerical
campaigns, actual zeta-zero computation, complex contour integration, Windows
execution, remote CI certification, or any unbounded degree experiment.

The written proofs, including cutoff limits, complex analytic continuation,
classical RH-to-Mertens input, and critical-zero existence, need mathematical
review. No finite certificate proves the OPEN subpower upper bound.
