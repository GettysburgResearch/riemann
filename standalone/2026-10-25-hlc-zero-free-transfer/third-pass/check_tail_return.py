#!/usr/bin/env python3
"""Exact local algebra and scale predicates for TAIL_RETURN.md.

This checker proves finite polynomial equalities by coefficient
comparison. It does not certify a global Euler product, contour
deformation, mean-value estimate, or zero-free theorem.
"""

from fractions import Fraction as F
from itertools import product
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


NVARS = 5  # r, t, X, u, P, where P=1/Np.
ZERO = (0,) * NVARS


def constant(c):
    return {ZERO: F(c)} if c else {}


def variable(index):
    power = [0] * NVARS
    power[index] = 1
    return {tuple(power): F(1)}


def plus(*polynomials):
    result = {}
    for polynomial in polynomials:
        for power, coefficient in polynomial.items():
            result[power] = result.get(power, F(0)) + coefficient
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def scale(polynomial, scalar):
    return {power: scalar * coefficient for power, coefficient in polynomial.items()
            if scalar * coefficient}


def times(*polynomials):
    result = constant(1)
    for polynomial in polynomials:
        next_result = {}
        for a, ca in result.items():
            for b, cb in polynomial.items():
                power = tuple(x + y for x, y in zip(a, b))
                next_result[power] = next_result.get(power, F(0)) + ca * cb
        result = {power: coefficient for power, coefficient in next_result.items()
                  if coefficient}
    return result


def specialize_u_to_p(polynomial):
    result = {}
    for power, coefficient in polynomial.items():
        target = list(power)
        target[4] += target[3]
        target[3] = 0
        target = tuple(target)
        result[target] = result.get(target, F(0)) + coefficient
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def test_local_polynomial():
    r, t, x, u, p = (variable(i) for i in range(NVARS))
    one = constant(1)
    delta = times(plus(one, scale(times(r, p), -1)),
                  plus(one, scale(times(t, p), -1)))
    c1 = plus(scale(r, -1), scale(t, -1), times(r, t, p))
    c2 = times(r, t)
    # delta+(c1*X+c2*X^2)(1-Y), using X*Y=u.
    lhs = plus(delta, times(c1, x), times(c2, x, x),
               scale(times(c1, u), -1), scale(times(c2, x, u), -1))
    main = times(plus(one, scale(times(r, x), -1)),
                 plus(one, scale(times(t, x), -1)))
    remainder = times(plus(u, scale(p, -1)),
                      plus(r, t, scale(times(r, t, p), -1),
                           scale(times(r, t, x), -1)))
    rhs = plus(main, remainder)
    require(lhs == rhs, "coherent local numerator polynomial failed")
    require(specialize_u_to_p(lhs) == main, "h=0 return failed")
    wrong_c1 = plus(scale(r, -1), scale(t, -1))
    wrong_overlap = plus(delta, times(wrong_c1, x), times(c2, x, x),
                         scale(times(wrong_c1, u), -1), scale(times(c2, x, u), -1))
    require(specialize_u_to_p(wrong_overlap) != main,
            "omitted repeated-prime term was not detected")
    wrong_independent = plus(delta, times(c1, x), times(c2, x, x))
    require(specialize_u_to_p(wrong_independent) != main,
            "omitted numerator/denominator coprimality was not detected")
    return {"exact_polynomial_coefficient_identities": 2,
            "coherent_numerator_nonzero_monomials": len(lhs),
            "negative_drop_repeated_prime": True,
            "negative_drop_reduced_coprimality": True}


def test_local_root():
    q = F(7)
    r = t = F(5, 4)
    delta = (1 - r / q) * (1 - t / q)

    def local(x):
        return 1 - (r + t - r * t / q) * x / delta + r * t * x * x / delta

    require(delta == F(529, 784), "explicit scalar denominator failed")
    require(local(F(2, 5)) == F(11, 529), "left sign certificate failed")
    require(local(F(1, 2)) == F(-229, 2116), "right sign certificate failed")
    require(r**8 < q, "example beta must exceed 7/8")
    require(1 - r * F(1, 2) == F(3, 8), "ordinary factors are not separated from zero")
    require(F(1, 2) < 1 / (r * r), "example root must be right of correction boundary")
    return {"rational_root_bracket": ["2/5", "1/2"],
            "left_polynomial_value": "11/529",
            "right_polynomial_value": "-229/2116",
            "ordinary_factor_lower_bound_on_bracket": "3/8",
            "predicates": 6}


def test_scale_envelope():
    shifts = (F(-1, 4), F(-1, 8), F(0), F(1, 8), F(1, 4))
    count = negative_control = 0
    for r, a, fraction, s, z, h in product(
        (F(29, 25), F(117, 100), F(7, 5)),
        (F(1, 2), F(3, 4), F(4, 5), F(7, 8)),
        (F(1, 4), F(1, 2), F(3, 4)),
        shifts, shifts, (F(-1, 8), F(0), F(1, 8)),
    ):
        alpha = fraction * r
        minimum = min(s, z)
        sigma = a - h - minimum
        exponent = r * (sigma - F(1, 2)) + r * h + alpha * s + (r - alpha) * z
        exact = r * (a - F(1, 2)) + alpha * (s - minimum) + (r - alpha) * (z - minimum)
        require(exponent == exact, "joint scale identity failed")
        require(exponent >= r * (a - F(1, 2)), "buffered-contour scale inequality failed")
        require((exponent == r * (a - F(1, 2))) == (s == z),
                "interior-cutoff equality condition failed")
        wrong_sigma = a - h
        wrong_exponent = r * (wrong_sigma - F(1, 2)) + r * h + alpha * s + (r - alpha) * z
        negative_control += wrong_exponent < r * (a - F(1, 2))
        count += 3
    require(negative_control > 0, "ignoring the contour displacement was not detected")
    return {"rational_predicates": count,
            "negative_ignored_required_displacement": negative_control}


def test_density_resource():
    a = F(4, 5)
    density = (31 - 32 * a) / (21 - 12 * a)
    require(density == F(9, 19), "density example failed")
    count = 1
    for thousandths in range(1160, 1171):
        r = F(thousandths, 1000)
        inherited = (1 + 5 * r) / 6
        resource = density + (2 * a - 1) * r
        target = inherited - F(1, 1000)
        difference = resource - target
        require(difference == F(35, 114) - F(7, 30) * r + F(1, 1000),
                "density-resource comparison formula failed")
        require(difference >= F(499, 14250) > 0,
                "the optimistic resource unexpectedly reaches the proposed target")
        count += 2
    return {"rational_predicates": count,
            "minimum_gap_to_proposed_target": "499/14250",
            "scope": "upper-bound resource comparison, not an actual moment lower bound"}


def main():
    result = {
        "local_identity": test_local_polynomial(),
        "local_polynomial_zero": test_local_root(),
        "scale_envelope": test_scale_envelope(),
        "density_resource": test_density_resource(),
        "scope": "exact finite algebra only; no global contour or tail moment certification",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
