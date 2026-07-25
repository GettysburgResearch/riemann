# X-7501 — Direct completed-xi modulus witnesses

Experiment ID: `X-7501`  
Agent: `gpt56-01-g`  
Issue: #75  
Status: exact checker and production workflow complete; Riemann-xi scan pending

## Research question

Can direct rigorous rectangles for

```text
xi(1/2 + x + iT)
```

produce a finite RH-disproof witness without dividing by `xi`?

L-7501 proves that under RH

```text
H_T(x^2) = |xi(1/2+x+iT)|^2
```

is absolutely monotone as a function of `u=x^2`. Therefore every increasing
node list has nonnegative divided differences. The first test is simply

```text
|xi(1/2+x_2+iT)|^2 >= |xi(1/2+x_1+iT)|^2
```

for `0<=x_1<x_2`.

A directed strict reversal disproves RH. Every RH failure creates an open family
of such two-point reversals immediately to the left of the positive squared
offset of an off-line zero.

## Why this route is new

The current proof-grade `xi'/xi` value table is closed by an exact feasible
anchor: no dual portfolio over those unchanged primitive boxes can be robustly
negative. X-7501 changes the primitive feature space itself. It retains direct
completed-xi rectangles and uses modulus, divided-difference, and multiplicative
shape constraints that cannot be reconstructed from the old `Re(xi'/xi)`
feature boxes.

The route also avoids the hardest near-zero log-derivative gate:

- no division by `xi`;
- no proof that a denominator rectangle excludes zero;
- no derivative jet;
- no finite-difference differentiation.

## Files

```text
arb_modulus_producer.py          python-flint/Arb direct-xi producer
verify_modulus_certificate.py   integer/Fraction-only exact checker
compare_precision.py             exact rectangle identity/nesting gate
configs/                         exact dyadic production points and rows
certificates/                    synthetic exact controls
results/                         retained checker outputs and transcripts
tests/                           fail-closed checker tests
```

## Exact checker

The checker accepts exact rational complex rectangles and computes

```text
|[a,b]+i[c,d]|^2
```

outward. If a coordinate interval crosses zero, its square lower endpoint is
zero; endpoint squaring is never used blindly.

Supported finite rows are:

1. two-point monotonicity;
2. arbitrary divided differences in `u=x^2`;
3. three-point integer-power log concavity from L-7502.

The checker evaluates no special function and uses no floating point.

## Synthetic validation

The committed synthetic certificate contains:

- an on-line positive-factor model whose first and second divided differences
  are nonnegative;
- an off-line-dip model with exact two-point reversal
  `-95/256`;
- a separate forbidden-shape control with exact multiplicative row `-1023`.

Seven tests pass, including normalization mutation, point-digest mutation,
reversed-node rejection, Boolean-as-integer rejection, zero-crossing square
logic, and a mutation that removes one negative control.

Synthetic negatives are checker controls only. They are not Riemann-xi values.

## Arb producer

`arb_modulus_producer.py` evaluates the standard completed product

```text
xi(s) = 0.5*s*(s-1)*pi^(-s/2)*Gamma(s/2)*zeta(s)
```

at exact dyadic points. It does not divide by the result and therefore permits a
rectangle containing zero. It independently evaluates `xi(1-s)` and requires
the two functional-equation rectangles to overlap.

All exported endpoints are exact rational numbers reconstructed from Arb binary
endpoints.

## First production grid

The high-carrier config uses the exact dyadic ordinate

```text
20225875608343121406355 / 2^32
= 4709203636353.630899999989...
```

and horizontal offsets

```text
2^-20, 2^-18, ..., 2^-6, 2^-5.
```

It checks all adjacent monotonicity rows, all adjacent second divided
differences, and adjacent integer-power log-concavity rows at 192 and 256 bits.
Every 256-bit coordinate rectangle must lie inside its 192-bit counterpart.

## Reproduction

```bash
python -m pip install 'python-flint==0.9.0'
python -m unittest discover -s tests -v

python arb_modulus_producer.py configs/high-carrier-horizontal.json \
  --output /tmp/modulus.json
python verify_modulus_certificate.py /tmp/modulus.json
```

The GitHub workflow runs both precisions, exact checker replay, and nesting.

## Proof boundary

A negative Riemann-xi row is a rigorous nomination only after:

1. both directed precisions agree and nest;
2. an independent special-function backend reproduces the primitive rectangles;
3. L-7501 and the standard completed-xi normalization receive independent
   analytic review;
4. every point and row fingerprint is frozen.

No actual Riemann-xi negative interval is currently claimed.

## Suggested next attack

If the first horizontal grid is nonnegative, retain its direct xi rectangles and
adaptively insert nodes where the normalized monotonicity or divided-difference
moat is smallest. Move to distinct exact ordinate windows rather than optimizing
indefinitely on one feature table.
