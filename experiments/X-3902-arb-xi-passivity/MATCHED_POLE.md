# X-3903 — Rigorous matched-pole Pick scan

Experiment ID: `X-3903`  
Agent: `gpt56-02-f`  
Issue: #39  
Stacked base: X-3902 / draft PR #56  
Mathematical dependency: L-3904 on draft PR #52  
Status: proof-grade producer/checker pipeline; result determined by CI artifacts

## Objective

Evaluate exact L-3904 fixed Pick vectors with the rigorous Python-FLINT/Arb
producer and the standard-library exact contraction checker from X-3902.

A strict negative complete interval would be a finite RH-disproof witness through
the proposed D-3201/L-3202 interface. A negative modeled pair contribution is
not a candidate and is never used as the final sign.

## Finite search domain

The scan evaluates four exact rational ordinates:

```text
4709203636353.6309
4709203636353.6409
3157430112465.8695095
3157430112425.8695095
```

At each ordinate it evaluates eleven exact horizontal offsets:

```text
0.00001, 0.00002, 0.00004, 0.00008,
0.00016, 0.00032, 0.00064, 0.00128,
0.00256, 0.00512, 0.01024.
```

For every adjacent offset gap, the modeled displacement is placed at one-third,
one-half, and two-thirds of the gap. Exact L-3904 vectors are built in dimensions
3, 4, and 5. This gives:

```text
points:   44
channels: 4 * 10 * 3 * 3 = 360
```

## Trust boundary

Before any Arb call, every channel verifies exactly:

- all L-3904 moment cancellations;
- modeled alpha overlap `0`;
- modeled beta overlap `-1`;
- modeled isolated-pair contribution `-2 d`;
- exact rational vector and contracted coefficients.

The producer evaluates each primitive `F=xi'/xi` point by two completed-xi
assemblies and checks the functional equation through the X-3902 gates. The
existing `real-pick-rayleigh` checker reconstructs the final contraction from
outward rational rectangles.

The summary normalizes every complete interval by the exact vector norm. It also
records the modeled pair scale and the exact L1 coefficient amplification so a
small midpoint cannot hide a badly conditioned certificate.

## Reproduce

From the experiment directory:

```bash
python -m unittest discover -s tests -v
python matched_pole_scan.py \
  --precision-bits 160 \
  --certificate results/matched-pole-p160-certificate.json \
  --verification results/matched-pole-p160-verification.json \
  --summary results/matched-pole-p160-summary.json

python matched_pole_scan.py \
  --precision-bits 224 \
  --certificate results/matched-pole-p224-certificate.json \
  --verification results/matched-pole-p224-verification.json \
  --summary results/matched-pole-p224-summary.json
```

GitHub Actions workflow `.github/workflows/arb-matched-pole-scan.yml` runs both
precision levels and uploads all result JSON files.

## Promotion boundary

A channel is not promoted merely because its modeled pair score is negative.
Promotion requires:

1. a complete outward interval with negative upper endpoint;
2. stable identity and sign at increased precision;
3. an independent directed special-function implementation;
4. review of D-3201, L-3202, X-3902/L-3903, and L-3904;
5. only then allocation of a `Z-####` candidate.
