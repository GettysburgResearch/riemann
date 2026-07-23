# X-2802 — Exact rational carrier-scalar enclosure

Experiment ID: `X-2802`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: exact finite computation, lemma pending review  
Date: 2026-07-23

## Question

Can the scalar

```text
alpha(T) = log(T/(2*pi))/(2*pi)
```

at the optimized carrier be removed entirely from the ball-arithmetic producer
and replaced by a compact exact certificate?

## Result

For

```text
T = 4709203636353.65 = 94184072727073/20
```

`exact_alpha.py` proves

```text
27316188863170422972141786876274838781565257086415513364963 / 2^192
 <= alpha(T) <=
27316188863170422972141786876274838781565257086415513364964 / 2^192.
```

The enclosure is one dyadic unit wide, namely `2^-192`.

## Proof backend

The script uses only Python integers and `fractions.Fraction`:

1. `pi = 16 atan(1/5) - 4 atan(1/239)`;
2. alternating arctangent intervals with next-term remainders;
3. exact power-of-two range reduction;
4. the positive atanh series for real logarithms;
5. an explicit geometric tail;
6. exact interval division;
7. final outward floor/ceiling to denominator `2^192`.

No floating-point or special-function value enters the certificate result.
`mpmath` is used only by one independent regression test.

## Reproduction

```bash
python exact_alpha.py \
  certificates/target-alpha-c1e11.json \
  --output results/target-alpha-output.json

PYTHONPATH=. python -m unittest discover -s tests -v \
  > results/tests.txt 2>&1
```

## Files

- `exact_alpha.py` — proof-producing rational checker;
- `certificates/target-alpha-c1e11.json` — exact carrier and series counts;
- `results/target-alpha-output.json` — retained dyadic enclosure;
- `tests/test_exact_alpha.py` — six adversarial/regression tests;
- `results/tests.txt` and `results/SHA256SUMS` — transcript and provenance.

## Proof boundary

This closes only the `alpha(T)` leaf in L-2804. It does not certify:

- the frozen vector;
- any prime phase or prime Rayleigh interval;
- D-0801 admissibility;
- the Guinand--Weil normalization;
- a positive or negative complete carrier sign.

## Integration

A real `riemann.piecewise-carrier-fixed-vector.v1` certificate should copy the
committed dyadic endpoints exactly and bind the X-2802 result digest in its
producer ledger.
