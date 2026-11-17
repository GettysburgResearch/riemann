#!/usr/bin/env python3
"""C1: translate the rigorous verification height T0 (Platt-Trudgian 2021) into minimal indices/scales.
Two kinds of numbers (see REPORT Sec. 1):
  (I)  implication horizons  -- rigorous: RH(T0) => criterion holds up to this index (THEOREM / IMPORTED);
  (II) single-defect detection scales -- model/heuristic: first failure caused by one quadruple at height ~T0.
All arithmetic in mpmath (non-rigorous high precision); formulas are documented in the report.
"""
import sys, math, time
import mpmath as mp
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common
from scipy.integrate import quad

mp.mp.dps = 50
T0 = mp.mpf(common.T0_PLATT_TRUDGIAN)
L0 = mp.log(T0)
ZFR = mp.mpf('5.558691')                       # Mossinghoff-Trudgian 2015 zero-free region constant
dmax = mp.mpf(1) / 2 - 1 / (ZFR * L0)          # largest admissible delta at height T0
deltas = [mp.mpf('1e-6'), mp.mpf('1e-3'), mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25'), dmax]
EG = mp.euler
BETA = 2 + EG - mp.log(4 * mp.pi)

def li_nstar(T, d):
    rho = mp.mpc(mp.mpf(1) / 2 + d, T); z = 1 - 1 / rho
    a = -mp.log(abs(z))
    trend = lambda n: n / 2 * (mp.log(n) - 1 + EG - mp.log(2 * mp.pi))
    f = lambda n: 4 * mp.cosh(n * a) - trend(n)
    X = 1 / a
    lo, hi = X, X
    while f(hi) < 0: hi *= 2
    n = mp.findroot(f, (lo, hi), solver='anderson')
    LX = mp.log(X)
    return a, n, X * (LX + 2 * mp.log(LX) - mp.log(4))

def lattice_tc(y0, s):
    y0, s = float(y0), float(s)
    def S(y):
        return (math.pi / (2 * y * s)) * math.tanh(math.pi * y / s) - 1.0 / (y * y + s * s / 4)
    f = lambda y: 2 * y / (2 + 8 * y * y * S(y)) if y > 1e-9 else y
    return quad(f, 0, y0, limit=200)[0]

def nb_floor(T, d):
    r1 = mp.mpc(mp.mpf(1) / 2 + d, T); rs = [r1, mp.conj(r1)]
    H = mp.matrix(2, 2)
    for j in range(2):
        for k in range(2):
            H[j, k] = 1 / (rs[j] + mp.conj(rs[k]) - 1)
    a = mp.matrix([1 / r for r in rs]); b = mp.matrix([1 / (r - 1) for r in rs])
    Hi = H**-1
    aa = (a.H * Hi * a)[0]; bb = (b.H * Hi * b)[0]; ba = (b.H * Hi * a)[0]
    return mp.re(aa - abs(ba)**2 / (1 + bb))

rows = []
s_H = 4 * mp.pi / mp.log(T0 / (2 * mp.pi))     # mean zero spacing of H_0 at height 2*T0
for d in deltas:
    a, n_li, n_li2 = li_nstar(T0, d)
    tc = lattice_tc(2 * d, s_H)
    F = nb_floor(T0, d)
    rho = mp.mpc(mp.mpf(1) / 2 + d, T0)
    u_nic = mp.log(abs(rho * (1 - rho))) / d
    # Schoenfeld psi: 2 x^d/|rho| = log^2 x/(8 pi)
    g = lambda u: mp.log(2 / abs(rho)) + d * u - mp.log(u * u / (8 * mp.pi))
    u_psi = mp.findroot(g, (mp.mpf(10), 10 * u_nic + 1000), solver='anderson')
    # Mertens: 2 x^d / |rho zeta'| = 0.5, |zeta'(rho0)| in [1e-2, 1e2]
    u_mer = [mp.log(mp.mpf('0.25') * abs(rho) * zp) / d for zp in (mp.mpf('1e-2'), 1, mp.mpf(100))]
    rows.append({"delta": float(d),
                 "Li: a=-log|z|": float(a), "Li: n*(model, amplitude crossing)": float(n_li), "Li: n_2 formula": float(n_li2),
                 "dBN: t_c (gap-lattice model)": tc, "Jensen(even): d* = T0^2/(2 t_c)": float(T0**2 / (2 * tc)),
                 "NB: floor F": float(F), "NB: log N* = beta/F": float(BETA / F),
                 "psi/Schoenfeld: log10 x*": float(u_psi / mp.log(10)),
                 "Nicolas: log10 x* (= log10 log n* for Robin, heuristic)": float(u_nic / mp.log(10)),
                 "Mertens: log10 x* for |zeta'(rho0)| = 1e-2, 1, 1e2": [float(u / mp.log(10)) for u in u_mer]})
    print(rows[-1], flush=True)

# implication horizons
def buthe_x(T):
    h = lambda lx: 4.92 * mp.sqrt(mp.exp(lx) / lx) - T
    return mp.findroot(h, 58)
x_but = buthe_x(T0)
impl = {"T0": float(T0), "delta_max(T0) from zero-free region": float(dmax),
        "Li: n <= T0^2 (Theorem L1)": float(T0**2),
        "Jensen: d <= floor(T0)^2 (Chasse; GORTTW Thm 1.2)": float(mp.floor(T0)**2),
        "psi/theta/pi Schoenfeld bounds: x <= (Buthe Thm 2)": float(mp.exp(x_but)), "log10": float(x_but / mp.log(10)),
        "Nicolas worst-case sketch: x <= (1.9 pi T0/log(T0/2pi))^2": float((1.9 * mp.pi * T0 / mp.log(T0 / (2 * mp.pi)))**2),
        "dBN: max_delta t_c(T0,delta) (model)": max(r["dBN: t_c (gap-lattice model)"] for r in rows),
        "NB: min_delta log N*": min(r["NB: log N* = beta/F"] for r in rows)}
print(impl)
out = {"campaign": "C1-detection-horizons", "experiment": "T0 translation table", "env": common.env(),
       "T0": float(T0), "s_H(T0)": float(s_H), "rows": rows, "implication_horizons": impl}
p = common.save_json("T0_table.json", out)
print("saved", p, common.sha256(p))
