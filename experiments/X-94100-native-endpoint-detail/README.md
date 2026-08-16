# X-94100 — Native endpoint-detail compiler replay

Run:

```bash
python3 generate.py --endpoint 256 --output results/certificate-X256.json
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile generate.py verify.py tests/test_generate.py tests/test_verify.py
```

`generate.py` emits the complete endpoint-scale certificate: every endpoint
owner, greedy coefficient, physical row coefficient, ordinary `q`, ordinary
`4q`, radix-four detail, native target, slack, `Y_4` weight, score and endpoint
deficit. It evaluates the actual parabolic/carry formulas, not synthetic
vectors or a schema-only fixture.

The analytic proof of `L-94100` is general. The finite high-precision grids and
the `X=256` certificate are deterministic regressions and hostile interface
firewalls, not substitutes for the proof. The experiment does not prove the
asymptotic blocker-localization statement `NEDB`, the frozen prime-square/Landau
consumer, or RH.
