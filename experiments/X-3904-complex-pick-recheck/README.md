# X-3904 — Full-complex Pick recheck

This experiment reopens the strongest negative midpoint screens from X-3902 and
checks what the earlier real-vector audit did not:

1. exact complex Gaussian-rational Pick contractions;
2. the true full-complex Hermitian minimum direction;
3. a whole-matrix midpoint-plus-radius positive-definiteness certificate;
4. every previously retained 192-bit ambiguous block;
5. an independent Riemann--Siegel precision ladder for the strongest remaining
   128-bit complex midpoint screen.

No counterexample was found.

## Main verdict

At the exact point set previously described as a refuted real-vector candidate,
`L-7101` proves the complete `8 x 8` complex Pick matrix box positive definite.
The certificate uses

```text
delta = 2^-136
E < 5.758e-147 < delta
```

and exact Gaussian-rational `LDL^*` pivots for `M-delta I`. Thus every admitted
complex direction has lower margin greater than about `1.1479e-41`.

The fourteen earlier ambiguous height blocks were also replayed at 192 bits.
All fourteen frozen full-complex directions are strictly positive.

The strongest newly discovered 128-bit midpoint negative, at grid offset
`j=-15`, is unresolved by its original interval boxes. An independent mpmath
Riemann--Siegel replay is positive and stable at 60 and 70 decimal digits near
`1.2260274656e-35`. This is a high-precision refutation of the numerical
nomination, not a directed positive certificate.

## Files

- `verify_complex_pick.py` — standard-library exact checker;
- `tests/test_verify_complex_pick.py` — exact Gram, negative synthetic, whole
  matrix, and parser controls;
- `rs_complex_candidate.c` — frozen FLINT C producer for the `j=-15` direction;
- `results/frozen-candidate-full-matrix-summary.json` — exact whole-matrix
  certificate summary for the original finalist;
- `results/complex-batch-192-summary.json` — fourteen directed full-complex
  frozen-vector replays;
- `results/jm15-independent-precision-ladder.json` — independent ordinary
  high-precision ladder for `j=-15`.

## Exact checker

```bash
python -m unittest discover \
  -s experiments/X-3904-complex-pick-recheck/tests -v

python experiments/X-3904-complex-pick-recheck/verify_complex_pick.py \
  certificate.json --output verification.json
```

The checker evaluates no special function. It intersects the two supplied
primitive rectangles and uses Python integers plus `fractions.Fraction` for all
contractions and `LDL^*` steps.

## Certification boundary

- Fixed-vector and whole-matrix algebra: exact rational arithmetic.
- Original finalist primitive rectangles: retained directed FLINT artifacts.
- Fourteen-block replay: retained directed 192-bit FLINT artifact.
- `j=-15` second implementation: ordinary high precision only.
- Parent Pick theorem and completed-xi normalization: retain current repository
  statuses.
- Positivity of these finite objects says nothing about RH elsewhere.

## Strategic conclusion

The same-height eight-node table has been adversarially exhausted far beyond the
original one-vector test. Further progress should enlarge the primitive feature
space or return to the directed carrier route:

- cross-height complex Pick packets;
- direct `xi'/xi` jets;
- adaptive horizontal nodes at new ordinates;
- the complete D-0801 directed prime-power coefficient pass and postselection.
