#!/usr/bin/env python3
"""Exact integral spectrum of the square-tower endpoint-three zero curve.

The replay proves a signed-divisor parametrization and the exact factorization
of K=q*a^2-b^2 along the curve.  It uses no finite-field or curve enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path

Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "native_qadic_wavelet_square_integral_spectrum.json"
NOTE_PATH = HERE / "NATIVE_QADIC_WAVELET_SQUARE_INTEGRAL_SPECTRUM.md"
TEST_PATH = ROOT / "tests" / "test_native_qadic_wavelet_square_integral_spectrum.py"

UPSTREAM_FIXTURE_PATH = HERE / "native_qadic_wavelet_square_tower_bifurcation.json"
UPSTREAM_NOTE_PATH = HERE / "NATIVE_QADIC_WAVELET_SQUARE_TOWER_BIFURCATION.md"
UPSTREAM_PRODUCER_PATH = HERE / "native_qadic_wavelet_square_tower_bifurcation.py"
UPSTREAM_TEST_PATH = (
    ROOT / "tests" / "test_native_qadic_wavelet_square_tower_bifurcation.py"
)

EXPECTED_UPSTREAM_PAYLOAD = (
    "4505d667bb9eb1bf43bebf15cffe1e6dd7321245110c8d310aa5fb825669a5e4"
)
S_CROSS_SECTIONS = (3, 5, 7, 9, 11, 13)
MAX_SYMBOLIC_COEFFICIENT_OPERATIONS = 1024
MAX_DIVISOR_TRIALS = 512
MAX_SIGNED_DIVISORS = 512
MAX_WALL_SECONDS = 5.0


@dataclass
class Meter:
    symbolic_operations: int = 0
    divisor_trials: int = 0
    signed_divisors: int = 0

    def symbolic(self, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise TypeError("symbolic charge must be a nonnegative integer")
        self.symbolic_operations += amount
        if self.symbolic_operations > MAX_SYMBOLIC_COEFFICIENT_OPERATIONS:
            raise RuntimeError("symbolic coefficient-operation cap exceeded")

    def divisor(self) -> None:
        self.signed_divisors += 1
        if self.signed_divisors > MAX_SIGNED_DIVISORS:
            raise RuntimeError("signed-divisor cap exceeded")

    def divisor_trial(self) -> None:
        self.divisor_trials += 1
        if self.divisor_trials > MAX_DIVISOR_TRIALS:
            raise RuntimeError("divisor-trial cap exceeded")


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _load_upstream() -> dict[str, object]:
    value = json.loads(UPSTREAM_FIXTURE_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("square-tower source is not an object")
    claimed = value.get("payload_sha256")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != EXPECTED_UPSTREAM_PAYLOAD or claimed != _canonical_sha256(payload):
        raise ValueError("square-tower payload lock failed")
    theorem = value.get("square_field_theorem")
    if not isinstance(theorem, dict):
        raise TypeError("square-field theorem missing")
    expected = {
        "zero_curve": "(2*a+s+1)*b=a*(a^2+(s+1)*a+s*(s+1))",
        "excluded_vertical_a": "-(s+1)/2",
        "vertical_value": "(s+1)^2*(3*s-1)/8",
    }
    if any(
        theorem.get(key) != expected_value for key, expected_value in expected.items()
    ):
        raise ValueError("square-field theorem semantics drifted")
    return value


def _clean(value: Polynomial) -> Polynomial:
    return {
        monomial: coefficient for monomial, coefficient in value.items() if coefficient
    }


def _p_add(
    left: Polynomial, right: Polynomial, meter: Meter, scale: int = 1
) -> Polynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        meter.symbolic()
        result[monomial] = result.get(monomial, 0) + scale * coefficient
    return _clean(result)


def _p_scale(value: Polynomial, scale: int, meter: Meter) -> Polynomial:
    meter.symbolic(len(value))
    return _clean(
        {monomial: scale * coefficient for monomial, coefficient in value.items()}
    )


def _p_mul(left: Polynomial, right: Polynomial, meter: Meter) -> Polynomial:
    result: Polynomial = {}
    for (ai, si), left_coefficient in left.items():
        for (aj, sj), right_coefficient in right.items():
            meter.symbolic()
            key = ai + aj, si + sj
            result[key] = result.get(key, 0) + left_coefficient * right_coefficient
    return _clean(result)


def _p_pow(value: Polynomial, exponent: int, meter: Meter) -> Polynomial:
    if exponent < 0:
        raise ValueError("negative polynomial exponent")
    result: Polynomial = {(0, 0): 1}
    for _ in range(exponent):
        result = _p_mul(result, value, meter)
    return result


def _symbolic_certificate(meter: Meter) -> dict[str, object]:
    one: Polynomial = {(0, 0): 1}
    a: Polynomial = {(1, 0): 1}
    s: Polynomial = {(0, 1): 1}
    two_a = _p_scale(a, 2, meter)
    t = _p_add(_p_add(two_a, s, meter), one, meter)
    s_plus_one = _p_add(s, one, meter)
    three_s_minus_one = _p_add(_p_scale(s, 3, meter), one, meter, -1)
    c_value = _p_mul(_p_pow(s_plus_one, 2, meter), three_s_minus_one, meter)

    a_square = _p_pow(a, 2, meter)
    s_times_s_plus_one = _p_mul(s, s_plus_one, meter)
    inner = _p_add(
        _p_add(a_square, _p_mul(s_plus_one, a, meter), meter), s_times_s_plus_one, meter
    )
    numerator = _p_mul(a, inner, meter)

    division_rhs = _p_add(
        _p_add(
            _p_add(
                _p_pow(t, 3, meter),
                _p_mul(s_plus_one, _p_pow(t, 2, meter), meter),
                meter,
                -1,
            ),
            _p_mul(
                _p_add(
                    _p_add(
                        _p_scale(_p_pow(s, 2, meter), 3, meter),
                        _p_scale(s, 2, meter),
                        meter,
                    ),
                    one,
                    meter,
                    -1,
                ),
                t,
                meter,
            ),
            meter,
        ),
        c_value,
        meter,
        -1,
    )
    if division_rhs != _p_scale(numerator, 8, meter):
        raise ArithmeticError("signed-divisor polynomial identity failed")

    sa_t = _p_mul(_p_mul(s, a, meter), t, meter)
    k_numerator = _p_add(_p_pow(sa_t, 2, meter), _p_pow(numerator, 2, meter), meter, -1)
    factorized = _p_mul(
        _p_mul(
            _p_pow(a, 3, meter),
            _p_add(a, _p_scale(s, 2, meter), meter),
            meter,
        ),
        _p_mul(
            _p_add(_p_add(s, one, meter, -1), a, meter, -1),
            _p_add(_p_add(a, s, meter), one, meter),
            meter,
        ),
        meter,
    )
    if k_numerator != factorized:
        raise ArithmeticError("K chamber factorization failed")

    return {
        "ring": "Z[a,s]",
        "substitution": "t=2*a+s+1",
        "division_identity": (
            "8*a*(a^2+(s+1)*a+s*(s+1))=t^3-(s+1)*t^2+(3*s^2+2*s-1)*t-(s+1)^2*(3*s-1)"
        ),
        "K_identity": (
            "t^2*K=a^3*(a+2*s)*(s-1-a)*(a+s+1) on t*b=a*(a^2+(s+1)*a+s*(s+1))"
        ),
    }


def signed_divisors(value: int, meter: Meter | None = None) -> list[int]:
    if value <= 0:
        raise ValueError("divisor source must be positive")
    positive: list[int] = []
    for divisor in range(1, math.isqrt(value) + 1):
        if meter is not None:
            meter.divisor_trial()
        if value % divisor:
            continue
        positive.append(divisor)
        partner = value // divisor
        if partner != divisor:
            positive.append(partner)
    return sorted([entry for divisor in positive for entry in (divisor, -divisor)])


def k_sign(a_value: int, b_value: int, s_value: int) -> int:
    value = s_value * s_value * a_value * a_value - b_value * b_value
    return (value > 0) - (value < 0)


def compact_admissible(a_value: int, b_value: int, s_value: int) -> bool:
    return (
        abs(a_value) <= 4 * s_value
        and b_value >= 2 * abs(a_value) * s_value - 2 * s_value * s_value
        and 4 * b_value <= a_value * a_value + 8 * s_value * s_value
    )


def point_from_divisor(s_value: int, t_value: int) -> dict[str, int] | None:
    c_value = (s_value + 1) ** 2 * (3 * s_value - 1)
    if t_value == 0 or c_value % t_value:
        raise ValueError("t must be a nonzero signed divisor of C_s")
    if (t_value - s_value - 1) % 2:
        return None
    a_value = (t_value - s_value - 1) // 2
    numerator = (
        t_value * t_value
        - (s_value + 1) * t_value
        + 3 * s_value * s_value
        + 2 * s_value
        - 1
        - c_value // t_value
    )
    if numerator % 8:
        return None
    b_value = numerator // 8
    if t_value * b_value != a_value * (
        a_value * a_value + (s_value + 1) * a_value + s_value * (s_value + 1)
    ):
        raise ArithmeticError("divisor reconstruction missed the zero curve")
    return {
        "a": a_value,
        "b": b_value,
        "t": t_value,
        "K_sign": k_sign(a_value, b_value, s_value),
    }


def _cross_section(s_value: int, meter: Meter) -> dict[str, object]:
    if s_value < 3 or s_value % 2 == 0:
        raise ValueError("s must be odd and at least three")
    c_value = (s_value + 1) ** 2 * (3 * s_value - 1)
    divisors = signed_divisors(c_value, meter)
    points: list[dict[str, int]] = []
    for divisor in divisors:
        meter.divisor()
        point = point_from_divisor(s_value, divisor)
        if point is not None:
            points.append(point)
    points.sort(key=lambda row: (row["a"], row["b"], row["t"]))
    compact = [row for row in points if compact_admissible(row["a"], row["b"], s_value)]
    return {
        "s": s_value,
        "q": s_value * s_value,
        "C_s": c_value,
        "signed_divisors_tested": len(divisors),
        "integral_zero_curve_points": len(points),
        "compact_integral_points": len(compact),
        "compact_rows": compact,
    }


def _source_manifest() -> list[dict[str, str]]:
    paths = (
        UPSTREAM_FIXTURE_PATH,
        UPSTREAM_NOTE_PATH,
        UPSTREAM_PRODUCER_PATH,
        UPSTREAM_TEST_PATH,
        NOTE_PATH,
        Path(__file__).resolve(),
        TEST_PATH,
    )
    return [
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for path in paths
    ]


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    _load_upstream()
    meter = Meter()
    symbolic = _symbolic_certificate(meter)
    rows = [_cross_section(s_value, meter) for s_value in S_CROSS_SECTIONS]
    if [row["compact_integral_points"] for row in rows] != [5, 7, 10, 4, 15, 4]:
        raise ArithmeticError("frozen compact cross-sections changed")

    universal_points = [
        {
            "a": "0",
            "b": "0",
            "t": "s+1",
        },
        {
            "a": "s-1",
            "b": "s*(s-1)",
            "t": "3*s-1",
        },
        {
            "a": "-2*s",
            "b": "2*s^2",
            "t": "-(3*s-1)",
        },
        {
            "a": "-s-1",
            "b": "s*(s+1)",
            "t": "-(s+1)",
        },
    ]

    payload: dict[str, object] = {
        "schema": "riemann.function_field.native_qadic_wavelet_square_integral_spectrum.v1",
        "status": "PROVED_EXACT_SIGNED_DIVISOR_CLASSIFICATION",
        "scope": {
            "q": "q=s^2 for every odd integer s>=3",
            "finite_fields_enumerated": 0,
            "curves_enumerated": 0,
            "family_members_enumerated": 0,
            "numeric_approximations": 0,
        },
        "upstream_payload_lock": EXPECTED_UPSTREAM_PAYLOAD,
        "definitions": {
            "zero_curve": ("(2*a+s+1)*b=a*(a^2+(s+1)*a+s*(s+1))"),
            "t": "2*a+s+1",
            "C_s": "(s+1)^2*(3*s-1)",
            "minor": "K=s^2*a^2-b^2",
        },
        "signed_divisor_theorem": {
            "statement": (
                "integral zero-curve points are in bijection with signed divisors "
                "t of C_s satisfying the parity and mod-8 conditions"
            ),
            "parity_condition": "t == s+1 (mod 2)",
            "mod_8_condition": ("t^2-(s+1)*t+3*s^2+2*s-1-C_s/t == 0 (mod 8)"),
            "recovery_a": "a=(t-s-1)/2",
            "recovery_b": ("b=(t^2-(s+1)*t+3*s^2+2*s-1-C_s/t)/8"),
            "upper_bound": "at most 2*tau(C_s) integral coefficient points",
            "excluded_vertical": (
                "t=0 is not a solution because W_3=(s+1)^2*(3*s-1)/8>0"
            ),
        },
        "compact_intersection": {
            "necessary_and_sufficient_criterion": [
                "abs(a)<=4*s",
                "2*abs(a)*s-2*s^2<=b",
                "4*b<=a^2+8*s^2",
            ],
            "cross_sections": rows,
            "interpretation": (
                "compact-admissible reciprocal spectra only; Jacobian realization "
                "is not asserted"
            ),
        },
        "minor_chambers": {
            "factorization": ("K=a^3*(a+2*s)*(s-1-a)*(a+s+1)/(2*a+s+1)^2"),
            "universal_zero_points": universal_points,
            "universal_divisor_parameters": [
                "s+1",
                "-(s+1)",
                "3*s-1",
                "-(3*s-1)",
            ],
            "sign_intervals": [
                {"interval": "a<-2*s", "sign": -1},
                {"interval": "-2*s<a<-s-1", "sign": 1},
                {"interval": "-s-1<a<0", "sign": -1},
                {"interval": "0<a<s-1", "sign": 1},
                {"interval": "a>s-1", "sign": -1},
            ],
        },
        "symbolic_certificate": symbolic,
        "resource_contract": {
            "symbolic_coefficient_operations": meter.symbolic_operations,
            "maximum_symbolic_coefficient_operations": (
                MAX_SYMBOLIC_COEFFICIENT_OPERATIONS
            ),
            "divisor_trials": meter.divisor_trials,
            "maximum_divisor_trials": MAX_DIVISOR_TRIALS,
            "signed_divisors_evaluated": meter.signed_divisors,
            "maximum_signed_divisors": MAX_SIGNED_DIVISORS,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": "exact integers only",
        },
        "firewalls": [
            "The divisor theorem classifies coefficient-lattice points, not curves or family multiplicities.",
            "Compact admissibility does not assert abelian-surface or Jacobian realization.",
            "The K sign chambers are not a memberwise RH criterion.",
            "No motive, compatible system, global Euler-product, or novelty claim is made.",
        ],
        "source_manifest": _source_manifest(),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    if time.perf_counter() - started > MAX_WALL_SECONDS:
        raise RuntimeError("integral-spectrum replay exceeded wall cap")
    return payload


def _main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(fixture, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {OUTPUT_PATH}")
        return 0
    checked_in = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    if checked_in != fixture:
        raise SystemExit(f"fixture drift: regenerate {OUTPUT_PATH}")
    print(f"OK: integral-spectrum fixture matches {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
