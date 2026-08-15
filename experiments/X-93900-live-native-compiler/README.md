# X-93900 — Live native source-to-physical-row compiler

This experiment replaces toy vector fixtures with the actual finite formulas.
It enumerates every active `P_61` divisor on the hostile leaf `(p,y)=(67,13)`,
constructs the actual parent/child causal atoms, applies one Target-Lorenz
coefficient to the equality and reserve channels, evaluates every component row
`2..871`, every ordinary column `2..871`, and forms radix-four detail only after
ordinary `q` and `4q` are assembled on the same row.

Run:

```bash
python3 live_compiler.py --output /tmp/live_certificate.json --summary results/live_certificate.summary.json
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile live_compiler.py verify.py tests/test_verify.py
```

The universal all-parameter row signs remain supplied by the frozen complete
AVLT theorem. This replay is the live arithmetic compiler/regression and does
not establish RH.
