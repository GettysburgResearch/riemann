# Validation and proof boundary

The delivered results are component PAPER proofs, plus bounded checks.
There is no arithmetic count power saving, new positive range, formal
proof build, independent referee acceptance or RH completion.

## Fresh executable work

The standard-library-only checker reconstructs 14 named groups of bounded
controls. There are 4,785 individual fixtures, of which 3,369 are elementary
rational exponent-iteration steps; these are not independent theorem counts.
Other groups cover the Mellin weight/reflection, affine pole residue factor,
exact bad-cell length bound, unit-cell background shift, and finite resonant
Fourier means. The prime-power sieve is compared with independent trial
factorization through 512.

Eleven native scalar values, m=2,...,12, use every prime power through 576.
They are small calibration fixtures, not new positive-range results. The
source constant C0 is freshly enclosed using rational Machin/atanh series
and the full elementary harmonic enclosure for Euler's constant. Its
nonzero harmonic error is not suppressed: the enclosure lies strictly
between 1/25 and 1/20. No zeta/gamma/zero oracle or floating-point arithmetic
enters these accepting calculations.

The normal and optimized isolated-interpreter executions reconstruct the
same result.json. Eight deliberate corruptions per mode exercise the actual
CLI after a successful pristine copy: false RH and power-saving claims,
Boolean count alias, duplicate JSON, re-sealed changed proof, changed parent,
omitted checksum entry and extra file. Semantic result mutations are
re-sealed to test reconstruction rather than merely hashes.

All eight manifest entries and the exact nine-file recursive inventory are
checked, with no symlinks allowed. The three mathematical parent manuscripts
are matched against hard-coded Git blob and SHA-256 identities before use;
no parent code is imported or executed. The source metadata is separate
from a claim of independent acceptance of the old proofs.

## Commands

From this directory, with the three parent proof paths present alongside it:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

A minimal-context Git patch roundtrip and clean archive extraction are used
for delivery validation. They preserve an unrelated sentinel and compare
all new bytes, then replay both modes. They are not a complete remote
checkout, remote CI run, or mathematical integration.

## What the checks cannot prove

They do not establish the unknown zero supremum, the all-K count saving,
Landau's analytic theorem, the infinite Hadamard/Laplace identities, or
almost-periodic recurrence. Those arguments are written out in PROOF.md.
The new conditional iteration cannot be interpreted as 100 computed
zero-free improvements: every step assumes the SAME unproved count bound.

The external literature check used parsed text and HTML as recorded in
SOURCES_AND_SYNTHESIS.md. Failed external PDF screenshot calls are not
claimed to be a successful visual paper audit. No external numerical
producer or full historical repository suite was rerun.

## Preparation interruption

An initial combined normal/optimized refusal invocation hit its orchestration
timeout after the normal run completed. That partial optimized run is not
counted. The optimized run was repeated separately and completed; final
sealed delivery replays are recorded separately. No mathematical assertion
was inferred from the interrupted process.
