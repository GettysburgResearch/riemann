#!/usr/bin/env python3
"""Signed dual quantity versus its positivity bound for the Oct 5 sextic Moebius family.

Status: EMPIRICAL (floating point, finite).  Not certified, not directed rounding.

For K = Q(omega), O = Z[omega], S = {2, lambda}, nu = 1, W the bump of moments/common.py on (1,2),
Phi(x) = exp(-pi x) (row weight), H = D^rho:

  A_u(D)  = sum_{n sqfree, (n,6)=1} mu(n) chi_n(u) W(Nn/D),   chi_n(u) = (u/n)_6
  M_D     = (1/D) sum_{u != 0} Phi(Nu/H) |A_u(D)|^2
  Z       = (H/D) Phihat(0) sum*_g |W(Ng/D)|^2 prod_{p|g}(1 - 1/Np),  Phihat(0) = 2/sqrt(3)
  S       = M_D - Z            (the exact signed dual sum_xi c_xi S_xi of Oct 5 prop:poisson-reduction)
  Diag    = (1/D) sum_n |W|^2 sum_{u != 0} Phi(Nu/H) 1_{(u,n)=1}  (exact primal diagonal)
  Off     = M_D - Diag
  P       = sum*_n 2^{omega(n)} (Nn/D) |W(Nn/D)|^2   (main term of the diagonal of the positivity
            bound of eq:weighted, i.e. mu(f) -> |mu(f)|; derivation in README section 1.3)
  Prin    = (1/D) sum_{u = eps v^6} Phi(Nu/H) |A_u|^2   (sixth-power rows)

Usage: python3 -I signed_dual_numerics.py OUT.json D1 D2 ... --rho 0.6 0.75 0.9
Single-threaded numpy.
"""
import json
import math
import sys
import time

import numpy as np


def W(y):
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m = (y > 1) & (y < 2)
    out[m] = np.exp(4.0 - 1.0 / ((y[m] - 1) * (2 - y[m])))
    return out


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


def powmod_vec(x, e, q):
    x = x.astype(np.int64) % q
    r = np.ones_like(x)
    while e:
        if e & 1:
            r = (r * x) % q
        x = (x * x) % q
        e >>= 1
    return r


def f2_mul(a, b, c, d, p):
    # (a + b w)(c + d w), w^2 = -1 - w
    return (a * c - b * d) % p, (a * d + b * c - b * d) % p


def f2_pow_vec(a, b, e, p):
    ra = np.ones_like(a)
    rb = np.zeros_like(b)
    while e:
        if e & 1:
            ra, rb = f2_mul(ra, rb, a, b, p)
        a, b = f2_mul(a, b, a, b, p)
        e >>= 1
    return ra, rb


def prime_ideals(maxnorm):
    """List of (norm, kind, data): split (q, r) with omega -> r mod q; inert p (norm p^2)."""
    out = []
    for q in primes_upto(maxnorm):
        q = int(q)
        if q % 3 == 1:
            # roots of x^2 + x + 1 mod q
            rr = [x for x in range(2, q) if (x * x + x + 1) % q == 0] if q < 200 else None
            if rr is None:
                # find via a cube root of unity: g^((q-1)/3)
                for g in range(2, q):
                    t = pow(g, (q - 1) // 3, q)
                    if t != 1:
                        rr = [t, (t * t) % q]
                        break
            for r in rr:
                out.append((q, "s", r))
        elif q % 3 == 2 and q >= 5 and q * q <= maxnorm:
            out.append((q * q, "i", q))
    out.sort(key=lambda t: t[0])
    return out


ZERO = 64


def exponent_table(pi):
    """Return function mapping (a,b) arrays to exponent e with (u/pi)_6 = zeta6^e, ZERO if pi | u."""
    norm, kind, dat = pi
    if kind == "s":
        q, r = norm, dat
        x = np.arange(q, dtype=np.int64)
        y = powmod_vec(x, (q - 1) // 6, q)
        t = (-(r * r)) % q  # image of zeta6 = -omega^2
        lut = {}
        v = 1
        for k in range(6):
            lut[v] = k
            v = (v * t) % q
        tab = np.full(q, ZERO, dtype=np.int16)
        for val, k in lut.items():
            tab[(y == val) & (x != 0)] = k

        def f(a, b):
            return tab[(a + b * r) % q]
        return f
    p = dat
    A, B = np.meshgrid(np.arange(p, dtype=np.int64), np.arange(p, dtype=np.int64), indexing="ij")
    A = A.ravel(); B = B.ravel()
    ya, yb = f2_pow_vec(A.copy(), B.copy(), (p * p - 1) // 6, p)
    # zeta6 = -omega^2 = 1 + omega -> (1, 1)
    lut = {}
    va, vb = 1, 0
    for k in range(6):
        lut[(va, vb)] = k
        va, vb = f2_mul(va, vb, 1, 1, p)
    tab = np.full(p * p, ZERO, dtype=np.int16)
    for (va, vb), k in lut.items():
        tab[(ya == va) & (yb == vb) & ((A != 0) | (B != 0))] = k

    def f(a, b):
        return tab[(a % p) * p + (b % p)]
    return f


def rows(Hcut):
    R = int(math.isqrt(int(4 * Hcut / 3)) + 2)
    a, b = np.meshgrid(np.arange(-R, R + 1), np.arange(-R, R + 1), indexing="ij")
    a = a.ravel(); b = b.ravel()
    N = a * a - a * b + b * b
    m = (N > 0) & (N <= Hcut)
    return a[m].astype(np.int64), b[m].astype(np.int64), N[m]


def principal_mask(a, b, N):
    """u = eps v^6 for a unit eps and v in O."""
    keys = set(zip(a.tolist(), b.tolist()))
    units = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]  # 1,-1,w,-w,-w^2=1+w,w^2=-1-w
    mark = set()
    Nmax = int(N.max())
    R = int(round(Nmax ** (1 / 6))) + 2
    for va in range(-R, R + 1):
        for vb in range(-R, R + 1):
            nv = va * va - va * vb + vb * vb
            if nv == 0 or nv ** 6 > Nmax:
                continue
            # v^6
            xa, xb = 1, 0
            for _ in range(6):
                xa, xb = xa * va - xb * vb, xa * vb + xb * va - xb * vb
            for ea, eb in units:
                ua, ub = ea * xa - eb * xb, ea * xb + eb * xa - eb * xb
                if (ua, ub) in keys:
                    mark.add((ua, ub))
    return np.array([(x, y) in mark for x, y in zip(a.tolist(), b.tolist())])


def run(D, rhos, cut=6.0):
    t0 = time.time()
    Hs = {rho: D ** rho for rho in rhos}
    Hcut = cut * max(Hs.values())
    a, b, Nu = rows(Hcut)
    P = prime_ideals(2 * D)
    tabs = [exponent_table(pi) for pi in P]
    E = np.empty((len(P), a.size), dtype=np.int8)
    for i, f in enumerate(tabs):
        E[i] = f(a, b)
    Z6 = np.exp(2j * np.pi * np.arange(7) / 6)
    Z6[6] = 0
    A = np.zeros(a.size, dtype=complex)
    cop = np.zeros(a.size)  # sum_n |W|^2 1_{(u,n)=1}
    zsum = 0.0  # sum |W|^2 prod(1-1/Np)
    psum = 0.0  # sum 2^omega(n) x |W(x)|^2
    count = 0
    norms = [pi[0] for pi in P]
    lim = 2 * D

    # DFS over squarefree products of distinct prime ideals
    stack = [(0, 1, 1, 1.0, 0, None)]  # (next index, norm, mu, prod(1-1/Np), omega, exponent row)
    while stack:
        i0, nn, mu, ph, om, er = stack.pop()
        if nn > D:
            x = nn / D
            w = float(W(np.array([x]))[0])
            if w != 0.0:
                idx = np.where(er >= ZERO, 6, er % 6)
                A += mu * w * Z6[idx]
                cop += (w * w) * (er < ZERO)
                zsum += w * w * ph
                psum += (2 ** om) * x * w * w
                count += 1
        for i in range(i0, len(P)):
            n2 = nn * norms[i]
            if n2 >= lim:
                break
            row = E[i].astype(np.int16) if er is None else er + E[i]
            stack.append((i + 1, n2, -mu, ph * (1 - 1 / norms[i]), om + 1, row))
    pm = principal_mask(a, b, Nu)
    out = []
    for rho in rhos:
        H = Hs[rho]
        phi = np.exp(-np.pi * Nu / H)
        M = float(np.sum(phi * np.abs(A) ** 2) / D)
        Diag = float(np.sum(phi * cop) / D)
        Zv = (H / D) * (2 / math.sqrt(3)) * zsum
        Prin = float(np.sum(phi[pm] * np.abs(A[pm]) ** 2) / D)
        nprin = int(pm.sum())
        S = M - Zv
        res = dict(D=D, rho=rho, H=H, M=M, Z=Zv, S=S, Diag=Diag, Off=M - Diag, P=psum,
                   Prin=Prin, nprin_rows=nprin, ncols=count,
                   A1=float(abs(A[(a == 1) & (b == 0)][0])) if np.any((a == 1) & (b == 0)) else None,
                   ratio_S_over_H=S / H, ratio_P_over_S=psum / abs(S) if S != 0 else None,
                   saving_exp=math.log(psum / abs(S)) / math.log(D) if S != 0 else None,
                   needed_full=1 - rho, needed_beat_11_12=(1 - rho) / 6,
                   offdiag_rel=(M - Diag) / Diag)
        out.append(res)
    return out, time.time() - t0


def main():
    args = sys.argv[1:]
    outp = args[0]
    i = args.index("--rho")
    Ds = [int(x) for x in args[1:i]]
    rhos = [float(x) for x in args[i + 1:]]
    allres = []
    for D in Ds:
        res, dt = run(D, rhos)
        for r in res:
            r["seconds"] = dt
            print(json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in r.items()}),
                  flush=True)
        allres += res
        with open(outp, "w") as fh:
            json.dump(allres, fh, indent=1)


if __name__ == "__main__":
    main()
