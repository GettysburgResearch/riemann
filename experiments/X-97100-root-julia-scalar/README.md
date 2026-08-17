# X-97100 root-Julia scalar regression

Run:

```bash
python3 verify.py certificates/control.json --output /tmp/x97100.json
cmp /tmp/x97100.json results/verification.json
python3 -m unittest discover -s tests -v
```

The replay verifies finite coefficient and formal prime-log algebra only. It explicitly does not prove `RJTE` or RH.
