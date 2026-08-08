# X-27204 — Pascal-cycle fragmentation kernel

This standard-library checker verifies:

- elementary Pascal four-cycle divergence cancellation;
- that those cycles have the full unrestricted kernel rank;
- the explicit reduction of every split to unit edges modulo Pascal cycles;
- canonical eta=`1/4` balanced trees;
- the balanced fundamental-cycle basis;
- the canonical signed solution for arbitrary size-zero divergence;
- invariance of divergence under cycle corrections.

Run:

```bash
python verify.py
python -m unittest discover -s tests -v
```

The checker proves finite algebra only. It does not construct nonnegative cycle
coordinates for the Möbius target, prove MFT, or prove RH.
