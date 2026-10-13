#!/usr/bin/env python3
"""O3b: small-scale numerical test of the non-alignment statement (NA) of O3 Section 2.3.

EMPIRICAL / floating point, finite.  Nothing here is certified; no theorem is proved by it.

Toy model M0 (documented simplifications of [S30] eq:general-probe / eq:low-separated):
  ring O = Z[omega]; S = {2, lambda=1-omega}; b_* = 2*lambda; xi = (quadratic char mod lambda) x
  (cubic char mod 2), order 6, nonprincipal at both primes (as in [S30] l. 3352ff).
  m runs over ALL nonzero elements of O with N(m) <= Q, weight Omega(N m/Q) = (1 - N m/Q)^3_+.
  A_m(Y') = Y'^{-1} sum_{s sf primary, (s,2)=1} W1(r_s) r_s^{-1/2} c(s) q_s^{-1/2} g_{chi_s}(s,-m),
      r_s = N s / Y', W1(r) = sin^2(pi (r-1)) on [1,2], v = 0, c(s) = chi_s(b_*) conj(xi(s))
      (tau dropped: |tau| = 1; ray-class restriction 1_{s in sigma} dropped = one fixed class).
      For squarefree s:  q_s^{-1/2} g_{chi_s}(s,-m) = conj(chi_s(-m)) gamma_1(s)  (zero-extended).
  B_m(Z)  = sum_{c sf primary, (c,2)=1} theta(c) conj(Xi(c)) chi_c(m) V(N c/Z) N(c)^{-1/2},
      theta(c) = gamma_2(c) conj(alpha(c)) = mu(c) conj(gamma_2(c))^2   (alpha := mu gamma_2^3,
      [S30] eq:signal), Xi(c) = xi(c) chi_c(b_*), V(x) = exp(-x^2), eta = 1, R(.,s_sigma) and the
      G-correction a_theta dropped, n = 1 (cube part) dropped, Mellin t -> 0.
  pairing <A,B> = sum_m Omega(N m/Q) xi(m) A_m B_m   (bilinear, as in eq:low-separated).
"""
import cmath, json, math, os, sys, time
import numpy as np

ZETA = np.exp(1j * np.pi * np.arange(6) / 3)

def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
def is_primary(x): return x[0] % 3 == 1 and x[1] % 3 == 0
def primary(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(x)

def sieve(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]

def factor_int(n):
    f = []; d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: f.append(n)
    return f

class Prime:
    """primary prime element of O prime to 6, with residue map, sextic log table, Gauss sums."""
    def __init__(self, kind, p, a, b):
        self.kind, self.p, self.el = kind, p, (a, b)
        if kind == 0:                       # split, N = p
            self.N = p
            fs = factor_int(p - 1)
            g = 2
            while any(pow(g, (p - 1) // f, p) == 1 for f in fs): g += 1
            self.r = (-a) * pow(b % p, p - 2, p) % p
            t = pow(g, (p - 1) // 6, p); z = (1 + self.r) % p; zk = 1; k0 = None
            for k in range(6):
                if zk == t: k0 = k; break
                zk = zk * z % p
            assert k0 is not None
            ind = np.zeros(p, dtype=np.int64); x = 1
            for j in range(p - 1):
                ind[x] = j; x = x * g % p
            e = (k0 * (ind % 6)) % 6
            e[0] = -1
            self.tab = e.astype(np.int8)
            xs = np.arange(p)
            ph = np.exp(-2j * np.pi * ((b % p) * xs % p) / p)
        else:                               # inert, pi = -q, N = q^2
            q = p; self.N = q * q; n2 = q * q - 1; fs = factor_int(n2)
            def zm(x, y):
                return ((x[0] * y[0] - x[1] * y[1]) % q, (x[0] * y[1] + x[1] * y[0] - x[1] * y[1]) % q)
            def zp(x, e):
                r = (1, 0)
                while e:
                    if e & 1: r = zm(r, x)
                    x = zm(x, x); e >>= 1
                return r
            gen = None
            for gu in range(q):
                for gv in range(1, q):
                    if all(zp((gu, gv), n2 // f) != (1, 0) for f in fs): gen = (gu, gv); break
                if gen: break
            t = zp(gen, n2 // 6); zk = (1, 0); k0 = None
            for k in range(6):
                if zk == t: k0 = k; break
                zk = zm(zk, (1, 1))
            assert k0 is not None
            ind = np.zeros(q * q, dtype=np.int64); x = (1, 0)
            for j in range(n2):
                ind[x[0] * q + x[1]] = j; x = zm(x, gen)
            e = (k0 * (ind % 6)) % 6; e[0] = -1
            self.tab = e.astype(np.int8)
            vs = np.arange(q * q) % q
            ph = np.exp(-2j * np.pi * vs / q)
        tab = self.tab.astype(np.int64)
        bins = np.zeros(6, complex)
        msk = tab >= 0
        for k in range(6): bins[k] = ph[msk & (tab == k)].sum()
        self.gam = {j: (bins * ZETA[(j * np.arange(6)) % 6]).sum() / math.sqrt(self.N) for j in (1, 2, 3)}

    def resid(self, x, y):
        if self.kind == 0: return (x + y * self.r) % self.p
        q = self.p
        return (x % q) * q + (y % q)
    def e_of(self, el):
        return int(self.tab[self.resid(el[0], el[1])])

def make_primes(X):
    out = []
    for p in sieve(X):
        if p < 5: continue
        if p % 3 == 1:
            b = 1
            while True:
                d = 4 * p - 3 * b * b
                s = math.isqrt(d)
                if s * s == d:
                    a = (s + b) // 2 if (s + b) % 2 == 0 else None
                    if a is not None and a * a - a * b + b * b == p: break
                    a = (b - s) // 2 if (b - s) % 2 == 0 else None
                    if a is not None and a * a - a * b + b * b == p: break
                b += 1
            pi = primary((a, b)); pib = primary(conj((a, b)))
            for el in (pi, pib): out.append(Prime(0, p, el[0], el[1]))
        elif p * p <= X:
            out.append(Prime(1, p, -p, 0))
    out.sort(key=lambda P: P.N)
    return out

def sf_elements(primes, X):
    """squarefree primary elements with N <= X: list of (el, N, [prime idx])."""
    res = []
    def dfs(start, el, N, fac):
        res.append((el, N, list(fac)))
        for i in range(start, len(primes)):
            P = primes[i]
            if N * P.N > X: break
            fac.append(i); dfs(i + 1, mul(el, P.el), N * P.N, fac); fac.pop()
    dfs(0, (1, 0), 1, [])
    return res

def chi_exp_el(primes, fac, el):
    """exponent k of chi_s(el) = zeta^k (s = prod primes[fac]), or -1."""
    t = 0
    for i in fac:
        k = primes[i].e_of(el)
        if k < 0: return -1
        t += k
    return t % 6

def gamma_sf(primes, fac, j):
    g = 1 + 0j
    for i in fac: g *= primes[i].gam[j]
    for u in range(len(fac)):
        for v in range(u + 1, len(fac)):
            pu, pv = primes[fac[u]], primes[fac[v]]
            k = pu.e_of(pv.el) + pv.e_of(pu.el)
            g *= ZETA[(j * k) % 6]
    return g

def ball(Q):
    pts = []
    ymax = int(math.isqrt(int(4 * Q / 3))) + 1
    for y in range(-ymax, ymax + 1):
        for x in range(-2 * ymax - 2, 2 * ymax + 3):
            n = x * x - x * y + y * y
            if 0 < n <= Q: pts.append((x, y, n))
    a = np.array(pts, dtype=np.int64)
    return a[:, 0], a[:, 1], a[:, 2]

def xi_vec(x, y):
    l = (x + y) % 3
    xl = np.where(l == 0, 0.0, np.where(l == 1, 1.0, -1.0))
    u, v = x % 2, y % 2
    x2 = np.where((u == 0) & (v == 0), 0, np.where((u == 1) & (v == 0), 1, np.where((u == 0) & (v == 1), np.exp(2j * np.pi / 3), np.exp(4j * np.pi / 3))))
    return xl * x2

def xi_el(el):
    return complex(xi_vec(np.array([el[0]]), np.array([el[1]]))[0])
