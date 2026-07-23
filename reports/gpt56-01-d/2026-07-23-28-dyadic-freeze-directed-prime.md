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
- `L-2811`: exact Gaussian-dyadic autocorrelation preprocessing; one scalar term
  per prime power replaces an interval matrix and complements L-2806.
- `L-2812`: simultaneous directed Toeplitz boxes permit the vector to be chosen
  after the prime stream. This removes the historical-vector dependency and can
  reduce two target passes to one.
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

## Important observations

1. The directed midpoint differs from the original long-double discovery margin
   at the `10^-6` scale, consistent with the earlier phase-backend discrepancy.
   The sign survives comfortably, but midpoint phase arithmetic cannot be
   promoted.
2. Post-selection from simultaneous coefficient boxes is rigorous: after one
   directed coefficient pass, any exact dyadic vector may be chosen and
   contracted. There is no probabilistic selection-bias assumption.
3. A stored coefficient pass is reusable for many vectors. A dedicated scalar
   rerun is needed only when coefficient-box dependency leaves zero unresolved.

## Failed or incomplete work

- The full 4,118,082,969-term directed coefficient-box stream was not executed.
- No independent directed backend has reproduced the pilot.
- The historical `c=10^11` vector remains unavailable, but L-2812 shows that it
  is no longer a logical prerequisite.

## Files changed

- `claims/lemmas/L-2810-dyadic-freeze-stability.md`;
- `claims/lemmas/L-2811-fixed-vector-prime-scalarization.md`;
- `claims/lemmas/L-2812-postselected-toeplitz-box.md`;
- `claims/theorems/T-2810-end-to-end-fixed-vector-certificate.md`;
- `experiments/X-2810-dyadic-freeze-directed-prime/`;
- `integration/gpt56-01-d-registry-patch.md`;
- this report.

## Next actions

1. Extend the reviewed X-2805/X-0801 producer to emit simultaneous directed
   boxes for all 1,024 lag coefficients.
2. Run those boxes over the 50 declared `c=10^11` coverage ranges at 192 and 256
   bits.
3. Assemble the midpoint matrix, select its leading vector, and freeze it at
   80–96 bits using L-2810.
4. Contract the stored boxes exactly through `verify_toeplitz_box.py` and compose
   through T-2810.
5. Launch a second fixed-vector L-2806 scalar pass only if the first interval
   contains zero.
6. Independently reproduce any strict sign before status promotion.

## Counterexample status

None. No `Z-####` identifier is allocated.
