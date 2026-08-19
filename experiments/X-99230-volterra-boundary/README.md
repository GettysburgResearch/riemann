# X-99230 — Volterra boundary replay

Run:

```bash
python3 verify.py
```

The replay checks the homogeneous roots, Green-kernel jump normalization,
boundary coefficient recovery, a positive two-anchor fixture, and a negative
anchor-cone mutation. It does not reconstruct PR #620's actual endpoint data.
