# T99320 — Target-aligned rank-one row frame

The new exact identity is

\[
Q_Y(j)=\int_1^Y(4\sqrt{Y/t}-3)\eta_j(t)\frac{dt}{t},
\qquad \eta_j(t)>0.
\]

At each source coordinate, every component row is therefore the same positive
row atom times the scalar SHARP target. Compact target Hall has zero matched-row
cost and its residual lifts simultaneously to all rows. The causal
parent-minus-child row is also pointwise positive in the same atom.

The signed finite/continuum and Volterra calibration remains in the bounded
fixed-row ledger of PR #641. The resulting candidate has one imported arithmetic
producer: the exact target Hall/root source registry.

```bash
python3 experiments/X-99320-target-aligned-row-frame/verify.py \
  --output /tmp/x99320.json
cmp /tmp/x99320.json \
  experiments/X-99320-target-aligned-row-frame/results/verification.json
sha256sum -c T99320_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_X_99320_TARGET_ALIGNED_RANK_ONE_ROW_FRAME
```

**RH remains unproved pending hostile independent reconstruction.**
