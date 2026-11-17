#!/usr/bin/env python3
"""SKEPTIC independent spot check of C1-E1 ODE collapse times t_c(T,delta) for H_t (zeros of H_0 at z=2*gamma).
Differences from the investigator's code: all zeros 2*gamma_j with |j-k|<=M move; the far zeros (both sides, and the
mirror zeros -2*gamma) are included as a STATIC background through their exact velocity contribution
sum 2/(z - z_l) (not neglected); collapse detected on y^2 (d(y^2)/dt) with event y^2 = 0 via linear extrapolation.
NUMERICAL-NONRIGOROUS (scipy RK45/DOP853)."""
import math, json, time
import numpy as np
from scipy.integrate import solve_ivp
D = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data/"
g = np.array([float(l.split()[1]) for f in ("zeros_1_50000.tsv", "zeros_50001_100000.tsv") for l in open(D + f)])
def tc(T_target, delta, M=300, include_far=True):
    k = max(int(np.searchsorted(g, T_target)) - 1, 0)
    T = 0.5*(g[k] + g[k + 1])
    lo, hi = max(0, k - M), min(len(g), k + 2 + M)
    dyn = 2*np.r_[g[lo:k], g[k + 2:hi]]
    far = 2*np.r_[g[:lo], g[hi:]]
    farall = np.r_[far, -2*g] if include_far else np.array([])
    n = len(dyn)
    def bg(zz):   # static background velocity 2*sum 1/(z - z_l), plus smooth tail beyond gamma_100000 (both signs) ~ 0 by symmetry at leading order
        return 2*np.sum(1.0/(zz[:, None] - farall[None, :]), axis=1) if len(farall) else np.zeros(len(zz), dtype=complex)
    def rhs(t, s):
        x = s[:n]; X, V = s[n], s[n + 1]          # pair X +- i y, V = y^2
        y = math.sqrt(max(V, 1e-30)); zc = complex(X, y)
        Dm = x[:, None] - x[None, :]; np.fill_diagonal(Dm, np.inf)
        vx = 2*np.sum(1/Dm, axis=1) + np.real(2/(x - zc) + 2/(x - np.conj(zc))) + np.real(bg(x.astype(complex)))
        vz = 2*np.sum(1/(zc - x)) + 2/(zc - np.conj(zc)) + bg(np.array([zc]))[0]
        return np.r_[vx, vz.real, 2*y*vz.imag]
    ev = lambda t, s: s[n + 1] - 1e-6*(2*delta)**2; ev.terminal = True; ev.direction = -1
    sol = solve_ivp(rhs, (0, 2), np.r_[dyn, 2*T, (2*delta)**2], method="DOP853", events=ev, rtol=1e-10, atol=1e-13)
    ts = sol.t_events[0][0]; ss = sol.y_events[0][0]
    dV = rhs(ts, ss)[n + 1]
    return T, ts + ss[n + 1]/(-dV)
rows = []
t0 = time.time()
for Tt, d, inv in [(17.6, 0.45, 0.4011), (1000, 0.45, 0.32657), (1000, 0.2, 0.07612), (70000, 0.45, 0.22324)]:
    for far in (False, True):
        T, t = tc(Tt, d, include_far=far)
        rows.append({"T": T, "delta": d, "include_far_static": far, "t_c": t, "investigator": inv})
        print(rows[-1], flush=True)
json.dump({"rows": rows, "runtime_s": time.time() - t0}, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_dbn_ode.json", "w"), indent=1)
