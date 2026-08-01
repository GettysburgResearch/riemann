# X-16204 — Directed cofinal CCM wrapper

This experiment is the exact finite consumer for `T-16205`.

It verifies one support-block certificate containing:

- the rational radial stationary window `[17/8,9/4]`;
- the exact higher-alias moat `1/50`;
- the exact stationary second-derivative moat `11/12`;
- the fold cubic interval `[8,60/7]`;
- a 2,048-box exact rational proof of the Airy phase enclosure;
- an a-posteriori interval-ODE radial residual;
- the `p=4` Poisson endpoint and alias-tail ledger;
- a positive-measure cofinal good-support calculation;
- the profile-Gram floor;
- the relative local-Weyl error;
- the final target/gap ratio.

The retained certificate is synthetic. Its radial primitive contains no PSWF or
zeta data. It demonstrates the exact proof-object boundary only.

A production certificate must replace the synthetic interval-ODE and Gram
digests with source-bound directed artifacts while preserving the schema.

Run:

```bash
python verify.py certificate.json --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Retained result:

```text
classification                       EXACT_COFINAL_CCM_WRAPPER_BLOCK
cofinal good-measure lower bound     97/100
relative scalarization epsilon       13/500
target/gap ratio                     7/316
tests                                10/10 pass
proof-object SHA-256
3b9615ecc0bdc14a00f24c45953b8ce4350fe875b6da3fb6edad9c4cdb09657c
```

No production CCM block and no RH proof are claimed.
