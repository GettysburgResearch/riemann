from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from json import dumps
from math import comb

NMAX = 96


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def v2(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def a2(n):
    return v2(n) + 1


def lin_log(n):
    return {p: Fraction(e) for p, e in factor(n).items()}


def lin_add(a, b, ca=1, cb=1):
    out = defaultdict(Fraction)
    for k, v in a.items():
        out[k] += ca * v
    for k, v in b.items():
        out[k] += cb * v
    return {k: v for k, v in out.items() if v}


def quad_outer(a, b, coefficient=1):
    out = defaultdict(Fraction)
    for p, x in a.items():
        for q, y in b.items():
            out[tuple(sorted((p, q)))] += coefficient * x * y
    return {k: v for k, v in out.items() if v}


def quad_add(*terms):
    out = defaultdict(Fraction)
    for term, coefficient in terms:
        for k, v in term.items():
            out[k] += coefficient * v
    return {k: v for k, v in out.items() if v}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def lambda2(n):
    fac = factor(n)
    if len(fac) != 1:
        return {}
    p = next(iter(fac))
    return {2: Fraction(2)} if p == 2 else {p: Fraction(1)}


def c2(n):
    out = defaultdict(Fraction)
    for key, value in quad_outer(lambda2(n), lin_log(n)).items():
        out[key] += value
    for d in divisors(n):
        for key, value in quad_outer(lambda2(d), lambda2(n // d)).items():
            out[key] += value
    return {k: v for k, v in out.items() if v}


def chi(n, q, j):
    return n // q - j // q - (n - j) // q


def p_direct(n, j):
    out = {}
    for q in range(1, n + 1):
        c = chi(n, q, j)
        if c:
            out = lin_add(out, lambda2(q), 1, c)
    return out


def s_direct(n, j):
    out = defaultdict(Fraction)
    for q in range(1, n + 1):
        c = chi(n, q, j)
        if c:
            for key, value in c2(q).items():
                out[key] += c * value
    return {k: v for k, v in out.items() if v}


def h1(n):
    out = {}
    for m in range(n // 2 + 1, n + 1):
        out = lin_add(out, lin_log(m), 1, a2(m))
    return out


def h2(n):
    out = defaultdict(Fraction)
    for m in range(n // 2 + 1, n + 1):
        for key, value in quad_outer(lin_log(m), lin_log(m), a2(m)).items():
            out[key] += value
    return {k: v for k, v in out.items() if v}


def tau(n, t):
    while 2 * t <= n:
        t *= 2
    return t


def square(linear):
    return quad_outer(linear, linear)


def reserve_poly(n, j):
    return quad_add((square(p_direct(n, j)), 1), (s_direct(n, j), -1))


def qterm(a, b, coefficient=1):
    return quad_outer(a, b, coefficient)


checks = {
    "inverse_convolution": 0,
    "top_half_rows": 0,
    "dyadic_lifts": 0,
    "paired_order": 0,
    "endpoint_formula": 0,
    "j2_formula": 0,
    "finite_exception_formulas": 0,
    "binomial_threshold": 0,
}

# b2 * a2 = epsilon.
mu = [0] * (NMAX + 1)
mu[1] = 1
primes = []
composite = [False] * (NMAX + 1)
for i in range(2, NMAX + 1):
    if not composite[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        if i * p > NMAX:
            break
        composite[i * p] = True
        if i % p == 0:
            mu[i * p] = 0
            break
        mu[i * p] = -mu[i]

b2 = [0] * (NMAX + 1)
for n in range(1, NMAX + 1):
    b2[n] = mu[n] - (mu[n // 2] if n % 2 == 0 else 0)

for n in range(1, NMAX + 1):
    value = sum(b2[d] * a2(n // d) for d in divisors(n))
    assert value == (1 if n == 1 else 0), (n, value)
    checks["inverse_convolution"] += 1

# Direct generalized-prime/Selberg rows equal the top-half formulas.
for n in range(2, NMAX + 1):
    for j in range(n + 1):
        p_expected = lin_add(lin_add(h1(n), h1(j), 1, -1), h1(n - j), 1, -1)
        s_expected = quad_add((h2(n), 1), (h2(j), -1), (h2(n - j), -1))
        assert p_direct(n, j) == p_expected, (n, j, "P")
        assert s_direct(n, j) == s_expected, (n, j, "S")
        checks["top_half_rows"] += 1

# Top-half dyadic-lift multiset, including multiplicity a2(m).
for n in range(1, NMAX + 1):
    lhs = []
    for m in range(n // 2 + 1, n + 1):
        lhs.extend([m] * a2(m))
    rhs = [tau(n, t) for t in range(1, n + 1)]
    assert sorted(lhs) == sorted(rhs), n
    checks["dyadic_lifts"] += 1

# The paired numerator lift always dominates the matched denominator lift.
for n in range(2, NMAX + 1):
    for j in range(1, n // 2 + 1):
        k = n - j
        for t in range(1, k + 1):
            assert tau(n, t) >= tau(k, t)
            checks["paired_order"] += 1
        for r in range(1, j + 1):
            assert tau(n, k + r) > n / 2 >= tau(j, r)
            checks["paired_order"] += 1

# Endpoint-neighbor reserve: r(r+1) log(2)^2.
l2 = {2: Fraction(1)}
for n in range(2, NMAX + 1):
    expected = qterm(l2, l2, v2(n) * (v2(n) + 1))
    assert reserve_poly(n, 1) == expected, n
    checks["endpoint_formula"] += 1

# j=2 formula for every n.
for n in range(4, NMAX + 1):
    e = n if n % 2 == 0 else n - 1
    o = n - 1 if n % 2 == 0 else n
    r = v2(e)
    le, lo = lin_log(e), lin_log(o)
    expected = quad_add(
        (qterm(le, lo, 2), 1),
        (qterm(le, l2, -4), 1),
        (qterm(l2, lo, 2 * (r - 2)), 1),
        (qterm(l2, l2, r * r - 3 * r + 6), 1),
    )
    assert reserve_poly(n, 2) == expected, n
    checks["j2_formula"] += 1

# Four finite interior formulas from the proof.
finite = {
    (6, 3): quad_add(
        (qterm(l2, l2, 6), 1),
        (qterm(l2, {3: Fraction(1)}, -4), 1),
        (qterm(l2, {5: Fraction(1)}, 8), 1),
    ),
    (7, 3): quad_add(
        (qterm({5: Fraction(1)}, {7: Fraction(1)}, 2), 1),
        (qterm(l2, {3: Fraction(1)}, -4), 1),
    ),
    (8, 3): quad_add(
        (qterm(l2, l2, 12), 1),
        (qterm(l2, {3: Fraction(1)}, -4), 1),
        (qterm(l2, {7: Fraction(1)}, 12), 1),
    ),
    (8, 4): quad_add(
        (qterm(l2, {5: Fraction(1)}, 4), 1),
        (qterm(l2, {7: Fraction(1)}, 4), 1),
        (qterm({5: Fraction(1)}, {7: Fraction(1)}, 2), 1),
        (qterm(l2, l2, -10), 1),
        (qterm(l2, {3: Fraction(1)}, -4), 1),
    ),
}
for key, expected in finite.items():
    assert reserve_poly(*key) == expected, key
    checks["finite_exception_formulas"] += 1

# Exact integer threshold used by the general interior proof.
for n in range(9, 10_000):
    assert comb(n, 3) >= n * n
    checks["binomial_threshold"] += 1

payload = {
    "verdict": "PASS_EXACT_TWO_CONTACT_SELBERG_RESERVE_ALGEBRA",
    "checks": checks,
    "NMAX": NMAX,
}
encoded = dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["proof_object_sha256"] = sha256(encoded).hexdigest()
print(dumps(payload, sort_keys=True, indent=2))
