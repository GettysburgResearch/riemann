"""
eisenstein.py -- arithmetic in O = Z[omega], omega = exp(2 pi i / 3).

Shared helpers for the EMPIRICAL sanity checks of the arithmetic core of
"The Quasi-Riemann Hypothesis" (OpenAI, October 5, 2026).  Nothing here is a
proof of anything; it only implements the paper's conventions so that the
identities of Lemma lem:arithmetic and the mean square (eq:ms) can be
evaluated numerically for small norms.

Conventions (paper, Sections 1-3 and Appendix app:gauss-identities)
-------------------------------------------------------------------
* An element a + b*omega is stored as the integer pair (a, b);
  omega^2 = -1 - omega, so (a, b)(c, d) = (ac - bd, ad + bc - bd).
* N(a + b omega) = a^2 - ab + b^2 = |a + b omega|^2.
* "primary" = congruent to 1 mod 3O, i.e. a = 1 (mod 3) and b = 0 (mod 3).
  Every ideal prime to 3 has exactly one primary generator.
* Prime ideals prime to 6 (the paper's S = {(2), (lambda)}, lambda = 1+2 omega):
    split:  pi = a + b omega primary with N(pi) = p prime, p = 1 (mod 3);
            O/pi = F_p via omega -> r := -a/b (mod p).
    inert:  primary generator -q, q prime, q = 2 (mod 3), q != 2;
            N = q^2 and O/q = F_q[omega] = F_{q^2}.
* chi_p(u) = (u/p)_6 is the sixth root of unity congruent to
  u^{(N(p)-1)/6} mod p, and 0 if p | u.  Values are encoded as uint8
  "codes": k in {0..5} means zeta^k with zeta = 1 + omega = exp(i pi/3),
  and ZERO (= 32) means the value 0.  For squarefree n = p_1 ... p_k
  (k <= 5 in all ranges used here), chi_n = prod chi_{p_i}, i.e. the codes
  are added; a sum >= ZERO means chi_n(u) = 0, otherwise the value is
  zeta^(sum mod 6).  VALUE[code_sum] turns a code sum into a complex number.
* e(z) = exp(4 pi i Im(z)/sqrt 3).  If z = (c + d omega)/M with c, d, M
  integers then Im z = d sqrt(3)/(2M) and e(z) = exp(2 pi i d / M).
"""

import math

import numpy as np

ZERO = 32                      # code for chi = 0
MAX_FACTORS = 5                # 5*5 < ZERO and 5*ZERO < 256 (uint8 safe)
ZETA = np.exp(1j * np.pi * np.arange(6) / 3)        # zeta^k, zeta = e^{i pi/3}
# zeta^k as elements of O: 1, 1+w, w, -1, -1-w, -w
ZETA_O = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]

VALUE = np.zeros(256, dtype=np.complex128)          # code sum -> complex value
for _c in range(ZERO):
    VALUE[_c] = ZETA[_c % 6]
NEG = np.full(256, ZERO, dtype=np.uint8)            # code of the conjugate
NEG[:6] = (6 - np.arange(6)) % 6

OMEGA = complex(-0.5, math.sqrt(3) / 2)


# --------------------------------------------------------------------------
# element arithmetic
# --------------------------------------------------------------------------
def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def conj(x):
    a, b = x
    return (a - b, -b)


def norm(x):
    a, b = x
    return a * a - a * b + b * b


def to_complex(x):
    return x[0] + x[1] * OMEGA


def is_primary(x):
    return x[0] % 3 == 1 and x[1] % 3 == 0


def power(x, k):
    r = (1, 0)
    for _ in range(k):
        r = mul(r, x)
    return r


def divides_exact(m, z):
    """True iff m | z in O (exact integer test: z * conj(m) = 0 mod N(m))."""
    c, d = mul(z, conj(m))
    nm = norm(m)
    return c % nm == 0 and d % nm == 0


def reduce_mod(z, m):
    """Some representative of z mod m (coefficientwise rounding of z/m)."""
    c, d = mul(z, conj(m))
    nm = norm(m)
    q = ((2 * c + nm) // (2 * nm), (2 * d + nm) // (2 * nm))
    qm = mul(q, m)
    return (z[0] - qm[0], z[1] - qm[1])


def powmod(z, e, m):
    """z^e mod m in O, exact integer arithmetic (independent of the tables)."""
    result = (1, 0)
    base = reduce_mod(z, m)
    while e:
        if e & 1:
            result = reduce_mod(mul(result, base), m)
        base = reduce_mod(mul(base, base), m)
        e >>= 1
    return result


def sextic_symbol_exact(u, p):
    """(u/p)_6 for a prime p (element) by exact computation in O.

    Returns the code k (value zeta^k) or ZERO.  Slow; used only to validate
    the fast residue-field tables."""
    if divides_exact(p, u):
        return ZERO
    t = powmod(u, (norm(p) - 1) // 6, p)
    hits = [k for k in range(6)
            if divides_exact(p, (t[0] - ZETA_O[k][0], t[1] - ZETA_O[k][1]))]
    assert len(hits) == 1, (u, p, t, hits)
    return hits[0]


# --------------------------------------------------------------------------
# rational helpers
# --------------------------------------------------------------------------
def prime_sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def prime_factors(n):
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p):
    fac = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // l, p) != 1 for l in fac):
            return g
    raise ValueError(p)


# --------------------------------------------------------------------------
# prime ideals and residue-symbol tables
# --------------------------------------------------------------------------
class PrimeIdeal:
    """A prime ideal prime to 6, with its primary generator and a table of
    sextic-symbol codes on its residue field."""

    __slots__ = ("gen", "N", "p", "kind", "r", "table", "neg")

    def __repr__(self):
        return f"PrimeIdeal(gen={self.gen}, N={self.N}, {self.kind})"

    def codes(self, x, y):
        """Codes of chi_p(x + y*omega) for int64 arrays x, y."""
        if self.kind == "split":
            idx = np.mod(x + y * self.r, self.p)
        else:
            q = self.p
            idx = np.mod(x, q) * q + np.mod(y, q)
        c = self.table[idx]
        return NEG[c] if self.neg else c


def _split_table(p, r):
    """codes[x] for x in F_p, with omega -> r, i.e. x^{(p-1)/6} = (1+r)^code."""
    g = primitive_root(p)
    B = math.isqrt(p) + 1
    small = np.empty(B, dtype=np.int64)
    small[0] = 1
    for i in range(1, B):
        small[i] = small[i - 1] * g % p
    gB = pow(g, B, p)
    nb = (p - 1 + B - 1) // B
    big = np.empty(nb, dtype=np.int64)
    big[0] = 1
    for i in range(1, nb):
        big[i] = big[i - 1] * gB % p
    pw = ((big[:, None] * small[None, :]) % p).ravel()[: p - 1]   # g^k
    h = pow(g, (p - 1) // 6, p)
    t = 1 if h == (1 + r) % p else 5
    assert pow(h, t, p) == (1 + r) % p
    table = np.empty(p, dtype=np.uint8)
    table[pw] = ((np.arange(p - 1) % 6) * t) % 6
    table[0] = ZERO
    return table


def _f_mul(x, y, q):
    """Multiplication in F_q[omega] for pairs of arrays/ints."""
    a, b = x
    c, d = y
    return ((a * c - b * d) % q, (a * d + b * c - b * d) % q)


def _f_pow(x, e, q):
    r = (1, 0)
    while e:
        if e & 1:
            r = _f_mul(r, x, q)
        x = _f_mul(x, x, q)
        e >>= 1
    return r


def _inert_table(q):
    """codes[a*q+b] for a + b omega in F_{q^2} = F_q[omega]."""
    order = q * q - 1
    fac = prime_factors(order)
    gen = None
    for a in range(q):
        for b in range(1, q):
            if all(_f_pow((a, b), order // l, q) != (1, 0) for l in fac):
                gen = (a, b)
                break
        if gen:
            break
    B = math.isqrt(order) + 1
    sa = np.empty(B, dtype=np.int64)
    sb = np.empty(B, dtype=np.int64)
    cur = (1, 0)
    for i in range(B):
        sa[i], sb[i] = cur
        cur = _f_mul(cur, gen, q)
    gB = _f_pow(gen, B, q)
    nb = (order + B - 1) // B
    ba = np.empty(nb, dtype=np.int64)
    bb = np.empty(nb, dtype=np.int64)
    cur = (1, 0)
    for i in range(nb):
        ba[i], bb[i] = cur
        cur = _f_mul(cur, gB, q)
    pa, pb = _f_mul((ba[:, None], bb[:, None]), (sa[None, :], sb[None, :]), q)
    pa = pa.ravel()[:order]
    pb = pb.ravel()[:order]
    h = _f_pow(gen, order // 6, q)
    t = 1 if h == (1, 1) else 5           # (1, 1) = 1 + omega = zeta
    assert _f_pow(h, t, q) == (1, 1)
    table = np.empty(q * q, dtype=np.uint8)
    table[pa * q + pb] = ((np.arange(order) % 6) * t) % 6
    table[0] = ZERO
    return table


def prime_ideals(X):
    """All prime ideals prime to 6 with norm <= X, sorted by norm.

    Each split rational prime p contributes pi and conj(pi), which share one
    table (the code table of conj(pi) is the negative of that of pi)."""
    isp = prime_sieve(max(X, 10))
    out = []
    # split primes: primary a + b omega with prime norm
    bmax = int(2 * math.sqrt(X / 3)) + 2
    seen = {}          # rational p -> (table, r) of the first pi found
    for b in range(-bmax, bmax + 1):
        if b % 3:
            continue
        # a^2 - ab + b^2 <= X  <=>  (a - b/2)^2 <= X - 3b^2/4
        disc = X - 0.75 * b * b
        if disc < 0:
            continue
        lo = int(math.floor(b / 2 - math.sqrt(disc))) - 1
        hi = int(math.ceil(b / 2 + math.sqrt(disc))) + 1
        for a in range(lo, hi + 1):
            if a % 3 != 1:
                continue
            n = a * a - a * b + b * b
            if n <= X and n > 3 and isp[n]:
                P = PrimeIdeal()
                P.gen, P.N, P.p, P.kind = (a, b), n, n, "split"
                P.r = (-a * pow(b, -1, n)) % n
                if n in seen:                   # this is conj of the first
                    P.table, r0 = seen[n]
                    P.neg = True
                    assert P.r == r0 * r0 % n       # r(conj pi) = r(pi)^2
                else:
                    P.table, P.neg = _split_table(n, P.r), False
                    seen[n] = (P.table, P.r)
                out.append(P)
    # inert primes: -q, q = 2 mod 3, q >= 5
    q = 5
    while q * q <= X:
        if isp[q] and q % 3 == 2:
            P = PrimeIdeal()
            P.gen, P.N, P.p, P.kind = (-q, 0), q * q, q, "inert"
            P.r, P.table, P.neg = None, _inert_table(q), False
            out.append(P)
        q += 1
    out.sort(key=lambda P: (P.N, P.gen))
    return out


def squarefree_primary(primes, X, include_one=False):
    """Squarefree primary n prime to 6 with N(n) <= X.

    Returns a list of (generator, norm, tuple_of_prime_indices); the generator
    is the product of the primary prime generators, hence primary."""
    out = []
    if include_one:
        out.append(((1, 0), 1, ()))

    def rec(start, gen, n, facs):
        for i in range(start, len(primes)):
            P = primes[i]
            if n * P.N > X:
                break
            g2 = mul(gen, P.gen)
            f2 = facs + (i,)
            assert len(f2) <= MAX_FACTORS
            out.append((g2, n * P.N, f2))
            rec(i + 1, g2, n * P.N, f2)

    rec(0, (1, 0), 1, ())
    return out


def nonzero_lattice(H):
    """All nonzero (a, b) with N(a + b omega) <= H, as int64 arrays."""
    bmax = int(2 * math.sqrt(H / 3)) + 2
    A, B = [], []
    for b in range(-bmax, bmax + 1):
        disc = H - 0.75 * b * b
        if disc < 0:
            continue
        lo = int(math.floor(b / 2 - math.sqrt(disc))) - 1
        hi = int(math.ceil(b / 2 + math.sqrt(disc))) + 1
        a = np.arange(lo, hi + 1, dtype=np.int64)
        n = a * a - a * b + b * b
        keep = (n <= H) & (n > 0)
        A.append(a[keep])
        B.append(np.full(keep.sum(), b, dtype=np.int64))
    return np.concatenate(A), np.concatenate(B)


UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # zeta^k


def self_test(primes, n_samples=300, seed=1):
    """Compare the fast tables with exact computation of u^{(N-1)/6} mod p,
    for random u and a sample of primes.  Returns the number of checks."""
    rng = np.random.default_rng(seed)
    checks = 0
    sample = primes if len(primes) <= 60 else (
        primes[:30] + [primes[i] for i in rng.choice(len(primes), 30, replace=False)])
    for P in sample:
        xs = rng.integers(-5 * P.N, 5 * P.N, n_samples)
        ys = rng.integers(-5 * P.N, 5 * P.N, n_samples)
        # include multiples of p, units and small elements
        mp = mul(P.gen, (3, -7))
        xs[:3] = [mp[0], 1, 4]
        ys[:3] = [mp[1], 0, 0]
        fast = P.codes(xs.astype(np.int64), ys.astype(np.int64))
        for x, y, c in zip(xs.tolist(), ys.tolist(), fast.tolist()):
            assert c == sextic_symbol_exact((x, y), P.gen), (P, x, y, c)
            checks += 1
    return checks
