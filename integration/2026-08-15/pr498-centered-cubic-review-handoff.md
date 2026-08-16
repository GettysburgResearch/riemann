# PR #498 exact-head review handoff

```text
proposal:       PR #498
proposal head:  6cc0da2fa5711017e260ebdcea4ba8c22e453288
review cutoff:  2026-08-15T23:51:56Z
verdict:        VERIFIED WITH FIXES at RH-equivalent-criterion scope
RH:             UNPROVEN
```

## Reconstructed chain

```text
centered Q4 field
-> mean-zero Bernoulli projection
-> exact cubic source sum
-> zero-safe Mellin multiplier
-> centered-energy <=> RH
-> prime-base scalar blocks
-> same-prime O(N log N)
-> zero-mode-free square-root major arc
-> CPBD
```

Every arrow through the major-arc reduction reconstructs at the stated exact or imported scope. The terminal CPBD arrow is an open arithmetic estimate and is itself RH-equivalent.

## Integration rule

Retain `L-93250`, `T-93251`, `L-93252`, `T-93253`, and `R-93254`. Label the two theorems as `RH-EQUIVALENT CRITERION`, not as evidence that RH is proved.

## First open theorem

Prove a genuine cross-prime upper bound, for example

\[
|\sum_pZ_{p,N}|^2\ll N\log^B N.
\]

The separate proposed heat-resolvent successor supplied after this review is not part of the verdict and is not evidence for PR #498.