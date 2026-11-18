"""Adjudicator checks for C4-weil-window-locality (independent of investigator and skeptic code).

(a) coincidence window L_c = (1/2) log(gamma_1 / 2 pi), gamma_1 from Arb; 2 pi e^{2 * 0.405408}.
(b) kappa_c: root of sinh k = 2k (Arb-enclosed by bisection with ball sign tests).
(c) Theorem C4-B inequality, re-implemented from the REPORT text (mpmath, 50 digits):
    L_B(T, delta), delta* at the Platt-Trudgian height, the asymptotic coefficient (0.704 vs 1.407),
    and the INVERSE map: for a window L, the largest T (>= 100) with the C4-B margin > 0.
(d) Lattice-model aside: mirror-pair term with p sinc factors near the Nyquist edge, and the repair
    q(r) = (r+T0)^2 + delta^2.

Usage: python3 adj_numbers.py   (writes ../../../results/C4-weil-window-locality/adjudicator/adj_numbers.json)
"""
import json, time, os, hashlib, platform
import mpmath as mp
import flint

mp.mp.dps = 50
OUT = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/adjudicator/adj_numbers.json"
T_PT = mp.mpf("3000175332800")  # Platt-Trudgian 2021 verification height (rounded down)
res = {}
t0 = time.time()

# ---------------- (a) coincidence window ----------------
flint.ctx.prec = 200
g1 = flint.acb.zeta_zeros(1, 1)[0].imag if hasattr(flint.acb, "zeta_zeros") else None
g1s = g1.str(30, radius=False) if g1 is not None else "14.134725141734693790457251983562"
g1m = mp.mpf(g1s.strip("[]").split(" ")[0])
Lc = mp.log(g1m / (2 * mp.pi)) / 2
res["a_coincidence"] = {
    "gamma1": mp.nstr(g1m, 25),
    "L_c = (1/2)log(gamma1/2pi)": mp.nstr(Lc, 12),
    "2pi e^{2*0.405408}": mp.nstr(2 * mp.pi * mp.e ** (2 * mp.mpf("0.405408")), 10),
    "2pi e^{2*(log 2)/2} = 4pi": mp.nstr(4 * mp.pi, 10),
    "CC/Yoshida window L=(log 2)/2": mp.nstr(mp.log(2) / 2, 10),
}

# ---------------- (b) kappa_c ----------------
flint.ctx.prec = 200
lo, hi = flint.arb(2), flint.arb(3)
for _ in range(150):
    mid = (lo + hi) / 2
    v = mid.sinh() - 2 * mid
    if v < 0:
        lo = mid
    elif v > 0:
        hi = mid
    else:
        break
res["b_kappa_c"] = {"enclosure": [lo.str(20, radius=False), hi.str(20, radius=False)],
                    "method": "Arb bisection with certified signs of sinh(k)-2k"}

# ---------------- (c) Theorem C4-B ----------------
def Sstar(t):
    return mp.mpf("0.112") * mp.log(t) + mp.mpf("0.278") * mp.log(mp.log(t)) + mp.mpf("2.510")


def margin(L, T, d):
    """LHS - RHS of the C4-B inequality: 2 s^4 - s^2[log(T/2pi) + 4 pi L S*(2T)] - eps."""
    L, T, d = mp.mpf(L), mp.mpf(T), mp.mpf(d)
    s2 = mp.sinh(2 * d * L) / (2 * d) - L
    A = 2 * mp.sinh(d * L)
    B = 2 * L * mp.sinh(d * L)
    Ac = 3 * mp.e ** (d * L) * mp.sinh(d * L) + d * L
    S2T = Sstar(2 * T)
    eps = (Ac ** 2 / (2 * T ** 2) + 8 * A ** 2 / T ** 2 + s2 / (2 * mp.sqrt(T))
           + 4 * A ** 2 / (mp.pi * T ** mp.mpf(0.75)) + (2 * A ** 2 / mp.pi) * (mp.log(T) + 1) / T
           + (mp.mpf("0.4") / mp.pi) * (10 * A ** 2 / (mp.pi * T ** 2) + 16 * mp.pi * s2 / T ** 2)
           + 8 * A * B * S2T / T
           + 32 * A * B * (S2T + mp.mpf("0.112") + mp.mpf("0.278") / mp.log(2 * T)) / T)
    return 2 * s2 ** 2 - s2 * (mp.log(T / (2 * mp.pi)) + 4 * mp.pi * L * S2T) - eps


def L_B(T, d, Lmax=4000):
    """Smallest L (bisection, 1e-6) with margin > 0, scanning upward in steps of 0.05 first."""
    L = mp.mpf("0.05")
    prev = None
    while L < Lmax:
        if margin(L, T, d) > 0:
            lo_, hi_ = (prev if prev is not None else mp.mpf(0)), L
            for _ in range(40):
                m = (lo_ + hi_) / 2
                if margin(m, T, d) > 0:
                    hi_ = m
                else:
                    lo_ = m
            return hi_
        prev = L
        L += mp.mpf("0.05") if L < 50 else mp.mpf(1)
    return None


def LN(T):
    return mp.log(mp.mpf(T) / (2 * mp.pi)) / 2

tab = {}
for T in [T_PT, mp.mpf(10) ** 100, mp.mpf(10) ** 1000]:
    row = {}
    for d in ["0.49", "0.4", "0.3", "0.2354", "0.235", "0.22", "0.2", "0.1"]:
        lb = L_B(T, d)
        row[d] = mp.nstr(lb, 8) if lb is not None else None
    tab[mp.nstr(T, 12)] = {"L_N": mp.nstr(LN(T), 8), "L_B": row}
res["c1_LB_table"] = tab

# delta* at T_PT: smallest delta with L_B < L_N
lo_, hi_ = mp.mpf("0.2"), mp.mpf("0.3")
for _ in range(30):
    m = (lo_ + hi_) / 2
    if L_B(T_PT, m) < LN(T_PT):
        hi_ = m
    else:
        lo_ = m
res["c2_delta_star_at_T_PT"] = {"delta_star": mp.nstr(hi_, 8),
                                 "meaning": "for delta >= delta_star, L_B(T_PT,delta) < L_N(T_PT)"}

# asymptotic coefficient check: e^{2 d L_B}/(4 d) vs (0.5 + c L_B) log T for c = 0.704, 1.407
asy = []
for e10 in [100, 1000, 10000, 100000]:
    T = mp.mpf(10) ** e10
    for d in ["0.49", "0.3"]:
        lb = L_B(T, d, Lmax=10 ** 6)
        dd = mp.mpf(d)
        lhs = mp.e ** (2 * dd * lb) / (4 * dd)
        asy.append({"log10T": e10, "delta": d, "L_B": mp.nstr(lb, 8),
                    "ratio_to_(0.5+0.7037L)logT": mp.nstr(lhs / ((mp.mpf(0.5) + 2 * mp.pi * mp.mpf("0.112") * lb) * mp.log(T)), 6),
                    "ratio_to_(0.5+1.407L)logT": mp.nstr(lhs / ((mp.mpf(0.5) + 4 * mp.pi * mp.mpf("0.112") * lb) * mp.log(T)), 6)})
res["c3_asymptotic_coefficient"] = {"2pi*0.112": mp.nstr(2 * mp.pi * mp.mpf("0.112"), 6), "rows": asy}

# inverse map: for window L, largest T >= 100 with margin(L,T,d) > 0 (C4-B detection region)
inv = []
for L in ["0.8", "1.2", "2", "2.5", "3", "4", "5", "6", "8", "10", "12"]:
    row = {"L": L}
    for d in ["0.49", "0.4", "0.3", "0.2"]:
        if margin(L, 100, d) <= 0:
            row[d] = "none (margin<=0 already at T=100)"
            continue
        # margin decreases in T for large T; bisect in log10 T on [2, 1e7]
        a, b = mp.mpf(2), mp.mpf(2)
        while margin(L, mp.mpf(10) ** b, d) > 0 and b < 1e7:
            a, b = b, b * 2
        if b >= 1e7:
            row[d] = ">1e(1e7)"
            continue
        for _ in range(60):
            m = (a + b) / 2
            if margin(L, mp.mpf(10) ** m, d) > 0:
                a = m
            else:
                b = m
        row[d] = "log10 Tmax = " + mp.nstr(a, 6)
    inv.append(row)
res["c4_inverse_map"] = {"meaning": "Under H1 (single quadruple, all other zeros on the line), if W>=0 on window L then no "
                                    "off-line quadruple with 100 <= T <= Tmax(L,delta) and that delta (C4-B contrapositive). "
                                    "Valid only where the margin is positive on the whole T-range [100, Tmax]; checked "
                                    "on a grid below.", "rows": inv}
# monotonicity sanity check of margin in T on [100, Tmax] for the rows above (grid of 200 points in log10 T)
mono = []
for L in ["2", "3", "5", "10"]:
    for d in ["0.49", "0.3"]:
        if margin(L, 100, d) <= 0:
            continue
        vals = [margin(L, mp.mpf(10) ** (2 + k * mp.mpf("0.05")), d) for k in range(0, 400)]
        sign_changes = sum(1 for i in range(len(vals) - 1) if (vals[i] > 0) != (vals[i + 1] > 0))
        mono.append({"L": L, "delta": d, "sign_changes_on_log10T_in_[2,22]": sign_changes})
res["c5_inverse_map_sign_changes"] = mono

# ---------------- (d) lattice aside ----------------
# Lattice Gamma_R = lambda0 + s Z, s = 1 (Psi0 = 2pi), lambda0 = 0, T0 = k + 1/2.
def lattice_terms(T0, d, L, p, repair=False):
    s = mp.mpf(1); lam0 = mp.mpf(0)
    eps = (L - mp.pi / s) / p
    def h(r):
        sincp = (mp.sin(eps * (r - T0)) / (eps * (r - T0))) ** p if r != T0 else mp.mpf(1)
        val = (r - T0) * mp.sin(mp.pi * (r - lam0) / s) * sincp
        if repair:
            val *= (r + T0) ** 2 + d ** 2
        return val
    j = mp.mpc(0, 1)
    main = 2 * mp.re(h(T0 - j * d) * mp.conj(h(T0 + j * d)))
    mirror = 2 * mp.re(h(-T0 + j * d) * mp.conj(h(-T0 - j * d)))
    return main, mirror

lat = []
for (T0, d, dL) in [(mp.mpf("10.5"), mp.mpf("0.3"), mp.mpf("0.05")), (mp.mpf("10.5"), mp.mpf("0.3"), mp.mpf("0.5")),
                    (mp.mpf("100.5"), mp.mpf("0.3"), mp.mpf("0.05"))]:
    L = mp.pi + dL
    for p in [4, 8, 16, 32]:
        m1, m2 = lattice_terms(T0, d, L, p)
        lat.append({"T0": mp.nstr(T0, 6), "delta": mp.nstr(d, 3), "L-pi/s": mp.nstr(dL, 3), "p": p, "repair": False,
                    "main(+T0 pair)": mp.nstr(m1, 6), "mirror(-T0 pair)": mp.nstr(m2, 6)})
    for p in [6]:
        m1, m2 = lattice_terms(T0, d, L, p, repair=True)
        lat.append({"T0": mp.nstr(T0, 6), "delta": mp.nstr(d, 3), "L-pi/s": mp.nstr(dL, 3), "p": p, "repair": True,
                    "main(+T0 pair)": mp.nstr(m1, 6), "mirror(-T0 pair)": mp.nstr(m2, 6)})
res["d_lattice_mirror"] = lat

res["meta"] = {"python": platform.python_version(), "mpmath": mp.__version__, "python-flint": flint.__version__,
               "dps": mp.mp.dps, "runtime_s": round(time.time() - t0, 2)}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res, indent=1))
print("sha256", hashlib.sha256(open(OUT, "rb").read()).hexdigest())
