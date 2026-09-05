#!/usr/bin/env python3
"""Lane 2 validation:
(1) brute-force margin cross-check (independent direct-Q greedy, core.py style);
(2) H-envelope validation on [1e6, 1e7] against exact prefix sums;
(3) derivative identities (B1),(B2) vs central finite differences;
(4) rigorous global constants: Q>=0 cellwise, rhobar_j, tgbar_j (saved to JSON);
(5) F-identity residual.
"""
import json
import numpy as np
from math import sqrt, log
import common as C

OUT = {}

# ---------- (1) brute force ----------
def brute_margins(x):
    n = np.searchsorted(C.LAT["d"], x, side="right")
    d = C.LAT["d"][:n]; mu = C.LAT["mu"][:n]
    T = (4.0 * np.sqrt(x / d) - 3.0) / np.sqrt(d)
    Q = {2: np.zeros(n), 3: np.zeros(n)}
    for i in range(n):
        Y = x / d[i]
        M = int(np.floor(Y))
        for j in (2, 3):
            if M < j:
                continue
            m = np.arange(j, M + 1, dtype=np.float64)
            g = np.full(len(m), C.CJ[j]); g[0] = C.AJ[j]
            if len(m) > 1:
                g[1] = -C.BJ[j]
            Q[j][i] = float(np.sum(g * np.log(Y / m) / np.sqrt(m)))
    odd = mu == -1; even = ~odd
    D = float(np.sum(T[odd]))
    Te = T[even]; cc = np.cumsum(Te)
    k = int(np.searchsorted(cc, D))
    below = float(cc[k - 1]) if k else 0.0
    tp = (D - below) / float(Te[k])
    res = {}
    for j in (2, 3):
        qe = Q[j][even] / np.sqrt(d[even])
        qo = float(np.sum(Q[j][odd] / np.sqrt(d[odd])))
        res[f"M{j}"] = float(np.sum(qe[:k])) + tp * float(qe[k]) - qo
    iv = 1.0 / np.sqrt(d)
    res["M_sc"] = 0.75 * (float(np.sum(iv[odd]))
                          - (float(np.sum(iv[even][:k])) + tp * float(iv[even][k])))
    return res

print("== (1) brute-force cross-check ==")
OUT["brute"] = {}
for x in (88.0, 1e4, 1.234567e5, 1e6):
    b = brute_margins(x)
    f = C.eval_point(x)
    row = {k: (b[k], f[k], abs(b[k] - f[k])) for k in ("M2", "M3", "M_sc")}
    OUT["brute"][f"{x:.6e}"] = {k: v[2] for k, v in row.items()}
    print(f"x={x:.4e}: " + "  ".join(
        f"{k}: brute={v[0]:.9f} fast={v[1]:.9f} diff={v[2]:.2e}" for k, v in row.items()))

# ---------- (2) envelope validation ----------
print("== (2) H-envelope on [1e6, 1e7] ==")
T1 = 10**7
m = np.arange(0, T1 + 1, dtype=np.float64); m[0] = 1.0
inv = 1.0 / np.sqrt(m); inv[0] = 0.0
lm = np.log(m); lm[0] = 0.0
S7 = np.cumsum(inv); SL7 = np.cumsum(inv * lm)
rng = np.random.default_rng(105040)
Ys = np.exp(rng.uniform(np.log(1e6), np.log(1e7), 4000))
Ys = np.concatenate([Ys, np.arange(1e6, 1e6 + 50), np.arange(1e6, 1e6 + 50) + 0.5])
N = np.floor(Ys).astype(np.int64)
lY = np.log(Ys)
Hex = S7[N] * lY - SL7[N]
E = Hex - (4 * np.sqrt(Ys) + C.Z12 * lY + C.Z12P)
Eb = C.E_envelope(Ys, lY)
viol = np.sum(np.abs(E) > Eb)
print(f"max |E| = {np.max(np.abs(E)):.3e}; envelope bound min={Eb.min():.3e}; "
      f"violations (|E|>bound): {viol}")
OUT["envelope"] = dict(maxE=float(np.max(np.abs(E))), viol=int(viol),
                       ratio_max=float(np.max(np.abs(E) / Eb)))

# ---------- (3) derivative identities ----------
print("== (3) derivative identities vs finite differences ==")
def rho_j(j, x, e):
    Y = x / e
    if Y < C.T0:
        Nn = int(np.floor(Y))
        Q = C.TAB[(j, "a")][Nn] * log(Y) - C.TAB[(j, "b")][Nn]
    else:
        Q = 4 * C.CJ[j] * sqrt(Y) + C.CINF[j] * log(Y) + C.KINF[j]
    return Q / (4 * sqrt(Y) - 3)

def g_j(j, Y):
    if Y < j:
        return -2 * C.CJ[j] * sqrt(Y)
    Nn = int(np.floor(Y))
    if Nn <= C.T0:
        return C.TAB[(j, "a")][Nn] - 2 * C.CJ[j] * sqrt(Y)
    return C.CINF[j] + 0.0  # asymptotic value (error ~1/sqrt(Y))

OUT["deriv"] = {}
for x in (3.777e6, 5.2e8, 7.77e12):
    h = 2e-7
    p1 = C.eval_point(x * (1 - h)); p2 = C.eval_point(x * (1 + h))
    p0 = C.eval_point(x)
    if p1["n_active"] != p2["n_active"]:
        print(f"x={x:.3e}: activation inside FD window, skipping"); continue
    dt = log(1 + h) - log(1 - h)
    fd_sc = (p2["M_sc"] - p1["M_sc"]) / dt
    pred_sc = -1.5 * p0["M_sc"] / (4 * sqrt(x / p0["e_star"]) - 3)
    print(f"x={x:.3e}: dMsc/dt FD={fd_sc:.6f} pred={pred_sc:.6f}")
    row = dict(fd_sc=fd_sc, pred_sc=pred_sc)
    # (B2): R_j sum
    n = np.searchsorted(C.LAT["d"], x, side="right")
    d = C.LAT["d"][:n]; mu = C.LAT["mu"][:n]
    Y = x / d
    gv = {j: np.array([g_j(j, y) for y in Y]) for j in (2, 3)}
    odd = mu == -1; even = ~odd
    iv = 1.0 / np.sqrt(d)
    k = p0["kstar"]; tp = p0["theta_p"]
    for j in (2, 3):
        ge = gv[j][even] * iv[even]
        R = float(np.sum(ge[:k])) + tp * float(ge[k]) - float(np.sum(gv[j][odd] * iv[odd]))
        pred = 2 * p0["M_sc"] * (rho_j(j, x, p0["e_star"]) - C.CJ[j]) + R
        fd = (p2[f"M{j}"] - p1[f"M{j}"]) / dt
        print(f"    dM{j}/dt FD={fd:.6f} pred={pred:.6f} diff={abs(fd-pred):.2e}")
        row[f"fd{j}"] = fd; row[f"pred{j}"] = pred
    OUT["deriv"][f"{x:.3e}"] = row

# ---------- (4) rigorous global constants ----------
print("== (4) Q>=0, rhobar_j, tgbar_j (cellwise exact on [1, T0] + tails) ==")
consts = {}
mm = np.arange(1, C.T0, dtype=np.int64)  # cells [m, m+1), m = 1..T0-1
lml = np.log(mm.astype(np.float64)); lmr = np.log(mm.astype(np.float64) + 1.0)
for j in (2, 3):
    a = C.TAB[(j, "a")][mm]; b = C.TAB[(j, "b")][mm]
    Qmin = a * lml - b     # Q increasing in Y on each cell (a>0 for m>=j)
    Qmax = a * lmr - b
    bad = np.sum(Qmin < -1e-12)
    print(f"j={j}: min cellwise Q left-endpoint = {Qmin.min():.3e} (negatives: {bad})")
    # rho sup on [j, T0): cell bound Qmax/(4 sqrt(m)-3)
    den = 4 * np.sqrt(mm.astype(np.float64)) - 3.0
    rho_cell = np.where(mm >= j, np.maximum(Qmax, 0.0) / den, 0.0)
    im = int(np.argmax(rho_cell))
    # tail Y >= T0: Q <= 4C sqrt(Y) + cinf*lY + kinf + C*Ehi; cinf<0, so
    # Q <= 4C sqrt Y + kinf + C*Ehi(T0) if kinf<0 -> rho <= C*(4 sqrt Y)/(4 sqrt Y - 3)
    Eh = float(C.E_envelope(np.array([C.T0 * 1.0]), np.array([log(C.T0)]))[0])
    assert C.CINF[j] < 0 and C.KINF[j] + C.CJ[j] * Eh < 0
    rho_tail = C.CJ[j] * 4 * sqrt(C.T0) / (4 * sqrt(C.T0) - 3)
    rhobar = max(float(rho_cell[im]), rho_tail)
    print(f"j={j}: rhobar (cell sup {rho_cell[im]:.6f} at m={mm[im]}, tail {rho_tail:.6f})"
          f" -> {rhobar:.6f}")
    consts[f"rhobar{j}"] = rhobar
    consts[f"Qneg{j}"] = int(bad)
    # tgbar on (0, Ycut]: sup |g_j - cinf|; g = a[m] - 2C sqrt(Y) on [m, m+1), monotone
    Ycut = 100
    mc = np.arange(0, Ycut, dtype=np.int64)
    ac = np.where(mc >= 1, C.TAB[(j, "a")][np.maximum(mc, 1)], 0.0)
    gl = ac - 2 * C.CJ[j] * np.sqrt(mc.astype(np.float64))          # left end
    gr = ac - 2 * C.CJ[j] * np.sqrt(mc.astype(np.float64) + 1.0)    # right end
    tg = np.maximum(np.abs(gl - C.CINF[j]), np.abs(gr - C.CINF[j])).max()
    # also must dominate the r-bound at Ycut so gammabar can switch there
    rY = 1.0 / sqrt(Ycut - 1) + 0.25 * (Ycut - 1) ** -1.5
    consts[f"tgbar{j}"] = float(max(tg, C.CJ[j] * rY))
    consts["Ycut"] = Ycut
    print(f"j={j}: tgbar (Y<= {Ycut}) = {consts[f'tgbar{j}']:.6f}")

# verify g_j - cinf bound C_j*(1/sqrt(N)+...) on [Ycut, T0] cellwise
for j in (2, 3):
    sel = mm >= consts["Ycut"]
    a = C.TAB[(j, "a")][mm[sel]].astype(np.float64)
    mf = mm[sel].astype(np.float64)
    dev_l = np.abs(a - 2 * C.CJ[j] * np.sqrt(mf) - C.CINF[j])
    dev_r = np.abs(a - 2 * C.CJ[j] * np.sqrt(mf + 1.0) - C.CINF[j])
    bound = C.CJ[j] * (1.0 / np.sqrt(mf) + 0.25 * mf ** -1.5)
    # NOTE bound uses N = m = floor(Y); Ylo-1 < N form used in certify is weaker
    okl = np.all(dev_l <= bound); okr = np.all(dev_r <= bound)
    print(f"j={j}: |g-cinf| <= C_j(1/sqrt(N)+N^-1.5/4) on [{consts['Ycut']},T0): "
          f"left {okl} right {okr} maxratio="
          f"{max((dev_l/bound).max(), (dev_r/bound).max()):.4f}")
    consts[f"gdev_ok{j}"] = bool(okl and okr)

# ---------- (5) F-identity residual ----------
print("== (5) F-identity ==")
for x in (1e6, 1e10, 1e15, 1e20, 5e23):
    p = C.eval_point(x)
    n = np.searchsorted(C.LAT["d"], x, side="right")
    d = C.LAT["d"][:n]; mu = C.LAT["mu"][:n]
    odd = mu == -1; even = ~odd
    invd = 1.0 / d
    k = p["kstar"]; tp = p["theta_p"]
    ie = invd[even]
    F = float(np.sum(ie[:k])) + tp * float(ie[k]) - float(np.sum(invd[odd]))
    resid = F + p["M_sc"] / sqrt(x)
    print(f"x={x:.1e}: F={F:.3e}  F + Msc/sqrt(x) = {resid:.3e}")
    OUT.setdefault("Fident", {})[f"{x:.1e}"] = resid

OUT["consts"] = consts
with open("validate_out.json", "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("saved validate_out.json")
