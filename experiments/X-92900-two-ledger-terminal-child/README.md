# X-92900 — Two-ledger root and terminal-child exact regression

This lightweight checker authenticates only the finite composition algebra added
by `R/L/T-92900`.

It verifies:

```text
signed observation defects are not accepted as positive source;
positive source ownership is disjoint;
unused capacity minus signed overfill is nonnegative;
current + children + root slack reconstructs the native vector;
factor-67 root target mass gives child deficit <6039/8;
60989 + 6039/8 = 493951/8 <61744;
seven hostile mutations fail closed.
```

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
```

Expected verdict:

```text
PASS_TWO_LEDGER_TERMINAL_CHILD_FACTOR67_ALGEBRA
```

Proof-object digest:

```text
64b4f13c625802462641fd36d20494ed35c07e287623a28195821934bb2b983b
```

The checker does not replay the frozen Hall/profile inequalities, endpoint
integrals, all-column analytic estimates, PNT, prime-square asymptotic, Mellin
transform, Landau theorem or prove RH.
