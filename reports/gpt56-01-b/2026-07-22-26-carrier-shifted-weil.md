# Agent report — carrier-shifted compact-support Weil search

Agent: `gpt56-01-b`  
Issue: #26  
Branch: `agent/gpt56-01-b/26-carrier-shifted-weil-search`  
Starting hypothesis: a translated compact-support test family can probe unknown
spectral height with fixed dimension and may expose a negative Weil direction
that unshifted low-band scans cannot reach.

## Approaches attempted

1. Derived a scalar triangular carrier family with a finite prime trigonometric
   sum and compact archimedean formula.
2. Validated its normalization at `T=0` against the cutoff-free `N=0` matrix.
3. Ran scalar random carrier screens above `3e12`; no negative survived complete
   prime reevaluation.
4. Derived a finite carrier-localized cosine Gram family and its exact compact
   convolution kernel.
5. Built high-carrier leading matrices and screened top-weight prime subsets.
6. Recomputed finalists with every prime power through `c=10^7`, using safer
   long-double phase reduction.
7. Checked dimension growth at the strongest retained carrier.

## New results

### Proposed mathematical results

- `D-0701`: carrier-shifted nonnegative compact-support test family.
- `L-0701`: compact archimedean formula for the triangular carrier.
- `L-0702`: exact Gram, prime, pole, and compact archimedean matrix formulas.
- `M-0701`: mandatory complete-prime reevaluation protocol.

### Empirical computational results

- Complete coefficient set: 665,134 prime-power terms through `10^7`.
- Two apparent negative top-prime screens were refuted by the complete sum.
- Best retained complete leading value: approximately `+0.18535251496676164`
  at `T=3157430112465.479`, `N=12`.
- The same carrier at `N=16` remained positive at approximately
  `+0.18491323202279908`.

## Candidate counterexamples

None. No `Z-####` identifier was allocated.

## Certified computations

None. The elementary test suite checks formulas numerically but does not certify
a Weil sign.

## Failed approaches

- Scalar carrier random search at cutoffs through `10^8`: no negative retained.
- Treating a top-prime subset as the matrix: produced false negative signs.
- Increasing dimension at the best complete carrier: only marginal improvement.

## Potential errors

- Shared explicit-formula sign or Fourier normalization error.
- Inadequate phase accuracy in huge products `T*log(q)`.
- Omitted high-carrier corrections in the leading matrix.
- Ordinary eigensolver error near a multiple eigenvalue.
- Incomplete independent proof of admissibility and integral interchange.

## Files changed

See draft PR for D-0701, L-0701, L-0702, M-0701, O-0701, X-0701, tests,
results, and this report.

## Claims affected

Adds D-0701, L-0701, L-0702, M-0701, O-0701, X-0701. Does not change D-0001
or L-0001 status.

## Recommended next actions

1. Independently audit L-0701 and L-0702.
2. Implement a fixed-vector Arb evaluator for exact `P+R+A`.
3. Create a certified segmented prime stream with reproducible phase balls.
4. Search larger cutoffs using multilevel tail control rather than naive subsets.
5. Use complete leading negatives, if found, only as nominations for the exact
   fixed-vector pipeline.

## Organizational improvement ideas

Record the amount of the prime sum included in every computational artifact.
The label `complete through c` should be machine-verifiable, and partial sums
should carry a mandatory `TRUNCATED_PRIME_SCREEN` classification.
