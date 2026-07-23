# X-5701 — Exact conic witness-portfolio checker

Experiment ID: X-5701  
Status: exact algebraic synthetic controls  
Agent: `gpt56-06-c`  
Issue: #57  
Date: 2026-07-23  
Related claims: D-5701, L-5701, L-5702, M-5701  
Candidate IDs: none

## Purpose

`verify.py` is a tiny standard-library checker for two first certificate kinds:

- `affine-box-portfolio`: nonnegative exact combinations of affine RH-valid rows
  over shared rational interval features;
- `psd-gram-box`: exact Gram sums of frozen vectors against an affine symmetric
  matrix pencil.

The checker contracts all row or matrix coefficients before applying feature
radii. It rejects negative weights, malformed Gram terms, hidden or decorative
features, blocking logical gates, non-strict endpoints, and false claimed
endpoints.

It proves only quantitative conic separation. It does not prove any imported RH
criterion, normalization, or primitive special-function enclosure.

## Run

```bash
python verify.py --self-test
python verify.py certificates/affine-shared-cancellation.json
python verify.py certificates/psd-gram-cancellation.json
```

Expected self-test output:

```text
3 exact conic controls passed
```

## Exact controls

### Shared scalar uncertainty

\[
q_1=-2/5+u,
\qquad q_2=-2/5-u,
\qquad |u|\le1.
\]

Each row has individual robust upper `3/5`; the exact portfolio has robust upper
`-4/5`. Its combined primitive coefficient is zero, so no perturbation in the
declared one-feature space can repair it.

### PSD Gram cancellation

\[
K(u)=\operatorname{diag}(-1/2+u,-1/2-u).
\]

Each coordinate vector has robust upper `1/2`; the exact Gram multiplier
`e_1e_1^T+e_2e_2^T=I` gives robust upper `-1`.

These are synthetic algebraic controls. No `zeta` or `xi` value is evaluated.

## Proof boundary

Exact:

- rational parsing and arithmetic;
- nonnegative scalar and Gram weights;
- symmetric matrix contraction;
- shared-feature coefficient aggregation;
- interval support function;
- strict final sign;
- scale-invariant `L-infinity` feature-repair lower bound for affine portfolios;
- exact feature and logical-gate manifest equality.

External obligations:

- every imported RH-valid row or PSD condition;
- soundness of primitive enclosures;
- independence of decisive implementations;
- compiler, runtime, and hardware trust.
