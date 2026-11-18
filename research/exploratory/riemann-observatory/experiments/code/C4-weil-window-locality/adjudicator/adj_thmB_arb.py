"""Adjudicator: Arb (ball-arithmetic) certification of the explicit Theorem C4-B inequality at the points
used in C4-B2 and in the inverse map C4-ADJ-INV.

margin(L,T,d) = 2 s^4 - s^2 [log(T/2pi) + 4 pi L S*(2T)] - eps(L,T,d)  (formula as in REPORT.md, C4-B),
s^2 = sinh(2dL)/(2d) - L.  margin > 0  =>  (under H1) lambda_min(L) < 0, i.e. L*(T,d) <= L.

(1) Point certificates margin(L,T,d) > 0 at the reported L_B values rounded UP (rigorous upper bounds
    for L* under H1), and sign certificates for the delta* correction at T_PT = 3000175332800.
(2) Interval certificates: margin(L, 10^t, d) > 0 for ALL t in [2, t_max] (T in [100, 10^t_max]),
    by adaptive bisection of t-intervals with ball evaluation; this is the inverse map
    "W >= 0 on window L  =>  (under H1) no quadruple with that d and 100 <= T <= 10^t_max".
Usage: python3 adj_thmB_arb.py
"""
import json, time, os, hashlib, platform
import flint
from flint import arb

flint.ctx.prec = 256
OUT = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/adjudicator/adj_thmB_arb.json"
PI = arb.pi()
c112, c278, c251, c04 = arb("0.112"), arb("0.278"), arb("2.510"), arb("0.4")


def Sstar(t):
    return c112 * t.log() + c278 * t.log().log() + c251


def margin(L, T, d):
    L, d = arb(L), arb(d)
    s2 = (2 * d * L).sinh() / (2 * d) - L
    A = 2 * (d * L).sinh()
    B = 2 * L * (d * L).sinh()
    Ac = 3 * (d * L).exp() * (d * L).sinh() + d * L
    S2T = Sstar(2 * T)
    eps = (Ac ** 2 / (2 * T ** 2) + 8 * A ** 2 / T ** 2 + s2 / (2 * T.sqrt())
           + 4 * A ** 2 / (PI * T ** arb("0.75")) + (2 * A ** 2 / PI) * (T.log() + 1) / T
           + (c04 / PI) * (10 * A ** 2 / (PI * T ** 2) + 16 * PI * s2 / T ** 2)
           + 8 * A * B * S2T / T
           + 32 * A * B * (S2T + c112 + c278 / (2 * T).log()) / T)
    return 2 * s2 ** 2 - s2 * ((T / (2 * PI)).log() + 4 * PI * L * S2T) - eps


def T10(t):
    return (arb(t) * arb(10).log()).exp()


res = {"points": [], "delta_star": [], "intervals": []}
t0 = time.time()
T_PT = arb(3000175332800)
LN_PT = (T_PT / (2 * PI)).log() / 2
# (1) point certificates at reported L_B rounded up
pts = [("3000175332800", T_PT, "0.49", "6.490"), ("3000175332800", T_PT, "0.4", "7.938"),
       ("3000175332800", T_PT, "0.3", "10.565"), ("3000175332800", T_PT, "0.2", "15.819"),
       ("3000175332800", T_PT, "0.1", "31.581"),
       ("1e100", T10(100), "0.49", "8.262"), ("1e100", T10(100), "0.4", "10.102"), ("1e100", T10(100), "0.3", "13.443"),
       ("1e100", T10(100), "0.2", "20.123"), ("1e100", T10(100), "0.1", "40.162"), ("1e100", T10(100), "0.05", "80.239"),
       ("1e1000", T10(1000), "0.49", "10.734"), ("1e1000", T10(1000), "0.1", "52.318")]
for (lab, T, d, L) in pts:
    m = margin(L, T, d)
    res["points"].append({"T": lab, "delta": d, "L": L, "margin": m.str(8), "certified_positive": bool(m > 0)})
# delta* signs at L just below L_N(T_PT)
for d in ["0.2355", "0.24", "0.3", "0.4", "0.49"]:
    m = margin(LN_PT - arb("1e-6"), T_PT, d)
    res["delta_star"].append({"L": "L_N(T_PT)-1e-6", "delta": d, "margin": m.str(8), "certified_positive": bool(m > 0)})
for d in ["0.2354", "0.22"]:
    m = margin(LN_PT, T_PT, d)
    res["delta_star"].append({"L": "L_N(T_PT)", "delta": d, "margin": m.str(8), "certified_negative": bool(m < 0)})
res["L_N(T_PT)"] = LN_PT.str(12)


# (2) interval certificates
def certify_interval(L, d, ta, tb, depth=0, stats=None):
    t = arb((arb(ta) + arb(tb)) / 2, (arb(tb) - arb(ta)) / 2 * (1 + arb("1e-30")))
    m = margin(L, T10(t), d)
    stats["evals"] += 1
    if m > 0:
        return True
    if depth > 40:
        return False
    mid = (ta + tb) / 2
    return certify_interval(L, d, ta, mid, depth + 1, stats) and certify_interval(L, d, mid, tb, depth + 1, stats)


inv = [("6", "0.49", 4.94), ("8", "0.49", 76.97), ("8", "0.4", 13.50), ("10", "0.49", 513.14), ("10", "0.4", 92.06),
       ("10", "0.3", 6.68), ("12", "0.49", 3152.4), ("12", "0.4", 431.0), ("12", "0.3", 39.58)]
for (L, d, tmax) in inv:
    st = {"evals": 0}
    ok = certify_interval(L, d, 2.0, tmax, 0, st)
    res["intervals"].append({"L": L, "delta": d, "log10T_range": [2.0, tmax], "certified_positive_on_whole_range": ok,
                             "ball_evaluations": st["evals"]})
res["meta"] = {"python": platform.python_version(), "python-flint": flint.__version__, "prec_bits": 256,
               "runtime_s": round(time.time() - t0, 2)}
with open(OUT, "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
print("sha256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
