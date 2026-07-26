#!/usr/bin/env python3
"""Exact rational checker for slab-complement cross-height Pick localizers.

The checker evaluates no special function and certifies no zero. It consumes
exact rational rectangles for F=xi'/xi, an exact Gaussian-rational zero-sum
vector, and a complete list of certified critical-line zero bins in one slab.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "riemann.slab-complement-pick.v1"
VERIFY_SCHEMA = "riemann.slab-complement-pick.verification.v1"
GOOD_GATES = {"PROVED", "INDEPENDENTLY_VERIFIED", "SYNTHETIC_CONTROL"}


class CertificateError(ValueError):
    pass


def q(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name}: boolean is not rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name}: invalid rational {value!r}") from exc
    if isinstance(value, list) and len(value) == 2:
        p = q(value[0], f"{name}[0]")
        r = q(value[1], f"{name}[1]")
        if p.denominator != 1 or r.denominator != 1 or r == 0:
            raise CertificateError(f"{name}: [p,q] requires integers and q!=0")
        return Fraction(p.numerator, r.numerator)
    raise CertificateError(f"{name}: rational required")


def integer(value: Any, name: str) -> int:
    out = q(value, name)
    if out.denominator != 1:
        raise CertificateError(f"{name}: integer required")
    return out.numerator


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    @classmethod
    def exact(cls, value: Fraction) -> "Interval":
        return cls(value, value)

    @classmethod
    def parse(cls, raw: Any, name: str) -> "Interval":
        if not isinstance(raw, dict) or set(raw) != {"lower", "upper"}:
            raise CertificateError(f"{name}: expected lower/upper object")
        return cls(q(raw["lower"], f"{name}.lower"), q(raw["upper"], f"{name}.upper"))

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lo - other.hi, self.hi - other.lo)

    def scale(self, value: Fraction) -> "Interval":
        if value >= 0:
            return Interval(value * self.lo, value * self.hi)
        return Interval(value * self.hi, value * self.lo)

    def mul(self, other: "Interval") -> "Interval":
        values = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return Interval(min(values), max(values))

    def reciprocal_positive(self) -> "Interval":
        if self.lo <= 0:
            raise CertificateError("positive interval required for reciprocal")
        return Interval(1 / self.hi, 1 / self.lo)

    def distance_to_zero(self) -> Fraction:
        if self.lo <= 0 <= self.hi:
            return Fraction(0)
        return min(abs(self.lo), abs(self.hi))

    def max_abs(self) -> Fraction:
        return max(abs(self.lo), abs(self.hi))

    def to_json(self) -> dict[str, str]:
        return {"lower": text(self.lo), "upper": text(self.hi)}


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction

    @classmethod
    def parse(cls, raw: Any, name: str) -> "QComplex":
        if not isinstance(raw, dict) or set(raw) != {"re", "im"}:
            raise CertificateError(f"{name}: expected re/im object")
        return cls(q(raw["re"], f"{name}.re"), q(raw["im"], f"{name}.im"))

    def add(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re + other.re, self.im + other.im)

    def sub(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re - other.re, self.im - other.im)

    def mul(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re * other.re - self.im * other.im,
                        self.re * other.im + self.im * other.re)

    def conj(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def div(self, other: "QComplex") -> "QComplex":
        denominator = other.re * other.re + other.im * other.im
        if denominator == 0:
            raise CertificateError("complex division by zero")
        return QComplex((self.re * other.re + self.im * other.im) / denominator,
                        (self.im * other.re - self.re * other.im) / denominator)

    def to_json(self) -> dict[str, str]:
        return {"re": text(self.re), "im": text(self.im)}


ZERO = QComplex(Fraction(0), Fraction(0))
ONE = QComplex(Fraction(1), Fraction(0))


@dataclass(frozen=True)
class CInterval:
    re: Interval
    im: Interval

    @classmethod
    def parse(cls, raw: Any, name: str) -> "CInterval":
        if not isinstance(raw, dict) or set(raw) != {"real", "imag"}:
            raise CertificateError(f"{name}: expected real/imag interval object")
        return cls(Interval.parse(raw["real"], f"{name}.real"),
                   Interval.parse(raw["imag"], f"{name}.imag"))

    @classmethod
    def exact(cls, value: QComplex) -> "CInterval":
        return cls(Interval.exact(value.re), Interval.exact(value.im))

    def add(self, other: "CInterval") -> "CInterval":
        return CInterval(self.re.add(other.re), self.im.add(other.im))

    def mul_exact(self, value: QComplex) -> "CInterval":
        return CInterval(self.re.scale(value.re).add(self.im.scale(-value.im)),
                         self.re.scale(value.im).add(self.im.scale(value.re)))

    def modulus2(self) -> Interval:
        lower = self.re.distance_to_zero() ** 2 + self.im.distance_to_zero() ** 2
        upper = self.re.max_abs() ** 2 + self.im.max_abs() ** 2
        return Interval(lower, upper)


@dataclass(frozen=True)
class Point:
    identifier: str
    z: QComplex
    f: CInterval
    gate_id: str


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def parse_points(payload: dict[str, Any]) -> tuple[list[Point], set[str]]:
    raw = payload.get("points")
    if not isinstance(raw, list) or not raw:
        raise CertificateError("points must be a nonempty list")
    out: list[Point] = []
    ids: set[str] = set()
    gates: set[str] = set()
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = item.get("id")
        gate_id = item.get("gate_id")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise CertificateError("invalid or duplicate point id")
        if not isinstance(gate_id, str) or not gate_id:
            raise CertificateError(f"point {identifier!r} lacks gate_id")
        z = QComplex(q(item.get("x"), f"points[{index}].x"),
                     q(item.get("t"), f"points[{index}].t"))
        if z.re <= 0:
            raise CertificateError(f"point {identifier!r} is not in Re(s)>1/2")
        out.append(Point(identifier, z,
                         CInterval.parse(item.get("f"), f"points[{index}].f"), gate_id))
        ids.add(identifier)
        gates.add(gate_id)
    return out, gates


def parse_vector(payload: dict[str, Any], size: int) -> list[QComplex]:
    raw = payload.get("vector")
    if not isinstance(raw, list) or len(raw) != size:
        raise CertificateError("vector dimension does not match point table")
    out = [QComplex.parse(item, f"vector[{index}]") for index, item in enumerate(raw)]
    if all(value == ZERO for value in out):
        raise CertificateError("vector is zero")
    total = ZERO
    for value in out:
        total = total.add(value)
    if total != ZERO:
        raise CertificateError("vector must have exact zero sum")
    return out


def parse_bins(payload: dict[str, Any], slab_lo: Fraction, slab_hi: Fraction,
               expected_count: int) -> tuple[list[tuple[str, Interval, int, str]], set[str]]:
    raw = payload.get("zero_bins")
    if not isinstance(raw, list) or not raw:
        raise CertificateError("zero_bins must be a nonempty list")
    rows: list[tuple[str, Interval, int, str]] = []
    ids: set[str] = set()
    gates: set[str] = set()
    count_sum = 0
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            raise CertificateError(f"zero_bins[{index}] must be an object")
        identifier = item.get("id")
        gate_id = item.get("gate_id")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise CertificateError("invalid or duplicate zero-bin id")
        if not isinstance(gate_id, str) or not gate_id:
            raise CertificateError(f"zero bin {identifier!r} lacks gate_id")
        interval = Interval(q(item.get("lower"), f"zero_bins[{index}].lower"),
                            q(item.get("upper"), f"zero_bins[{index}].upper"))
        count = integer(item.get("count"), f"zero_bins[{index}].count")
        if count <= 0:
            raise CertificateError(f"zero bin {identifier!r} has nonpositive count")
        if not slab_lo < interval.lo <= interval.hi < slab_hi:
            raise CertificateError(f"zero bin {identifier!r} is not strictly inside the slab")
        rows.append((identifier, interval, count, gate_id))
        ids.add(identifier)
        gates.add(gate_id)
        count_sum += count
    rows.sort(key=lambda row: (row[1].lo, row[1].hi, row[0]))
    for left, right in zip(rows, rows[1:]):
        if left[1].hi >= right[1].lo:
            raise CertificateError("zero bins overlap or share an endpoint")
    if count_sum != expected_count:
        raise CertificateError("zero-bin multiplicities do not equal the exact slab count")
    return rows, gates


def parse_gates(payload: dict[str, Any], used: set[str]) -> dict[str, Any]:
    raw = payload.get("logical_gates")
    if not isinstance(raw, list):
        raise CertificateError("logical_gates must be a list")
    found: set[str] = set()
    states: list[str] = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            raise CertificateError(f"logical_gates[{index}] must be an object")
        identifier, state, evidence = item.get("id"), item.get("state"), item.get("evidence")
        if not isinstance(identifier, str) or not identifier or identifier in found:
            raise CertificateError("invalid or duplicate logical gate id")
        if state not in GOOD_GATES:
            raise CertificateError(f"logical gate {identifier!r} remains blocking")
        if not isinstance(evidence, str) or not evidence:
            raise CertificateError(f"logical gate {identifier!r} lacks evidence")
        found.add(identifier)
        states.append(state)
    if found != used:
        raise CertificateError(f"logical gate manifest mismatch: declared={sorted(found)}, used={sorted(used)}")
    return {"logical_gate_count": len(states),
            "logical_manifest_closed": all(state != "SYNTHETIC_CONTROL" for state in states),
            "synthetic_gate_count": states.count("SYNTHETIC_CONTROL")}


def alpha(z_i: QComplex, z_j: QComplex, slab_lo: Fraction, slab_hi: Fraction) -> QComplex:
    # Center first: algebraically identical, but avoids huge high-ordinate cancellation.
    center = (slab_lo + slab_hi) / 2
    half_width = (slab_hi - slab_lo) / 2
    w_i = QComplex(z_i.re, z_i.im - center)
    w_j = QComplex(z_j.re, z_j.im - center)
    numerator = QComplex(-(half_width * half_width), Fraction(0)).sub(w_i.mul(w_i))
    return numerator.div(w_i.add(w_j.conj()))


def ordinary_coefficients(points: list[Point], vector: list[QComplex]) -> list[QComplex]:
    out: list[QComplex] = []
    for point_i, value_i in zip(points, vector):
        inner = ZERO
        for point_j, value_j in zip(points, vector):
            inner = inner.add(value_j.mul(ONE.div(point_i.z.add(point_j.z.conj()))))
        out.append(value_i.conj().mul(inner))
    return out


def weighted_coefficients(points: list[Point], vector: list[QComplex],
                          slab_lo: Fraction, slab_hi: Fraction) -> list[QComplex]:
    out: list[QComplex] = []
    for point_i, value_i in zip(points, vector):
        inner = ZERO
        for point_j, value_j in zip(points, vector):
            inner = inner.add(value_j.mul(alpha(point_i.z, point_j.z, slab_lo, slab_hi)))
        out.append(value_i.conj().mul(inner))
    return out


def contract_f(coefficients: Iterable[QComplex], points: list[Point]) -> Interval:
    total = Interval.exact(Fraction(0))
    for coefficient, point in zip(coefficients, points):
        contribution = point.f.re.scale(coefficient.re).add(point.f.im.scale(-coefficient.im))
        total = total.add(contribution)
    return total.scale(Fraction(2))


def reciprocal_rectangle(z: QComplex, gamma: Interval) -> CInterval:
    y = Interval(z.im - gamma.hi, z.im - gamma.lo)
    y2_min = Fraction(0) if y.lo <= 0 <= y.hi else min(y.lo * y.lo, y.hi * y.hi)
    y2_max = max(y.lo * y.lo, y.hi * y.hi)
    inv = Interval(z.re * z.re + y2_min,
                   z.re * z.re + y2_max).reciprocal_positive()
    return CInterval(inv.scale(z.re), Interval(-y.hi, -y.lo).mul(inv))


def phi_rectangle(points: list[Point], vector: list[QComplex], gamma: Interval) -> CInterval:
    total = CInterval.exact(ZERO)
    for point, value in zip(points, vector):
        total = total.add(reciprocal_rectangle(point.z, gamma).mul_exact(value.conj()))
    return total


def quadratic_range(gamma: Interval, slab_lo: Fraction, slab_hi: Fraction) -> Interval:
    def evaluate(value: Fraction) -> Fraction:
        return (value - slab_lo) * (value - slab_hi)
    candidates = [evaluate(gamma.lo), evaluate(gamma.hi)]
    vertex = (slab_lo + slab_hi) / 2
    if gamma.lo <= vertex <= gamma.hi:
        candidates.append(evaluate(vertex))
    return Interval(min(candidates), max(candidates))


def classify(interval: Interval) -> tuple[str, Fraction]:
    if interval.hi < 0:
        return "CERTIFIED_NEGATIVE_SLAB_COMPLEMENT_WITNESS", -interval.hi
    if interval.lo >= 0:
        return "CERTIFIED_NONNEGATIVE_CONTROL", Fraction(0)
    return "UNRESOLVED_ZERO_TOUCH", Fraction(0)


def check_claim(payload: dict[str, Any], key: str, interval: Interval) -> None:
    raw = payload.get(key)
    if raw is not None and Interval.parse(raw, key) != interval:
        raise CertificateError(f"{key} does not match exact reconstruction")


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    slab = payload.get("slab")
    if not isinstance(slab, dict):
        raise CertificateError("slab must be an object")
    slab_lo = q(slab.get("lower"), "slab.lower")
    slab_hi = q(slab.get("upper"), "slab.upper")
    exact_count = integer(slab.get("exact_zero_count"), "slab.exact_zero_count")
    complete_gate = slab.get("complete_gate_id")
    endpoint_gate = slab.get("endpoint_gate_id")
    parent_gate = payload.get("parent_gate_id")
    if slab_lo >= slab_hi:
        raise CertificateError("slab endpoints are not increasing")
    if exact_count <= 0:
        raise CertificateError("slab exact_zero_count must be positive")
    for value, name in ((complete_gate, "slab.complete_gate_id"),
                        (endpoint_gate, "slab.endpoint_gate_id"),
                        (parent_gate, "parent_gate_id")):
        if not isinstance(value, str) or not value:
            raise CertificateError(f"{name} must be a nonempty string")

    points, point_gates = parse_points(payload)
    vector = parse_vector(payload, len(points))
    bins, bin_gates = parse_bins(payload, slab_lo, slab_hi, exact_count)
    ordinary_coeff = ordinary_coefficients(points, vector)
    weighted_coeff = weighted_coefficients(points, vector, slab_lo, slab_hi)
    ordinary = contract_f(ordinary_coeff, points)
    weighted = contract_f(weighted_coeff, points)

    inside = Interval.exact(Fraction(0))
    bin_details: list[dict[str, Any]] = []
    for identifier, gamma, count, _ in bins:
        polynomial = quadratic_range(gamma, slab_lo, slab_hi)
        if polynomial.hi > 0:
            raise CertificateError(f"zero bin {identifier!r} is not in the nonpositive slab region")
        phi2 = phi_rectangle(points, vector, gamma).modulus2()
        contribution = polynomial.mul(phi2).scale(Fraction(count))
        inside = inside.add(contribution)
        bin_details.append({"id": identifier, "count": count,
                            "gamma": gamma.to_json(),
                            "polynomial_weight": polynomial.to_json(),
                            "phi_modulus_squared": phi2.to_json(),
                            "weighted_contribution": contribution.to_json()})

    residual = weighted.sub(inside)
    status, moat = classify(residual)
    check_claim(payload, "claimed_ordinary_pick", ordinary)
    check_claim(payload, "claimed_weighted_full", weighted)
    check_claim(payload, "claimed_inside_contribution", inside)
    check_claim(payload, "claimed_residual", residual)
    claimed_status = payload.get("claimed_status")
    if claimed_status is not None and claimed_status != status:
        raise CertificateError("claimed_status does not match exact reconstruction")

    used_gates = point_gates | bin_gates | {complete_gate, endpoint_gate, parent_gate}
    result: dict[str, Any] = {
        "schema": VERIFY_SCHEMA,
        "verified": True,
        "status": status,
        "strict_moat": text(moat),
        "ordinary_pick_interval": ordinary.to_json(),
        "weighted_full_interval": weighted.to_json(),
        "inside_contribution_interval": inside.to_json(),
        "slab_complement_residual_interval": residual.to_json(),
        "slab": {"lower": text(slab_lo), "upper": text(slab_hi),
                 "exact_zero_count": exact_count},
        "point_count": len(points),
        "zero_bin_count": len(bins),
        "vector": [value.to_json() for value in vector],
        "ordinary_contracted_coefficients": [value.to_json() for value in ordinary_coeff],
        "weighted_contracted_coefficients": [value.to_json() for value in weighted_coeff],
        "zero_bins": bin_details,
        "manifest": parse_gates(payload, used_gates),
        "interpretation": ("Exact finite slab-complement contraction only. Primitive F rectangles, "
                           "slab completeness, critical-line zero bins, and the parent RH Pick "
                           "implication remain external logical gates."),
    }
    result["verification_sha256"] = canonical_digest(result)
    return result


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = verify(load(args.certificate))
        code = 0
    except CertificateError as exc:
        result = {"schema": VERIFY_SCHEMA, "verified": False,
                  "status": "REJECTED", "reason": str(exc)}
        code = 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
