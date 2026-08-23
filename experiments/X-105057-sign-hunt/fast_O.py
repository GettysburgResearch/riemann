#!/usr/bin/env python3
"""Lane S: fast exact evaluation of the HHFE off-diagonal O(X) via band separation.

O = sum_{U<m!=n<=N, 1/4<m/n<4} h_U(m)h_U(n)(mn)^{-1/2} R(log(m/n)),
R piecewise linear => O separates into prefix sums: O(N) time after h build.
Exact rearrangement of the deposited pair sum (hhfe_energy.py pair_sums).
Also D = 3log2 * sum h^2/n and (optional) exact sweep H for Gram check.
"""
import json, math, sys, time
import numpy as np

H2 = math.log(2.0)
SQ2 = math.sqrt(2.0)


def mobius_np(n):
    isp = np.ones(n + 1, dtype=bool)
    isp[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = False
    primes = np.nonzero(isp)[0]
    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    lim = int(n ** 0.5)
    for p in primes:
        mu[p::p] *= -1
        if p <= lim:
            pp = p * p
            mu[pp::pp] = 0
    return mu


def eta_val(e):
    v = 1.0
    x = e
    d = 2
    while d * d <= x:
        if x % d == 0:
            k = 0
            while x % d == 0:
                x //= d
                k += 1
            v *= math.comb(2 * k, k) / 4.0 ** k
        d += 1
    if x > 1:
        v *= 0.5
    return v


def build_h(U, N, mu):
    h = np.zeros(N + 1)
    Emax = N // (U + 1)
    for e in range(1, Emax + 1):
        ee = eta_val(e)
        if ee == 0.0:
            continue
        dmax = N // e
        h[(U + 1) * e:(dmax * e) + 1:e] += mu[U + 1:dmax + 1] * ee
    return h


def band_O_D(U, N, h):
    """Exact O and D via prefix sums. Returns (O, D)."""
    n = np.arange(U + 1, N + 1, dtype=np.float64)
    hn = h[U + 1:N + 1]
    D = 3 * H2 * float(np.sum(hn * hn / n))
    c = hn / np.sqrt(n)
    ln = np.log(n)
    d = c * ln
    # prefix arrays over full index 0..N (index j holds sum_{U<i<=j})
    # use offsets: for query x in [U+1..N], C(x) = cum[x-U-1]; C(x<=U)=0
    cumC = np.cumsum(c)
    cumD = np.cumsum(d)

    def pref(cum, idx):
        # idx: integer array of query points (values <= N); returns sum_{U<j<=idx}
        r = np.zeros(len(idx))
        m = idx > U
        r[m] = cum[idx[m] - (U + 1)]
        return r

    O = 0.0
    ni = np.arange(U + 1, N + 1, dtype=np.int64)
    CH = 1 << 20
    for lo in range(0, len(ni), CH):
        sl = slice(lo, min(lo + CH, len(ni)))
        nn = ni[sl]
        m2 = np.minimum(2 * nn, N)
        m4 = np.minimum(4 * nn - 1, N)
        Cn = pref(cumC, nn)
        C2 = pref(cumC, m2)
        C4 = pref(cumC, m4)
        Dn = pref(cumD, nn)
        D2 = pref(cumD, m2)
        D4 = pref(cumD, m4)
        lnn = ln[sl]
        cc = c[sl]
        t = ((3 * H2 + (3 + SQ2) * lnn) * (C2 - Cn) - (3 + SQ2) * (D2 - Dn)
             + (-2 * SQ2 * H2 - SQ2 * lnn) * (C4 - C2) + SQ2 * (D4 - D2))
        O += 2.0 * float(np.dot(cc, t))
    return O, D


def energy_sweep(U, N, h):
    ns = np.arange(U + 1, N + 1)
    coef = h[U + 1:N + 1] / np.sqrt(ns)
    pts = np.concatenate([ns, 2 * ns, 4 * ns]).astype(np.float64)
    jumps = np.concatenate([coef, -(1 + SQ2) * coef, SQ2 * coef])
    order = np.argsort(pts, kind='stable')
    pts = pts[order]
    jumps = jumps[order]
    logs = np.log(pts)
    V = np.cumsum(jumps)
    dlog = np.diff(logs)
    return float(np.sum(V[:-1] ** 2 * dlog))


def UN_for(X, theta=None):
    if theta is None:
        U = int(round(X ** (1 / 3)))
        while U ** 3 > X:
            U -= 1
        while (U + 1) ** 3 <= X:
            U += 1
    else:
        U = int(X ** theta)
        while (U + 1) <= X ** theta:
            U += 1
        while U > X ** theta:
            U -= 1
        U = max(U, 1)
    N = X // U
    return U, N


def run_grid(Xs, theta=None, mu=None, do_sweep=False, tag=""):
    rows = []
    Nmax = max(UN_for(X, theta)[1] for X in Xs)
    if mu is None or len(mu) <= Nmax:
        t0 = time.time()
        mu = mobius_np(Nmax)
        print(f"# sieve to {Nmax}: {time.time()-t0:.1f}s", flush=True)
    for X in Xs:
        U, N = UN_for(X, theta)
        if N <= U + 1:
            continue
        t0 = time.time()
        h = build_h(U, N, mu)
        O, D = band_O_D(U, N, h)
        row = {"X": X, "U": U, "N": N, "O": O, "D": D, "H": D + O,
               "theta": theta, "t": round(time.time() - t0, 2)}
        if do_sweep:
            row["H_sweep"] = energy_sweep(U, N, h)
            row["gram_err"] = row["H_sweep"] - (D + O)
        rows.append(row)
        print(json.dumps(row), flush=True)
    return rows, mu


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    out = {"mode": mode, "rows": []}
    if mode == "validate":
        Xs = [10**4, 2*10**4, 4*10**4, 10**5, 2*10**5, 4*10**5, 10**6, 2*10**6, 4*10**6]
        rows, _ = run_grid(Xs, do_sweep=True)
        out["rows"] = rows
        ref = {10000: -2.1756786323180446, 20000: -2.1170763149806198}
        with open("/home/user/riemann/experiments/X-105053-assault/results.json") as f:
            dep = json.load(f)
        for r in rows:
            for dr in dep["rows"]:
                if dr["X"] == r["X"]:
                    r["dep_O"] = dr["O_signed"]
                    r["diff_vs_dep"] = r["O"] - dr["O_signed"]
                    print(f"X={r['X']}: band O={r['O']:.12f} dep={dr['O_signed']:.12f} diff={r['diff_vs_dep']:.2e}", flush=True)
    fn = f"/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneS/out_{mode}.json"
    with open(fn, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", fn)
