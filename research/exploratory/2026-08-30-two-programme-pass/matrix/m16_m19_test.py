"""Fourth held-out round for the torsion entry law m = 2 ord(alpha^2) + 1
(O-108512). Predictions, written BEFORE the run:
  m = 16, 17, 18: NO new torsion factors (only persistence of the
    already-entered ones);
  m = 19: BOTH ord(alpha^2) = 9 cubics enter JOINTLY —
    a^3 - 3a + 1   (2cos 2pi/9,  ord alpha = 9)
    a^3 - 3a - 1   (2cos pi/9,   ord alpha = 18)
    — and the ord(alpha^2) = 10 quartic a^4 - 5a^2 + 5 (2cos pi/10,
    ord alpha = 20; predicted entry m = 21) stays absent.
Writes matrix/m16_m19_spectrum.json incrementally.
rh_established = false.
"""
import sys, json, time
sys.path.insert(0, '.')
sys.path.insert(0, 'matrix')
import sympy as sp
from c1_defect_atlas import defect_numerator, spectrum_poly, check_selfdual, a, b, z

C9A = sp.Poly(a**3 - 3*a + 1, a)     # 2cos(2pi/9), ord 9
C9B = sp.Poly(a**3 - 3*a - 1, a)     # 2cos(pi/9),  ord 18
C20 = sp.Poly(a**4 - 5*a**2 + 5, a)  # 2cos(pi/10), ord 20 -> m=21

out = {}
for m in (16, 17, 18, 19):
    t0 = time.time()
    N = defect_numerator(m)
    assert check_selfdual(N, m)
    M, eps, ok = spectrum_poly(N, m)
    assert ok
    disc = sp.discriminant(sp.Poly(M, z), z)
    d1 = sp.expand(disc.subs(b, 1))
    tests = {"ord9_2cos2pi9": sp.rem(sp.Poly(d1, a), C9A).is_zero,
             "ord18_2cospi9": sp.rem(sp.Poly(d1, a), C9B).is_zero,
             "ord20_2cospi10": sp.rem(sp.Poly(d1, a), C20).is_zero}
    print(f"m={m} ({time.time()-t0:.0f}s) tests={tests}", flush=True)
    out[str(m)] = {k: bool(v) for k, v in tests.items()}
    json.dump(out, open('matrix/m16_m19_spectrum.json', 'w'), indent=1)
print("prediction: m=16..18 all False; m=19 ord9 True, ord18 True, ord20 False")
