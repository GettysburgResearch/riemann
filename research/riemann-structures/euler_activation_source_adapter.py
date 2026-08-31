#!/usr/bin/env python3
"""Exact Euler activation/complement replay with primitive source normalization."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import comb, factorial, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "EULER_ACTIVATION_SOURCE_ADAPTER.md"
FIXTURE = HERE / "euler_activation_source_adapter.json"
TEST = ROOT / "tests" / "test_euler_activation_source_adapter.py"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SCB = "1623f1924c62035918a94bcacf2ccad7d3bb6cf7"
SOURCES = {
    (
        OLD,
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        OLD,
        "claims/lemmas/L-102709-regionwise-gauge-selection-is-source-exact.md",
    ): "6080f9c6d36f5654a69d2c8148d3aa4483f39dfb",
    (
        OLD,
        "claims/lemmas/L-102741-wick-gauge-and-exact-prime-carrier-quotient.md",
    ): "b526c4889f7027fee0fd1db69c41621cab8a0a23",
    (
        OLD,
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ): "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        SCB,
        "research/riemann-structures/SUBCRITICAL_OBSERVED_BOOLEAN_BLOCK.md",
    ): "6aa04020b9f4afd538928688be9ed68c01e293ae",
    (
        SCB,
        "research/riemann-structures/subcritical_observed_boolean_block.json",
    ): "b6464ebbd4560e50d9ad7033d051dc9cddd4a7f4",
}
MAX_BYTES = 262144


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key: tuple[str, str]) -> bytes:
    require(key in SOURCES, "frozen source identity")
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
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen source Git blob")
    return raw


def trim(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    require(type(poly) is tuple and 0 < len(poly) <= 70, "polynomial size cap")
    require(all(type(x) is Fraction for x in poly), "exact rational coefficients")
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def add(left, right):
    left, right = trim(left), trim(right)
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(tuple(out))


def multiply(left, right):
    left, right = trim(left), trim(right)
    require(len(left) + len(right) - 1 <= 70, "polynomial product cap")
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def scale(poly, scalar: int):
    require(type(scalar) is int and abs(scalar) <= 64, "integer density scale")
    return trim(tuple(scalar * x for x in trim(poly)))


def power(poly, exponent: int):
    require(type(exponent) is int and 0 <= exponent <= 32, "density exponent cap")
    out = (Fraction(1),)
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


def derivative(poly):
    poly = trim(poly)
    return trim(tuple(i * poly[i] for i in range(1, len(poly))) or (Fraction(0),))


def integral(poly) -> Fraction:
    return sum(
        (value / Fraction(i + 1) for i, value in enumerate(trim(poly))), Fraction(0)
    )


def density_record(k: int) -> dict[str, object]:
    require(type(k) is int and 1 <= k <= 16, "nonempty core depth cap")
    # Literal local coefficients in e_t: [x]e_t=-t, [x^2]e_t=-1+t.
    owner_local = (Fraction(0), Fraction(-1))
    core_local = (Fraction(-1), Fraction(1))
    coefficient = multiply(power(owner_local, 2), power(core_local, k))
    owner_site = multiply(
        multiply(derivative(owner_local), owner_local), power(core_local, k)
    )
    core_site = multiply(
        power(owner_local, 2),
        multiply(derivative(core_local), power(core_local, k - 1)),
    )
    owner, complement = scale(owner_site, 2), scale(core_site, k)
    require(add(owner, complement) == derivative(coefficient), "literal product rule")
    owner_integral, core_integral = integral(owner), integral(complement)
    native = Fraction((-1) ** k, comb(k + 2, 2))
    require(
        owner_integral == native and core_integral == -native, "exact source adapter"
    )
    require(integral(derivative(coefficient)) == 0, "complete raw mixed endpoint")
    site_time = integral(
        add(
            scale(multiply(owner_site, owner_site), 2),
            scale(multiply(core_site, core_site), k),
        )
    )
    site = 2 * integral(owner_site) ** 2 + k * integral(core_site) ** 2
    sectors = owner_integral**2 + core_integral**2
    require(
        site_time == Fraction(4, (2 * k - 1) * (2 * k + 1) * (2 * k + 3)),
        "primitive site-time diagonal",
    )
    require(site == Fraction(2, k * (k + 1) ** 2 * (k + 2)), "integrated-site diagonal")
    require(sectors == Fraction(8, (k + 1) ** 2 * (k + 2) ** 2), "two-sector diagonal")
    return {
        "core_depth": k,
        "full_coefficient_polynomial": [str(x) for x in coefficient],
        "owner_density": [str(x) for x in owner],
        "core_density": [str(x) for x in complement],
        "owner_coefficient_before_physical_weight": str(owner_integral),
        "core_coefficient_before_physical_weight": str(core_integral),
        "site_time_diagonal_times_N": str(site_time),
        "integrated_site_diagonal_times_N": str(site),
        "two_sector_diagonal_times_N": str(sectors),
        "linear_total": "0",
        "centered_site_time_form_times_N": str(-site_time),
    }


def raw_coefficients(exponents: tuple[int, ...]) -> dict[str, Fraction]:
    require(type(exponents) is tuple and 1 <= len(exponents) <= 18, "label cap")
    require(
        all(type(e) is int and 0 <= e <= 2 for e in exponents), "literal exponent cap"
    )
    e_coeff = prod(Fraction((-1) ** e) if e <= 1 else Fraction(0) for e in exponents)
    s_coeff = prod(
        Fraction(-1) if e == 2 else Fraction(1) if e == 0 else Fraction(0)
        for e in exponents
    )

    def rs_local(e):
        return Fraction(1, factorial(e)) - (Fraction(1, factorial(e - 1)) if e else 0)

    carrier = Fraction(0)
    for site, exponent in enumerate(exponents):
        if exponent:
            carrier -= prod(
                rs_local(value - (index == site))
                for index, value in enumerate(exponents)
            )
    return {
        "E": e_coeff,
        "S": s_coeff,
        "Wick_carrier": carrier,
        "raw_hard_remainder": e_coeff - s_coeff - carrier,
    }


def boolean_rows(labels: tuple[int, ...], cutoff: int) -> dict[str, object]:
    require(type(labels) is tuple and 1 <= len(labels) <= 6, "Boolean label cap")
    require(
        all(type(p) is int and 1 < p and p.bit_length() <= 128 for p in labels),
        "positive source prime labels",
    )
    require(len(set(labels)) == len(labels), "distinct source labels")
    require(
        type(cutoff) is int and 1 <= cutoff and cutoff.bit_length() <= 128,
        "cutoff type/range",
    )

    def mu_u(group):
        return (-1) ** len(group) if prod(group) <= cutoff else 0

    def a_u(group):
        total = sum(
            mu_u(tuple(p for p, take in zip(group, bits, strict=True) if take))
            for bits in product((0, 1), repeat=len(group))
        )
        return int(not group) - total

    convolution, balanced = 0, 0
    histories = []
    for allocation in product(range(3), repeat=len(labels)):
        groups = [
            tuple(p for p, slot in zip(labels, allocation, strict=True) if slot == j)
            for j in range(3)
        ]
        convolution += mu_u(groups[0]) * mu_u(groups[1])
        value = a_u(groups[0]) * a_u(groups[1]) * (-1) ** len(groups[2])
        balanced += value
        if value:
            histories.append(
                {"groups": [list(x) for x in groups], "coefficient": value}
            )
    truncated = 2 * mu_u(labels)
    type_i = truncated - convolution
    full = type_i + balanced
    require(full == (-1) ** len(labels), "complete Boolean row identity")
    return {
        "twice_truncated_mu": truncated,
        "truncated_double_convolution": convolution,
        "type_I": type_i,
        "balanced": balanced,
        "full_mu": full,
        "nonzero_balanced_histories": histories,
        "complete_allocations": 3 ** len(labels),
    }


def build() -> dict[str, object]:
    raw = {key: source_bytes(key) for key in SOURCES}
    block = json.loads(
        raw[
            (SCB, "research/riemann-structures/subcritical_observed_boolean_block.json")
        ]
    )
    require(
        block["proof_object_sha256"]
        == "3385b68dd20c2c10a361eac3afda8aa1f5b3ba767649ed7d7016913650ace388",
        "frozen subcritical proof identity",
    )
    densities = [density_record(k) for k in range(1, 17)]
    raw_controls = []
    for k in range(1, 17):
        values = raw_coefficients((1, 1) + (2,) * k)
        require(
            all(value == 0 for value in values.values()),
            "raw labelled mixed sector zero",
        )
        raw_controls.append(
            {"core_depth": k, **{key: str(value) for key, value in values.items()}}
        )
    require(
        raw_coefficients((1, 1))["raw_hard_remainder"] == 1,
        "empty-core terminal retained",
    )
    panels = []
    for panel in block["panels"]:
        primes = {key: value["prime"] for key, value in panel["primes"].items()}
        require(67 not in primes.values(), "physical duplicated-label alias excluded")
        sides = {}
        for side, reduced, physical in (("left", "ell", "N"), ("right", "rho", "M")):
            labels = (primes["A"], primes["B"], primes[reduced])
            rows = boolean_rows(labels, panel["U"])
            require(
                rows["type_I"] == 1
                and rows["balanced"] == -2
                and rows["full_mu"] == -1,
                "complete frozen block rows",
            )
            require(
                len(rows["nonzero_balanced_histories"]) == 2, "two balanced histories"
            )
            n = panel[physical]
            sides[side] = {
                "core_labels": list(labels),
                "physical_integer": n,
                "rows": rows,
                "full_owner_amplitude_square": str(Fraction(1, 100 * n)),
                "core_complement_amplitude_square": str(Fraction(1, 100 * n)),
                "primitive_site_time_diagonal": str(Fraction(4, 315 * n)),
            }
        panels.append(
            {
                "j": panel["j"],
                "fixed_g": panel["g"],
                "sides": sides,
                "bilateral_ratios_to_old_balanced_block": [
                    "1/4",
                    "-1/4",
                    "-1/4",
                    "1/4",
                ],
                "complete_activation_bilateral_sum": "0",
            }
        )
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.euler_activation_adapter.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "arithmetic": "EXACT_INTEGER_RATIONAL_POLYNOMIAL",
        "density_and_diagonal_controls": densities,
        "raw_labelled_mixed_controls": raw_controls,
        "empty_core_endpoint_coefficient": "1",
        "frozen_subcritical_full_row_panels": panels,
        "new_prime_search_run": False,
        "source_binding": "OWNER_ACTIVATION_PROJECTION_OF_EXPLICIT_EULER_HOMOTOPY",
        "all_completed_retained_mask_identity_asserted": False,
        "T106140_diagonal_identification_asserted": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main() -> None:
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
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(
            canonical(candidate) == canonical(result), "exact canonical source replay"
        )
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
