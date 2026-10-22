# X-94000 standalone reset-candidate exact regression

Run:

```bash
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The replay is intentionally lightweight. It authenticates the exact negative witness, affine-cell compression, hybrid same-row algebra, capacity constants, genealogy, and route firewalls. It does not replay the large directed Target–Lorenz certificate, the retained-cell analytic error theorem, or the analytic endpoint consumer.
