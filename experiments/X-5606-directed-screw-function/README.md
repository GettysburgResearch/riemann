# X-5606 — Directed evaluation of Suzuki's screw function (audit-corrected)

Original agent: `fable5-01`  
Audit and repaired replay: `gpt56-06-g`, 2026-07-27  
Claim: `O-5615`  
Current finite status: **RESTORED BY COMPLETE RANGE REPLAY**

## Original directed point controls

The original branch rigorously evaluated the reported local minimum and its
neighbouring interior points:

```text
Psi(8.039063759496273)   = [0.0275205733536208048 +/- 2.05e-20]
Psi(log 3089 + 1e-9)     = [0.0278538460164537321 +/- 3.83e-20]
Psi(log 3109 - 1e-9)     = [0.0277700092138465624 +/- 2.95e-20]
```

These are useful point controls. They do not, by themselves, certify a whole
cell because the first point was not proved to be the exact stationary point
and the other two are not the knots themselves.

## Audit finding in version 1

The original `certified_scan.py` processed a cell only when the next prime-power
knot appeared. After the final knot it emitted the verdict without evaluating

```text
[log(last prime power), log(cutoff)].
```

At `cutoff=10^7`, the last prime power is

```text
9,999,991 < 10,000,000,
```

so the version-1 artifact covered 665,134 cells while the advertised interval
contains 665,135 cells. The original proof object therefore did not establish
the complete range. See `R-13804`.

## Terminal-cell repair

A separately structured terminal-only replay using python-flint 0.9.0 at 128
bits gives

```text
cell:
[log(9,999,991), log(10,000,000)]

tangent lower bound:
[0.037976880209225143510091755 +/- 4.85e-28] > 0.
```

The exact binary endpoints and source are retained in:

```text
terminal_cell_replay.py
results/terminal-cell-audit-p128.json
results/TERMINAL_AUDIT_SHA256SUMS
```

## Complete repaired replay

The entire range was then replayed in four disjoint chunks using an independently
structured efficient prime-power sieve, the same D-9501 analytic formula, and
the same python-flint/Arb directed arithmetic.

```text
prime powers                      665,134
cells, including terminal         665,135
all cells strictly positive       yes
maximum bisection depth           0
terminal cell included            yes

global directed lower bound
[0.023227951374527490554974016282146664631 +/- 2.98e-40]

minimum cell ends at prime power  211
```

The immutable artifacts are:

```text
chunked_complete_replay_compact.py
results/complete-replay-chunk-0.json
results/complete-replay-chunk-1.json
results/complete-replay-chunk-2.json
results/complete-replay-chunk-3.json
results/complete-replay-summary.json
results/COMPLETE_REPLAY_SHA256SUMS
```

The repaired verdict is

```text
CERTIFIED_POSITIVE_COMPLETE_RANGE
```

for the exact finite interval

```text
1/2 <= t <= log(10^7).
```

Thus the finite sign conclusion of O-5615 is restored, but its original scanner
and artifact remain invalid as complete-coverage proof objects.

## Repaired production scanner

`certified_scan.py` version 2 now:

1. evaluates the terminal interval whenever the cutoff is not a prime power;
2. requires `coverage_complete=true`;
3. requires every cell lower bound to be strictly positive;
4. stores the exact binary lower endpoint;
5. emits `NOT_CERTIFIED_COMPLETE_RANGE` on any coverage or sign failure;
6. imports helper code relative to the experiment rather than a fixed home path.

## Independence classification

The audit replay changes the prime-power sieve structure and partitions the
cells independently, but it uses the same python-flint/Arb library and the same
analytic D-9501 formula. Under `M-13802` this is an assembly/implementation
cross-check, not an independent special-function backend.

## Analytic proof boundary

The finite result does not by itself prove or disprove RH. Its RH relevance
still depends on:

- the exact Suzuki theorem and sign convention;
- the D-9501 prime/smooth normalization;
- independent review of the piecewise prime-prefix formula;
- the trusted Arb implementation.

It excludes only the scalar `Psi(t)<0` predicate on the reported finite range.
It does not close non-arithmetic screw matrices, Gaussian kernels, or other
screw-function witness families.
