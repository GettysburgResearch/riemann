# X-100130 — Minimal-wavelet spectral audit replay

Run:

```bash
python3 verify.py
```

The exact standard-library replay checks:

- 256 finite Möbius/floor-kernel cancellation identities;
- the algebraic wavelet multiplier
  `(1-sqrt(2)x)(1-x)^2`;
- its double zero at `s=0` and zero at `s=1/2`;
- the zero-real-part / energy-abscissa exponent dictionary;
- fail-closed status for `MWOC99910` and RH.

Expected verdict:

```text
PASS_T100130_MINIMAL_WAVELET_SPECTRAL_AUDIT
```

The replay authenticates finite algebra. The Mellin-Hardy abscissa theorem is
proved in `L-100130/L-100131`; it is not replaced by numerical sampling.
