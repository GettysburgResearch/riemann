#!/usr/bin/env python3
"""C1 / families (b) Jensen polynomials and (e) de Bruijn-Newman heat flow.

Part A (dBN): zero dynamics of H_t = exp(-t d^2/dz^2) H_0 (Polymath15 normalisation, zeros of H_0 at z=2*gamma).
  Model: real zeros 2*gamma_j (first 100000 Arb-certified ordinates) in a window of +-M around the
  injected pair; gamma_k, gamma_{k+1} removed and replaced by the conjugate pair 2T +- 2i delta.
  ODE: dz_j/dt = 2 sum_{l != j} 1/(z_j - z_l) (Csordas-Smith-Varga / Polymath15 Prop. 3.1 type dynamics),
  far zeros outside the window neglected. Output: collapse time t_c(T,delta) when Im of the pair -> 0.
  Compared with: isolated pair 2 delta^2; gap-lattice analytic model (formula in report); Polymath15 heuristic ~ 1/log T.
Part B (Jensen <-> heat bridge, validation on Farmer 2020, Table 4.1):
  Heuristic: the (classical) degree-d Jensen polynomial multiplies the k-th Taylor coefficient by
  prod_{i<k}(1-i/d) ~ exp(-(k^2-k)/(2d)), i.e. applies exp(-tau (D^2 - D)), D = d/dw, w = log z, tau = 1/(2d).
  Zero ODE in w (exact for the flow exp(-tau(D^2-D)) of a genus-0/symmetric product):
      dw_k/dtau = sum_{l != k} [coth((w_k - w_l)/2) + 1].
  Predicted threshold d* = 1/(2 tau_c) where tau_c = time at which the nonreal pair reaches the real line.
  Farmer's X_j: cos(z) with the two zeros closest to j (and their negatives) moved to +-j +- i.
Part C: same bridge for the even Jensen polynomials of the Xi-model (variable x = t^2, w = log x = 2 log t),
  predicted d*_ev(T,delta) = 1/(2 tau_c); also the local estimate T^2/(2 t_c^{dBN}).
Numerical class: NUMERICAL-NONRIGOROUS (scipy DOP853), heuristic model; Part B compares with published exact data.
"""
import sys, time, math, json
import numpy as np
from scipy.integrate import solve_ivp, quad
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import common

T_START = time.time()
g, rad = common.load_zeros()

def collapse(real0, pair0, kernel, y_stop_frac=0.02, t_max=10.0):
    """Generic zero ODE with real zeros 'real0' (array, real) and one conjugate pair pair0 (upper member).
    kernel(zk, zl) returns the pair-interaction velocity contribution of zero zl on zk (vectorised).
    Returns collapse time (Im of pair -> 0), extrapolated linearly in y^2 from y = y_stop_frac*y0."""
    nr = len(real0)
    y0 = pair0.imag
    def rhs(t, s):
        x = s[:nr]; zc = s[nr] + 1j * s[nr + 1]
        allz = np.concatenate([x.astype(complex), [zc, np.conj(zc)]])
        # velocities of real zeros
        D = x[:, None] - x[None, :]
        np.fill_diagonal(D, np.inf)
        vr = kernel(x[:, None].astype(complex), x[None, :].astype(complex), D).real.sum(1)
        vr += (kernel(x.astype(complex), zc, None) + kernel(x.astype(complex), np.conj(zc), None)).real
        vz = kernel(zc, x.astype(complex), None).sum() + kernel(zc, np.conj(zc), None)
        return np.concatenate([vr, [vz.real, vz.imag]])
    ev = lambda t, s: s[nr + 1] - y_stop_frac * y0
    ev.terminal = True; ev.direction = -1
    s0 = np.concatenate([real0, [pair0.real, pair0.imag]])
    sol = solve_ivp(rhs, (0, t_max), s0, method='DOP853', events=ev, rtol=1e-9, atol=1e-12)
    if sol.status != 1:
        return float('nan'), sol
    ts = sol.t_events[0][0]; ss = sol.y_events[0][0]
    dy = rhs(ts, ss)[nr + 1]; y = ss[nr + 1]
    return ts + y * y / (-2 * y * dy), sol

# ---------------- Part A: dBN in H-coordinates ----------------
def kernel_lin(zk, zl, D):
    if D is not None:
        return 2.0 / D
    return 2.0 / (zk - zl)

def lattice_tc(y0, s):
    """Gap-lattice analytic model: pair at x=0 +- i y, static real neighbours at +-(k+1/2)s, k>=1.
    d(y^2)/dt = -2 - 8 y^2 S(y), S(y) = sum_{k>=1} 1/(y^2+(k+1/2)^2 s^2) = (pi/(2 y s)) tanh(pi y/s) - 1/(y^2+s^2/4)."""
    def S(y):
        if y < 1e-12:
            return sum(1.0 / ((k + 0.5)**2 * s * s) for k in range(1, 200000))
        return (math.pi / (2 * y * s)) * math.tanh(math.pi * y / s) - 1.0 / (y * y + s * s / 4)
    f = lambda y: 2 * y / (2 + 8 * y * y * S(y))   # dt = d(y^2)/(2+8y^2S) = 2y dy/(...)
    return quad(f, 0, y0, limit=200)[0]

def dbn_case(T_target, delta, M=300):
    k = max(int(np.searchsorted(g, T_target)) - 1, M + 1)
    T = 0.5 * (g[k] + g[k + 1])
    idx = np.r_[k - M:k, k + 2:min(k + 2 + M, len(g))]
    real0 = 2.0 * g[idx]
    pair0 = complex(2 * T, 2 * delta)
    tc, sol = collapse(real0, pair0, kernel_lin)
    s_mean = 4 * math.pi / math.log(T / (2 * math.pi))
    return {"T": T, "k": k + 1, "delta": delta, "t_c_ode": tc, "t_iso=2delta^2": 2 * delta**2,
            "t_lattice_model": lattice_tc(2 * delta, s_mean), "4delta/log(T/2pi)": 4 * delta / math.log(T / (2 * math.pi)),
            "local_spacing_H": s_mean, "gap_actual_H": 2 * (g[k + 2] - g[k - 1]) / 3.0}

rowsA = []
for Tt in [17.6, 50, 100, 300, 1000, 3000, 10000, 30000, 70000]:
    for d in [0.01, 0.05, 0.1, 0.2, 0.3, 0.45]:
        if Tt < 200:
            # low zeros: use all zeros up to k+M (window starts at first zero)
            k = max(int(np.searchsorted(g, Tt)) - 1, 0)
            T = 0.5 * (g[k] + g[k + 1])
            idx = np.r_[0:k, k + 2:k + 2 + 300]
            tc, _ = collapse(2.0 * g[idx], complex(2 * T, 2 * d), kernel_lin)
            s_mean = 4 * math.pi / math.log(max(T, 7.0) / (2 * math.pi))
            r = {"T": T, "k": k + 1, "delta": d, "t_c_ode": tc, "t_iso=2delta^2": 2 * d * d,
                 "t_lattice_model": lattice_tc(2 * d, s_mean), "4delta/log(T/2pi)": 4 * d / math.log(T / (2 * math.pi)),
                 "local_spacing_H": s_mean, "gap_actual_H": None}
        else:
            r = dbn_case(Tt, d)
        r["jensen_ev_d*_local=T^2/(2tc)"] = r["T"]**2 / (2 * r["t_c_ode"])
        rowsA.append(r)
        print("A", {k_: (round(v, 6) if isinstance(v, float) else v) for k_, v in r.items()}, flush=True)

# window-size sensitivity check at one point
sens = []
for M in [100, 200, 400]:
    r = dbn_case(10000, 0.2, M=M); sens.append({"M": M, "t_c": r["t_c_ode"]})
print("sensitivity", sens, flush=True)

# ---------------- Part B: Farmer's X_j, classical Jensen, w = log z ----------------
def kernel_w(wk, wl, D):
    if D is not None:
        # D = wk - wl for real-line zeros stored as complex w (we pass complex arrays)
        return 1.0 / np.tanh(D / 2.0) + 1.0
    return 1.0 / np.tanh((wk - wl) / 2.0) + 1.0

def collapse_w(wreal_pos, wreal_neg, wpair, y_stop_frac=0.02):
    """Zeros on Im w = 0 (positive real z), Im w = pi (negative real z), and one conjugate pair (upper member wpair).
    State: real parts of the line zeros (imag parts fixed by symmetry), pair (re, im)."""
    a, b = len(wreal_pos), len(wreal_neg)
    y0 = wpair.imag
    def rhs(t, s):
        wp = s[:a].astype(complex); wn = s[a:a + b] + 1j * math.pi; wc = s[a + b] + 1j * s[a + b + 1]
        allw = np.concatenate([wp, wn, [wc, np.conj(wc)]])
        n = len(allw)
        Dm = allw[:, None] - allw[None, :]
        np.fill_diagonal(Dm, 1.0)
        K = 1.0 / np.tanh(Dm / 2.0) + 1.0
        np.fill_diagonal(K, 0.0)
        v = K.sum(1)
        return np.concatenate([v[:a].real, v[a:a + b].real, [v[a + b].real, v[a + b].imag]])
    ev = lambda t, s: s[a + b + 1] - y_stop_frac * y0
    ev.terminal = True; ev.direction = -1
    s0 = np.concatenate([wreal_pos, wreal_neg, [wpair.real, wpair.imag]])
    sol = solve_ivp(rhs, (0, 5.0), s0, method='DOP853', events=ev, rtol=1e-9, atol=1e-13)
    ts = sol.t_events[0][0]; ss = sol.y_events[0][0]
    dy = rhs(ts, ss)[a + b + 1]; y = ss[a + b + 1]
    return ts + y * y / (-2 * y * dy)

def farmer_case(j, Mz=400):
    c = (np.arange(Mz) + 0.5) * math.pi
    order = np.argsort(np.abs(c - j))
    moved = sorted(order[:2])
    keep = np.setdiff1d(np.arange(Mz), moved)
    wpos = np.log(c[keep]); wneg = np.log(c[keep])      # negative zeros: log|z| + i pi
    wpair = complex(math.log(abs(complex(j, 1))), math.atan2(1, j))
    # mirror pair -j +- i is at log|.| + i(pi - atan(1/j)): include as additional fixed-symmetry pair? It lies
    # at distance ~ pi - 2/j in Im from the upper pair; we include it by symmetry: it mirrors the pair, so we
    # approximate its effect by adding it as two more "complex" zeros moving consistently (same real part).
    tau = collapse_w_full(wpos, wneg, wpair, tail2=cos_tail2(Mz))
    return {"j": j, "moved_zeros": [float(c[m]) for m in moved], "tau_c": tau, "d*_pred=1/(2tau_c)": 1 / (2 * tau)}

def collapse_w_full(wpos, wneg, wpair, y_stop_frac=0.02, tail2=0.0):
    """Even function: zeros come in +- pairs. Upper pair member wc = log(j+i); its partners: conj (log(j-i)),
    and the mirrored ones -j+-i -> log|.| + i(pi -+ atan(1/j)). Re parts of all four coincide by symmetry,
    Im parts are +-y and pi -+ y."""
    a, b = len(wpos), len(wneg)
    y0 = wpair.imag
    Rdyn = 0.3 * math.exp(max(wpos.max(), wneg.max()))
    dynp = np.exp(wpos) <= Rdyn; dynn = np.exp(wneg) <= Rdyn
    def rhs(t, s):
        wp = s[:a].astype(complex); wn = s[a:a + b] + 1j * math.pi
        X, Y = s[a + b], s[a + b + 1]
        quadw = np.array([X + 1j * Y, X - 1j * Y, X + 1j * (math.pi - Y), X + 1j * (math.pi + Y)])
        allw = np.concatenate([wp, wn, quadw])
        Dm = allw[:, None] - allw[None, :]
        np.fill_diagonal(Dm, 1.0)
        K = 1.0 / np.tanh(Dm / 2.0) + 1.0
        np.fill_diagonal(K, 0.0)
        v = K.sum(1) - 4.0 * np.exp(2 * allw) * tail2   # omitted symmetric pairs +-c_l, l >= L: -4 z^2 sum 1/c_l^2
        v[:a][~dynp] = 0.0; v[a:a + b][~dynn] = 0.0     # outer zeros frozen (they are stationary for cos; avoids edge stiffness)
        return np.concatenate([v[:a].real, v[a:a + b].real, [v[a + b].real, v[a + b].imag]])
    ev = lambda t, s: s[a + b + 1] - y_stop_frac * y0
    ev.terminal = True; ev.direction = -1
    s0 = np.concatenate([wpos, wneg, [wpair.real, wpair.imag]])
    sol = solve_ivp(rhs, (0, 5.0), s0, method='DOP853', events=ev, rtol=1e-9, atol=1e-13)
    ts = sol.t_events[0][0]; ss = sol.y_events[0][0]
    dy = rhs(ts, ss)[a + b + 1]; y = ss[a + b + 1]
    return ts + y * y / (-2 * y * dy)

import mpmath as _mp
def cos_tail2(L):
    """sum_{l>=L} 1/c_l^2, c_l=(l+1/2)pi  = psi'(L+1/2)/pi^2"""
    return float(_mp.psi(1, L + 0.5)) / math.pi**2

# sanity check: for cos itself the first-order velocities must vanish at the zeros
c = (np.arange(400) + 0.5) * math.pi
allw = np.concatenate([np.log(c).astype(complex), np.log(c) + 1j * math.pi])
Dm = allw[:, None] - allw[None, :]; np.fill_diagonal(Dm, 1.0)
K = 1.0 / np.tanh(Dm / 2.0) + 1.0; np.fill_diagonal(K, 0.0)
v = K.sum(1) - 4.0 * np.exp(2 * allw) * cos_tail2(400)
sanity = {"max|v| over first 20 positive cos zeros (should be ~0, truncation 400 zeros)": float(np.abs(v[:20]).max()),
          "v[0..4]": [complex(x).real for x in v[:5]]}
print("sanity", sanity, flush=True)

FARMER = {10: 118, 20: 749, 40: 1897, 60: 4242}   # Farmer 2020 Table 4.1: J^{d,0}_{X_j,cl} real-rooted iff d <= value
rowsB = []
for j, dmax in FARMER.items():
    r = farmer_case(j)
    r["farmer_d_max_real"] = dmax
    r["farmer_first_nonreal_d"] = dmax + 1
    r["ratio_pred/farmer"] = r["d*_pred=1/(2tau_c)"] / (dmax + 1)
    rowsB.append(r)
    print("B", r, flush=True)

# ---------------- Part C: even Jensen polynomials of the Xi-model ----------------
def xi_even_case(T_target, delta, M=300):
    k = max(int(np.searchsorted(g, T_target)) - 1, 0)
    T = 0.5 * (g[k] + g[k + 1])
    lo = max(0, k - M)
    idx = np.r_[lo:k, k + 2:min(k + 2 + M, len(g))]
    w = 2 * np.log(g[idx])
    Md = 100
    dynC = (idx >= k - Md) & (idx <= k + 1 + Md)
    wpair = 2 * np.log(complex(T, delta))   # = 2log|T+i delta| + 2i atan(delta/T)
    a = len(w)
    y0 = wpair.imag
    w_in = 2 * np.log(g[:lo])                       # static inner zeros (exact kernel)
    hi = min(k + 2 + M, len(g))
    S1 = float(np.sum(1.0 / g[hi:]**2)); S2 = float(np.sum(1.0 / g[hi:]**4))
    ts_ = g[-1]
    S1 += quad(lambda t: common.dens(t) / t**2, ts_, np.inf)[0]; S2 += quad(lambda t: common.dens(t) / t**4, ts_, np.inf)[0]
    def rhs(t, s):
        X, Y = s[a], s[a + 1]
        allw = np.concatenate([s[:a].astype(complex), [X + 1j * Y, X - 1j * Y]])
        Dm = allw[:, None] - allw[None, :]; np.fill_diagonal(Dm, 1.0)
        K = 1.0 / np.tanh(Dm / 2.0) + 1.0; np.fill_diagonal(K, 0.0)
        v = K.sum(1)
        if lo > 0:
            v = v + (1.0 / np.tanh((allw[:, None] - w_in[None, :]) / 2.0) + 1.0).sum(1)
        ex = np.exp(allw)
        v = v - 2.0 * ex * S1 - 2.0 * ex**2 * S2      # omitted outer zeros: coth+1 = -2q-2q^2-..., q = x/gamma^2
        v[:a][~dynC] = 0.0
        return np.concatenate([v[:a].real, [v[a].real, v[a].imag]])
    ev = lambda t, s: s[a + 1] - 0.02 * y0
    ev.terminal = True; ev.direction = -1
    sol = solve_ivp(rhs, (0, 1.0), np.concatenate([w, [wpair.real, wpair.imag]]), method='DOP853', events=ev, rtol=1e-9, atol=1e-15)
    ts = sol.t_events[0][0]; ss = sol.y_events[0][0]
    dy = rhs(ts, ss)[a + 1]; y = ss[a + 1]
    tau = ts + y * y / (-2 * y * dy)
    return {"T": T, "delta": delta, "tau_c_w": tau, "d*_ev_pred=1/(2tau)": 1 / (2 * tau)}

rowsC = []
for Tt in [17.6, 50, 100, 300, 1000, 3000]:
    for d in [0.05, 0.1, 0.2, 0.45]:
        r = xi_even_case(Tt, d)
        # match with Part A local estimate
        rA = [x for x in rowsA if abs(x["T"] - r["T"]) < 1e-6 and x["delta"] == d]
        if rA:
            r["d*_local=T^2/(2 t_c^dBN)"] = rA[0]["jensen_ev_d*_local=T^2/(2tc)"]
        rowsC.append(r)
        print("C", r, flush=True)

out = {"campaign": "C1-detection-horizons", "experiment": "dBN collapse times and Jensen-heat bridge",
       "env": common.env(), "partA_dBN": rowsA, "window_sensitivity": sens, "sanity_cos": sanity,
       "partB_farmer": rowsB, "partC_xi_even_jensen": rowsC, "runtime_s": time.time() - T_START}
p = common.save_json("dbn_jensen.json", out)
print("saved", p, common.sha256(p), "runtime", out["runtime_s"])
