import json, sys, time
from fractions import Fraction as Fr
sys.path.insert(0, '.')
from directed_xi import xi_scaled, rect_json, T_NUM, T_DEN, SCALE_P, NORMALIZATION

prec = int(sys.argv[1]) if len(sys.argv) > 1 else 768
cert = json.load(open('atomized-min-certificate-p512.json'))
out = {"schema": "riemann.x5605-regenerated-table.v1", "agent": "fable5-01",
       "ordinate": {"numerator": T_NUM, "denominator": T_DEN},
       "normalization_id": NORMALIZATION,
       "common_xi_scale_power_of_two": SCALE_P,
       "classification": "RIEMANN_XI_DIRECTED", "prec_bits": prec,
       "count_windows": cert["count_windows"], "points": []}
for p in sorted(cert["points"], key=lambda q: Fr(q["u"]["numerator"], q["u"]["denominator"])):
    u = Fr(p["u"]["numerator"], p["u"]["denominator"])
    # u = 4^-j so x = 2^-j exactly
    x = Fr(1, int(round((1/u) ** 0.5)))
    assert x * x == u, (x, u)
    t0 = time.time()
    z = xi_scaled(x, prec)
    out["points"].append({"id": p["id"], "u": {"numerator": u.numerator, "denominator": u.denominator},
                          "xi_rectangle": rect_json(z)})
    print("%s  [%.1f s]" % (p["id"], time.time() - t0), flush=True)
json.dump(out, open('results/regenerated-table-p%d.json' % prec, 'w'))
print("wrote results/regenerated-table-p%d.json" % prec)
