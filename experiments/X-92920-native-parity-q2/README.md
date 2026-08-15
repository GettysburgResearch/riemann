# X-92920 — Native/rough parity and exact `q=2` normalization replay

Run from the repository root:

```bash
python3 experiments/X-92920-native-parity-q2/verify.py \
  --mutations \
  --output experiments/X-92920-native-parity-q2/results/verification.json
python3 -m unittest discover \
  -s experiments/X-92920-native-parity-q2/tests -v
python3 -m py_compile \
  experiments/X-92920-native-parity-q2/verify.py \
  experiments/X-92920-native-parity-q2/tests/test_verify.py
sha256sum -c FACTOR67_92920_SHA256SUMS
```

The replay uses exact `Fraction` arithmetic.  It proves the conditional
`109/1200` rough-lift separator, checks the paired swap/native cancellation,
authenticates frozen heads and content hashes, and rejects orientation and
full-capacity-promotion mutations.

It does not independently replay the Hall/profile inequalities, endpoint
integrals, all-column analytic estimates, prime-square theorem, Mellin
continuation, Landau theorem, or prove RH.
