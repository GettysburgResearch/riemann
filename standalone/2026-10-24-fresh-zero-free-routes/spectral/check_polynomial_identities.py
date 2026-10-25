#!/usr/bin/env python3
"""Exact rational identities, not a numerical theta or zero-free certificate."""

import json
from fractions import Fraction as Q
from math import comb


def require(predicate, label):
    if not predicate:
        raise ArithmeticError(label)
    return label


def derivative_polynomial(p):
    result = [Q(0)] * (len(p) + 1)
    for j, coefficient in enumerate(p):
        result[j] += (Q(1, 2) + 2 * j) * coefficient
        result[j + 1] -= 2 * coefficient
    return result


def shift(p, offset, scale=1):
    return [
        sum(p[j] * comb(j, i) * offset ** (j - i) * scale**i
            for j in range(i, len(p)))
        for i in range(len(p))
    ]


def bernstein(p, left, right):
    power = shift(p, left, right - left)
    degree = len(power) - 1
    return [
        sum(power[i] * Q(comb(k, i), comb(degree, i))
            for i in range(k + 1))
        for k in range(degree + 1)
    ]


def main():
    checks = []
    polynomials = [[Q(0), Q(-6), Q(4)]]
    for _ in range(4):
        polynomials.append(derivative_polynomial(polynomials[-1]))
    checks.append(require(
        polynomials[2] == [Q(0), Q(-75, 2), Q(165), Q(-112), Q(16)],
        "second derivative polynomial"))
    checks.append(require(
        polynomials[4] == [Q(0), Q(-1875, 8), Q(15465, 4), Q(-8512),
                            Q(5176), Q(-1056), Q(64)],
        "fourth derivative polynomial"))

    difference = polynomials[4][:]
    for i, coefficient in enumerate(polynomials[2]):
        difference[i] -= coefficient
    positivity = difference[:]
    for i, coefficient in enumerate(polynomials[0]):
        positivity[i] += 10000 * coefficient

    finite = bernstein(positivity, Q(3), Q(10))
    expected_finite = [Q(1551429, 8), Q(6801147, 16), Q(4709161, 6),
                       Q(18462881, 16), Q(8691051, 8), Q(3777125, 48),
                       Q(21472625, 4)]
    checks.append(require(finite == expected_finite,
                          "complete Bernstein coefficient identity on [3,10]"))
    checks.append(require(all(value > 0 for value in finite),
                          "strict positivity throughout [3,10]"))
    tail = shift(difference, Q(10))
    expected_tail = [Q(7872625, 4), Q(30350625, 8), Q(7550805, 4),
                     Q(422000), Q(48360), Q(2784), Q(64)]
    checks.append(require(tail == expected_tail,
                          "complete tail polynomial identity at u=10+y"))
    checks.append(require(all(value > 0 for value in tail),
                          "strict positivity for every y>=0"))

    x2, y2 = Q(199, 4), Q(201, 4)
    real_z2 = x2 - y2
    imag_z2_squared = 4 * x2 * y2
    checks.append(require(real_z2**2 - imag_z2_squared + real_z2 + 10000 == 0,
                          "explicit quartet real polynomial equation"))
    checks.append(require(2 * real_z2 + 1 == 0,
                          "explicit quartet imaginary polynomial equation"))
    checks.append(require(y2 > 0 and x2 > 0,
                          "explicit quartet is nonreal and off the imaginary axis"))
    checks.append(require(-2 * Q(1, 10000) == -Q(1, 5000),
                          "exact variance decrement"))

    # A universal coefficient identity in e=epsilon and h=eta^2:
    # 4 e^2 (1/e+h) h = 4 h e (1+h e).
    # Test several rational instances as additional finite regression checks;
    # the symbolic identity and analytic positivity proof are in the text.
    examples = []
    for epsilon, height_squared in [(Q(1, 100), Q(1, 16)),
                                     (Q(1, 10000), Q(9, 100)),
                                     (Q(2, 7), Q(5, 13))]:
        delta = 4 * height_squared * epsilon * (1 + height_squared * epsilon)
        r2 = 1 / epsilon + height_squared
        checks.append(require(4 * epsilon**2 * r2 * height_squared == delta,
                              "prescribed-width quartet identity " + str(epsilon)))
        examples.append({"epsilon": str(epsilon), "eta_squared": str(height_squared),
                         "delta": str(delta), "real_part_squared": str(r2)})

    result = {
        "status": "EXACT_POLYNOMIAL_CHECKS_PASS",
        "checks": checks,
        "bernstein_coefficients": list(map(str, finite)),
        "tail_coefficients": list(map(str, tail)),
        "quartet_examples": examples,
        "analytic_scope": "Global polynomial positivity for the explicit theta-derivative density; theta/Weil identities are analytic premises proved in the notes.",
        "zero_free_region_certified": False,
        "theta_quadrature_performed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
