#!/usr/bin/env python3
"""SKEPTIC independent check of C1-L3 (single-defect Li detection index) in the investigator's collision model,
but WITHOUT the trend replacement: lambda_n^RH is the direct sum over all 100000 zeros plus a smooth-density tail
(t > t_s, density log(t/2pi)/2pi), evaluated exactly on a window [n_lo, n_hi] containing the amplitude crossing.
Window: n_lo = first n with 4cosh(na)+8 > 0.85*trend(n) (below it, negativity would need a fluctuation of
>15% of the trend; we also sample the direct-sum fluctuation there). Independent code (complex recurrence z^n).
Numerical class: NUMERICAL-NONRIGOROUS, model-world statement only."""
import math, time, json
import numpy as np, mpmath as mp
from scipy import integrate, optimize
t0 = time.time()
D = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/"
g = np.array([float(l.split()[1]) for f in ("zeros_1_50000.tsv", "zeros_50001_100000.tsv") for l in open(D + f)])
EG = 0.5772156649015329
Nsm = lambda t: t/(2*math.pi)*math.log(t/(2*math.pi*math.e)) + 7/8
t_s = optimize.brentq(lambda t: Nsm(t) - 100000.5, g[-1] - 10, g[-1] + 10)
dens = lambda t: math.log(t/(2*math.pi))/(2*math.pi)
def tail(n):
    # integrate over v = n*phi(t), t = 1/(2 tan(v/(2n))), |dt/dv| = 1/(4 n sin^2(v/(2n)))
    vmax = n*2*math.atan(1/(2*t_s))
    f = lambda v: 2*(1 - math.cos(v))*dens(1/(2*math.tan(v/(2*n))))/(4*n*math.sin(v/(2*n))**2) if v > 0 else n*dens(1e300)*0
    pts = np.linspace(0, vmax, int(vmax/(2*math.pi)) + 2)
    s = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        s += integrate.quad(f, max(lo, 1e-12), hi, limit=200)[0]
    return s
trend = lambda n: 0.5*n*(np.log(n) - 1 + EG - math.log(2*math.pi))
z_all = np.exp(1j*2*np.arctan(1/(2*g)))     # z = e^{i phi}, |z|=1 on the line
def window_scan(T_target, d, investigator_nstar):
    k = max(int(np.searchsorted(g, T_target)) - 1, 0)
    T = 0.5*(g[k] + g[k + 1])
    mp.mp.dps = 30
    rho = mp.mpc(0.5 + d, T); zq = 1 - 1/rho
    a = float(-mp.log(abs(zq))); ph = float(mp.arg(zq))
    # window
    f = lambda n: 4*math.cosh(n*a) + 8 - 0.85*trend(n)
    X = 1/a
    lo = X*0.5
    while f(lo) > 0: lo *= 0.7
    hi = lo
    while f(hi) < 0: hi *= 1.05
    n_lo = int(optimize.brentq(f, lo, hi))
    n_amp = optimize.brentq(lambda n: 4*math.cosh(n*a) - trend(n), n_lo, 10*n_lo)
    n_hi = int(n_amp*1.03 + 4*math.pi*T) + 10
    # tail on coarse grid, interpolate
    grid = np.linspace(n_lo, n_hi, 40)
    tg = np.array([tail(n) for n in grid])
    keep = np.ones(len(g), bool); keep[[k, k + 1]] = False
    zk = z_all[keep]
    w = np.exp(1j*n_lo*2*np.arctan(1/(2*g[keep])))
    first = None; minRHdev = 1e99; maxRHdev = -1e99
    for n in range(n_lo, n_hi + 1):
        lamRH_minus2 = 2*np.sum(1 - w.real) + np.interp(n, grid, tg)   # model sum without the two removed zeros
        lam = lamRH_minus2 + 4*(1 - math.cosh(n*a)*math.cos(n*ph))
        # fluctuation of the full lambda^RH (add back removed zeros) relative to trend
        full = lamRH_minus2 + 2*(1 - math.cos(n*2*math.atan(1/(2*g[k])))) + 2*(1 - math.cos(n*2*math.atan(1/(2*g[k + 1]))))
        dev = full - trend(n); minRHdev = min(minRHdev, dev); maxRHdev = max(maxRHdev, dev)
        if lam < 0:
            first = n; break
        w *= zk
        if (n - n_lo) % 2048 == 0: w /= np.abs(w)
    return {"T": T, "delta": d, "a": a, "n_lo(window)": n_lo, "n_amp": n_amp, "first_negative_direct": first,
            "investigator_n*": investigator_nstar, "diff": (first - investigator_nstar) if first else None,
            "lambdaRH-trend range in window": [minRHdev, maxRHdev], "phase_period_2piT": 2*math.pi*T}
cases = [(17.6, 0.45, 6406), (17.6, 0.2, 16016), (17.6, 0.1, 34578), (50, 0.45, 70361), (50, 0.1, 363780),
         (100, 0.45, 302437), (100, 0.2, 728131), (300, 0.45, 3246393)]
rows = []
for Tt, d, ns in cases:
    t1 = time.time()
    r = window_scan(Tt, d, ns); r["sec"] = round(time.time() - t1, 1)
    rows.append(r); print(r, flush=True)
# fluctuation sample below the windows (direct sum), to support the window choice
samp = {}
for n in [1000, 5000, 20000, 50000, 100000, 200000, 400000, 1000000, 2000000]:
    lam = float(np.sum(2*(1 - np.cos(n*2*np.arctan(1/(2*g)))))) + tail(n)
    samp[n] = {"lambda_model": lam, "minus_trend": lam - float(trend(n))}
print(samp)
out = {"t_s": t_s, "rows": rows, "fluct_sample": samp, "runtime_s": time.time() - t0,
       "versions": {"numpy": np.__version__, "mpmath": mp.__version__}}
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_li_defect.json", "w"), indent=1, default=float)
print("runtime", out["runtime_s"])
