# Conrey functional reconstruction and unconditional low-order bounds

## Executive result

The previous adjacent-companion `92.18%` claim could not be reconstructed from
a deposited theorem and is now firewalled.

The primary Conrey variational theorem was rebuilt from the full 1983 source
transcription on PR #742. A separate exact standard-library replay evaluates
four rational admissible test functions and proves

```text
alpha_0 > 0.30
alpha_1 > 0.80
alpha_2 > 0.925
alpha_3 > 0.96
```

without floating-point sign decisions.

## Why this matters

The published optimized table is stronger, but its old decimal values had been
treated as a black-box historical import. T104620 creates a trusted,
replayable baseline:

```text
primary analytic theorem
  -> exact finite functional
  -> rational polynomial certificate
  -> rational transcendental enclosure
  -> unconditional fixed-order proportion.
```

This is the correct foundation for future higher-degree optimization.

## Remaining research

1. Recover Conrey's published polynomial coefficients from the primary page
   images and certify the entire historical table.
2. Optimize the admissible polynomial family in exact rational arithmetic.
3. Reconstruct any adjacent-derivative companion mean square separately; do not
   infer it from the original theorem.
4. Compare the direct fixed-order route with the persistence--Mellin and
   stationary-horizontal-minimum programmes only after each uses the same
   normalization and short-window count.
