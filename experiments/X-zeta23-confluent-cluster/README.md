# X-zeta23-confluent-cluster

Finite standard-library diagnostic for
`research/external/anthropic-zeta23/proofs/CONFLUENT_CLUSTER_RENORMALIZATION.md`.

Run:

```bash
python3 experiments/X-zeta23-confluent-cluster/verify.py
sha256sum -c experiments/X-zeta23-confluent-cluster/SHA256SUMS
```

The script checks the rectangular-window control kernel

\[
K(z,w)=\int_{-1/2}^{1/2}e^{i(z-\overline w)u}\,du.
\]

It verifies numerically that:

- Newton-transformed cluster Grams converge to the exact jet moment Gram;
- raw determinants collapse while transformed Cholesky pivots remain positive;
- the unit reflected-pair capture cost is asymptotic to `12/y^2`;
- the depth-normalized capture cost tends to `12`;
- the pair Weil value is exactly `-2y^2` at multiplicity one;
- a finite two-cluster confluent Gram remains positive.

This is a finite diagnostic of the exact algebra. It does not prove a uniform-in-order conditioning theorem, a corrected-kernel floor, or RH.
