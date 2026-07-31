#!/usr/bin/env python3
"""Exact polynomial-cardinal regression for L-14321."""
from __future__ import annotations

import argparse
import hashlib
import json
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x14314-xi-cardinal-decomposition.v1"
OUTPUT_SCHEMA = "riemann.x14314-xi-cardinal-decomposition-verification.v1"
SYNTHETIC = "SYNTHETIC_MODEL"
PRODUCTION = "RIEMANN_XI_DIRECTED"
GATE = "CERTIFIED_XI_CARDINAL_AND_WEIL_ZERO_SUM"


class CertificateError(ValueError):
    pass


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError as exc:
            raise CertificateError(f"{name} must be integer text") from exc
    raise CertificateError(f"{name} must be an integer")


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} must be rational text") from exc
    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        raise CertificateError(f"{name} must be an exact rational")
    numerator = exact_int(value["numerator"], f"{name}.numerator")
    denominator = exact_int(value["denominator"], f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


@dataclass(frozen=True)
class QComplex:
    real: Fraction
    imag: Fraction = Fraction(0)

    def __add__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.real - other.real, self.imag - other.imag)

    def __neg__(self) -> "QComplex":
        return QComplex(-self.real, -self.imag)

    def __mul__(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def scale(self, scalar: Fraction) -> "QComplex":
        return QComplex(self.real * scalar, self.imag * scalar)

    def conjugate(self) -> "QComplex":
        return QComplex(self.real, -self.imag)

    def is_zero(self) -> bool:
        return self.real == 0 and self.imag == 0


def qc(value: Any, name: str) -> QComplex:
    if isinstance(value, (int, str)) and not isinstance(value, bool):
        return QComplex(rational(value, name))
    if not isinstance(value, dict) or set(value) != {"real", "imag"}:
        raise CertificateError(f"{name} must be real rational or a {{real,imag}} object")
    return QComplex(
        rational(value["real"], f"{name}.real"),
        rational(value["imag"], f"{name}.imag"),
    )


def qj(value: QComplex) -> dict[str, dict[str, str]]:
    return {
        "real": {"numerator": str(value.real.numerator), "denominator": str(value.real.denominator)},
        "imag": {"numerator": str(value.imag.numerator), "denominator": str(value.imag.denominator)},
    }


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def poly(raw: Any, name: str) -> list[Fraction]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty coefficient array")
    result = [rational(x, f"{name}[{i}]") for i, x in enumerate(raw)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_eval(coefficients: list[Fraction], z: QComplex) -> QComplex:
    value = QComplex(Fraction(0))
    for coefficient in reversed(coefficients):
        value = value * z + QComplex(coefficient)
    return value


def poly_derivative(coefficients: list[Fraction]) -> list[Fraction]:
    if len(coefficients) == 1:
        return [Fraction(0)]
    return [Fraction(i) * coefficients[i] for i in range(1, len(coefficients))]


def divide_linear(coefficients: list[Fraction], root: Fraction) -> tuple[list[Fraction], Fraction]:
    """Divide low-to-high real coefficients by (z-root)."""
    n = len(coefficients) - 1
    if n < 1:
        raise CertificateError("cannot divide a constant polynomial")
    high = list(reversed(coefficients))
    quotient_high = [high[0]]
    for coefficient in high[1:-1]:
        quotient_high.append(coefficient + root * quotient_high[-1])
    remainder = high[-1] + root * quotient_high[-1]
    return list(reversed(quotient_high)), remainder


def poly_add(left: list[Fraction], right: list[Fraction], right_scale: Fraction = Fraction(1)) -> list[Fraction]:
    n = max(len(left), len(right))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        if i < len(left):
            out[i] += left[i]
        if i < len(right):
            out[i] += right_scale * right[i]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def spectral_form(f: list[Fraction], g: list[Fraction], roots: list[QComplex]) -> QComplex:
    total = QComplex(Fraction(0))
    for root in roots:
        total = total + poly_eval(f, root) * poly_eval(g, root.conjugate()).conjugate()
    return total


def valid_sha(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a SHA-256 digest")
    return value.lower()


def canonical_sha(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")
    classification = data.get("classification")
    if classification not in {SYNTHETIC, PRODUCTION}:
        raise CertificateError("unsupported classification")
    if classification == PRODUCTION:
        gate = data.get("analytic_gate")
        if not isinstance(gate, dict) or gate.get("status") != GATE:
            raise CertificateError("production certificate lacks the analytic gate")
        valid_sha(gate.get("sha256"), "analytic_gate.sha256")

    p = poly(data.get("xi_polynomial"), "xi_polynomial")
    roots_raw = data.get("roots")
    if not isinstance(roots_raw, list) or len(roots_raw) != len(p) - 1:
        raise CertificateError("roots must list exactly degree(xi_polynomial) roots")
    roots = [qc(value, f"roots[{i}]") for i, value in enumerate(roots_raw)]
    if len(set(roots)) != len(roots):
        raise CertificateError("roots must be distinct")
    if any(not poly_eval(p, root).is_zero() for root in roots):
        raise CertificateError("a declared root is not a polynomial root")
    root_set = set(roots)
    if any(root.conjugate() not in root_set for root in roots):
        raise CertificateError("root list is not closed under conjugation")

    selected_raw = data.get("selected_real_roots")
    if not isinstance(selected_raw, list) or not selected_raw:
        raise CertificateError("selected_real_roots must be nonempty")
    selected = [rational(value, f"selected_real_roots[{i}]") for i, value in enumerate(selected_raw)]
    if len(set(selected)) != len(selected):
        raise CertificateError("selected roots must be distinct")
    if any(QComplex(root) not in root_set for root in selected):
        raise CertificateError("a selected real root is absent from roots")

    derivative = poly_derivative(p)
    cardinals: list[list[Fraction]] = []
    cardinal_values: list[list[QComplex]] = []
    for j, root in enumerate(selected):
        quotient, remainder = divide_linear(p, root)
        if remainder != 0:
            raise CertificateError("linear division left a nonzero remainder")
        slope_value = poly_eval(derivative, QComplex(root))
        if slope_value.imag != 0 or slope_value.real == 0:
            raise CertificateError("selected root is not simple")
        cardinal = [coefficient / slope_value.real for coefficient in quotient]
        values = [poly_eval(cardinal, z) for z in roots]
        for k, z in enumerate(roots):
            target = QComplex(Fraction(1 if z == QComplex(root) else 0))
            if values[k] != target:
                raise CertificateError(f"cardinal {j} failed at root {k}")
        cardinals.append(cardinal)
        cardinal_values.append(values)

    h = poly(data.get("test_polynomial"), "test_polynomial")
    if len(h) > len(p):
        raise CertificateError("test_polynomial degree must be below xi degree")
    residual = h[:]
    selected_values: list[Fraction] = []
    for root, cardinal in zip(selected, cardinals):
        value = poly_eval(h, QComplex(root))
        if value.imag != 0:
            raise CertificateError("real test polynomial has nonreal selected value")
        selected_values.append(value.real)
        residual = poly_add(residual, cardinal, -value.real)

    if any(not poly_eval(residual, QComplex(root)).is_zero() for root in selected):
        raise CertificateError("residual does not vanish at selected roots")

    q_global = spectral_form(h, h, roots)
    q_residual = spectral_form(residual, residual, roots)
    positive = sum(value * value for value in selected_values)
    if q_global.imag != 0 or q_residual.imag != 0:
        raise CertificateError("spectral form is unexpectedly nonreal")
    if q_global.real != q_residual.real + positive:
        raise CertificateError("cardinal spectral decomposition failed")

    for j, cardinal in enumerate(cardinals):
        cross = spectral_form(residual, cardinal, roots)
        if not cross.is_zero():
            raise CertificateError(f"residual/cardinal cross term {j} is nonzero")
        for k, other in enumerate(cardinals):
            gram = spectral_form(cardinal, other, roots)
            target = QComplex(Fraction(int(j == k)))
            if gram != target:
                raise CertificateError("cardinal spectral Gram is not identity")

    claimed_global = rational(data.get("claimed_global_form"), "claimed_global_form")
    claimed_positive = rational(data.get("claimed_selected_positive"), "claimed_selected_positive")
    claimed_residual = rational(data.get("claimed_residual_form"), "claimed_residual_form")
    if claimed_global != q_global.real:
        raise CertificateError("claimed_global_form is incorrect")
    if claimed_positive != positive:
        raise CertificateError("claimed_selected_positive is incorrect")
    if claimed_residual != q_residual.real:
        raise CertificateError("claimed_residual_form is incorrect")

    proof = {
        "classification": classification,
        "xi_polynomial": [fj(x) for x in p],
        "selected_real_roots": [fj(x) for x in selected],
        "global_form": fj(q_global.real),
        "selected_positive": fj(positive),
        "residual_form": fj(q_residual.real),
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "classification": classification,
        "analytic_claim": "L-14321",
        "degree": len(p) - 1,
        "selected_count": len(selected),
        "cardinal_root_values": [[qj(x) for x in row] for row in cardinal_values],
        "global_form": fj(q_global.real),
        "selected_positive_form": fj(positive),
        "residual_form": fj(q_residual.real),
        "decomposition_check": fj(q_residual.real + positive),
        "exact_proof_object_sha256": canonical_sha(proof),
        "verdict": "CERTIFIED_XI_CARDINAL_SPECTRAL_DECOMPOSITION",
        "proof_boundary": (
            "Exact synthetic polynomial/zero-sum algebra. A Riemann-Xi use also "
            "requires the Fourier-kernel, simple-zero, spectral-form, and localization gates."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(raw)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
