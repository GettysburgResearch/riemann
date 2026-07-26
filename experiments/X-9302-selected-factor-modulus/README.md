# X-9302 — Selected-factor direct-xi modulus certificates

Experiment ID: `X-9302`  
Agent: `gpt56-01-j`  
Issue: #93  
Status: exact checker, production adapter, and synthetic controls; Riemann-xi production pending  
Date: 2026-07-26

## Objective

Strengthen X-9301's conservative endpoint deflation when proof-grade critical-line zero balls are available.

For a selected line zero with ordinate `gamma`, the direct completed-xi logarithmic modulus contains the exact factor

```text
log(u + (T-gamma)^2).
```

X-9301 subtracts `log(u+B)` using only a safe upper squared-distance bound `B`. X-9302 carries the directed zero ball itself, encloses the actual squared distance as an interval, and subtracts the corresponding interval-valued factor. Under RH this removes the selected zero completely in the zero-ball limit.

The checker also reports every Loewner determinant after exact division by its positive row and column Vandermonde factors. This exposes whether a tiny raw determinant comes from the residual Stieltjes measure or merely from clustered nodes.

## Files

- `verify_selected_factor.py` — standard-library exact checker;
- `adapt_x9301_selected_factor.py` — converts an X-9301 directed certificate without another special-function pass;
- `certificates/synthetic-selected-factor.json` — hidden-offline-zero regression;
- `tests/` — fail-closed checker and adapter tests;
- `results/synthetic-summary.json` — compact retained result;
- `results/tests.txt` — retained test transcript.

## Certificate schema

The top-level schema is

```text
riemann.xi-modulus-selected-factor-deflation.v1
```

A production certificate contains:

- one exact rational common ordinate;
- positive exact rational intervals for direct completed-xi modulus squares;
- exact squared horizontal nodes;
- pairwise-disjoint directed critical-line zero balls;
- a positive lower multiplicity count and immutable gate digest for every ball;
- selected-factor monotonicity or cross-Loewner rows;
- an exact logarithm-series term count.

The checker evaluates no special function and uses no floating-point arithmetic after JSON parsing.

## Supported rows

### Selected-factor monotonicity

For `0<u<v`, it encloses

```text
H(v) product_j (u + Y_j)
-
H(u) product_j (v + Y_j),
```

where each `Y_j` is the exact rational interval containing the selected zero's squared distance from the common ordinate.

### Selected-factor cross-Loewner determinant

It encloses the logarithmic residual at each point,

```text
log H(u) - sum_j log(u+Y_j),
```

constructs every secant entry, and evaluates determinants through order four using exact interval arithmetic.

It reports:

```text
raw_interval
row_vandermonde
column_vandermonde
vandermonde_normalized_interval
```

The raw and normalized intervals have the same sign because the normalization divisor is an exact positive rational.

## X-9301 adapter

`adapt_x9301_selected_factor.py` consumes an existing

```text
riemann.xi-modulus-zero-deflation.v1
```

certificate and produces the X-9302 schema by:

1. converting each directed complex completed-xi rectangle into an exact rational modulus-square interval;
2. preserving the exact common ordinate and horizontal nodes;
3. preserving every zero-ball endpoint, lower count, and gate digest;
4. translating endpoint-deflated row identities to selected-factor row identities;
5. binding the output to the canonical SHA-256 of the complete X-9301 source certificate.

Thus one successful directed PR #71 artifact can be replayed under both the conservative and selected-factor theorems without rerunning FLINT.

## Exact synthetic separation

The model

```text
H(u)=(u-5)^2 (u+1)^50
```

contains one modeled off-line dip masked by fifty selected on-line factors.

Before factor removal:

```text
raw monotonicity       +88812771367611610316284546634444121
raw Loewner determinant approximately +5.8985579416206204
```

After removing the fifty exact selected factors:

```text
selected monotonicity  strictly negative
selected determinant  -4*(log 2)^2
normalized determinant approximately -0.213534672852534
```

Both negative rows are certified by integer/Fraction arithmetic. This is a synthetic checker control, not a Riemann-xi result.

## Reproduction

```bash
cd experiments/X-9302-selected-factor-modulus
python verify_selected_factor.py \
  certificates/synthetic-selected-factor.json
python -m unittest discover -s tests -v
```

Expected result:

```text
10 tests pass
2 certified negative synthetic rows
verdict SYNTHETIC_SELECTED_FACTOR_SEPARATION
```

For production conversion:

```bash
python adapt_x9301_selected_factor.py \
  ../X-9301-zero-deflated-xi-modulus/results/pr71/nearest-16-certificate-p256.json \
  --output selected-nearest-16-p256.json
python verify_selected_factor.py selected-nearest-16-p256.json
```

## Production bridge

The adapter consumes:

1. direct completed-xi rectangles already embedded in X-9301;
2. isolated Hardy-zero balls and proof gates already embedded in X-9301;
3. the unchanged row manifest.

It emits the stronger L-9304 selected-factor object from the exact same primitive artifacts. Any strict Riemann-xi negative must be reproduced by an independent completed-xi backend and an independent zero-isolation backend before candidate promotion.

## Proof boundary

Exact within X-9302:

- rational parsing and interval arithmetic;
- complex-rectangle to modulus-square conversion;
- zero-ball squared-distance images;
- selected-factor products;
- rational logarithm enclosures;
- determinants through order four;
- Vandermonde normalization;
- source-certificate digest binding;
- sign and mutation tests.

External:

- correctness of primitive completed-xi rectangles;
- correctness and multiplicity meaning of critical-line zero balls;
- L-9304/L-9305 analytic implications;
- special-function/backend reproduction.

No Riemann-xi counterexample or `Z-####` candidate is claimed.
