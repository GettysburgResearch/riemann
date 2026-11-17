# appA_zw.py -- Z[omega] arithmetic written from scratch for the Level-2 audit of
# Appendix A of "The Quasi-Riemann Hypothesis" (paper2.tex l.2687-3480).
# No code from the OpenAI repository is used or imported.  Run with python3 -I.
#
# Conventions (paper2.tex l.242-262, l.306-312, l.2900-2904):
#   omega = e^{2 pi i/3}; an element x = (a, b) means a + b*omega (Python ints).
#   lambda = 1 + 2 omega = sqrt(-3); primary <=> x == 1 (mod 3).
#   chi_n(u) = (u/n)_6, the sextic symbol: for a prime p not dividing 6, (u/p)_6 is the
#   sixth root of unity == u^{(Np-1)/6} (mod p), zero if p | u; multiplicative in n.
#   e(z) = exp(4 pi i Im z / sqrt 3) = exp(2 pi i Tr(z/lambda));  for z = u + v*omega
#   with u, v rational this is exp(2 pi i v).
#   breve-e(z) = exp(2 pi i (z + zbar)) = exp(2 pi i Tr z) = exp(2 pi i (2u - v)).
# Values of sixth roots of unity are stored as exponents k mod 6 of zeta6 = e^{i pi/3}
# = -omega^2 = 1 + omega.
import math, cmath
from fractions import Fraction
import sympy

SQ3 = math.sqrt(3.0)
W = complex(-0.5, SQ3 / 2)          # omega
ZETA6 = cmath.exp(1j * math.pi / 3)  # = 1 + omega
LAM = (1, 2)
ONE = (1, 0); ZERO = (0, 0)
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]  # zeta6^k, k = 0..5


def cv(x): return x[0] + x[1] * W
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def conj(x): return (x[0] - x[1], -x[1])
def norm(x): return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
def is_zero(x): return x[0] == 0 and x[1] == 0
def pw(x, e):
    r = ONE
    for _ in range(e): r = mul(r, x)
    return r
def divides(d, x):
    n = norm(d); z = mul(x, conj(d))
    return z[0] % n == 0 and z[1] % n == 0
def exdiv(x, d):
    n = norm(d); z = mul(x, conj(d))
    assert z[0] % n == 0 and z[1] % n == 0, ("not divisible", x, d)
    return (z[0] // n, z[1] // n)
def cong(x, y, m): return divides(m, sub(x, y))
def is_primary(x): return (x[0] - 1) % 3 == 0 and x[1] % 3 == 0


def _nearest(a, n):  # nearest integer to a/n, n > 0, exact for big ints
    return (2 * a + n) // (2 * n)
def rmod(x, m):
    """Euclidean remainder of x modulo m (small norm representative)."""
    n = norm(m); z = mul(x, conj(m))
    q = (_nearest(z[0], n), _nearest(z[1], n))
    best = None
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            r = sub(x, mul((q[0] + da, q[1] + db), m))
            if best is None or norm(r) < norm(best): best = r
    return best
def egcd(x, y):
    """returns (g, s, t) with s x + t y = g, g a gcd."""
    r0, r1 = x, y; s0, s1 = ONE, ZERO; t0, t1 = ZERO, ONE
    while not is_zero(r1):
        n = norm(r1); z = mul(r0, conj(r1))
        q = (_nearest(z[0], n), _nearest(z[1], n))
        r2 = sub(r0, mul(q, r1))
        if norm(r2) >= norm(r1):
            # fall back to a full search around q (never needed for Z[omega], kept as guard)
            r2 = rmod(r0, r1); q = exdiv(sub(r0, r2), r1)
        r0, r1 = r1, r2
        s0, s1 = s1, sub(s0, mul(q, s1)); t0, t1 = t1, sub(t0, mul(q, t1))
    return r0, s0, t0
def is_unit(x): return norm(x) == 1
def inv_mod(x, m):
    g, s, t = egcd(x, m)
    assert is_unit(g), ("not invertible", x, m)
    # s x + t m = g (unit) -> x^{-1} = s * g^{-1}
    return rmod(mul(s, conj(g)), m)
def primary_assoc(x):
    """the unique associate == 1 mod 3 (x coprime to 3)."""
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError(("not coprime to 3", x))
def unit_exponent(u):
    return UNITS.index(u)


_hnf_cache = {}
def hnf(m):
    """(h1, k, h2): the lattice mO (as integer vectors) has basis (h1, k), (0, h2)."""
    if m in _hnf_cache: return _hnf_cache[m]
    a, b = m
    M = [[a, b], [-b, a - b]]   # m and m*omega as integer vectors
    while M[1][0] != 0:
        q = M[0][0] // M[1][0]
        M[0] = [M[0][0] - q * M[1][0], M[0][1] - q * M[1][1]]
        M[0], M[1] = M[1], M[0]
    if M[0][0] < 0: M[0] = [-M[0][0], -M[0][1]]
    h1 = M[0][0]; k = M[0][1]; h2 = abs(M[1][1])
    assert h1 * h2 == norm(m), (m, M)
    _hnf_cache[m] = (h1, k, h2)
    return h1, k, h2
def red(x, m):
    """canonical representative of x mod m, in {(i, j): 0 <= i < h1, 0 <= j < h2}."""
    h1, k, h2 = hnf(m)
    s = x[0] // h1
    return (x[0] - s * h1, (x[1] - s * k) % h2)
def residues(m):
    h1, k, h2 = hnf(m)
    return [(i, j) for i in range(h1) for j in range(h2)]


# ---------- factorization ----------
_split_cache = {}
def split_prime(q):
    """primary pi with N(pi) = q for rational prime q == 1 mod 3."""
    if q in _split_cache: return _split_cache[q]
    for b in range(0, int(math.isqrt(4 * q // 3)) + 2):
        # a^2 - ab + b^2 = q
        disc = 4 * q - 3 * b * b
        if disc < 0: break
        r = math.isqrt(disc)
        if r * r == disc:
            for a in ((b + r) // 2, (b - r) // 2):
                if a * a - a * b + b * b == q:
                    pi = primary_assoc((a, b)); _split_cache[q] = pi; return pi
    raise ValueError(q)
def factor(x):
    """returns (unit u, dict prime->exponent) with x = u * prod p^e, primes primary or lambda."""
    assert not is_zero(x)
    fac = {}; y = x
    for q, e in sympy.factorint(norm(x)).items():
        if q == 3:
            cands = [LAM]
        elif q % 3 == 2:
            cands = [(-q, 0)]
        else:
            pi = split_prime(q); cands = [pi, conj(pi)]
            cands = [primary_assoc(c) for c in cands]
        for p in cands:
            while divides(p, y):
                y = exdiv(y, p); fac[p] = fac.get(p, 0) + 1
    assert is_unit(y), (x, y, fac)
    return y, fac
def is_squarefree(x):
    _, f = factor(x); return all(e == 1 for e in f.values())
def mobius(x):
    _, f = factor(x)
    if any(e > 1 for e in f.values()): return 0
    return (-1) ** len(f)


# ---------- residue fields and the sextic symbol ----------
class PrimeRes:
    """O/(p) for a primary prime p coprime to 6, with discrete logs."""
    def __init__(self, p):
        self.p = p; self.N = norm(p)
        self.res = residues(p)
        # discrete log table
        n1 = self.N - 1
        fac = sympy.factorint(n1)
        g = None
        for r in self.res:
            if is_zero(r): continue
            if all(not cong(self.powmod(r, n1 // q), ONE, p) for q in fac):
                g = r; break
        self.g = g
        self.log = {}
        x = ONE
        for k in range(n1):
            self.log[self.canon(x)] = k
            x = red(mul(x, g), p)
        assert len(self.log) == n1
        # g^{(N-1)/6} is a primitive sixth root of unity; find its exponent k0 wrt zeta6 = 1+omega
        t = self.powmod(g, n1 // 6)
        k0 = [k for k in range(6) if cong(t, UNITS[k], p)]
        assert len(k0) == 1 and math.gcd(k0[0], 6) == 1
        self.k0 = k0[0]
        self._red = {}
    def canon(self, x):
        return red(x, self.p)
    def powmod(self, x, e):
        r = ONE; b = rmod(x, self.p)
        while e:
            if e & 1: r = rmod(mul(r, b), self.p)
            b = rmod(mul(b, b), self.p); e >>= 1
        return r
    def ind(self, x):
        c = self.canon(x)
        if is_zero(rmod(c, self.p)): return None
        return self.log[c]
    def sym6(self, x):
        """exponent k with (x/p)_6 = zeta6^k, or None if p | x."""
        i = self.ind(x)
        if i is None: return None
        return (i * self.k0) % 6


_pr_cache = {}
def PR(p):
    if p not in _pr_cache: _pr_cache[p] = PrimeRes(p)
    return _pr_cache[p]


def sym6_direct(x, p):
    """sextic symbol by definition: x^{(Np-1)/6} mod p matched to a unit (independent of logs)."""
    if divides(p, x): return None
    N = norm(p)
    t = ONE; b = rmod(x, p); e = (N - 1) // 6
    while e:
        if e & 1: t = rmod(mul(t, b), p)
        b = rmod(mul(b, b), p); e >>= 1
    ks = [k for k in range(6) if cong(t, UNITS[k], p)]
    assert len(ks) == 1, (x, p, t)
    return ks[0]


def chi(n, x):
    """chi_n(x) = (x/n)_6 as exponent mod 6 (None = 0) for primary n coprime to 6."""
    if n == ONE: return 0
    _, f = factor(n)
    k = 0
    for p, e in f.items():
        s = PR(p).sym6(x)
        if s is None: return None
        k += e * s
    return k % 6
def chi_c(n, x, j=1):
    """complex value of chi_n(x)^j with zero extension (j=0 gives the indicator of (x,n)=1)."""
    k = chi(n, x)
    if k is None: return 0.0
    return ZETA6 ** ((j * k) % 6)


def ecoord(z_num, den):
    """for z = z_num/den (z_num in O, den in O), return rational coordinates (u, v) of z."""
    n = norm(den); w = mul(z_num, conj(den))
    return Fraction(w[0], n), Fraction(w[1], n)
def e_add(z_num, den=ONE):
    """paper's e(z) = exp(2 pi i v) for z = u + v omega."""
    u, v = ecoord(z_num, den)
    return cmath.exp(2j * math.pi * float(v - math.floor(v)))
def ebreve(z_num, den=ONE):
    """DR's breve-e(z) = exp(2 pi i (2u - v))."""
    u, v = ecoord(z_num, den)
    t = 2 * u - v
    return cmath.exp(2j * math.pi * float(t - math.floor(t)))
def alpha(x): z = cv(x); return z / abs(z)


def gamma_j(n, j):
    """normalized Gauss sum gamma_j(n) = N(n)^{-1/2} sum_{x mod n} chi_n(x)^j e(x/n), by brute force."""
    s = 0
    for x in residues(n):
        c = chi_c(n, x, j)
        if c != 0: s += c * e_add(x, n)
    return s / math.sqrt(norm(n))


def primary_primes(maxN, include_inert=True):
    out = []
    for q in sympy.primerange(5, maxN + 1):
        if q % 3 == 1:
            pi = split_prime(q); out.append(primary_assoc(pi)); out.append(primary_assoc(conj(pi)))
        elif include_inert and q * q <= maxN:
            out.append((-q, 0))
    out.sort(key=norm)
    return out


# ---------- cubic residue symbol by reciprocity (for very large arguments) ----------
def cubic_supp(d):
    """DR (1.5): for primary d == 1 + a2 lambda^2 + a3 lambda^3 (mod 9), a2,a3 in {-1,0,1},
    return (a2, a3), so (omega/d)_3 = omega^{a2}, (lambda/d)_3 = omega^{-a3}."""
    assert is_primary(d)
    L2 = pw(LAM, 2); L3 = pw(LAM, 3); NINE = (9, 0)
    for a2 in (-1, 0, 1):
        for a3 in (-1, 0, 1):
            t = add(ONE, add(mul((a2, 0), L2), mul((a3, 0), L3)))
            if cong(d, t, NINE): return a2, a3
    raise ValueError(d)
def cubic_sym_recip(x, d):
    """(x/d)_3 as exponent mod 3 of omega (None if not coprime), d primary, via cubic
    reciprocity DR (1.4) and supplements DR (1.5).  Used only for huge arguments; validated
    against the direct definition on small cases in appA2_arith.py."""
    assert is_primary(d)
    k = 0
    while True:
        if norm(d) == 1: return k % 3
        x = rmod(x, d)
        if is_zero(x): return None
        # strip lambda powers and the unit
        a2, a3 = cubic_supp(d)
        while divides(LAM, x):
            x = exdiv(x, LAM); k += -a3
        # x = u * x' with x' primary;  u = zeta6^e: -1 is a cube, omega^m contributes a2*m
        xp = primary_assoc(x); u = exdiv(x, xp); e = unit_exponent(u)
        # zeta6^e = (-1)^e * omega^{?}: zeta6 = -omega^2 -> zeta6^e = (-1)^e omega^{2e}
        k += a2 * (2 * e)
        # (x'/d) = (d/x')  (both primary)
        x, d = d, xp


# ---------- fast exact-phase additive characters for x/n with x, n in O ----------
TWO_PI_I = 2j * math.pi
def e_xn(x, n):
    """e(x/n) = exp(2 pi i v), x/n = u + v omega; computed with integers."""
    N = norm(n); w = mul(x, conj(n))
    return cmath.exp(TWO_PI_I * ((w[1] % N) / N))
def eb_xn(x, n):
    """breve-e(x/n) = exp(2 pi i (2u - v))."""
    N = norm(n); w = mul(x, conj(n))
    return cmath.exp(TWO_PI_I * (((2 * w[0] - w[1]) % N) / N))


_fac_cache = {}
def fac(n):
    if n not in _fac_cache: _fac_cache[n] = factor(n)
    return _fac_cache[n]
def chi_fast(n, x):
    """chi_n(x) exponent mod 6 or None, using cached factorization of n."""
    if n == ONE: return 0
    k = 0
    for p, e in fac(n)[1].items():
        s = PR(p).sym6(x)
        if s is None: return None
        k += e * s
    return k % 6
def gauss(n, j):
    """gamma_j(n) by brute force over x mod n (n primary, coprime to 6)."""
    s = 0
    for x in residues(n):
        k = chi_fast(n, x)
        if k is None: continue
        s += ZETA6 ** ((j * k) % 6) * e_xn(x, n)
    return s / math.sqrt(norm(n))
