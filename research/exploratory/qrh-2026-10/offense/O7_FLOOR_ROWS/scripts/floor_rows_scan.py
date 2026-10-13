#!/usr/bin/env python3
"""O7 scans (PROPOSED / EXPLORATORY; same model and certificates as floor_rows_lp.py).
(A) exact limit bin delta -> delta0+ included (DH count R = 1 - delta0 - thNC);
(B) raised floor: a0 = (1 + delta0)/2 with floor saving theta_F = kappa*delta0 + thNC, DH bins above;
(C) closed forms checked at rational theta."""
from fractions import Fraction as Fr
import numpy as np
import floor_rows_lp as F

def rows(a0, thF, gram, energy, thNC=Fr(0)):
    r = F.rows_for(a0, thF, gram, energy, dh=True, thNC=thNC)
    d0 = 2*a0 - 1
    r.append(F.bin_row(a0, max(1 - d0 - thNC, (1 - d0)/2)))      # limit bin delta -> delta0+
    return r

def val(a0, thF, gram, energy, thNC=Fr(0)):
    rr = rows(a0, thF, gram, energy, thNC)
    res = F.solve(rr); ok, b = F.certify(rr, res)
    ok = ok and F.posterior(res.x, a0, thNC, True)
    return res.fun, ok, b, np.round(res.x[:3], 4)

if __name__ == '__main__':
    print("(A) floor-only saving with exact delta0+ limit bin (DH counts above the floor)")
    for gram in ('b12', 'zero'):
        for energy in ('paper', 'optimal'):
            for a0 in (Fr(51, 100), Fr(1, 2)):
                out = []
                for th in (Fr(0), Fr(1, 200), Fr(1, 100), Fr(1, 50), Fr(1, 20), Fr(1, 10)):
                    v, ok, b, g = val(a0, th, gram, energy)
                    out.append(f"{th}:{b if ok else '%.6f?' % v}")
                print(f"  gram={gram:4s} energy={energy:7s} a0={a0}: " + "  ".join(out))
    print("(B) raised floor a0=(1+d0)/2, floor saving theta_F = kappa*d0 (+thNC), DH bins above, no NC unless stated")
    for gram in ('b12', 'zero'):
        for energy in ('paper', 'optimal'):
            for kappa in (Fr(1, 4), Fr(1, 2), Fr(5, 6), Fr(1)):
                out = []
                for d0 in (Fr(0), Fr(1, 50), Fr(1, 20), Fr(1, 10), Fr(1, 6), Fr(1, 4), Fr(1, 3), Fr(1, 2)):
                    a0 = (1 + d0)/2
                    v, ok, b, g = val(a0, kappa*d0, gram, energy)
                    out.append(f"{d0}:{b if ok else '%.6f?' % v}")
                print(f"  gram={gram:4s} energy={energy:7s} kappa={kappa}: " + "  ".join(out))
    print("(B') geometry at kappa=1, gram=zero, paper energy")
    for d0 in (Fr(1, 10), Fr(1, 6), Fr(1, 4), Fr(1, 3), Fr(1, 2)):
        v, ok, b, g = val((1 + d0)/2, d0, 'zero', 'paper')
        print(f"   d0={d0}: {b if ok else v} at {g}")
