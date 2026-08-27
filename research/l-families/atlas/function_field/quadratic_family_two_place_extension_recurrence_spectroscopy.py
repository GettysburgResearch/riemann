#!/usr/bin/env python3
"""Exact replay for two-place extension recurrence spectroscopy."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_COMMIT = "a91f985329f04e4c3dee9662589980ff7ab8ccf5"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "QUADRATIC_FAMILY_TWO_PLACE_CUMULANT_DEFECT.md"
    ): "bf255c1978b7de4a7f6d697b1c40878c50b7a449",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_two_place_cumulant_defect.py"
    ): "bd359c41670bbec94fbe79dea096a3cb89bf647d",
}
EXPECTED_COEFFICIENTS = {
    2: (-6, 4),
    3: (-9, 6),
    4: (-186, 360, -336, 312, -276, 146, -32),
    5: (-720, 1200, -840, 600, -555, 345, -90),
    6: (
        -15300,
        45720,
        -68040,
        82200,
        -90690,
        81870,
        -60960,
        41760,
        -26196,
        12766,
        -3914,
        544,
    ),
}
EXPECTED_ORIENTATION_6 = (0, 0, 0, 0, 1620, -3780, 2880, -720)
CLEARING_POWER = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3}


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{FROZEN_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")


def validate_sign(value: int, label: str) -> None:
    if value not in (-1, 1):
        raise ValueError(f"{label} must be +1 or -1")


def base_polynomials() -> dict[str, sp.Poly]:
    q = sp.symbols("q")
    family_size = q**4 * (q - 1)
    v_num = q**5 - 2 * q**4 + 2 * q**3 - 2 * q**2 + 2 * q - 1
    w_num = q**5 - 3 * q**4 + 5 * q**3 - 7 * q**2 + 9 * q - 6
    covariance_num = 2 * q - 3
    rows = {
        "P2": 2 * covariance_num,
        "P3": 3 * covariance_num,
        "P4": (
            family_size * (8 * covariance_num + 6 * w_num)
            - 6 * v_num**2
            - 24 * v_num * covariance_num
            - 12 * covariance_num**2
        ),
        "P5": 15 * covariance_num * (family_size - 4 * (v_num + covariance_num)),
        "P6": (
            family_size**2 * (32 * covariance_num + 30 * w_num)
            - 30
            * family_size
            * (v_num + covariance_num)
            * (2 * v_num + 8 * covariance_num + 6 * w_num)
            - 180 * family_size * covariance_num**2
            + 240 * (v_num + covariance_num) ** 3
            + 30 * family_size * v_num**2
            - 60 * v_num**3
        ),
        "Q6": -180 * family_size * covariance_num**2,
    }
    return {
        name: sp.Poly(sp.expand(expression), q) for name, expression in rows.items()
    }


def ascending_coefficients(poly: sp.Poly) -> tuple[int, ...]:
    degree = poly.degree()
    symbol = poly.gens[0]
    return tuple(int(poly.coeff_monomial(symbol**power)) for power in range(degree + 1))


def family_data(q: int) -> tuple[int, int, int, int]:
    if isinstance(q, bool) or not isinstance(q, int) or q < 3 or q % 2 == 0:
        raise ValueError("q must be an odd integer at least three")
    family_size = q**4 * (q - 1)
    v_num = q**5 - 2 * q**4 + 2 * q**3 - 2 * q**2 + 2 * q - 1
    w_num = q**5 - 3 * q**4 + 5 * q**3 - 7 * q**2 + 9 * q - 6
    covariance_num = 2 * q - 3
    return family_size, v_num, w_num, covariance_num


def cumulant_defect(
    q: int, separation_sign: int, minus_one_sign: int, order: int
) -> Fraction:
    validate_sign(separation_sign, "separation sign")
    validate_sign(minus_one_sign, "minus-one sign")
    if order not in CLEARING_POWER:
        raise ValueError("cumulant order must lie between two and six")
    family_size, v_num, w_num, covariance_num = family_data(q)
    v = Fraction(v_num, family_size)
    w = Fraction(w_num, family_size)
    c = Fraction(covariance_num, family_size)
    u = separation_sign * (1 + minus_one_sign) * c
    if order == 2:
        return 2 * c
    if order == 3:
        return 3 * u
    if order == 4:
        return 8 * c + 6 * w - 6 * v**2 - 24 * v * c - 12 * c**2
    if order == 5:
        return 15 * u * (1 - 4 * (v + c))
    return (
        32 * c
        + 30 * w
        - 30 * (v + c) * (2 * v + 8 * c + 6 * w)
        - 90 * u**2
        + 240 * (v + c) ** 3
        + 30 * v**2
        - 60 * v**3
    )


def cleared_defect(
    q: int, separation_sign: int, minus_one_sign: int, order: int
) -> int:
    family_size = family_data(q)[0]
    value = family_size ** CLEARING_POWER[order] * cumulant_defect(
        q, separation_sign, minus_one_sign, order
    )
    if value.denominator != 1:
        raise ArithmeticError("cleared cumulant defect is not integral")
    return value.numerator


def coefficient_map(poly: sp.Poly) -> dict[int, int]:
    symbol = poly.gens[0]
    return {
        power: int(poly.coeff_monomial(symbol**power))
        for power in range(poly.degree() + 1)
        if poly.coeff_monomial(symbol**power)
    }


def add_spectral_term(spectrum: dict[int, int], root: int, amplitude: int) -> None:
    spectrum[root] = spectrum.get(root, 0) + amplitude
    if not spectrum[root]:
        del spectrum[root]


def spectral_ledger(order: int, prime: int, alpha: int, epsilon: int) -> dict[int, int]:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not sp.isprime(prime)
    ):
        raise ValueError("replay base must be an odd prime")
    validate_sign(alpha, "alpha")
    validate_sign(epsilon, "epsilon")
    if order not in CLEARING_POWER:
        raise ValueError("cumulant order must lie between two and six")
    polynomials = base_polynomials()
    spectrum: dict[int, int] = {}
    base = coefficient_map(polynomials[f"P{order}"])
    if order in (3, 5):
        for power, amplitude in base.items():
            add_spectral_term(spectrum, alpha * prime**power, amplitude)
            add_spectral_term(spectrum, alpha * epsilon * prime**power, amplitude)
    else:
        for power, amplitude in base.items():
            add_spectral_term(spectrum, prime**power, amplitude)
    if order == 6:
        for power, amplitude in coefficient_map(polynomials["Q6"]).items():
            add_spectral_term(spectrum, epsilon * prime**power, amplitude)
    return dict(sorted(spectrum.items()))


def spectral_value(spectrum: dict[int, int], extension_degree: int) -> int:
    if extension_degree < 1:
        raise ValueError("extension degree must be positive")
    return sum(
        amplitude * root**extension_degree for root, amplitude in spectrum.items()
    )


def polynomial_multiply(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def recurrence_polynomial(roots: tuple[int, ...]) -> tuple[int, ...]:
    output = (1,)
    for root in roots:
        output = polynomial_multiply(output, (-root, 1))
    return output


def verify_recurrence(spectrum: dict[int, int], horizon: int = 30) -> bool:
    roots = tuple(spectrum)
    coefficients = recurrence_polynomial(roots)
    values = tuple(spectral_value(spectrum, degree) for degree in range(1, horizon + 1))
    order = len(roots)
    if horizon < 2 * order:
        raise ValueError("recurrence horizon must be at least twice the order")
    return all(
        sum(
            coefficients[offset] * values[index + offset] for offset in range(order + 1)
        )
        == 0
        for index in range(horizon - order)
    )


def tower_panel(prime: int, alpha: int, epsilon: int) -> dict[str, object]:
    rows: dict[str, object] = {}
    for order in range(2, 7):
        spectrum = spectral_ledger(order, prime, alpha, epsilon)
        for extension_degree in range(1, 9):
            q = prime**extension_degree
            direct = cleared_defect(
                q,
                alpha**extension_degree,
                epsilon**extension_degree,
                order,
            )
            if direct != spectral_value(spectrum, extension_degree):
                raise ArithmeticError("spectral ledger disagrees with direct defect")
        if not verify_recurrence(spectrum, max(30, 2 * len(spectrum) + 2)):
            raise ArithmeticError("minimal-root recurrence failed")
        rows[str(order)] = {
            "minimal_rank": len(spectrum),
            "roots": [str(root) for root in spectrum],
            "first_three_values": [
                str(spectral_value(spectrum, degree)) for degree in range(1, 4)
            ],
        }
    return {
        "alpha": alpha,
        "epsilon": epsilon,
        "orders": rows,
        "prime": prime,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    polynomials = base_polynomials()
    for order, expected in EXPECTED_COEFFICIENTS.items():
        if ascending_coefficients(polynomials[f"P{order}"]) != expected:
            raise ArithmeticError(f"P{order} coefficient vector changed")
    if ascending_coefficients(polynomials["Q6"]) != EXPECTED_ORIENTATION_6:
        raise ArithmeticError("Q6 coefficient vector changed")
    towers = [
        tower_panel(prime, alpha, epsilon)
        for prime, epsilon in ((3, -1), (5, 1))
        for alpha in (-1, 1)
    ]
    expected_ranks = {
        "epsilon_minus": {"2": 2, "3": 4, "4": 7, "5": 14, "6": 16},
        "epsilon_plus": {"2": 2, "3": 2, "4": 7, "5": 7, "6": 12},
    }
    for tower in towers:
        key = "epsilon_plus" if tower["epsilon"] == 1 else "epsilon_minus"
        actual = {order: row["minimal_rank"] for order, row in tower["orders"].items()}
        if actual != expected_ranks[key]:
            raise ArithmeticError("minimal recurrence rank table changed")
    return {
        "source_contract": {
            "commit": FROZEN_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "polynomial_coefficients_low_to_high": {
            f"P{order}": list(coefficients)
            for order, coefficients in EXPECTED_COEFFICIENTS.items()
        }
        | {"Q6": list(EXPECTED_ORIENTATION_6)},
        "minimal_ranks": expected_ranks,
        "tower_controls": towers,
        "theorem": {
            "clearing_power": "A(q)^floor(m/2)",
            "extension_character_lift": ("chi_(p^n)(x)=chi_p(x)^n for x in F_p^*"),
            "spectral_roots": "only signed Tate roots +p^j and -p^j",
            "rank_two_verdict": (
                "false from m=4 onward: the fourth residual has exact minimal rank seven"
            ),
            "sign_control_scope": (
                "stored towers use the actual epsilon=(-1|p) at p=3,5; helper tests "
                "also exercise both formal signs algebraically"
            ),
        },
        "proof_ledger": {
            "cleared_polynomial_identities": "PROVED EXACT",
            "minimal_recurrence_ranks": "PROVED BY DISTINCT-ROOT VANDERMONDE",
            "rank_two_beyond_order_three": "REFUTED",
            "sheaf_or_tate_class_realization": "NOT CLAIMED",
            "raw_unscaled_finite_recurrence": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "base_primes": [3, 5],
            "maximum_extension_degree_producer": 34,
            "maximum_extension_degree_including_tests": 36,
            "maximum_q_expansion_degree": 15,
            "maximum_recurrence_degree": 16,
            "finite_field_elements": 0,
            "curves": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = (
        json.dumps(
            run(check_sources=not args.no_source_check), indent=2, sort_keys=True
        )
        + "\n"
    )
    canonical = Path(__file__).with_suffix(".json")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8", newline="\n")
    elif args.check and canonical.read_text(encoding="utf-8") != rendered:
        raise SystemExit("canonical JSON fixture is stale")
    elif not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
