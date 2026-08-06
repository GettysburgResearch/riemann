# X-17204 — hundred-zero refinement of the `q=8` raw moat

Status: `DIRECTED_SINGLE_ARB_BACKEND_PROPOSED`  
Claim: `L-17203`  
Issue: #172, negative route

## Purpose

This artifact sharpens the inherited `L-17202/X-17203` bound without changing
the filter.  At 320-bit precision Arb:

1. isolates `zeta_zero(j)` for every `1 <= j <= 100`;
2. verifies a cumulative-count jump from `j-1` to `j` across a radius
   `10^-70` bracket around each ordinate;
3. verifies `N(237)=100`;
4. directly ball-evaluates the exact ten-notch `G_8` transform at all 100
   ordinates;
5. subtracts their positive reciprocal mass from
   `2 + EulerGamma - log(4*pi)` and bounds the remainder above 237; and
6. directly evaluates the surviving trivial-zero terms `m=3,4,5` at `x=18`,
   then bounds `m>=6` using the inherited support and `L1` bounds.

The retained directed enclosure is

```text
nontrivial-zero line total  3.4777908371757601558902839891e-26
complete raw bound at x=18  3.4781388191451717896573312999e-26
declared raw moat            3.5e-26
```

The same bound holds for every `x>=18`, because each trivial-zero contribution
and the support/L1 tail majorant decrease with `x`.

## Files

- `certificate.json` freezes dependencies, hashes, census parameters, and
  every declared constant.
- `verify.py` performs the exact-rational dependency audit and the full Arb
  replay.  It has no floating midpoint mode.
- `results/verification.json` retains all 100 ordinate balls, count pairs, and
  individual transform-contribution balls.
- `tests/test_mutations.py` checks that dependency or bound mutations fail
  closed.

## Replay

With python-flint available on `PYTHONPATH`:

```powershell
python .\verify.py --output .\results\verification.json
python -m unittest discover -s .\tests -v
```

The dependency/hash checks can be replayed without Arb:

```powershell
python .\verify.py --rational-only
```

## Certification boundary

This is a single-backend Arb/FLINT certificate and remains `PROPOSED`.  The
smoothed raw von Mangoldt explicit formula and its normalization are inherited
from `L-17201/T-15404`.  No independent zero backend and no violating prime
support are claimed.

