# X-106450 — Endpoint-kernel correction replay

Run:

```bash
python3 experiments/X-106450-resolvent-frontier/verify.py \
  --output experiments/X-106450-resolvent-frontier/results/verification.json
```

The replay checks the exact fixture

```text
U=z^-1, N=1, D=z, g=1:
  H_U(1) != 0,
  H_U(Dg)=H_U(z)=0.
```

It also checks the endpoint numerator identity and the exact fourth-endpoint
full-Hankel allowance `237/2500`.

It does not evaluate Xi, compute a companion residue Gram, prove
`RESGRAM106450`, prove ninety percent, prove density one, or prove RH.