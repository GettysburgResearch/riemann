#!/usr/bin/env python3
"""
X-0020 -- The certified Pick detector (T-0005/L-0008/L-0009) at the fleet's
hot neighborhood: T0 = 20225875608343133989267/2^32 ~ 4.7092e12.

Agent: claude-02.  Fusion of the two research programs: the gpt56 fleet's
FLINT Riemann-Siegel jet reaches heights my Euler-Maclaurin stack cannot
(Q-0001), and my Pick machinery resolves off-line depth delta at cost
O(log 1/delta) where the fleet's moment cones pay full precision budgets.
This experiment aims the Pick detector at the ordinate where two independent
witness architectures (direct-xi atomized minimum and the carrier-Weil basin,
separation 0.016) selected the same neighborhood.

TRUST BOUNDARY: the evaluator here is FLINT's acb_dirichlet_zeta_jet_rs
(rigorous ball output per Arb's documented RS error bounds) -- the same trust
class as the entire PR #103 lineage, but a DIFFERENT class than this branch's
own certzeta-based results, which trust only L-0001/L-0006.  Stated openly:
a NOT_PSD here would be refutation-grade only modulo Arb's RS implementation.

Parts:
 1. Detector validation at this height/geometry: matched OFF/DOUBLE controls
    planted on the real F (delta ladder), 0 control firings required.
 2. The real verdict on the neighborhood, with witness extraction on alert.
"""
from __future__ import annotations
import json, sys, time
sys.path.insert(0, "/home/user/riemann/scripts")
from flint import acb, arb, ctx
import pick as PK

ctx.prec = 800
HALF = arb(1) / 2
R = "experiments/X-0020-pick-at-frontier/results/"
d = json.load(open(R + "probes-p512.json"))
T0NUM = 20225875608343133989267

def dy(num, e):  # exact dyadic num * 2^-e
    return arb(num) * arb(2) ** (-e)

def ball(iv):
    lo = arb(iv["lower"]["numerator"]) / arb(iv["lower"]["denominator"])
    hi = arb(iv["upper"]["numerator"]) / arb(iv["upper"]["denominator"])
    return ((lo + hi) / 2).union((lo + hi) / 2 + (hi - lo) / 2).union((lo + hi) / 2 - (hi - lo) / 2)

alphas, Fv = [], {}
lp2 = acb(arb.pi().log()) / 2
for p in d["points"]:
    t = dy(T0NUM + (12 + p["j"]) * (1 << 27), 32)
    a = acb(dy(9, 4), t)
    z = acb(ball(p["zeta"]["real"]), ball(p["zeta"]["imag"]))
    zp = acb(ball(p["zeta_prime"]["real"]), ball(p["zeta_prime"]["imag"]))
    F = -lp2 + (a / 2 + 1).polygamma(acb(0)) / 2 + 1 / (a - 1) + zp / z
    alphas.append(a)
    Fv[(str(a.real), str(a.imag))] = F

def Freal(s):
    return Fv[(str(acb(s).real), str(acb(s).imag))]

out = {"schema": "riemann.x0020-pick-frontier.v1", "agent": "claude-02",
       "prec_bits": 800, "n_probes": len(alphas),
       "re_probe": "9/16", "ordinate_base": str(d["ordinate_base"]),
       "trust": "FLINT acb_dirichlet_zeta_jet_rs ball output (Arb RS bounds)",
       "controls": [], }

# ---- part 1: matched controls at this height --------------------------------
c = dy(T0NUM, 32) + dy(27, 5)          # T0 + 27/32, inside the cluster span
def with_extra(zs):
    def F(s):
        s = acb(s)
        return Freal(s) + sum(1 / (s - z) for z in zs)
    return F

print("part 1: detector validation at height 4.71e12 (N=32, Re a = 9/16)")
dbl = [acb(HALF, c), acb(HALF, c), acb(HALF, -c), acb(HALF, -c)]
cd = PK.pick_certificate(alphas, F=with_extra(dbl))
print(f"  DOUBLE control: {cd['verdict']:<10} min_pivot={cd['min_pivot']:.3e}")
out["controls"].append({"mode": "DOUBLE", "verdict": cd["verdict"],
                        "min_pivot": cd["min_pivot"]})
fired_ctl = cd["verdict"] == "NOT_PSD"
det = None
for e in (3, 6, 9):
    dd = arb(10) ** (-e)
    off = [acb(HALF - dd, c), acb(HALF + dd, c),
           acb(HALF - dd, -c), acb(HALF + dd, -c)]
    co = PK.pick_certificate(alphas, F=with_extra(off))
    leh = [acb(HALF, c - dd), acb(HALF, c + dd),
           acb(HALF, -c + dd), acb(HALF, -c - dd)]
    cl = PK.pick_certificate(alphas, F=with_extra(leh))
    fired_ctl |= cl["verdict"] == "NOT_PSD"
    if co["verdict"] == "NOT_PSD":
        det = f"1e-{e}"
    print(f"  OFF delta=1e-{e}: {co['verdict']:<10} ({co['min_pivot']:.3e})   "
          f"LEHMER: {cl['verdict']:<10} ({cl['min_pivot']:.3e})")
    out["controls"].append({"delta": f"1e-{e}", "off": co["verdict"],
                            "off_min_pivot": co["min_pivot"],
                            "lehmer": cl["verdict"]})
out["smallest_delta_detected"] = det
out["control_firings"] = bool(fired_ctl)
print(f"  smallest delta detected: {det}   control firings: {fired_ctl}")

# ---- part 2: the real verdict ----------------------------------------------
print("\npart 2: the real neighborhood")
cr = PK.pick_certificate(alphas, F=Freal)
out["real"] = {"verdict": cr["verdict"], "min_pivot": cr["min_pivot"],
               "min_pivot_rad": cr["min_pivot_rad"]}
print(f"  REAL: {cr['verdict']}  min_pivot={cr['min_pivot']:.3e}  "
      f"rad={cr['min_pivot_rad']:.1e}")
if cr["verdict"] == "NOT_PSD":
    P = PK.pick_matrix(alphas, F=Freal)
    x = PK.ldl_witness_direction(P)
    q = PK.tuned_form(alphas, x, F=Freal)
    out["real"]["witness_q"] = float(q.mid())
    out["real"]["witness_q_negative"] = bool(q < 0)
    print(f"  *** P1 ALERT: scalar witness q = {float(q.mid()):.3e} ***")

out["conclusion"] = (
    "detector validated at height 4.71e12 and the real Pick matrix is "
    f"{cr['verdict']}: no off-line pair within reach of this cluster at the "
    "two-architecture convergence neighborhood"
    if cr["verdict"] == "PD" and not fired_ctl and det else "SEE FIELDS")
json.dump(out, open(R + "pick-frontier.json", "w"), indent=1)
print("\n " + out["conclusion"])
print("wrote", R + "pick-frontier.json")
