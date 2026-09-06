# Execution and assurance record — Reviewer D closeout

## What was actually executed

The new `checks.py` was independently written from the displayed identities.
It imports Python's standard library and SymPy, not an upstream source
producer or the first-pass checker. Environment: Python 3.13.5, SymPy 1.14.0.

```
python -B checks.py > checks.normal.json
python -O -B checks.py > checks.optimized.json
cmp checks.normal.json checks.optimized.json
python -B checks.py --check checks.normal.json
python -O -B checks.py --check checks.optimized.json
python -B validate.py
python -O -B validate.py
```

There are **35 named checks / 26,407 bounded fixtures** per mode. A fixture
count records a declared finite input or identity instance, not each internal
assertion. 21,613 fixtures are the simple finite Vaughan parabolic-support
inequality; they are not 21,613 new mathematical claims. The named checks are
fully listed in the JSON output.

The arithmetic class is exact integer/rational, Gaussian-rational or symbolic
algebraic arithmetic. SymPy is trusted for symbolic integration/simplification
and finite factorization. The Gaussian integrations check normalization only;
they are not a numerical certification of a full explicit formula. No zeta
value or large prime sum is evaluated. No actual xi box or zero verification
is rerun. No floating point value is used as an acceptance condition.

Acceptance uses explicit `require` exceptions, not Python `assert`. The JSON
reader rejects duplicate keys, floating values and nonfinite constants. Its
recursive comparison distinguishes booleans from integers. Normal and
optimized outputs are byte-identical.

## Corruption tests

`rejections.py` reconstructs the full expected mathematical result once per
mode, then calls the same parser and strict comparator used by `--check` on
eight corrupted records: count, Farkas sign, missing check, boolean/integer
alias, floating/integer alias, duplicate key, nonfinite constant, and an
RH-proof status promotion. All eight are rejected in each mode. This is an
in-process test of the acceptance path, not sixteen separate full upstream
production runs. The records are in `rejections.json`.

An independent outer harness copies the two review directories to a temporary
location and invokes `validate.py` in a separate normal or optimized Python
process after each of four mutations: changed new report, changed old report,
extra unlisted file, and missing claim table. All eight subprocess attempts
fail as intended. Results are in `package_rejections.json`. The outer harness
only changes temporary copies and is not a source or theorem producer.

## First-pass preservation and replay

In this closeout run the original checker was rerun from the original ZIP:

```
cd ../D
python -B checks.py --check checks.normal.json
python -O -B checks.py --check checks.optimized.json
python -B validate.py
```

Both reconstructed **45 named checks / 9,380 fixtures** and passed. The original
validator authenticated its tables, files and retained rejection records.
The original rejection CLI suite was NOT freshly executed here; its stored
records remain part of the unchanged first-pass packet.

The original manifest SHA-256 is pinned in the new validator:

```
99c1b6bacfc8bff9e433cc3065d01655d7f473a4cfc6ac89e5334396a92f8ac0
```

The new validator checks all fifteen old manifest entries and the exact old
sixteen-file set before checking its own fifteen hashes/sixteen files. The
original code and prose are not overwritten. The new table/source validator
checks record identities and scope, not the correctness of upstream proofs
or remote source bytes.

## Authoring corrections and execution limits

An initial local authoring run failed with a SyntaxError in an unused draft
expression. That expression was removed; it produced no retained passing
result. The final script is the one whose checksum and Git blob are published.
A strict type-comparison guard was then added and tested against boolean and
floating aliases before final publication. No failed result is counted as a
passing mathematical check.

These computations do not machine-prove Farkas over every real system,
Hardy Paley–Wiener, Borel–Carathéodory, the three-lines theorem, classical
zeta growth, Dickman/VK estimates, completed-source identities or infinite
trace-norm limits. Those are mathematical proofs or explicitly imported
inputs as identified in the report. No Lean, Comparator, Nanoda, remote CI,
repository-wide campaign, primary cardinal construction, complete historical
census or full source-tree replay is claimed.

## Publication

The commit must add only this sibling `reviews/D-final/` directory on PR #799's
review branch. The direct parent is the verified first D head
`55a7371432760ff44d396f6e63d95d65e64ad2a5`. The final commit and Git tree IDs,
remote comparison, and transport ZIP hash are placed in the publication
receipt outside the committed packet to avoid a self-referential checksum.
