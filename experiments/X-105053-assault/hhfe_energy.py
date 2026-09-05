#!/usr/bin/env python3
"""LANE A4: numerical verification of the HHFE102010 energy decomposition.

Objects (L-102010 / L-103100 / L-103102, branch 103100-fractional-hankel @ 89f9954):
  eta(p^k) = C(2k,k)/4^k ; b_U = mu*1_{>U} ; h_U = b_U * eta
  A_-(y) = 1 on (1,2), -sqrt2 on (2,4); R = log-autocorrelation (L-103100.2)
  U = floor(X^{1/3}), N = floor(X/U)
  H = int_U^{4N} |H_{U,N}|^2 dY/Y = D + O   (Gram identity, checked here)
Outputs results.json with, per X:
  D, O_signed, O_abs (|h||R| version), H_sweep (exact piecewise integral),
  O_hi(P) for P in Plist (signed + abs), prime-prime class (signed + abs),
plus kernel constants (hatA_-(1/2), int R e^{v/2}, int |R| e^{v/2}, w1).
"""
import json, math, os, sys
import numpy as np

H2 = math.log(2.0)
SQ2 = math.sqrt(2.0)

def sieve_mobius(n):
    mu = np.ones(n + 1, dtype=np.int8)
    primes = []
    is_comp = np.zeros(n + 1, dtype=bool)
    spf = np.zeros(n + 1, dtype=np.int64)
    # linear sieve for mobius
    mu = np.zeros(n + 1, dtype=np.int8)
    mu[1] = 1
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i); spf[i] = i; mu[i] = -1
        for p in primes:
            if i * p > n: break
            is_comp[i * p] = True; spf[i * p] = p
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu

def eta_val(e):
    # multiplicative, eta(p^k) = C(2k,k)/4^k
    v = 1.0
    x = e
    d = 2
    while d * d <= x:
        if x % d == 0:
            k = 0
            while x % d == 0:
                x //= d; k += 1
            v *= math.comb(2 * k, k) / 4.0 ** k
        d += 1
    if x > 1:
        v *= 0.5  # k=1: C(2,1)/4 = 1/2
    return v

def R_of_v(v):
    av = np.abs(v)
    out = np.zeros_like(av)
    m1 = av <= H2
    out[m1] = 3 * H2 - (3 + SQ2) * av[m1]
    m2 = (av > H2) & (av < 2 * H2)
    out[m2] = -SQ2 * (2 * H2 - av[m2])
    return out

def build_h(U, N, mu):
    h = np.zeros(N + 1)
    Emax = N // (U + 1)
    for e in range(1, Emax + 1):
        ee = eta_val(e)
        if ee == 0.0: continue
        dmax = N // e
        d = np.arange(U + 1, dmax + 1)
        idx = d * e
        h[idx] += mu[U + 1:dmax + 1] * ee
    return h

def energy_sweep(U, N, h):
    """Exact integral of the piecewise-constant field squared, dY/Y."""
    ns = np.arange(U + 1, N + 1)
    coef = h[U + 1:N + 1] / np.sqrt(ns)
    # events: at Y=n value jumps by +coef, at 2n by -(1+sqrt2)coef, at 4n by +sqrt2 coef
    pts = np.concatenate([ns, 2 * ns, 4 * ns]).astype(np.float64)
    jumps = np.concatenate([coef, -(1 + SQ2) * coef, SQ2 * coef])
    order = np.argsort(pts, kind='stable')
    pts = pts[order]; jumps = jumps[order]
    logs = np.log(pts)
    V = np.cumsum(jumps)
    dlog = np.diff(logs)
    return float(np.sum(V[:-1] ** 2 * dlog))

def pair_sums(U, N, h):
    """O_signed, O_abs over off-diagonal near-collision pairs (both orders)."""
    Os = 0.0; Oa = 0.0
    absh = np.abs(h)
    logn = np.log(np.arange(N + 1, dtype=np.float64), where=np.arange(N+1) > 0,
                  out=np.zeros(N + 1))
    sq = np.zeros(N + 1)
    sq[1:] = 1.0 / np.sqrt(np.arange(1, N + 1, dtype=np.float64))
    for n in range(U + 1, N + 1):
        if h[n] == 0.0 and absh[n] == 0.0:
            continue
        m_hi = min(N, 4 * n - 1)
        if m_hi <= n: continue
        m = np.arange(n + 1, m_hi + 1)
        v = logn[n + 1:m_hi + 1] - logn[n]
        Rv = R_of_v(v)
        w = h[n + 1:m_hi + 1] * sq[n + 1:m_hi + 1] * Rv
        Os += 2.0 * h[n] * sq[n] * float(np.sum(w))
        wa = absh[n + 1:m_hi + 1] * sq[n + 1:m_hi + 1] * np.abs(Rv)
        Oa += 2.0 * absh[n] * sq[n] * float(np.sum(wa))
    return Os, Oa

def gcd_split(U, N, h, Plist):
    """O_hi(P): pairs with coprime skeleton max(a,b) <= P (signed and abs)."""
    out = {}
    Pmax = max(Plist)
    absh = np.abs(h)
    # iterate coprime skeletons b < a <= Pmax, a < 4b
    contrib = {}  # (a) -> accumulate per skeleton then bucket by max(a,b)=a
    res_s = {P: 0.0 for P in Plist}
    res_a = {P: 0.0 for P in Plist}
    for a in range(2, Pmax + 1):
        for b in range(max(1, a // 4 + 1), a):
            if math.gcd(a, b) != 1: continue
            v = math.log(a / b)
            if v >= 2 * H2: continue
            Rv = 3 * H2 - (3 + SQ2) * v if v <= H2 else -SQ2 * (2 * H2 - v)
            qmin = U // b + 1          # qb > U
            qmax = N // a              # qa <= N
            if qmax < qmin: continue
            q = np.arange(qmin, qmax + 1)
            s = float(np.sum(h[q * a] * h[q * b] / q))
            sa = float(np.sum(absh[q * a] * absh[q * b] / q))
            pref = 2.0 * Rv / math.sqrt(a * b)
            prefa = 2.0 * abs(Rv) / math.sqrt(a * b)
            for P in Plist:
                if a <= P:
                    res_s[P] += pref * s
                    res_a[P] += prefa * sa
    return res_s, res_a

def prime_class(U, N, h, mu):
    """prime-prime off-diagonal subsum, signed R and |R|."""
    # primes p in (U,N]: mu[p]=-1 and p prime -> detect via smallest factor; easier: sieve
    isp = np.ones(N + 1, dtype=bool); isp[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if isp[i]: isp[i * i::i] = False
    ps = np.nonzero(isp)[0]
    ps = ps[ps > U]
    lp = np.log(ps.astype(np.float64))
    Os = 0.0; Oa = 0.0
    for i, p in enumerate(ps):
        j_hi = np.searchsorted(ps, 4 * p - 1, side='right')
        pj = ps[i + 1:j_hi]
        if len(pj) == 0: continue
        v = lp[i + 1:j_hi] - lp[i]
        Rv = R_of_v(v)
        inv = 1.0 / np.sqrt(p * pj.astype(np.float64))
        # h(p)h(p') = (-1)(-1) = +1
        Os += 2.0 * float(np.sum(Rv * inv))
        Oa += 2.0 * float(np.sum(np.abs(Rv) * inv))
    return Os, Oa, len(ps)

def kernel_constants():
    # int R(v) e^{v/2} dv and int |R| e^{v/2} dv, exact-ish by fine quadrature
    v = np.linspace(-2 * H2, 2 * H2, 2000001)
    Rv = R_of_v(v)
    w = np.exp(v / 2)
    dv = v[1] - v[0]
    iR = float(np.sum(Rv * w) * dv)
    iRa = float(np.sum(np.abs(Rv) * w) * dv)
    # hatA_-(1/2)
    hA_half = (1 - 2 ** (-0.5)) * (1 - SQ2 * 2 ** (-0.5)) / 0.5
    # w1 = min over gamma in [1,2] of |hatA_-(i gamma)|^2
    g = np.linspace(1, 2, 20001)
    s = 1j * g
    hA = (1 - np.exp(-s * H2)) * (1 - SQ2 * np.exp(-s * H2)) / s
    w1 = float(np.min(np.abs(hA) ** 2))
    return {"int_R_ev2": iR, "int_absR_ev2": iRa, "hatA_minus_at_half": hA_half,
            "w1_min_on_[1,2]": w1, "R0": 3 * H2}

def main():
    # results_ext.json was produced by extending this list with 2e6, 4e6
    # (set HHFE_EXT=1 to reproduce; O^hi fields are computed only for the
    # default list — the ext rows carry the O/D/H aggregates alone).
    Xs = [10**4, 2 * 10**4, 4 * 10**4, 10**5, 2 * 10**5, 4 * 10**5, 10**6]
    if os.environ.get("HHFE_EXT"):
        Xs += [2 * 10**6, 4 * 10**6]
    Plist = [2, 4, 8, 16, 32, 64]
    Nmax = 0
    setups = []
    for X in Xs:
        U = int(round(X ** (1 / 3)))
        while U ** 3 > X: U -= 1
        while (U + 1) ** 3 <= X: U += 1
        N = X // U
        setups.append((X, U, N)); Nmax = max(Nmax, N)
    mu = sieve_mobius(Nmax)
    out = {"kernel": kernel_constants(), "rows": []}
    for (X, U, N) in setups:
        h = build_h(U, N, mu)
        ns = np.arange(U + 1, N + 1)
        D = 3 * H2 * float(np.sum(h[U + 1:] ** 2 / ns))
        Hsw = energy_sweep(U, N, h)
        Os, Oa = pair_sums(U, N, h)
        gs, ga = gcd_split(U, N, h, Plist)
        pps, ppa, npr = prime_class(U, N, h, mu)
        row = {"X": X, "U": U, "N": N, "D": D, "H_sweep": Hsw,
               "O_signed": Os, "O_abs": Oa,
               "gram_check_D_plus_O_minus_H": D + Os - Hsw,
               "O_hi_signed": gs, "O_hi_abs": ga,
               "prime_prime_signed": pps, "prime_prime_abs": ppa,
               "n_primes": npr,
               "sum_abs_h": float(np.sum(np.abs(h))),
               "sum_h2": float(np.sum(h ** 2))}
        out["rows"].append(row)
        print(json.dumps(row), flush=True)
    with open(sys.path[0] + "/results.json", "w") as f:
        json.dump(out, f, indent=1)
    # exponent fits
    lx = np.log([r["X"] for r in out["rows"]])
    for key in ["O_abs", "H_sweep", "D"]:
        vals = np.array([abs(r[key]) for r in out["rows"]])
        if np.all(vals > 0):
            slope = np.polyfit(lx, np.log(vals), 1)[0]
            print(f"empirical exponent d log|{key}| / d log X = {slope:.4f}")
    ossgn = [r["O_signed"] for r in out["rows"]]
    print("O_signed values:", ossgn)

if __name__ == "__main__":
    main()
