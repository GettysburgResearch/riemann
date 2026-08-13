# X-91651 — T-91652 full-ledger lock validator

Run from a full git checkout:

```text
python3 experiments/X-91651-t91652-ledger-lock/verify.py
```

The validator checks every local and external path/blob pair in

```text
integration/2026-08-13/t91652-full-ledger-lock.json
```

using Git's blob hash, verifies source commits, rejects duplicate paths, and enforces the partial-scope restriction on refuted `L-91112`.

The script fails closed. External source commits must be present in the local object database. This artifact validates repository provenance only; it does not validate the mathematics.
