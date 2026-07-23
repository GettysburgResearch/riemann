# X-3901 — Adversarial xi-passivity scan at an optimized carrier basin

Experiment ID: `X-3901`  
Issue: #39, independent parallel attempt  
Agent: `gpt56-02-e`  
Status: ordinary high-precision reconnaissance plus exact rational kernel tests  
Created: 2026-07-23

## Question

Does the unusually low finite-Weil carrier basin near

```text
T = 4709203636353.65
```

also exhibit a scalar, differential, sampled-Pick, or shifted-Stieltjes failure
for `F=xi'/xi`?

A genuine off-line zero would create one or more compact finite witnesses. This
experiment attempts to distinguish those signals from Riemann--Siegel remainder
errors and nearly singular matrix arithmetic.

## Exact new kernel

`barycentric.py` implements L-3901 with `Fraction` arithmetic. For distinct
positive offsets `x_i`, the exact barycentric vector is

```text
c_i = 1 / product_{j != i} (x_i-x_j).
```

Under RH its Pick quadratic form is the positive resolvent-product sum

```text
sum_gamma 1 / product_i (x_i^2 + (T-gamma)^2).
```

For a same-ordinate off-line pair at displacement `delta`, the pair contribution
is

```text
2 / product_i (x_i^2-delta^2).
```

Two offsets bracketing `delta` therefore give a negative pair contribution.

## Numerical layers

- `xi_jets.py` assembles simultaneous Riemann--Siegel zeta derivatives through
  order four and converts them to `F` derivatives and low Stieltjes moments.
- Fast no-remainder curvature is nomination-only.
- Every matrix nomination is replaced by a fixed exact vector before precision
  escalation.
- The final proof path still requires directed complex balls and independent
  reproduction.

## Results

The optimized carrier center produced no surviving negative:

- scalar `Re F`: positive on the tested offset ladder;
- differential localizer: positive;
- adjacent two-point barycentric localizers: positive;
- `2 x 2` Hankel and localizing matrices: positive after sufficient precision;
- eight-point Pick/barycentric negative midpoints: precision artifacts that
  stabilize positive.

Two negative no-remainder curvature values in a `T +/- 100` scan were reversed
by simultaneous exact-point derivatives. The omitted remainder was divided by
a small approximate Hardy `Z` value.

See:

- `results/precision-ladder.json`;
- `results/carrier-audit.json`;
- `claims/observations/O-3901-carrier-basin-passivity-audit.md`.

## Reproduce exact tests

```bash
python -m unittest discover -s tests -v
python -m compileall -q barycentric.py xi_jets.py tests
```

The exact tests require only Python's standard library. Running `xi_jets.py`
requires the mpmath version used by the parent xi-passivity branch.

## Proof boundary

- Exact rational barycentric identities: algebraic tests.
- Riemann-xi point values: ordinary mpmath, not intervals.
- No negative directed sign exists.
- No `Z-####` candidate is created.

## Suggested next search

Use two-point dyadic brackets rather than ill-conditioned multi-point
eigenvalues. A stable negative midpoint should be frozen as one exact vector and
recomputed with Arb at increasing precision. Search both the scalar-left and
differential-right signatures around the same nominated ordinate.
