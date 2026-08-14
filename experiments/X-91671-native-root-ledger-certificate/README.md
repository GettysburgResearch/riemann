# X-91671 — Native root ledger certificate regression

Run without arguments for exact synthetic controls:

```bash
python3 verify.py --json results/verification.json
```

Expected verdict:

```text
PASS_NATIVE_ROOT_LEDGER_CERTIFICATE
```

The checker enforces the repaired P61/67 normalization, required d=1,d=2,d=5 occurrences, exact local native identities, atomwise source partition, one shared port channel, and exact global reconstruction. It also rejects a deliberate 3/5 + 3/5 source overdraw.

A live certificate may be supplied with `--certificate path.json`. The retained regression does not itself export the live L-91659 source/channel matrix and does not prove RH.
