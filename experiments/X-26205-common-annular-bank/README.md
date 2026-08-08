# X-26205 — Common annular bank embedding and parity no-go

This standard-library exact replay supports:

- `L-26213`, the common weighted annular bank embedding;
- `R-26202`, the rank-one unequal-channel transition obstruction.

Run:

```bash
python experiments/X-26205-common-annular-bank/verify.py
```

Expected verdict:

```text
PASS_EXACT_COMMON_WEIGHTED_ANNULAR_EMBEDDING_AND_PARITY_NO_GO
```

Retained proof-object SHA-256:

```text
a965f12f7bb2dad4e9186f8a83e5c0226b8d5ee14c60a8d448f1f566aaf51cad
```

The checker uses `fractions.Fraction` only. It verifies:

1. `F_(a*x)(r)=sum_d a(d)F_x(floor(r/d))` on deterministic signed sources;
2. equality of the physical weighted norm and the common-potential norm;
3. equality with one common oversupport carry row;
4. exact `1/d` weighted dilation scaling;
5. 400 exact real specializations of
   `det(vv*-T*vv*T)=-|v1v2|^2|a-b|^2`.

It does **not** prove:

- an upper estimate for the digital-bank observations;
- the factor-five transition/collar recurrence;
- RH.
