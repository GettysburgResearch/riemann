"""Evaluate the sufficient condition of Theorem C4-B (growth detection under the single-defect
hypothesis H1) and tabulate the guaranteed window L_B(T, delta), the Nyquist window
L_N = (1/2) log(T/2pi) and the flat-model window L_flat.

Sufficient condition (proved in the C4 report, test function g(x) = e^{-iTx} sinh(delta x) on [-L, L]):
    2 sigma^4 > sigma^2 [log(T/2pi) + 4 pi L S*(2T)] + eps(T, delta, L),
    sigma^2 = sinh(2 delta L)/(2 delta) - L,  S*(t) = 0.112 log t + 0.278 log log t + 2.510 (Trudgian 2014),
    eps = E1 + F0 + E2 + E3 + E4 + 8 A B S*(2T)/T + E5   (explicit, see report),
    A = 2 sinh(delta L), B = 2 L sinh(delta L), Ac = 3 sinh(delta L) e^{delta L} + delta L.
All arithmetic in mpmath (50 digits); this is an evaluation of explicit closed-form inequalities.
"""
import sys, os, json, math, hashlib
import mpmath as mp
mp.mp.dps = 50
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"


def Sstar(t):
    t = max(mp.mpf(t), mp.e)
    return mp.mpf('0.112') * mp.log(t) + mp.mpf('0.278') * mp.log(mp.log(t)) + mp.mpf('2.510')


def margin(T, d, L):
    T, d, L = mp.mpf(T), mp.mpf(d), mp.mpf(L)
    s2 = mp.sinh(2 * d * L) / (2 * d) - L
    A = 2 * mp.sinh(d * L)
    B = 2 * L * mp.sinh(d * L)
    Ac = 3 * mp.sinh(d * L) * mp.exp(d * L) + d * L
    S2T = Sstar(2 * T)
    E1 = Ac ** 2 / (2 * T ** 2)
    F0 = 8 * A ** 2 / T ** 2
    E2 = s2 / (2 * mp.sqrt(T)) + 4 * A ** 2 / (mp.pi * T ** mp.mpf(0.75))
    E3 = (2 * A ** 2 / mp.pi) * (mp.log(T) + 1) / T
    E4 = (mp.mpf('0.4') / mp.pi) * (20 * A ** 2 / (2 * mp.pi * T ** 2) + 16 * mp.pi * s2 / T ** 2)
    E5 = 32 * A * B * (S2T + mp.mpf('0.112') + mp.mpf('0.278') / mp.log(2 * T)) / T
    eps = E1 + F0 + E2 + E3 + E4 + 8 * A * B * S2T / T + E5
    return 2 * s2 ** 2 - s2 * (mp.log(T / (2 * mp.pi)) + 4 * mp.pi * L * S2T) - eps


def L_B(T, d, Lmax=400):
    """Smallest L (bisection, assuming the margin changes sign once) with margin > 0."""
    lo, hi = mp.mpf('0.01'), mp.mpf(1)
    while margin(T, d, hi) <= 0:
        hi *= 2
        if hi > Lmax:
            return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if margin(T, d, mid) > 0:
            hi = mid
        else:
            lo = mid
    return float(hi)


def L_flat(T, d):
    T, d = mp.mpf(T), mp.mpf(d)
    f = lambda L: mp.sinh(2 * d * L) / (2 * d) - L - mp.log(T / (2 * mp.pi)) / 2
    lo, hi = mp.mpf('1e-9'), mp.mpf(1)
    while f(hi) < 0:
        hi *= 2
    for _ in range(120):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return float((lo + hi) / 2)


def main():
    Ts = ['1e4', '1e6', '1e8', '1e10', '3e12', '1e13', '1e16', '1e20', '1e30', '1e50', '1e100', '1e1000']
    ds = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49]
    rows = []
    for Ts_ in Ts:
        T = mp.mpf(Ts_)
        LN = float(mp.log(T / (2 * mp.pi)) / 2)
        for d in ds:
            lb = L_B(T, d)
            rows.append({"T": Ts_, "delta": d, "L_N": LN, "L_flat": L_flat(T, d), "L_B": lb,
                         "L_B_over_L_N": None if lb is None else lb / LN})
    # crossover: smallest T (as log10) with L_B(T, d) < L_N(T)
    cross = {}
    for d in ds:
        lo, hi = mp.mpf(4), mp.mpf(4000)
        f = lambda x: (L_B(mp.mpf(10) ** x, d, Lmax=10 ** 6) or 1e9) - float(mp.log(mp.mpf(10) ** x / (2 * mp.pi)) / 2)
        if f(hi) > 0:
            cross[d] = None
            continue
        for _ in range(40):
            mid = (lo + hi) / 2
            if f(mid) < 0:
                hi = mid
            else:
                lo = mid
        cross[d] = float(hi)
    out = {"meta": {"mpmath": mp.__version__, "dps": 50, "S_bound": "Trudgian 2014: |S(t)| <= 0.112 log t + 0.278 log log t + 2.510, t >= e"},
           "rows": rows, "log10T_crossover_LB_below_LN": cross}
    path = os.path.join(RES, "thmB_table.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    for r in rows:
        print("%7s d=%.2f  L_N=%9.3f  L_flat=%8.3f  L_B=%s" % (r["T"], r["delta"], r["L_N"], r["L_flat"],
              "None" if r["L_B"] is None else "%.3f" % r["L_B"]))
    print("crossover log10 T:", cross)
    print("wrote", path, hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
