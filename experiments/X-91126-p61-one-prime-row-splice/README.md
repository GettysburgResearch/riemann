# X-91126 — Directed `P_61` one-prime inherited-row splice certificate

This replay certifies the finite and directed numerical gates used by `L-91347`.

It performs:

- an exact merge of all `2^18=262144` signed divisor states of `P_61`;
- fixed-denominator directed bounds for `beta_61`, `M_61`, and `E_61`;
- exact inherited-row signed-measure geometry through `j=66`;
- complete activation-spline scans for `p=67` and the bulk anchor `p=71`;
- exact rational comparisons for the two analytic margins.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_P61_ONE_PRIME_ROW_SPLICE
```

The replay certifies the displayed finite corridors. The proof that these corridors imply every `p>=67` row is analytic and recorded in `L-91347`. It does not certify simultaneous positive source typing or RH.
