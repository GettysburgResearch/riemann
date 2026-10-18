"""Exact integral ideals of Z[w], w^2+w+1=0; no numerical arithmetic.

An ideal is its column Hermite normal form (a,b,c), with basis
(a,0),(b,c), a,c>0 and 0<=b<a. Distinct ideals of the same norm stay
distinct. The enumeration is independent of the rational Euler algorithm.
"""
from functools import lru_cache
from array import array
from itertools import combinations
from math import gcd, isqrt

UNIT = (1, 0, 1)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def norm(ideal):
    return ideal[0] * ideal[2]


def member(ideal, vector):
    a, b, c = ideal
    x, y = vector
    return y % c == 0 and (x - b * (y // c)) % a == 0


def subset(left, right):
    a, b, c = left
    return member(right, (a, 0)) and member(right, (b, c))


def valid(ideal):
    a, b, c = ideal
    return (a > 0 and c > 0 and 0 <= b < a
            and member(ideal, (0, a)) and member(ideal, (-c, b-c)))


def egcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def hnf(vectors):
    det = 0
    for (x, y), (u, v) in combinations(vectors, 2):
        det = gcd(det, x*v-y*u)
    require(det > 0, 'Rank-two lattice required.')
    c = x_at_c = 0
    for x, y in vectors:
        new_c, s, t = egcd(c, y)
        x_at_c = s*x_at_c+t*x
        c = new_c
    require(c > 0 and det % c == 0, 'Invalid HNF index.')
    a = det // c
    return a, x_at_c % a, c


def element_product(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


@lru_cache(None)
def multiply(left, right):
    a, b, c = left
    d, e, f = right
    out = hnf(tuple(element_product(x, y)
                    for x in ((a, 0), (b, c))
                    for y in ((d, 0), (e, f))))
    require(valid(out), 'Product is not an ideal.')
    require(norm(out) == norm(left)*norm(right), 'Product index changed.')
    return out


def power(ideal, exponent):
    require(exponent >= 0, 'Nonnegative exponent required.')
    result = UNIT
    while exponent:
        if exponent & 1:
            result = multiply(result, ideal)
        exponent //= 2
        if exponent:
            ideal = multiply(ideal, ideal)
    return result


@lru_cache(None)
def ideals_up_to(limit):
    require(isinstance(limit, int) and limit >= 1, 'Positive integer cap required.')
    out = []
    # Stability under multiplication by w is equivalent to a=c*A,b=c*B,
    # 0<=B<A, and B^2-B+1=0 modulo A. This lists ALL HNF ideals.
    roots = {a: tuple(b for b in range(a) if (b*b-b+1) % a == 0)
             for a in range(1, limit+1)}
    for c in range(1, isqrt(limit)+1):
        for a in range(1, limit//(c*c)+1):
            out.extend((c*a, c*b, c) for b in roots[a])
    return tuple(sorted(out, key=lambda i: (norm(i), i)))


@lru_cache(None)
def integer_factors(n):
    require(n >= 1, 'Positive integer required.')
    factors = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            factors.append((p, e))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


@lru_cache(None)
def primes_over(p):
    require(integer_factors(p) == ((p, 1),), 'Rational prime required.')
    if p % 3 == 2:
        return ((p, 0, p),)
    return tuple((p, b, 1) for b in range(p) if (b*b-b+1) % p == 0)


@lru_cache(None)
def factor(ideal):
    require(valid(ideal), 'Invalid ideal.')
    result = []
    for p, rational_exponent in integer_factors(norm(ideal)):
        for prime in primes_over(p):
            e, p_power = 0, prime
            while norm(p_power) <= norm(ideal) and subset(ideal, p_power):
                e += 1
                p_power = multiply(p_power, prime)
            if e:
                result.append((prime, e))
    reconstructed = UNIT
    for prime, exponent in result:
        reconstructed = multiply(reconstructed, power(prime, exponent))
    require(reconstructed == ideal, 'Factorization did not reconstruct the ideal.')
    return tuple(result)


def mobius(ideal):
    factors = factor(ideal)
    return 0 if any(e > 1 for _, e in factors) else (-1)**len(factors)


def exterior(ideal):
    """S consists of the prime ideals above 2 and 3."""
    return gcd(norm(ideal), 6) == 1


def coprime(left, right):
    return not ({p for p, _ in factor(left)} & {p for p, _ in factor(right)})


def mask_signature(ideal):
    """For principal rows: number of excluded prime ideals over each p.

    A single split ideal excludes ONE local factor, rather than both ideals
    of its rational norm. Exponents in the masking ideal are immaterial.
    """
    counts = {}
    for prime, _ in factor(ideal):
        p = integer_factors(norm(prime))[0][0]
        counts[p] = counts.get(p, 0)+1
    return tuple(sorted(counts.items()))


def norm_mobius_coefficients(limit, signature=(), *, excluded=(2, 3), compact=False):
    """Independent rational Euler recurrence for masked ideal Mobius sums.

    This never calls HNF enumeration or ideal factorization. Array entries
    are sums over ALL ideals of a given norm, including conjugate ideals.
    """
    mask = dict(signature)
    require(isinstance(limit, int) and limit >= 1, 'Positive integer cap required.')
    out = array('i', [0])*(limit+1) if compact else [0]*(limit+1)
    out[1] = 1
    smallest = array('I', range(limit+1)) if compact else list(range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if smallest[p] == p:
            for n in range(p*p, limit+1, p):
                if smallest[n] == n:
                    smallest[n] = p
    for n in range(2, limit+1):
        p = smallest[n]
        m, e = n, 0
        while m % p == 0:
            m //= p
            e += 1
        if p in excluded:
            local = 0
        elif p == 3:
            local = -1 if e == 1 and not mask.get(p) else 0
        elif p % 3 == 2:
            local = -1 if e == 2 and not mask.get(p) else 0
        else:
            remaining = 2-mask.get(p, 0)
            require(0 <= remaining <= 2, 'Invalid split-prime mask.')
            local = (-remaining if e == 1 else
                     1 if e == 2 and remaining == 2 else 0)
        out[n] = out[m]*local
    return out


def mask_coefficients_from_principal(principal, signature):
    """Exact Euler-deletion recurrence, reusing one complete primitive source.

    Dividing a norm generating series by (1-X^q) means
    out[n] = in[n] + out[n/q] at multiples of q, in ascending n.
    Each actual excluded prime ideal is applied exactly once; two split
    conjugates have the same q but require TWO separate inverse factors.
    The caller's array is never changed.
    """
    require(len(principal) >= 2, 'A complete source including norm one is required.')
    out = principal[:]
    for p, count in signature:
        require(p not in (2, 3) and integer_factors(p) == ((p, 1),), 'Exterior prime mask required.')
        split = p % 3 == 1
        require(1 <= count <= (2 if split else 1), 'Wrong number of excluded prime ideals.')
        q = p if split else p*p
        for _ in range(count):
            for n in range(q, len(out), q):
                out[n] += out[n//q]
    return out
