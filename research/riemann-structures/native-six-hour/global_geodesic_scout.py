#!/usr/bin/env python3
"""One shared native path on all 63 factor pairs of a complete finite panel."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
SOURCES = {
    "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md": "6810bcece309b0c54ae6c8fc84b314990004549c",
    "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md": "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
}
PRIMES = (2, 3, 5)
HORIZON = 25
RADICANDS = (1, 2, 3, 5, 6, 10, 15, 30)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rad(values=None):
    result = {d: F(value) for d, value in (values or {}).items() if value}
    require(all(d in RADICANDS for d in result), "declared multiquadratic basis")
    return result


def scalar(value):
    return rad({1: value})


def ra(a, b):
    result = dict(a)
    for d, value in b.items():
        result[d] = result.get(d, F()) + value
    return rad(result)


def rs(a, b):
    return rad({d: value * b for d, value in a.items()})


def rm(a, b):
    result = {}
    for d, x in a.items():
        for e, y in b.items():
            g = gcd(d, e)
            f = d * e // (g * g)
            result[f] = result.get(f, F()) + g * x * y
    return rad(result)


def rational_exponents(value):
    require(type(value) in (int, F) and value > 0, "positive exact panel rational")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 64,
        "rational bit cap",
    )
    numerator, denominator = value.numerator, value.denominator
    result = []
    for p in PRIMES:
        exponent = 0
        while numerator % p == 0:
            numerator //= p
            exponent += 1
        while denominator % p == 0:
            denominator //= p
            exponent -= 1
        result.append(exponent)
    require(numerator == denominator == 1, "rational supported on declared prime panel")
    return tuple(result)


def sqrt_rational(value):
    coefficient, d = F(1), 1
    for p, exponent in zip(PRIMES, rational_exponents(value), strict=True):
        coefficient *= F(p) ** (exponent // 2)
        if exponent % 2:
            d *= p
    return rad({d: coefficient})


def ex(constant=None):
    return (rad(constant), {}, {}, {})


def ea(a, b):
    return tuple(ra(x, y) for x, y in zip(a, b, strict=True))


def es(a, value):
    return tuple(rs(x, value) for x in a)


def er(a, value):
    return tuple(rm(x, value) for x in a)


@lru_cache(maxsize=512, typed=True)
def gamma(shift):
    rational_exponents(shift)
    shift = F(shift)
    shift = shift if shift >= 1 else 1 / shift
    if shift >= 8:
        return ex()
    inverse_root = sqrt_rational(1 / shift)
    pieces = (
        (F(1), F(2), scalar(8), scalar(-4)),
        (F(2), F(4), rad({1: -8, 2: -8}), rad({2: 4})),
        (F(4), F(8), rad({2: 8}), scalar(-2)),
    )
    result = ex()
    for lo1, hi1, a, b in pieces:
        for lo2, hi2, c, d in pieces:
            lo, hi = max(lo1, shift * lo2), min(hi1, shift * hi2)
            if lo >= hi:
                continue
            logarithm = rm(a, c)
            root_term = rs(ra(rm(rm(a, d), inverse_root), rm(b, c)), 2)
            linear_term = rm(rm(b, d), inverse_root)
            constant = ra(
                rm(root_term, ra(sqrt_rational(hi), rs(sqrt_rational(lo), -1))),
                rs(linear_term, hi - lo),
            )
            term = (constant,) + tuple(
                rs(logarithm, exponent) for exponent in rational_exponents(hi / lo)
            )
            result = ea(result, term)
    return result


def ia(a, b):
    return a[0] + b[0], a[1] + b[1]


def im(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


@lru_cache(maxsize=3, typed=True)
def log_prime(p):
    require(type(p) is int and p in PRIMES, "declared logarithm prime")
    value, k = F(p), 0
    while value >= 2:
        value /= 2
        k += 1

    def small_log(x):
        z = (x - 1) / (x + 1)
        current, total = z, F()
        for j in range(48):
            total += 2 * current / (2 * j + 1)
            current *= z * z
        remainder = 2 * current / (97 * (1 - z * z))
        return total, total + remainder

    local, two = small_log(value), small_log(F(2))
    return ia(local, (k * two[0], k * two[1]))


def ri(value):
    result = (F(), F())
    denominator = 10**40
    for d, coefficient in value.items():
        if d == 1:
            root = F(1), F(1)
        else:
            lower = isqrt(d * denominator * denominator)
            root = F(lower, denominator), F(lower + 1, denominator)
        result = ia(result, im((coefficient, coefficient), root))
    return result


def ei(value):
    result = ri(value[0])
    for p, coefficient in zip(PRIMES, value[1:], strict=True):
        result = ia(result, im(ri(coefficient), log_prime(p)))
    return result


def bp(values=None):
    result = {key: F(value) for key, value in (values or {}).items() if value}
    require(
        all(
            type(e) is type(t) is int and 0 <= e <= 2 and 0 <= t <= 8 for e, t in result
        ),
        "native bivariate degree cap",
    )
    return result


def ba(a, b):
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, F()) + value
    return bp(result)


def bm(a, b):
    result = {}
    for (e, t), x in a.items():
        for (f, u), y in b.items():
            key = e + f, t + u
            result[key] = result.get(key, F()) + x * y
    return bp(result)


def bd(a):
    return bp({(e, t - 1): t * value for (e, t), value in a.items() if t})


def bi(a):
    result = [F(), F(), F()]
    for (e, t), value in a.items():
        result[e] += 2 * value / (t + 1)
    return tuple(result)


def primitive_site_square(a):
    result = [F()] * 5
    for (e, t), x in a.items():
        for (f, u), y in a.items():
            require(e + f <= 4 and t + u <= 16, "primitive diagonal degree cap")
            result[e + f] += 2 * x * y / (t + u + 1)
    return tuple(result)


def integrated_square(a):
    require(len(a) == 3, "integrated field degree")
    result = [F()] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            result[i + j] += x * y
    return tuple(result)


def sqrt_coefficient(degree):
    require(type(degree) is int and 0 <= degree <= 4, "local exponent cap")
    value = F(1)
    for j in range(degree):
        value *= -(F(1, 2) - j) / (j + 1)
    return value


def local(degree, deformed):
    require(type(deformed) is bool, "literal deformation switch")
    end = sqrt_coefficient(degree)
    start = sqrt_coefficient(degree // 2) if degree % 2 == 0 else F()
    difference = end - start
    result = bp({(0, 0): start, (0, 1): difference})
    return (
        ba(result, bp({(1, 1): difference, (1, 2): -difference}))
        if deformed
        else result
    )


def source(n, deformed_prime):
    require(type(n) is int and 1 <= n <= HORIZON, "physical source horizon")
    exponents = rational_exponents(n)
    factors = tuple(
        local(e, p == deformed_prime) for p, e in zip(PRIMES, exponents, strict=True)
    )
    value = bp({(0, 0): 1})
    for factor in factors:
        value = bm(value, factor)
    sites = []
    for j, p in enumerate(PRIMES):
        term = bp({(0, 0): 1})
        for i, factor in enumerate(factors):
            term = bm(term, bd(factor) if i == j else factor)
        if term:
            sites.append((p, term))
    summed = bp()
    for _, term in sites:
        summed = ba(summed, term)
    require(summed == bd(value), "all literal derivative sites retained")
    return value, sites


def panel_numbers():
    result = []
    for n in range(1, HORIZON + 1):
        residual = n
        for p in PRIMES:
            while residual % p == 0:
                residual //= p
        if residual == 1:
            result.append(n)
    return tuple(result)


def native_field(deformed_prime):
    require(
        type(deformed_prime) is int and deformed_prime in PRIMES,
        "one global source deformation",
    )
    numbers = panel_numbers()
    sources = {n: source(n, deformed_prime) for n in numbers}
    records, ratios, endpoints = [], {}, {}
    diagonals = {
        name: [F()] * 5
        for name in ("primitive_2ds_site", "integrated_site", "integrated_pair")
    }
    for n in numbers:
        for m in numbers:
            if n * m > HORIZON:
                continue
            left, sites = sources[n]
            right = sources[m][0]
            coefficient = bi(bm(bd(left), right))
            site_terms = [(p, bm(term, right)) for p, term in sites]
            literal = [(p, bi(term)) for p, term in site_terms]
            require(
                tuple(sum((entry[k] for _, entry in literal), F()) for k in range(3))
                == coefficient,
                "complete integrated site sum",
            )
            K, ratio = n * m, F(n, m)
            for _, term in site_terms:
                for j, value in enumerate(primitive_site_square(term)):
                    diagonals["primitive_2ds_site"][j] += value / K
            for _, row in literal:
                for j, value in enumerate(integrated_square(row)):
                    diagonals["integrated_site"][j] += value / K
            for j, value in enumerate(integrated_square(coefficient)):
                diagonals["integrated_pair"][j] += value / K
            records.append(
                {
                    "n": n,
                    "m": m,
                    "K": K,
                    "ratio": str(ratio),
                    "epsilon_coefficients_before_physical_weight": [
                        str(x) for x in coefficient
                    ],
                    "derivative_site_coefficients": [
                        [p, [str(x) for x in row]] for p, row in literal
                    ],
                }
            )
            endpoint = endpoints.setdefault(K, [F(), F(), F()])
            amplitudes = ratios.setdefault(ratio, [{}, {}, {}])
            weight = sqrt_rational(F(1, K))
            for j in range(3):
                endpoint[j] += coefficient[j]
                amplitudes[j] = ra(amplitudes[j], rs(weight, coefficient[j]))
            if n == 1:
                require(coefficient == (0, 0, 0), "root-free native left tangent")
    require(len(records) == 63, "complete preregistered ordered factor horizon")
    for K, values in endpoints.items():
        exponents = rational_exponents(K)
        beta = (
            (-1) ** sum(e > 0 for e in exponents)
            if all(e <= 1 for e in exponents)
            else 0
        )
        beta_square = (
            (-1) ** sum(e > 0 for e in exponents)
            if all(e in (0, 2) for e in exponents)
            else 0
        )
        require(
            values == [beta - beta_square, 0, 0], "every product endpoint is unchanged"
        )
    for ratio, coefficients in ratios.items():
        for j in (1, 2):
            require(
                ra(coefficients[j], ratios[1 / ratio][j]) == {},
                "all path variation is odd",
            )
    coalesced_diagonal = [{} for _ in range(5)]
    for coefficients in ratios.values():
        for i in range(3):
            for j in range(3):
                coalesced_diagonal[i + j] = ra(
                    coalesced_diagonal[i + j], rm(coefficients[i], coefficients[j])
                )
    require(
        all(set(row) <= {1} for row in coalesced_diagonal),
        "same-ratio physical square is rational",
    )
    diagonals["ratio_coalesced"] = [row.get(1, F()) for row in coalesced_diagonal]
    return records, ratios, endpoints, diagonals


def energy_polynomial(ratios):
    result = [ex() for _ in range(5)]
    for ratio, left in ratios.items():
        for other, right in ratios.items():
            correlation = gamma(ratio / other)
            for i in range(3):
                for j in range(3):
                    if left[i] and right[j]:
                        result[i + j] = ea(
                            result[i + j], er(correlation, rm(left[i], right[j]))
                        )
    return tuple(result)


def evaluate_energy(coefficients, parameter):
    require(
        type(parameter) in (int, F) and -1 <= parameter <= 1,
        "admissible source path parameter",
    )
    result = ex()
    for coefficient in reversed(coefficients):
        result = ea(es(result, parameter), coefficient)
    return result


def expr_json(value):
    return {
        name: {str(d): str(coefficient) for d, coefficient in sorted(row.items())}
        for name, row in zip(("constant", "log2", "log3", "log5"), value, strict=True)
    }


def interval_json(value):
    return {
        "lower": str(value[0]),
        "upper": str(value[1]),
        "approximate_midpoint": float((value[0] + value[1]) / 2),
    }


def discover(deformed_prime):
    records, ratios, endpoints, diagonals = native_field(deformed_prime)
    coefficients = energy_polynomial(ratios)
    observed_diagonals = {
        name: tuple(es(gamma(F(1)), value) for value in row)
        for name, row in diagonals.items()
    }
    centered_pair = tuple(
        ea(value, es(diagonal, -1))
        for value, diagonal in zip(
            coefficients, observed_diagonals["integrated_pair"], strict=True
        )
    )
    grid = []
    for denominator in (16, 8, 4, 2):
        for sign in (-1, 1):
            parameter = F(sign, denominator)
            gap = ea(coefficients[0], es(evaluate_energy(coefficients, parameter), -1))
            interval = ei(gap)
            centered_gap = ea(
                centered_pair[0], es(evaluate_energy(centered_pair, parameter), -1)
            )
            grid.append(
                {
                    "epsilon": str(parameter),
                    "energy_improvement": interval_json(interval),
                    "declared_pair_centered_improvement": interval_json(
                        ei(centered_gap)
                    ),
                    "strict_improvement_certified": interval[0] > 0,
                }
            )
    return {
        "deformed_prime": deformed_prime,
        "prime_panel": PRIMES,
        "physical_product_cap": HORIZON,
        "complete_ordered_factor_count": len(records),
        "complete_ratio_count": len(ratios),
        "records": records,
        "every_product_endpoint": {
            str(K): [str(x) for x in row] for K, row in sorted(endpoints.items())
        },
        "exact_energy_polynomial": [expr_json(row) for row in coefficients],
        "energy_polynomial_intervals": [interval_json(ei(row)) for row in coefficients],
        "diagonal_polynomials_before_Gamma0": {
            name: [str(x) for x in row] for name, row in diagonals.items()
        },
        "observed_diagonal_polynomial_intervals": {
            name: [interval_json(ei(x)) for x in row]
            for name, row in observed_diagonals.items()
        },
        "integrated_pair_centered_energy_intervals": [
            interval_json(ei(x)) for x in centered_pair
        ],
        "these_diagonals_identified_with_T106140_Wick_diagonal": False,
        "preregistered_parameter_grid": grid,
        "all_cross_product_interference_included": True,
        "physical_inverse_square_root_weights_included": True,
        "independent_tuple_parameters_used": False,
    }


def authenticate():
    for path, blob in SOURCES.items():
        raw = subprocess.run(
            ["git", "show", f"{OLD}:{path}"], cwd=ROOT, capture_output=True, check=True
        ).stdout
        require(
            0 < len(raw) < 65536
            and sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == blob,
            "original native source/kernel authentication",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    authenticate()
    require(
        gamma(F(1)) == (scalar(-288), rad({1: 384, 2: 128}), {}, {}),
        "original Gamma(0)",
    )
    require(
        gamma(F(4)) == (scalar(-48), rad({2: 64}), {}, {}), "independent Gamma(log4)"
    )
    result = {
        "schema": "riemann.native_six_hour.global_geodesic_discovery.v1",
        "sources": [
            {"commit": OLD, "path": path, "blob": blob}
            for path, blob in SOURCES.items()
        ],
        "models": [discover(p) for p in (3, 2, 5)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
