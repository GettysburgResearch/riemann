# X-15305 — Certified-frame and radical-tail cofinal gates

This experiment is the exact scalar companion to `L-15307`, `L-15308`, and
`T-15303`.

It checks the final proof-facing arithmetic

```text
beta = sigma2 - visible_residual_lower_loss
                - visible_ambient_cross_squared / ambient_coercivity

visible Schur floor = beta > 0

epsilon = radical_lower_loss
        + radical_row_dual_squared
        + assembly_radius

global floor = -epsilon.
```

The checker uses only Python integers and `fractions.Fraction`. It does not
produce any zeta-zero, symbol, tail, cross-map, or form-domain estimate. Those
are typed upstream source gates.

## Retained control

```text
sigma2                       5/2
visible residual loss        1/5
cross squared                1/4
ambient coercivity             2
visible Schur floor         87/40

radical lower loss          1/100
radical row dual squared    1/200
assembly radius            1/1000
complete negative loss       2/125
```

Proof-object SHA-256:

```text
759fc3158c1e83a59721344c4f323f1fe0c30191d913df3c4d1d0aeb631abfb6
```

Verification SHA-256:

```text
c1a2b2abb027828d9ad5c3429a1f795b52fd0ea71170dfab43dcd2b339cab1c5
```

Eight mutation/adversarial tests pass locally.

## Commands

```bash
python3 experiments/X-15305-zero-frame-tail-gates/verify.py \
  experiments/X-15305-zero-frame-tail-gates/certificates/synthetic.json

python3 -m unittest discover -v \
  -s experiments/X-15305-zero-frame-tail-gates/tests
```

## Proof boundary

A production certificate must source-bind:

- the whitened certified-zero or other positive frame;
- the omitted-zero/symbol residual lower and cross envelopes;
- the ambient coercivity metric;
- the complete radical-tail dual norm;
- the exact or directed assembly radius.

A positive visible midpoint or a finite diagonal tail estimate alone is not a
certificate.
