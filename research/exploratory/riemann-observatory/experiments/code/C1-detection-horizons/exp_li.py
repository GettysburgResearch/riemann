#!/usr/bin/env python3
"""C1 / family (a): Keiper-Li coefficients -- detection index of an injected off-line quadruple.

Model zero set Z_model: the first 100000 zeta zeros (Arb-certified ordinates, all on the line)
plus a smooth Riemann-von Mangoldt density (1/2pi)log(t/2pi) for t > t_s, where N_smooth(t_s)=100000.5.

lambda_n(model) = sum_{gamma>0} 2(1-cos(n phi_gamma)),  phi_gamma = arg(1-1/rho) = 2 arctan(1/(2 gamma)).

Injection ("collision model"): two consecutive on-line zeros gamma_k, gamma_{k+1} are removed and the
quadruple {rho0, conj(rho0), 1-rho0, 1-conj(rho0)}, rho0 = 1/2+delta+iT, T = (gamma_k+gamma_{k+1})/2, is added.
With z = 1-1/rho0 = r e^{i phi} (r<1) the quadruple contributes exactly Q_n = 4[1 - cosh(n a) cos(n phi)],
a = -log r  (since 1-1/(1-conj rho0) = (1/r) e^{i phi}).

lambda_n^mod = lambda_n^RH - 2(1-cos n phi_k) - 2(1-cos n phi_{k+1}) + Q_n.
For n <= NDIR, lambda_n^RH is the direct model sum; for n > NDIR it is the RH trend
(n/2)(log n - 1 + gamma_E - log 2 pi) + c_off, with c_off the mean offset fitted on [NDIR/2, NDIR]
("trend model"; the O(sqrt(n) log n) fluctuation is dropped -- recorded in the output).
n* = first n with lambda_n^mod < 0 (found by exhaustive scan where it can occur; final sign re-checked in mpmath).
Numerical class: NUMERICAL-NONRIGOROUS (float64 sums + mpmath spot checks), model-world statement only.
"""
import sys, time, json, math
import numpy as np
import mpmath as mp
from scipy import integrate, optimize
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common

t_start = time.time()
g, rad = common.load_zeros()
phi_all = 2.0 * np.arctan(1.0 / (2.0 * g))
# tail start t_s with N_smooth(t_s) = 100000.5
t_s = optimize.brentq(lambda t: common.N_smooth(t) - 100000.5, g[-1] - 10, g[-1] + 10)

def tail(n):
    f = lambda u: 2.0 * (1.0 - math.cos(n * 2.0 * math.atan(u / 2.0))) * math.log(1.0 / (u * 2 * math.pi)) / (2 * math.pi) / u**2
    val, err = integrate.quad(f, 0.0, 1.0 / t_s, limit=400)   # u = 1/t
    return val

def lam_model(nvals, chunk=400):
    out = np.empty(len(nvals))
    for i in range(0, len(nvals), chunk):
        nn = np.asarray(nvals[i:i + chunk], dtype=float)[:, None]
        out[i:i + chunk] = (2.0 * (1.0 - np.cos(nn * phi_all[None, :]))).sum(1)
    return out + np.array([tail(n) for n in nvals])

def trend(n):
    n = np.asarray(n, dtype=float)
    return 0.5 * n * (np.log(n) - 1.0 + common.EULER_GAMMA - math.log(2 * math.pi))

# ---------- Part 1: validation ----------
mp.mp.dps = 40
xi = lambda s: s * (s - 1) / 2 * mp.pi**(-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
coef = mp.taylor(lambda x: mp.log(xi(1 / (1 - x))), 0, 6, singular=True)
lam_exact_small = {n: float(coef[n] * n) for n in range(1, 7)}
JOHANSSON_L1e5 = 100000 * 4.62580782406902231409416038   # Johansson 2015 (Keiper normalisation x n)
val_n = [1, 2, 3, 4, 5, 6, 1000, 10000, 50000, 100000]
lam_val = lam_model(val_n)
validation = {str(n): {"model": float(l), "reference": (lam_exact_small.get(n) if n <= 6 else (JOHANSSON_L1e5 if n == 100000 else None)),
                       "trend": float(trend(n))} for n, l in zip(val_n, lam_val)}
print("validation", json.dumps(validation, indent=0), flush=True)

NDIR = 20000
nn = np.arange(1, NDIR + 1)
lam_dir = lam_model(nn)
fl = lam_dir - trend(nn)
c_off = float(fl[NDIR // 2:].mean())
fluct = {"mean_offset_[NDIR/2,NDIR]": c_off, "max_abs_dev_from_trend+off_[1000,NDIR]": float(np.abs(fl[999:] - c_off).max()),
         "min_lambda_model": float(lam_dir.min()), "argmin": int(nn[lam_dir.argmin()])}
print("fluct", fluct, flush=True)

def lam_RH(n):
    n = np.asarray(n, dtype=np.int64)
    out = trend(n) + c_off
    m = n <= NDIR
    out[m] = lam_dir[n[m] - 1]
    return out

# ---------- Part 2: detection grid ----------
def quad_params(T, d):
    rho = mp.mpc(0.5 + d, T)
    z = 1 - 1 / rho
    return float(-mp.log(abs(z))), float(mp.arg(z))

def lam_mod(n, T, d, a, phi, pa, pb):
    n = np.asarray(n, dtype=np.int64); nf = n.astype(float)
    return (lam_RH(n) - 2 * (1 - np.cos(nf * pa)) - 2 * (1 - np.cos(nf * pb))
            + 4 * (1 - np.cosh(nf * a) * np.cos(nf * phi)))

def lam_mod_mp(n, T, d, k):
    """mpmath recheck (trend-model / direct value for lambda^RH, exact quadruple & removed terms)."""
    mp.mp.dps = 30
    rho = mp.mpc(0.5 + d, T); z = 1 - 1 / rho
    r = abs(z); ph = mp.arg(z); a = -mp.log(r)
    pa = 2 * mp.atan(1 / (2 * mp.mpf(g[k]))); pb = 2 * mp.atan(1 / (2 * mp.mpf(g[k + 1])))
    base = mp.mpf(float(lam_RH(np.array([n]))[0]))
    return base - 2 * (1 - mp.cos(n * pa)) - 2 * (1 - mp.cos(n * pb)) + 4 * (1 - mp.cosh(n * a) * mp.cos(n * ph))

def first_failure(T, d, k):
    a, phi = quad_params(T, d)
    pa, pb = phi_all[k], phi_all[k + 1]
    # (i) direct range
    lm = lam_mod(nn, T, d, a, phi, pa, pb)
    neg = np.nonzero(lm < 0)[0]
    if len(neg):
        return int(nn[neg[0]]), a, phi
    # (ii) beyond NDIR: lambda^mod >= trend+c_off - 8 + 4 - 4cosh(na); skip n where this is > 0
    h = lambda n: trend(n) + c_off - 4 - 4 * math.cosh(n * a)
    lo = NDIR
    if h(lo) > 0:
        hi = lo
        while h(hi) > 0:
            hi *= 2
        lo = int(optimize.brentq(h, hi / 2, hi)) - 2  # last n where necessary condition fails ~ lo
        lo = max(lo, NDIR + 1)
    n = lo
    step = 2_000_000
    while True:
        blk = np.arange(n, n + step, dtype=np.int64)
        lm = lam_mod(blk, T, d, a, phi, pa, pb)
        neg = np.nonzero(lm < 0)[0]
        if len(neg):
            return int(blk[neg[0]]), a, phi
        n += step

def predictions(T, d, a):
    X = 1.0 / a
    f = lambda n: 4 * math.cosh(n * a) - (trend(n) + c_off)
    hi = X
    while f(hi) < 0:
        hi *= 1.5
    n_amp = optimize.brentq(f, X * 0.5 if f(X * 0.5) < 0 else 1.0, hi)
    LX = math.log(X)
    return {"X=1/a": X, "T^2/delta": T * T / d, "n_amp": n_amp, "n_lead=(T^2/d)log(T^2/d)": T * T / d * math.log(T * T / d),
            "n_2=X(logX+2loglogX-log4)": X * (LX + 2 * math.log(LX) - math.log(4))}

targets = [17.6, 50, 100, 300, 1000, 3000, 10000, 30000, 70000]
deltas = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3, 0.45]
rows = []
for Tt in targets:
    k = int(np.searchsorted(g, Tt)) - 1
    k = max(k, 0)
    T = 0.5 * (g[k] + g[k + 1])
    for d in deltas:
        t1 = time.time()
        nstar, a, phi = first_failure(T, d, k)
        chk = (float(lam_mod_mp(nstar, T, d, k)), float(lam_mod_mp(nstar - 1, T, d, k)) if nstar > 1 else None)
        pr = predictions(T, d, a)
        row = {"T": T, "k": k + 1, "delta": d, "a": a, "phi": phi, "n_star": nstar, "mp_check(n*, n*-1)": chk,
               "regime": "direct" if nstar <= NDIR else "trend-model", **pr,
               "n*/n_amp": nstar / pr["n_amp"], "n*/n_lead": nstar / pr["n_lead=(T^2/d)log(T^2/d)"],
               "n*/n_2": nstar / pr["n_2=X(logX+2loglogX-log4)"], "sec": round(time.time() - t1, 2)}
        rows.append(row)
        print(f"T={T:.3f} d={d} n*={nstar} n_amp={pr['n_amp']:.4g} n*/n_amp={row['n*/n_amp']:.4f} n*/n_lead={row['n*/n_lead']:.3f} n*/n_2={row['n*/n_2']:.3f} chk={chk}", flush=True)

out = {"campaign": "C1-detection-horizons", "experiment": "Li coefficients detection index (model)",
       "env": common.env(), "zeros": "first 100000 (Arb balls, max radius %.3g)" % rad, "t_s": t_s, "NDIR": NDIR,
       "validation": validation, "fluctuation": fluct, "rows": rows, "runtime_s": time.time() - t_start}
p = common.save_json("li_detection.json", out)
print("saved", p, common.sha256(p), "runtime", out["runtime_s"])
