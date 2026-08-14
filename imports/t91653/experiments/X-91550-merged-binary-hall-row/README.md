# X-91550 — merged binary Hall and component-row replay

This standard-library directed replay is run on the current live factor-54
descendant.  It certifies, throughout the stronger window `1 <= x < 55`:

- every no-upward Hall prefix for the survival target corridor
  `4/3 <= alpha <= 3/2`;
- every no-upward Hall prefix for the survival score channel `alpha=5/3`;
- every no-upward Hall prefix for both hazard corridors
  `1 <= alpha <= 6/5`;
- monotonicity of `Q_Y(j)/(alpha sqrt(Y)-1)` simultaneously for every
  `1 <= alpha <= 5/3`, every row `2 <= j < 55`, and every activation cell.

The actual survival/hazard parameter ranges are strict subsets of these
corridors for every `p>=67`.

All signs use exact `Fraction` arithmetic with directed rational square-root and
logarithm enclosures.  The replay does not certify the outer factor-54 loss
assembly or RH.

```bash
python3 verify.py
```
