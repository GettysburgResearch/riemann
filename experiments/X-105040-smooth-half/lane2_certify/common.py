#!/usr/bin/env python3
"""Lane 2 (T-105040): frozen 61-smooth margin evaluator with rigorous error bars.

Margins per L-105031(f)/core.py conventions:
  M_j(x)  = sum_e theta*(e) Q_{x/e}(j)/sqrt(e) - sum_o Q_{x/o}(j)/sqrt(o),  j=2,3
  M_sc(x) = (3/4)[ sum_o 1/sqrt(o) - sum_e theta*(e)/sqrt(e) ]
computed via the conditioning identity (NOTES §1):
  M_j = -4 C_j M_sc + sum_e theta* q_j(x/e)/sqrt(e) - sum_o q_j(x/o)/sqrt(o),
  q_j(Y) = Q_Y(j) - 4 C_j sqrt(Y).
Exact regime Y < T0 = 1e6 via prefix arrays; expansion regime Y >= T0 with the
rigorous envelope of NOTES §5. All error sources charged into eps fields.
"""
import numpy as np
from math import sqrt, log

EPS = np.finfo(np.float64).eps
T0 = 10**6
Z12 = -1.46035450880958681288949915252   # zeta(1/2), 30 dps (mpmath)
Z12P = -3.92264613920915172747153144671  # zeta'(1/2)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
P61 = 117288381359406970983270
XSAT = 5 * P61

CJ = {2: 1.0, 3: 1.0 / 3.0}
AJ = {2: 3.0, 3: 2.0}
BJ = {2: 0.0, 3: 2.0 / 3.0}


def build_lattice():
    """All 2^18 squarefree divisors of P61, sorted; float64 values, mu, weights."""
    d = np.ones(1, dtype=np.float64)
    mu = np.ones(1, dtype=np.int8)
    for p in PRIMES:
        d = np.concatenate([d, d * p])
        mu = np.concatenate([mu, -mu])
    order = np.argsort(d, kind="stable")
    d = d[order]
    mu = mu[order]
    sq = np.sqrt(d)
    ld = np.log(d)
    lat = dict(d=d, mu=mu, sq=sq, ld=ld, invsq=1.0 / sq, inv=1.0 / d,
               is_odd=(mu == -1), is_even=(mu == 1))
    # index prefix sums for jump budgets: odd 1/sqrt(d) cumulative
    w = np.where(lat["is_odd"], lat["invsq"], 0.0)
    lat["odd_invsq_cum"] = np.concatenate([[0.0], np.cumsum(w)])
    winv = np.where(lat["is_odd"], lat["inv"], 0.0)
    lat["odd_inv_cum"] = np.concatenate([[0.0], np.cumsum(winv)])
    return lat


def build_prefix(t0=T0):
    """Prefix arrays: a_j[N], b_j[N] (Q_Y(j) = a_j[N] log Y - b_j[N], N=floor(Y)<=t0);
    also S(N), SL(N) for H. Index 0 unused. Rounding budget returned."""
    m = np.arange(0, t0 + 1, dtype=np.float64)
    m[0] = 1.0
    invsq = 1.0 / np.sqrt(m)
    lm = np.log(m)
    tab = {}
    for j in (2, 3):
        g = np.full(t0 + 1, CJ[j])
        g[:j] = 0.0
        g[j] = AJ[j]
        if j + 1 <= t0:
            g[j + 1] = -BJ[j]
        tab[(j, "a")] = np.cumsum(g * invsq)
        tab[(j, "b")] = np.cumsum(g * invsq * lm)
    tab["S"] = np.cumsum(invsq) - 1.0 + 1.0  # index 0 fudge: m[0]=1 counted once
    # fix: element 0 should be 0
    s = invsq.copy(); s[0] = 0.0
    tab["S"] = np.cumsum(s)
    sl = invsq * lm; sl[0] = 0.0
    tab["SL"] = np.cumsum(sl)
    for j in (2, 3):
        tab[(j, "a")][0] = 0.0
        tab[(j, "b")][0] = 0.0
    # sequential-cumsum rounding budget, per exact-regime divisor:
    # err(a[N]) <= t0*EPS*a[t0]; err(q) <= err(a)*max lY + err(b), lY <= log t0.
    per_div = 0.0
    for j in (2, 3):
        per_div = max(per_div,
                      t0 * EPS * float(tab[(j, "a")][-1]) * log(t0)
                      + t0 * EPS * float(np.max(np.abs(tab[(j, "b")]))))
    tab["table_err_per_div"] = per_div  # multiply by sum of 1/sqrt(d) over exact divisors
    return tab


LAT = build_lattice()
TAB = build_prefix()


def q_exact(j, Y, lY):
    """q_j on exact regime (vector): Y < T0. q_j(Y)=a[N] lY - b[N] - 4 C_j sqrt(Y);
    for Y < j this equals -4C_j sqrt(Y) automatically (a=b=0)."""
    N = np.floor(Y).astype(np.int64)
    a = TAB[(j, "a")][N]
    b = TAB[(j, "b")][N]
    return a * lY - b - 4.0 * CJ[j] * np.sqrt(Y)


# closed-form constants for expansion regime
def cj_inf(j):
    S3 = TAB["S"][j + 1]
    return AJ[j] / sqrt(j) - BJ[j] / sqrt(j + 1) + CJ[j] * (Z12 - S3)


def kj_inf(j):
    SL3 = TAB["SL"][j + 1]
    return (-AJ[j] * log(j) / sqrt(j) + BJ[j] * log(j + 1) / sqrt(j + 1)
            + CJ[j] * (Z12P + SL3))


CINF = {j: cj_inf(j) for j in (2, 3)}
KINF = {j: kj_inf(j) for j in (2, 3)}


def E_envelope(Y, lY):
    """Rigorous |E(Y)| bound arrays for Y >= T0 (NOTES §5): returns half-width
    bound max(|Elo|,|Ehi|)."""
    ym1 = Y - 1.0
    inv12 = 1.0 / np.sqrt(ym1)
    inv32 = inv12 / ym1
    ehi = inv32 + (0.5 * inv12 + 0.25 * inv32) * lY
    elo = inv32 + np.log(ym1) * inv12
    return np.maximum(ehi, elo)


def q_expansion(j, lY):
    """q_j closed form (midpoint, E=0) on Y >= T0."""
    return CINF[j] * lY + KINF[j]


def eval_point(x, strict=False):
    """Evaluate margins at real x with rigorous error bars.
    strict=True: active set d < x (left limit at activation points).
    Returns dict."""
    lx = log(x)
    n = np.searchsorted(LAT["d"], x, side=("left" if strict else "right"))
    d = LAT["d"][:n]; sq = LAT["sq"][:n]; ld = LAT["ld"][:n]
    invsq = LAT["invsq"][:n]
    is_odd = LAT["is_odd"][:n]; is_even = ~is_odd
    Y = x / d
    lY = lx - ld
    sqY = np.sqrt(Y)
    T = (4.0 * sqY - 3.0) * invsq

    # ---- greedy fill ----
    To = T[is_odd]
    D = float(np.sum(To))
    Te = T[is_even]
    e_invsq = invsq[is_even]
    cc = np.cumsum(Te)
    Ctot = float(cc[-1])
    assert Ctot >= D, f"TB<0 at x={x:.6e}?! (contradicts proved TB_s>=1.676)"
    kstar = int(np.searchsorted(cc, D, side="left"))
    # theta: full below kstar, partial at kstar
    below = float(cc[kstar - 1]) if kstar > 0 else 0.0
    theta_p = (D - below) / float(Te[kstar])
    theta_p = min(max(theta_p, 0.0), 1.0)
    e_star = float(d[is_even][kstar])

    # rounding budgets on D and cumsum (pairwise numpy sums; charge generously)
    epsD = 64.0 * EPS * (abs(D) + Ctot)

    # ---- M_sc ----
    So_invsq = float(np.sum(invsq[is_odd]))
    Se_used = float(np.sum(e_invsq[:kstar])) + theta_p * float(e_invsq[kstar])
    M_sc = 0.75 * (So_invsq - Se_used)
    # error: fill placement of epsD mass moves Se_used by <= epsD * max(1/(T sqrt e))
    # over marginal evens = epsD / (4 sqrt(x/e)-3) <= epsD (since >=1); plus sum rounding
    eps_sc = 0.75 * (epsD + 64.0 * EPS * (So_invsq + float(np.sum(e_invsq))))

    # ---- q_j arrays: exact vs expansion split ----
    exact = Y < T0
    res = dict(x=x, D=D, kstar=kstar, e_star=e_star, theta_p=theta_p,
               M_sc=M_sc, eps_sc=eps_sc, n_active=n)
    idx_ex = np.nonzero(exact)[0]
    idx_xp = np.nonzero(~exact)[0]
    Ee = E_envelope(Y[idx_xp], lY[idx_xp]) if len(idx_xp) else np.zeros(0)
    for j in (2, 3):
        q = np.empty(n)
        if len(idx_ex):
            q[idx_ex] = q_exact(j, Y[idx_ex], lY[idx_ex])
        if len(idx_xp):
            q[idx_xp] = q_expansion(j, lY[idx_xp])
        qw = q * invsq
        qo = float(np.sum(qw[is_odd]))
        qe_arr = qw[is_even]
        qe = float(np.sum(qe_arr[:kstar])) + theta_p * float(qe_arr[kstar])
        Mj = -4.0 * CJ[j] * M_sc + qe - qo
        # errors:
        env = CJ[j] * float(np.sum(Ee / sq[idx_xp])) if len(idx_xp) else 0.0
        # summation rounding: charge on PRE-cancellation magnitudes (|a lY|+|b|+4C sqrt Y
        # <= 3*max(|Q|,4C sqrt Y) <= ~1.2e5 in exact regime; expansion regime |qw| small)
        big = 4.0 * CJ[j] * np.sqrt(Y[idx_ex]) if len(idx_ex) else np.zeros(0)
        rnd = 64.0 * EPS * (float(np.sum(np.abs(qw)))
                            + (3.0 * float(np.sum(big / sq[idx_ex])) if len(idx_ex) else 0.0))
        # prefix-table cumsum error, weighted by exact-regime 1/sqrt(d) mass
        tbl = TAB["table_err_per_div"] * (float(np.sum(1.0 / sq[idx_ex])) if len(idx_ex) else 0.0)
        # demand-equality slack (identity error) + fill placement (rhobar ~<= 1.2/0.45)
        rb = {2: 1.25, 3: 0.50}[j]  # safe rhobar overestimates; verified in validate.py
        slack = CJ[j] * epsD + epsD * rb + 4.0 * CJ[j] * eps_sc
        res[f"M{j}"] = Mj
        res[f"eps{j}"] = env + rnd + slack + tbl
    return res


def eval_grid(xs, strict=False, progress=None):
    out = []
    for i, x in enumerate(xs):
        out.append(eval_point(float(x), strict=strict))
        if progress and (i + 1) % progress == 0:
            print(f"  ...{i+1}/{len(xs)}", flush=True)
    return out


if __name__ == "__main__":
    r = eval_point(1e6)
    print({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()})
    print("c_inf:", CINF, "k_inf:", KINF)
