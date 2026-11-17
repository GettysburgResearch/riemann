#!/usr/bin/env python3
"""SKEPTIC re-derivation of the T0 table numbers (C1-0, C1-L3 T0 values, C1-E1, C1-J2 T0 values, C1-N1/N2,
C1-D1, C1-D2, C1-D3, C1-D5). Independent implementation (different formulas/solvers where possible).
Numerical class: NUMERICAL-NONRIGOROUS (mpmath 50 digits / scipy)."""
import math, json, time
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
mp.mp.dps = 50
t0 = time.time()
T0 = mp.mpf(3000175332800)
out = {"T0": float(T0), "T0^2": float(T0**2)}
L = mp.log(T0)
for R, name in [(mp.mpf('5.573412'), "MT2015"), (mp.mpf('5.558691'), "MTY2022")]:
    out["delta_max_" + name] = float(mp.mpf(1)/2 - 1/(R*L))
dmax = mp.mpf(1)/2 - 1/(mp.mpf('5.558691')*L)
EG = mp.euler
c = (EG - 1 - mp.log(2*mp.pi))/2
# Li: solve 4 cosh(n a) = n(log n /2 + c) independently via findroot on log form
def li_n(T, d):
    rho = mp.mpc(mp.mpf(1)/2 + d, T); r2 = abs(1 - 1/rho)**2
    a = -mp.log(r2)/2
    f = lambda u: mp.log(4*mp.cosh(mp.exp(u)*a)) - mp.log(mp.exp(u)*(u/2 + c))
    X = 1/a
    u = mp.findroot(f, mp.log(X*mp.log(X)))
    return float(a), float(mp.exp(u)), float(X*mp.log(X)), float(T**2/d*mp.log(T**2/d))
out["Li"] = {str(float(d)): li_n(T0, d) for d in [mp.mpf('0.001'), mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25'), dmax]}
# dBN collapse: integrate dy/dt = -1/y - 4 y S(y) with S as explicit lattice sum (not closed form)
s = float(4*mp.pi/mp.log(T0/(2*mp.pi)))
out["s_H(T0)"] = s
K = np.arange(1, 200001)
def S_sum(y):
    return float(np.sum(1.0/(y*y + ((K + 0.5)*s)**2))) + 1.0/(s*(200000.5))*0  # tail ~ 1/(s^2*200000) negligible
def tc_ode(y0):
    # integrate y^2 =: v; dv/dt = -2 - 8 v S(sqrt v)
    f = lambda t, v: [-2 - 8*v[0]*S_sum(math.sqrt(max(v[0], 0)))]
    ev = lambda t, v: v[0]; ev.terminal = True
    sol = solve_ivp(f, (0, 10), [y0*y0], events=ev, rtol=1e-10, atol=1e-14)
    return float(sol.t_events[0][0])
out["dBN_tc"] = {}
for d in [0.01, 0.1, 0.25, float(dmax)]:
    tc = tc_ode(2*d)
    out["dBN_tc"][str(d)] = {"t_c": tc, "2delta^2": 2*d*d, "4delta/log(T/2pi)": 4*d/float(mp.log(T0/(2*mp.pi))),
                            "Jensen d*=T0^2/(2tc)": float(T0**2)/(2*tc)}
# max over delta in (0, dmax]
tcs = [tc_ode(2*d) for d in np.linspace(0.05, float(dmax), 30)]
out["dBN_max_tc_T0"] = max(tcs)
# NB floor
def nb(T, d):
    r1 = mp.mpc(mp.mpf(1)/2 + d, T); rs = [r1, mp.conj(r1)]
    H = mp.matrix(2, 2)
    for j in range(2):
        for k in range(2):
            # Gram <e_j,e_k> with e_j = t^{conj(rho_j)-1} on (0,1): int t^{conj rho_j + rho_k - 2} dt
            H[j, k] = 1/(mp.conj(rs[j]) + rs[k] - 1)
    v = lambda C: mp.matrix([1/r - C/(r - 1) for r in rs])
    # minimise over complex C numerically: F(C) = v^* G^{-1} v + |C|^2  where G_{jk} = <e_k,e_j>? use generic
    G = H.T  # G[j,k] = <e_k, e_j>
    Gi = G**-1
    a = mp.matrix([1/r for r in rs]); b = mp.matrix([1/(r - 1) for r in rs])
    q = lambda x, y: (x.H*Gi*y)[0]
    F = q(a, a) - abs(q(b, a))**2/(1 + q(b, b))
    single = 2*d/(abs(r1)**2*(1 + 2*d/abs(r1 - 1)**2))
    # brute check of the C-minimisation
    Fbr = min(mp.re((v(mp.mpc(x, y)).H*Gi*v(mp.mpc(x, y)))[0] + x*x + y*y)
              for x in np.linspace(float(mp.re(q(b, a)/(1 + q(b, b))))*0.9, float(mp.re(q(b, a)/(1 + q(b, b))))*1.1 + 1e-30, 41)
              for y in [float(mp.im(q(b, a)/(1 + q(b, b))))])
    return float(mp.re(F)), float(single), float(4*d/T**2), float(Fbr)
out["NB"] = {f"T={T},d={d}": nb(mp.mpf(T), mp.mpf(d)) for T, d in [(17.6, 0.45), (100, 0.5), (1000, 0.1), (1e6, 0.01)]}
beta = 2 + EG - mp.log(4*mp.pi)
out["NB_beta"] = float(beta)
FT0 = nb(T0, dmax)
out["NB_T0"] = {"F": FT0[0], "logN*=beta/F": float(beta)/FT0[0], "beta/single": float(beta)/FT0[1]}
# Buthe implication horizon x with 4.92 sqrt(x/log x) = T
xb = mp.findroot(lambda lx: 4.92*mp.sqrt(mp.exp(lx)/lx) - T0, 58)
out["Buthe_x(T0)"] = float(mp.exp(xb)); out["Buthe_x(2.445e12)"] = float(mp.exp(mp.findroot(lambda lx: 4.92*mp.sqrt(mp.exp(lx)/lx) - 2.445e12, 58)))
# Schoenfeld single defect: 2 x^d/|rho| = log^2 x/(8 pi)
def psi_x(d):
    rho = mp.mpc(mp.mpf(1)/2 + d, T0)
    u = mp.findroot(lambda u: mp.log(2/abs(rho)) + d*u - mp.log(u*u/(8*mp.pi)), 100 if d > 0.2 else 1000/d)
    return float(u/mp.log(10))
out["psi_log10x*"] = {str(float(d)): psi_x(d) for d in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25'), dmax]}
# delta needed at x=1e29
u = 29*mp.log(10)
out["psi_delta_needed_at_1e29"] = float((mp.log(u*u/(8*mp.pi)) - mp.log(2/T0))/u)
# Nicolas single-defect x* = |rho(1-rho)|^{1/delta}; Nicolas worst-case sketch
out["Nicolas_log10x*"] = {str(float(d)): float(mp.log10(abs(mp.mpc(0.5 + d, T0)*mp.mpc(0.5 - d, -T0)))/d) for d in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25'), dmax]}
S2 = (mp.log(T0/(2*mp.pi)) + 1)/(2*mp.pi*T0)   # sum_{gamma>T0} gamma^-2 (main term)
out["Nicolas_worst_x_with_(log+1)"] = float(((2 - beta)/(2*S2))**2)
out["Nicolas_worst_x_report_formula"] = float((1.9*mp.pi*T0/mp.log(T0/(2*mp.pi)))**2)
# c_k: log k* = pi (T - gamma1)/(2 delta)
out["ck_logk*_dmax"] = float(mp.pi*(T0 - mp.mpf('14.134725'))/(2*dmax))
out["ck_T_probed_by_k=1e10(delta=1/2)"] = float(14.134725 + 2*0.5*mp.log(1e10)/mp.pi)
out["runtime_s"] = time.time() - t0
print(json.dumps(out, indent=1))
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_T0_numbers.json", "w"), indent=1)
