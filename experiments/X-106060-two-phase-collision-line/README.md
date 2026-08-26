# X-106060 — Two-phase collision-line replay

Exact standard-library replay for `R-106060`, `L-106060`, and `T-106060`.

It checks:

```text
multiplicity of (alpha,beta) -> tau*alpha+beta;
one-phase energy QD-|S|^2;
the sharp one-phase dimension barrier Q-1;
two-phase energy Q(Q-2)D+|S|^2;
coherent recovery of the unphased line;
sharp contraction (Q-1)/(Q^2-Q-1).
```

Run:

```bash
python3 verify.py --output /tmp/x106060.json
cmp /tmp/x106060.json results/verification.json
```

The replay checks exact finite-field kernel algebra. It does not prove the
root-residue occupancy `CROP106060`, the family moment, or RH.
