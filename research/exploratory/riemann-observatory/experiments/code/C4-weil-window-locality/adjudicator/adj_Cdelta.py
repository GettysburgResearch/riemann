"""Adjudicator: the constant C(delta) = sup_{T>=Tmin} [L_B(T,delta) - L_N(T)], Tmin = 100 and Tmin = T_PT = 3000175332800, implied by Theorem C4-B.

Under H1, monotonicity in L (nested windows) gives: a quadruple at (T,delta), T >= 100, forces
lambda_min(L) < 0 for every L >= L_N(T) + C(delta).  Finiteness of C(delta) is elementary (see FINAL.md);
here its value is (i) located on a grid in log10 T with mpmath (non-rigorous), and (ii) certified as an
upper bound with Arb on the whole range T in [100, 10^tmax]: for each T-interval [T1,T2] of the cover we
exhibit one L0 <= L_N(T1) + C_cert with margin(L0, T, delta) > 0 for all T in [T1,T2] (ball in T).
Beyond 10^tmax the argument is the asymptotic one in FINAL.md (L_B - L_N -> -infinity), checked by Arb
at L = L_N(T) on [10^(tmax/2), 10^tmax].
Usage: python3 adj_Cdelta.py
"""
import json, time, hashlib, platform
import mpmath as mp
import flint
from flint import arb

mp.mp.dps = 30
flint.ctx.prec = 256
OUT = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/adjudicator/adj_Cdelta.json"

PI = arb.pi()
c112, c278, c251, c04 = arb("0.112"), arb("0.278"), arb("2.510"), arb("0.4")


def Sstar_a(t):
    return c112 * t.log() + c278 * t.log().log() + c251


def margin_a(L, T, d):
    L, d = arb(L), arb(d)
    s2 = (2 * d * L).sinh() / (2 * d) - L
    A = 2 * (d * L).sinh(); B = 2 * L * (d * L).sinh()
    Ac = 3 * (d * L).exp() * (d * L).sinh() + d * L
    S2T = Sstar_a(2 * T)
    eps = (Ac ** 2 / (2 * T ** 2) + 8 * A ** 2 / T ** 2 + s2 / (2 * T.sqrt())
           + 4 * A ** 2 / (PI * T ** arb("0.75")) + (2 * A ** 2 / PI) * (T.log() + 1) / T
           + (c04 / PI) * (10 * A ** 2 / (PI * T ** 2) + 16 * PI * s2 / T ** 2)
           + 8 * A * B * S2T / T + 32 * A * B * (S2T + c112 + c278 / (2 * T).log()) / T)
    return 2 * s2 ** 2 - s2 * ((T / (2 * PI)).log() + 4 * PI * L * S2T) - eps


def margin_m(L, T, d):
    L, T, d = mp.mpf(L), mp.mpf(T), mp.mpf(d)
    s2 = mp.sinh(2 * d * L) / (2 * d) - L
    A = 2 * mp.sinh(d * L); B = 2 * L * mp.sinh(d * L)
    Ac = 3 * mp.e ** (d * L) * mp.sinh(d * L) + d * L
    S2T = mp.mpf("0.112") * mp.log(2 * T) + mp.mpf("0.278") * mp.log(mp.log(2 * T)) + mp.mpf("2.510")
    eps = (Ac ** 2 / (2 * T ** 2) + 8 * A ** 2 / T ** 2 + s2 / (2 * mp.sqrt(T))
           + 4 * A ** 2 / (mp.pi * T ** mp.mpf(0.75)) + (2 * A ** 2 / mp.pi) * (mp.log(T) + 1) / T
           + (mp.mpf("0.4") / mp.pi) * (10 * A ** 2 / (mp.pi * T ** 2) + 16 * mp.pi * s2 / T ** 2)
           + 8 * A * B * S2T / T + 32 * A * B * (S2T + mp.mpf("0.112") + mp.mpf("0.278") / mp.log(2 * T)) / T)
    return 2 * s2 ** 2 - s2 * (mp.log(T / (2 * mp.pi)) + 4 * mp.pi * L * S2T) - eps


def LB_m(T, d):
    lo, hi = mp.mpf("0.01"), mp.mpf(1)
    while margin_m(hi, T, d) <= 0:
        lo, hi = hi, hi * 2
    # scan upward from lo in coarse steps to catch the FIRST positive point
    step = (hi - lo) / 200
    L = lo
    while margin_m(L, T, d) <= 0:
        L += step
    a, b = L - step, L
    for _ in range(40):
        m = (a + b) / 2
        if margin_m(m, T, d) > 0:
            b = m
        else:
            a = m
    return b


def LN_m(T):
    return mp.log(mp.mpf(T) / (2 * mp.pi)) / 2


t0 = time.time()
out = {"rows": []}
T_PT_m = mp.mpf(3000175332800)
for tmin in [mp.mpf(2), mp.log10(T_PT_m)]:
    for d, tmax in [("0.49", 40), ("0.4", 40), ("0.3", 60), ("0.2", 80), ("0.1", 160), ("0.05", 300), ("0.01", 1200)]:
        # (i) grid search
        best = None
        ngrid = 240
        for k in range(ngrid + 1):
            t = tmin + (tmax - tmin) * mp.mpf(k) / ngrid
            T = mp.mpf(10) ** t
            diff = LB_m(T, d) - LN_m(T)
            if best is None or diff > best[1]:
                best = (t, diff)
        # refine around best
        a, b = max(mp.mpf(tmin), best[0] - (tmax - tmin) / ngrid), best[0] + (tmax - tmin) / ngrid
        for _ in range(30):
            m1, m2 = a + (b - a) / 3, b - (b - a) / 3
            f1 = LB_m(mp.mpf(10) ** m1, d) - LN_m(mp.mpf(10) ** m1)
            f2 = LB_m(mp.mpf(10) ** m2, d) - LN_m(mp.mpf(10) ** m2)
            if f1 < f2:
                a = m1
            else:
                b = m2
        tstar = (a + b) / 2
        Cnum = LB_m(mp.mpf(10) ** tstar, d) - LN_m(mp.mpf(10) ** tstar)
        # (ii) Arb certificate of C_cert = Cnum rounded up to 2 decimals + 0.01, on [100, 10^tmax]
        Cc = mp.ceil(Cnum * 100) / 100 + mp.mpf("0.01")
        Cc_a = arb(mp.nstr(Cc, 10))
        cover_ok, nint = True, 0
        t_lo = mp.mpf(tmin)
        while t_lo < tmax:
            # try to extend the interval as far as possible (doubling the width) with L0 = L_N(10^t_lo) + Cc
            w = mp.mpf("0.001")
            L0 = arb(mp.nstr(LN_m(mp.mpf(10) ** t_lo), 30)) + Cc_a - arb("1e-20")
            def ok(width):
                tb = arb(mp.nstr(t_lo, 25)), arb(mp.nstr(min(t_lo + width, tmax), 25))
                tball = arb((tb[0] + tb[1]) / 2, (tb[1] - tb[0]) / 2 * (1 + arb("1e-25")))
                return margin_a(L0, (tball * arb(10).log()).exp(), d) > 0
            if not ok(w):
                cover_ok = False
                break
            while t_lo + w < tmax and ok(2 * w):
                w *= 2
            t_lo = min(t_lo + w, mp.mpf(tmax))
            nint += 1
        # tail check: margin at L = L_N(T) on [10^(tmax/2), 10^tmax], log10-T steps of 0.05
        tail_ok = True
        t_lo = mp.mpf(tmax) / 2
        ntail = 0
        while t_lo < tmax and tail_ok:
            w = mp.mpf("0.05")  # narrow: Arb exp() of a wide ball is a crude midpoint-radius enclosure
            tb0, tb1 = arb(mp.nstr(t_lo, 25)), arb(mp.nstr(min(t_lo + w, tmax), 25))
            tball = arb((tb0 + tb1) / 2, (tb1 - tb0) / 2 * (1 + arb("1e-25")))
            Tb = (tball * arb(10).log()).exp()
            Lb = (Tb / (2 * PI)).log() / 2
            tail_ok = bool(margin_a(Lb, Tb, d) > 0)
            t_lo += w
            ntail += 1
        out["rows"].append({"delta": d, "argmax_log10T": mp.nstr(tstar, 6), "C_numerical": mp.nstr(Cnum, 6),
                            "C_certified_upper": mp.nstr(Cc, 6), "certified_on_log10T_range": [mp.nstr(tmin, 8), tmax], "T_min": mp.nstr(mp.mpf(10) ** tmin, 12),
                            "cover_ok": cover_ok, "cover_intervals": nint,
                            "tail_margin_at_L_N_positive_on_[tmax/2,tmax]": tail_ok})
        print(out["rows"][-1], flush=True)
out["meta"] = {"python": platform.python_version(), "mpmath": mp.__version__, "python-flint": flint.__version__,
               "runtime_s": round(time.time() - t0, 1)}
with open(OUT, "w") as fh:
    json.dump(out, fh, indent=1)
print("sha256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
