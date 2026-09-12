# CFC26 — calibrated connected ferromagnetic completion

**Proposed component mathematics, pending independent review. RH and all-order
theta reachability remain open.** This is not an integration or acceptance PR.

Read [PROOF.md](PROOF.md), then [REASSESSMENT.md](REASSESSMENT.md) and
[VALIDATION.md](VALIDATION.md).

The main theorem attaches a positive connected infinite chain to any finite
ferromagnetic core, imposing exactly the theta coefficients of h log h, h and
log h in its real-field logarithmic MGF. The complete fixed-disk perturbation
is O((log N)^2/N), with an explicit full-tail bound. A nonsingular finite
moment jet can be retained exactly by a proved small core-weight correction.

Applying this theorem to ICR26's proposed native core yields a connected
infinite model matching theta moments through degree fourteen, with analytic
density, real Fourier zeros, and the complete three-term growth calibration.
One deliberately enormous sufficient cloud length is N=10^1000. Its root is
defined by a contraction in the original seven-dimensional box, not by
rounded fitting parameters or an enumerated huge graph. Its sixteenth moment
still differs from theta, so the model is NOT Xi.

A structural consequence is equally important: these calibrated connected
laws have exactly the same bounded-variance closure as finite ferromagnetic
magnetizations. Matching the growth coefficients therefore adds no new
all-order reachability theorem. The remaining missing statement is displayed
as OPEN-CFC in the reassessment.

The fresh checker uses exact integers/Fractions and finite full-spin
enumeration for bounded general controls. ICR_PARAMETERS.json and
ICR_RECEIPT.json are byte-preserved IMPORTED source inputs, not a new moment
calculation. The original ICR26 backend was separately replayed in both modes;
its theta source and scope stay inherited. No new full infinite root was
numerically evaluated, no higher native moment was newly matched, and no
formal or repository-wide build is claimed.

Replay the new packet:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B -O test_rejections.py --optimized
```

`--emit` is producer-only. Accepting mode authenticates the exact inventory
and the imported identities, regenerates every bounded control, and compares
canonical JSON with strict type/duplicate-key handling.

Suggested branch: `research/astra/20260912-calibrated-ferromagnetic-completion`
Suggested base: #871 at `43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3`.
This packet adds only its own new standalone directory. Publication status is
recorded in the external delivery receipt, not inferred from this suggestion.
