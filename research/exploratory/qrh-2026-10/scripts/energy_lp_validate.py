#!/usr/bin/env python3
# Validates the closed form E_B = max(M',(2M'+1+3l')/4,2M'+l'-1) against the LP sup of eq. (14.14).
import sys; sys.path.insert(0, '.')
import random
from energy_lp import sup_energy
random.seed(3)
worst = 0; bad = 0; n = 0; inf = 0
for _ in range(400):
    Mp = random.uniform(0.2, 1.3); lp = random.uniform(0, 0.5)
    val, arg = sup_energy(Mp, lp)
    if arg is None: inf += 1; continue
    closed = max(Mp, (2*Mp + 1 + 3*lp)/4, 2*Mp + lp - 1)
    n += 1
    if abs(val - closed) > 1e-7:
        bad += 1
        if bad < 10: print("diff", Mp, lp, val, closed, arg[:2])
    worst = max(worst, abs(val-closed))
print("checked", n, "infeasible", inf, "max diff", worst, "bad", bad)
