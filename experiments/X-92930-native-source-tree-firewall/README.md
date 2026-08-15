# X-92930 — Native-source / rough-lift normalization firewall

Run:

```bash
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
```

The replay checks the exact rational inequalities behind the conditional
`109/1200` calculation, records its withdrawn PR-specific scope, distinguishes a
native current-plus-actual-child source identity from a row-first rough lift,
checks the two-ledger response complement, and authenticates the `<61744`
root-plus-terminal-child arithmetic. It does not replay the frozen analytic
source compiler or endpoint-to-RH chain and does not prove RH.
