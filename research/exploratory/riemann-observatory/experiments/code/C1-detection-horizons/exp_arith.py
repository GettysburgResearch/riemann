#!/usr/bin/env python3
"""C1 / families (c) Nyman-Beurling and (d) arithmetic criteria (Nicolas/Robin, Schoenfeld psi, Mertens).

(d1) Nicolas criterion (primorials): RH <=> c(x) := log prod_{p<=x}(1-1/p)^{-1} - gamma - log log theta(x) > 0 for all x>=2.
     Leading-order explicit-formula model (derivation in REPORT, Sec. 5.2):
        G(u) := sqrt(x) log(x) c(x) ~ 2 + sum_rho x^{rho-1/2} / (rho (1-rho)),   u = log x,
     the sum being absolutely convergent. On the line: x^{i gamma}/(1/4+gamma^2); Nicolas (1983): under RH
     limsup/liminf of G = 2 +- beta, beta = sum 1/|rho|^2 = 0.0461...
     Collision model as in exp_li.py. Scan u for the first u with G(u) < 0.  On-line sum uses zeros gamma <= GCUT
     exactly; remainder bounded by sum_{gamma>GCUT} 2/(1/4+gamma^2) (reported as error band).
(d2) Schoenfeld/psi: amplitude-crossing horizon 2 x^delta/|rho0| = log(x)^2/(8 pi) and Buthe's rigorous partial-RH range.
(d3) Mertens: amplitude 2 x^delta / |rho0 zeta_mod'(rho0)| vs observed sup|M(x)|/sqrt(x) ~ 0.5 (heuristic).
(c)  Nyman-Beurling (Baez-Duarte/BDBLS normalisation, L^2(0,inf), chi = 1_(0,1]):
     exact floor F(rho0) = min ||chi - f||^2 forced by the conjugate pair rho0, conj(rho0) (Hardy-space argument,
     REPORT Thm N1), and N* = exp(C_on / F), C_on = sum_{on-line} 1/|rho|^2 (Burnol / BDBLS asymptotics).
Numerical class: NUMERICAL-NONRIGOROUS (float64/mpmath) on HEURISTIC leading-order models, except the NB floor,
which is an exact closed-form evaluation of a rigorous lower bound (floating point).
"""
import sys, time, math
import numpy as np
import mpmath as mp
from scipy import optimize
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common

T_START = time.time()
g, rad = common.load_zeros()
BETA = float(np.sum(2.0 / (0.25 + g**2)))   # partial sum of sum_rho 1/|rho|^2 over first 1e5 zeros (both signs)
BETA_FULL = 2 + common.EULER_GAMMA - math.log(4 * math.pi)
GCUT = 2000.0
gc = g[g <= GCUT]
amp_on = 2.0 / (0.25 + gc**2)
rem_band = BETA_FULL - float(np.sum(amp_on))

def nicolas_case(Tt, d):
    k = max(int(np.searchsorted(g, Tt)) - 1, 0)
    T = 0.5 * (g[k] + g[k + 1])
    rho0 = complex(0.5 + d, T); rho1 = complex(0.5 - d, T)
    c0 = 1.0 / (rho0 * (1 - rho0)); c1 = 1.0 / (rho1 * (1 - rho1))
    ga, gb = g[k], g[k + 1]
    # safe start: before u_a the off-line amplitude cannot beat 2 - beta - removed - rho1-term
    A0 = 2 * abs(c0)
    margin = 2 - BETA_FULL - 2 * (2 / (0.25 + ga**2) + 2 / (0.25 + gb**2)) - 2 * abs(c1)
    u_a = max(0.0, math.log(margin / A0) / d) if margin > A0 else 0.0
    u_pred = math.log(1.0 / abs(c0)) / d              # amplitude crossing 2 x^d |c0| = 2
    step = 0.05 / max(T, GCUT)
    u = u_a
    on_mask = np.abs(gc - ga) > 1e-9
    on_mask &= np.abs(gc - gb) > 1e-9
    gcm, ampm = gc[on_mask], amp_on[on_mask]
    while True:
        uu = u + step * np.arange(200000)
        S_on = (ampm[None, :] * np.cos(np.outer(uu, gcm))).sum(1) if len(gcm) else 0.0
        if ga > GCUT:   # removed zeros above GCUT are not in S_on; nothing to subtract
            pass
        Sq = 2 * np.real(np.exp((d + 1j * T) * uu) * c0 + np.exp((-d + 1j * T) * uu) * c1)
        G = 2 + S_on + Sq
        neg = np.nonzero(G < 0)[0]
        if len(neg):
            us = float(uu[neg[0]])
            return {"T": T, "delta": d, "u*=log x*": us, "u_pred=log|rho0(1-rho0)|/delta": u_pred, "u*/u_pred": us / u_pred,
                    "log10 x*": us / math.log(10), "error_band_on_line_tail": rem_band}
        u = float(uu[-1]) + step
        if u > 50 * u_pred + 100:
            return {"T": T, "delta": d, "u*": None}

rows_nic = []
for Tt in [17.6, 50, 100, 300, 1000, 3000, 10000]:
    for d in [0.01, 0.05, 0.1, 0.2, 0.3, 0.45]:
        t1 = time.time()
        r = nicolas_case(Tt, d); r["sec"] = round(time.time() - t1, 1)
        rows_nic.append(r); print("NIC", r, flush=True)

# ---------------- (d2) Schoenfeld psi horizons ----------------
def schoenfeld_u(T, d):
    rho = complex(0.5 + d, T)
    f = lambda u: math.log(2 / abs(rho)) + d * u - math.log(u * u / (8 * math.pi))
    lo, hi = 1.0, 10.0
    while f(hi) < 0:
        hi *= 2
    # first crossing from below; f(lo) may be >0 for tiny u (log u^2 -> -inf), so start at u where u^2/(8pi) >= 1
    lo = math.sqrt(8 * math.pi)
    return optimize.brentq(f, lo, hi) if f(lo) < 0 else lo

def buthe_x(T):
    """largest x with 4.92 sqrt(x/log x) <= T (Buthe 2016/18, Thm 2)."""
    h = lambda lx: 4.92 * math.sqrt(math.exp(lx) / lx) - T
    lx = optimize.brentq(h, 5, 200)
    return lx / math.log(10)

T0 = common.T0_PLATT_TRUDGIAN
rows_psi = []
for T in [100, 1e3, 1e4, 1e6, T0]:
    for d in [0.01, 0.1, 0.25, 0.5]:
        u = schoenfeld_u(T, d)
        rows_psi.append({"T": T, "delta": d, "u*=log x*": u, "log10 x*": u / math.log(10)})
buthe = {"T0": T0, "log10 x_Buthe(T0)": buthe_x(T0), "check: T=2.445e12 (paper says 1.4e25)": buthe_x(2.445e12)}
print("PSI", rows_psi, buthe, flush=True)

# ---------------- (d3) Mertens amplitude in the collision model ----------------
mp.mp.dps = 25
rows_mer = []
for Tt in [17.6, 100, 1000, 10000, 70000]:
    k = max(int(np.searchsorted(g, Tt)) - 1, 0)
    T = 0.5 * (g[k] + g[k + 1])
    for d in [0.01, 0.1, 0.25, 0.45]:
        rho0 = mp.mpc(0.5 + d, T); rho0p = mp.mpc(0.5 - d, T)
        ra, rb = mp.mpc(0.5, g[k]), mp.mpc(0.5, g[k + 1])
        z = mp.zeta(rho0)
        conjfac = (rho0 - mp.conj(rho0)) * (rho0 - mp.conj(rho0p)) / ((rho0 - mp.conj(ra)) * (rho0 - mp.conj(rb)))
        zp = z * (rho0 - rho0p) / ((rho0 - ra) * (rho0 - rb)) * conjfac
        amp_coef = 2 / abs(rho0 * zp)
        mtyp = 0.5
        u = math.log(mtyp / float(amp_coef)) / d if mtyp > amp_coef else 0.0
        rows_mer.append({"T": T, "delta": d, "|zeta(rho0)|": float(abs(z)), "|zeta_mod'(rho0)|": float(abs(zp)),
                         "2/|rho0 zeta_mod'(rho0)|": float(amp_coef), "u*=log x* (m_typ=0.5)": u, "log10 x*": u / math.log(10)})
print("MER", rows_mer, flush=True)

# ---------------- (c) Nyman-Beurling floor ----------------
def nb_floor(T, d, dps=40):
    mp.mp.dps = dps
    r1 = mp.mpc(0.5 + d, T); r2 = mp.conj(r1)
    rs = [r1, r2]
    H = mp.matrix(2, 2)
    for j in range(2):
        for k_ in range(2):
            H[j, k_] = 1 / (rs[j] + mp.conj(rs[k_]) - 1)
    a = mp.matrix([1 / r for r in rs]); b = mp.matrix([1 / (r - 1) for r in rs])
    Hi = H**-1
    aa = (a.H * Hi * a)[0]; bb = (b.H * Hi * b)[0]; ba = (b.H * Hi * a)[0]
    F = aa - abs(ba)**2 / (1 + bb)
    single = (2 * d) / (abs(r1)**2 * (1 + (2 * d) / abs(r1 - 1)**2))
    return float(mp.re(F)), float(single)

rows_nb = []
for T in [17.578, 100, 1e3, 1e4, 7e4, 1e6, T0]:
    for d in [0.01, 0.1, 0.25, 0.5]:
        F, single = nb_floor(T, d, dps=40 if T < 1e7 else 60)
        C_on = BETA_FULL   # removal of two zeros changes it by < 4/T^2
        logN = C_on / F
        rows_nb.append({"T": T, "delta": d, "F_pair": F, "F_single_zero": single, "4delta/T^2": 4 * d / T**2,
                        "log N* = C_on/F": logN, "log10 log10 N*": math.log10(logN / math.log(10)) if logN > math.log(10) else None})
print("NB", rows_nb, flush=True)

out = {"campaign": "C1-detection-horizons", "experiment": "arithmetic criteria + Nyman-Beurling horizons",
       "env": common.env(), "beta_partial_1e5": BETA, "beta_full=2+gamma-log4pi": BETA_FULL, "GCUT": GCUT,
       "nicolas": rows_nic, "psi_schoenfeld": rows_psi, "buthe": buthe, "mertens": rows_mer, "nyman_beurling": rows_nb,
       "runtime_s": time.time() - T_START}
p = common.save_json("arith_nb.json", out)
print("saved", p, common.sha256(p), "runtime", out["runtime_s"])
