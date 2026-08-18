# X-98800 — Score-free Hall / native-dual exact algebra replay

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

The checker uses only the Python standard library.  It verifies exact finite
algebra and mutation firewalls.  It does not replay the inherited large Hall,
interval, endpoint, or zeta-analytic campaigns and does not prove RH.
