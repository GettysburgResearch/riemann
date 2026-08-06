# X-22101 — Prime-ramp wavelet and resolution barrier

This standard-library experiment verifies the finite algebra behind
`L-22101` and `R-22102`.

It checks:

```text
Q_H^P = Delta_1^3 (I-2T_log4) F(.-1),
```

the eight formal translate coefficients, vanishing moments through degree two,
exact annihilation of the `exp(x/2)` pole model, and the narrow-window norm

```text
||H_delta||_2^2 = 20/(3 delta)
```

when the four translated triangular pieces are disjoint.

The retained synthetic scaling `delta_X=exp(-X)` gives diagonal Hardy exponent
`1/2`, demonstrating the resolution/diagonalization barrier.

## Replay

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Expected proof-object SHA-256:

```text
bc8da6a56ff84ed48d33706d2c4478837b6dc9169f784d7d93afec6ff4705a71
```

## Proof boundary

The checker uses exact rational/formal-shift algebra only. It contains no prime,
zeta, PNT, or semiprime computation and supplies no RH sign.
