"""Two probes: (a) corr_3 layer conjecture at rank 6 (stdlib instantiations);
(b) does N_5 factor over Q(a,b) into deformation L-data (bridge extension)?
Writes matrix/layer_probes.json"""
import json, sys
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from core.exact import (minimal_rational_form, power_sums_from_satake,
                        op_sym2, op_ext2, elementary_from_power_sums,
                        satake_poly_from_power_sums, coefficient_sequence_from_satake)

out = {"rank6_corr3": [], "rh_established": False}

def corr3_rank6(es):
    d = 6
    sat = [Fr(1)] + [(-1) ** k * Fr(es[k - 1]) for k in range(1, d + 1)]
    r_sym, r_ext = 21, 15
    hs = coefficient_sequence_from_satake(sat, 2 * r_sym + 10)
    mf = minimal_rational_form([x * x for x in hs])
    if mf is None: return None
    P, Q = mf
    ps = power_sums_from_satake(sat, 2 * r_sym + 4)
    D = satake_poly_from_power_sums(op_sym2(ps, r_sym), r_sym)
    if Q != D: return None
    e_ext = elementary_from_power_sums(op_ext2(ps, r_ext), r_ext)
    pred3 = (-1) ** 3 * e_ext[2]
    corr3 = (P[3] if len(P) > 3 else Fr(0)) - pred3
    e1,e2,e3,e4,e5,e6 = map(Fr, es)
    h2 = e1*e1 - e2
    conj = 2 * (e4*h2 - e5*e1 + e6)
    return corr3, conj

for es in [(1,2,3,2,1,2), (2,1,-1,3,2,1), (1,1,2,1,3,-1), (2,-1,1,2,-2,3), (1,2,1,-1,2,2)]:
    r = corr3_rank6(es)
    if r is None:
        out["rank6_corr3"].append({"es": es, "note": "degenerate/skip"})
        print(f"{es}: degenerate", flush=True)
    else:
        c, conj = r
        out["rank6_corr3"].append({"es": es, "corr3": str(c), "conjecture_2(e4h2-e5h1+e6h0)": str(conj), "match": c == conj})
        print(f"{es}: corr3={c} conj={conj} match={c==conj}", flush=True)

import sympy as sp
a, b, T = sp.symbols('a b T')
N5 = 1 + a*b*(4*a**2-3*b)*T + 2*b**3*(a**2-b)*(3*a**2-b)*T**2 + a*b**6*(4*a**2-3*b)*T**3 + b**10*T**4
fac = sp.factor(N5)
out["N5_factor_over_Qab"] = str(fac)
print("N5 factors as:", fac, flush=True)
# symmetric self-dual ansatz: (1+xT+b^5T^2)(1+yT+b^5T^2): x+y = c1, xy = c2-2b^5
c1 = sp.expand(a*b*(4*a**2-3*b)); c2 = sp.expand(2*b**3*(a**2-b)*(3*a**2-b))
disc = sp.factor(sp.expand(c1**2 - 4*(c2 - 2*b**5)))
out["ansatz_disc_factored"] = str(disc)
print("self-dual-pair ansatz disc:", disc, flush=True)
json.dump(out, open('matrix/layer_probes.json','w'), indent=1)
print("WROTE matrix/layer_probes.json", flush=True)
