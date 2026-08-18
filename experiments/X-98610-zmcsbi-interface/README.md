# X-98610 — ZMCSCBI interface correction

This lightweight exact replay checks:

1. the orthogonal-feature construction behind `R-98610`;
2. one nontrivial exact semigroup instance of the Tao prime-update identity;
3. the exact three-node countermodel showing negative local current can be
   repaired by the two-prime future term.

Run:

```bash
python3 experiments/X-98610-zmcsbi-interface/verify.py \
  > experiments/X-98610-zmcsbi-interface/results/verification.json
python3 -m pytest experiments/X-98610-zmcsbi-interface/tests -q
```

The replay does not prove RH. It verifies the correction to the proposed
cross-scale interface.
