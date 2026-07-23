# Agent session report — dyadic freeze and directed prime pilot

Agent: `gpt56-01-d`  
Issue: #28  
Branch: `agent/gpt56-01-d/28-dyadic-freeze-directed-prime`  
Date: 2026-07-23

## Starting hypothesis

The PR #49 exact consumer could be exercised on a real complete carrier vector
at a smaller cutoff, exposing vector, phase, knot, interval, and schema failures
before the 4.1-billion-term target run.

## New mathematical results

- `L-2810`: exact coordinatewise dyadic-freezing stability, including the target
  result that 80 fractional bits perturb the normalized leading Rayleigh value
  by less than `10^-15` under a crude unconditional operator bound.
- `L-2811`: exact fixed-vector scalarization through Gaussian-dyadic
  autocorrelations; one real scalar term per prime power replaces an interval
  matrix.
- `T-2810`: end-to-end center/radius and sharded-moat theorem, composed with
  T-2801 and L-2803.

## Certified computational result

At `c=10^8`, `K=1024`, and the target carrier:

- 5,761,455 primes and 1,404 higher prime powers were included;
- the vector was frozen at 96 bits;
- every prime scalar term was evaluated with directed MPFR arithmetic;
- the exact composed full interval was approximately
  `[0.006641912535150959, 0.006641913487198074]`;
- the lower endpoint is positive.

This certifies only the fixed pilot vector, conditional on code and dependency
review. No RH claim follows.

## Important observation

The directed midpoint differs from the original long-double discovery margin
at the `10^-6` scale, consistent with the earlier phase-backend discrepancy.
The sign survives comfortably, but the result reinforces that midpoint phase
arithmetic cannot be promoted.

## Failed or incomplete work

- The `c=10^11` vector remains unavailable because the coefficient/eigenvector
  artifact was not retained by the complete-stream run.
- The full 4,118,082,969-term directed stream was not executed.
- No independent directed backend has reproduced the pilot.

## Files changed

- `claims/lemmas/L-2810-dyadic-freeze-stability.md`;
- `claims/lemmas/L-2811-fixed-vector-prime-scalarization.md`;
- `claims/theorems/T-2810-end-to-end-fixed-vector-certificate.md`;
- `experiments/X-2810-dyadic-freeze-directed-prime/`;
- `integration/gpt56-01-d-registry-patch.md`;
- this report.

## Next actions

1. Regenerate the `c=10^11`, `K=1024` coefficient vector and freeze it at 80–96
   bits.
2. Use `directed_prime_shard.c` over disjoint contiguous ranges, with exactly one
   higher-power shard.
3. Wrap each outward endpoint as an exact rational shard interval.
4. Compose through PR #49's exact checker and T-2801 normalization fingerprint.
5. Independently reproduce any strict sign before status promotion.

## Counterexample status

None. No `Z-####` identifier is allocated.
