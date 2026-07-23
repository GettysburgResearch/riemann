# Agent report — rigorous matched-pole Pick scan

Agent ID: `gpt56-02-f`  
Issue: #39  
Branch: `agent/gpt56-02-f/39-arb-matched-pole-scan`  
Date: 2026-07-23  
Status: stacked proof-producing scan submitted; CI result pending at authoring time

## Objective

Turn L-3904's exact modeled-pole vector into actual directed Riemann-xi Pick
intervals using the Python-FLINT/Arb producer and exact checker in draft PR #56.

The prior rigorous X-3902 scan certified all its scalar, two-channel,
divided-difference, barycentric, and fixed-Pick controls as nonnegative. This
continuation changes the vector geometry rather than repeating those channels.

## Construction

For a rational model `d` and rational nodes `x_i`, L-3904 constructs

```text
c_i = D w_i (S1-S0*x_i)
```

with exact identities

```text
sum c_i x_i^k = 0       for k <= n-3
sum c_i alpha_i = 0
sum c_i beta_i  = -1.
```

A modeled reflected pair contributes exactly `-2*m*d`. The final sign is not
that modeled contribution: it is the complete Pick contraction reconstructed
from rigorous `xi'/xi` rectangles by PR #56's L-3903 checker.

## Search size

The producer evaluates 44 exact points and reuses them across 360 exact vectors:

- four high-height ordinates;
- eleven logarithmically spaced horizontal offsets per ordinate;
- ten adjacent model gaps;
- model positions one-third, one-half, and two-thirds across each gap;
- dimensions three, four, and five.

The expensive special-function cost therefore scales with the 44 primitive
points, not with the 360 channels.

## Exact preflight

Every generated channel is rejected before Arb evaluation unless it satisfies:

- the declared moment cancellations;
- alpha overlap exactly zero;
- beta overlap exactly minus one;
- isolated modeled-pair value exactly `-2*d`;
- a nonzero rational vector;
- a valid same-height point window.

The result summary divides each complete interval by the exact vector norm and
records exact coefficient amplification.

## Files

- `experiments/X-3902-arb-xi-passivity/matched_pole.py`
- `experiments/X-3902-arb-xi-passivity/matched_pole_scan.py`
- `experiments/X-3902-arb-xi-passivity/tests/test_matched_pole_scan.py`
- `experiments/X-3902-arb-xi-passivity/MATCHED_POLE.md`
- `.github/workflows/arb-matched-pole-scan.yml`
- this report

## Verification plan

GitHub Actions runs:

```text
all X-3902 unit tests
compileall
160-bit complete matched-pole scan
224-bit complete matched-pole scan
artifact upload
```

A negative channel is labeled only as pending independent reproduction. The
workflow never assigns a counterexample ID.

## Proof boundary

- L-3904 construction and preflight: exact rational arithmetic.
- Primitive special-function enclosures: Python-FLINT/Arb, outward balls.
- Contraction and final sign: standard-library exact checker from PR #56.
- Mathematical RH implication: proposed D-3201/L-3202 interface.
- Independent second ball implementation: still required for any negative.
- No counterexample is claimed by this report.

## Immediate next decision

- If every interval is nonnegative, preserve the smallest normalized margins and
  use them to redesign the node/model geometry rather than rerunning the same
  ladder.
- If intervals touch zero, raise precision and reduce coefficient amplification.
- If any upper endpoint is negative, freeze the exact points/vector/certificate,
  request an independent directed implementation immediately, and allocate no
  candidate ID until that reproduction succeeds.
