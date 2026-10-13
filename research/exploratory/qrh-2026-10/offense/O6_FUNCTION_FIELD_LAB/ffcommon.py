"""ffcommon.py -- exact polynomial arithmetic over F_q (q prime) for the O6 function-field lab.

Polynomials are tuples of coefficients c[0..deg] (low to high), all reduced mod q.
Everything here is exact integer / finite-field arithmetic.
"""
from functools import lru_cache
from itertools import product


def trim(c, q):
    c = [x % q for x in c]
    while c and c[-1] == 0:
        c.pop()
    return tuple(c)


def deg(a):
    return len(a) - 1


def pmul(a, b, q):
    if not a or not b:
        return ()
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] = (r[i + j] + x * y) % q
    return trim(r, q)


def padd(a, b, q):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)], q)


def pmod(a, m, q):
    a = list(a)
    dm = deg(m)
    inv = pow(m[-1], q - 2, q)
    for i in range(len(a) - 1, dm - 1, -1):
        f = a[i] * inv % q
        if f:
            for j in range(dm + 1):
                a[i - dm + j] = (a[i - dm + j] - f * m[j]) % q
    return trim(a[:dm] if dm > 0 else [], q)


def deriv(a, q):
    return trim([i * a[i] for i in range(1, len(a))], q)


def resultant(A, B, q):
    """Res(A,B) = lc(A)^deg B * prod_{A(t)=0} B(t), mod q."""
    if not A or not B:
        return 0
    res = 1
    while True:
        n, m = deg(A), deg(B)
        if n == 0:
            return res * pow(A[0], m, q) % q
        if m == 0:
            return res * pow(B[0], n, q) % q
        R = pmod(B, A, q)
        if not R:
            return 0
        r = deg(R)
        res = res * pow(A[-1], m - r, q) % q
        if (n * r) % 2:
            res = (-res) % q
        A, B = R, A


def monics(k, q):
    for low in product(range(q), repeat=k):
        yield tuple(low) + (1,)


def allpolys_below(M, q):
    """all polynomials of degree < M (including 0)."""
    for c in product(range(q), repeat=M):
        yield trim(c, q)


def primroot(q):
    for g in range(2, q):
        if all(pow(g, (q - 1) // p, q) != 1 for p in set(_factor_int(q - 1))):
            return g


def _factor_int(n):
    f, p = [], 2
    while p * p <= n:
        while n % p == 0:
            f.append(p)
            n //= p
        p += 1
    if n > 1:
        f.append(n)
    return f


def dlog_table(q):
    g = primroot(q)
    t, x = {}, 1
    for e in range(q - 1):
        t[x] = e
        x = x * g % q
    return g, t


def is_squarefree(a, q):
    """gcd(a, a') == 1 (q prime > deg a, so separable <=> squarefree)."""
    return resultant(a, deriv(a, q), q) != 0 if deg(a) > 0 else True


def factor_degrees(a, q, primes_by_deg):
    """list of (prime, multiplicity) by trial division with a supplied prime list."""
    out = []
    rest = a
    for P in primes_by_deg:
        if deg(P) > deg(rest):
            break
        e = 0
        while deg(rest) >= deg(P):
            r = pmod(rest, P, q)
            if r:
                break
            rest = pdiv_exact(rest, P, q)
            e += 1
        if e:
            out.append((P, e))
    if deg(rest) > 0:
        out.append((rest, 1))
    return out


def pdiv_exact(a, m, q):
    a = list(a)
    dm = deg(m)
    inv = pow(m[-1], q - 2, q)
    quo = [0] * (len(a) - dm)
    for i in range(len(a) - 1, dm - 1, -1):
        f = a[i] * inv % q
        quo[i - dm] = f
        if f:
            for j in range(dm + 1):
                a[i - dm + j] = (a[i - dm + j] - f * m[j]) % q
    return trim(quo, q)


def primes_upto(k, q):
    ps = []
    for d in range(1, k + 1):
        for a in monics(d, q):
            if all(pmod(a, P, q) for P in ps if 2 * deg(P) <= d):
                ps.append(a)
    return ps


def mobius(a, q, primes):
    if not is_squarefree(a, q):
        return 0
    f = factor_degrees(a, q, primes)
    return (-1) ** len(f)
