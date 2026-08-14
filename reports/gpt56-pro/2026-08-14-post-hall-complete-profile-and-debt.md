# Post-Hall complete arithmetic profile and debt report

## Freeze

```text
repository:       gfreund123/riemann
parent PR:        #462
parent head:      8642e062b6c6f5a4c7d443a1ee5a6e9ecf3e4706
review date:      2026-08-14
```

The exact stopped-leaf Hall counterexamples remain binding.  This packet does not revive them.

## Main outcome

The unbounded causal-order problem is fully closed on the actual arithmetic source domain for both score and target normalization, with no rough-prime cutoff.  The score/target Lorenz cutoffs are both below `2000`.  The target-proportional score debt is zero above `p=500000` and has one absolute compact-range sum below it.  A target-Lorenz source producer has exact target, no score debt and one source ray; its sole remaining condition is the explicit component-row family in `L-91684.5`.

## Directed replay

```text
PASS_GLOBAL_TARGET_NORMALIZED_COMPONENT_MONOTONICITY
PASS_COMPLETE_ARITHMETIC_CAUSAL_SCORE_PROFILE
PASS_COMPLETE_ARITHMETIC_CAUSAL_TARGET_PROFILE
PASS_P61_SCORE_AND_TARGET_LORENZ_CUTOFF_2000
PASS_TARGET_PROPORTIONAL_SCORE_DEBT_COMPACT_SUPPORT
PASS_POST_HALL_COMPLETE_PROFILE_AND_DEBT_PACKET
```

Aggregate proof-object digest:

```text
7cce71153cd751be8c2b20a2bd3d136e4ef926912d4e036b4b0ec3fa4c13bd42
```

## Honest verdict

This is a substantial unconditional advance, not a full proof.  Numerical reconnaissance found positive row margins throughout a broad grid, with the smallest sampled target-Lorenz margin in the first quotient cell, but no numerical scan is promoted as a theorem.  Independent review should first reconstruct `L-91682` and `L-91683`, then attack the finite row family in `L-91684`.
