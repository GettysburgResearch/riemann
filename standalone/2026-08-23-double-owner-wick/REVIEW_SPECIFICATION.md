# Hostile review specification — T-102820

Frozen predecessor:

```text
PR #719
a608c99ef525d0855fec46ea3f58d46d0eb50d84
```

The publication branch advances beyond that predecessor additively.

## Mandatory reconstruction

1. Expand
   \[
   e^{-L}-I+L=L^2\int_0^1(1-t)e^{-tL}\,dt
   \]
   coefficientwise.
2. For every squarefree set of size \(k\ge2\), recover the ordered-pair share
   \((-1)^k/[k(k-1)]\) and unordered-pair share
   \((-1)^k/\binom{k}{2}\).
3. Keep the two labelled copies of \(67\) distinct through the owner ledger.
4. Separate the diagonal of \(L^2\) and verify that it consists only of
   prime-square shifts of activity \(p^{-1}\).
5. Recompute the free pair energy
   \[
   \frac12\left[(\sum 1/p)^2-\sum1/p^2\right].
   \]
6. Verify that collapsing \(\binom{k}{2}\) equal owner shares costs exactly
   \(\binom{k}{2}\) in squared norm, not its square.
7. Reconstruct the existing same-product factor-pair and owner/core
   injectivity inputs before declaring equal-product collapse closed.
8. Write the remaining physical restriction with both integer-product and
   unordered-pair coordinates visible.
9. Reproduce `R-102728`; reject any implication from free Fock energy to a
   one-parameter physical restriction without arithmetic input.
10. Confirm that `DPWNC102749`, `WNC102743`, `OER102780`, and RH remain
    unproved.

## Immediate falsifiers

```text
merging the two 67 labels before ownership;
charging an ordered-pair coefficient as an unordered-pair coefficient;
counting the pair-collapse loss twice;
retaining prime-square diagonals in the hard packet;
using free pair energy as a physical restriction theorem;
taking an absolute value before exact carrier and equal-product recombination;
claiming that a finite-chaos truncation closes the all-chaos current;
claiming RH from the retained replay.
```

## Replay

```text
PASS_T102820_DOUBLE_OWNER_WICK_REDUCTION
9b460f281fd4be4cc3c187c6d4b6ec620eca8b1e5e66b5041d238136d3287b2e
```

The replay checks finite algebra and fixtures only.
