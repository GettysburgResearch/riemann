# X-18504 — Direct complete-complement residual shorting

This experiment replays the exact scalar control for `L-18512` and `T-18504`.

Run:

```bash
python verify.py certificates/synthetic.json
python -m unittest discover -s tests -v
```

The certificate deliberately uses an inexact harmonic solve. The squared solve
residual recovers the exact Schur value while the older separated terminal/cross
bound proves only a zero floor.

No zeta data are used and no RH conclusion is asserted.
