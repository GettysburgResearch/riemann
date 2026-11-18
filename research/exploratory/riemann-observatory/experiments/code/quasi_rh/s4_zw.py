# s4_zw.py -- independent Z[omega] arithmetic for the Level-2 audit of Section 4 of
# "The Quasi-Riemann Hypothesis" (paper2.tex, l.773-1253).  Written from scratch for
# this audit; no code from the OpenAI repository is used.
#
# Conventions follow paper2.tex:
#   omega = e^{2 pi i/3}; elements are integer pairs (a,b) = a + b*omega.
#   primary  <=>  x = 1 mod 3.
#   e(z) = exp(4 pi i Im z / sqrt 3)          (l.305-308, l.804)
#   chi_n(u) = (u/n)_6, multiplicative in n, zero extension, chi_1 = 1 (footnote l.256-262)
#   gamma_j(n) = N(n)^{-1/2} sum_{x mod n} chi_n(x)^j e(x/n)                 (l.309-313)
#   alpha(n) = n/|n|
import math, cmath
import numpy as np

SQ3 = math.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
Z6 = cmath.exp(2j * math.pi / 6)            # zeta_6 = 1 + omega

def cv(x):
    return x[0] + x[1] * OMEGA

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
    r = (1, 0)
    for _ in range(e):
        r = mul(r, x)
    return r

def prod(xs):
    r = (1, 0)
    for x in xs:
        r = mul(r, x)
    return r

# zeta_6^k as elements of O
UNIT = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
for k in range(6):
    assert abs(cv(UNIT[k]) - Z6 ** k) < 1e-12

def is_primary(x):
    return (x[0] - 1) % 3 == 0 and x[1] % 3 == 0

def primary(x):
    for u in UNIT:
        y = mul(u, x)
        if is_primary(y):
            return y
    raise ValueError("not prime to 3: %r" % (x,))

def alpha(x):
    z = cv(x)
    return z / abs(z)

def e_add(z):
    """paper's additive character e(z) = exp(4 pi i Im z / sqrt3)"""
    return cmath.exp(4j * math.pi * z.imag / SQ3)

def residues(m):
    """complete residue system of O modulo m (HNF of the lattice mO)"""
    n0, n1 = m
    w = mul(m, (0, 1))
    g = math.gcd(n1, w[1])
    N = norm(m)
    return [(a, b) for b in range(g) for a in range(N // g)]

def rational_primes(L):
    s = bytearray([1]) * (L + 1); s[0] = s[1] = 0
    for i in range(2, int(L ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(L + 1) if s[i]]

class Prime:
    """A prime ideal of O not dividing 6, with primary generator self.g and a
    sextic-residue table on O/p."""
    def __init__(self, g):
        assert is_primary(g)
        self.g = g
        self.q = norm(g)
        q = self.q
        if q % 3 == 1 and all(q % t for t in range(2, int(q ** 0.5) + 1)):
            # split: O/p = Z/q with omega -> r
            self.split = True
            self.ell = q
            r = next(r for r in range(q) if divides(g, (-r, 1)))
            self.r = r
            # discrete-log free: direct exponent table
            e6 = (q - 1) // 6
            unit_res = {((u[0] + u[1] * r) % q): k for k, u in enumerate(UNIT)}
            tab = [None] * q
            for v in range(1, q):
                tab[v] = unit_res[pow(v, e6, q)]
            self.tab = tab
        else:
            # inert: g = -ell, O/p = F_{ell^2}
            self.split = False
            ell = int(round(math.sqrt(q)))
            assert ell * ell == q and ell % 3 == 2
            self.ell = ell
            e6 = (q - 1) // 6
            def fmul(x, y):
                a, b = x; c, d = y
                return ((a * c - b * d) % ell, (a * d + b * c - b * d) % ell)
            def fpow(x, e):
                r_ = (1, 0)
                while e:
                    if e & 1: r_ = fmul(r_, x)
                    x = fmul(x, x); e >>= 1
                return r_
            unit_res = {(u[0] % ell, u[1] % ell): k for k, u in enumerate(UNIT)}
            tab = [None] * q
            for a in range(ell):
                for b in range(ell):
                    if a == 0 and b == 0: continue
                    tab[a + ell * b] = unit_res[fpow((a, b), e6)]
            self.tab = tab

    def idx(self, x):
        if self.split:
            return (x[0] + x[1] * self.r) % self.ell
        return (x[0] % self.ell) + self.ell * (x[1] % self.ell)

    def sym(self, x):
        """exponent k with (x/p)_6 = zeta6^k, or None if p | x"""
        return self.tab[self.idx(x)]

    def idx_arr(self, A, B):
        if self.split:
            return (A + B * self.r) % self.ell
        return (A % self.ell) + self.ell * (B % self.ell)

    def sym_arr(self, A, B):
        """vectorised: exponents (int, -1 for zero)"""
        t = getattr(self, "_tarr", None)
        if t is None:
            t = np.array([(-1 if v is None else v) for v in self.tab], dtype=np.int64)
            self._tarr = t
        return t[self.idx_arr(A, B)]

    def __repr__(self):
        return "P%r" % (self.g,)

def eisenstein_primes(maxnorm, exclude_inert=(2,)):
    out = []
    for ell in rational_primes(maxnorm):
        if ell == 3: continue
        if ell % 3 == 1:
            a0 = None
            for a in range(-ell, ell + 1):
                for b in range(-ell, ell + 1):
                    if norm((a, b)) == ell:
                        a0 = (a, b); break
                if a0: break
            p1 = primary(a0); p2 = primary(conj(a0))
            out += [p1, p2]
        else:
            if ell in exclude_inert: continue
            if ell * ell <= maxnorm:
                out.append((-ell, 0))
    out = sorted(set(out), key=lambda x: (norm(x), x))
    return [Prime(g) for g in out]

def chi(primes, x, j=1):
    """chi_n(x)^j for squarefree n = prod(primes); zero extension; chi_1 = 1"""
    tot = 0
    for p in primes:
        k = p.sym(x)
        if k is None:
            return 0
        tot += k * j
    return Z6 ** (tot % 6)

def chi_arr(primes, A, B, j=1):
    """vectorised chi_n(x)^j over arrays of coordinates"""
    tot = np.zeros(A.shape, dtype=np.int64)
    zero = np.zeros(A.shape, dtype=bool)
    for p in primes:
        s = p.sym_arr(A, B)
        zero |= (s < 0)
        tot += np.where(s < 0, 0, s) * j
    val = np.exp(2j * np.pi * (tot % 6) / 6)
    val[zero] = 0
    return val

def gauss_general(m, char_fn):
    """N(m)^{-1/2} sum_{x mod m} char(x) e(x/m)"""
    R = residues(m)
    A = np.array([r[0] for r in R], dtype=np.int64)
    B = np.array([r[1] for r in R], dtype=np.int64)
    vals = char_fn(A, B)
    zc = (A + B * OMEGA) / cv(m)
    ph = np.exp(4j * np.pi * zc.imag / SQ3)
    return complex(np.sum(vals * ph)) / math.sqrt(norm(m))

def gamma(primes, j):
    m = prod([p.g for p in primes])
    if not primes:
        return 1.0 + 0j
    return gauss_general(m, lambda A, B: chi_arr(primes, A, B, j))

def lattice_points(R):
    """all x in O with 0 < N(x) <= R (as arrays a,b), plus list"""
    bmax = int(math.ceil(math.sqrt(4 * R / 3))) + 2
    pts = []
    for b in range(-bmax, bmax + 1):
        # a^2 - ab + b^2 <= R  -> a in [b/2 - s, b/2 + s], s = sqrt(R - 3b^2/4)
        disc = R - 0.75 * b * b
        if disc < 0: continue
        s = math.sqrt(disc)
        for a in range(int(math.floor(b / 2 - s)) - 1, int(math.ceil(b / 2 + s)) + 2):
            n = a * a - a * b + b * b
            if 0 < n <= R:
                pts.append((a, b))
    A = np.array([p[0] for p in pts], dtype=np.int64)
    B = np.array([p[1] for p in pts], dtype=np.int64)
    return A, B

def squarefree_products(primes, maxnorm, exclude=()):
    """all squarefree products (as lists of Prime) with norm <= maxnorm (including [])"""
    ps = [p for p in primes if p.g not in exclude]
    out = [[]]
    def rec(start, cur, nrm):
        for i in range(start, len(ps)):
            nn = nrm * ps[i].q
            if nn > maxnorm: continue
            out.append(cur + [ps[i]])
            rec(i + 1, cur + [ps[i]], nn)
    rec(0, [], 1)
    return out

def nm(primes):
    r = 1
    for p in primes: r *= p.q
    return r

def elt(primes):
    return prod([p.g for p in primes])

# ---- quadratic Gauss sum and G on classes mod 4 (App. A.1 definitions) ----
def gamma_quad(c):
    """|c|^{-1} sum_{x mod c} e(x^2/c), computed by brute force"""
    R = residues(c)
    A = np.array([r[0] for r in R], dtype=np.int64)
    B = np.array([r[1] for r in R], dtype=np.int64)
    # x^2 = (a^2 - b^2) + (2ab - b^2) omega
    X0 = A * A - B * B; X1 = 2 * A * B - B * B
    zc = (X0 + X1 * OMEGA) / cv(c)
    return complex(np.sum(np.exp(4j * np.pi * zc.imag / SQ3))) / abs(cv(c))

def mod4(x):
    return (x[0] % 4, x[1] % 4)
