# X-99580 — Exact finite algebra for the IHR67 attack

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
```

The replay checks finite coefficient algebra and mutation firewalls. It does not
prove the global prime-log transport, IHR67, or RH.
