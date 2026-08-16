# T-96200 publication handoff

Intended branch: `research/gpt56-pro/96200-affine-volterra-score-hardening`  
Base: PR #533 at `624db1e68f0197a002a542ffa37375dc7b26e197`.

Validation:

```bash
cd experiments/X-96200-normalization-score-firewall
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../X-96201-mpfr-target-lorenz-hardening
g++ -O2 -std=c++17 smoke.cpp -lmpfr -lgmp -o smoke
./smoke
cd ../..
sha256sum -c T96200_CONTENT_SHA256SUMS
```

The full MPFR workflow is deliberately separate and fail-closed. Its artifact must pass before PR #508's tail may be treated as certified.
