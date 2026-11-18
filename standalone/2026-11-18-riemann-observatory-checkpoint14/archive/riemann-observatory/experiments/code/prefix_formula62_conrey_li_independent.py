"""Independent interval replay of the zeta reciprocal-kernel witness."""
from fractions import Fraction
from math import comb, factorial

import mpmath


iv = mpmath.iv
iv.dps = 75
N = 512
M = 12


def bernoulli_numbers(maximum):
    numbers = [Fraction(1)]
    for order in range(1, maximum + 1):
        total = sum(comb(order + 1, j) * numbers[j] for j in range(order))
        numbers.append(-total / (order + 1))
    return numbers


BERNOULLI = bernoulli_numbers(2 * M)


def rational(value):
    return iv.mpf(value.numerator) / value.denominator


def add_error(value, radius):
    box = iv.mpf([-1, 1]) * radius
    return value + iv.mpc(box, box)


def zeta(s):
    """Euler–Maclaurin truncation with the periodic Bernoulli remainder."""
    log_n = iv.log(N)
    total = sum(iv.exp(-s * iv.log(n)) for n in range(1, N))
    total += iv.exp((1 - s) * log_n) / (s - 1)
    total += iv.exp(-s * log_n) / 2
    rising = iv.mpc(1)
    for order in range(1, 2 * M + 1):
        rising *= s + (order - 1)
        if order % 2 == 1:
            coefficient = rational(BERNOULLI[order + 1] / factorial(order + 1))
            total += coefficient * rising * iv.exp((-s - order) * log_n)
    exponent = s.real + 2 * M - 1
    error = (
        rational(abs(BERNOULLI[2 * M]) / factorial(2 * M))
        * abs(rising) * iv.exp(-exponent * log_n) / exponent
    )
    return add_error(total, error), error


def log_gamma(z):
    """Stirling series with the periodic Bernoulli integral remainder."""
    total = (z - iv.mpf(1) / 2) * iv.log(z) - z + iv.log(2 * iv.pi) / 2
    for k in range(1, M + 1):
        coefficient = rational(BERNOULLI[2 * k] / (2 * k * (2 * k - 1)))
        total += coefficient / z ** (2 * k - 1)
    error = (
        2 ** M * rational(abs(BERNOULLI[2 * M]) / (2 * M * (2 * M - 1)))
        / abs(z) ** (2 * M - 1)
    )
    return add_error(total, error), error


def main():
    s = iv.mpc(1 + rational(Fraction(1, 10**6)), 282)
    zeta_left, zeta_left_error = zeta(s)
    zeta_right, zeta_right_error = zeta(s + 1)
    gamma_left, gamma_left_error = log_gamma(s / 2)
    gamma_right, gamma_right_error = log_gamma((s + 1) / 2)
    assert abs(zeta_left) > 0 and abs(zeta_right) > 0

    printed_ratio = (
        (s - 1) / (s + 1) * iv.sqrt(iv.pi)
        * iv.exp(gamma_left - gamma_right) * zeta_left / zeta_right
    )
    kernel_ratio = 1 / printed_ratio
    assert iv.mpf('-0.000131764') < printed_ratio.real < iv.mpf('-0.000131763')
    assert kernel_ratio.real < 0
    print('mpmath', mpmath.__version__, 'interval decimal precision', iv.dps)
    print('s = 1 + 1/1000000 + 282 i')
    print('zeta remainder bounds:', zeta_left_error, zeta_right_error)
    print('loggamma remainder bounds:', gamma_left_error, gamma_right_error)
    print('Re completed ratio:', printed_ratio.real)
    print('Re reciprocal kernel ratio:', kernel_ratio.real)


if __name__ == '__main__':
    main()
