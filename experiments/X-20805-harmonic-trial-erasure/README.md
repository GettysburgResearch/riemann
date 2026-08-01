# X-20805 — Harmonic trial erasure and negative-channel update

This exact standard-library experiment replays `L-20806/L-20807` over
`fractions.Fraction`.

It verifies:

1. positivity of the comparator constrained block and the full comparator;
2. two different source-normalized trials;
3. exact equality of their comparator-harmonic source vectors;
4. positivity of the actual constrained block after a negative rank-one update;
5. the conditional defect and conditional negative amplitude;
6. equality of the direct source Schur complement and the Woodbury formula;
7. a strictly negative final source Schur value despite a positive comparator.

Retained exact values:

```text
comparator harmonic vector          (1,-9/46,8/69)
negative-channel defect              2213/2300
conditional negative amplitude       4069/2760
comparator source Schur              5/4
actual source Schur                 -7394941/7329456
```

Proof-object SHA-256:

```text
00b991cce684e4c9f2f8f4efb65726645acca621dcb2d67c33a4821ee05fa9e6
```

The packet is synthetic. It certifies the finite algebra and the scope
correction; it is not a zeta sign or an RH result.

Run:

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```
