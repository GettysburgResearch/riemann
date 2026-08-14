# Root score-Hall causal-envelope closure

This packet is the review front door for `T-91657`.

## Freeze

```text
repository:   gfreund123/riemann
base PR:      #462
base branch:  research/gpt56-sol/91680-causal-proportional-tail
base SHA:     8642e062b6c6f5a4c7d443a1ee5a6e9ecf3e4706
head branch:  research/gpt56-pro/91683-root-score-hall-causal-closure
```

## Main correction

The packet accepts the stopped-leaf Hall counterexample from PR #456. It never applies Hall to a stopped one-prime parent `py`.

Instead it applies score Hall only to the certified root quotient window

\[
1\le x\le c_0^{-1}<54.2192,
\]

obtains one explicit positive target/score/all-row decomposition there, transports that identity through the positive endpoint frame and one global quantizer, and then uses the exact causal packet reset for all rough recursion.

## Review order

1. `claims/refutations/R-91673-t91656-reimports-refuted-stopped-leaf-hall.md`
2. `claims/lemmas/L-91673-fixed-window-score-hall-is-an-explicit-simultaneous-native-root-decomposition.md`
3. `claims/lemmas/L-91674-positive-endpoint-frame-commutes-with-root-hall-and-one-global-quantization.md`
4. `claims/theorems/T-91657-root-score-hall-causal-envelope-resolution-proposal.md`
5. experiment `X-91673`
6. `REVIEW_SPECIFICATION.md`
7. dependency lock under `integration/2026-08-14/`

## Replay

```bash
cd experiments/X-91673-root-score-hall-common-normalization
python3 verify.py --json results/verification.json
```

Expected:

```text
PASS_ROOT_SCORE_HALL_COMMON_NORMALIZATION_ALGEBRA
```

## Status

This is a candidate complete implication architecture, not an accepted proof of RH. The principal review-bearing interface is the frozen analytic endpoint-frame realization and the one-use finite mismatch/collar/terminal estimates.
