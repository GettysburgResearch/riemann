"""
joint_moment.py -- EMPIRICAL 'joint moment' test for the sextic row family
psi_u(n) = chi_n(u) of the OpenAI QRH manuscript (eqs. (4.1)-(4.2), Prop. 8.3).

Status: EMPIRICAL (floating point, complex64 matrix products). Finite ranges only;
says nothing about asymptotics.

Objects (central normalisation, smooth bump W(y) = exp(4 - 1/((y-1)(2-y))) on (1,2)):
  M_u(t) = D^{-1/2}  sum_{n sf, (n,6)=1}  mu(n) chi_n(u) W(N n / D) N(n)^{-it}   (inverse polynomial)
  S_u(t) = L^{-1/2}  sum_{l,     (l,6)=1}        chi_l(u) W(N l / L) N(l)^{-it}   (plain polynomial)
Rows: all elements u (unit factor included) with U <= N(u) < 2U and (u, 6) = 1; for 2U < 7^6
these are automatically sixth-power free.  Prop. 8.3 attaches to a row ONE common twist height
for both polynomials; here t_u := argmax_{|t| <= T} |M_u(t) S_u(t)| on a grid.

Statistics (means over rows):
  joint_max   = E_u max_t |M_u(t) S_u(t)|^2              (rowwise-maximised common twist)
  marg_max    = E_u max_t |M_u|^2  *  E_u max_t |S_u|^2   (separately maximised marginals)
  marg_typ    = E_{u,t} |M_u(t)|^2 * E_{u,t} |S_u(t)|^2   (typical-twist marginals)
  joint_0     = E_u |M_u(0) S_u(0)|^2 vs  E|M_u(0)|^2 E|S_u(0)|^2
  corr_max    = Pearson correlation over rows of (max_t |M_u|^2, max_t |S_u|^2)
The same statistics are computed for two NULL models with the same supports and weights:
  null_iid:  every chi_n(u), chi_l(u) replaced by an independent uniform sixth root of unity;
  null_mult: chi_p(u) replaced by an independent uniform sixth root of unity for each (u, p)
             (zeros kept), extended multiplicatively -- so M_u and S_u share prime values the
             way the true characters do (relevant when the supports of n and l overlap).
They calibrate how much of any ratio is caused by maximisation and shared primes alone.

Run:  python3 -I joint_moment.py results/joint_moment.json 500 1000 2000 4000 8000
"""

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eisenstein as E  # noqa: E402
from check_kintali_phase import ideals_upto  # noqa: E402


def bump(y):
    out = np.zeros_like(y, dtype=np.float64)
    m = (y > 1) & (y < 2)
    out[m] = np.exp(4 - 1 / ((y[m] - 1) * (2 - y[m])))
    return out


def rows_window(U):
    A, B = E.nonzero_lattice(2 * U - 1)
    N = A * A - A * B + B * B
    keep = (N >= U) & (N % 3 != 0) & (N % 2 == 1)
    return A[keep], B[keep], N[keep]


def code_matrix(primes, ua, ub, plist):
    """codes[p_index][u] for the primes in plist (uint8, ZERO = 32)."""
    return {i: primes[i].codes(ua, ub) for i in plist}


def values_for(fac_list, codes, nrows):
    """Matrix [rows, cols] of chi_c(u), c given by {prime index: exponent}."""
    V = np.zeros((nrows, len(fac_list)), dtype=np.complex64)
    zeta = np.exp(1j * np.pi * np.arange(6) / 3).astype(np.complex64)
    for j, fac in enumerate(fac_list):
        tot = np.zeros(nrows, dtype=np.int64)
        zero = np.zeros(nrows, dtype=bool)
        for i, e in fac.items():
            c = codes[i].astype(np.int64)
            zero |= c == E.ZERO
            tot += e * c
        col = zeta[tot % 6]
        col[zero] = 0
        V[:, j] = col
    return V


def stats(Mt, St):
    """Mt, St: [rows, T] complex arrays."""
    aM = np.abs(Mt) ** 2
    aS = np.abs(St) ** 2
    aMS = aM * aS
    t0 = Mt.shape[1] // 2
    maxM = aM.max(1)
    maxS = aS.max(1)
    maxMS = aMS.max(1)
    joint_max = maxMS.mean()
    marg_max = maxM.mean() * maxS.mean()
    marg_typ = aM.mean() * aS.mean()
    joint0 = aMS[:, t0].mean()
    marg0 = aM[:, t0].mean() * aS[:, t0].mean()
    corr = float(np.corrcoef(maxM, maxS)[0, 1])
    return dict(E_maxM2=float(maxM.mean()), E_maxS2=float(maxS.mean()),
                E_M2_typ=float(aM.mean()), E_S2_typ=float(aS.mean()),
                joint_max=float(joint_max), marg_max=float(marg_max), marg_typ=float(marg_typ),
                ratio_joint_max_over_marg_max=float(joint_max / marg_max),
                ratio_joint_max_over_marg_typ=float(joint_max / marg_typ),
                ratio_rowwise_prod_of_maxima=float((maxM * maxS).mean() / marg_max),
                joint0=float(joint0), marg0=float(marg0), ratio0=float(joint0 / marg0),
                corr_max=corr, max_row_maxMS=float(maxMS.max()))


def run(D, L, U, T, dt, primes, rng):
    t_grid = np.arange(-T, T + dt / 2, dt)
    ua, ub, uN = rows_window(U)
    X = max(2 * D, 2 * L)
    ids = ideals_upto(primes, X)
    ncols = [(f, n) for g, n, f in ids if D < n < 2 * D and all(e == 1 for e in f.values())]
    lcols = [(f, n) for g, n, f in ids if L < n < 2 * L]
    need = sorted({i for f, _ in ncols + lcols for i in f})
    codes = code_matrix(primes, ua, ub, need)
    nrows = len(ua)
    VM = values_for([f for f, _ in ncols], codes, nrows)
    VS = values_for([f for f, _ in lcols], codes, nrows)
    nN = np.array([n for _, n in ncols], dtype=np.float64)
    lN = np.array([n for _, n in lcols], dtype=np.float64)
    mu = np.array([(-1) ** len(f) for f, _ in ncols], dtype=np.float64)
    cM = (mu * bump(nN / D) / math.sqrt(D))
    cS = (bump(lN / L) / math.sqrt(L))
    TwM = (cM[:, None] * np.exp(-1j * np.log(nN)[:, None] * t_grid[None, :])).astype(np.complex64)
    TwS = (cS[:, None] * np.exp(-1j * np.log(lN)[:, None] * t_grid[None, :])).astype(np.complex64)
    Mt = VM @ TwM
    St = VS @ TwS
    real = stats(Mt, St)
    # null model: iid uniform sixth roots of unity on the same supports
    zeta = np.exp(1j * np.pi * np.arange(6) / 3).astype(np.complex64)
    RM = zeta[rng.integers(0, 6, VM.shape)] * (VM != 0)
    RS = zeta[rng.integers(0, 6, VS.shape)] * (VS != 0)
    null = stats(RM @ TwM, RS @ TwS)
    # random multiplicative null: chi_p(u) -> iid uniform sixth root per (u, p), extended
    # multiplicatively (zeros kept), so M_u and S_u share prime values exactly as chi does
    rcodes = {i: np.where(c == E.ZERO, E.ZERO, rng.integers(0, 6, c.shape)).astype(np.uint8)
              for i, c in codes.items()}
    mult = stats(values_for([f for f, _ in ncols], rcodes, nrows) @ TwM,
                 values_for([f for f, _ in lcols], rcodes, nrows) @ TwS)
    # row types: u = unit * v^2 (cubic-type character) or unit * v^3 (quadratic-type)
    return dict(D=D, L=L, U=U, T=T, dt=dt, rows=nrows, cols_M=len(ncols), cols_S=len(lcols),
                real=real, null_iid=null, null_multiplicative=mult)


def main():
    out_path = sys.argv[1]
    Ds = [int(x) for x in sys.argv[2:]] or [500, 1000, 2000, 4000]
    T, dt = 25.0, 0.04
    rng = np.random.default_rng(7)
    t0 = time.time()
    primes = E.prime_ideals(2 * max(Ds) + 10)
    results = []
    configs = [(D, D, D) for D in Ds] + [(max(Ds), max(Ds) // 4, max(Ds))]
    for D, L, U in configs:
        t1 = time.time()
        r = run(D, L, U, T, dt, primes, rng)
        r["seconds"] = time.time() - t1
        results.append(r)
        re, nu, mu_ = r["real"], r["null_iid"], r["null_multiplicative"]
        print(f"D={D} L={L} U={U}: rows={r['rows']} |n|={r['cols_M']} |l|={r['cols_S']} "
              f"({r['seconds']:.1f}s)", flush=True)
        for name, s in (("sextic   ", re), ("null_iid ", nu), ("null_mult", mu_)):
            print(f"   {name}: E max|M|^2={s['E_maxM2']:.3f} E max|S|^2={s['E_maxS2']:.3f} "
                  f"E|M|^2={s['E_M2_typ']:.3f} E|S|^2={s['E_S2_typ']:.3f} | "
                  f"joint_max/marg_max={s['ratio_joint_max_over_marg_max']:.3f} "
                  f"joint_max/marg_typ={s['ratio_joint_max_over_marg_typ']:.2f} "
                  f"rowprod/marg_max={s['ratio_rowwise_prod_of_maxima']:.3f} "
                  f"t=0 ratio={s['ratio0']:.3f} corr={s['corr_max']:.3f}", flush=True)
    out = dict(label="EMPIRICAL", T=T, dt=dt, weight="exp(4-1/((y-1)(2-y))) on (1,2)",
               results=results, runtime_s=time.time() - t0)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"done in {out['runtime_s']:.1f} s -> {out_path}")


if __name__ == "__main__":
    main()
