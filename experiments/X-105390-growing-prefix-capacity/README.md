# X-105390 — Growing-prefix capacity replay

This standard-library replay authenticates the exact reciprocal-square
Vandermonde and exponent algebra used in `L-105390` and `T-105390`.

Run:

```bash
python -B experiments/X-105390-growing-prefix-capacity/verify.py \
  --output experiments/X-105390-growing-prefix-capacity/results/verification.json
```

Expected verdict:

```text
PASS_X_105390_GROWING_PREFIX_CAPACITY
```

The checker performs 200 exact rational checks:

```text
192  tangent/cotangent k-atom Gram determinant, trace and lower-proxy checks;
8    growth-exponent inequalities for k=1,2,3,4.
```

It verifies exactly that, after omitting the harmless positive powers of pi,

```text
det(V D V^T)=det(V)^2 product(D_jj)>0
```

for consecutive reciprocal-square atoms in both parity models, and it checks
that

```text
gamma*d_k < 1/2,
gamma*(d_k+1) < 1/2
```

for the retained test exponents.

The replay does **not** evaluate Xi or authenticate the analytic real-saddle
concentration, the growing complex-strip approximation, the existence of the
actual growing real critical prefix, the omitted critical tail, or RH. All
such result flags are false.
