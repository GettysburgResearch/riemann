# X-99600 — Exact three-interface audit replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The standard-library checker verifies:

- all 66 compact SHARP Hall-prefix thresholds with outward \(2^{-40}\)
  square-root intervals;
- the exact worst state `(t,x)=(13,67)` and margin above `7/20`;
- the SHARP RN cocycle and the `(16,4,4)` raw-cutoff mutation;
- the one-prime alpha/native coefficient separator;
- the exact sequential first-owner Euler identity on all 16 monomials of a
  four-prime rational fixture;
- the exact two-row common-zero elimination;
- fail-closed status flags for `FCHD67`, Harnack negative mass, and RH.

It does not prove the remaining arithmetic sign theorem.
