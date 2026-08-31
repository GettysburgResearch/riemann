#!/usr/bin/env python3
"""Complete positive smooth-cost prefixes and original-source completion bounds."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from math import comb, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "primitive": (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        "6810bcece309b0c54ae6c8fc84b314990004549c",
    ),
    "kernel": (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
        "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    ),
    "completion": (
        "822646ffea23d906c385f0273a8c45693e982c4d",
        PREFIX + "FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md",
        "851e4331c12d9f3f073ab73dca26baa33bd5e548",
    ),
}
PRIMES = (2, 3, 5)
BITS = 512
DENOMINATOR = 2**BITS
MAX_BITS = 8192
MAX_DEGREE = 20
MAX_COST = 2**20
MAX_COSTS = 4096
MAX_BYTES = 8 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def bounded(value):
    require(type(value) in (int, F), "literal exact rational")
    result = F(value)
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= MAX_BITS,
        "registered rational bit cap",
    )
    return result


def rounded(value):
    require(type(value) is tuple and len(value) == 2, "rational interval pair")
    lo, hi = map(bounded, value)
    require(lo <= hi, "ordered exact interval")
    lower = lo.numerator * DENOMINATOR // lo.denominator
    upper = -((-hi.numerator * DENOMINATOR) // hi.denominator)
    return F(lower, DENOMINATOR), F(upper, DENOMINATOR)


def point(value):
    value = bounded(value)
    return rounded((value, value))


def add(left, right):
    return rounded((bounded(left[0] + right[0]), bounded(left[1] + right[1])))


def neg(value):
    return -value[1], -value[0]


def sub(left, right):
    return add(left, neg(right))


def mul(left, right):
    candidates = [bounded(a * b) for a in left for b in right]
    return rounded((min(candidates), max(candidates)))


def scale(value, coefficient):
    coefficient = bounded(coefficient)
    candidates = (bounded(value[0] * coefficient), bounded(value[1] * coefficient))
    return rounded((min(candidates), max(candidates)))


def total(values):
    result = point(0)
    for value in values:
        result = add(result, value)
    return result


def product_intervals(values):
    result = point(1)
    for value in values:
        result = mul(result, value)
    return result


def sqrt_endpoint(value, upper):
    value = bounded(value)
    require(
        value >= 0 and type(upper) is bool, "nonnegative exact square-root endpoint"
    )
    require(
        value.numerator.bit_length() + 2 * BITS <= MAX_BITS,
        "bounded square-root integer shift",
    )
    numerator = value.numerator << (2 * BITS)
    floor = isqrt(numerator // value.denominator)
    require(
        floor * floor * value.denominator
        <= numerator
        < (floor + 1) * (floor + 1) * value.denominator,
        "exact integer-square-root bracket",
    )
    if upper and floor * floor * value.denominator != numerator:
        floor += 1
    return F(floor, DENOMINATOR)


def sqrt_interval(value):
    lo, hi = value
    require(0 <= lo <= hi, "nonnegative square-root interval")
    return sqrt_endpoint(lo, False), sqrt_endpoint(hi, True)


def interval_json(value):
    lo, hi = value
    return {
        "lower": str(lo),
        "upper": str(hi),
        "approximate_midpoint": float((lo + hi) / 2),
    }


def log_two():
    terms = 256
    lower = bounded(
        2 * sum((F(1, 3 ** (2 * k + 1) * (2 * k + 1)) for k in range(terms)), F())
    )
    remainder = bounded(F(2, 3 ** (2 * terms + 1) * (2 * terms + 1)) / F(8, 9))
    return rounded((lower, bounded(lower + remainder)))


def beta(degree):
    require(
        type(degree) is int and 0 <= degree <= MAX_DEGREE,
        "declared local source degree",
    )
    if degree == 0:
        return F(1)
    return bounded(F(comb(2 * degree, degree), 4**degree * (2 * degree - 1)))


def convolve(left, right):
    require(
        len(left) == len(right) == MAX_DEGREE + 1,
        "complete bounded local coefficient arrays",
    )
    return [
        bounded(sum((left[k] * right[e - k] for k in range(e + 1)), F()))
        for e in range(MAX_DEGREE + 1)
    ]


def local_coefficients():
    source = [F(1)] + [-beta(e) for e in range(1, MAX_DEGREE + 1)]
    squared = convolve(source, source)
    require(
        squared == [F(1), F(-1)] + [F()] * (MAX_DEGREE - 1),
        "literal square-root source coefficient identity",
    )
    alpha = [F(1)] + [
        beta(e // 2) if e % 2 == 0 else beta(e) for e in range(1, MAX_DEGREE + 1)
    ]
    derivative = [F()] + [
        beta(e // 2) - beta(e) if e % 2 == 0 else beta(e)
        for e in range(1, MAX_DEGREE + 1)
    ]
    require(
        all(value > 0 for value in alpha)
        and all(value > 0 for value in derivative[1:]),
        "nonnegative coefficientwise source majorants",
    )
    return alpha, derivative, convolve(alpha, alpha), convolve(derivative, alpha)


def coefficient(powers, alpha_squared, derivative_alpha):
    require(
        type(powers) is tuple
        and len(powers) == 3
        and all(type(e) is int and 0 <= e <= MAX_DEGREE for e in powers),
        "literal smooth-cost powers",
    )
    return bounded(
        2
        * sum(
            (
                derivative_alpha[powers[i]]
                * alpha_squared[powers[(i + 1) % 3]]
                * alpha_squared[powers[(i + 2) % 3]]
                for i in range(3)
            ),
            F(),
        )
    )


def cost_rows(maximum, alpha_squared, derivative_alpha):
    require(
        type(maximum) is int and maximum in (60, MAX_COST),
        "declared complete acquisition maximum",
    )
    result = []
    for a in range(MAX_DEGREE + 1):
        power2 = 2**a
        if power2 > maximum:
            break
        for b in range(MAX_DEGREE + 1):
            base = power2 * 3**b
            if base > maximum:
                break
            for c in range(MAX_DEGREE + 1):
                cost = base * 5**c
                if cost > maximum:
                    break
                powers = (a, b, c)
                value = coefficient(powers, alpha_squared, derivative_alpha)
                require(value >= 0, "positive complete product-cost coefficient")
                result.append((cost, powers, value))
    result.sort()
    require(
        len(result) <= MAX_COSTS and len({row[0] for row in result}) == len(result),
        "bounded unique complete smooth costs",
    )
    return result


def majorant_total(local):
    return scale(
        total(
            mul(
                mul(row["D"], row["A"]),
                product_intervals(
                    mul(other["A"], other["A"])
                    for j, other in enumerate(local)
                    if j != i
                ),
            )
            for i, row in enumerate(local)
        ),
        2,
    )


def constants():
    local = []
    for prime in PRIMES:
        rho = sqrt_interval(point(F(1, prime)))
        minus = sqrt_interval(sub(point(1), rho))
        plus = sqrt_interval(add(point(1), rho))
        even = sqrt_interval(point(1 - F(1, prime)))
        derivative = sub(plus, even)
        actual = sub(point(2), minus)
        coefficientwise = add(sub(point(2), even), scale(sub(plus, minus), F(1, 2)))
        require(
            derivative[0] > 0 and actual[0] > 1 and coefficientwise[0] > 1,
            "positive closed local source sums",
        )
        local.append(
            {
                "prime": prime,
                "rho": rho,
                "D": derivative,
                "A_actual": actual,
                "A_max": coefficientwise,
            }
        )
    physical = majorant_total([{"A": row["A_actual"], "D": row["D"]} for row in local])
    coefficientwise = majorant_total(
        [{"A": row["A_max"], "D": row["D"]} for row in local]
    )
    root2 = sqrt_interval(point(2))
    endpoint = scale(root2, 192)
    mass = sub(scale(mul(add(point(3), root2), log_two()), 128), point(288))
    require(
        mass[0] > 0 and physical[0] > 0 and coefficientwise[0] > 0,
        "positive original measure and source bounds",
    )
    return local, physical, coefficientwise, endpoint, mass


def authenticate():
    require(
        "completion" in PINS,
        "completion theorem freeze must be installed before acquisition",
    )
    result = []
    for role, (commit, path, blob) in PINS.items():
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "bounded authenticated source proof")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(raw) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
            "exact completed-source proof identity",
        )
        result.append({"role": role, "commit": commit, "path": path, "blob": blob})
    return result


def discover(phase):
    require(phase in ("calibration", "heldout"), "declared positive-tail phase")
    sources = authenticate()
    horizons = (25, 30, 60) if phase == "calibration" else (900, MAX_COST)
    alpha, derivative, alpha_squared, derivative_alpha = local_coefficients()
    rows = cost_rows(max(horizons), alpha_squared, derivative_alpha)
    low = {cost: value for cost, _, value in rows if cost in (1, 2, 4, 6, 8)}
    require(
        low == {1: F(), 2: F(1), 4: F(5, 4), 6: F(2), 8: F(1)},
        "independent low-cost source controls",
    )
    local, physical, majorant, endpoint, mass = constants()
    records, panels, prefix = [], [], point(0)
    for cost, powers, value in rows:
        contribution = scale(sqrt_interval(point(F(1, cost))), value)
        prefix = add(prefix, contribution)
        records.append(
            {
                "cost": cost,
                "powers": list(powers),
                "exact_majorant_coefficient": str(value),
                "directed_contribution": interval_json(contribution),
            }
        )
        if cost in horizons:
            raw_tail = sub(majorant, prefix)
            require(
                raw_tail[1] >= 0, "positive majorant total-minus-prefix upper endpoint"
            )
            tail = max(F(), raw_tail[0]), raw_tail[1]
            endpoint_rate = mul(endpoint, sqrt_interval(point(F(1, cost))))
            field_upper = min(tail[1], endpoint_rate[1])
            hilbert_upper = mul(sqrt_interval(mass), point(field_upper))[1]
            energy_upper = scale(mul(mul(mass, physical), point(field_upper)), 2)[1]
            panels.append(
                {
                    "H": cost,
                    "complete_prefix_count": len(records),
                    "complete_prefix_costs": [row["cost"] for row in records],
                    "prefix_sha256": sha256(canonical(records).encode()).hexdigest(),
                    "positive_majorant_prefix": interval_json(prefix),
                    "raw_total_minus_prefix": interval_json(raw_tail),
                    "positive_majorant_remainder": interval_json(tail),
                    "independent_endpoint_rate": interval_json(endpoint_rate),
                    "uniform_field_error_upper": str(field_upper),
                    "uniform_Hilbert_error_upper": str(hilbert_upper),
                    "uniform_energy_and_minimum_error_upper": str(energy_upper),
                    "approximate_field_error_upper": float(field_upper),
                    "approximate_energy_error_upper": float(energy_upper),
                }
            )
    require(
        [row["H"] for row in panels] == list(horizons),
        "all complete registered prefixes",
    )
    owned = {
        path.relative_to(ROOT).as_posix(): sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in (
            Path(__file__),
            HERE / "NATIVE_POSITIVE_COMPLETION_TAIL.md",
            HERE / "NATIVE_POSITIVE_TAIL_PREREGISTRATION.md",
        )
    }
    result = {
        "schema": "riemann.native_six_hour.positive_completion_tail_discovery.v1",
        "phase": phase,
        "sources": sources,
        "owned_sha256_lf": owned,
        "interval_bits": BITS,
        "all_local_alpha_coefficients": list(map(str, alpha)),
        "all_local_absolute_derivative_coefficients": list(map(str, derivative)),
        "all_local_Amax_squared_coefficients": list(map(str, alpha_squared)),
        "all_local_D_Amax_coefficients": list(map(str, derivative_alpha)),
        "local_closed_sums": [
            {
                "prime": row["prime"],
                **{
                    key: interval_json(value)
                    for key, value in row.items()
                    if key != "prime"
                },
            }
            for row in local
        ],
        "original_kernel_mass": interval_json(mass),
        "uniform_physical_source_bound": interval_json(physical),
        "closed_positive_majorant_total": interval_json(majorant),
        "unweighted_endpoint_source_bound": interval_json(endpoint),
        "complete_smooth_cost_records": records,
        "panels": panels,
        "signed_observed_tail_evaluated": False,
        "optimal_path_persistence_claimed": False,
        "full_gamma_identified": False,
        "all_prime_limit_claimed": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    args = parser.parse_args()
    raw = (
        json.dumps(discover(args.phase), sort_keys=True, indent=2, allow_nan=False)
        + "\n"
    ).encode()
    require(len(raw) <= MAX_BYTES, "bounded complete positive-tail artifact")
    print(raw.decode(), end="")


if __name__ == "__main__":
    main()
