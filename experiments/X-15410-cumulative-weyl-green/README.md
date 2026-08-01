# X-15410 — Cumulative Weyl, Green-lift, and Jordan exact regression

Status: exact finite rational algebra  
Agent: `gpt56-05-l`  
Claims: `L-15421`--`L-15424`, `T-15409`  
Issue: #180

## Checks

The standard-library verifier reconstructs four finite identities:

1. the factor-four horizontal derivative law behind
   `partial_omega D_omega = (4/pi) K_omega^W`;
2. the endpoint primitive
   `(||M_+||^2-||M_-||^2)/2`;
3. one exact quotient Green-lift contraction `T=C K E`, including the positive
   defect `I-T^T T`;
4. the generalized Jordan normalization and divisor carré du champ.

Retained values:

```text
horizontal derivative weight  58/35
Weyl weight                    29/70
endpoint cumulative energy      7/12
Green defect pivots             3/4, 7/16
Jordan mean                    -161/144
Jordan variance                 38735/20736
```

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

Seven deterministic tests passed in the authoring session. They reject a false
flow factor, a bad right inverse, a noncontractive multiplier, an incomplete
divisor manifest, a false Jordan variance, and Boolean integer fields.

## Proof boundary

This experiment verifies exact finite algebra only. It does not prove that the
normalized Volterra quotient norm equals the physical/original Riemann Weyl
metric. That metric identification is the smallest remaining positive gate.
