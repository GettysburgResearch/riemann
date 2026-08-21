# X-103300 balanced phase/Gram replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks exact carrier-normalized operator algebra, the exact phase
monotonicity/gain formula, the half-divisor convolution square root, the cubic
B-spline autocorrelation phase relation, and the exact local-cone counterexample.

It is fail-closed: `BPOE103300` and RH remain false in the retained status
object.
