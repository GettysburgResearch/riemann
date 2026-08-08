from fractions import Fraction
from math import comb


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


def producer_from_target(w, X):
    mu = mobius_sieve(X)
    U = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        s = Fraction(0)
        for k in range(1, X // m + 1):
            if mu[k]:
                s += mu[k] * w[m * k]
        U[m] = s

    r = [Fraction(0) for _ in range(X + 2)]
    for m in range(1, X + 1):
        r[m] = U[m] - U[m + 1]

    A = [Fraction(0) for _ in range(X + 2)]
    incoming = [Fraction(0) for _ in range(X + 2)]
    for m in range(X, 1, -1):
        A[m] = r[m] + incoming[m]
        a3 = (m + 2) // 3
        b3 = m - a3
        a2 = m // 2
        b2 = m - a2
        for child in (a3, b3, a2, b2):
            if child >= 2:
                incoming[child] += A[m] / 2
    return A, r


# Generic positive-target preservation is false.
X = 8
w = [Fraction(0) for _ in range(X + 1)]
w[4] = Fraction(1)
A, _ = producer_from_target(w, X)
assert A[3] == -1, A[3]

# Second Abel-prefix positivity is false.
X = 60
Q = 59
w = [Fraction(0) for _ in range(X + 1)]
for q in range(2, Q + 1):
    w[q] = Fraction(Q - q + 1)
A, _ = producer_from_target(w, X)
assert A[11] == Fraction(-13, 16), A[11]

# Third Abel-prefix kernel is nonnegative through level 80.
checked = 0
minimum = None
argmin = None
X = 80
for Q in range(2, X + 1):
    w = [Fraction(0) for _ in range(X + 1)]
    for q in range(2, Q + 1):
        w[q] = Fraction(comb(Q - q + 2, 2))
    A, _ = producer_from_target(w, X)
    for n in range(2, X + 1):
        value = A[n]
        checked += 1
        if minimum is None or value < minimum:
            minimum = value
            argmin = (Q, n)
        assert value >= 0, (Q, n, value)

print("PASS_EXACT_THIRD_ABEL_KERNEL_RECONNAISSANCE")
print("generic_negative_K_3_4", "-1")
print("second_prefix_witness_Q59_n11", "-13/16")
print("third_prefix_rows_checked", checked)
print("third_prefix_minimum", minimum)
print("third_prefix_argmin", argmin)
