# arXiv-ready proposal v1

## Summary

This PR adds the first single-file, arXiv-style reconstruction of the strongest live factor-67 proof proposal, together with its compiled PDF and a theorem/lemma ledger.

The manuscript is deliberately written as a **conditional proof proposal and adversarial audit**, not as an announcement that RH has been proved. It reconstructs the native factor-67 compiler around the active PR #524 line, enforces the three source-type firewalls, carries the same-row construction through all-column thinning and the sparse `Y4` dual, and derives the conditional endpoint implication through the prime-square moat and Mellin–Landau converse.

## Main conditional statement

Under a precisely stated certification package `Cert_67`, the construction gives for every `X >= 10^12` a nonnegative native-feasible source `d_X` with

```text
0 <= J_nat(X) - H(d_X) < 60989,
```

which, through the frozen endpoint consumer, implies RH.

## Adversarial findings made explicit

1. **Target–Lorenz tail is not currently certified.** The available program wraps point values returned by standard `sqrt` and `log` calls as singleton intervals. This is not an outward enclosure proof.
2. **Native normalization has a load-bearing notation collision.** Some dependencies use `J_Lambda` for the smoothed prime sum, while the endpoint consumer uses `P_Lambda` for that sum and reserves `J` for the native benchmark. The PDF separates `P_Lambda` and `J_nat` and states the exact identity/bound that must be proved.
3. **Three source sorts are enforced.** Complete sources, current-only row bonuses, and signed observations may not be promoted into one another.
4. **The Volterra fibre remains unsplit.** The exact negative counterexample to causal splitting is included.
5. **Every native literal has one owner.** The finite tree, retained continuum, top collar, and signed localization errors form an explicit one-use ledger.

## Files

- `standalone/2026-08-16-arxiv-ready-proposal-v1/main.tex` — full standalone source
- `standalone/2026-08-16-arxiv-ready-proposal-v1/native-factor67-proposal-v1.pdf` — compiled PDF
- `standalone/2026-08-16-arxiv-ready-proposal-v1/THEOREM_LEDGER.md` — source theorem/lemma map and status
- `standalone/2026-08-16-arxiv-ready-proposal-v1/build.sh` — deterministic local build command

## Suggested review order

1. Expand and verify the native normalization (`N67`).
2. Replay the Target–Lorenz tail using Arb/MPFR with genuine outward rounding (`F67`).
3. Check the type discipline and one-use ownership.
4. Recompute the constants `130 > 129`, `5033 - 4452 = 581`, and the `60989` cost ledger.
5. Re-derive the prime-square occupancy signs and Mellin transform normalization.

## Proof status

**RH remains unproved in the repository.** The paper identifies a complete conditional composition and a machine-checkable closure contract; it does not conceal the two unresolved certification interfaces.
