# Second-pass addendum to Reviewer A's cross-review of Reviewer B

**Primary cross-review PR:** #710  
**Primary reviewed object:** PR #708 at `eb1987502ef9043e782ac6ab1e19c47be9daef93`  
**Frozen main:** `677203992eb0168920365ee45ae9db76bfa97dcf`  
**Scientific status:** **RH remains unproved.**

This addendum records two findings from the final exact-source read-back. It does not replace `VERDICT_DELTA.tsv`; it supplements that packet and is controlling only for the two semantic IDs in `SECOND_PASS_VERDICT_DELTA.tsv`.

## 1. Suzuki first-chaos theorem requires a non-minor scope weakening

Reviewer B classified `OPERATOR.SUZUKI.FOCK_FIRST_CHAOS` as `VERIFIED_WITH_FIXES`. The exact source theorem, PR #400 `L-91036`, proves the reduction only under a structured family:

1. naturality under every intensity scaling `rν`;
2. an orthogonal Wiener–Itô chaos grading, or equivalent independent-increment product-system decomposition;
3. exact target linearity `K_r=rK_1` for every `r≥0`.

The source explicitly says that an arbitrary isometry constructed after fixing `r=1` need not display this grading. Therefore the theorem is not a universal statement about every source-linear positive colligation. The cross-verdict is:

```text
VERIFIED_WITH_FIXES -> WEAKEN_TO_CONDITIONAL
```

The surviving result is still valuable: **under the three structural hypotheses**, all higher positive chaos kernels vanish and the output factors through compensated first chaos. Suzuki's amplitude embedding and the open coefficient-one first-chaos domination gate are unaffected.

## 2. PRs #446 and #460 share one critical-reserve resource

The order-three actual-`Xi` theorem in PR #446 and the later curvature/anchor formulation in PR #460 use the same verified critical-orbit reserve mechanism. No double-spending occurs inside the reviewed PR #446 proof, so the `VERIFIED_WITH_FIXES` order-three verdict remains unchanged.

For canonical graph purposes, however, these are not two independent resources. They must be represented by one shared reserve-ledger node. A later conjunctive graph must not add, multiply, or independently reuse the two appearances.

The PR #710 body should therefore be read as:

> no critical-orbit reserve misuse was found inside the reviewed order-three theorem; PRs #446 and #460 nevertheless require a shared-resource alias in canonical reconciliation.

## Effect on the overall cross-review

Reviewer B remains high quality and suitable as major evidence for reconciliation after the recorded repairs. The overall actual-`Xi` order-three theorem remains `AGREE_VERIFIED_WITH_FIXES`. The only new mathematical weakening is the conditional scope of `L-91036`.

No heavy computation was rerun. Neither PR #708 nor PR #709 was modified. RH remains unproved.
