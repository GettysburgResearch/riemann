#!/usr/bin/env python3
"""SKEPTIC independent re-implementation of the Jensen-heat bridge prediction (C1-J2/J3) for Farmer's X_j.
Flow F_tau = -(D^2 - D)F, D = z d/dz; zero ODE written in the z-variable: dz_k/dtau = 2 z_k^2 sum_{l!=k} 1/(z_k - z_l)
(the investigator used w = log z with coth kernels and froze/ tail-corrected differently).
Dynamic zeros: all zeros with |z| < Rdyn; static zeros of cos up to index L; analytic tail beyond L.
Prediction d* = 1/(2 tau_c), tau_c = time when the moved pair reaches the real axis.
NUMERICAL-NONRIGOROUS (scipy DOP853)."""
import math, json, time
import numpy as np
from scipy.integrate import solve_ivp
import mpmath as mp
def predict(j, moved_idx, L=4000, Rdyn=120.0):
    c = (np.arange(L) + 0.5)*math.pi
    keep = np.setdiff1d(np.arange(L), moved_idx)
    real = np.r_[c[keep], -c[keep]]
    dynR = real[np.abs(real) < Rdyn]; stat = real[np.abs(real) >= Rdyn]
    zq = np.array([complex(j, 1), complex(j, -1), complex(-j, 1), complex(-j, -1)])
    z0 = np.r_[dynR.astype(complex), zq]
    S2 = float(mp.psi(1, L + 0.5))/math.pi**2; S4 = float(mp.psi(3, L + 0.5)/6)/math.pi**4
    def vel(z):
        Dm = z[:, None] - z[None, :]; np.fill_diagonal(Dm, np.inf)
        s = (1/Dm).sum(1) + (1/(z[:, None] - stat[None, :])).sum(1) - 2*z*S2 - 2*z**3*S4
        return 2*z*z*s
    n = len(z0)
    def rhs(t, y):
        z = y[:n] + 1j*y[n:]
        v = vel(z)
        return np.r_[v.real, v.imag]
    iq = n - 4    # index of j+i
    y0 = 1.0
    ev = lambda t, y: y[n + iq] - 0.02*y0; ev.terminal = True; ev.direction = -1
    sol = solve_ivp(rhs, (0, 1), np.r_[z0.real, z0.imag], method="DOP853", events=ev, rtol=1e-10, atol=1e-13)
    ts = sol.t_events[0][0]; ys = sol.y_events[0][0]
    vy = rhs(ts, ys)[n + iq]; yy = ys[n + iq]
    tau = ts + yy*yy/(-2*yy*vy)      # linear extrapolation in y^2
    # sanity: velocity of cos zeros without moved pair
    zc = np.r_[c[:L][np.abs(c[:L]) < Rdyn], -c[:L][np.abs(c[:L]) < Rdyn]].astype(complex)
    stat_c = np.r_[c[c >= Rdyn], -c[c >= Rdyn]]
    Dm = zc[:, None] - zc[None, :]; np.fill_diagonal(Dm, np.inf)
    vc = 2*zc*zc*((1/Dm).sum(1) + (1/(zc[:, None] - stat_c[None, :])).sum(1) - 2*zc*S2 - 2*zc**3*S4)
    return {"j": j, "moved": [float(c[i]) for i in moved_idx], "tau_c": tau, "d*_pred": 1/(2*tau),
            "sanity_max|v|_cos_zeros(|z|<20)": float(np.abs(vc[np.abs(zc) < 20]).max())}
rows = []
t0 = time.time()
for j, mv, inv, exact in [(10, [2, 3], 119.63, 120), (20, [4, 5], 769.40, 750), (20, [5, 6], 480.72, 478), (40, [12, 13], 1891.9, None)]:
    r = predict(j, mv); r["investigator_pred"] = inv; r["exact_first_nonreal(skeptic-certified)"] = exact
    rows.append(r); print(r, flush=True)
json.dump({"rows": rows, "runtime_s": time.time() - t0}, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_jensen_bridge_ode.json", "w"), indent=1)
