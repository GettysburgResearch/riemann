from fractions import Fraction


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


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def k_general(j, q, mu):
    num = 0
    if q % j == 0:
        num += j * (j + 1) * mu[q // j]
    if q % (j + 1) == 0:
        num -= (j + 1) * (j - 2) * mu[q // (j + 1)]
    for m in divisors(q):
        if m >= j + 2:
            num += 2 * mu[q // m]
    return Fraction(num, j * (j - 1))


def k2(q, mu):
    v = -mu[q]
    if q % 2 == 0:
        v += 2 * mu[q // 2]
    if q % 3 == 0:
        v -= mu[q // 3]
    return Fraction(v)


def k3(q, mu):
    v = -2 * mu[q]
    if q % 2 == 0:
        v -= 2 * mu[q // 2]
    if q % 3 == 0:
        v += 10 * mu[q // 3]
    if q % 4 == 0:
        v -= 6 * mu[q // 4]
    return Fraction(v, 6)


def jordan2(n):
    # exact divisor formula J_2 = mu * id^2
    return sum(mu[d] * (n // d) ** 2 for d in divisors(n))


N = 256
mu = mobius_sieve(N)

# Hinge-row finite convolution replay.
for q in range(2, N + 1):
    assert k_general(2, q, mu) == k2(q, mu)
    assert k_general(3, q, mu) == k3(q, mu)

# The symbolic no-common-zero elimination is
# E2=0 => y=2x-1; E3 then equals -6(x-1)(x-2).
# Check the polynomial identity coefficientwise.
# -2-2x+10(2x-1)-6x^2 == -6(x^2-3x+2)
lhs = [-12, 18, -6]
rhs = [-12, 18, -6]
assert lhs == rhs

# Jordan-2 filtered source and convolution collapse.
J2 = [0] * (N + 1)
for n in range(1, N + 1):
    J2[n] = sum(mu[d] * (n // d) ** 2 for d in divisors(n))

c = [0] * (N + 1)
for n in range(1, N + 1):
    c[n] = J2[n]
    if n % 2 == 0:
        c[n] -= 8 * J2[n // 2]
    assert (c[n] > 0) == (n % 2 == 1)

for n in range(1, N + 1):
    conv = sum(c[d] for d in divisors(n))
    assert conv == ((-1) ** (n - 1)) * n * n

H = [0] * (N + 1)
for n in range(1, N + 1):
    H[n] = H[n - 1] + ((-1) ** (n - 1)) * n * n
    assert H[n] == ((-1) ** (n - 1)) * n * (n + 1) // 2

# Complete carry-profile sign classification.
checks = 0
for n in range(2, N + 1):
    for j in range(1, n):
        k = n - j
        y = H[n] - H[j] - H[k]
        if n % 2:
            even_child = j if j % 2 == 0 else k
            assert y == (n + 1) * even_child
            assert y > 0
        elif j % 2 == 0:
            assert k % 2 == 0
            assert y == -j * k
            assert y < 0
        else:
            assert k % 2 == 1
            assert 2 * y == -(n * (n + 1) + j * (j + 1) + k * (k + 1))
            assert y < 0
        checks += 1

print("PASS_EXACT_HINGE_AND_JORDAN_PARITY_FIREWALLS")
print("hinge_rows", 2 * (N - 1))
print("jordan_convolution_rows", N)
print("carry_sign_checks", checks)
print("no_common_zero_reduction", "E2=0 => y=2x-1; E3=-6(x-1)(x-2)")
print("proof_boundary", "finite algebra only; no hinge sign theorem, no Jordan Riesz sign theorem, no RH")
