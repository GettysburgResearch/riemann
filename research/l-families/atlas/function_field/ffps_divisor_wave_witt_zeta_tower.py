#!/usr/bin/env python3
"""Exact bounded replay for the divisor-wave free-Lie/Witt zeta tower."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_DIVISOR_WAVE_WITT_ZETA_TOWER.md"
SOURCE_COMMIT = "5122e939df2fa322b5a3185cf1d78d4b402f3d5f"
SOURCE_BLOBS = {
    "research/l-families/atlas/function_field/"
    "FFPS_DIVISOR_WAVE_SHIFTED_ZETA_FACTORIZATION.md": (
        "21ef6a6e0078beb85f81fc880e5f161fc6288a8f"
    ),
    "research/l-families/atlas/function_field/"
    "ffps_divisor_wave_shifted_zeta_factorization.py": (
        "74cdcfd5e638e8bca9f70646e66ebe47e783f77b"
    ),
    "research/l-families/atlas/function_field/"
    "ffps_divisor_wave_shifted_zeta_factorization.json": (
        "f716c083a0c4f7cc578084503c1a228d1d93e3fc"
    ),
    "tests/test_ffps_divisor_wave_shifted_zeta_factorization.py": (
        "f232c040e83202519bb40e73d116f91e70b08ba4"
    ),
}
REPLAY_DEPTH = 8


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    factors: list[tuple[int, int]] = []
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def mobius(n: int) -> int:
    sign = 1
    for _, exponent in factorization(n):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def divisors(n: int) -> tuple[int, ...]:
    values = [1]
    for prime, exponent in factorization(n):
        old = tuple(values)
        power = 1
        for _ in range(exponent):
            power *= prime
            values.extend(item * power for item in old)
    return tuple(sorted(values))


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        actual = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if actual != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "free-Lie/Witt tower",
        "PBW",
        "1/(R+1)",
        "finite-local cancellation firewall",
        "HIGHFARGCDWAVE remains open",
        "RH and GRH remain unproved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing: {marker}")


def witt_multiplicity(a: int, b: int) -> int:
    """Multigraded free-Lie multiplicity for a plus and b minus letters."""
    if isinstance(a, bool) or isinstance(b, bool) or a < 0 or b < 0 or a + b < 1:
        raise ValueError("a,b must be nonnegative with positive sum")
    n = a + b
    if a == 0 or b == 0:
        return int(n == 1)
    common_divisors = divisors(math.gcd(a, b))
    numerator = sum(
        mobius(d) * math.comb(n // d, a // d) for d in common_divisors
    )
    if numerator % n:
        raise ArithmeticError("Witt numerator was not divisible by degree")
    result = numerator // n
    if result < 0:
        raise ArithmeticError("Witt multiplicity became negative")
    return result


def total_lie_dimension(n: int) -> int:
    return sum(witt_multiplicity(a, n - a) for a in range(n + 1))


Polynomial = dict[tuple[int, int], int]


def multiply_polynomials(left: Polynomial, right: Polynomial, cap: int) -> Polynomial:
    result: dict[tuple[int, int], int] = defaultdict(int)
    for (degree_left, weight_left), value_left in left.items():
        for (degree_right, weight_right), value_right in right.items():
            degree = degree_left + degree_right
            if degree <= cap:
                result[(degree, weight_left + weight_right)] += value_left * value_right
    return {key: value for key, value in result.items() if value}


def local_factor_polynomial(
    degree: int, weight: int, multiplicity: int, cap: int
) -> Polynomial:
    return {
        (choose * degree, choose * weight): (-1) ** choose
        * math.comb(multiplicity, choose)
        for choose in range(multiplicity + 1)
        if choose * degree <= cap
    }


def truncated_witt_product(cap: int) -> Polynomial:
    result: Polynomial = {(0, 0): 1}
    for n in range(1, cap + 1):
        for a in range(n + 1):
            multiplicity = witt_multiplicity(a, n - a)
            if multiplicity:
                result = multiply_polynomials(
                    result,
                    local_factor_polynomial(n, 2 * a - n, multiplicity, cap),
                    cap,
                )
    return result


def witt_factor_panel(depth: int = REPLAY_DEPTH) -> dict[str, object]:
    rows = []
    for n in range(1, depth + 1):
        weights = [
            {"weight": 2 * a - n, "multiplicity": witt_multiplicity(a, n - a)}
            for a in range(n + 1)
            if witt_multiplicity(a, n - a)
        ]
        expected_dimension = sum(
            mobius(d) * 2 ** (n // d) for d in divisors(n)
        ) // n
        actual_dimension = total_lie_dimension(n)
        if actual_dimension != expected_dimension:
            raise ArithmeticError("ordinary and multigraded Witt formulas disagree")
        rows.append(
            {"degree": n, "dimension": actual_dimension, "weights": weights}
        )

    product = truncated_witt_product(depth)
    target: Polynomial = {(0, 0): 1, (1, 1): -1, (1, -1): -1}
    for degree in range(depth + 1):
        actual_layer = {
            weight: value
            for (item_degree, weight), value in product.items()
            if item_degree == degree
        }
        target_layer = {
            weight: value
            for (item_degree, weight), value in target.items()
            if item_degree == degree
        }
        if actual_layer != target_layer:
            raise ArithmeticError(f"Witt product mismatch in degree {degree}")
    return {
        "depth": depth,
        "rows": rows,
        "local_identity_verified_through_degree": depth,
        "target": "1-(z+z^-1)x",
    }


def first_extractions_panel() -> dict[str, object]:
    expected = {
        1: {1: 1, -1: 1},
        2: {0: 1},
        3: {1: 1, -1: 1},
        4: {2: 1, 0: 1, -2: 1},
    }
    actual = {
        n: {
            2 * a - n: witt_multiplicity(a, n - a)
            for a in range(n + 1)
            if witt_multiplicity(a, n - a)
        }
        for n in expected
    }
    if actual != expected:
        raise ArithmeticError("first four Witt packets changed")
    return {
        "packets": {str(n): weights for n, weights in actual.items()},
        "degree_two_factor": "1/zeta^(67)(2s)",
        "remainder_after_depth_R": "O_R(p^(-(R+1)Re(s)))",
        "normal_convergence": "Re(s)>1/(R+1)+delta",
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta / primitive-pair route",
        "witt_tower": witt_factor_panel(),
        "first_extractions": first_extractions_panel(),
        "exact_factorization": (
            "F_xi(s)=prod_(n>=1) prod_(a+b=n) "
            "zeta^(67)(n*s-i*(a-b)*xi)^(-ell_(a,b))"
        ),
        "finite_depth_factorization": (
            "extract n<=R; correction normal for Re(s)>1/(R+1)+delta"
        ),
        "scope_firewall": {
            "finite_local_factors_nonzero_at_every_hypothetical_zero": False,
            "hyperbola_cutoff_removed": False,
            "highgcdwave_proved": False,
            "rh_or_grh_proved": False,
        },
        "source_commit": SOURCE_COMMIT,
        "source_blobs": SOURCE_BLOBS,
        "resource_caps": {"witt_depth": REPLAY_DEPTH, "zeta_zeros": 0},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-lock", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(
        run(check_sources=not args.no_source_lock), indent=2, sort_keys=True
    ) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
