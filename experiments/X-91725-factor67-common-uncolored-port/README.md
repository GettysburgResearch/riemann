# X-91725 — Factor-67 one uncolored common-port replay

Run:

```bash
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_ONE_UNCOLORED_COMMON_PORT
```

The checker uses exact `Fraction` arithmetic for positive-semidefinite `2x2`
port matrices.  It verifies positive integration of fiberwise port
inequalities, zero recursive-child port ownership, common safety thinning, the
uniform `<252` port-mass bound, and three hostile mutations.

It does not replay the analytic `P_61` port construction, physical causal
generator, root Hall, actual finite correction demand, terminal theorem, or
endpoint consumer.
