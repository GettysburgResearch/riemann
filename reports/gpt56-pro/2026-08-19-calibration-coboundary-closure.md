# Integrator report — calibration as a Bellman coboundary

The newest endpoint-nested route and the distributional Volterra audit appear
to disagree only because the signed calibration was being treated as a new
debt at every recursive node.

The exact frame algebra shows otherwise.  If the full frame is `E=P+A` and
the positive frame is `P=J+PT`, the local calibration is `A-AT`.  The complete
tree resolves to

```text
E = J(I-T)^(-1) + A.
```

The root compact calibration is the entire defect.  Descendant calibrations
cancel.  This converts PR #641's bounded-defect argument from a geometric
estimate into an exact telescoping identity and removes its pending signed
ledger interface.

The distributional factorisation

```text
d(Vf) = x d[x^(-1/2)(D-1)f]
```

makes the primitive calibration canonical and finite-dimensional: one
bounded-variation state, its activation jumps, and two boundary modes.

The resulting candidate avoids every known parity/oriented-child obstruction
because it never observes a child separately and never selects a terminal
orientation after accumulated rough parity.

Scientific status: proposed complete candidate on the frozen compact Hall and
endpoint-frame inputs; RH remains unproved pending hostile reconstruction.

The exact retained-cell identity from PR #513 is used only as a source-level cross-check: its positive direct integral enters `P`, while its signed cell error enters the root potential `A`. The parity-sensitive Target–Lorenz terminalization from that historical branch is not imported.
