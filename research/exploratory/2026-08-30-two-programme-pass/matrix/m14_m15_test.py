"""Third held-out test of the torsion entry law m = 2 ord(alpha^2) + 1:
m = 14 must add no new torsion; m = 15 must gain BOTH ord-7-related
cubics (min polys of 2cos(2pi/7): a^3+a^2-2a-1, and of 2cos(pi/7):
a^3-a^2-2a+1 — ord(alpha) = 7 and 14, both ord(alpha^2) = 7) and
NOT the ord-9-related sextic factor territory (ord(alpha^2)=9 -> m=19).
Writes matrix/m14_m15_spectrum.json. rh_established = false.
"""
import sys, json, time
sys.path.insert(0, '.')
sys.path.insert(0, 'matrix')
import sympy as sp
from c1_defect_atlas import defect_numerator, spectrum_poly, check_selfdual, a, b, z

C7A = sp.Poly(a**3 + a**2 - 2*a - 1, a)   # 2cos(2pi/7): ord 7
C7B = sp.Poly(a**3 - a**2 - 2*a + 1, a)   # 2cos(pi/7):  ord 14
C9 = sp.Poly(a**3 - 3*a + 1, a)           # 2cos(2pi/9): ord 9 (alpha^2 ord 9 -> m=19)

out = {}
for m in (14, 15):
    t0 = time.time()
    N = defect_numerator(m)
    assert check_selfdual(N, m)
    M, eps, ok = spectrum_poly(N, m)
    assert ok
    disc = sp.discriminant(sp.Poly(M, z), z)
    d1 = sp.expand(disc.subs(b, 1))
    tests = {"ord7_2cos2pi7": sp.rem(sp.Poly(d1, a), C7A).is_zero,
             "ord14_2cospi7": sp.rem(sp.Poly(d1, a), C7B).is_zero,
             "ord9_2cos2pi9": sp.rem(sp.Poly(d1, a), C9).is_zero}
    small = []
    for (f, mult) in sp.factor_list(d1)[1]:
        p = sp.Poly(f, a)
        if 0 < p.degree() <= 6:
            small.append([str(f.as_expr()), int(mult), int(p.degree())])
    print(f"m={m} ({time.time()-t0:.0f}s) small={small} tests={tests}", flush=True)
    out[str(m)] = {"small_factors": small,
                   "divisibility": {k: bool(v) for k, v in tests.items()}}
json.dump(out, open('matrix/m14_m15_spectrum.json', 'w'), indent=1)
print("prediction: m=14 all False; m=15 ord7 True, ord14 True, ord9 False")
