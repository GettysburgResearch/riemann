#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Iterable

VERDICT = "PASS_T105100_CRITICAL_RESIDUE_SECOND_MOMENT_LEDGER"
REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_FILES = (
    "PACKET_METADATA_105100.json",
    "claims/lemmas/L-105100-critical-residue-second-moment-balance.md",
    "claims/methodology/M-105100-hostile-review-contract.md",
    "claims/refutations/R-105100-root-ledger-alone-does-not-bound-m2.md",
    "claims/theorems/T-105100-critical-residue-second-moment-frontier.md",
    "experiments/X-105100-critical-residue-second-moment/verify.py",
    "experiments/X-105100-critical-residue-second-moment/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def derivative(coefficients: list[F]) -> list[F]:
    return [F(k) * coefficients[k] for k in range(1, len(coefficients))]


def evaluate(coefficients: list[F], x: F) -> F:
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def multiply(left: list[F], right: list[F]) -> list[F]:
    product = [F(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            product[i + j] += left_value * right_value
    return product


def series_quotient(
    numerator: list[F], denominator: list[F], order: int
) -> list[F]:
    if not denominator or denominator[0] == 0:
        raise ValueError("series denominator must have nonzero constant term")
    quotient: list[F] = []
    for k in range(order + 1):
        value = numerator[k] if k < len(numerator) else F(0)
        for j in range(1, min(k, len(denominator) - 1) + 1):
            value -= denominator[j] * quotient[k - j]
        quotient.append(value / denominator[0])
    return quotient


def laurent_minus_one_coefficient(coefficients: list[F]) -> F:
    """Coefficient of z^-1 in p(z)^2/(p'(z)*p''(z)), without factoring."""
    first = derivative(coefficients)
    second = derivative(first)
    numerator = multiply(coefficients, coefficients)
    denominator = multiply(first, second)
    if len(numerator) - len(denominator) != 3:
        raise ValueError("unexpected rational-function degree")
    reversed_numerator = list(reversed(numerator))
    reversed_denominator = list(reversed(denominator))
    # Q(1/t)=t^-3*N_rev(t)/D_rev(t); z^-1 is t^1, hence order four.
    return series_quotient(reversed_numerator, reversed_denominator, 4)[4]


def translate_polynomial(coefficients: list[F], shift: F) -> list[F]:
    """Return q(x)=p(x-shift), with coefficients in ascending order."""
    degree = len(coefficients) - 1
    translated = [F(0) for _ in range(degree + 1)]
    for power, coefficient in enumerate(coefficients):
        for target_power in range(power + 1):
            translated[target_power] += (
                coefficient
                * F(math.comb(power, target_power))
                * (-shift) ** (power - target_power)
            )
    return translated


def elementary_symmetric_sums(coefficients: list[F]) -> list[F]:
    degree = len(coefficients) - 1
    if coefficients[-1] != 1:
        raise ValueError("the verifier expects a monic polynomial")
    # p(x)=x^n-e1*x^(n-1)+e2*x^(n-2)-...
    elementary = [F(1)]
    for index in range(1, degree + 1):
        elementary.append((-1) ** index * coefficients[degree - index])
    return elementary


def root_power_sums(coefficients: list[F], maximum_power: int = 4) -> list[F]:
    degree = len(coefficients) - 1
    elementary = elementary_symmetric_sums(coefficients)
    powers = [F(degree)]
    for m in range(1, maximum_power + 1):
        total = F(0)
        for j in range(1, min(m, degree) + 1):
            if j == m:
                continue
            total += (-1) ** (j - 1) * elementary[j] * powers[m - j]
        if m <= degree:
            total += (-1) ** (m + 1) * F(m) * elementary[m]
        powers.append(total)
    return powers


def centered_root_moments(coefficients: list[F]) -> tuple[F, F]:
    degree = len(coefficients) - 1
    powers = root_power_sums(coefficients, 4)
    mean = powers[1] / degree
    v2 = powers[2] - 2 * mean * powers[1] + degree * mean**2
    v4 = (
        powers[4]
        - 4 * mean * powers[3]
        + 6 * mean**2 * powers[2]
        - 4 * mean**3 * powers[1]
        + degree * mean**4
    )
    return v2, v4


def root_moment_ledger(coefficients: list[F]) -> F:
    degree = len(coefficients) - 1
    if degree < 2:
        raise ValueError("degree must be at least two")
    v2, v4 = centered_root_moments(coefficients)
    numerator = (
        F(6 * degree * degree - 18 * degree + 13) * v2**2
        - F(3 * degree * (degree - 1) * (degree - 2)) * v4
    )
    denominator = F(degree**4 * (degree - 1) ** 3)
    return numerator / denominator


def residue_sums(
    coefficients: list[F],
    critical_roots: Iterable[F],
    second_critical_roots: Iterable[F],
) -> tuple[list[F], list[F]]:
    first = derivative(coefficients)
    second = derivative(first)
    third = derivative(second)
    critical_roots = list(critical_roots)
    second_critical_roots = list(second_critical_roots)

    degree = len(coefficients) - 1
    if len(critical_roots) != degree - 1:
        raise ValueError("critical-root fixture does not have complete coverage")
    if len(second_critical_roots) != max(degree - 2, 0):
        raise ValueError("second-critical-root fixture does not have complete coverage")
    if len(set(critical_roots)) != len(critical_roots):
        raise ValueError("critical-root fixture is not simple")
    if len(set(second_critical_roots)) != len(second_critical_roots):
        raise ValueError("second-critical-root fixture is not simple")

    rho: list[F] = []
    for c in critical_roots:
        require(evaluate(first, c) == 0, f"{c} is not a critical root")
        require(evaluate(second, c) != 0, f"{c} is not a simple critical root")
        require(evaluate(coefficients, c) != 0, f"{c} is also a root of p")
        rho.append(evaluate(coefficients, c) / evaluate(second, c))

    tau: list[F] = []
    for d in second_critical_roots:
        require(evaluate(second, d) == 0, f"{d} is not a second critical root")
        require(evaluate(first, d) != 0, f"{d} is also a critical root")
        require(
            evaluate(third, d) != 0, f"{d} is not a simple second critical root"
        )
        tau.append(
            evaluate(coefficients, d) ** 2
            / (evaluate(first, d) * evaluate(third, d))
        )
    return rho, tau


def fixture_payload(
    name: str,
    coefficients: list[F],
    critical_roots: list[F],
    second_critical_roots: list[F],
) -> dict[str, object]:
    rho, tau = residue_sums(coefficients, critical_roots, second_critical_roots)
    critical_square_sum = sum((value * value for value in rho), F(0))
    second_level_debt = sum(tau, F(0))
    ledger = root_moment_ledger(coefficients)
    require(
        critical_square_sum + second_level_debt == ledger,
        f"residue balance failed for {name}",
    )
    v2, v4 = centered_root_moments(coefficients)
    return {
        "name": name,
        "degree": len(coefficients) - 1,
        "centered_v2": str(v2),
        "centered_v4": str(v4),
        "critical_residues": [str(value) for value in rho],
        "second_level_cross_residues": [str(value) for value in tau],
        "critical_square_sum": str(critical_square_sum),
        "second_level_debt": str(second_level_debt),
        "root_moment_ledger": str(ledger),
        "balance_verified": True,
    }


def quartic_firewall_exact() -> dict[str, object]:
    coefficients = [F(2), F(0), F(-2), F(0), F(1)]
    second = derivative(derivative(coefficients))
    rho = [
        evaluate(coefficients, c) / evaluate(second, c)
        for c in (F(-1), F(0), F(1))
    ]
    critical_square_sum = sum((value * value for value in rho), F(0))

    u = F(1, 3)
    p_at_d = u**2 - 2 * u + 2
    p_prime_times_p_third = F(96) * u * (u - 1)
    tau_each = p_at_d**2 / p_prime_times_p_third
    second_level_debt = 2 * tau_each
    ledger = root_moment_ledger(coefficients)

    require(rho == [F(1, 8), F(-1, 2), F(1, 8)], "quartic rho mutation")
    require(critical_square_sum == F(9, 32), "quartic M2 mutation")
    require(tau_each == F(-169, 1728), "quartic tau mutation")
    require(second_level_debt == F(-169, 864), "quartic debt mutation")
    require(ledger == F(37, 432), "quartic root-ledger mutation")
    require(
        critical_square_sum + second_level_debt == ledger,
        "quartic residue balance failed",
    )
    require(critical_square_sum > ledger, "quartic firewall lost strictness")

    return {
        "polynomial": "x^4-2*x^2+2",
        "critical_square_sum": str(critical_square_sum),
        "second_level_debt": str(second_level_debt),
        "root_moment_ledger": str(ledger),
        "root_ledger_is_not_an_upper_bound": True,
        "dropping_second_level_debt_fails": critical_square_sum != ledger,
    }


def nonreal_critical_correction_exact() -> dict[str, object]:
    # For p=x^3+x+1, p' vanishes at c=+-i/sqrt(3), where
    # rho_c=1/9 -/+ i*sqrt(3)/6. This fixture genuinely distinguishes the
    # algebraic square sum from the sum of absolute squares.
    coefficients = [F(1), F(1), F(0), F(1)]
    residue_real_part = F(1, 9)
    residue_imaginary_part_squared = F(1, 12)
    off_real_algebraic_square_sum = 2 * (
        residue_real_part**2 - residue_imaginary_part_squared
    )
    off_real_absolute_square_sum = 2 * (
        residue_real_part**2 + residue_imaginary_part_squared
    )

    # p'' has the sole zero d=0.
    second_level_debt = F(1, 6)
    ledger = root_moment_ledger(coefficients)
    real_m2 = F(0)

    require(
        off_real_algebraic_square_sum == F(-23, 162),
        "nonreal fixture algebraic correction mutation",
    )
    require(
        off_real_absolute_square_sum == F(31, 162),
        "nonreal fixture absolute-square control mutation",
    )
    require(
        off_real_algebraic_square_sum != off_real_absolute_square_sum,
        "nonreal fixture does not distinguish algebraic and absolute squares",
    )
    require(second_level_debt == F(1, 6), "nonreal fixture debt mutation")
    require(ledger == F(2, 81), "nonreal fixture ledger mutation")
    require(
        real_m2 == ledger - off_real_algebraic_square_sum - second_level_debt,
        "nonreal correction decomposition failed",
    )

    return {
        "polynomial": "x^3+x+1",
        "real_critical_residue_m2": str(real_m2),
        "off_real_algebraic_square_sum": str(off_real_algebraic_square_sum),
        "off_real_absolute_square_sum": str(off_real_absolute_square_sum),
        "second_level_debt": str(second_level_debt),
        "root_moment_ledger": str(ledger),
        "real_nonreal_decomposition_verified": True,
        "algebraic_squares_not_absolute_squares": True,
    }


def formal_laurent_checks() -> dict[str, object]:
    polynomials = [
        [F(-2), F(3), F(1)],
        [F(1), F(-3), F(0), F(1)],
        [F(1), F(64), F(-32), F(-4, 3), F(1)],
        [F(2), F(3), F(-1), F(5), F(-2), F(1)],
        [F(-3), F(0), F(2), F(-4), F(1), F(3), F(1)],
        [F(5), F(-2), F(7), F(0), F(-3), F(1), F(2), F(1)],
        [F(1), F(4), F(-2), F(6), F(0), F(-5), F(3), F(-1), F(1)],
    ]
    rows = []
    for coefficients in polynomials:
        coefficient_at_infinity = laurent_minus_one_coefficient(coefficients)
        ledger = root_moment_ledger(coefficients)
        require(
            coefficient_at_infinity == ledger,
            f"factor-free Laurent check failed in degree {len(coefficients) - 1}",
        )
        rows.append(
            {
                "degree": len(coefficients) - 1,
                "coefficient_at_infinity": str(coefficient_at_infinity),
                "root_moment_ledger": str(ledger),
            }
        )

    degree = 4
    # Use the asymmetric quartic because its centered V4 is nonzero.
    asymmetric = [F(1), F(64), F(-32), F(-4, 3), F(1)]
    v2, v4 = centered_root_moments(asymmetric)
    wrong_v4_sign = (
        F(6 * degree * degree - 18 * degree + 13) * v2**2
        + F(3 * degree * (degree - 1) * (degree - 2)) * v4
    ) / F(degree**4 * (degree - 1) ** 3)
    require(
        wrong_v4_sign != laurent_minus_one_coefficient(asymmetric),
        "V4 sign mutation was not detected",
    )

    return {
        "degree_range": [2, 8],
        "exact_rows": rows,
        "v4_sign_mutation_rejected": True,
    }


def build_payload() -> dict[str, object]:
    cubic = [F(1), F(-3), F(0), F(1)]
    asymmetric_quartic = [F(1), F(64), F(-32), F(-4, 3), F(1)]

    fixtures = [
        fixture_payload(
            "cubic_rational_critical_ladder",
            cubic,
            [F(-1), F(1)],
            [F(0)],
        ),
        fixture_payload(
            "asymmetric_quartic_rational_critical_ladder",
            asymmetric_quartic,
            [F(-4), F(1), F(4)],
            [F(-2), F(8, 3)],
        ),
    ]

    shift = F(7)
    translated = translate_polynomial(cubic, shift)
    translated_fixture = fixture_payload(
        "translated_cubic",
        translated,
        [F(-1) + shift, F(1) + shift],
        [shift],
    )
    require(
        root_moment_ledger(translated) == root_moment_ledger(cubic),
        "root ledger is not translation invariant",
    )
    require(
        translated_fixture["critical_square_sum"]
        == fixtures[0]["critical_square_sum"],
        "critical square sum is not translation invariant",
    )
    require(
        translated_fixture["second_level_debt"]
        == fixtures[0]["second_level_debt"],
        "second-level debt is not translation invariant",
    )

    payload: dict[str, object] = {
        "schema": "riemann.t105100.critical-residue-second-moment.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL",
        "source": {
            "integrated_main": "852d8aa05c701ea7818ce8a50543e68987fef5cc",
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "checks": {
            "formal_laurent_expansions": formal_laurent_checks(),
            "rational_fixtures": fixtures,
            "translation_fixture": translated_fixture,
            "translation_invariance": True,
            "quartic_firewall": quartic_firewall_exact(),
            "nonreal_critical_correction": nonreal_critical_correction_exact(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "finite_polynomial_identity_proof_supplied": True,
            "exact_rational_fixtures_replayed": True,
            "height_localization_proved": False,
            "canonical_product_limit_proved": False,
            "off_real_correction_controlled": False,
            "second_level_debt_controlled": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
