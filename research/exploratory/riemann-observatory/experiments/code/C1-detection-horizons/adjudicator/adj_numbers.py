#!/usr/bin/env python3
"""C1-detection-horizons -- ADJUDICATOR independent numerics (mpmath, NUMERICAL-NONRIGOROUS high precision).

Written from scratch by the adjudicator. It does not import the investigator's or the skeptic's code.
It settles the numerical points where REPORT.md and SKEPTIC_REVIEW.md disagree or where FINAL.md needs a number.

 (a) Li single-defect sign index at T0 (amplitude crossing 4 cosh(n a) = lambda_n^RH-trend), ratio to the
     leading formula (T^2/delta) log(T^2/delta) and to n_2 = X(log X + 2 log log X - log 4).
 (b) Constant c(T) = n_amp / (T^2 log T) for one quadruple with delta -> 1/2 just above T (C1-L4 barrier).
 (c) THEOREM L1: analytic tail bounds from Rosser's N(T) estimate, written out, plus the final margin.
 (d) THEOREM N1: F/(4 delta/T^2) and the scaled error (1 - ratio) T^2, to fix the order of the error term.
 (e) psi/pi implication horizons at T0: Buthe (4.92 sqrt(x/log x) <= T) and Johnston (9.06/loglog x * sqrt(x/log x) <= T).
 (f) de Bruijn-Newman gap-lattice collapse time t_c(T0, delta) (closed-form integral of C1-E1).
 (g) Nyman-Beurling model scale at T0 with the two-zero floor and with the one-zero corollary.
 (h) Nicolas constant beta = 2 + gamma - log 4 pi; Nicolas single-defect x*; C1-D3 sketch horizon at T0.
"""
import json, time, math, hashlib, platform, sys
import mpmath as mp

t0 = time.time()
mp.mp.dps = 50
T0 = mp.mpf(3000175332800)
EG = mp.euler
R_MTY = mp.mpf('5.558691')   # Mossinghoff-Trudgian-Yang 2022 (arXiv:2212.06867 abstract)
R_MT = mp.mpf('5.573412')    # Mossinghoff-Trudgian 2015 (as quoted by Platt-Trudgian 2021, Sec. 3.2)
out = {"campaign": "C1-detection-horizons", "role": "adjudicator", "script": "adj_numbers.py",
       "env": {"python": platform.python_version(), "mpmath": mp.__version__}, "dps": mp.mp.dps}

def a_of(T, d):
    """a = -log|1 - 1/rho0|, rho0 = 1/2 + d + iT (exact)."""
    u = 2 * d / ((mp.mpf(1) / 2 + d)**2 + T**2)     # 1 - |z|^2
    return -mp.log1p(-u) / 2

def trend(n):
    return n / 2 * (mp.log(n) - 1 + EG - mp.log(2 * mp.pi))

def n_amp(a):
    X = 1 / a
    f = lambda n: 4 * mp.cosh(n * a) - trend(n)
    lo, hi = X, X
    while f(lo) > 0: lo /= 2
    while f(hi) < 0: hi *= 2
    for _ in range(400):            # bisection (f < 0 at lo, f > 0 at hi)
        mid = (lo + hi) / 2
        if f(mid) < 0: lo = mid
        else: hi = mid
        if hi - lo < 1e-30 * hi: break
    return (lo + hi) / 2

# ---------- (a) Li at T0 ----------
dmax_MTY = mp.mpf(1) / 2 - 1 / (R_MTY * mp.log(T0))
dmax_MT = mp.mpf(1) / 2 - 1 / (R_MT * mp.log(T0))
rows = []
for d in [dmax_MTY, mp.mpf('0.25'), mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001')]:
    a = a_of(T0, d); X = 1 / a; LX = mp.log(X)
    na = n_amp(a)
    lead = T0**2 / d * mp.log(T0**2 / d)
    n2 = X * (LX + 2 * mp.log(LX) - mp.log(4))
    rows.append({"delta": float(d), "X=1/a": float(X), "X/(T^2/delta)": float(X / (T0**2 / d)),
                 "n_amp": float(na), "n_amp/lead": float(na / lead), "n_amp/n_2": float(na / n2)})
out["a_li_T0"] = {"T0": float(T0), "delta_max_MTY(5.558691)": float(dmax_MTY), "delta_max_MT(5.573412)": float(dmax_MT),
                  "rows": rows,
                  "note": "lambda^RH replaced by the RH trend; c_off ~ 1.8 and the removed on-line pair (|.|<=8) shift n_amp by a relative ~1e-26 at T0."}

# ---------- (b) L4 barrier constant ----------
rowsb = []
for T in [mp.mpf(100), mp.mpf(150), mp.mpf(1000), mp.mpf(10)**4, mp.mpf(10)**6, mp.mpf(10)**9, T0, mp.mpf(10)**30, mp.mpf(10)**100, mp.mpf(10)**1000]:
    a = a_of(T, mp.mpf(1) / 2 - mp.mpf(10)**-30)   # delta -> 1/2
    na = n_amp(a)
    rowsb.append({"T": mp.nstr(T, 6), "X*1/(2T^2)": float(1 / a / (2 * T**2)), "n_amp/(T^2 log T)": float(na / (T**2 * mp.log(T)))})
out["b_L4_single_quadruple_barrier"] = rowsb

# ---------- (c) THEOREM L1: tail bounds (analytic) and margin ----------
# Rosser 1941: |N(t) - M(t)| <= R(t) = 0.137 log t + 0.443 log log t + 1.588 (t >= 2), M(t) = (t/2pi) log(t/2pi e) + 7/8.
# For t >= T >= 100: R(t) <= R(T) + 0.58 log(t/T).
# Upper: sum_{gamma>T} gamma^-4 = int_T^inf 4 t^-5 (N(t)-N(T)) dt <= (1/(6 pi T^3))(log(T/2pi)+1/3) + (2R(T)+0.145)/T^4 =: U4(T)
# Lower: sum_{gamma>=n} gamma^-2 >= (log(n/2pi)+1)/(2 pi n) - (2R(n)+0.29)/n^2 =: L2(n)
R = lambda t: mp.mpf('0.137') * mp.log(t) + mp.mpf('0.443') * mp.log(mp.log(t)) + mp.mpf('1.588')
U4 = lambda T: (mp.log(T / (2 * mp.pi)) + mp.mpf(1) / 3) / (6 * mp.pi * T**3) + (2 * R(T) + mp.mpf('0.145')) / T**4
L2 = lambda n: (mp.log(n / (2 * mp.pi)) + 1) / (2 * mp.pi * n) - (2 * R(n) + mp.mpf('0.29')) / n**2
claimU4 = lambda T: 2 * (mp.log(T / (2 * mp.pi)) + mp.mpf(1) / 3) / (3 * mp.pi * T**3)
claimL2 = lambda n: mp.log(n / (2 * mp.pi)) / (10 * mp.pi * n)
rowsc = []
for T in [mp.mpf(100), mp.mpf(317), mp.mpf(10)**3, mp.mpf(10)**6, mp.mpf(10)**9, T0]:
    marg = mp.mpf('0.0894') * T * mp.log(T / (2 * mp.pi)) - mp.mpf('0.1881') * (mp.log(T / (2 * mp.pi)) + mp.mpf(1) / 3)
    rowsc.append({"T": mp.nstr(T, 8), "U4/claimU4": float(U4(T) / claimU4(T)), "claimL2/L2(T)": float(claimL2(T) / L2(T)),
                  "claimL2/L2(T^2)": float(claimL2(T**2) / L2(T**2)), "final_margin": float(marg)})
# monotonicity of the final margin for T >= 100: derivative = 0.0894(log(T/2pi)+1) - 0.1881/T > 0
out["c_theoremL1_tails"] = {"rows": rowsc,
    "derivative_of_margin_at_100": float(mp.mpf('0.0894') * (mp.log(100 / (2 * mp.pi)) + 1) - mp.mpf('0.1881') / 100),
    "Lemma_B_constants": {"min (1-cos y)/y^2 on (0,1.1]": float((1 - mp.cos(mp.mpf('1.1'))) / mp.mpf('1.21')),
                           "max (cosh x-1)/x^2 on (0,0.5001]": float((mp.cosh(mp.mpf('0.5001')) - 1) / mp.mpf('0.5001')**2)},
    "corollaries": {"T0^2": float(T0**2), "317^2": 317**2}}

# ---------- (d) THEOREM N1 floor ----------
def F_floor(T, d):
    r1 = mp.mpc(mp.mpf(1) / 2 + d, T); r2 = mp.conj(r1)
    rs = [r1, r2]
    H = mp.matrix(2, 2)
    for j in range(2):
        for k in range(2):
            H[j, k] = 1 / (rs[j] + mp.conj(rs[k]) - 1)
    a = mp.matrix([1 / r for r in rs]); b = mp.matrix([1 / (r - 1) for r in rs])
    Hi = H**-1
    aHa = (a.H * Hi * a)[0]; bHb = (b.H * Hi * b)[0]; bHa = (b.H * Hi * a)[0]
    return mp.re(aHa - abs(bHa)**2 / (1 + bHb))
rowsd = []
for T in [mp.mpf('17.578382'), mp.mpf(100), mp.mpf(1000), mp.mpf(10)**4]:
    for d in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25'), mp.mpf('0.49')]:
        F = F_floor(T, d); ratio = F / (4 * d / T**2)
        rowsd.append({"T": float(T), "delta": float(d), "F": float(F), "F/(4d/T^2)": float(ratio), "(1-ratio)*T^2": float((1 - ratio) * T**2)})
out["d_N1_floor"] = rowsd

# ---------- (e) psi/pi implication horizons ----------
def solve(fun, T):
    g = lambda lx: fun(mp.e**lx) - T
    return mp.e**mp.findroot(g, 58)
buthe = solve(lambda x: mp.mpf('4.92') * mp.sqrt(x / mp.log(x)), T0)
johnston = solve(lambda x: mp.mpf('9.06') / mp.log(mp.log(x)) * mp.sqrt(x / mp.log(x)), T0)
out["e_psi_pi_horizon_T0"] = {"Buthe_4.92": float(buthe), "Johnston_9.06/loglogx": float(johnston),
    "note": "Johnston (arXiv:2109.02249v2, Thm 3.2 and abstract) states 1.101e26 for pi; psi/theta stated to 1.03e26 after iteration."}

# ---------- (f) dBN gap-lattice collapse time ----------
def t_c(T, d):
    s = 4 * mp.pi / mp.log(T / (2 * mp.pi))
    S = lambda y: (mp.pi / (2 * y * s)) * mp.tanh(mp.pi * y / s) - 1 / (y**2 + s**2 / 4)
    return mp.quad(lambda y: 2 * y / (2 + 8 * y**2 * S(y)), [0, 2 * d])
out["f_dBN_tc_T0"] = {str(float(d)): float(t_c(T0, d)) for d in [dmax_MTY, mp.mpf('0.25'), mp.mpf('0.1'), mp.mpf('0.01')]}

# ---------- (g) Nyman-Beurling model scale ----------
beta = 2 + EG - mp.log(4 * mp.pi)
F2 = F_floor(T0, dmax_MTY)
F1 = 2 * dmax_MTY / (abs(mp.mpc(mp.mpf(1) / 2 + dmax_MTY, T0))**2 * (1 + 2 * dmax_MTY / abs(mp.mpc(dmax_MTY - mp.mpf(1) / 2, T0))**2))
out["g_NB_T0"] = {"beta=2+gamma-log4pi": float(beta), "two_zero_floor_F": float(F2), "logN*=beta/F": float(beta / F2),
                  "one_zero_floor_F1": float(F1), "logN*_one_zero=beta/F1": float(beta / F1)}

# ---------- (h) Nicolas ----------
rowsh = {}
for d in [dmax_MTY, mp.mpf('0.25'), mp.mpf('0.1'), mp.mpf('0.01')]:
    rho = mp.mpc(mp.mpf(1) / 2 + d, T0)
    rowsh[str(float(d))] = float(mp.log10(abs(rho * (1 - rho))) / d)
S2tail = (mp.log(T0 / (2 * mp.pi)) + 1) / (2 * mp.pi * T0)
xD3 = ((2 - beta) / (2 * S2tail))**2
out["h_nicolas"] = {"log10_x*_single_defect": rowsh, "D3_sketch_horizon_x": float(xD3)}

out["runtime_s"] = time.time() - t0
p = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/adjudicator/adj_numbers.json"
with open(p, "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("sha256", hashlib.sha256(open(p, "rb").read()).hexdigest())
