#!/usr/bin/env python3
"""Exact second moment and sharp two-moment sign floor for the genus-two toy minor.

This is a consequence packet.  It source-locks the separately proved first
moment, A4, M22, and B4 identities together with the exact USp(4) support
range, closes E[K_D^2] by exact Laurent-polynomial algebra, and proves the
optimal Cantelli lower bound within the information class consisting only of
support plus the first two moments.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_toy_minor_second_moment.json"
NOTE_PATH = HERE / "GENUS2_TOY_MINOR_SECOND_MOMENT.md"
TEST_PATH = ROOT / "tests" / "test_genus2_toy_minor_second_moment.py"

SECOND_REDUCTION_PATH = HERE / "genus2_second_moment_reduction.json"
M22_PATH = HERE / "genus2_m22_triangular_trace_average.json"
B4_PATH = HERE / "genus2_b4_triangular_trace_average.json"
Q_SCAN_PATH = HERE / "genus2_q_scan.json"
USP4_RANGE_PATH = HERE / "usp4_toy_minor_moments.json"

EXPECTED_PAYLOAD_SHA256 = {
    "second_reduction": "55c5c9ef04a65ca46044ac1d76c76f33afc02b51c2d38a8ca196b99498ee16ec",
    "M22": "4d147295e3d2b7bc4b62eb8ba113c946f528606d82dd28d1a1ec002e2f93d60c",
    "B4": "d12099e24425badd5106f61caa151578ee04dd099a221eca7217b599783c5e5b",
    "q_scan": "80a28d820e45b2548e3e4b482982ef8313c8919f4a3fb9cc2c0b622b244870b5",
    "usp4_range": "843a2fe286e52bcf83f971c624454c8a2e8c69e8c894b79c898728ff74e35e6f",
}
EXPECTED_LF_SHA256 = {
    "second_reduction": "0966565c0b29d7bf85f6ad20f8c6634365a8fff674e3c3b06589125fe0bdbaf0",
    "M22": "a93f288ddce023005989cc0a7ed543d859697e68fa378a24ae7619af35fc9633",
    "B4": "31eec8f78bc81eb9d157f727c229efb16d112b94e7c27dbf0ea1f81f5005fde2",
    "q_scan": "b49b7e2803401904b0bc1f82eb442bf1d8e81bdeb1ec388ff7fb14e7e5628dc6",
    "usp4_range": "6544641ac6a8f164d774f7e846926774659f6f0e0554c56b6850f12d6c79de42",
}

MAX_LAURENT_UPDATES = 512
MAX_TRANSLATION_UPDATES = 256
MAX_HISTOGRAM_ATOMS = 256
MAX_WALL_SECONDS = 3.0

Laurent: TypeAlias = dict[int, Fraction]


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


def _load_locked(name: str, path: Path) -> dict[str, object]:
    if _lf_sha256(path) != EXPECTED_LF_SHA256[name]:
        raise RuntimeError(f"source-locked file changed: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected object fixture: {path}")
    claimed = value.get("payload_sha256")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ValueError(f"invalid embedded payload hash: {path}")
    if claimed != EXPECTED_PAYLOAD_SHA256[name]:
        raise ValueError(f"source payload changed: {path}")
    return value


class Algebra:
    def __init__(self) -> None:
        self.updates = 0
        self.translation_updates = 0

    def _guard(self, count: int) -> None:
        self.updates += count
        if self.updates > MAX_LAURENT_UPDATES:
            raise RuntimeError("Laurent update cap exceeded")

    def translation_tick(self) -> None:
        self.translation_updates += 1
        if self.translation_updates > MAX_TRANSLATION_UPDATES:
            raise RuntimeError("translation update cap exceeded")

    def clean(self, value: Laurent) -> Laurent:
        result = {
            degree: coefficient for degree, coefficient in value.items() if coefficient
        }
        self._guard(len(value))
        return result

    def add(self, left: Laurent, right: Laurent) -> Laurent:
        result = dict(left)
        for degree, coefficient in right.items():
            result[degree] = result.get(degree, Fraction(0)) + coefficient
        return self.clean(result)

    def scale(self, value: Laurent, scalar: int | Fraction) -> Laurent:
        factor = Fraction(scalar)
        return self.clean(
            {degree: factor * coefficient for degree, coefficient in value.items()}
        )

    def multiply(self, left: Laurent, right: Laurent) -> Laurent:
        result: Laurent = {}
        for left_degree, left_coefficient in left.items():
            for right_degree, right_coefficient in right.items():
                degree = left_degree + right_degree
                result[degree] = (
                    result.get(degree, Fraction(0))
                    + left_coefficient * right_coefficient
                )
                self._guard(1)
        return self.clean(result)

    def derivative(self, value: Laurent) -> Laurent:
        return self.clean(
            {
                degree - 1: degree * coefficient
                for degree, coefficient in value.items()
                if degree
            }
        )


def _poly(*coefficients_low_to_high: int) -> Laurent:
    return {
        degree: Fraction(coefficient)
        for degree, coefficient in enumerate(coefficients_low_to_high)
        if coefficient
    }


def _shift(value: Laurent, amount: int) -> Laurent:
    return {degree + amount: coefficient for degree, coefficient in value.items()}


def _pairs(value: Laurent) -> list[list[int]]:
    if not value:
        return []
    low = min(value)
    high = max(value)
    rows: list[list[int]] = []
    for degree in range(low, high + 1):
        coefficient = value.get(degree, Fraction(0))
        if coefficient.denominator != 1:
            raise ValueError("expected integral Laurent coefficients")
        rows.append([degree, coefficient.numerator])
    return rows


def _evaluate(value: Laurent, q: int) -> Fraction:
    total = Fraction(0)
    for degree, coefficient in value.items():
        total += coefficient * (Fraction(q) ** degree)
    return total


def _dense_integral_coefficients(value: Laurent) -> list[int]:
    if not value:
        return []
    if min(value) < 0:
        raise ValueError("expected an ordinary polynomial")
    result: list[int] = []
    for degree in range(max(value) + 1):
        coefficient = value.get(degree, Fraction(0))
        if coefficient.denominator != 1:
            raise ValueError("expected integral polynomial coefficients")
        result.append(coefficient.numerator)
    return result


def _translate_nonnegative(
    coefficients: list[int], algebra: Algebra, shift: int = 3
) -> list[int]:
    """Return coefficients of P(t+shift), low to high, exactly."""
    result = [0] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for chosen in range(degree + 1):
            # Small local binomial avoids importing a symbolic dependency.
            numerator = 1
            denominator = 1
            for index in range(chosen):
                numerator *= degree - index
                denominator *= index + 1
            result[chosen] += (
                coefficient * (numerator // denominator) * shift ** (degree - chosen)
            )
            algebra.translation_tick()
    return result


def _assert_source_theorems(
    second: dict[str, object],
    m22: dict[str, object],
    b4: dict[str, object],
    q_scan: dict[str, object],
) -> None:
    master = second.get("master_reduction")
    if not isinstance(master, dict):
        raise TypeError("missing second-moment master reduction")
    if master.get("formula") != "sum_D K_D^2=q^2*A4(q)-2*q*M22(q)+B4(q)":
        raise ValueError("second-moment reduction formula changed")
    proven_a4 = master.get("proven_A4")
    if not isinstance(proven_a4, dict) or proven_a4.get("mean") != (
        "3*q^2-7*q+5+12/q-14/q^2-11/q^3"
    ):
        raise ValueError("A4 theorem changed")

    m22_theorem = m22.get("theorem")
    if not isinstance(m22_theorem, dict) or m22_theorem.get("M22_mean") != (
        "E[a_D^2*b_D^2]=(q+1)*(5*q^5-19*q^4+29*q^3-5*q^2-21*q-3)/q^3"
    ):
        raise ValueError("M22 theorem changed")

    b4_theorem = b4.get("theorem")
    if not isinstance(b4_theorem, dict) or b4_theorem.get("B4_mean") != (
        "E[b_D^4]=(10*q^7-29*q^6+21*q^5+44*q^4-47*q^3-56*q^2-10*q-1)/q^3"
    ):
        raise ValueError("B4 theorem changed")

    closed_formula = q_scan.get("closed_formula_target")
    if not isinstance(closed_formula, dict) or (
        closed_formula.get("mean_K"),
        closed_formula.get("normalized_mean_K"),
    ) != (
        "-(q-1)^2+(q+1)/q^3",
        "-(1-1/q)^2+(q+1)/q^5",
    ):
        raise ValueError("first-moment theorem changed")


def _held_out_histogram_controls(
    q_scan: dict[str, object], second_moment: Laurent
) -> list[dict[str, object]]:
    families = q_scan.get("families")
    if not isinstance(families, list):
        raise TypeError("q scan has no family list")
    controls: list[dict[str, object]] = []
    atoms = 0
    for row in families:
        if not isinstance(row, dict):
            raise TypeError("invalid family row")
        q = row.get("q")
        histogram = row.get("K_histogram")
        members = row.get("member_count")
        if (
            not isinstance(q, int)
            or not isinstance(histogram, dict)
            or not isinstance(members, int)
        ):
            raise TypeError("invalid q-scan histogram row")
        atoms += len(histogram)
        if atoms > MAX_HISTOGRAM_ATOMS:
            raise RuntimeError("histogram atom cap exceeded")
        direct_sum = sum(int(k) ** 2 * int(count) for k, count in histogram.items())
        direct_mean = Fraction(direct_sum, members)
        formula_mean = _evaluate(second_moment, q)
        if direct_mean != formula_mean:
            raise ArithmeticError(f"held-out K^2 control failed at q={q}")
        controls.append(
            {
                "q": q,
                "members": members,
                "histogram_atoms": len(histogram),
                "sum_K_squared": direct_sum,
                "mean_K_squared": [direct_mean.numerator, direct_mean.denominator],
                "matches_all_q_formula": True,
            }
        )
    return controls


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    second = _load_locked("second_reduction", SECOND_REDUCTION_PATH)
    m22_source = _load_locked("M22", M22_PATH)
    b4_source = _load_locked("B4", B4_PATH)
    q_scan = _load_locked("q_scan", Q_SCAN_PATH)
    usp4_range = _load_locked("usp4_range", USP4_RANGE_PATH)
    _assert_source_theorems(second, m22_source, b4_source, q_scan)
    range_certificate = usp4_range.get("range_certificate")
    if not isinstance(range_certificate, dict) or (
        range_certificate.get("minimum"),
        range_certificate.get("maximum"),
    ) != ([-20, 1], [4, 3]):
        raise ValueError("USp(4) range certificate changed")

    algebra = Algebra()
    q_plus_1 = _poly(1, 1)
    a4 = {
        2: Fraction(3),
        1: Fraction(-7),
        0: Fraction(5),
        -1: Fraction(12),
        -2: Fraction(-14),
        -3: Fraction(-11),
    }
    m22_numerator = _poly(-3, -21, -5, 29, -19, 5)
    m22 = _shift(algebra.multiply(q_plus_1, m22_numerator), -3)
    b4 = _shift(_poly(-1, -10, -56, -47, 44, 21, -29, 10), -3)
    mean_k = algebra.add(
        algebra.scale(algebra.multiply(_poly(-1, 1), _poly(-1, 1)), -1),
        _shift(q_plus_1, -3),
    )
    mean_k_squared = algebra.add(
        algebra.add(_shift(a4, 2), algebra.scale(_shift(m22, 1), -2)),
        b4,
    )
    variance = algebra.add(
        mean_k_squared, algebra.scale(algebra.multiply(mean_k, mean_k), -1)
    )

    expected_mean_k_squared = _shift(_poly(-1, -4, -19, -9, 8, 6, -8, 3), -3)
    expected_variance = _shift(
        algebra.multiply(q_plus_1, _poly(-1, -1, 0, 1, -7, -14, 6, 6, -6, 2)),
        -6,
    )
    if mean_k_squared != expected_mean_k_squared:
        raise ArithmeticError("K^2 closure failed")
    if variance != expected_variance:
        raise ArithmeticError("variance closure failed")

    deficit = _poly(-1, -1, 0, 1, -2, 1)
    k2_numerator = _poly(-1, -4, -19, -9, 8, 6, -8, 3)
    monotonicity_factor = _poly(-3, -17, -103, -114, 22, 94, 54, -93, -40, 48, -16, 4)
    one_third_gap = _poly(-3, -6, -3, 5, -10, -25, -6, 20, -12, 4)
    old_bound_gap = _poly(1, 4, -1, -11, -8, 14, -32, 17)

    # For C=P^2/(q^3*N), differentiation reduces its numerator to
    # P*(2*q*P'*N-P*(3*N+q*N')).  Verify the stored D exactly.
    deficit_derivative = algebra.derivative(deficit)
    k2_derivative = algebra.derivative(k2_numerator)
    calculated_monotonicity_factor = algebra.add(
        algebra.scale(algebra.multiply(_shift(deficit_derivative, 1), k2_numerator), 2),
        algebra.scale(
            algebra.multiply(
                deficit,
                algebra.add(algebra.scale(k2_numerator, 3), _shift(k2_derivative, 1)),
            ),
            -1,
        ),
    )
    if calculated_monotonicity_factor != monotonicity_factor:
        raise ArithmeticError("Cantelli derivative identity failed")

    calculated_one_third_gap = algebra.add(
        _shift(k2_numerator, 3),
        algebra.scale(algebra.multiply(deficit, deficit), -3),
    )
    if calculated_one_third_gap != one_third_gap:
        raise ArithmeticError("one-third gap identity failed")

    # The saturating two-point law uses x_q=E[Z^2]/E[Z]=-N/(q^2 P).
    # The strict support inequality x_q>-20 is exactly 20*q^2*P-N=G>0.
    twenty_q2_deficit_minus_k2 = algebra.add(
        algebra.scale(_shift(deficit, 2), 20), algebra.scale(k2_numerator, -1)
    )
    if twenty_q2_deficit_minus_k2 != old_bound_gap:
        raise ArithmeticError("support witness identity failed")

    shifted = {
        "mean_deficit": _translate_nonnegative(
            _dense_integral_coefficients(deficit), algebra
        ),
        "K2_numerator": _translate_nonnegative(
            _dense_integral_coefficients(k2_numerator), algebra
        ),
        "monotonicity_factor": _translate_nonnegative(
            _dense_integral_coefficients(monotonicity_factor), algebra
        ),
        "one_third_gap": _translate_nonnegative(
            _dense_integral_coefficients(one_third_gap), algebra
        ),
        "old_bound_gap": _translate_nonnegative(
            _dense_integral_coefficients(old_bound_gap), algebra
        ),
    }
    if any(any(coefficient <= 0 for coefficient in row) for row in shifted.values()):
        raise ArithmeticError("shifted positivity certificate failed")

    controls = _held_out_histogram_controls(q_scan, mean_k_squared)
    q3_bound = Fraction(1352, 8127)
    if (
        Fraction(_evaluate(deficit, 3) ** 2, 1)
        / (Fraction(3**3) * _evaluate(k2_numerator, 3))
        != q3_bound
    ):
        raise ArithmeticError("q=3 Cantelli endpoint changed")

    if algebra.updates > MAX_LAURENT_UPDATES:
        raise RuntimeError("Laurent update cap exceeded")
    if algebra.translation_updates > MAX_TRANSLATION_UPDATES:
        raise RuntimeError("translation update cap exceeded")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("second-moment consequence replay exceeded wall cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_toy_minor_second_moment.v1",
        "status": "PROVED_EXACT_ALL_ODD_PRIME_POWERS",
        "scope": {
            "q": "every odd prime power",
            "family": "all monic squarefree quintics D in F_q[T]",
            "statistic": "K_D=q*a_D^2-b_D^2 and Z_D=K_D/q^2",
            "finite_fields_enumerated_by_theorem_replay": 0,
            "sampled_values_used_as_theorem_input": 0,
        },
        "theorem": {
            "mean_K_squared": "E[K_D^2]=(3*q^7-8*q^6+6*q^5+8*q^4-9*q^3-19*q^2-4*q-1)/q^3",
            "mean_Z_squared": "E[Z_D^2]=(3*q^7-8*q^6+6*q^5+8*q^4-9*q^3-19*q^2-4*q-1)/q^7",
            "variance_K": "Var(K_D)=(q+1)*(2*q^9-6*q^8+6*q^7+6*q^6-14*q^5-7*q^4+q^3-q-1)/q^6",
            "variance_Z_limit": 2,
            "mean_Z_squared_limit": 3,
        },
        "sign_density": {
            "cantelli_bound": "Pr(K_D<0)>=P(q)^2/[q^3*N(q)]",
            "P(q)": "q^5-2*q^4+q^3-q-1",
            "N(q)": "3*q^7-8*q^6+6*q^5+8*q^4-9*q^3-19*q^2-4*q-1",
            "monotonicity": "strictly increasing for every real q>=3",
            "q3_value": [q3_bound.numerator, q3_bound.denominator],
            "limit": [1, 3],
            "strictly_stronger_than_old_range_bound": "P(q)/(20*q^5) for every real q>=3",
            "sharp_information_class": (
                "No larger universal lower bound follows from only support Z in [-20,4/3], E[Z], and E[Z^2]: "
                "the two-point law on {x_q,0}, x_q=-N(q)/(q^2*P(q)) in [-20,0), has negative mass exactly P(q)^2/[q^3*N(q)]."
            ),
            "improvement_requires": [
                "a third or higher moment",
                "an independent constraint on the zero atom",
                "or arithmetic/geometric information beyond support and two moments",
            ],
        },
        "algebra_certificate": {
            "A4_low_to_high": _pairs(a4),
            "M22_low_to_high": _pairs(m22),
            "B4_low_to_high": _pairs(b4),
            "mean_K_low_to_high": _pairs(mean_k),
            "mean_K_squared_low_to_high": _pairs(mean_k_squared),
            "variance_K_low_to_high": _pairs(variance),
            "shifted_positive_coefficients_low_to_high": shifted,
            "derivative_identity": "C'(q)=P(q)*D(q)/[q^4*N(q)^2] with D(q+3) coefficientwise positive",
            "one_third_identity": "1/3-C(q)=R(q)/[3*q^3*N(q)] with R(q+3) coefficientwise positive",
            "old_bound_identity": "C(q)-P(q)/(20*q^5)=P(q)*G(q)/[20*q^5*N(q)] with G(q+3) coefficientwise positive",
        },
        "held_out_falsification_controls": controls,
        "source_manifest": {
            **{
                name: {
                    "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "payload_sha256": EXPECTED_PAYLOAD_SHA256[name],
                    "lf_sha256": EXPECTED_LF_SHA256[name],
                }
                for name, path in {
                    "second_reduction": SECOND_REDUCTION_PATH,
                    "M22": M22_PATH,
                    "B4": B4_PATH,
                    "q_scan": Q_SCAN_PATH,
                    "usp4_range": USP4_RANGE_PATH,
                }.items()
            },
            **{
                name: {
                    "path": str(path.resolve().relative_to(ROOT)).replace("\\", "/"),
                    "lf_sha256": _lf_sha256(path),
                }
                for name, path in {
                    "packet_note": NOTE_PATH,
                    "packet_producer": Path(__file__).resolve(),
                    "packet_test": TEST_PATH,
                }.items()
            },
        },
        "resource_contract": {
            "maximum_laurent_updates": MAX_LAURENT_UPDATES,
            "actual_laurent_updates": algebra.updates,
            "maximum_translation_updates": MAX_TRANSLATION_UPDATES,
            "actual_translation_updates": algebra.translation_updates,
            "maximum_histogram_atoms": MAX_HISTOGRAM_ATOMS,
            "actual_histogram_atoms": sum(row["histogram_atoms"] for row in controls),
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "held_out_histograms_are_not_theorem_inputs": True,
            "first_moment_source": (
                "the locked q-scan closed_formula_target; its q=3,5,7 "
                "histograms remain held-out controls"
            ),
        },
        "firewalls": [
            "The K^2 theorem is an exact consequence of separately source-locked all-q A4, M22, and B4 theorems; it is not interpolated from q=3,5,7.",
            "The sharpness statement concerns what support and two moments alone can prove; the saturating law is not asserted to be an arithmetic family law.",
            "The toy coefficient minor K_D is not XD, HCNC, Pick/Loewner, RH, or GRH.",
            "No equidistribution or novelty claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(
                fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    if args.check:
        stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: second-moment fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
