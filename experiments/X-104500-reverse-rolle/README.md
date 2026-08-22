# X-104500 — Exact reverse-Rolle and Riccati algebra replay

Run:

```bash
python3 verify.py --output /tmp/t104500.json
cmp /tmp/t104500.json results/verification.json
```

Expected:

```text
PASS_T104500_XI_RICCATI_ROLLE_EXACT_ALGEBRA
f855b1b266df57938d94694c624449bb895f853b7931dc8c45bff5235d533c27
```

The checker uses only exact rational arithmetic.  It verifies:

- 25 global polynomial defect-conservation identities;
- 310 bounded-interval edge and boundary identities;
- 25 Riccati and positive-residue identities;
- the exact factor-two quartic counterexample.

It does not evaluate Xi, replay external derivative-zero estimates, prove
`GBOX104500`, prove `RPCH104500`, or prove RH.
