# AC27 validation and evidence boundary

**PROPOSED mathematics, independent review pending. No proof of RH.**
Date: 2026-09-10. Parent: PR845 at
`be78f076b9abe8d8d6a40c14f71d0df36a4e0407`.

## Exact source identity

The parent proof was read from the supplied archive/local file and its live
pinned GitHub source. Its 17,112 bytes match Git blob
`822f24c624af00675ee42795d9354eecc6c2349b`; its SHA-256 is in SOURCES.json.
Main was read at `f99d9e3908dde4865377c75d9ca051c1f545bf4f` and the parent PR
was open, draft and unmerged. No discussion comments were returned at capture.
No parent proof, source, artifact or previous status is edited by this packet.

## Finite computations actually completed

The complete mathematical payload was regenerated normally, with -O, and
with -OO. All three agree byte-for-byte and reject ten distinct resealed
corruptions per self-test, after pristine acceptance. The entry point uses
explicit exceptions, not assertions removed by optimized Python.

    python -B check.py --write /tmp/ac27.json --self-test
    python -O -B check.py --write /tmp/ac27-O.json --self-test
    python -OO -B check.py --write /tmp/ac27-OO.json --self-test

The publication replay uses the nonwriting, manifest-authenticating commands:

    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

The semantic digest is

    8db1e2fff6b17b26ae432d115ce59576cd5fd7d3a0ee45b01b8528ed078473e0

The code reconstructs:

| Object | Finite coverage |
|---|---:|
| Sieve versus trial-factorized Mobius values | 729 |
| Native inverse entries, divisor recursion versus harmonic sums | 49,460 |
| Odd divisor positions for derivative/sign checks, including zero entries | 1,484 |
| Finite derivative traces with the declared analytic tail control | 6 |
| Exact mean-row entries, with rational endpoint Q values | 179 |
| Native mean-probe lower certificates | 12 |
| Complete positive matrix certificates | 5 |
| Positive leading principal minors in those matrices | 80 |
| Exact activation-strip sample positions | 1,180 |
| Actual threshold changes among them | 524 |
| Algebraic multiplicity-cost controls (NOT zeta zeros) | 6 |
| Inherited nonnative control substitutions | 8 |

The five matrix certificates are the four A=81 band blocks with C=3/5,
eta=1/100, and the complete A=81 matrix with C=1. Rational LDL pivots are
checked against independently computed fraction-free integer leading
principal determinants. All-vector positivity follows in these exact finite
dimensions; it is not an all-A theorem.

The complete expected JSON is recomputed from primitive definitions. Raw
large exact fractions are first used for the mathematical comparisons, then
encoded by outward rational enclosures [lo/2^48,hi/2^48] and exact-object
hashes. No floating value is a certificate input. Floats, nonfinite values,
duplicate JSON keys, unexpected envelope keys and an incorrect full payload
are rejected. The manifest binds precisely seven filenames; symlinks and
missing/duplicate entries are refused.

Self-tests mutate the source head, primitive counts, inverse coverage,
activation coverage, claimed status, band constant, combined ratio, mean-probe
lower bound, trace list, and OPEN target status. The payloads are resealed so
the mathematical comparison, not just their hash, must reject them. These
are ten calls of the exact acceptance function per mode, not thirty separately
launched CLI corruption processes. Same-author alternative implementations
are not independent mathematical peer review.

## Development and exclusions

A combined optimized/fully-optimized publication batch reported both PASS
lines but its container call hit the combined timeout. That batch is not
counted as a completed execution; the modes were rerun in separate calls.

Uncertified floating eigenvalue reconnaissance at A=81,243,729,2187 was used
to choose the A=81 rational forcing test. It is not stored as proof evidence
or extrapolated to larger cutoffs. The final exact report representation was
compressed from raw fractions to rational intervals/hashes without weakening
any underlying comparison; intermediate development digests are not retained
as canonical versions.

The analytic global Hilbert--Schmidt trace uses the written Euler-product
argument and classical zeta values. The unbounded native transmission and
constant-cost conclusions use the written Laplace arguments, not a large
finite norm calculation. The grid error bound is proved for all cells in the
manuscript; the 1,180 samples only exercise its finite boundary semantics.
No actual zeta zero, numerical contour integral, high-zero table, arithmetic
prime-distribution estimate, or infinite zero expansion was evaluated.

No full authenticated repository checkout was obtained, and no repository-wide
validator or proof assistant was run. Connector publication and a complete
packet replay are not a full-tree validation. External primary pages were
inspected at the levels specified in SOURCES.json; no third-party paper or
binary payload is redistributed. The final remote commit/PR identity and
addition-only comparison belong to the publication receipt.
