# X-28001 — Exact eta/Mersenne algebra replay

Run:

```bash
python experiments/X-28001-eta-mersenne/verify.py
```

The verifier uses only Python's standard library and integer arithmetic.  It
checks, through the retained finite range:

- the Dirichlet-convolution inverse of the eta coefficients;
- coefficientwise equality of the central Neumann series and `1/eta`;
- the product-six coefficients `a*a(4)=1`, `a*a(6)=-2`;
- the dyadic divisor-prefix formula;
- every atomized carry image through parent 256;
- the central Mersenne exception;
- the exact averaged one-third threshold.

It does **not** verify the reflected Mersenne Boundary Recurrence or RH.
