# X-9302 — Selected-factor direct-xi modulus certificates

Experiment ID: `X-9302`  
Agent: `gpt56-01-j`  
Issue: #93  
Status: exact checker and synthetic controls; Riemann-xi production pending  
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
- `certificates/synthetic-selected-factor.json` — hidden-offline-zero regression;
- `tests/test_verify_selected_factor.py` — fail-closed tests;
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
7 tests pass
2 certified negative synthetic rows
verdict SYNTHETIC_SELECTED_FACTOR_SEPARATION
```

## Production bridge

The intended production adapter consumes:

1. direct completed-xi rectangles from X-7501;
2. isolated Hardy-zero balls from X-5603/X-9301;
3. an unchanged row manifest.

It should emit both the conservative L-9301 endpoint-deflated result and the stronger L-9304 selected-factor result from the same primitive artifacts. Any strict Riemann-xi negative must be reproduced by an independent completed-xi backend and an independent zero-isolation backend before candidate promotion.

## Proof boundary

Exact within X-9302:

- rational parsing and interval arithmetic;
- zero-ball squared-distance images;
- selected-factor products;
- rational logarithm enclosures;
- determinants through order four;
- Vandermonde normalization;
- sign and mutation tests.

External:

- correctness of primitive completed-xi rectangles;
- correctness and multiplicity meaning of critical-line zero balls;
- L-9304/L-9305 analytic implications;
- special-function/backend reproduction.

No Riemann-xi counterexample or `Z-####` candidate is claimed.
