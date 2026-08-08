# X-28101 — Fixed-dyadic top source and common-fiber congruence

Run:

```bash
python experiments/X-28101-fixed-dyadic-top-source/verify.py
```

Expected output:

```text
PASS_EXACT_FIXED_DYADIC_TOP_SOURCE_AND_FIBER_CONGRUENCE
cases 5
mutation tests 7/7
proof-object SHA-256 b8980012fe9f4b116b77e1e4c6c2bd70dc323cb5e74113c5aa3070c4c12b3fc
```

The checker uses only the Python standard library and exact integer/Fraction
arithmetic.

Verified:

- top prime-anchor normal form on finite controls;
- support floor of the top source;
- vacuity of a radix `Q=V`;
- nonvacuity of the fixed radix `Q=2`;
- `D_2=b_2*H_(K,V)`;
- `S=omega_2*H_(K,V)`;
- both causal dyadic recoveries;
- finite PSD common-fiber congruence.

Not verified:

- the independent-frequency physical boundary map;
- a production factor-five LMI;
- the cofinal boundary recurrence;
- RH.

Verifier SHA-256:

```text
9ec17dc9e58e03d537dcb0f50c23381a08ede3a413f46b98f2964162460f6bb1
```

Result-file SHA-256:

```text
bda070ba46d4bbf2eae6bf1b4533affa0da838e0f1f19cc98cae6da50a96d7c1
```
