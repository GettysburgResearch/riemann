# X-105446 — Six-dimensional differential-microscope replay

Run from the repository root:

```bash
python -B experiments/X-105446-six-dimensional-microscope/verify.py
```

Expected output:

```text
PASS_X_105446_SIX_DIMENSIONAL_MICROSCOPE
1c895a14a0e7f91bc9de158e8ce42633ac5efbd795f62b7623506f3e82b28487
checks= 57
```

The exact `Fraction` replay checks:

- the elliptic equation for the differential microscope;
- the `C=h^3 W` conversion to the six-dimensional axisymmetric Laplace equation;
- the Newton-kernel contribution of a critical residue;
- the regular zero-height trace on the cubic fixture;
- the dual top-zero/top-critical capacity calibration for `F=z^2-1`.

It does **not** replay the strong maximum principle, the completed-zeta coarse
asymptotic, Xi zero-height escape exclusion, or RH. The retained result records
all of these boundaries fail-closed.