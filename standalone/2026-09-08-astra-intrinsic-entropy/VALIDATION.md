# IE26 validation and execution boundary

This is bounded author verification, not independent mathematical acceptance.
No finite result proves J=0, RH, or the requested growing-horizon theorem.

## What is reconstructed

`check.py` reconstructs 86 bounded algebraic CASES in five named groups:
39 sharp real-Blaschke sensitivity cases; 15 single-node projection cases;
12 finite synthetic Toeplitz matrices; 12 explicitly synthetic strip-qualified
conjugate pairs; and eight equal-Gram/different-normalization cases. Case counts
are not counts of independent analytic theorems. The positive phase correction
in the strip decomposition is checked with exact rationals and directed logs.

A separate actual-source certificate integrates exactly 2047 integer cells
through x=2048, retaining all primitive filter states and the whole infinite
tail. These cells are COVERAGE UNITS, not 2047 independent theorem proofs.
The source is the literal factorial g, and the target is exp(-t/2) of norm one.
The rational trial has degree six. Its complete squared error lies between
0.047034408869 and 0.051343069499 and is therefore below13/250. The analytic
identity delta=1-exp(-2J) implies 0<=J<27/1000. The positive lower endpoint
for this trial error is not a lower bound for delta or for J.

All accepting arithmetic is integer, Fraction or 160-bit outward dyadic.
Logarithms use range-reduced atanh series with an explicit remainder; pi uses
Machin arctangents with alternating-series remainders. Polynomial integrals use
exact moment recurrences. Neither numerical quadrature nor float comparisons
enter acceptance. The shared interval core is copied from FR26 and authenticated
by SHA256, Git blob and byte count before direct byte compilation.

## Commands

From this directory:

```bash
python -B check.py
python -B -O check.py
python -B test_check.py
python -B -O test_check.py
```

The ordinary and optimized replays are required to reconstruct byte-identical
verification.json. Four unit methods include one pristine copied-packet CLI
run and twelve distinct corrupted-packet refusals in EACH mode. Five altered
semantic results are resealed, so rejection exercises primitive reconstruction
rather than only the checksum: false RH flag, target substitution, wrong energy
endpoint, boolean degree alias, and missing synthetic case. Other cases cover
duplicate JSON, float alias, empty manifest, extra file, symlink core, changed
executable core and source-lock drift. Acceptance does not use assert.

The fixed eleven-file inventory and exact ten-entry manifest are enforced.
Local cache directories are not permitted in the authenticated payload; run
with -B as shown. The manifest detects changed bytes but is not a mathematical
proof. Remote commit identity and the frozen copied-core identity provide
independent publication/source binding; self-consistent hashes alone do not.

## Discovery and provenance limits

A separate, NON-DIRECTED NumPy/SciPy calculation selected rational trial
coefficients, using finite degree16 and integer cells through4096 with an
approximate smooth tail. Its approximate Grams and energies are NOT proof
inputs or accepted outcomes. The new directed certificate independently reads
the fixed rational trial, literal source and analytic tail contract. No random
search, prime/zeta-zero campaign or high-rank source computation was performed.

The HC26 rate is an explicitly inherited PAPER dependency. Its source proof was
read and its local Git identity matches the live #817 inventory; no parent
Python, tests, or full proof audit is counted as executed here. No PNT/Mertens
estimate or numerical zero-height verification is used by the new certificate.
Classical BSY/Hardy/Szego claims are reconstructed analytically and attributed;
no formal kernel verification of those arguments occurred.

## Delivery boundary

The new directory is add-only. Parent branches, previous research files,
canonical/formal sources, workflows and repository permissions/settings are not
changed. A clean ZIP replay and temporary-Git patch roundtrip are delivery
checks, not a full repository checkout/build or remote CI result. Publication
receipts outside this mathematical payload record the final commit and actual
commands. No Windows execution, Lean build, independent referee acceptance,
new zero-free range, exact intrinsic zero, or complete RH proof is claimed.

## Interrupted runs and completed replacements

The first combined invocation completed both replay modes but timed out during
the normal test suite; that partial suite is not counted. A standalone normal
run then completed all four methods successfully. A later full optimized test
invocation timed out and is likewise not counted. Two explicit optimized
partitions subsequently completed all four methods and all twelve refusals:

```bash
python -B -O -m unittest test_check.Tests.test_result_corruptions test_check.Tests.test_rational_threshold
python -B -O -m unittest test_check.Tests.test_parser_and_inventory test_check.Tests.test_pristine
```

The timeouts were execution-envelope limits, not reported PASS results. No
mathematical outcome is inferred from the interrupted commands.
