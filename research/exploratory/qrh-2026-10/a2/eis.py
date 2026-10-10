"""Minimal exact arithmetic in O = Z[omega] (omega = e^{2 pi i/3}) for structural checks.
Elements are integer pairs (a, b) <-> a + b*omega.  Conventions follow the OpenAI QRH manuscripts:
primary = 1 mod 3; chi_n(u) = (u/n)_6 = sixth root of unity == u^{(Np-1)/6} mod p, multiplicative in n;
e(z) = exp(4 pi i Im z / sqrt 3); gamma_j(n) = N(n)^{-1/2} sum_{v mod n} chi_n(v)^j e(v/n)."""
import cmath, math
from functools import lru_cache

UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta^k, zeta = 1+omega = e^{i pi/3}
def mul(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c - b*d)
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0]*x[0] - x[0]*x[1] + x[1]*x[1]
def is_primary(x): return x[0] % 3 == 1 and x[1] % 3 == 0
def primary(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(x)
def divides(m, z):
    c, d = mul(z, conj(m)); n = norm(m)
    return c % n == 0 and d % n == 0
def reduce_mod(z, m):
    c, d = mul(z, conj(m)); n = norm(m)
    q = ((2*c + n)//(2*n), (2*d + n)//(2*n)); qm = mul(q, m)
    return (z[0] - qm[0], z[1] - qm[1])
def powmod(z, e, m):
    r, b = (1, 0), reduce_mod(z, m)
    while e:
        if e & 1: r = reduce_mod(mul(r, b), m)
        b = reduce_mod(mul(b, b), m); e >>= 1
    return r

def sym_prime(u, p):
    """(u/p)_6 as k in 0..5 (value zeta^k) or None if p | u."""
    if divides(p, u): return None
    t = powmod(u, (norm(p) - 1)//6, p)
    for k, z in enumerate(UNITS):
        if divides(p, (t[0] - z[0], t[1] - z[1])): return k
    raise RuntimeError

def primes_upto(N):
    """primary prime elements (prime to 6) with norm <= N."""
    out = []
    isp = [True]*(N + 1); isp[0] = isp[1] = False
    for i in range(2, int(N**0.5) + 1):
        if isp[i]: isp[i*i::i] = [False]*len(isp[i*i::i])
    for p in range(5, N + 1):
        if not isp[p]: continue
        if p % 3 == 1:
            found = None
            for a in range(-p, p + 1):
                for b in range(-p, p + 1):
                    if a*a - a*b + b*b == p:
                        found = (a, b); break
                if found: break
            pi = primary(found); pib = primary(conj(found))
            out += [pi, pib]
        elif p % 3 == 2 and p*p <= N:
            out.append(primary((p, 0)))
    return sorted(set(out), key=norm)

def chi(n_factors, u):
    """chi_n(u) for squarefree n given by its list of primary prime factors; returns k mod 6 or None."""
    s = 0
    for p in n_factors:
        k = sym_prime(u, p)
        if k is None: return None
        s += k
    return s % 6

def residues(n):
    """complete residue system of O/nO via HNF of the lattice {n, n*omega} in Z^2."""
    v1, v2 = n, mul(n, (0, 1))
    # HNF in basis (1, omega): find d2 = gcd of b-coordinates etc.
    import math
    a1, b1 = v1; a2, b2 = v2
    # lattice L = Z v1 + Z v2 ; index N = |a1 b2 - a2 b1|
    N = abs(a1*b2 - a2*b1)
    g = math.gcd(b1, b2)            # minimal positive b-coordinate in L is g
    # find x,y with x b1 + y b2 = g
    def egcd(a, b):
        if b == 0: return (a, 1, 0)
        q, x, y = egcd(b, a % b); return (q, y, x - (a//b)*y)
    gg, x, y = egcd(b1, b2)
    if gg < 0: gg, x, y = -gg, -x, -y
    w = (x*a1 + y*a2, g)            # lattice vector with b = g
    d1 = N // g                     # lattice contains (d1, 0)
    return [(i, j) for j in range(g) for i in range(d1)], N

def e_of(z, n):
    """e(z/n) = exp(4 pi i Im(z/n)/sqrt3); z/n = z conj(n)/N(n) = (c + d omega)/N -> exp(2 pi i d / N)."""
    c, d = mul(z, conj(n)); N = norm(n)
    return cmath.exp(2j*math.pi*(d % N)/N)

ZETA = [cmath.exp(1j*math.pi*k/3) for k in range(6)]

def gamma(j, n_factors):
    n = (1, 0)
    for p in n_factors: n = mul(n, p)
    R, N = residues(n)
    assert N == norm(n), (N, norm(n))
    s = 0
    for v in R:
        k = chi(n_factors, v)
        if k is None or (j % 6 == 0): 
            if k is None: continue
            s += e_of(v, n); continue
        s += ZETA[(j*k) % 6]*e_of(v, n)
    return s/math.sqrt(N)
