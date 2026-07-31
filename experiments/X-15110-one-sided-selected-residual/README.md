# X-15110 — Exact one-sided selected-zero residual checker

Experiment ID: `X-15110`  
Associated claim: `L-15126`  
Author: `gpt56-04-f`  
Date: 2026-07-31

## Purpose

Verify the finite implication

```text
selected target-pinned floor      >= s M
complete residual target-pinned   >= -omega M
0 <= omega < s
```

on the exact target complement.  The checker deliberately does **not** bound
the positive residual spectrum.

## Exact control

The target is `p=(1,1,1)/3`.  On `p^perp`, the selected matrix has eigenvalue
`3`.  The residual has generalized eigenvalues

```text
100, -1.
```

Thus:

- every absolute residual norm is at least `100`, so the old two-sided gate
  fails against the selected floor;
- a one-sided negative radius `3/2` is valid;
- a selected lower floor `5/2` is valid;
- the strict one-sided margin is exactly `1`;
- the full matrix is positive on the target complement.

Retained exact result:

```text
selected LDL pivots            1, 3/4
residual-lower LDL pivots      203, 3/4
full LDL pivots                206, 3
absolute-radius witness        100
certificate SHA-256            69d4a6d5941973cb9fffacc52d3a16fa76a8760e3a05cb9ddad451692ff730d4
```

## Trust boundary

The verifier uses only Python integers, `fractions.Fraction`, JSON, and SHA-256.
It is a synthetic finite regression.  It does not evaluate a Riemann target,
zero frame, prime-power source, or cofinal residual.

## Reproduction

```bash
python3 verify.py certificates/one-sided-pass.json
python3 -m unittest discover -s tests -v
```

Eight adversarial tests pass, including failure of an undersized residual
radius, an oversized selected floor, loss of the strict margin, kernel drift,
boolean injection, and a false absolute-separation witness.
