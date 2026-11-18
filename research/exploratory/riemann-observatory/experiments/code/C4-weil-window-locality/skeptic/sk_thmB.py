"""SKEPTIC (C4): independent checks of Theorem C4-B / C4-B2.

(1) Re-implementation (from the REPORT statement, not from thmB_bound.py) of the sufficient condition
    2 s^4 > s^2 [log(T/2pi) + 4 pi L S*(2T)] + eps  and of L_B(T, delta), crossover log10 T.
(2) Ingredient checks: what(+-i delta) = -+ ... , ||what||^2 = 2 pi s^2, |what(s)| <= 2A/|s|,
    |what'(s)| <= 2B/|s| (real s), |what(z)| <= Ac/|z| (|Im z| <= delta), theta' bounds.
(3) Against true zeros (first 100000 Arb ordinates + smooth tail): P(g0) = sum_{gamma>0} F(gamma),
    F(t) = |what(t-T)|^2 + |what(t+T)|^2, compared with the C4-B upper bound for P and with the flat value
    s^2 log(T/2pi); and the main-term integral (1/pi) int F theta' vs s^2 log(T/2pi) + E2 + E3 + E4.
mpmath / numpy, non-rigorous evaluation.
"""
import os, json, math
import numpy as np
import mpmath as mp

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic"
ZD = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data"
mp.mp.dps = 40


def Sst(t):
    t = mp.mpf(t)
    return mp.mpf("0.112") * mp.log(t) + mp.mpf("0.278") * mp.log(mp.log(t)) + mp.mpf("2.510")


def parts(T, d, L):
    T, d, L = mp.mpf(T), mp.mpf(d), mp.mpf(L)
    s2 = mp.sinh(2 * d * L) / (2 * d) - L
    A = 2 * mp.sinh(d * L); B = 2 * L * mp.sinh(d * L); Ac = 3 * mp.exp(d * L) * mp.sinh(d * L) + d * L
    S2 = Sst(2 * T)
    eps = (Ac ** 2 / (2 * T ** 2) + 8 * A ** 2 / T ** 2 + s2 / (2 * mp.sqrt(T)) + 4 * A ** 2 / (mp.pi * T ** mp.mpf("0.75"))
           + (2 * A ** 2 / mp.pi) * (mp.log(T) + 1) / T + (mp.mpf("0.4") / mp.pi) * (10 * A ** 2 / (mp.pi * T ** 2) + 16 * mp.pi * s2 / T ** 2)
           + 8 * A * B * S2 / T + 32 * A * B * (S2 + mp.mpf("0.112") + mp.mpf("0.278") / mp.log(2 * T)) / T)
    Pbound = s2 * (mp.log(T / (2 * mp.pi)) + 4 * mp.pi * L * S2) + eps - Ac ** 2 / (2 * T ** 2)
    return s2, Pbound, eps


def margin(T, d, L):
    s2, Pb, eps = parts(T, d, L)
    return 2 * s2 ** 2 - (s2 * (mp.log(mp.mpf(T) / (2 * mp.pi)) + 4 * mp.pi * mp.mpf(L) * Sst(2 * mp.mpf(T))) + eps)


def LB(T, d):
    f = lambda L: margin(T, d, L)
    lo, hi = mp.mpf("0.05"), mp.mpf("1")
    while f(hi) <= 0:
        lo, hi = hi, 2 * hi
    # check single sign change on a coarse grid below hi
    for _ in range(100):
        m = (lo + hi) / 2
        if f(m) > 0:
            hi = m
        else:
            lo = m
    return float(hi)


def LN(T):
    return float(mp.log(mp.mpf(T) / (2 * mp.pi)) / 2)


def what(s, d, L):
    """int_{-L}^{L} sinh(d x) e^{i s x} dx (closed form, valid for complex s != +-i d)."""
    return 2j * (d * mp.cosh(d * L) * mp.sin(s * L) - s * mp.sinh(d * L) * mp.cos(s * L)) / (d * d + s * s)


out = {"table": [], "crossover": {}, "ingredients": [], "zeros_check": []}
# (1) table
for Ts in ["1e4", "1e10", "3e12", "1e100", "1e1000"]:
    for d in [0.05, 0.1, 0.2, 0.3, 0.4, 0.49]:
        T = mp.mpf(Ts)
        r = {"T": Ts, "delta": d, "L_N": LN(T), "L_B": LB(T, d)}
        out["table"].append(r)
for d in [0.49, 0.45, 0.4, 0.3, 0.2, 0.1, 0.05, 0.01]:
    lo, hi = mp.mpf(3), mp.mpf(1000)
    g = lambda x: LB(mp.mpf(10) ** x, d) - LN(mp.mpf(10) ** x)
    if g(hi) > 0:
        out["crossover"][str(d)] = None
        continue
    for _ in range(30):
        m = (lo + hi) / 2
        if g(m) < 0:
            hi = m
        else:
            lo = m
    out["crossover"][str(d)] = float(hi)
print(json.dumps(out["crossover"]))
for r in out["table"]:
    print(r)

# (2) ingredients
for d in [0.1, 0.3, 0.49]:
    for L in [0.5, 2.0, 5.0]:
        d_, L_ = mp.mpf(d), mp.mpf(L)
        s2 = mp.sinh(2 * d_ * L_) / (2 * d_) - L_
        wm = mp.quad(lambda x: mp.sinh(d_ * x) * mp.exp(d_ * x), [-L_, L_])     # what(-i d)
        wp = mp.quad(lambda x: mp.sinh(d_ * x) * mp.exp(-d_ * x), [-L_, L_])    # what(+i d)
        A = 2 * mp.sinh(d_ * L_); B = 2 * L_ * mp.sinh(d_ * L_); Ac = 3 * mp.exp(d_ * L_) * mp.sinh(d_ * L_) + d_ * L_
        ss = np.linspace(0.05, 400, 20001)
        r1 = max(float(abs(what(mp.mpf(s), d_, L_)) * s / (2 * A)) for s in ss[::20])
        wder = lambda s: mp.diff(lambda u: what(u, d_, L_), s)
        r2 = max(float(abs(wder(mp.mpf(s))) * s / (2 * B)) for s in ss[::400])
        r3 = 0.0
        for s in ss[::400]:
            for im in (-d, -d / 2, 0, d / 2, d):
                z = mp.mpc(s, im)
                r3 = max(r3, float(abs(what(z, d_, L_)) * abs(z) / Ac))
        out["ingredients"].append({"delta": d, "L": L, "what(-i d)/s2": float(wm / s2), "what(+i d)/s2": float(wp / s2),
                                   "max |what| s/(2A)": r1, "max |what'| s/(2B)": r2, "max |what(z)||z|/Ac": r3})
th1 = lambda t: mp.diff(mp.siegeltheta, t)
tb = [float(th1(t)) for t in np.linspace(0.05, 2 * math.pi, 60)]
tc = [float((th1(t) - mp.log(t / (2 * mp.pi)) / 2) * t * t) for t in np.linspace(2 * math.pi, 2000, 80)]
out["theta"] = {"max theta' on (0,2pi]": max(tb), "max (theta'-0.5log(t/2pi)) t^2 on [2pi,2000]": max(tc),
                "min (theta'-0.5log(t/2pi)) t^2": min(tc)}
print(json.dumps(out["ingredients"], indent=0)[:2000]); print(out["theta"])

# (3) zeros check
g = np.concatenate([np.loadtxt(os.path.join(ZD, f), usecols=1) for f in ("zeros_1_50000.tsv", "zeros_50001_100000.tsv")])
G = g[-1]


def w_np(s, d, L):
    return 2 * (d * np.cosh(d * L) * np.sin(s * L) - s * np.sinh(d * L) * np.cos(s * L)) / (d * d + s * s)


for T in [1000.0, 1.0e4, 3.0e4]:
    for d in [0.1, 0.3, 0.49]:
        for L in [1.0, 2.0, 3.0, 4.0]:
            F = w_np(g - T, d, L) ** 2 + w_np(g + T, d, L) ** 2
            P = float(np.sum(F))
            # smooth tail: average |what(s)|^2 ~ 2 sinh^2(dL)/s^2
            c = 2 * math.sinh(d * L) ** 2
            tail = float(mp.quad(lambda t: c * (1 / (t - T) ** 2 + 1 / (t + T) ** 2) * mp.log(t / (2 * mp.pi)) / (2 * mp.pi), [G, mp.inf]))
            s2, Pb, eps = parts(T, d, L)
            # main-term integral (1/pi) int_0^inf F theta'
            Fm = lambda t: (what(t - T, mp.mpf(d), mp.mpf(L)) * mp.conj(what(t - T, mp.mpf(d), mp.mpf(L)))).real + \
                           (what(t + T, mp.mpf(d), mp.mpf(L)) * mp.conj(what(t + T, mp.mpf(d), mp.mpf(L)))).real
            th = lambda t: (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2)) - mp.log(mp.pi)) / 2
            pts = [0, 2 * math.pi] + [T + k for k in range(-200, 201, 10)] + [3 * T, 30 * T, mp.inf]
            pts = sorted(set([p for p in pts if (p == mp.inf or p >= 0)]), key=lambda x: float(x) if x != mp.inf else 1e300)
            mt = float(mp.quad(lambda t: Fm(t) * th(t), pts) / mp.pi)
            T_, d_, L_ = mp.mpf(T), mp.mpf(d), mp.mpf(L)
            A = 2 * mp.sinh(d_ * L_)
            E234 = float(s2 / (2 * mp.sqrt(T_)) + 4 * A ** 2 / (mp.pi * T_ ** mp.mpf("0.75")) + (2 * A ** 2 / mp.pi) * (mp.log(T_) + 1) / T_
                         + (mp.mpf("0.4") / mp.pi) * (10 * A ** 2 / (mp.pi * T_ ** 2) + 16 * mp.pi * s2 / T_ ** 2))
            rec = {"T": T, "delta": d, "L": L, "P_zeros": P + tail, "tail": tail, "flat s2*log(T/2pi)": float(s2 * mp.log(T_ / (2 * mp.pi))),
                   "C4B_P_upper_bound": float(Pb), "bound_holds": bool(P + tail <= float(Pb)),
                   "main_term_integral": mt, "main_term_bound": float(s2 * mp.log(T_ / (2 * mp.pi))) + E234,
                   "main_bound_holds": bool(mt <= float(s2 * mp.log(T_ / (2 * mp.pi))) + E234),
                   "Wmod_additive(g0)=P-2s4": P + tail - 2 * float(s2) ** 2, "C4B_margin": float(margin(T, d, L))}
            out["zeros_check"].append(rec)
            print(json.dumps(rec), flush=True)
json.dump(out, open(os.path.join(RES, "sk_thmB.json"), "w"), indent=1)
