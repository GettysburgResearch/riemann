#!/usr/bin/env python3
"""Finite, source-faithful checks for the native angular-ray component.

Standard library only. Integer/Fraction checks remain active under python -O.
The floating Gaussian replay is a normalization check, not a proof or a
rigorous enclosure. The theorem is proved in NATIVE_ANGULAR_RAY_MOMENT.md.
"""

from collections import defaultdict
from fractions import Fraction
import cmath
import json
import math
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def norm(z):
    a, b = z
    return a * a - a * b + b * b


def mul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c - b * d)


def conjugate(z):
    a, b = z
    return (a - b, -b)


def canonical(z):
    values = []
    current = z
    for _ in range(3):
        values.extend((current, (-current[0], -current[1])))
        current = mul(current, (0, 1))
    return min(values)


def divide(z, w):
    denominator = norm(w)
    numerator = mul(z, conjugate(w))
    if numerator[0] % denominator or numerator[1] % denominator:
        return None
    return (numerator[0] // denominator, numerator[1] // denominator)


def sieve_spf(limit):
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor(n, spf):
    result = []
    while n > 1:
        p = spf[n]
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        result.append((p, exponent))
    return result


def rational_mu(n, spf):
    factors = factor(n, spf)
    if any(e > 1 for _, e in factors):
        return 0
    return (-1) ** len(factors)


def chi3(n):
    return (0, 1, -1)[n % 3]


def exact_psi1(z):
    sixth = (1, 0)
    for _ in range(6):
        sixth = mul(sixth, z)
    denominator = norm(z) ** 3
    return (Fraction(sixth[0], denominator), Fraction(sixth[1], denominator))


def to_complex(z):
    a, b = z
    return complex(float(a) - float(b) / 2, math.sqrt(3) * float(b) / 2)


def all_ideals(limit):
    cap = math.isqrt(2 * limit) + 1
    generators = set()
    for a in range(-cap, cap + 1):
        for b in range(-cap, cap + 1):
            z = (a, b)
            if 0 < norm(z) <= limit:
                generators.add(canonical(z))
    return sorted(generators, key=lambda z: (norm(z), z))


def factor_ideal_mobius(z, split_generators, spf):
    """Independent Mobius evaluation by exact prime-ideal division."""
    current = z
    exponents = []
    for p, _ in factor(norm(z), spf):
        if p == 3:
            generators = [(1, -1)]
        elif p % 3 == 2:
            generators = [(p, 0)]
        else:
            generators = split_generators[p]
            require(len(generators) == 2, "split prime must have two ideals")
        for generator in generators:
            exponent = 0
            while True:
                quotient = divide(current, generator)
                if quotient is None:
                    break
                current = quotient
                exponent += 1
            if exponent:
                exponents.append(exponent)
    require(norm(current) == 1, "prime-ideal division left a nonunit")
    return 0 if any(e > 1 for e in exponents) else (-1) ** sum(exponents)


def ray_fixture(limit=1024, q=6):
    spf = sieve_spf(limit)
    ideals = all_ideals(limit)
    split_generators = defaultdict(list)
    for z in ideals:
        n = norm(z)
        if n > 1 and spf[n] == n and n % 3 == 1:
            split_generators[n].append(z)
    mobius = {
        z: factor_ideal_mobius(z, split_generators, spf) for z in ideals
    }
    phases = {z: exact_psi1(z) for z in ideals}
    core_phase_to_core = {}
    good = []
    for z in ideals:
        n = norm(z)
        if math.gcd(n, q) != 1:
            continue
        content = math.gcd(abs(z[0]), abs(z[1]))
        core = canonical((z[0] // content, z[1] // content))
        require(norm(z) == content * content * norm(core), "norm/content identity")
        require(phases[z] == phases[core], "rational content changed angular phase")
        phase = phases[core]
        require(phase[0] ** 2 - phase[0] * phase[1] + phase[1] ** 2 == 1,
                "exact angular value is not a unit complex number")
        previous = core_phase_to_core.setdefault(phase, core)
        require(previous == core, "two distinct primitive cores have one angular phase")
        expected = 0
        if math.gcd(content, q * norm(core)) == 1:
            expected = (mobius[core] * rational_mu(content, spf) ** 2
                        * chi3(content))
        require(mobius[z] == expected, "actual Mobius sign differs from ray identity")
        if mobius[core]:
            core_factors = factor(norm(core), spf)
            require(all(p % 3 == 1 and e == 1 for p, e in core_factors),
                    "squarefree primitive core is not split-supported")
        good.append((z, n, content, core, mobius[z]))

    rows = []
    for x in (64, 128, 256, 512, 1024):
        native = defaultdict(int)
        unsigned = defaultdict(int)
        for z, n, content, core, mu in good:
            if x / 2 < n <= x and mu:
                native[core] += mu
                unsigned[core] += 1
        for core in list(native):
            n = norm(core)
            upper = math.isqrt(x // n)
            expected = 0
            for a in range(1, upper + 1):
                if x < 2 * a * a * n <= 2 * x and math.gcd(a, q * n) == 1:
                    expected += rational_mu(a, spf) ** 2 * chi3(a)
            require(native[core] == mobius[core] * expected,
                    "independent ray sum does not reproduce full ideal source")
        diagonal = sum(value * value for value in native.values())
        unsigned_diagonal = sum(value * value for value in unsigned.values())
        rows.append({
            "X": x,
            "nonzero_squarefree_ideals_in_window": sum(unsigned.values()),
            "rays_present_before_cancellation": len(unsigned),
            "rays_with_nonzero_native_sum": sum(value != 0 for value in native.values()),
            "native_ray_diagonal_exact": diagonal,
            "unsigned_ray_diagonal_exact": unsigned_diagonal,
            "native_diagonal_divided_by_X": diagonal / x,
        })

    x = 512
    native = defaultdict(int)
    original_terms = []
    for z, n, content, core, mu in good:
        if x / 2 < n <= x and mu:
            native[core] += mu
            original_terms.append((mu, cmath.phase(to_complex(phases[z]))))
    angles = [(value, cmath.phase(to_complex(phases[core])))
              for core, value in native.items() if value]
    discrepancies = []
    for ell in (0, 1, 2, 7, 19):
        raw = sum(mu * cmath.exp(1j * ell * angle) for mu, angle in original_terms)
        grouped = sum(value * cmath.exp(1j * ell * angle) for value, angle in angles)
        discrepancy = abs(raw - grouped)
        require(discrepancy < 1e-10, "floating raw/grouped native source mismatch")
        discrepancies.append(discrepancy)
    all_core_angles = sorted(cmath.phase(to_complex(phases[core]))
                             for core in native)
    gaps = [right - left for left, right in zip(all_core_angles, all_core_angles[1:])]
    gaps.append(all_core_angles[0] + 2 * math.pi - all_core_angles[-1])
    minimum_gap = min(gaps)
    require(minimum_gap + 1e-12 >= 3 * math.sqrt(3) / x,
            "primitive ray determinant separation failed")

    gaussian_rows = []
    diagonal = sum(value * value for value, _ in angles)
    for width, center in ((4, 0), (32, 0), (512, 0), (32, 7)):
        cap = math.ceil(8 * width)
        weights = [math.exp(-j * j / (2 * width * width))
                   for j in range(-cap, cap + 1)]
        normalization = math.fsum(weights)
        direct_terms = []
        for offset, weight in zip(range(-cap, cap + 1), weights):
            ell = center + offset
            value = sum(coefficient * cmath.exp(1j * ell * angle)
                        for coefficient, angle in angles)
            direct_terms.append(weight * abs(value) ** 2)
        direct = math.fsum(direct_terms) / normalization
        periodic_denominator = math.fsum(
            math.exp(-2 * math.pi ** 2 * width ** 2 * j * j)
            for j in range(-2, 3)
        )
        kernel_terms = []
        for coefficient, angle in angles:
            for coefficient2, angle2 in angles:
                delta = math.remainder(angle - angle2, 2 * math.pi)
                theta = math.fsum(
                    math.exp(-width ** 2 * (delta - 2 * math.pi * j) ** 2 / 2)
                    for j in range(-2, 3)
                ) / periodic_denominator
                kernel_terms.append(coefficient * coefficient2 * theta
                                    * math.cos(center * delta))
        kernel = math.fsum(kernel_terms)
        discrepancy = abs(direct - kernel)
        require(discrepancy < 1e-8, "finite Gaussian normalization mismatch")
        gaussian_rows.append({
            "X": x, "width_R": width, "angular_center": center,
            "radial_parameter": 0,
            "finite_angular_sum_8_sigma": round(direct, 12),
            "periodized_kernel_5_images": round(kernel, 12),
            "absolute_difference": round(discrepancy, 14),
            "exact_ray_diagonal": diagonal,
        })

    return {
        "Q": q,
        "maximum_ideal_norm": limit,
        "all_ideals_enumerated_modulo_six_units": len(ideals),
        "good_ideals_checked_including_nonsquarefree": len(good),
        "independent_prime_ideal_factorization": True,
        "exact_Fraction_angular_phase_checked": True,
        "primitive_angle_collision_classes_checked": True,
        "hard_window_fixtures": rows,
        "largest_raw_grouped_float_error": round(max(discrepancies), 14),
        "minimum_core_angle_gap_times_X_at_X512": round(minimum_gap * x, 12),
        "determinant_bound_3sqrt3": round(3 * math.sqrt(3), 12),
        "finite_gaussian_replay": gaussian_rows,
    }


def hull_fixture(limit=200000, q=6):
    spf = sieve_spf(limit)
    ideals_by_norm = [0] * (limit + 1)
    direct_hull = [0] * (limit + 1)
    ideals_by_norm[1] = direct_hull[1] = 1
    for n in range(2, limit + 1):
        ideal_coefficient = 1
        hull_coefficient = 1
        for p, exponent in factor(n, spf):
            if q % p == 0:
                ideal_coefficient = hull_coefficient = 0
                break
            if p % 3 == 1:
                ideal_coefficient *= exponent + 1
                hull_coefficient *= (2 if exponent == 1 else 1 if exponent == 2 else 0)
            elif p % 3 == 2:
                ideal_coefficient *= 1 if exponent % 2 == 0 else 0
                hull_coefficient *= -1 if exponent == 2 else 0
            else:
                raise RuntimeError("unexpected unexcluded ramified prime")
        ideals_by_norm[n] = ideal_coefficient
        direct_hull[n] = hull_coefficient
    convolution_hull = [0] * (limit + 1)
    for d in range(1, math.isqrt(limit) + 1):
        coefficient = 1
        for p, exponent in factor(d, spf):
            if q % p == 0:
                coefficient = 0
                break
            coefficient *= (-2 if exponent == 1 else 1 if exponent == 2 else 0)
        if coefficient:
            square = d * d
            for m in range(1, limit // square + 1):
                convolution_hull[square * m] += coefficient * ideals_by_norm[m]
    require(direct_hull == convolution_hull, "hull Euler quotient coefficient identity")
    constant = 9 * math.sqrt(3) / (2 * math.pi ** 3)
    points = (100, 1000, 10000, 100000, limit)
    rows = []
    cumulative = 0
    for n in range(1, limit + 1):
        cumulative += direct_hull[n]
        if n in points:
            rows.append({
                "Y": n,
                "exact_signed_cumulative_hull": cumulative,
                "density_observed": round(cumulative / n, 12),
                "density_predicted": round(constant, 12),
                "error_divided_by_sqrtY_log3Y_squared": round(
                    (cumulative - constant * n) / (math.sqrt(n) * math.log(3 * n) ** 2),
                    12,
                ),
            })
    return {
        "Q": q,
        "coefficients_checked_exactly_through": limit,
        "direct_split_inert_Euler_factors_equal_quotient_convolution": True,
        "density_samples_not_asymptotic_certificates": rows,
    }


def main():
    report = {
        "status": "all exact finite checks and floating normalization replays passed",
        "scope": "finite source fixtures; no numerical proof of asymptotics or RH",
        "native_ideal_fixture": ray_fixture(),
        "angular_hull_fixture": hull_fixture(),
    }
    target = Path(__file__).with_name("NATIVE_ANGULAR_CHECK_RESULTS.json")
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    target.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
