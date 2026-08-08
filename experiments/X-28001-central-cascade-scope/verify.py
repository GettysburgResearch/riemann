from fractions import Fraction
from math import comb, isqrt


def sqrt_interval(x: Fraction, digits: int = 50):
    scale = 10 ** digits
    numerator = x.numerator * scale * scale
    denominator = x.denominator
    lo = isqrt(numerator // denominator)
    while (lo + 1) * (lo + 1) * denominator <= numerator:
        lo += 1
    while lo * lo * denominator > numerator:
        lo -= 1
    return Fraction(lo, scale), Fraction(lo + 1, scale)


def log_interval(x: Fraction, terms: int = 100):
    assert x > 1
    y = (x - 1) / (x + 1)
    total = Fraction(0)
    power = y
    for k in range(terms):
        total += Fraction(2, 2 * k + 1) * power
        power *= y * y
    remainder = Fraction(2, 2 * terms + 1) * power / (1 - y * y)
    return total, total + remainder


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul_positive(a, b):
    return a[0] * b[0], a[1] * b[1]


def scale_positive(c, a):
    assert c >= 0
    return c * a[0], c * a[1]


def reciprocal_positive(a):
    return Fraction(1, a[1]), Fraction(1, a[0])


def continuum_counterexamples():
    sqrt2 = sqrt_interval(Fraction(2))
    sqrt3 = sqrt_interval(Fraction(3))
    sqrt6 = sqrt_interval(Fraction(6))
    sqrt7 = sqrt_interval(Fraction(7))
    sqrt8 = sqrt_interval(Fraction(8))

    log2 = log_interval(Fraction(2))
    log43 = log_interval(Fraction(4, 3))
    log74 = log_interval(Fraction(7, 4))
    log76 = log_interval(Fraction(7, 6))

    f2_at_1_over_7 = mul_positive(
        sqrt7,
        sub(
            scale_positive(Fraction(1, 2), log74),
            mul_positive(scale_positive(2, reciprocal_positive(sqrt6)), log76),
        ),
    )
    f2_at_1_over_8 = mul_positive(
        sqrt8,
        sub(
            scale_positive(Fraction(1, 2), log2),
            mul_positive(scale_positive(2, reciprocal_positive(sqrt6)), log43),
        ),
    )
    monotonicity_gap = sub(f2_at_1_over_7, f2_at_1_over_8)
    assert monotonicity_gap[0] > Fraction(9, 100)

    f3_at_1_over_16 = sub(
        mul_positive(sqrt2, log2),
        scale_positive(2, mul_positive(sqrt3, log43)),
    )
    assert f3_at_1_over_16[1] < Fraction(-1, 100)

    return monotonicity_gap, f3_at_1_over_16


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


def binary_ternary_producer(target, endpoint):
    mu = mobius_sieve(endpoint)
    multiple_mobius = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(1, endpoint + 1):
        for k in range(1, endpoint // m + 1):
            if mu[k]:
                multiple_mobius[m] += mu[k] * target[m * k]

    divergence = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(1, endpoint + 1):
        divergence[m] = multiple_mobius[m] - multiple_mobius[m + 1]

    producer = [Fraction(0) for _ in range(endpoint + 2)]
    incoming = [Fraction(0) for _ in range(endpoint + 2)]
    for m in range(endpoint, 1, -1):
        producer[m] = divergence[m] + incoming[m]
        one_third = (m + 2) // 3
        children = (one_third, m - one_third, m // 2, m - m // 2)
        for child in children:
            if child >= 2:
                incoming[child] += producer[m] / 2
    return producer


def third_abel_counterexample():
    endpoint = 520
    target = [Fraction(0) for _ in range(endpoint + 1)]
    for q in range(2, endpoint + 1):
        target[q] = Fraction(comb(endpoint - q + 2, 2))
    producer = binary_ternary_producer(target, endpoint)
    assert producer[15] == Fraction(-91, 256)
    return producer[15]


if __name__ == "__main__":
    gap, f3 = continuum_counterexamples()
    third = third_abel_counterexample()
    print("EXACT_CENTRAL_CASCADE_SCOPE_COUNTEREXAMPLES")
    print("T2_monotonicity_gap_gt", "9/100")
    print("T3_at_1_over_16_lt", "-1/100")
    print("third_Abel_Q520_n15", third)
    print("arithmetic", "Fraction + directed atanh-log and integer-sqrt intervals")
    print("proof_boundary", "scope counterexamples only; no RH conclusion")