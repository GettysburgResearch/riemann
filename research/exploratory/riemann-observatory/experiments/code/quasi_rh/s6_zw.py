# s6_zw.py -- independent Z[omega] arithmetic for the Level-2 audit of Section 6 of
# "The Quasi-Riemann Hypothesis" (paper2.tex l.1632-2216, with App. A.2 l.2874-3479).
# Written from scratch for this audit; no code from the OpenAI repository is used.
#
# Elements are integer pairs (a,b) = a + b*omega, omega = e^{2 pi i/3}.
# lambda = 1 + 2 omega = sqrt(-3).  "primary" = congruent to 1 mod 3.
import math, cmath
from functools import lru_cache
import sympy

SQ3 = math.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
LAM = (1, 2)
ONE = (1, 0); OM = (0, 1); OM2 = (-1, -1)
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]   # 1,-1,w,-w,w^2,-w^2


def cv(x): return x[0] + x[1] * OMEGA
def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def conj(x):
    a, b = x
    return (a - b, -b)
def norm(x):
    a, b = x
    return a * a - a * b + b * b
def divides(d, x):
    n = norm(d); z = mul(x, conj(d))
    return z[0] % n == 0 and z[1] % n == 0
def exact_div(x, d):
    n = norm(d); z = mul(x, conj(d))
    assert z[0] % n == 0 and z[1] % n == 0, (x, d)
    return (z[0] // n, z[1] // n)
def power(x, e):
    r = ONE
    for _ in range(e): r = mul(r, x)
    return r
def is_primary(x): return (x[0] - 1) % 3 == 0 and x[1] % 3 == 0
def is_zero(x): return x[0] == 0 and x[1] == 0
def from_complex(z):
    # inverse of cv for exact lattice points
    b = round(z.imag / (SQ3 / 2)); a = round(z.real + b / 2)
    assert abs(cv((a, b)) - z) < 1e-9
    return (a, b)

def _rdiv(a, n):
    # exact nearest-integer division for (possibly huge) Python ints, n > 0
    return (2 * a + n) // (2 * n)
def rmod(x, m):
    n = norm(m); z = mul(x, conj(m))
    q = (_rdiv(z[0], n), _rdiv(z[1], n))
    best = None
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            qq = (q[0] + da, q[1] + db); r = sub(x, mul(qq, m))
            if best is None or norm(r) < norm(best): best = r
    return best
def egcd(x, y):
    # returns (g, s, t) with s x + t y = g
    r0, r1 = x, y; s0, s1 = ONE, (0, 0); t0, t1 = (0, 0), ONE
    while not is_zero(r1):
        n = norm(r1); z = mul(r0, conj(r1))
        q = (_rdiv(z[0], n), _rdiv(z[1], n))
        # Euclidean quotient: pick neighbour with smallest remainder
        best = None
        for da in (-1, 0, 1):
            for db in (-1, 0, 1):
                qq = (q[0] + da, q[1] + db); r = sub(r0, mul(qq, r1))
                if best is None or norm(r) < norm(best[1]): best = (qq, r)
        q, r = best
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    return r0, s0, t0
def inv_mod(x, m):
    g, s, t = egcd(x, m)
    assert norm(g) == 1, ("not invertible", x, m)
    # g unit; s x = g mod m
    ginv = conj(g)   # unit inverse = conjugate
    return rmod(mul(s, ginv), m)
def powmod(x, e, m):
    r = ONE; x = rmod(x, m)
    while e:
        if e & 1: r = rmod(mul(r, x), m)
        x = rmod(mul(x, x), m); e >>= 1
    return r

def make_primary(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(("cannot make primary", x))

@lru_cache(maxsize=None)
def primes_over(p):
    """Primary generators (or lambda for p=3) of the prime ideals above rational prime p."""
    if p == 3: return (LAM,)
    if p % 3 == 2: return (make_primary((p, 0)),)
    for a in range(0, p + 1):
        for b in range(0, p + 1):
            if norm((a, b)) == p:
                pi = make_primary((a, b))
                return (pi, make_primary(conj(pi)))
    raise ValueError(p)

def factor(x):
    """Return (unit, list of (prime, exp)) with x = unit * prod prime^exp; primes primary except lambda."""
    assert not is_zero(x)
    fac = []
    y = x
    for p, e in sympy.factorint(norm(x)).items():
        for pi in primes_over(p):
            k = 0
            while divides(pi, y):
                y = exact_div(y, pi); k += 1
            if k: fac.append((pi, k))
    assert norm(y) == 1, (x, y)
    return y, fac

def unit_index(u):
    return UNITS.index(u)

# cubic residue symbol (x/pi)_3 for a prime pi != lambda, returned as exponent j with value omega^j, or None if pi | x
def cubic_exp_prime(x, pi):
    if divides(pi, x): return None
    q = norm(pi)
    r = powmod(x, (q - 1) // 3, pi)
    for j, w in enumerate((ONE, OM, OM2)):
        if divides(pi, sub(r, w)): return j
    raise ValueError(("not a cube root of unity", x, pi, r))

def cubic_symbol(x, a):
    """(x/a)_3 for a coprime to 3 (any associate), multiplicative in a; exponent j (value omega^j) or None if not coprime."""
    u, fac = factor(a)
    tot = 0
    for pi, e in fac:
        assert pi != LAM
        j = cubic_exp_prime(x, pi)
        if j is None: return None
        tot += j * e
    return tot % 3

def omega_pow(j): return OMEGA ** (j % 3)

def ebreve(z):
    """DR (2.1)/(1.7): e-breve(z) = exp(2 pi i (z + conj z)) = exp(4 pi i Re z)."""
    return cmath.exp(4j * math.pi * z.real)

def e_add(z):
    """paper: e(z) = exp(4 pi i Im z/sqrt 3) = ebreve(z/lambda)."""
    return cmath.exp(4j * math.pi * z.imag / SQ3)

def residues(m):
    a, b = m
    n = norm(m)
    v1 = m; v2 = mul(m, OM)
    g = math.gcd(v1[1], v2[1])
    d1 = n // g
    return [(x, y) for y in range(g) for x in range(d1)]

# ---------------------------------------------------------------------------------------------
# Cubic residue symbol (x/y)_3 for arbitrary (large) y coprime to 3, WITHOUT factoring y:
# Euclid-type algorithm using cubic reciprocity (a/b)_3=(b/a)_3 for primary a,b and the
# supplementary laws DR (1.5) for omega, lambda (both verified numerically against the
# factorization-based definition in s6_cubic_selftest below).  (-1/y)_3 = 1.
def _supp(d):
    """for primary d: (alpha2, alpha3) with d = 1 + a2 lam^2 + a3 lam^3 mod 9."""
    L2 = power(LAM, 2); L3 = power(LAM, 3)
    for a2 in (-1, 0, 1):
        for a3 in (-1, 0, 1):
            t = (1 + a2 * L2[0] + a3 * L3[0], a2 * L2[1] + a3 * L3[1])
            if divides((9, 0), sub(d, t)): return a2, a3
    raise ValueError(d)

def cubic_jacobi(x, y):
    """(x/y)_3 as exponent mod 3 (value omega^j), None if gcd(x,y) nontrivial. y coprime to 3."""
    y = make_primary(y)
    acc = 0
    while True:
        if norm(y) == 1: return acc % 3
        x = rmod(x, y)
        if is_zero(x): return None
        # strip lambda powers
        a2, a3 = _supp(y)
        while divides(LAM, x):
            x = exact_div(x, LAM); acc += -a3
        # strip unit: x = u * x' with x' primary
        xp = make_primary(x)
        u = exact_div(x, xp)
        # (u/y)_3 : units -1 -> 1, omega -> w^{a2}, omega^2 -> w^{2 a2}
        k = {(1, 0): 0, (-1, 0): 0, (0, 1): 1, (0, -1): 1, (-1, -1): 2, (1, 1): 2}[u]
        acc += k * a2
        # reciprocity
        x, y = y, xp

def canon_mod(x, m):
    """canonical representative of x mod m (m nonzero), via the HNF residue system used in residues()."""
    n = norm(m); v1 = m; v2 = mul(m, OM)
    g = math.gcd(v1[1], v2[1])
    # find lattice vector with omega-coordinate g: solve s*v1[1] + t*v2[1] = g
    import sympy as _sp
    s_, t_, gg = _sp.gcdex(v1[1], v2[1])
    s_, t_ = int(s_), int(t_)
    if gg < 0: s_, t_ = -s_, -t_
    w = add((s_ * v1[0], s_ * v1[1]), (t_ * v2[0], t_ * v2[1]))   # w = (w0, g)
    assert w[1] == g
    d1 = n // g
    k = x[1] // g
    y = sub(x, (k * w[0], k * w[1]))
    return (y[0] % d1, y[1])
