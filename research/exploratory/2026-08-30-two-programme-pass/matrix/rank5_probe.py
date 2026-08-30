"""Rank-5 pointwise-square defect: exact stdlib probe of the correction to
the Gauss-sign Ext^2 prediction, at integer instantiations. Tests whether
the rank-4 correction shape (2 e4 h2 T^3 - 2 e2 e4^2 T^5) persists, changes,
or vanishes at rank 5. Writes matrix/rank5_probe.json"""
import json, sys
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from core.exact import (minimal_rational_form, power_sums_from_satake,
                        op_sym2, op_ext2, elementary_from_power_sums,
                        satake_poly_from_power_sums, coefficient_sequence_from_satake)

def probe(es):
    d = len(es)
    sat = [Fr(1)] + [(-1) ** k * Fr(es[k - 1]) for k in range(1, d + 1)]
    r_sym, r_ext = d * (d + 1) // 2, d * (d - 1) // 2
    hs = coefficient_sequence_from_satake(sat, 2 * r_sym + 10)
    P, Q = minimal_rational_form([x * x for x in hs])
    ps = power_sums_from_satake(sat, 2 * r_sym + 4)
    D = satake_poly_from_power_sums(op_sym2(ps, r_sym), r_sym)
    if Q != D:
        return None   # degeneration locus: reduced denominator (recorded)
    e_ext = elementary_from_power_sums(op_ext2(ps, r_ext), r_ext)
    pred = [Fr(1)] + [(-1) ** (j * (j - 1) // 2) * e_ext[j - 1]
                      for j in range(1, r_ext + 1)]
    while len(P) < r_ext + 1: P.append(Fr(0))
    corr = [P[j] - pred[j] for j in range(r_ext + 1)]
    return corr

CASES = [(1,2,3,2,1), (2,1,-1,3,2), (1,0,2,-1,1), (3,-2,1,5,-1),
         (1,1,1,1,2), (2,3,1,-2,3), (-1,2,-3,1,2), (1,-1,2,1,-2)]
out = {"cases": {}}
for es in CASES:
    corr = probe(es)
    if corr is None:
        out["cases"][str(es)] = "DEGENERATE (reduced denominator; skipped)"
        print(f"{es}: DEGENERATE instantiation, recorded", flush=True)
        continue
    nz = {j: str(c) for j, c in enumerate(corr) if c != 0}
    out["cases"][str(es)] = nz
    print(f"{es}: nonzero corrections at {sorted(nz)}: {nz}", flush=True)
    # rank-4-shape test: corr_3 == 2 e4 h2? with h2 = e1^2 - e2
    e1,e2,e3,e4,e5 = map(Fr, es)
    h2 = e1*e1 - e2
    print(f"   rank4-shape at j=3? corr3={corr[3]} vs 2*e4*h2={2*e4*h2}", flush=True)
out["rh_established"] = False
json.dump(out, open('matrix/rank5_probe.json','w'), indent=1)
print("WROTE matrix/rank5_probe.json", flush=True)
