# X-100400 exact replay

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
```

The replay checks exact shifted-square scaling on rational-square fixtures,
the negative atom-free collar witness, unique largest-prime ownership for all
squarefree integers through 20,000, and the exact phase-Hasse decomposition on
finite rational phase fixtures.

The replay does not prove `QACG100400`, `LPMW100410`, or RH.
