# X-20706 — Exact source-resolvent regression

This finite rational experiment checks the algebra of `L-20704` independently
of any floating matrix inversion.

Run:

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

The certificate is synthetic. Its purpose is to make the two proof consumers—
block shorting and scalar resolvent/Sherman--Morrison—fail closed before they are
used on a directed D-0001 packet.
