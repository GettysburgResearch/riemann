#!/usr/bin/env python3
"""Complete native half-geodesic factors, actual measure and exchange controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha1, sha256
from itertools import product
from math import isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "GEODESIC_FACTOR_EXCHANGE.md"
FIXTURE = HERE / "geodesic_factor_exchange.json"
TEST = ROOT / "tests" / "test_native_six_hour_geodesic_exchange.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
PREDECESSOR = "1904d20cdb76ecd26e0e63472625da930075303e"
DENSE = "1fea3c9ce079325d19f5b43c6daa59c76afff921"
DENSE_JSON = "research/riemann-structures/dense_owner_principal_coefficient_family.json"
SOURCES = {
    (
        OLD,
        "claims/lemmas/L-102700-half-divisor-factorization-of-completion-defect.md",
    ): "6d68773121a8c9d32e151f9e83d1546da4814d80",
    (
        OLD,
        "claims/lemmas/L-102701-common-mother-ratiofour-two-field-form.md",
    ): "70eb455a3b2bb0398f8bba22dee82c39ef803156",
    (
        OLD,
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
    ): "6810bcece309b0c54ae6c8fc84b314990004549c",
    (
        OLD,
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
    ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    (
        FAMILY,
        "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md",
    ): "cf40354ff8810a2d4bea9459cf142c300ba36237",
    (
        PREDECESSOR,
        "research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md",
    ): "7cebffd3b6b0db96128755e392f622029a74435a",
    (DENSE, DENSE_JSON): "1c289fb3c7d8e959b010267751834ebad6914ec5",
}
MAX_BYTES = 1048576
MAX_DEGREE = 48


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lower=0, upper=64):
    require(type(value) is int and lower <= value <= upper, "bounded exact integer")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "declared source")
    ref = f"{key[0]}:{key[1]}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(len(raw) == size, "source length")
    require(
        sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == SOURCES[key],
        "exact Git blob authentication",
    )
    return raw


def poly(values):
    require(len(values) <= MAX_DEGREE + 1, "polynomial degree cap")
    result = [Fraction(value) for value in values]
    while result and not result[-1]:
        result.pop()
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 4096
            for x in result
        ),
        "rational bit cap",
    )
    return tuple(result)


def add(a, b):
    return poly(
        [
            (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))
        ]
    )


def scale(a, b):
    return poly([x * b for x in a])


def multiply(a, b):
    if not a or not b:
        return ()
    require(len(a) + len(b) - 2 <= MAX_DEGREE, "product degree cap")
    result = [Fraction()] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return poly(result)


def polynomial_product(items):
    result = poly([1])
    for item in items:
        result = multiply(result, item)
    return result


def derivative(a):
    return poly([i * a[i] for i in range(1, len(a))])


def integral(a):
    return sum((x / (i + 1) for i, x in enumerate(a)), Fraction())


def evaluate(a, x):
    require(type(x) in (int, Fraction), "exact evaluation parameter")
    value = Fraction()
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


@lru_cache(maxsize=8, typed=True)
def sqrt_coefficient(degree):
    integer(degree, upper=4)
    result = Fraction(1)
    for k in range(degree):
        result *= Fraction(1, 2) - k
        result /= k + 1
        result *= -1
    return result


@lru_cache(maxsize=32, typed=True)
def local(degree, schedule_power=1):
    integer(degree, upper=4)
    integer(schedule_power, lower=1, upper=3)
    start = sqrt_coefficient(degree // 2) if degree % 2 == 0 else Fraction()
    end = sqrt_coefficient(degree)
    return poly([start] + [0] * (schedule_power - 1) + [end - start])


@lru_cache(maxsize=32, typed=True)
def prime(value):
    integer(value, lower=2, upper=2000000)
    require(
        value == 2
        or (value % 2 and all(value % d for d in range(3, isqrt(value) + 1, 2))),
        "literal prime label",
    )
    return value


def validate_spec(labels, exponents):
    require(
        type(labels) is tuple
        and type(exponents) is tuple
        and len(labels) == len(exponents),
        "equal tuple lengths",
    )
    require(
        1 <= len(labels) <= 9 and len(set(labels)) == len(labels),
        "distinct bounded labels",
    )
    for p, e in zip(labels, exponents, strict=True):
        prime(p)
        integer(e, lower=1, upper=4)
    require(prod(e + 1 for e in exponents) <= 4096, "complete allocation count cap")


@lru_cache(maxsize=256)
def pattern_data(pattern):
    """Preserve each derivative site, caching only its exponent-pattern algebra."""
    require(type(pattern) is tuple and len(pattern) <= 9, "pattern cap")
    for e, a in pattern:
        integer(e, lower=1, upper=4)
        integer(a, upper=e)
    left_factors = [local(a) for _, a in pattern]
    right = polynomial_product(local(e - a) for e, a in pattern)
    left = polynomial_product(left_factors)
    sites = []
    site_sum = ()
    for i, (_, a) in enumerate(pattern):
        if not a:
            continue
        term = polynomial_product(
            [derivative(left_factors[i]), right]
            + left_factors[:i]
            + left_factors[i + 1 :]
        )
        site_sum = add(site_sum, term)
        sites.append((i, term))
    direct = multiply(derivative(left), right)
    require(site_sum == direct, "all derivative sites equal full chain-rule derivative")
    value = 2 * integral(direct)
    endpoint = evaluate(multiply(left, right), 1) - evaluate(multiply(left, right), 0)
    return {
        "value": value,
        "endpoint": endpoint,
        "primitive_site_diagonal": sum(
            (2 * integral(multiply(v, v)) for _, v in sites), Fraction()
        ),
        "integrated_site_diagonal": sum(
            ((2 * integral(v)) ** 2 for _, v in sites), Fraction()
        ),
        "sites": tuple((i, 2 * integral(v)) for i, v in sites),
    }


def factor_control(labels, exponents, selected_n):
    validate_spec(labels, exponents)
    K = prod(p**e for p, e in zip(labels, exponents, strict=True))
    require(
        type(selected_n) is int and selected_n > 0 and K % selected_n == 0,
        "selected divisor",
    )
    total = Fraction()
    site_diagonal = Fraction()
    integrated_site_diagonal = Fraction()
    aggregated_diagonal = Fraction()
    symmetric_diagonal = Fraction()
    antisymmetric_diagonal = Fraction()
    pattern_counts = Counter()
    coefficient_counts = Counter()
    record_hash = sha256()
    selected = {}
    sectors = {
        "exactly_two_odd_each": [0, Fraction()],
        "and_two_squared_each": [0, Fraction()],
    }
    root_free = True
    for allocation in product(*(range(e + 1) for e in exponents)):
        pattern = tuple(sorted(zip(exponents, allocation, strict=True)))
        data = pattern_data(pattern)
        reverse = pattern_data(tuple(sorted((e, e - a) for e, a in pattern)))
        value, reflected = data["value"], reverse["value"]
        require(
            value + reflected == 2 * data["endpoint"],
            "pointwise exchange endpoint identity",
        )
        n = prod(p**a for p, a in zip(labels, allocation, strict=True))
        m = K // n
        site_by_exponents = {pattern[i]: v for i, v in data["sites"]}
        physical_sites = [
            [p, str(site_by_exponents[(e, a)])]
            for p, e, a in zip(labels, exponents, allocation, strict=True)
            if a
        ]
        record = {
            "n": n,
            "m": m,
            "allocation": allocation,
            "coefficient": str(value),
            "integrated_derivative_sites_by_prime": physical_sites,
        }
        record_hash.update((canonical(record) + "\n").encode())
        pattern_counts[pattern] += 1
        coefficient_counts[str(value)] += 1
        total += value
        site_diagonal += data["primitive_site_diagonal"]
        integrated_site_diagonal += data["integrated_site_diagonal"]
        aggregated_diagonal += value**2
        symmetric_diagonal += ((value + reflected) / 2) ** 2
        antisymmetric_diagonal += ((value - reflected) / 2) ** 2
        if n in (1, K, selected_n, K // selected_n):
            selected[str(n)] = record | {
                "summed_derivative_site_count": len(data["sites"]),
                "integrated_sites_by_sorted_exponent_pattern": [
                    [i, str(v)] for i, v in data["sites"]
                ],
                "endpoint_symmetric_coefficient": str(data["endpoint"]),
            }
        if n == 1:
            root_free = value == 0 and not data["sites"]
        right_exponents = tuple(
            e - a for e, a in zip(exponents, allocation, strict=True)
        )
        if sum(a % 2 for a in allocation) == sum(a % 2 for a in right_exponents) == 2:
            sectors["exactly_two_odd_each"][0] += 1
            sectors["exactly_two_odd_each"][1] += value
            if (
                sum(a == 2 for a in allocation) >= 2
                and sum(a == 2 for a in right_exponents) >= 2
            ):
                sectors["and_two_squared_each"][0] += 1
                sectors["and_two_squared_each"][1] += value
    beta = (-1) ** len(labels) if all(e == 1 for e in exponents) else 0
    beta_square = (-1) ** len(labels) if all(e == 2 for e in exponents) else 0
    require(total == beta - beta_square, "complete native endpoint coefficient")
    require(root_free, "native root-free left tangent")
    require(
        aggregated_diagonal == symmetric_diagonal + antisymmetric_diagonal,
        "counting coefficient exchange orthogonality",
    )
    patterns = []
    for pattern, count in sorted(pattern_counts.items()):
        data = pattern_data(pattern)
        patterns.append(
            {
                "pattern": pattern,
                "multiplicity": count,
                "coefficient": str(data["value"]),
                "sites": [[i, str(v)] for i, v in data["sites"]],
            }
        )
    return {
        "labels": labels,
        "exponents": exponents,
        "K": K,
        "complete_factor_count": prod(e + 1 for e in exponents),
        "streamed_physical_records_sha256": record_hash.hexdigest(),
        "coalesced_patterns": patterns,
        "coefficient_histogram": dict(sorted(coefficient_counts.items())),
        "complete_stripped_coefficient": str(total),
        "endpoint_beta_minus_beta_square": beta - beta_square,
        "selected_records": selected,
        "physical_odd_owner_sectors": {
            name: {"count": value[0], "coefficient": str(value[1])}
            for name, value in sectors.items()
        },
        "primitive_site_diagonal_times_K": str(site_diagonal),
        "separately_integrated_site_diagonal_times_K": str(integrated_site_diagonal),
        "aggregated_coefficient_diagonal_times_K": str(aggregated_diagonal),
        "symmetric_diagonal_times_K": str(symmetric_diagonal),
        "antisymmetric_diagonal_times_K": str(antisymmetric_diagonal),
        "primitive_measure": "2 d_tau; not probability",
        "left_unit_zero_right_unit_retained": True,
        "Mellin_orthogonality": "proof via real kappa, even nu and exact reflection intertwining",
        "site_aggregation_is_an_isometry": False,
    }


def deformation_control(k):
    integer(k, lower=1, upper=3)
    u, v = local(1, 1), local(1, k)
    pq = 2 * integral(multiply(derivative(u), v))
    qp = 2 * integral(multiply(u, derivative(v)))
    require(
        pq == Fraction(1, 2 * (k + 1)) and qp == Fraction(k, 2 * (k + 1)),
        "source-permitted path deformation with full chain rule",
    )
    unit_right = 2 * integral(derivative(multiply(u, v)))
    require(
        unit_right == Fraction(1, 2) and pq + qp + unit_right == 1,
        "deformed complete product",
    )
    return {
        "q_schedule_power": k,
        "p_q": str(pq),
        "q_p": str(qp),
        "pq_unit": str(unit_right),
        "unit_pq": "0",
        "symmetric_each": "1/4",
        "antisymmetric_p_q": str((pq - qp) / 2),
        "complete_endpoint": "1",
        "positive_ratio_energy_changes": k != 1,
        "original_product_current_changes": False,
    }


def zero_spec():
    return (
        (2, 3, 5, 7, 71, 73, 79, 401, 421),
        (1, 1, 1, 1, 2, 2, 2, 2, 2),
        1005930209094,
    )


def held_out_spec(native):
    require(
        type(native) is dict
        and native.get("schema")
        == "riemann.dense_owner_principal_coefficient_family.v1",
        "frozen dense schema",
    )
    require(
        native.get("full_gamma_source_identified_with_projection") is False,
        "native gamma scope",
    )
    row = native["record"]
    labels = (1049639, 1050713, 1051747, 1052797, row["g"], row["ell"], row["rho"])
    exponents = (1, 1, 1, 1, 4, 2, 2)
    first = row["entries"][0]
    N = labels[0] * labels[1] * (labels[4] * labels[5]) ** 2
    M = labels[2] * labels[3] * (labels[4] * labels[6]) ** 2
    require(
        type(first["N"]) is int
        and type(first["M"]) is int
        and (first["N"], first["M"]) == (N, M),
        "held-out physical coefficient",
    )
    return labels, exponents, N


def replay_equal(candidate, expected):
    require(canonical(candidate) == canonical(expected), "typed canonical replay")


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    zero = factor_control(*zero_spec())
    positive = factor_control(*held_out_spec(json.loads(raw[(DENSE, DENSE_JSON)])))
    require(zero["complete_factor_count"] == 3888, "full zero dependency cone")
    require(
        zero["physical_odd_owner_sectors"]["exactly_two_odd_each"]
        == {"count": 192, "coefficient": "-3/8192"},
        "complete physical owner sector",
    )
    require(
        zero["physical_odd_owner_sectors"]["and_two_squared_each"]
        == {"count": 120, "coefficient": "-15/65536"},
        "complete balanced-size physical sector",
    )
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.geodesic_exchange.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "blob": value}
            for key, value in SOURCES.items()
        ],
        "source_hashes": bindings,
        "zero_chart": zero,
        "held_out_positive_chart": positive,
        "deformations": [deformation_control(k) for k in range(1, 4)],
        "fixed_product_Hankel_observation_preserved": True,
        "ratio_Mellin_observation_preserved_by_path_deformation": False,
        "exchange_projector_preserves_every_fixed_conductor_fibre": False,
        "complete_post_renewal_gamma_identified": False,
        "native_principal_moment_counterexample": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact byte cap")
        replay_equal(json.loads(FIXTURE.read_text(encoding="utf-8")), result)
    print(f"PASS native geodesic exchange {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
