# T-94000 publication handoff

Intended branch: `research/gpt56-pro/94000-standalone-reset-rh-candidate`  
Intended base: `main` at `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`.

The packet is add-only. The deterministic external archive contains a one-command publisher and an add-only patch.

Commit message:

```text
research reset: standalone affine-Volterra RH candidate
```

Validation:

```bash
cd experiments/X-94000-standalone-reset-candidate
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c standalone/2026-08-16-standalone-reset-candidate/CONTENT_SHA256SUMS
sha256sum -c T94000_CONTENT_SHA256SUMS
```
