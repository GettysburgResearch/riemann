#!/usr/bin/env python3
"""Exact rational checker for certified critical-line-zero deflation.

The checker proves only finite algebraic consequences of supplied primitive
F=xi'/xi rectangles and certified lower zero counts. It does not certify the
zero counts, evaluate special functions, or prove the parent RH implication.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.zero-deflation.v1"
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
        a = q(value[0], name + "[0]")
        b = q(value[1], name + "[1]")
        if a.denominator != 1 or b.denominator != 1 or b == 0:
            raise CertificateError(f"{name}: [p,q] must contain integers with q!=0")
        return Fraction(a.numerator, b.numerator)
    raise CertificateError(f"{name}: rational required")


def integer(value: Any, name: str) -> int:
    x = q(value, name)
    if x.denominator != 1:
        raise CertificateError(f"{name}: integer required")
    return x.numerator


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    @classmethod
    def parse(cls, raw: Any, name: str) -> "Interval":
        if not isinstance(raw, dict) or set(raw) != {"lower", "upper"}:
            raise CertificateError(f"{name}: expected lower/upper object")
        out = cls(q(raw["lower"], name + ".lower"), q(raw["upper"], name + ".upper"))
        if out.lo > out.hi:
            raise CertificateError(f"{name}: reversed interval")
        return out

    @classmethod
    def exact(cls, value: Fraction) -> "Interval":
        return cls(value, value)

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def scale(self, a: Fraction) -> "Interval":
        if a >= 0:
            return Interval(a * self.lo, a * self.hi)
        return Interval(a * self.hi, a * self.lo)

    def mul(self, other: "Interval") -> "Interval":
        values = (self.lo * other.lo, self.lo * other.hi, self.hi * other.lo, self.hi * other.hi)
        return Interval(min(values), max(values))

    def subtract_exact(self, value: Fraction) -> "Interval":
        return Interval(self.lo - value, self.hi - value)

    def distance_to_zero(self) -> Fraction:
        if self.lo <= 0 <= self.hi:
            return Fraction(0)
        return min(abs(self.lo), abs(self.hi))

    def to_json(self) -> dict[str, str]:
        return {"lower": text(self.lo), "upper": text(self.hi)}


@dataclass(frozen=True)
class CInterval:
    re: Interval
    im: Interval

    @classmethod
    def exact(cls, z: "QComplex") -> "CInterval":
        return cls(Interval.exact(z.re), Interval.exact(z.im))

    def add(self, other: "CInterval") -> "CInterval":
        return CInterval(self.re.add(other.re), self.im.add(other.im))

    def mul_exact(self, z: "QComplex") -> "CInterval":
        return CInterval(
            self.re.scale(z.re).add(self.im.scale(-z.im)),
            self.re.scale(z.im).add(self.im.scale(z.re)),
        )

    def modulus2_lower(self) -> Fraction:
        a = self.re.distance_to_zero()
        b = self.im.distance_to_zero()
        return a * a + b * b


@dataclass(frozen=True)
class QComplex:
    re: Fraction
    im: Fraction

    @classmethod
    def parse(cls, raw: Any, name: str) -> "QComplex":
        if not isinstance(raw, dict) or set(raw) != {"re", "im"}:
            raise CertificateError(f"{name}: expected re/im object")
        return cls(q(raw["re"], name + ".re"), q(raw["im"], name + ".im"))

    def add(self, other: "QComplex") -> "QComplex":
        return QComplex(self.re + other.re, self.im + other.im)

    def mul(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conj(self) -> "QComplex":
        return QComplex(self.re, -self.im)

    def div(self, other: "QComplex") -> "QComplex":
        d = other.re * other.re + other.im * other.im
        if d == 0:
            raise CertificateError("complex division by zero")
        return QComplex(
            (self.re * other.re + self.im * other.im) / d,
            (self.im * other.re - self.re * other.im) / d,
        )


ZERO = QComplex(Fraction(0), Fraction(0))


def parse_gates(payload: dict[str, Any], used: set[str]) -> dict[str, Any]:
    raw = payload.get("logical_gates")
    if not isinstance(raw, list):
        raise CertificateError("logical_gates must be a list")
    found: set[str] = set()
    states: list[str] = []
    for i, gate in enumerate(raw):
        if not isinstance(gate, dict):
            raise CertificateError(f"logical_gates[{i}] must be an object")
        gid, state, evidence = gate.get("id"), gate.get("state"), gate.get("evidence")
        if not isinstance(gid, str) or not gid or gid in found:
            raise CertificateError("invalid or duplicate logical gate id")
        if state not in GOOD_GATES:
            raise CertificateError(f"logical gate {gid!r} remains blocking")
        if not isinstance(evidence, str) or not evidence:
            raise CertificateError(f"logical gate {gid!r} lacks evidence")
        found.add(gid)
        states.append(state)
    if found != used:
        raise CertificateError(
            f"logical gate manifest mismatch: declared={sorted(found)}, used={sorted(used)}"
        )
    return {
        "logical_gate_count": len(states),
        "logical_manifest_closed": all(s != "SYNTHETIC_CONTROL" for s in states),
        "synthetic_gate_count": states.count("SYNTHETIC_CONTROL"),
    }


def parse_bins(payload: dict[str, Any]) -> tuple[list[tuple[str, Fraction, Fraction, int, str]], set[str]]:
    raw = payload.get("zero_bins")
    if not isinstance(raw, list) or not raw:
        raise CertificateError("zero_bins must be a nonempty list")
    bins: list[tuple[str, Fraction, Fraction, int, str]] = []
    ids: set[str] = set()
    gates: set[str] = set()
    for i, item in enumerate(raw):
        if not isinstance(item, dict):
            raise CertificateError(f"zero_bins[{i}] must be an object")
        bid, gid = item.get("id"), item.get("gate_id")
        if not isinstance(bid, str) or not bid or bid in ids:
            raise CertificateError("invalid or duplicate zero-bin id")
        if not isinstance(gid, str) or not gid:
            raise CertificateError(f"zero bin {bid!r} lacks gate_id")
        lo = q(item.get("lower"), f"zero_bins[{i}].lower")
        hi = q(item.get("upper"), f"zero_bins[{i}].upper")
        count = integer(item.get("count"), f"zero_bins[{i}].count")
        if lo > hi:
            raise CertificateError(f"zero bin {bid!r} is reversed")
        if count <= 0:
            raise CertificateError(f"zero bin {bid!r} count must be positive")
        ids.add(bid)
        gates.add(gid)
        bins.append((bid, lo, hi, count, gid))
    bins.sort(key=lambda row: (row[1], row[2], row[0]))
    for left, right in zip(bins, bins[1:]):
        if left[2] >= right[1]:
            raise CertificateError("zero bins must be strictly disjoint to prevent double counting")
    return bins, gates


def classify(interval: Interval) -> tuple[str, Fraction]:
    if interval.hi < 0:
        return "CERTIFIED_NEGATIVE_DEFLATED_WITNESS", -interval.hi
    if interval.lo >= 0:
        return "CERTIFIED_NONNEGATIVE_CONTROL", Fraction(0)
    return "UNRESOLVED_ZERO_TOUCH", Fraction(0)


def check_claim(payload: dict[str, Any], interval: Interval) -> None:
    raw = payload.get("claimed_interval")
    if raw is not None and Interval.parse(raw, "claimed_interval") != interval:
        raise CertificateError("claimed_interval does not match exact reconstruction")
    status = payload.get("claimed_status")
    actual, _ = classify(interval)
    if status is not None and status != actual:
        raise CertificateError("claimed_status does not match exact reconstruction")


def scalar(payload: dict[str, Any]) -> dict[str, Any]:
    x = q(payload.get("x"), "x")
    t = q(payload.get("t"), "t")
    if x <= 0:
        raise CertificateError("x must be positive")
    f = Interval.parse(payload.get("f_real"), "f_real")
    bins, gates = parse_bins(payload)
    total = Fraction(0)
    details = []
    for bid, lo, hi, count, _ in bins:
        d = max(abs(t - lo), abs(t - hi))
        lower = x / (x * x + d * d)
        contribution = count * lower
        total += contribution
        details.append(
            {
                "id": bid,
                "count": count,
                "distance_upper": text(d),
                "per_zero_lower": text(lower),
                "subtracted_lower": text(contribution),
            }
        )
    residual = f.subtract_exact(total)
    check_claim(payload, residual)
    status, moat = classify(residual)
    parent = payload.get("parent_gate_id")
    manifest = parse_gates(payload, gates | {parent})
    return {
        "schema": SCHEMA,
        "kind": "scalar-count-deflation",
        "status": status,
        "residual_interval": residual.to_json(),
        "strict_moat": text(moat),
        "subtracted_lower": text(total),
        "zero_bins": details,
        "manifest": manifest,
        "interpretation": (
            "Exact finite deflation algebra only; zero-count and xi-log-derivative "
            "soundness are external logical gates."
        ),
    }


def reciprocal_rectangle(x: Fraction, y: Interval) -> CInterval:
    if x <= 0:
        raise CertificateError("sample point must have x>0")
    if y.lo <= 0 <= y.hi:
        y2_min = Fraction(0)
    else:
        y2_min = min(y.lo * y.lo, y.hi * y.hi)
    y2_max = max(y.lo * y.lo, y.hi * y.hi)
    denom = Interval(x * x + y2_min, x * x + y2_max)
    inv = Interval(1 / denom.hi, 1 / denom.lo)
    real = inv.scale(x)
    imag = Interval(-y.hi, -y.lo).mul(inv)
    return CInterval(real, imag)


def rayleigh_interval(
    points: list[dict[str, Any]], vector: list[QComplex]
) -> tuple[Interval, list[QComplex]]:
    zs: list[QComplex] = []
    fre: list[Interval] = []
    fim: list[Interval] = []
    ids: set[str] = set()
    for i, point in enumerate(points):
        if not isinstance(point, dict):
            raise CertificateError(f"points[{i}] must be an object")
        identifier = point.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise CertificateError("invalid or duplicate point id")
        ids.add(identifier)
        x = q(point.get("x"), f"points[{i}].x")
        t = q(point.get("t"), f"points[{i}].t")
        if x <= 0:
            raise CertificateError(f"points[{i}].x must be positive")
        zs.append(QComplex(x, t))
        fraw = point.get("f")
        if not isinstance(fraw, dict) or set(fraw) != {"real", "imag"}:
            raise CertificateError(f"points[{i}].f must contain real/imag intervals")
        fre.append(Interval.parse(fraw["real"], f"points[{i}].f.real"))
        fim.append(Interval.parse(fraw["imag"], f"points[{i}].f.imag"))
    coeffs: list[QComplex] = []
    total = Interval.exact(Fraction(0))
    for i, (zi, vi) in enumerate(zip(zs, vector)):
        inner = ZERO
        for zj, vj in zip(zs, vector):
            denom = QComplex(zi.re + zj.re, zi.im - zj.im)
            inner = inner.add(vj.div(denom))
        c = vi.conj().mul(inner)
        c = QComplex(2 * c.re, 2 * c.im)
        coeffs.append(c)
        total = total.add(fre[i].scale(c.re)).add(fim[i].scale(-c.im))
    return total, coeffs


def phi_rectangle(
    points: list[dict[str, Any]],
    vector: list[QComplex],
    lo: Fraction,
    hi: Fraction,
) -> CInterval:
    total = CInterval.exact(ZERO)
    for i, (point, v) in enumerate(zip(points, vector)):
        x = q(point.get("x"), f"points[{i}].x")
        t = q(point.get("t"), f"points[{i}].t")
        y = Interval(t - hi, t - lo)
        term = reciprocal_rectangle(x, y).mul_exact(v.conj())
        total = total.add(term)
    return total


def pick(payload: dict[str, Any]) -> dict[str, Any]:
    points = payload.get("points")
    vector_raw = payload.get("vector")
    if not isinstance(points, list) or not points:
        raise CertificateError("points must be a nonempty list")
    if not isinstance(vector_raw, list) or len(vector_raw) != len(points):
        raise CertificateError("vector must match points")
    vector = [QComplex.parse(raw, f"vector[{i}]") for i, raw in enumerate(vector_raw)]
    if all(v.re == 0 and v.im == 0 for v in vector):
        raise CertificateError("vector must be nonzero")
    base, coeffs = rayleigh_interval(points, vector)
    bins, gates = parse_bins(payload)
    total = Fraction(0)
    details = []
    for bid, lo, hi, count, _ in bins:
        enclosure = phi_rectangle(points, vector, lo, hi)
        lower = enclosure.modulus2_lower()
        contribution = count * lower
        total += contribution
        details.append(
            {
                "id": bid,
                "count": count,
                "phi_rectangle": {
                    "real": enclosure.re.to_json(),
                    "imag": enclosure.im.to_json(),
                },
                "per_zero_modulus2_lower": text(lower),
                "subtracted_lower": text(contribution),
            }
        )
    residual = base.subtract_exact(total)
    check_claim(payload, residual)
    status, moat = classify(residual)
    parent = payload.get("parent_gate_id")
    manifest = parse_gates(payload, gates | {parent})
    return {
        "schema": SCHEMA,
        "kind": "pick-count-deflation",
        "status": status,
        "base_rayleigh_interval": base.to_json(),
        "residual_interval": residual.to_json(),
        "strict_moat": text(moat),
        "subtracted_lower": text(total),
        "contracted_coefficients": [
            {"re": text(c.re), "im": text(c.im)} for c in coeffs
        ],
        "zero_bins": details,
        "manifest": manifest,
        "interpretation": (
            "Exact fixed-vector contraction and zero-bin lower bounds only; "
            "primitive F rectangles and zero counts require independent proof."
        ),
    }


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("wrong schema")
    kind = payload.get("kind")
    parent = payload.get("parent_gate_id")
    if not isinstance(parent, str) or not parent:
        raise CertificateError("parent_gate_id is required")
    if kind == "scalar-count-deflation":
        return scalar(payload)
    if kind == "pick-count-deflation":
        return pick(payload)
    raise CertificateError("unsupported certificate kind")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(raw)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}
        code = 2
    out = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(out, encoding="utf-8")
    else:
        print(out, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
