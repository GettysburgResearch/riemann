"""kintali_lemma3_common.py -- exact arithmetic in O = Z[omega] for the Lemma 3 / App. B review.

Elements are integer pairs (a, b) <-> a + b*omega, omega = exp(2 pi i/3), lambda = 1 + 2 omega.
Conventions (Kintali App. B and Dunn-Radziwill arXiv:2109.07463v3, Sec. 2-5):
  e(z)    = exp(2 pi i Tr(z/lambda)) = exp(4 pi i Im z / sqrt 3)     [Kintali Sec. 2.1]
  ech(z)  = exp(2 pi i (z + conj z)) = exp(4 pi i Re z) = e(lambda z) [DR "check e"]
  (x/p)_3 = cube root of unity == x^{(Np-1)/3} mod p  (p prime, not above 3)  [DR Sec. 2]
  chi_p(x) = sixth root of unity == x^{(Np-1)/6} mod p                        [Kintali Sec. 2.1]
  "primary" = congruent to 1 mod 3.
Only exact integer arithmetic is used for symbols; exponentials are floating point.
"""
import cmath
import math
from fractions import Fraction

import sympy

OMEGA = complex(-0.5, math.sqrt(3) / 2)
LAM = (1, 2)                       # lambda = 1 + 2 omega, lambda^2 = -3
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta^k, zeta = 1 + omega = e^{i pi/3}


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def neg(x):
    return (-x[0], -x[1])


def conj(x):
    return (x[0] - x[1], -x[1])


def norm(x):
    return x[0] * x[0] - x[0] * x[1] + x[1] * x[1]


def power(x, k):
    r = (1, 0)
    for _ in range(k):
        r = mul(r, x)
    return r


def to_c(x):
    return x[0] + x[1] * OMEGA


def is_zero(x):
    return x[0] == 0 and x[1] == 0


def divides(m, z):
    c, d = mul(z, conj(m))
    n = norm(m)
    return c % n == 0 and d % n == 0


def exact_div(z, m):
    c, d = mul(z, conj(m))
    n = norm(m)
    assert c % n == 0 and d % n == 0, (z, m)
    return (c // n, d // n)


def round_div(z, m):
    c, d = mul(z, conj(m))
    n = norm(m)
    return ((2 * c + n) // (2 * n), (2 * d + n) // (2 * n))


def reduce_mod(z, m):
    q = round_div(z, m)
    return sub(z, mul(q, m))


def congruent(x, y, m):
    return divides(m, sub(x, y))


def is_primary(x):
    return x[0] % 3 == 1 and x[1] % 3 == 0


def primary(x):
    """(unit u, primary y) with x = u*y, for x prime to lambda."""
    for k, u in enumerate(UNITS):
        y = mul(power(UNITS[(6 - k) % 6], 1), x)   # u^{-1} x
        if is_primary(y):
            return u, y
    raise ValueError(x)


def egcd(x, y):
    """Bezout in the Euclidean ring O: returns (g, s, t) with s*x + t*y = g."""
    r0, r1 = x, y
    s0, s1 = (1, 0), (0, 0)
    t0, t1 = (0, 0), (1, 0)
    while not is_zero(r1):
        q = round_div(r0, r1)
        r0, r1 = r1, sub(r0, mul(q, r1))
        s0, s1 = s1, sub(s0, mul(q, s1))
        t0, t1 = t1, sub(t0, mul(q, t1))
    return r0, s0, t0


def inv_mod(x, m):
    g, s, _ = egcd(x, m)
    assert norm(g) == 1, ("not invertible", x, m)
    # g is a unit; s*x = g mod m, so x^{-1} = s * g^{-1}
    ginv = conj(g)      # for a unit, conj = inverse
    return reduce_mod(mul(s, ginv), m)


def crt(residues):
    """residues: list of (r_i, m_i) with pairwise coprime m_i; returns (x, M)."""
    x, M = (0, 0), (1, 0)
    for r, m in residues:
        # x' = x + M * ((r - x) * M^{-1} mod m)
        t = mul(sub(r, x), inv_mod(M, m))
        t = reduce_mod(t, m)
        x = add(x, mul(M, t))
        M = mul(M, m)
        x = reduce_mod(x, M)
    return x, M


def powmod(z, e, m):
    r, b = (1, 0), reduce_mod(z, m)
    while e:
        if e & 1:
            r = reduce_mod(mul(r, b), m)
        b = reduce_mod(mul(b, b), m)
        e >>= 1
    return r


def lam_val(x):
    """lambda-adic valuation and the lambda-free part."""
    v = 0
    while divides(LAM, x):
        x = exact_div(x, LAM)
        v += 1
    return v, x


_PRIME_ABOVE = {}


def primes_above(p):
    """Prime elements of O above the rational prime p (primary generators when p != 3)."""
    if p in _PRIME_ABOVE:
        return _PRIME_ABOVE[p]
    if p == 3:
        out = [LAM]
    elif p % 3 == 2:
        out = [primary((p, 0))[1]]
    else:
        s3 = sympy.sqrt_mod(-3 % p, p)
        r = ((-1 + s3) * pow(2, -1, p)) % p        # r^2 + r + 1 = 0 mod p
        found = egcd((p, 0), (-r, 1))[0]           # gcd(p, w - r): a prime of norm p
        assert norm(found) == p, (p, found)
        pi = primary(found)[1]
        pib = primary(conj(found))[1]
        out = [pi, pib] if pi != pib else [pi]
    _PRIME_ABOVE[p] = out
    return out


def factor(x):
    """Factor x != 0: returns (unit-and-leftover u, list of (prime element, exponent)).
    Primes above p != 3 are primary; lambda is used above 3. x = u * prod p^e."""
    assert not is_zero(x)
    fac = []
    for p, _ in sympy.factorint(norm(x)).items():
        for pi in primes_above(p):
            e = 0
            while divides(pi, x):
                x = exact_div(x, pi)
                e += 1
            if e:
                fac.append((pi, e))
    assert norm(x) == 1, x
    return x, fac


def sextic_code(x, p):
    """chi_p(x) as code k (value zeta^k) or None if p | x; p a prime element not above 3."""
    if divides(p, x):
        return None
    t = powmod(x, (norm(p) - 1) // 6, p) if norm(p) % 6 == 1 else None
    if t is None:
        raise ValueError("sextic symbol needs N p = 1 mod 6", p)
    for k, z in enumerate(UNITS):
        if congruent(t, z, p):
            return k
    raise RuntimeError


def cubic_code(x, p):
    """(x/p)_3 as k in {0,1,2} (value omega^k) or None if p | x; p prime element not above 3.
    Valid also for the prime 2 (N = 4)."""
    if divides(p, x):
        return None
    t = powmod(x, (norm(p) - 1) // 3, p)
    for k, z in enumerate([(1, 0), (0, 1), (-1, -1)]):
        if congruent(t, z, p):
            return k
    raise RuntimeError((x, p, t))


def cubic_symbol(x, A):
    """(x/A)_3 for A prime to 3 (any generator; symbol depends only on the ideal), as code mod 3,
    None if not coprime. Multiplicative in A via prime factorization."""
    _, fac = factor(A)
    s = 0
    for p, e in fac:
        assert p != LAM, "A must be prime to 3"
        k = cubic_code(x, p)
        if k is None:
            return None
        s += e * k
    return s % 3


def omega_pow(k):
    return cmath.exp(2j * math.pi * k / 3)


def zeta_pow(k):
    return cmath.exp(1j * math.pi * k / 3)


def ech(z):
    """DR check-e of a complex number z: exp(4 pi i Re z)."""
    return cmath.exp(4j * math.pi * z.real)


def e_k(z):
    """Kintali e(z) of a complex number z: exp(4 pi i Im z / sqrt 3)."""
    return cmath.exp(4j * math.pi * z.imag / math.sqrt(3))


def frac_e_coord(alpha, beta):
    """For z = alpha/beta (alpha, beta in O), the omega-coordinate of z as an exact Fraction;
    e(z) = exp(2 pi i * that)."""
    c, d = mul(alpha, conj(beta))
    return Fraction(d, norm(beta))


def frac_ech_coord(alpha, beta):
    """For z = alpha/beta, the real number Tr(z) = z + conj z as an exact Fraction;
    ech(z) = exp(2 pi i * that). Tr(a + b w) = 2a - b."""
    c, d = mul(alpha, conj(beta))
    return Fraction(2 * c - d, norm(beta))


def residues(n):
    """Complete residue system of O/nO (HNF of the lattice n*O in the basis 1, omega)."""
    v1, v2 = n, mul(n, (0, 1))
    a1, b1 = v1
    a2, b2 = v2
    N = abs(a1 * b2 - a2 * b1)
    g = math.gcd(b1, b2)
    d1 = N // g
    return [(i, j) for j in range(g) for i in range(d1)]


def lattice(X):
    """All nonzero (a, b) with N(a + b w) <= X."""
    out = []
    bmax = int(2 * math.sqrt(X / 3)) + 2
    for b in range(-bmax, bmax + 1):
        disc = X - 0.75 * b * b
        if disc < 0:
            continue
        lo = int(math.floor(b / 2 - math.sqrt(disc))) - 1
        hi = int(math.ceil(b / 2 + math.sqrt(disc))) + 1
        for a in range(lo, hi + 1):
            n = a * a - a * b + b * b
            if 0 < n <= X:
                out.append((a, b))
    return out


def primary_primes_upto(X, include_two=False):
    """Primary prime elements with norm <= X, prime to 6 (plus -2 if include_two)."""
    out = []
    for p in sympy.primerange(2, X + 1):
        if p == 3:
            continue
        if p == 2:
            if include_two and 4 <= X:
                out.append(primary((2, 0))[1])
            continue
        if p % 3 == 1:
            out += primes_above(p)
        elif p * p <= X:
            out += primes_above(p)
    return sorted(out, key=norm)
