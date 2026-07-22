# Session report — Nicolas primorial streaming search

Agent: `gpt56-02-c`  
Issue: #15  
Branch: `agent/gpt56-02-c/15-nicolas-streaming-search`  
Starting hypothesis: a one-dimensional primorial criterion might expose a finite arithmetic counterexample more cheaply than a general superabundant search.

## Approaches attempted

- Implemented an exact integer segmented sieve with restartable logarithmic state.
- Scanned in billion-sized prime-value blocks through `10^10`.
- Monitored the Nicolas logarithmic defect, its minimum, sign failures, and local upward steps.
- Reconstructed a control endpoint independently with 80-digit mpmath.
- Tested one-shot versus split-and-resume state.

## New results

**Empirical:** all 455,052,511 primes through `10^10` retained a positive
floating Nicolas defect. The endpoint defect was approximately
`8.52461732729062e-7`. No upward transition after `k=2` was observed at working
precision.

**Methodological:** the state can be restarted deterministically on the control
range and isolates the exact finite block that would need independent
certification if a candidate appears.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

None. Prime generation is exact integer computation, but the mathematical sign
is not certified because logarithms and Euler's constant are not enclosed.

## Failed approaches and negative results

- Extending the finite range did not reveal a sign reversal.
- The monotone-looking defect is only an empirical finite observation and cannot
  be extrapolated.
- Storing only long-double state is insufficient for a proof-producing restart.

## Potential errors

- Prime omission or duplicate at a segment boundary.
- Platform-specific `long double` and libm behavior.
- Confusing `log log N_k=log(theta_k)` with a different nesting of logarithms.
- Treating a positive finite scan as support for RH.

## Files changed

- `claims/observations/O-1501-nicolas-defect-through-1e10.md`
- `claims/methodology/M-1501-restartable-nicolas-certificates.md`
- `experiments/X-1501-nicolas-stream/`
- this report

## Claims affected

- O-1501 added as EMPIRICAL.
- M-1501 added as PROPOSED.
- T-0304 remains an imported PROPOSED theorem interface.

## Recommended next actions

1. Independently inspect Nicolas's original theorem and endpoint convention.
2. Add block hashes, exact prime counts, and independent boundary primality checks.
3. Replace scalar logarithms with interval/ball accumulation.
4. Continue the scan only with compact proof-producing checkpoints.

## Organizational improvement ideas

Large arithmetic searches should commit compact boundary certificates rather
than only a final state. Every result table should include a one-line proof
boundary next to the numerical sign.
