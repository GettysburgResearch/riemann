# X-91666 — full direct-row closure algebra

This standard-library directed replay supports `L-91666`, the exact native
response identities used by `L-91667`, and the algebraic shell of `T-91654`.

Run:

```bash
python3 verify.py --json results/verification.json
```

Expected:

```text
PASS_FULL_DIRECT_ROW_CLOSURE_ALGEBRA
proof object: 2162b25bbfc824848bdd1fbf9bdf074f07194de23d21de510c48d39c0f33004d
```

The replay is deliberately scoped. It does not rerun the expensive frozen Hall,
outer equality, mismatch, collar, terminal, or endpoint-port certificates and
sets `rh_established_by_replay=false`.
