# X-28002 — Exact `omega_(2,3)` critical prefix bank

Run

```bash
python experiments/X-28002-omega23-prefix-bank/verify.py
```

The checker uses only Python's standard library and integer arithmetic.

It verifies through every cutoff `2<=R<=256`:

```text
finite hyperbola reconstruction coefficients   32,640
strict multiplicative delay pairs              170,444
local Euler coefficient formulas                   256
max |omega_(2,3)(n)|                                  4
```

It also verifies that deleting the `d=2` synthesis term makes the coefficient at
`m=2` equal to `2`, so the complete source bank is mandatory.

Retained digest, computed before inserting the digest field:

```text
6acf516e24858910b6865d091123a04fa8a74c28a6a9f03f311e59c6f1f60a8f
```

## Assurance boundary

The replay proves finite convolution and delay-support algebra. It does not
prove:

```text
BTEBC;
the physical upper estimate for the prefix observations;
a strict physical source reserve;
the Riemann Hypothesis.
```
