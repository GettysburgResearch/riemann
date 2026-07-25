# X-8401 — Exact checker for certified critical-line-zero deflation

`verify.py` is a small standard-library checker for the finite algebra in
L-8401 and L-8402.

It supports:

- `scalar-count-deflation`;
- `pick-count-deflation` for arbitrary-height exact complex points and vectors.

All arithmetic after JSON parsing uses Python integers and
`fractions.Fraction`. The checker does **not**:

- evaluate `zeta`, `xi`, `xi'/xi`, or Hardy `Z`;
- certify a zero count;
- prove D-3201/L-3201/L-3202;
- establish implementation independence.

Those are explicit logical or trusted-base obligations.

## Core rules

1. Zero bins must be strictly disjoint.
2. Counts must be positive integer lower counts.
3. Only lower contribution bounds are subtracted.
4. Fixed-vector Pick matrices are contracted before primitive rectangles are
   widened.
5. A residual touching zero is unresolved.
6. Logical-gate manifests must match exactly and no gate may remain blocking.

## Synthetic controls

### Positive ordinary scalar, negative deflated scalar

At `x=1/20`, a line zero contributes `20` and an off-line reflected pair at
`delta=1/10` contributes `-40/3`. Thus the ordinary scalar is `20/3>0`. A broad
certified line-zero bin guarantees subtraction `10`, leaving `-10/3`.

### Positive ordinary Pick form, negative deflated Pick form

At the same one-point sample with vector `1`, the ordinary Pick form is `400/3`.
The exact line-zero Gram contribution is `400`, leaving `-800/3`.

These are finite synthetic models only. They demonstrate strict logical strength,
not an actual Riemann-xi candidate.

## Commands

```bash
python verify.py certificates/synthetic-hidden-offline-scalar.json
python verify.py certificates/synthetic-online-scalar-control.json
python verify.py certificates/synthetic-hidden-offline-pick.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Expected tests: `9/9` pass.

## Proof boundary

An actual negative needs:

1. proof-grade Issue #39 primitive `F` rectangles;
2. unconditional certified critical-line zero bins;
3. exact X-8401 replay;
4. independent directed special-function reproduction;
5. independent analytic review of the parent passivity criterion.
