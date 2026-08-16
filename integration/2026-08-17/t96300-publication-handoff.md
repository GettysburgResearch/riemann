# T-96300 publication handoff

Base PR #544 at `d4dcd1256dc9c8e110c860cff87b3f89aee842a5`.

Suggested branch:

`research/gpt56-pro/96300-annular-gap-single-row-assault`

Commit message:

`attack complete gap annulus and single reciprocal row`

Replay:

```bash
cd experiments/X-96300-two-front-assault
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c standalone/2026-08-17-two-front-assault/CONTENT_SHA256SUMS
sha256sum -c T96300_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T96300_RADICAL_TWO_FRONT_ASSAULT_ALGEBRA
fa2cacdc80a74b9bf8d7a1fe9fe561b2aa898184e590ae9ca0b2fa0f6ca57d18
```
