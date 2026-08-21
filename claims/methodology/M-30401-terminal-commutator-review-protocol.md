# M-30401 — Terminal-commutator source-manifest review protocol

Status: **FAIL-CLOSED ADVERSARIAL REVIEW PROTOCOL**  
Target: `T-30401`  
Date: 2026-08-08

## 1. Frozen dependencies

Review the following exact scopes:

```text
PR #272  L-27204/L-27205/L-27207/L-27208;
PR #280  exact finite central saturation only;
PR #286  shifted 6/7 bulk and finite Euler/Peano ledger;
PR #301  positive stopped-power resolution and common-tail recombination;
PR #303  correct absolute divisor-source coordinate and Hausdorff residual;
this PR  R/L-30401, L-30402, L-30403, T-30401, X-30401.
```

Do not import PR #301's standalone nonnegative source-flow claim or PR #303's
root-only capacity equality.

## 2. Review order

1. Expand `T_2,T_3,T_4` and reproduce the `3/4` descendant-capacity witness.
2. Prove the node-multiplicity formula in `L-30401`.
3. Reconstruct the dyadic Haar formula by finite summation by parts.
4. Prove the recurrence for the actual expanded capacities.
5. Reconstruct the adjacent-tree recursions and the `24 sqrt(h+1)` capacity
   bound.
6. Check the divisor-source load of `Phi(sigma)` for every column.
7. Check the paired representation `(A-B)E+B(S-C)` independently.
8. Freeze one complete PR #286 boundary generation and map every source label to
   its integer divisor node `m`.
9. Verify that its declared capacity weight is exactly bounded by the atomic
   `sqrt(m)` weight.
10. Reconstruct the divisor-switch estimate including every shift and collar.
11. Replay the complete finite carry vector after replacing the boundary source
    by adjacent commutators.
12. Only then invoke PR #272's Cycle-Debt and RH consumer.

## 3. Mandatory production manifest

For every cascade depth, export:

```text
analytic input channels and coefficients;
finite shifted-even and unshifted-odd legs;
common-destination recombination;
Euler jets and exact remainder;
unmatched first terms;
endpoint and zero-extension atoms;
final divisor-source vector sigma_a;
atomic norm sum sqrt(m)|sigma_a(m)|;
adjacent commutator coefficients;
complete balanced split flow;
negative capacity debt;
complete carry-column replay.
```

The same source coefficient may occur in only one of the analytic or boundary
banks.

## 4. Automatic rejection

Reject a claimed completion if it:

```text
uses root contribution c_n-c_(n+1) as the expanded edge coefficient;
claims descendants always supply the requested central capacity;
uses the nonnegative edge pair as a standalone divisor-source flow;
omits one negative central edge in S-C;
uses the unweighted O(log n) commutator count instead of the capacity recursion;
replaces the actual critical n^(-3/2) coefficient by the source-blind 1/n toy;
takes absolute values before common-destination recombination;
omits an unmatched first odd term;
leaves a boundary source to be paid twice;
identifies the PR #286 cap norm without emitting its source-node map;
promotes X-30401 finite replay to the all-generation theorem;
changes the PR #272 capacity normalization or square-screw consumer.
```

## 5. Acceptance boundary

The new local lemmas can be accepted independently.  `T-30401` is accepted only
when the complete finite Euler/Peano source manifest is reconstructed and the
atomic-norm identification in `L-30403` is verified at every source type.
Until that reconstruction is complete, RH remains unverified.
