# X-zeta23-diagonal-heat-wedge

Finite controls for the growing-resolution positivity theorem stacked on PR #384.

The replay checks:

- the exact saddle identity `t/2-t^2/(4q)=q/4-(t-q)^2/(4q)`;
- the `q exp(q/4)` scale of the continuum all-integer prime envelope;
- decay of `q^(5/2)exp(q/4)/log x` when `q=(4-epsilon)log log x`;
- growth above the constant-four phase-blind boundary;
- the depth-sensitive resolution scale `q~(log log x)/y^2`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_GROWING_RESOLUTION_HEAT_WEDGE
```

The replay is a finite diagnostic. It does not prove Guinand--Weil, the gamma lower bound, signed prime cancellation, the boundary case, or RH.
