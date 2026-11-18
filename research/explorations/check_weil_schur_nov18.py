"""Rational row-sum upper bound on the interval [-log(12), log(12)]."""
from fractions import Fraction


def log_unit_upper(q):
    """Upper log(q) for 1 <= q <= 2 by a finite atanh series."""
    v = (q - 1) / (q + 1)
    count = 12
    partial = sum(2 * v ** (2 * j + 1) / (2 * j + 1) for j in range(count))
    tail = 2 * v ** (2 * count + 1) / ((2 * count + 1) * (1 - v * v))
    return partial + tail


def log_prime_upper(p):
    exponent = p.bit_length() - 1
    bound = exponent * log_unit_upper(Fraction(2))
    bound += log_unit_upper(Fraction(p, 2**exponent))
    milli = (1000 * bound.numerator + bound.denominator - 1) // bound.denominator
    return Fraction(milli, 1000)


def prime_power_weights(limit):
    weights = {}
    for p in range(2, limit + 1):
        if any(p % n == 0 for n in range(2, p)):
            continue
        n = p
        while n <= limit:
            weights[n] = log_prime_upper(p)
            n *= p
    return weights


def row_sum(v, edge, weights):
    numerator = Fraction(0)
    for n, weight in weights.items():
        if n * v <= edge:
            numerator += weight * (v + Fraction(1, n))
        if n <= edge * v:
            numerator += weight * (1 + v / n)
    return numerator / (v + 1)


def main():
    edge = 12
    weights = prime_power_weights(edge**2)
    nodes = {Fraction(1), Fraction(edge)}
    nodes.update(Fraction(n, edge) for n in weights)
    nodes.update(Fraction(edge, n) for n in weights)
    maximum, at = max(
        (row_sum(v, edge, weights), v) for v in nodes if 1 <= v <= edge
    )
    assert maximum < Fraction(1531, 100)
    print("Prime powers:", len(weights))
    print("Maximum rational upper bound:", maximum)
    print("Attaining node:", at)


if __name__ == "__main__":
    main()
