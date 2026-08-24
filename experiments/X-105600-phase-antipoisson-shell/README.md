# X-105600 — Phase barycenter, anti-Poisson and height-shell replay

This deterministic exact-rational replay authenticates finite algebra used by
`L-105600--L-105603` and `T-105600`:

- the Herglotz phase probability law and unit-phase barycenter;
- directional and full phase-variance identities;
- equality with the differential/Newton microscope;
- the downward-base signed kernel and hyperbolic threshold;
- core/tail inequalities behind the local-hole condition;
- the positive finite-measure spatial-infinity coefficient;
- polynomial height-shell degree and derivative-ladder telescoping;
- the even-integer `<2` shell gate;
- the frozen reciprocal-source multiplier `(1+h n)` and coefficient positivity.

Run:

```bash
python3 experiments/X-105600-phase-antipoisson-shell/verify.py \
  experiments/X-105600-phase-antipoisson-shell/results/verification.json
```

Expected verdict:

```text
PASS_X_105600_PHASE_BARYCENTER_ANTIPOISSON_SHELL
checks=2187
RH_UNPROVEN
```

The replay does **not** prove the finite-rectangle Xi `H^(1/2)` transfer,
physical one-sided-Hardy transfer, spatial-escape exclusion, the moving-saddle
theorem, or RH.
