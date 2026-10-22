# X-30101 — Recombined common-tail Euler audit

Run:

```bash
python experiments/X-30101-recombined-tail-euler/verify.py
```

Expected classification:

```text
EXACT_RECOMBINED_COMMON_TAIL_EULER_MISMATCH_VERIFIED
```

The checker uses only Python's standard library and exact `fractions.Fraction` arithmetic. It verifies:

1. the rational control
   ```text
   D_1+D_2=4/5,
   D_1-D_2=8/15;
   ```
2. the distinction between the ordinary Hausdorff kernel `1/(1-y)` and the alternating kernel `1/(1+y)`;
3. 10,496 exact instances of the interlacing telescope;
4. 2,277 exact direct-pair recombination identities.

It proves no asymptotic theorem and no RH conclusion.

Retained proof-object digest:

```text
6d0b3839f4c1062229a226535abd6fc6e1289b47ac57b13a7a8fd1972fe99338
```
