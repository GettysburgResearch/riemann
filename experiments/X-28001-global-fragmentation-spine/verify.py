from fractions import Fraction
from math import comb
import hashlib
from pathlib import Path


def mobius_sieve(n):
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    composite = [False] * (n + 1)
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def children_probabilities(m):
    children = (m // 2, m - m // 2, (m + 2) // 3, m - (m + 2) // 3)
    out = {}
    for child in children:
        out[child] = out.get(child, Fraction(0)) + Fraction(child, 2 * m)
    assert sum(out.values()) == 1
    return out


def producer_from_target(w, X):
    mu = mobius_sieve(X)
    U = [Fraction(0) for _ in range(X + 2)]
    for k in range(1, X + 1):
        if mu[k]:
            for m in range(1, X // k + 1):
                U[m] += mu[k] * w[m * k]
    r = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        r[m] = U[m] - U[m + 1]

    A = [Fraction(0) for _ in range(X + 2)]
    incoming = [Fraction(0) for _ in range(X + 2)]
    for m in range(X, 1, -1):
        A[m] = r[m] + incoming[m]
        children = (m // 2, m - m // 2, (m + 2) // 3, m - (m + 2) // 3)
        for child in children:
            if child >= 2:
                incoming[child] += A[m] / 2
    return A, r


def hitting_probabilities(X, target):
    h = [Fraction(0) for _ in range(X + 1)]
    h[target] = 1
    for m in range(target + 1, X + 1):
        h[m] = sum(probability * h[child]
                   for child, probability in children_probabilities(m).items()
                   if child >= target)
    return h


def first_entrance_source(r, X, n):
    source = [Fraction(0) for _ in range(X + 1)]
    for m in range(1, X + 1):
        source[m] = m * r[m]

    far = [Fraction(0) for _ in range(X + 1)]
    for m in range(2 * n, X + 1):
        far[m] = source[m]
    entrance = [Fraction(0) for _ in range(X + 1)]

    for m in range(X, 2 * n - 1, -1):
        for child, probability in children_probabilities(m).items():
            parcel = far[m] * probability
            if child >= 2 * n:
                far[child] += parcel
            elif child >= n:
                entrance[child] += parcel

    upper = min(2 * n, X + 1)
    return [source[p] + entrance[p] for p in range(n, upper)]


def extraction_tree(n, m):
    assert n >= 2 * m
    k = 1
    while 2 * k <= n // (2 * m):
        k *= 2

    leaves = [n]
    while len(leaves) < k:
        nxt = []
        for parent in leaves:
            left = parent // 2
            right = parent - left
            assert parent <= 4 * left <= 3 * parent
            assert parent <= 4 * right <= 3 * parent
            nxt.extend((left, right))
        leaves = nxt

    assert all(2 * m <= parent <= 4 * m for parent in leaves)
    final = []
    for parent in leaves:
        left = m
        right = parent - m
        assert parent <= 4 * left <= 3 * parent
        assert parent <= 4 * right <= 3 * parent
        final.extend((left, right))
    assert final.count(m) >= k
    assert Fraction(k) >= Fraction(n, 4 * m)
    return k


def log_interval(integer, terms):
    z = Fraction(integer - 1, integer + 1)
    lower = sum((2 * z ** (2 * k + 1) / (2 * k + 1)
                 for k in range(terms)), Fraction(0))
    remainder = (2 * z ** (2 * terms + 1)
                 / ((2 * terms + 1) * (1 - z * z)))
    return lower, lower + remainder


def inverse_sqrt_interval(integer, denominator=10**6):
    candidate = int((integer ** -0.5) * denominator)
    lower = Fraction(candidate, denominator)
    upper = Fraction(candidate + 1, denominator)
    assert lower * lower < Fraction(1, integer) < upper * upper
    return lower, upper


stochastic_rows = 0
for m in range(2, 257):
    assert sum(children_probabilities(m).values()) == 1
    stochastic_rows += 1

green_rows = 0
entrance_rows = 0
for X in (12, 18, 24):
    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, X + 1):
        w[q] = Fraction((X - q) * (q + 1), X + 3)
    A, r = producer_from_target(w, X)
    for n in range(2, X + 1):
        h = hitting_probabilities(X, n)
        rhs = sum(Fraction(m) * r[m] * h[m] for m in range(n, X + 1))
        assert Fraction(n) * A[n] == rhs
        green_rows += 1

        sigma = first_entrance_source(r, X, n)
        transition = Fraction(0)
        for offset, p in enumerate(range(n, min(2 * n, X + 1))):
            transition += sigma[offset] * hitting_probabilities(p, n)[p]
        assert transition == Fraction(n) * A[n]
        entrance_rows += 1

tree_rows = 0
for n in range(4, 257):
    for m in range(1, n // 2 + 1):
        extraction_tree(n, m)
        tree_rows += 1

a2 = inverse_sqrt_interval(2)
a3 = inverse_sqrt_interval(3)
l2 = log_interval(2, 40)
l3 = log_interval(3, 60)
l5 = log_interval(5, 120)
candidates = []
for x2 in a2:
    for x3 in a3:
        for y2 in l2:
            for y3 in l3:
                for L in l5:
                    candidates.append(1 + L / 2
                                      - x2 * (1 + (L - y2) / 2)
                                      - x3 * (1 + (L - y3) / 2))
top_fifth_lower = min(candidates)
assert top_fifth_lower > Fraction(1, 25)

abel_witnesses = []
for order, X, node, expected in (
    (1, 8, 3, Fraction(-1)),
    (2, 60, 11, Fraction(-13, 16)),
    (3, 520, 15, Fraction(-91, 256)),
    (4, 8000, 23, Fraction(-1168054960769, 4096)),
):
    w = [Fraction(0) for _ in range(X + 1)]
    if order == 1:
        w[4] = 1
    else:
        Q = X if order >= 3 else 59
        for q in range(2, Q + 1):
            w[q] = comb(Q - q + order - 1, order - 1)
    A, _ = producer_from_target(w, X)
    assert A[node] == expected, (order, A[node], expected)
    abel_witnesses.append(str(expected))

digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print("PASS_EXACT_GLOBAL_FRAGMENTATION_SPINE_ALGEBRA")
print("stochastic_rows", stochastic_rows)
print("green_rows", green_rows)
print("first_entrance_rows", entrance_rows)
print("quarter_balanced_tree_rows", tree_rows)
print("top_fifth_derivative_lower_gt", "1/25")
print("abel_witnesses", ",".join(abel_witnesses))
print("verifier_sha256", digest)
