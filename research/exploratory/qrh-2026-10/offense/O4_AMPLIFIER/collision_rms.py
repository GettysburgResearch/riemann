"""collision_rms.py -- HEURISTIC prediction of the explicit collision term (l n = l' n') in
T(l l'^5)/sqrt(T(l,l) T(l',l')), continuous approximation sum_k f(N k) ~ c * integral, for the 46 prime
ideals of norm <= 211 used by tm_twisted.py.  Compare with off_rms in results/tm.log.  Not a proof."""
import os, sys
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "moments")))
import numpy as np
import eisenstein as E
import common as C
pr = [P.N for P in E.prime_ideals(211) if P.N <= 211]
y = np.linspace(1, 2, 20001)
W2 = np.trapezoid(C.W(y) ** 2, y)
vals = []
for i, a in enumerate(pr):
    for j, b in enumerate(pr):
        if i < j:
            # T(l,l') collision: n' = n l / l' (dyadic window); relative size (1/sqrt(Na Nb)) * overlap
            r = a / b
            ov = np.trapezoid(C.W(y) * C.W(y * r), y) / W2
            vals.append(ov / np.sqrt(a * b))
vals = np.array(vals)
print(f"#primes={len(pr)} predicted collision rms={np.sqrt(np.mean(vals**2)):.4f} max={vals.max():.4f}")
