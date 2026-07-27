#!/usr/bin/env python3
"""
X-0021 -- The wide-net Pick screen: many clusters, any height.

Agent: claude-02.  Executes the X-0020 recommendation at scale: a 10-cluster
band widening the exclusion around the two-architecture convergence ordinate
T0 ~ 4.7092e12, plus single clusters at T = 1e6 and 1e9 measuring how the
detector floor scales with zero density (Q-0017 field data).  Trust class:
Arb RS jet, as X-0020.
"""
from __future__ import annotations
import glob, json, sys
sys.path.insert(0, "/home/user/riemann/scripts")
from flint import acb, arb, ctx
import pick as PK

ctx.prec = 800
HALF = arb(1) / 2
R = "experiments/X-0021-pick-widenet/results/"

def ball(iv):
    lo = arb(iv["lower"]["numerator"]) / arb(iv["lower"]["denominator"])
    hi = arb(iv["upper"]["numerator"]) / arb(iv["upper"]["denominator"])
    m = (lo + hi) / 2
    return m.union(m + (hi - lo) / 2).union(m - (hi - lo) / 2)

def load(fp):
    d = json.load(open(fp))
    tn = int(d["ordinate_base"]["numerator"])
    jb = int(d.get("jbase", 12))
    lp2 = acb(arb.pi().log()) / 2
    alphas, Fv = [], {}
    for p in d["points"]:
        t = arb(tn + (jb + p["j"]) * (1 << 27)) * arb(2) ** (-32)
        a = acb(arb(9) * arb(2) ** (-4), t)
        z = acb(ball(p["zeta"]["real"]), ball(p["zeta"]["imag"]))
        zp = acb(ball(p["zeta_prime"]["real"]), ball(p["zeta_prime"]["imag"]))
        Fv[(str(a.real), str(a.imag))] = (-lp2 + (a / 2 + 1).polygamma(acb(0)) / 2
                                          + 1 / (a - 1) + zp / z)
        alphas.append(a)
    centre = arb(tn) * arb(2) ** (-32) + arb(jb + 15) * arb(2) ** (-5)
    return alphas, (lambda s: Fv[(str(acb(s).real), str(acb(s).imag))]), centre

out = {"schema": "riemann.x0021-widenet.v1", "agent": "claude-02",
       "prec_bits": 800, "clusters": []}
alert = False
for fp in sorted(glob.glob(R + "band-k*.json")) + [R + "h1e6.json", R + "h1e9.json"]:
    alphas, F, c = load(fp)
    cert = PK.pick_certificate(alphas, F=F)
    rec = {"file": fp.split("/")[-1], "centre": str(c)[:26],
           "verdict": cert["verdict"], "min_pivot": cert["min_pivot"]}
    # per-cluster OFF/DOUBLE control at the cluster centre
    def wex(zs, F=F):
        return lambda s: F(s) + sum(1 / (acb(s) - z) for z in zs)
    dd = arb(10) ** (-9)
    off = [acb(HALF - dd, c), acb(HALF + dd, c), acb(HALF - dd, -c), acb(HALF + dd, -c)]
    dbl = [acb(HALF, c), acb(HALF, c), acb(HALF, -c), acb(HALF, -c)]
    co = PK.pick_certificate(alphas, F=wex(off))
    cd = PK.pick_certificate(alphas, F=wex(dbl))
    rec["off_1e-9"] = co["verdict"]
    rec["double"] = cd["verdict"]
    rec["double_floor"] = cd["min_pivot"]
    if cert["verdict"] == "NOT_PSD":
        alert = True
        P = PK.pick_matrix(alphas, F=F)
        x = PK.ldl_witness_direction(P)
        q = PK.tuned_form(alphas, x, F=F)
        rec["witness_q"] = float(q.mid())
    out["clusters"].append(rec)
    print(f"{rec['file']:<14} {rec['verdict']:<8} piv={rec['min_pivot']:.2e} "
          f"| OFF(1e-9)={rec['off_1e-9']:<8} DBL={rec['double']:<3} "
          f"floor={rec['double_floor']:.2e}", flush=True)

bad_ctl = any(r["double"] == "NOT_PSD" for r in out["clusters"])
out["conclusion"] = ("P1 ALERT -- see clusters" if alert else
                     "control failure" if bad_ctl else
                     "all clusters PD; band [T0-4, T0+6.3] and heights 1e6, 1e9 "
                     "excluded to the per-cluster OFF-validated depth; 0 control firings")
json.dump(out, open(R + "widenet.json", "w"), indent=1)
print("\n " + out["conclusion"])
