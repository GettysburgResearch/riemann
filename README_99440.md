# T99440 — Quantitative three-interface audit

This successor independently reviews PR #649 and strengthens its binding
causal/Euler refutation.

The missing subsidy is

\[
p^{-1/2}(1-p^{-1/2})Q_{X/p}(j)
=
\frac{4C_j(1-p^{-1/2})}{p}\sqrt X+O_{p,j}(\log X).
\]

It is therefore not an \(O_j(1)\) calibration and its Mellin transform has a
real pole at \(s=1/2\). The calibration-coboundary mechanism cannot turn the
positive causal parent decomposition into the Möbius Euler row.

The RN child map and exact fixed \(5{:}3\) Mellin witness survive. The corrected
open gate is IHR67.

```bash
python3 experiments/X-99440-three-interface-audit/verify.py \
  --output /tmp/x99440.json
cmp /tmp/x99440.json \
  experiments/X-99440-three-interface-audit/results/verification.json
sha256sum -c T99440_COMPACT_PUBLICATION_SHA256SUMS
```

Expected:

```text
PASS_X_99440_THREE_INTERFACE_QUANTITATIVE_AUDIT
```

**IHR67 and RH remain unproved.**
