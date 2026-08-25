#!/usr/bin/env python3
"""Exact square-tower bifurcation for the native endpoint-three wavelet.

The replay uses sparse polynomials over Q[a,b,s].  It performs no finite-field
or family enumeration and imports no symbolic-algebra package.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, Fraction]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "native_qadic_wavelet_square_tower_bifurcation.json"
NOTE_PATH = HERE / "NATIVE_QADIC_WAVELET_SQUARE_TOWER_BIFURCATION.md"
TEST_PATH = ROOT / "tests" / "test_native_qadic_wavelet_square_tower_bifurcation.py"

NATIVE_NOTE_PATH = HERE / "NATIVE_QADIC_RECIPROCAL_WAVELET_SPECTROSCOPY.md"
NATIVE_PRODUCER_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.py"
NATIVE_FIXTURE_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
NATIVE_TEST_PATH = (
    ROOT / "tests" / "test_native_qadic_reciprocal_wavelet_spectroscopy.py"
)
ZERO_NOTE_PATH = HERE / "NATIVE_QADIC_WAVELET_ZERO_STRATUM.md"
ZERO_PRODUCER_PATH = HERE / "native_qadic_wavelet_zero_stratum.py"
ZERO_FIXTURE_PATH = HERE / "native_qadic_wavelet_zero_stratum.json"
ZERO_TEST_PATH = ROOT / "tests" / "test_native_qadic_wavelet_zero_stratum.py"

EXPECTED_UPSTREAM_PAYLOADS = {
    "native_wavelet": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
    "nonsquare_zero_stratum": "b90d69e9143c5d1e4afeb4741a2680f803de366184a6fc37dd0e71cd76a2052b",
}
MAX_POLYNOMIAL_OPERATIONS = 512


@dataclass
class Meter:
    operations: int = 0

    def charge(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise TypeError("operation charge must be a nonnegative integer")
        self.operations += amount
        if self.operations > MAX_POLYNOMIAL_OPERATIONS:
            raise RuntimeError("sparse-polynomial operation cap exceeded")


def _clean(poly: Mapping[Monomial, Fraction | int]) -> Polynomial:
    return {
        monomial: Fraction(coefficient)
        for monomial, coefficient in poly.items()
        if coefficient
    }


def _add(
    left: Mapping[Monomial, Fraction],
    right: Mapping[Monomial, Fraction],
    meter: Meter,
    scale: Fraction | int = 1,
) -> Polynomial:
    result = dict(left)
    factor = Fraction(scale)
    for monomial, coefficient in right.items():
        meter.charge()
        result[monomial] = result.get(monomial, Fraction(0)) + factor * coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def _mul(
    left: Mapping[Monomial, Fraction],
    right: Mapping[Monomial, Fraction],
    meter: Meter,
) -> Polynomial:
    result: Polynomial = {}
    for (ai, bi, si), left_coefficient in left.items():
        for (aj, bj, sj), right_coefficient in right.items():
            meter.charge()
            monomial = ai + aj, bi + bj, si + sj
            result[monomial] = (
                result.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            )
    return _clean(result)


def _pow(value: Mapping[Monomial, Fraction], exponent: int, meter: Meter) -> Polynomial:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    result: Polynomial = {(0, 0, 0): Fraction(1)}
    base = dict(value)
    power = exponent
    while power:
        if power & 1:
            result = _mul(result, base, meter)
        power //= 2
        if power:
            base = _mul(base, base, meter)
    return result


def _substitute(
    value: Mapping[Monomial, Fraction],
    variable: int,
    replacement: Mapping[Monomial, Fraction],
    meter: Meter,
) -> Polynomial:
    if variable not in (0, 1, 2):
        raise ValueError("variable index must be 0, 1, or 2")
    result: Polynomial = {}
    for monomial, coefficient in value.items():
        exponent = monomial[variable]
        residual = list(monomial)
        residual[variable] = 0
        term = _pow(replacement, exponent, meter)
        shifted = {
            (
                key[0] + residual[0],
                key[1] + residual[1],
                key[2] + residual[2],
            ): coefficient * term_coefficient
            for key, term_coefficient in term.items()
        }
        result = _add(result, shifted, meter)
    return result


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _verify_upstream_fixture(path: Path, expected_payload: str) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = dict(data)
    claimed = payload.pop("payload_sha256", None)
    actual = _canonical_sha256(payload)
    if claimed != actual or claimed != expected_payload:
        raise ValueError(f"upstream payload lock failed for {path.name}")
    return data


def _source_manifest(paths: Iterable[Path]) -> list[dict[str, str]]:
    result = []
    for path in paths:
        if not path.is_file():
            raise FileNotFoundError(path)
        result.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256_lf_normalized": _lf_sha256(path),
            }
        )
    return result


def _shift_s_by_three(
    coefficients: tuple[Fraction | int, ...], meter: Meter
) -> tuple[Fraction, ...]:
    """Return the ascending coefficients after the exact shift s=t+3."""

    shifted = [Fraction(0)] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for target in range(degree + 1):
            meter.charge()
            # Small local binomial evaluator avoids an extra dependency.
            numerator = 1
            denominator = 1
            for index in range(target):
                numerator *= degree - index
                denominator *= index + 1
            shifted[target] += Fraction(coefficient * numerator, denominator) * 3 ** (
                degree - target
            )
    return tuple(shifted)


def _positive_for_s_at_least_three(
    coefficients: tuple[Fraction | int, ...], meter: Meter
) -> bool:
    """Certify strict positivity on s>=3 by shifting s=t+3."""

    shifted = _shift_s_by_three(coefficients, meter)
    return bool(shifted) and shifted[0] > 0 and all(value >= 0 for value in shifted)


def _nonnegative_for_s_at_least_three(
    coefficients: tuple[Fraction | int, ...], meter: Meter
) -> bool:
    """Certify nonnegativity on s>=3 by shifting s=t+3."""

    shifted = _shift_s_by_three(coefficients, meter)
    return bool(shifted) and all(value >= 0 for value in shifted)


def _s_polynomial(coefficients: tuple[int, ...]) -> Polynomial:
    """Build an exact polynomial in s from ascending integer coefficients."""

    return _clean(
        {
            (0, 0, degree): Fraction(coefficient)
            for degree, coefficient in enumerate(coefficients)
        }
    )


def _integer_s_coefficients(value: Mapping[Monomial, Fraction]) -> tuple[int, ...]:
    """Extract ascending integral s-coefficients, rejecting hidden a or b terms."""

    if not value:
        return (0,)
    if any(ai or bi for ai, bi, _ in value):
        raise ArithmeticError("compact certificate did not eliminate a and b")
    degree = max(si for _, _, si in value)
    result = []
    for exponent in range(degree + 1):
        coefficient = value.get((0, 0, exponent), Fraction(0))
        if coefficient.denominator != 1:
            raise ArithmeticError("compact certificate is not integral")
        result.append(coefficient.numerator)
    return tuple(result)


def build_fixture() -> dict[str, object]:
    native = _verify_upstream_fixture(
        NATIVE_FIXTURE_PATH, EXPECTED_UPSTREAM_PAYLOADS["native_wavelet"]
    )
    zero = _verify_upstream_fixture(
        ZERO_FIXTURE_PATH, EXPECTED_UPSTREAM_PAYLOADS["nonsquare_zero_stratum"]
    )
    if native.get("definition", {}).get("coefficient_form") != (
        "W_D(N)=r_D(N)-(1+sqrt(q))*r_D(N-1)+sqrt(q)*r_D(N-2)"
    ):
        raise ValueError("native wavelet definition drifted")
    if zero.get("endpoint_three_theorem", {}).get("statement") != (
        "W_D(3)=0 iff K_D=0 iff (a_D,b_D)=(0,0)"
    ):
        raise ValueError("nonsquare zero theorem drifted")

    meter = Meter()
    one: Polynomial = {(0, 0, 0): Fraction(1)}
    a: Polynomial = {(1, 0, 0): Fraction(1)}
    b: Polynomial = {(0, 1, 0): Fraction(1)}
    s: Polynomial = {(0, 0, 1): Fraction(1)}
    s2 = _mul(s, s, meter)
    s4 = _mul(s2, s2, meter)

    reciprocal: list[Polynomial] = [one]
    p_coefficients = {1: a, 2: b, 3: _mul(s2, a, meter), 4: s4}
    for degree in range(1, 4):
        value: Polynomial = {}
        for shift in range(1, min(4, degree) + 1):
            value = _add(
                value,
                _mul(p_coefficients[shift], reciprocal[degree - shift], meter),
                meter,
                -1,
            )
        reciprocal.append(value)

    expected_r1 = {(1, 0, 0): Fraction(-1)}
    expected_r2 = {(2, 0, 0): Fraction(1), (0, 1, 0): Fraction(-1)}
    expected_r3 = {
        (3, 0, 0): Fraction(-1),
        (1, 1, 0): Fraction(2),
        (1, 0, 2): Fraction(-1),
    }
    if reciprocal[1:] != [expected_r1, expected_r2, expected_r3]:
        raise ArithmeticError("reciprocal coefficient derivation failed")

    rational = _add(reciprocal[3], reciprocal[2], meter, -1)
    radical = _add(reciprocal[1], reciprocal[2], meter, -1)
    wavelet = _add(rational, _mul(s, radical, meter), meter)
    expected_wavelet = {
        (3, 0, 0): Fraction(-1),
        (2, 0, 1): Fraction(-1),
        (2, 0, 0): Fraction(-1),
        (1, 1, 0): Fraction(2),
        (1, 0, 2): Fraction(-1),
        (1, 0, 1): Fraction(-1),
        (0, 1, 1): Fraction(1),
        (0, 1, 0): Fraction(1),
    }
    if wavelet != expected_wavelet:
        raise ArithmeticError("square-field wavelet expansion failed")

    two_a_plus_s_plus_one = _add(_add({(0, 0, 0): Fraction(1)}, s, meter), a, meter, 2)
    inside = _add(_mul(a, a, meter), _mul(_add(s, one, meter), a, meter), meter)
    inside = _add(inside, _mul(s, _add(s, one, meter), meter), meter)
    graph_equation = _add(
        _mul(two_a_plus_s_plus_one, b, meter), _mul(a, inside, meter), meter, -1
    )
    if graph_equation != wavelet:
        raise ArithmeticError("rational zero-curve identity failed")

    exceptional_a = _add(s, one, meter)
    exceptional_a = {
        monomial: Fraction(-1, 2) * coefficient
        for monomial, coefficient in exceptional_a.items()
    }
    exceptional = _substitute(wavelet, 0, exceptional_a, meter)
    expected_exceptional = {
        (0, 0, 3): Fraction(3, 8),
        (0, 0, 2): Fraction(5, 8),
        (0, 0, 1): Fraction(1, 8),
        (0, 0, 0): Fraction(-1, 8),
    }
    if exceptional != expected_exceptional:
        raise ArithmeticError("vertical exceptional-value certificate failed")

    plus_line = _mul(s, a, meter)
    minus_line = {monomial: -coefficient for monomial, coefficient in plus_line.items()}
    wavelet_plus = _substitute(wavelet, 1, plus_line, meter)
    wavelet_minus = _substitute(wavelet, 1, minus_line, meter)
    expected_plus = _mul(
        _mul(a, a, meter), _add(_add(s, {(0, 0, 0): -1}, meter), a, meter, -1), meter
    )
    expected_minus = _mul(
        {monomial: -coefficient for monomial, coefficient in a.items()},
        _mul(
            _add(a, s, meter, 2),
            _add(_add(a, s, meter), one, meter),
            meter,
        ),
        meter,
    )
    if wavelet_plus != expected_plus or wavelet_minus != expected_minus:
        raise ArithmeticError("K-line intersection factorization failed")

    compact_specs = [
        {
            "a_coefficients": (0,),
            "b_coefficients": (0,),
            "expected_numerators": {
                "discriminant": (0, 0, 8),
                "quadratic_at_minus_2": (0, 0, 2),
                "quadratic_at_plus_2": (0, 0, 2),
                "four_plus_x_plus_y": (0, 4),
                "four_minus_x_plus_y": (0, 4),
            },
            "row": {
                "label": "origin",
                "a": "0",
                "b": "0",
                "x_plus_y": "0",
                "x_times_y": "-2",
                "discriminant": "8",
                "quadratic_at_minus_2": "2",
                "quadratic_at_plus_2": "2",
                "four_plus_x_plus_y": "4",
                "four_minus_x_plus_y": "4",
            },
        },
        {
            "a_coefficients": (-1, 1),
            "b_coefficients": (0, -1, 1),
            "expected_numerators": {
                "discriminant": (1, 2, 5),
                "quadratic_at_minus_2": (0, 1, 1),
                "quadratic_at_plus_2": (0, -3, 5),
                "four_plus_x_plus_y": (1, 3),
                "four_minus_x_plus_y": (-1, 5),
            },
            "row": {
                "label": "positive_line_nonzero",
                "a": "s-1",
                "b": "s*(s-1)",
                "x_plus_y": "-1+1/s",
                "x_times_y": "-1-1/s",
                "discriminant": "(5*s^2+2*s+1)/s^2",
                "quadratic_at_minus_2": "(s+1)/s",
                "quadratic_at_plus_2": "(5*s-3)/s",
                "four_plus_x_plus_y": "(3*s+1)/s",
                "four_minus_x_plus_y": "(5*s-1)/s",
            },
        },
        {
            "a_coefficients": (0, -2),
            "b_coefficients": (0, 0, 2),
            "expected_numerators": {
                "discriminant": (0, 0, 4),
                "quadratic_at_minus_2": (0, 0, 8),
                "quadratic_at_plus_2": (0,),
                "four_plus_x_plus_y": (0, 6),
                "four_minus_x_plus_y": (0, 2),
            },
            "row": {
                "label": "double_endpoint",
                "a": "-2*s",
                "b": "2*s^2",
                "x_plus_y": "2",
                "x_times_y": "0",
                "discriminant": "4",
                "quadratic_at_minus_2": "8",
                "quadratic_at_plus_2": "0",
                "four_plus_x_plus_y": "6",
                "four_minus_x_plus_y": "2",
            },
        },
        {
            "a_coefficients": (-1, -1),
            "b_coefficients": (0, 1, 1),
            "expected_numerators": {
                "discriminant": (1, -2, 5),
                "quadratic_at_minus_2": (0, 3, 5),
                "quadratic_at_plus_2": (0, -1, 1),
                "four_plus_x_plus_y": (1, 5),
                "four_minus_x_plus_y": (-1, 3),
            },
            "row": {
                "label": "negative_line_nonzero",
                "a": "-s-1",
                "b": "s*(s+1)",
                "x_plus_y": "1+1/s",
                "x_times_y": "-1+1/s",
                "discriminant": "(5*s^2-2*s+1)/s^2",
                "quadratic_at_minus_2": "(5*s+3)/s",
                "quadratic_at_plus_2": "(s-1)/s",
                "four_plus_x_plus_y": "(5*s+1)/s",
                "four_minus_x_plus_y": "(3*s-1)/s",
            },
        },
    ]
    compact_rows = []
    for spec in compact_specs:
        a_value = _s_polynomial(spec["a_coefficients"])
        b_value = _s_polynomial(spec["b_coefficients"])
        a_times_s = _mul(a_value, s, meter)
        derived = {
            # These three quantities have positive denominator s^2.
            "discriminant": _add(
                _add(_mul(a_value, a_value, meter), b_value, meter, -4),
                s2,
                meter,
                8,
            ),
            "quadratic_at_minus_2": _add(
                _add(s2, a_times_s, meter, -2),
                _add(b_value, s2, meter),
                meter,
            ),
            "quadratic_at_plus_2": _add(
                _add(s2, a_times_s, meter, 2),
                _add(b_value, s2, meter),
                meter,
            ),
            # These two quantities have positive denominator s.
            "four_plus_x_plus_y": _add(
                {monomial: 4 * coefficient for monomial, coefficient in s.items()},
                a_value,
                meter,
                -1,
            ),
            "four_minus_x_plus_y": _add(
                {monomial: 4 * coefficient for monomial, coefficient in s.items()},
                a_value,
                meter,
            ),
        }
        coefficients = {
            label: _integer_s_coefficients(value) for label, value in derived.items()
        }
        if coefficients != spec["expected_numerators"]:
            raise ArithmeticError(
                f"compact row identity failed for {spec['row']['label']}"
            )
        if not _positive_for_s_at_least_three(coefficients["discriminant"], meter):
            raise ArithmeticError("compact discriminant certificate failed")
        for label in ("quadratic_at_minus_2", "quadratic_at_plus_2"):
            if not _nonnegative_for_s_at_least_three(coefficients[label], meter):
                raise ArithmeticError(
                    f"compact endpoint certificate failed for {label}"
                )
        for label in ("four_plus_x_plus_y", "four_minus_x_plus_y"):
            if not _positive_for_s_at_least_three(coefficients[label], meter):
                raise ArithmeticError(
                    f"compact root-sum certificate failed for {label}"
                )
        row = dict(spec["row"])
        row["nonnegative_numerators_ascending"] = {
            label: list(values) for label, values in coefficients.items()
        }
        compact_rows.append(row)

    source_paths = (
        NATIVE_NOTE_PATH,
        NATIVE_PRODUCER_PATH,
        NATIVE_FIXTURE_PATH,
        NATIVE_TEST_PATH,
        ZERO_NOTE_PATH,
        ZERO_PRODUCER_PATH,
        ZERO_FIXTURE_PATH,
        ZERO_TEST_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    payload: dict[str, object] = {
        "schema": "riemann.function_field.native_qadic_wavelet_square_tower_bifurcation.v1",
        "status": "PROVED_EXACT_POLYNOMIAL_ALGEBRA",
        "scope": {
            "q": "q=s^2 with s an odd integer at least 3",
            "computation": "sparse exact Q[a,b,s] algebra only",
            "field_or_curve_enumeration": 0,
        },
        "definition": {
            "reciprocal_polynomial": "P(u)=1+a*u+b*u^2+s^2*a*u^3+s^4*u^4",
            "wavelet": "W_3=r_3-(1+s)*r_2+s*r_1",
            "toy_minor": "K=s^2*a^2-b^2",
        },
        "square_field_theorem": {
            "expanded_W_3": "-a^3-a^2*s-a^2+2*a*b-a*s^2-a*s+b*s+b",
            "zero_curve": "(2*a+s+1)*b=a*(a^2+(s+1)*a+s*(s+1))",
            "graph": "b=a*(a^2+(s+1)*a+s*(s+1))/(2*a+s+1)",
            "excluded_vertical_a": "-(s+1)/2",
            "vertical_value": "(s+1)^2*(3*s-1)/8",
        },
        "toy_minor_intersection": {
            "K_factorization": "(s*a-b)*(s*a+b)",
            "on_b_equals_s_a": "W_3=a^2*(s-1-a)",
            "on_b_equals_minus_s_a": "W_3=-a*(a+2*s)*(a+s+1)",
            "points": [
                ["0", "0"],
                ["s-1", "s*(s-1)"],
                ["-2*s", "2*s^2"],
                ["-s-1", "s*(s+1)"],
            ],
        },
        "compact_admissibility": {
            "status": "PROVED_FOR_THE_FOUR_INTERSECTION_POINTS",
            "criterion": "z^4+A*z^3+B*z^2+A*z+1=(z^2-x*z+1)*(z^2-y*z+1), x,y in [-2,2]",
            "sufficiency_certificate": (
                "for the roots x,y of Q(t)=t^2-(x+y)*t+x*y, "
                "disc(Q)>=0, Q(-2)>=0, Q(2)>=0, and abs(x+y)<=4 "
                "are necessary and sufficient for x,y to be real and in [-2,2]"
            ),
            "rows": compact_rows,
            "boundary": "q-Weil/compact admissibility is not Jacobian realization",
        },
        "tower_bifurcation": {
            "odd_extension_degree": "sqrt(q) irrational; W_3=0 iff (a,b)=(0,0)",
            "even_extension_degree": "sqrt(q)=s integral; W_3=0 is the rational zero curve",
            "interpretation": "exact extension-parity normalization bifurcation",
        },
        "upstream_payload_locks": EXPECTED_UPSTREAM_PAYLOADS,
        "source_manifest": _source_manifest(source_paths),
        "resource_accounting": {
            "operation_cap_inclusive": MAX_POLYNOMIAL_OPERATIONS,
            "sparse_polynomial_operations": meter.operations,
            "finite_fields": 0,
            "curves": 0,
            "family_members": 0,
        },
        "firewall": [
            "The rational zero curve is coefficient geometry, not a family count law.",
            "Compact-admissible Weil polynomials are not asserted to be Jacobians.",
            "No novelty, RH, GRH, motive, or global Euler-product claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def _render(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    arguments = parser.parse_args()
    actual = _render(build_fixture())
    if arguments.write:
        OUTPUT_PATH.write_text(actual, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return 0
    if not OUTPUT_PATH.is_file():
        raise FileNotFoundError(OUTPUT_PATH)
    expected = OUTPUT_PATH.read_text(encoding="utf-8")
    if actual != expected:
        raise SystemExit(f"fixture drift: run {Path(__file__).name} --write")
    print(f"OK: square-tower bifurcation fixture matches {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
