# Frozen implementation audit: rational-rotation positive-real exact degree

Status: **frozen replay passed; non-conclusion-bearing input-guard and metadata
repairs**.

Audited source: `ae15f136dda168eb052665c9c5493df65d47cda3`.
Source baseline: `3fd6c34d1cd8109eab3622d3966e05a0ad8fc7a4`.
Scope: the new exact-degree producer, fixture, source manifest, and tests,
plus adjacent rational-rotation uniform-degree and branch-census regressions.
This is an implementation/source/cap audit, not a replacement for the
separate mathematical review or a prior-art audit.

## Findings and repairs

At the audited SHA, `divide_monic` trimmed trailing zero-valued coefficients
before checking their types. Thus `divide_monic((1, 0.0), (1,))`, or a trailing
`False` in either polynomial, was accepted despite the exact-integer contract.
The canonical census constructs integer coefficients internally, so this did
not invalidate its results or the analytic theorem. The repair validates every
raw coefficient before trimming; regressions reject Boolean, floating, and
Fraction zeros in either polynomial while retaining valid integer zero padding.
The repaired producer/tests/fixture receive a new Git identity; the audited
past is not retrospectively described as containing the repair.

The audited producer also declared the noncanonical arithmetic class `EXACT`.
`CONTRIBUTING.md` and `canonical/provenance.schema.json` permit `MIXED`,
`EXACT_RATIONAL`, and `CERTIFIED_INTEGER_COVERAGE`, but not `EXACT`. The repair
uses `MIXED` with the latter two components: exact integer-polynomial coefficient
arithmetic and certified finite census coverage. The cyclotomic quotient domain
is explicitly retained. This is a metadata correction, not a change in arithmetic.

## Frozen authentication and replay

- A fresh checkout of the audited SHA passed the producer under normal Python
  and `-O`, all 14 new tests, and all 32 combined tests including the two adjacent
  packets, in both modes.
- The source manifest is pinned by LF-normalized SHA-256 before parsing. Its
  two source rows are matched to exact Git objects, LF-normalized blob content,
  and current worktree content. The complete CLI fixture is compared as canonical
  serialized text, so JSON Boolean/integer substitution cannot pass.
- The fresh checkout replay passed. An added hostile regression substitutes
  CRLF bytes for every file hash read and verifies the complete reconstructed
  fixture stays identical. No changed-source or missing-source exception is
  suppressed.
- The maximal allowed census, `b<=24`, integer exponent `k<=12`, and sign
  denominator `b<=64`, passed: 276 integer-spectrum rows and 1024 sign rows.
  Its declared work bound is 4,876,848, strictly below the exclusive 10,000,000
  cap. The bound covers 218,642 cyclotomic coefficient updates, 440,910 grouped
  binomial additions, 4,195,440 mode-division coefficient updates, and 21,856
  sign evaluations. These are named-loop bounds, not RAM/bit-complexity bounds.
  A separate cold-cache line-instrumented maximal replay counted 19,335 actual
  cyclotomic coefficient updates, 1,451,930 mode-division coefficient updates,
  440,910 grouped additions, and 21,856 sign evaluations, each within its bound.
- No source-data authentication bypass or mathematical regression was found.
  The source/producer/runtime itself remains part of the trusted computing
  base; this is not a sandbox against malicious Python execution.

After the repairs, both producer modes, all 16 new tests and all 34 combined
tests in both modes, the maximal census, Ruff, and `git diff --check` passed.
The fixture's census hashes and work figures are unchanged; only the arithmetic
taxonomy, artifact hashes, and payload hash change.

## Remaining boundary

The finite exact cyclotomic census checks positive integer exponents. The
all-positive-real theorem depends on the separately supplied analytic
Descartes/Rolle/parity proof; the code does not certify noninteger sine powers.
The real-exponent restriction, absolute-power convention, zero convention,
and local rank-two scope remain mandatory. No global L-function or RH/GRH
conclusion, nor novelty claim, is added.

Replay commands (add `-O` after `python -B` for optimized replay):

```text
python -B research/l-families/atlas/generalized/rational_rotation_real_power_exact_degree.py --check
python -B -m unittest tests.test_rational_rotation_real_power_exact_degree tests.test_rational_rotation_uniform_degree_gate tests.test_rational_rotation_branch_census
```
