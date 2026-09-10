# Validation and evidence limits

**All mathematical claims remain PROPOSED pending independent review.**
The complete expected finite payload is reconstructed from primitive divisor
relations, not accepted merely because a submitted digest is self-consistent.
These bounded checks do not prove Q-AC26 or RH.

## Scope and independent implementations within the checker

For each odd exclusive endpoint X=3,5,9,17,33,65,129:

- Construct B_X directly from divisibility and differences.
- Independently invert it by rational triangular elimination and by the
  Mobius formula using trial factorization. Compare all entries and both
  matrix products with the identity.
- Reconstruct the incidence matrix from finite prime-shift geometric factors.
- Integrate the literal piecewise constant m exactly, compare the complete
  first-column and trace identities, and check the harmonic upper bound.
- Prove 4 B_X^*B_X-I positive definite by positive leading determinants.

At A=3,9,27,81, reconstruct the complete matrix through 3A, retain both old/new
blocks, and check the exact block inverse. For each eta=1/10 and 1/100,
C=1, certify the entire Loewner matrix from PROOF.md (4.4). Clearing a common
rational denominator yields an integer matrix. Its leading principal
minors are computed by fraction-free Bareiss elimination and compared to
an independently written rational LDL calculation. Positive definiteness
therefore applies to every complex vector in the declared finite dimension,
not only sampled vectors or the native source.

The uniform estimate for the fresh-shell block is also recomputed exactly.
For q=2,4,8, finite Hilbert--Schmidt norms check the high-relative-forcing
estimate; the universal claim rests on its written proof.

The nonnative control kernel is checked by divisor convolution on every odd
n<=729 and by its complete first-column equations at A=3^r, r=1,...,7.
Its energies and the lower bounds on C_eta are rational identities. It is
explicitly labeled synthetic and not passed off as the zeta source.

## Exact coverage

| Category | Declared coverage |
|---|---:|
| Native inverse entries compared | 5,461 |
| Finite prime-factor applications across the native cutoffs | 66 |
| Native coercivity certificates | 7 |
| Complete shell block reconstructions | 4 |
| Full-vector shell Loewner certificates | 8 |
| Positive leading principal minors, across both groups | 243 |
| High-relative-forcing checks | 12 |
| Synthetic divisor-inverse equations | 365 |
| Synthetic first-column source equations | 1,636 |
| Distinct resealed semantic corruption rejections per self-test | 10 |

Prime-factor applications are counted with their separate cutoffs; 66 is not
a count of distinct primes. Every finite cutoff and full coverage field is
included in results.json. This is a bounded protocol, not a certificate for
all future cutoffs or all eta.

## Commands actually completed

From this packet directory, each of the following completed successfully:

    python -B check.py --write results.json --self-test
    python -B check.py --check results.json --self-test
    python -O -B check.py --check results.json --self-test
    python -OO -B check.py --check results.json --self-test

All produced the same semantic digest:

    76d57ea6088254a5f3a03286850c2d904f1e9226b2e60a5d09e5b0bd4f899b72

The self-test first accepts a pristine regenerated report, then changes ten
different semantic fields and reseals each modified report. Every altered
record is rejected by the same accept function. These are direct acceptance-
path tests, not ten separate subprocess runs. The parser additionally rejects
floating values, nonfinite constants, duplicate keys and report symlinks.
Complete primitive-payload byte serialization is compared, so a Boolean
cannot replace an integer merely through Python equality. Predicates use
explicit exceptions and remain active under optimization.

The checker imports no previous research module, generator, zero table or
repository tool. Both algorithmic paths have the SAME author. Their agreement
is an implementation cross-check, not independent mathematical peer review.

## Disclosed development failures and exploratory work

The first generation attempt exceeded Python's 4,300-decimal-digit conversion
limit when hashing large exact principal determinants. It was not a passing
run. The final program hashes those determinants as positive hexadecimal
strings, explicitly labels this encoding, and leaves the interpreter's input
integer limit intact. The exact integer calculations were not replaced by
floating approximations.

An attempted combined normal/optimized/dual-optimized run hit the command
budget after completing only its first invocation. The unfinished invocations
were not counted. Each later separated command completed as listed above.

Exploratory floating eigensolver calculations were used to choose small
candidate constants and cutoffs for the exact tests. No floating eigenvalue,
fitted trend, or guessed asymptotic is an acceptance input. All published
finite inequalities are reconstructed with integer/rational arithmetic.

## Integrity and publication boundaries

MANIFEST.sha256 pins the seven other files; it does not hash itself. New
files are confined to this standalone packet. The publication commit and PR
supply the immutable new head and parent; source heads are in SOURCES.json.
A fresh addition-only patch replay is recorded in the external publication
receipt rather than being confused with a full repository checkout.

The repository was read through the connected GitHub interface. No complete
authenticated checkout, repository-wide validator run, remote CI result,
formal proof assistant, analytic integral evaluation or zero census is
claimed. No third-party PDF was successfully inspected in this pass; the
matrix prior-art source was read as author-uploaded HTML and bibliographic
metadata. Nothing in these tests closes the all-scale arithmetic estimate.
