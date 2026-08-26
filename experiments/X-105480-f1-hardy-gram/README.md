# X-105480 — F1 Hardy–Gram replay

Run

```bash
python experiments/X-105480-f1-hardy-gram/verify.py
python experiments/X-105480-f1-hardy-gram/tests/test_verify.py
```

The replay checks:

```text
weighted Hardy l1-to-l2 Cauchy;
closed complex cell-square formula;
uniform endpoint-square inequalities;
exact finite Gram expansion and positivity;
ratio-eight support;
diagonal/off-diagonal orientation;
endpoint jump Hilbert comparison;
finite jump-square ledger;
explicit linear-loss source-blind counterexample;
compact autocorrelation support and kernel supremum.
```

It authenticates finite algebra and the stated firewalls.  It does not prove
`F1GRAM105480`, `F1HCNC105481`, `F1HARDY105470`, `BCI102990`, or RH.
