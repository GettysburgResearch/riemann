# X-91004 — Radial curvature and depth projector

This finite regression checks:

- the Peano identity connecting the unit-disc generator to radial log-curvature;
- the safe-line derivative-jet relation;
- the exact Fourier transform of the line curvature kernel;
- the sharp centre-integral depth projector on both sides of the depth threshold;
- the signature `(1,1)` Pick block of one complex off-line pair;
- the negative rank-one Pick limit of a matched real pole;
- the negative curvature blow-up immediately to the right of an off-line depth.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR
```

The replay establishes finite algebra and synthetic numerical controls only. It proves no sign for actual Riemann data and does not prove RH.
