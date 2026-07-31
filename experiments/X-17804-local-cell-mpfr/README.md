# X-17804 — Directed local-cell MPFR prime replay

This experiment evaluates the complete `J=12`, five-normalized-difference prime window at

```text
x = 17730793345827 / 2^40
```

without FFTs, interpolation, numerical quadrature, or an infinite-convolution tail.

## Build

```bash
cc -O3 -std=gnu11 directed_local_cell.c -lmpfr -lgmp -lm -o directed_local_cell
for p in 256 320 384 448; do ./directed_local_cell "$p"; done
python verify.py results/summary.json --source directed_local_cell.c
python -m unittest discover -s tests -v
```

The producer:

1. constructs all 800 base knots and coefficients from exact GMP rationals;
2. builds the local degree-23 cells by the exact translation recurrence of `L-17804`;
3. encloses `log 4`, every `log q`, `sqrt(q)`, window value and accumulation outward with MPFR;
4. enumerates every prime power in the exact support ceiling;
5. fails closed on any knot ambiguity or structural count mismatch.

`moment_sweep.py` is an algebraically independent ordinary-high-precision replay. It is not a proof backend.

## Retained result

```text
DIRECTED_COMPLETE_PRIME_CELL_CLOSED
segments             800
prime-power terms     103384
ambiguous knots       0
precision nesting     256 -> 320 -> 384 -> 448
```

Proof-object SHA-256 is recorded in `results/verification.json`.

## Scope

This closes only the finite prime interval. It does not certify the first-100-zero phase model and does not decide RH.
