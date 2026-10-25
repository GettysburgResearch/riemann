#!/usr/bin/env python3
"""Exact finite checks for the coefficient-continuation note.

The finite checks authenticate interpolation identities and the displayed
counterexample. They do not certify Baire category, the arithmetic moment
input, analytic continuation, or any zero-free region.
"""

from fractions import Fraction
from math import comb, floor, log, sqrt
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def lagrange_weight(r, j):
    return (-1) ** (j - 1) * j * comb(r + 2, j + 1)


def chebyshev(r, x):
    if r == 0:
        return Fraction(1)
    p, q = Fraction(1), Fraction(x)
    for _ in range(1, r):
        p, q = q, 2 * x * q - p
    return q


def polynomial_counterexample(r, z):
    p = Fraction(1)
    for j in range(1, r + 1):
        p *= 1 - Fraction(z, j)
    return p


def density(s):
    return (31 - 32 * s) / (21 - 12 * s)


def envelope(r, z, beta=0.874886647039964):
    a = 1 - z / 2
    sigma = max(0.5, min(beta, (21 - sqrt(150 * a / r)) / 12))
    return sigma, a * density(sigma) + z / 2 + r * (2 * sigma - 1)


def main():
    interpolation_cases = 0
    mass_cases = 0
    counterexample_cases = 0
    chebyshev_cases = 0
    for r in range(33):
        for k in range(r + 1):
            value = sum(lagrange_weight(r, j) * j**k for j in range(1, r + 2))
            require(value == (-1) ** k, f"Interpolation failed r={r}, k={k}")
            interpolation_cases += 1
        require(sum(abs(lagrange_weight(r, j)) for j in range(1, r + 2)) == r * 2 ** (r + 1) + 1,
                f"Absolute mass failed r={r}")
        mass_cases += 1
        require(chebyshev(r, Fraction(5)) <= 10**r, f"Chebyshev cost failed r={r}")
        chebyshev_cases += 1
        require(polynomial_counterexample(r, -1) == r + 1, f"Counterexample at -1 failed r={r}")
        counterexample_cases += 1
        for j in range(1, r + 1):
            require(polynomial_counterexample(r, j) == 0, f"Counterexample zero failed r={r}, j={j}")
            counterexample_cases += 1

    density_cases = 0
    for numerator in range(50, 88):
        s = Fraction(numerator, 100)
        require(density(s) == Fraction(8, 3) - Fraction(25, 1) / (21 - 12 * s),
                f"Density decomposition failed at {s}")
        if s != Fraction(1, 2):
            require((1 - density(s)) / (2 * s - 1) == Fraction(10, 1) / (21 - 12 * s),
                    f"Density threshold identity failed at {s}")
        density_cases += 1

    corner_r = Fraction(25, 24)
    corner_sigma = Fraction(3, 4)
    target_density = 1 - corner_r * (2 * corner_sigma - 1)
    require(target_density == Fraction(23, 48), "Native target density corner failed")
    require(density(corner_sigma) - target_density == Fraction(5, 48),
            "Native target density deficit failed")

    table = []
    for r in [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(8, 9), Fraction(1), Fraction(8, 7)]:
        for z in [0, 0.05]:
            s, e = envelope(float(r), z)
            table.append({"r": str(r), "z": z, "sigma_max": round(s, 12), "maximum_exponent": round(e, 12)})

    result = {
        "exact_interpolation_monomials": interpolation_cases,
        "exact_coefficient_mass_checks": mass_cases,
        "exact_chebyshev_cost_checks": chebyshev_cases,
        "exact_counterexample_values": counterexample_cases,
        "exact_density_identity_checks": density_cases,
        "native_density_deficit_at_three_quarters": "5/48",
        "density_envelope_numeric_diagnostics": table,
        "zero_free_region_certified": False,
        "analytic_moment_input_proved_by_this_checker": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
