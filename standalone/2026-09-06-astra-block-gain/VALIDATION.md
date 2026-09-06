# Validation contract and executed bounded replays

**Scientific scope:** exact rational controls and directed enclosures of
fixed full infinite Gram problems. BG26.G and RH are not proved. The
all-scale detail argument is a prose proof requiring independent review,
not a conclusion of the finite tests.

## Primitive source and arithmetic

The primitive source is `h_k(n)=(n mod k)/k`, with weight `1/[n(n+1)]`.
The selected parent functions reconstruct the full infinite Gram, using
period `lcm(j,k)` and a finite digamma-difference expression. Their outward
rounding, Bernoulli remainder, logarithm series and Machin pi enclosure
are documented in the unchanged parent NUMERICS.md. Dyadic endpoints are
integers divided by `2^224`. No floating-point value enters acceptance.
Every interval solve refuses nonpositive or zero-containing pivots.
All reported scalar/coefficient widths must be below `10^-24`.

Four parent files are SHA-256 authenticated before parent code is loaded.
The two consumed Python modules are compiled directly from those acquired
bytes; parent bytecode caches are not trusted.
The new checker uses only selected parent interval/Gram/projection
functions; the separate whole-parent replay is identified below. A
selected-function replay is not mislabeled as a fresh audit of every
parent theorem or of the broader repository.

## Fixed coverage

The exact checker reconstructs 7,234 finite controls: independent Mobius
values through 192, Jordan divisor identities, 48 finite-support weighted
Haar vectors, literal generator differences, all odd-divisor Gram
factorizations through 31, two formulas for the optimizer, literal coarse-source and signed-normalization identities, complete
parity source reconstruction through index 16, and bounded checks of the
squarefree-count constants. These counts are acceptance checks, not a
count of independently proved infinite theorems.

There are 92 directed acceptance checks for the three fixed stages
`N=2,4,8`. Original infinite-Gram projections are compared against the
lossless parity recursion and against the completed-square adjustment.
The two-channel lower bound retains every odd birth, including 9 and 15.
The actual `8 -> 16` detail-lift failure, increasing coarse penalty and
nonzero nonsquarefree full coefficient are decided by strict intervals.
No larger Gram stage is accepted by the public interface.

## Commands

Run from this sibling packet directory:

```bash
python3 -I -S scripts/replay.py --check
python3 -I -S -O scripts/replay.py --check
python3 -I -S scripts/test_replay.py
python3 -I -S -O scripts/test_replay.py
```

The new script's `--write` mode constructs verification.json for authors;
`--check` redoes the mathematics and compares the entire canonical object.
The checksum inventory must equal eight explicit paths. Empty, unknown,
duplicate and unsafe inventories are refused. POSIX-relative serialization
avoids the parent's separately documented Windows-path defect. No actual
Windows run is claimed.

The unit suite contains eleven tests, including nine actual subprocess
corruption refusals in each interpreter mode. The cases cover a false RH
flag, false full-gain flag, float alias, duplicate JSON key, omitted index
9, changed scalar endpoint, changed proof bytes, changed parent source and
an empty inventory. Changed semantic fixtures are resealed where needed
so the mathematical/configuration checks are exercised beyond checksums.
Ordinary and optimized execution must give identical verification bytes.

The unchanged parent's `scripts/replay.py --check` is also run separately
in both modes. This repeats its 14,073 bounded controls but not an
independent analytic proof or the old Windows adaptation. No parent file
is edited. The separate parent unit/CLI suites are not counted as new
executions in this continuation.

## Explicitly unperformed

No unbounded gain estimate, cofinal overshoot theorem, zero census, prime
scan, RH proof, independent-kernel build, new Lean theorem, repository-wide
CI campaign, or independent referee acceptance. We do not infer a global
inequality from three positive finite ratios. Publication readback verifies
bytes and branch placement, not scientific validity.

Full command stdout/stderr, return codes and the resulting verification
hash are retained in the downloadable execution receipt. The proof/source
packet itself contains no machine-specific filesystem paths or transient
GitHub download tokens. Reproduction requires the exact sibling parent;
a source export omitting it is deliberately refused.
