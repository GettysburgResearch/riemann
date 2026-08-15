# Publication handoff — T-91752 one-shot SONTR / NRCT hardening

## Intended base

```text
PR #486
research/gpt56-pro/91750-canonical-factor67-closure
0d8badeda73626598a74dc3ef009b67a74af3b81
```

## Intended successor branch

```text
research/gpt56-pro/91754-exact-one-shot-sontr-nrct
```

## Suggested draft PR title

```text
hardening: exact Hall integration and bounded one-shot SONTR/NRCT slack
```

## Scientific disposition

This packet is a strict hardening of the one-shot implementation in PR #486.
It adds three controlling changes:

1. integrate the measurable Hall kernel exactly, eliminating Hall meshes and activation-knot collars;
2. use no auxiliary Schur port and no signed finite-correction row;
3. combine PR #485's elementary Chebyshev bound with the sparse Y4 estimates to obtain the explicit root bound
   `J_Lambda(X)-H(d_X)<61000` for `X>=10^12`.

The packet presents a complete RH proof proposal for independent frozen-head review. RH is not treated as accepted before that review.

## Required post-push verification

```bash
python3 experiments/X-91754-one-shot-native-slack/verify.py
python3 -m py_compile experiments/X-91754-one-shot-native-slack/verify.py
sha256sum -c standalone/2026-08-15-one-shot-sontr-nrct/CONTENT_SHA256SUMS
```

Expected:

```text
PASS_ONE_SHOT_SONTR_NRCT_HARDENING_ALGEBRA
f1065b2326671048f6550ed8f216ca29029df58acdb0a39cc4f4293a32c4f418
```
