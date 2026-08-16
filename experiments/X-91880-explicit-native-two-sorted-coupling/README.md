# X-91880 — Exact finite regression for the explicit native two-sorted coupling

The replay checks:

```text
forced q=2 Hall-score obstruction;
two-sorted Hall residual/row-bonus algebra;
rank-one native Volterra Hall marginals;
native finite/bulk sector partition;
rough-lift exclusion;
bulk-causal-reset exclusion;
many-to-one first ownership;
single application of child coefficients;
one block realization;
identity Hall-bonus channel;
one immutable downstream row identifier;
all q<K ordinary columns;
common-row q/4q detail assembly;
terminal margin 581;
native ledger below 60989;
endpoint orientation and benchmark firewall.
```

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The replay does not prove the frozen analytic inputs or RH.
