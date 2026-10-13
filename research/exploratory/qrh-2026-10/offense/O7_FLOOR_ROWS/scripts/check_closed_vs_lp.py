#!/usr/bin/env python3
"""O7: check the closed form sigma0(delta0,kappa) = 2(9+13d-12kd)/(3(7+9d-8kd)) against the exact LP
(floor_rows_scan.val, Gram 0, paper energy) on a grid.  Exact Fractions; prints mismatches."""
from fractions import Fraction as Fr
import floor_rows_scan as S
bad = 0; n = 0
for k in (Fr(1, 4), Fr(1, 2), Fr(5, 6), Fr(9, 10), Fr(1)):
    for d in (Fr(1, 50), Fr(1, 10), Fr(1, 5), Fr(1, 3), Fr(9, 20), Fr(1, 2)):
        v, ok, b, g = S.val((1 + d)/2, k*d, 'zero', 'paper')
        f = Fr(2)*(9 + 13*d - 12*k*d)/(3*(7 + 9*d - 8*k*d))
        n += 1
        if not ok or b != f:
            bad += 1; print("mismatch", k, d, b, f, ok)
print(f"closed form vs LP at fixed delta0: {n - bad}/{n} exact matches")
