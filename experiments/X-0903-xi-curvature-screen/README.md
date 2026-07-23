# X-0903 — Broad xi-curvature and differential reconnaissance

Status: ordinary numerical discovery; no Riemann--Siegel remainder and no ball arithmetic.  
Agent: `gpt56-01-c`  
Issue: #42  
Dependencies: D-3201/L-3201 and the proposed L-4101 differential witness.

## Question

Does the unusually low complete-prime Weil carrier basin also exhibit a
negative pointwise `xi'/xi` curvature or right-side differential signature, and
do random unknown-height samples nominate a stronger location?

## Search performed

- 600 deterministic random integer carriers on `[3e12,6e12)`;
- 101 points in a `0.1`-spaced neighborhood of the optimized carrier;
- five independent 1,000-point deterministic random batches on
  `[3e12,1e13)`;
- total: **5,701** no-remainder curvature screens.

The curvature screen is the X-0901 Riemann--Siegel approximation to
`Re (xi'/xi)'` on the critical line. It omits the Riemann--Siegel remainder and
is only a nomination device.

## Result

- negative curvature screens: **0**;
- overall minimum:

```text
T = 4709203636353.65
curvature_no_remainder = +30.766317291130875
Hardy_Z_no_remainder = -259.8439819576623
```

The optimized Weil carrier remained the smallest sampled curvature, but it was
not close to the pointwise sign boundary.

At the adjacent fine-grid point `t=4709203636353.6309`, ordinary 30-digit
second-derivative evaluations gave the proposed L-4101 quantity

```text
D = Re F'(s) + Re F(s)/x
```

as positive for every tested `x`:

```text
x=0.0001  D=+61.51716658187289582884679
x=0.001   D=+61.51687704262896431651287
x=0.005   D=+61.5098588002472014746892
x=0.01    D=+61.48793781554332073546519
x=0.05    D=+60.79517823890546276123596
```

No candidate is created.

## Reproduce

A batch is generated with

```bash
python batch_scan.py --seed 2026072302 --count 1000 \
  --low 3000000000000 --high 10000000000000 --workers 8 \
  --output batch.json
```

The differential points are generated with

```bash
python xi_differential.py 4709203636353.6309 \
  --xs 0.0001 0.001 0.005 0.01 0.05 --dps 30 --workers 5
```

## Proof boundary

- The curvature screen omits the Riemann--Siegel remainder.
- All array arithmetic is ordinary floating point.
- The differential evaluator uses high-precision mpmath, not directed balls.
- A positive finite scan proves nothing about RH.
- Any future negative must be reproduced at an exact dyadic point with an
  outward enclosure excluding zero from `xi(s)` and placing the complete sign
  interval below zero.
