# AC28 validation and publication boundary

Status: author computation supporting PROPOSED component proofs. This is not
independent mathematical review, a proof of all-degree positivity, or RH.
Parent: `e6dbb8ef4e458ea4c8d1b17ced77ec28905a7472`.

## Reproduction contract

From the repository root, set

    P=standalone/2026-09-10-astra-safe-source-kernel
    python -B "$P/check.py" --check "$P/results.json" --self-test
    python -O -B "$P/check.py" --check "$P/results.json" --self-test
    python -OO -B "$P/check.py" --check "$P/results.json" --self-test

The expected semantic SHA-256 is

    bb08ee376fd6b8e42db4c802efd999970889343ffec46cef5b2811798d7b5fd1

All three commands completed successfully during finalization. A separate
fresh-directory application of the addition-only patch, manifest check, and
normal/optimized replay also passed. The publication receipt records the new
commit and Git identities; a local fixture is not a complete checkout.

The seven named source/result files must match MANIFEST.sha256 before a
--check run. --write is a generator operation and does not authenticate an
existing package. The check always reconstructs the ENTIRE expected payload
from finite primitive definitions and compares it, not just the digest.
Floats, nonfinite JSON numbers, duplicate keys, Boolean/integer aliases, and
mismatched schema fields cannot satisfy the strict comparison. Assertions
are not used for acceptance, so optimization does not remove checks.

## Finite native certificates

Safe sample nodes are z_k=2k-1/2, k=1,...,8. The eight matrices have dimensions
2,4,6,8 at eta=0 and eta=1/100, all with C=1. Every matrix retains every
mixed source term. The exact unknown real values Z(2k) are bounded by two
independently structured interval paths:

1. Machin pi: 16 arctan(1/5)-4 arctan(1/239), alternating-series brackets
   at 100 and 50 terms respectively; the exact Bernoulli recurrence and
   classical even-zeta formula then give outward enclosures.
2. A rational Euler--Maclaurin sum at N=64 through B_48. Its ENTIRE omitted
   periodic-Bernoulli remainder is bounded, not estimated by an asymptotic
   guess. The Fourier bound |B_48({x})|<=|B_48| gives a remainder at most
   |B_48|(s)_47 N^(-s-47)/48!, the magnitude of the last displayed term.

Every interval operation rounds outward to a 256-bit dyadic lattice. There
is no floating point in the checker. The two source paths' intervals overlap.
One matrix path integrates the closed exponential formula and certifies all
40 LDL pivots; the other expands x=exp(r/2) into powers and certifies all
40 leading principal minors by interval fraction-free elimination. Each
corresponding matrix enclosure overlaps. These certify eight complete finite
Loewner inequalities, not 80 different operator inequalities.

Sixteen additional coefficient vectors reconstruct the fixed-interval
polynomial quadratic directly and compare it with the kernel form. They also
check the noncritical unweighted derivative inequality. These bounded controls
do not establish the all-degree polynomial theorem's OPEN estimate.

## Exact negative and model controls

At eta=1/100,C=1 the complete finite-prime controls give:

| Odd prime set | Dimension | Exact determinant |
|---|---:|---|
| empty | 1 | -199/300 |
| {3} | 2 | -275075489/336000000 |
| {3,5} | 2 | -249029326809149/930349056000000 |
| {3,5,7} | 3 | -539929624902919658426743886175138867881/10745363314905868754097231259238400000000 |

These are NONNATIVE Euler truncations, not alleged zeta counterexamples.
Nine rational one-pole marginal controls use horizon values 1,2,3/2, not a
numerical substitution for log3. They test the sharp sum-of-squares cost and
failure after lowering C. Eight rational multiplicity optimizations do not
use any actual zeta zero. The analytic all-parameter proofs are separate.

Each self-test first accepts the pristine regenerated record, then alters
TEN distinct payloads and recomputes their digests. All ten are rejected
through the exact acceptance function. These are NOT ten separately launched
CLI processes. Mutations include a false RH flag, precision, coverage,
source parent, scope, native pivot, Euler sign, and model constants.

## Development and evidence limits

Nondirected mpmath scouting at 70 decimal digits examined native matrices up
to dimension 12 only to choose the final test sizes and constants. None of
its eigenvalues is certificate data. The final protocol uses the directed
source enclosures above; no numerical contour or zeta-zero computation occurs.

A first generator run succeeded before the polynomial controls were added;
its digest was superseded, not counted as the final protocol. The final
--write plus self-test produced the digest above. No timed-out or incomplete
execution is counted as a passed replay.

Both source and matrix paths were written by the same author. Implementation
agreement does not replace an independent referee. The following need direct
mathematical review: weighted input-domain passage, feature-map continuation,
Blaschke uniqueness for the unbounded even-zeta nodes, zero/pole cancellation,
the exact polynomial isometry, and the distinction between weighted and
unweighted derivative estimates. None is machine-proved by the finite checks.

Direct `git ls-remote` failed with `Could not resolve host: github.com`.
GitHub connector reads/writes are distinct from an authenticated complete
checkout. No repository-wide validator, external formalization, Lean build,
remote CI success, prior experiment replay, or mathematical status promotion
is claimed. The new commit adds only this packet and preserves parent bytes.
