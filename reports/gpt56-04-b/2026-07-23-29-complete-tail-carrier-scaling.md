# Agent report — complete-tail carrier scaling

Agent: `gpt56-04-b`  
Issue: #29  
Branch: `agent/gpt56-04-b/29-complete-tail-carrier-scaling`  
Base: `agent/gpt56-01-b/26-carrier-shifted-weil-search` / draft PR #27  
Date: 2026-07-23

## Starting hypothesis

The `+0.18535` complete near miss in X-0701 might cross after enlarging the
prime cutoff and carrier envelope, but truncated-prime screens were known to
reverse signs.  The continuation therefore had to include every prime power at
each retained cutoff.

## Approaches attempted

1. Reproduced the X-0701 carrier matrix at `c=10^7`.
2. Implemented segmented complete prime-power continuation through `10^8`,
   `10^9`, and `10^10` with long-double phase reduction.
3. Increased the local Fourier lattice from 3 to 5 cells.
4. Tested continuously spaced local frequency offsets.
5. Derived D-0801, a piecewise-constant autocorrelation carrier family.
6. Derived L-0801, reducing its complete prime side to an `O(K)` lag stream and
   one Hermitian Toeplitz eigensolve.
7. Evaluated `K=1024` with all 455,062,595 terms through `c=10^10`.
8. Added shard coverage checks and adversarial unit tests.

## New results

### Proposed mathematics

- D-0801: compact autocorrelation carriers with nonnegative real-axis spectral
  tests and finite Fourier support.
- L-0801: exact hat deposition and Hermitian Toeplitz reduction of the complete
  finite prime side.

### Empirical computation

The integer-lattice leading margin decreased from approximately `+0.24246` at
`c=10^7` to `+0.01965` at `c=10^10` when five cells were used.  The new
1,024-cell family reduced the final margin further to

```text
+0.010646422368668418.
```

The final stream contained 455,052,511 primes and 10,084 higher prime powers.
No negative complete leading value was found.

## Candidate counterexamples

None.  No `Z-####` ID was allocated.

## Certified computations

None.  Stream coverage is exact at the combinatorial level, but phases,
summation, eigenvalues, and the high-carrier archimedean replacement are not
ball-enclosed.

## Failed or blocked approaches

- Increasing the cutoff by three decimal decades did not produce a crossing.
- A 5-cell lattice improved the margin but appeared to saturate.
- Continuous spacing optimization gave only modest gains.
- Direct high-height `zeta'` root finding with mpmath was too slow for a reliable
  reconnaissance pass in the available session and produced no retained result.
- The exact D-0801 archimedean matrix remains unimplemented.

## Potential errors

- A sign or factor mismatch inherited from D-0001/L-0702.
- Long-double phase reduction is not a proof at carriers near `3e12`.
- The D-0801 piecewise family may require smoothing to meet the exact imported
  explicit-formula admissibility class.
- The leading scalar may conceal a small archimedean correction, although the
  observed positive margin is much larger than the expected high-carrier scale.
- Dense binary64 eigensolving has no certified residual or gap enclosure.

## Files changed

- `claims/definitions/D-0801-piecewise-autocorrelation-carrier.md`
- `claims/lemmas/L-0801-piecewise-prime-toeplitz.md`
- `claims/observations/O-0801-complete-tail-decade-continuation.md`
- `experiments/X-0801-piecewise-carrier-tail/README.md`
- `experiments/X-0801-piecewise-carrier-tail/stream.py`
- `experiments/X-0801-piecewise-carrier-tail/merge.py`
- `experiments/X-0801-piecewise-carrier-tail/tests/test_stream.py`
- compact result and test files
- integration patch
- this report

## Claims affected

- D-0801 — new, PROPOSED
- L-0801 — new, PROPOSED
- O-0801 — new, EMPIRICAL
- X-0801 — new, EMPIRICAL
- Issue #29 — remains open
- no counterexample candidate

## Recommended next actions

1. Independently reconstruct D-0801 and L-0801, including matrix orientation.
2. Derive exact cellwise archimedean and pole Toeplitz blocks.
3. Add a rational fixed-vector checker and a ball phase producer.
4. Run several cell resolutions in one pass to measure discretization error.
5. Scan cutoff intervals adaptively; decimal endpoints alone can miss threshold
   excursions.
6. Treat a future negative as a nomination until Issue #28 certifies every term.

## Organizational improvement ideas

Large finite prime searches should be stored as coverage-checked shards.  A
merger should reject gaps, overlaps, and duplicated special streams before it
is allowed to print an eigenvalue.  This turns “complete through c” from prose
into a machine-checkable property.
