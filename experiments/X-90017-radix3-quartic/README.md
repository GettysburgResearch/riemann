# X-90017 — Radix-three quartic annular replay

Companion to `L-90017` and `T-90013`.

```bash
python experiments/X-90017-radix3-quartic/verify.py --max-x 5000000
```

The checker supplies an exact four-cell Bernstein certificate over `Q(sqrt(3))` for `|P_3(e^{it})|^2 <= 18`, verifies the resulting RH-side margin, and scans every aligned endpoint `X=81N` through the retained maximum. The finite scan is not a cofinal sign proof.
