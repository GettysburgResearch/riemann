# X-91556 — binary native row-score budget

This exact symbolic replay checks the one-prime normalization in `L-91556`.

With `r=p^-1/2` and `z=sqrt(x/n)`, it certifies:

```text
survival target + hazard target = 4z-3;
(1-r^2)(5z-3) + r^2(5z-3) = 5z-3;
row coefficients (1-r^2) + r^2 = 1;
actual hazard score
  = r^2(5z-3) + r(1-r)(z-1);
both target/native-score ratios are increasing in z;
both ratios equal 1/2 at z=1;
the fixed-67 score slopes are exactly five times the row coefficients.
```

The replay uses exact SymPy algebra. It does not certify the Hall existence
inputs, directed component-row monotonicity, the native `J_Lambda` boundary,
continuum-to-finite collar assembly, final radix-four feasibility, or RH.

```bash
python3 verify.py
```
