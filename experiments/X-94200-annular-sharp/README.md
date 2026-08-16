# X-94200 — annular SHARP regression

```bash
python3 verify.py
```

The checker solves the original lower-triangular average-binomial system at
high precision. It tests native and scale-four annular row positivity and
response reconstruction at deterministic endpoints, including nonmultiples of
four. It also verifies a negative control: the unsmoothed step target has a
negative inverse row.

It does not prove the symbolic four-block identity or RH.
