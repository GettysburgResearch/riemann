# X-96400 — two-row prime-sieved hardening regression

Run:
```bash
python3 verify.py --output results/verification.json
```

The checker authenticates:

* the exact \(j=3,P=6,n=24\) same-knot residue;
* the exact \(P=30\) rough-store occupancy;
* the rows-\(2,3\) Dirichlet-convolution dictionaries;
* the finite \(2,3\)-valuation tables;
* the two-row common-zero polynomial;
* a small finite sign reconnaissance.

It does **not** prove `TRP23`, a global transport, or RH.
