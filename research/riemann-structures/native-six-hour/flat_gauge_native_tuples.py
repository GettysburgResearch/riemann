#!/usr/bin/env python3
"""Exact native complementary-source tuples and flat-gauge coinvariants."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from functools import lru_cache
from hashlib import sha1, sha256
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTE = HERE / "FLAT_GAUGE_NATIVE_TUPLES.md"
FIXTURE = HERE / "flat_gauge_native_tuples.json"
TEST = ROOT / "tests" / "test_native_six_hour_flat_gauge.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
PREDECESSOR = "1904d20cdb76ecd26e0e63472625da930075303e"
DENSE = "1fea3c9ce079325d19f5b43c6daa59c76afff921"
DENSE_JSON = "research/riemann-structures/dense_owner_principal_coefficient_family.json"
SOURCES = {
    (
        OLD,
        "claims/lemmas/L-102901-primewise-complementary-temperatures-form-an-infinite-dimensional-flat-gauge.md",
    ): "65fa60eb0ac25ea9797eba3d057bc765cb10c1cd",
    (
        OLD,
        "claims/lemmas/L-102903-sparse-endpoint-gauge-gives-unique-critical-prime-placement.md",
    ): "1adb6a98327784259114d5da29823a7ec6405e8a",
    (
        OLD,
        "claims/lemmas/L-102904-endpoint-color-walsh-expansion-has-only-squared-activity-off-the-midpoint.md",
    ): "f0bdbf09e620027eafe9a198350f588edafdd269",
    (
        OLD,
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
    ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md",
    ): "b988b14eb982504a799158eed4c76e7f033c96f0",
    (
        FAMILY,
        "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
    ): "388c7e166a0e6e534d7e908685f71a16de246575",
    (
        FAMILY,
        "claims/lemmas/L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
    ): "cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df",
    (
        PREDECESSOR,
        "research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md",
    ): "7cebffd3b6b0db96128755e392f622029a74435a",
    (DENSE, DENSE_JSON): "1c289fb3c7d8e959b010267751834ebad6914ec5",
}
MAX_BYTES = 524288
MAX_POLY_DEGREE = 32


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def exact_int(value, lower=0, upper=256):
    require(type(value) is int and lower <= value <= upper, "bounded exact integer")
    return value


def source_bytes(key):
    require(key in SOURCES, "declared frozen source")
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
        ["git", "show", ref],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    require(len(raw) == size, "source length")
    require(
        sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == SOURCES[key],
        "source Git blob authentication",
    )
    return raw


def poly(values):
    require(len(values) <= MAX_POLY_DEGREE + 1, "polynomial degree cap")
    result = [Fraction(value) for value in values]
    while result and result[-1] == 0:
        result.pop()
    require(
        all(
            max(v.numerator.bit_length(), v.denominator.bit_length()) <= 2048
            for v in result
        ),
        "coefficient bit cap",
    )
    return tuple(result)


def add(left, right):
    return poly(
        [
            (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
            for i in range(max(len(left), len(right)))
        ]
    )


def scale(value, scalar):
    return poly([coefficient * scalar for coefficient in value])


def multiply(left, right):
    if not left or not right:
        return ()
    require(len(left) + len(right) - 2 <= MAX_POLY_DEGREE, "product degree cap")
    result = [Fraction()] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly(result)


def power(value, exponent):
    exact_int(exponent, upper=16)
    result = poly([1])
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def evaluate(value, parameter):
    require(type(parameter) in (int, Fraction), "exact rational temperature")
    parameter = Fraction(parameter)
    require(
        max(parameter.numerator.bit_length(), parameter.denominator.bit_length()) <= 32,
        "temperature bit cap",
    )
    result = Fraction()
    for coefficient in reversed(value):
        result = result * parameter + coefficient
    return result


@lru_cache(maxsize=32, typed=True)
def binomial_polynomial(degree):
    exact_int(degree, upper=8)
    result = poly([1])
    for j in range(degree):
        result = scale(multiply(result, poly([-j, 1])), Fraction(1, j + 1))
    return result


@lru_cache(maxsize=32, typed=True)
def half_coefficient(degree):
    exact_int(degree, upper=8)
    current = binomial_polynomial(degree)
    return (
        current
        if degree == 0
        else add(current, scale(binomial_polynomial(degree - 1), -1))
    )


def complement(value):
    result = ()
    for degree, coefficient in enumerate(value):
        result = add(result, scale(power(poly([1, -1]), degree), coefficient))
    return result


def local_allocations(degree):
    exact_int(degree, upper=8)
    return [
        multiply(half_coefficient(a), complement(half_coefficient(degree - a)))
        for a in range(degree + 1)
    ]


def local_product_control(degree):
    rows = local_allocations(degree)
    total = ()
    for row in rows:
        total = add(total, row)
    expected = (1, -1, -1, 1)[degree] if degree <= 3 else 0
    require(total == poly([expected]), "complete native local product")
    midpoint = [evaluate(row, Fraction(1, 2)) for row in rows]
    energy = sum((value * value for value in midpoint), Fraction())
    return {
        "total_exponent": degree,
        "complete_allocation_count": len(rows),
        "temperature_polynomials": [[str(v) for v in row] for row in rows],
        "product_coefficient": expected,
        "midpoint_allocations": [str(value) for value in midpoint],
        "midpoint_ratio_energy_over_Gamma0_p_minus_n": str(energy),
        "orthogonality_scope": "one odd prime p>=3; spacing 2log(p)>log(8)",
    }


def bivariate_add(left, right):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, Fraction()) + value
        if not result[key]:
            del result[key]
    return result


def bivariate_scale(value, scalar):
    return {
        key: coefficient * scalar
        for key, coefficient in value.items()
        if coefficient * scalar
    }


def bivariate_multiply(left, right, degree):
    exact_int(degree, lower=1, upper=8)
    result = {}
    for (a, b), coefficient in left.items():
        for (c, d), other in right.items():
            if a + b + c + d <= degree:
                key = (a + c, b + d)
                result[key] = result.get(key, Fraction()) + coefficient * other
    return {key: value for key, value in result.items() if value}


def collapse(value):
    result = {}
    for (a, b), coefficient in value.items():
        result[a + b] = result.get(a + b, Fraction()) + coefficient
    return {key: value for key, value in result.items() if value}


def coinvariant_control(degree):
    exact_int(degree, lower=1, upper=8)
    generator = {}
    unit = {}
    for n in range(1, degree + 1):
        coefficient = Fraction((-1) ** (n + 1), n)
        generator[(n, 0)] = coefficient
        generator[(0, n)] = -coefficient
        for a in range(n):
            unit[(n - 1 - a, a)] = coefficient
    difference = {(1, 0): Fraction(1), (0, 1): Fraction(-1)}
    require(bivariate_multiply(difference, unit, degree) == generator, "L=(x-y)unit")
    identity = {(0, 0): Fraction(1)}
    nilpotent = bivariate_add(unit, {(0, 0): Fraction(-1)})
    inverse = dict(identity)
    term = dict(identity)
    for _ in range(degree):
        term = bivariate_multiply(term, bivariate_scale(nilpotent, -1), degree)
        inverse = bivariate_add(inverse, term)
    require(
        bivariate_multiply(unit, inverse, degree) == identity, "finite unit inverse"
    )
    require(
        bivariate_multiply(generator, inverse, degree) == difference,
        "same generated ideal",
    )
    multipliers = 0
    for total in range(degree):
        for a in range(total + 1):
            monomial = {(a, total - a): Fraction(1)}
            require(
                not collapse(bivariate_multiply(generator, monomial, degree)),
                "every bounded source multiplier is killed after product collapse",
            )
            multipliers += 1
    return {
        "D": degree,
        "ambient_basis_count": comb(degree + 2, 2),
        "difference_ideal_basis_count": multipliers,
        "quotient_basis_count": degree + 1,
        "L_equals_difference_times_unit": True,
        "finite_inverse_verified": True,
        "physical_ratio_degree_one_formal_modes": [
            {"total_activity_degree": 1, "ratio_exponent": 1, "coefficient": 1},
            {"total_activity_degree": 1, "ratio_exponent": -1, "coefficient": -1},
        ],
        "physical_ratio_readout_is_truncated_ring_homomorphism": False,
    }


@lru_cache(maxsize=32, typed=True)
def prime(value):
    exact_int(value, lower=2, upper=2000000)
    require(
        all(value % divisor for divisor in range(2, isqrt(value) + 1)),
        "exact fixture prime",
    )
    return value


def boolean_histories(support, cutoff):
    exact_int(cutoff, lower=2, upper=2000000)
    require(type(support) is tuple and 1 <= len(support) <= 5, "bounded core support")
    support = tuple(prime(value) for value in support)
    require(len(set(support)) == len(support), "squarefree core labels")

    def a_u(part):
        total = 0
        for bits in product((0, 1), repeat=len(part)):
            divisor = prod(p for p, bit in zip(part, bits, strict=True) if bit)
            if divisor <= cutoff:
                total += (-1) ** sum(bits)
        return int(not part) - total

    rows = []
    for assignment in product(range(3), repeat=len(support)):
        parts = [
            tuple(p for p, tag in zip(support, assignment, strict=True) if tag == j)
            for j in range(3)
        ]
        coefficient = a_u(parts[0]) * a_u(parts[1]) * (-1) ** len(parts[2])
        if coefficient:
            r, s, m = (prod(part) for part in parts)
            require(r > cutoff and s > cutoff, "literal balanced support")
            rows.append({"r": r, "s": s, "m": m, "coefficient": coefficient})
    return {
        "complete_allocations": 3 ** len(support),
        "nonzero_histories": rows,
        "b_U": sum(row["coefficient"] for row in rows),
        "owner_pair_share": str(Fraction(1, comb(len(support) + 2, 2))),
    }


def tuple_spec(name, cutoff, owners_left, owners_right, core_left, core_right):
    require(type(name) is str and len(name) <= 32, "tuple name")
    for owners in (owners_left, owners_right):
        require(
            type(owners) is tuple and len(owners) == 2 and len(set(owners)) == 2,
            "two distinct owners",
        )
    all_owners = owners_left + owners_right
    require(len(set(all_owners)) == 4, "disjoint owner pairs")
    require(
        not set(all_owners).intersection(core_left + core_right),
        "clean owner/core split",
    )
    left = boolean_histories(core_left, cutoff)
    right = boolean_histories(core_right, cutoff)
    for value in all_owners:
        prime(value)
    labels = sorted(set(all_owners + core_left + core_right))
    require(
        len(labels) <= 11 and 67 not in labels, "bounded clean ordinary-prime fixture"
    )
    incidence = []
    for p in labels:
        a = int(p in owners_left) + 2 * int(p in core_left)
        b = int(p in owners_right) + 2 * int(p in core_right)
        incidence.append((p, a, b))
    n = prod(p**a for p, a, _ in incidence)
    m = prod(p**b for p, _, b in incidence)
    require(max(n.bit_length(), m.bit_length()) <= 128, "physical index bit cap")
    p_owner, q_owner = prod(owners_left), prod(owners_right)
    common = gcd(prod(core_left), prod(core_right))
    require(Fraction(1, 8) < Fraction(n, m) < 8, "physical ratio-eight chart")
    require(n <= 16 * cutoff**6 and m <= 16 * cutoff**6, "physical horizon")
    canonical_coefficient = (
        left["b_U"]
        * Fraction(left["owner_pair_share"])
        * right["b_U"]
        * Fraction(right["owner_pair_share"])
    )
    return {
        "name": name,
        "U": cutoff,
        "P": p_owner,
        "Q": q_owner,
        "g": common,
        "N": n,
        "M": m,
        "incidence": incidence,
        "left_boolean": left,
        "right_boolean": right,
        "canonical_stripped_coefficient": str(canonical_coefficient),
        "canonical_coefficient_square": str(canonical_coefficient**2 / (n * m)),
    }


def raw_temperature_polynomial(spec):
    result = poly([1])
    for _, a, b in spec["incidence"]:
        result = multiply(result, half_coefficient(a))
        result = multiply(result, complement(half_coefficient(b)))
    return result


def walsh(coefficients):
    require(
        type(coefficients) is list
        and 1 <= len(coefficients) <= 2048
        and len(coefficients) & (len(coefficients) - 1) == 0,
        "bounded full Walsh cube",
    )
    result = [Fraction(value) for value in coefficients]
    width = 1
    while width < len(result):
        for start in range(0, len(result), 2 * width):
            for offset in range(width):
                a, b = result[start + offset], result[start + width + offset]
                result[start + offset] = a + b
                result[start + width + offset] = a - b
        width *= 2
    return [value / len(result) for value in result]


def endpoint_colours(spec):
    incidence = spec["incidence"]
    require(1 <= len(incidence) <= 11, "endpoint cube cap")
    e, c = {0: 1, 1: -1}, {0: 1, 2: -1}
    values = []
    for bits in product((0, 1), repeat=len(incidence)):
        value = 1
        for (_, a, b), bit in zip(incidence, bits, strict=True):
            left, right = (e, c) if bit == 0 else (c, e)
            value *= left.get(a, 0) * right.get(b, 0)
        values.append(value)
    count = len(values)
    mean = Fraction(sum(values), count)
    diagonal = Fraction(sum(value * value for value in values), count)
    transform = walsh(values)
    require(
        sum((value * value for value in transform), Fraction()) == diagonal,
        "complete Walsh Parseval",
    )
    require(transform[0] == mean, "probability mean is the trivial Walsh coordinate")
    return {
        "complete_colour_count": count,
        "probability_per_colour": str(Fraction(1, count)),
        "nonzero_colour_coefficients": [
            {"index": index, "coefficient": value}
            for index, value in enumerate(values)
            if value
        ],
        "mean_stripped_coefficient": str(mean),
        "native_probability_diagonal_stripped": str(diagonal),
        "regrouped_mean_diagonal_stripped": str(mean * mean),
        "walsh_nonzero_count": sum(value != 0 for value in transform),
        "complete_walsh_coefficients": [str(value) for value in transform],
        "native_mean_coefficient_square": str(mean * mean / (spec["N"] * spec["M"])),
        "native_probability_diagonal": str(diagonal / (spec["N"] * spec["M"])),
    }


def tuple_control(spec):
    value = raw_temperature_polynomial(spec)
    panels = []
    for temperature in (
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1),
    ):
        scalar = evaluate(value, temperature)
        panels.append(
            {
                "temperature": str(temperature),
                "raw_stripped_coefficient": str(scalar),
                "physical_coefficient_square": str(
                    scalar * scalar / (spec["N"] * spec["M"])
                ),
            }
        )
    return {
        **spec,
        "raw_temperature_polynomial": [str(coefficient) for coefficient in value],
        "temperature_panels": panels,
        "endpoint_probability": endpoint_colours(spec),
        "all_omitted_physical_prime_labels_have_constant_coefficient_one": True,
        "post_renewal_gamma_identified": False,
        "raw_tensor_coefficient_equals_canonical_coefficient_claimed": False,
    }


def dense_spec(native):
    require(
        type(native) is dict
        and native.get("schema")
        == "riemann.dense_owner_principal_coefficient_family.v1",
        "frozen dense schema",
    )
    require(
        native.get("full_gamma_source_identified_with_projection") is False,
        "inherited gamma boundary",
    )
    record = native["record"]
    first = record["entries"][0]
    spec = tuple_spec(
        "held_out_positive",
        record["U"],
        (1049639, 1050713),
        (1051747, 1052797),
        (record["g"], record["ell"]),
        (record["g"], record["rho"]),
    )
    for key in ("P", "Q", "N", "M"):
        require(
            type(first[key]) is int and first[key] == spec[key], "frozen physical tuple"
        )
    require(
        Fraction(first["coefficient_square"])
        == Fraction(spec["canonical_coefficient_square"]),
        "frozen canonical square",
    )
    require(first["positive_branch"] is True, "positive square-root branch")
    return spec


def build():
    raw = {key: source_bytes(key) for key in SOURCES}
    zero = tuple_spec("zero_boolean", 64, (2, 3), (5, 7), (71, 73, 79), (401, 421))
    positive = dense_spec(json.loads(raw[(DENSE, DENSE_JSON)]))
    t = poly([0, 1])
    t_minus_one, t_minus_three, t_plus_two = poly([-1, 1]), poly([-3, 1]), poly([2, 1])
    zero_formula = scale(
        multiply(
            multiply(power(t, 5), power(t_minus_one, 4)),
            multiply(power(t_minus_three, 3), power(t_plus_two, 2)),
        ),
        Fraction(1, 32),
    )
    positive_formula = scale(
        multiply(
            multiply(power(t, 4), power(t_minus_one, 4)),
            multiply(power(t_minus_three, 2), power(t_plus_two, 2)),
        ),
        Fraction(1, 16),
    )
    require(
        raw_temperature_polynomial(zero) == zero_formula,
        "zero-chart exact polynomial identity",
    )
    require(
        raw_temperature_polynomial(positive) == positive_formula,
        "held-out exact polynomial identity",
    )
    bindings = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "owned file byte cap")
        bindings[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_six_hour.flat_gauge_tuples.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": value}
            for key, value in SOURCES.items()
        ],
        "source_hashes": bindings,
        "complete_local_source_products": [local_product_control(n) for n in range(9)],
        "coinvariant_controls": [coinvariant_control(degree) for degree in range(1, 7)],
        "zero_tuple": tuple_control(zero),
        "held_out_positive_tuple": tuple_control(positive),
        "two_distinct_prime_frequency_classification": "proof_only_unique_factorization",
        "module_coinvariants_not_differential_connection_quotient": True,
        "native_temperature_probability_measure_invented": False,
        "endpoint_probability_measure": "independent uniform signs from L-102904",
        "original_Mellin_measure_retained": True,
        "all_integrated_scalar_functionals_excluded": False,
        "complete_post_renewal_gamma_identification": False,
        "native_principal_moment_counterexample": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def replay_equal(candidate, expected):
    require(
        canonical(candidate) == canonical(expected), "strict typed canonical replay"
    )


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
    print(f"PASS native flat-gauge tuples {result['proof_object_sha256']}")


if __name__ == "__main__":
    main()
