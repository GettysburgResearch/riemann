#!/usr/bin/env python3
"""Exact checker for total-zero-count-deflated direct-xi modulus witnesses.

The checker uses only integers and fractions after JSON parsing. Under RH, an
unconditional lower count of *total* zeta zeros in a symmetric ordinate window
is also a lower count of critical-line zeros in that window. Nested total-count
windows therefore yield the order-statistic deflation from L-9302 without
isolating individual Hardy-Z zeros.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import string
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SCHEMA = "riemann.xi-modulus-total-count-deflation.v1"
NORMALIZATION = "riemann-xi-standard-half-s-sminus1-v1"
PRODUCTION_GATE = "CERTIFIED_TOTAL_ZETA_ZERO_LOWER_BOUND"
SYNTHETIC_GATE = "SYNTHETIC_TOTAL_ZERO_COUNT"
PRIMITIVE_SCHEMA = "riemann.xi-modulus-primitives.v1"
COUNT_SCHEMA = "riemann.x9302-pr71-total-count-windows.v1"
COUNT_CLASSIFICATION = "CERTIFIED_NESTED_TOTAL_ZETA_ZERO_COUNTS"


class CertificateError(ValueError):
    pass


@dataclass(frozen=True)
class Interval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise CertificateError("interval lower endpoint exceeds upper endpoint")

    def add(self, other: "Interval") -> "Interval":
        return Interval(self.lower + other.lower, self.upper + other.upper)

    def sub(self, other: "Interval") -> "Interval":
        return Interval(self.lower - other.upper, self.upper - other.lower)

    def scale(self, scalar: Fraction) -> "Interval":
        a, b = self.lower * scalar, self.upper * scalar
        return Interval(min(a, b), max(a, b))

    def mul(self, other: "Interval") -> "Interval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return Interval(min(values), max(values))


def exact_int(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise CertificateError(f"{name} must be an integer")
    return value


def rational(raw: Any, name: str) -> Fraction:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    numerator = exact_int(raw.get("numerator"), f"{name}.numerator")
    denominator = exact_int(raw.get("denominator"), f"{name}.denominator")
    if denominator <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(numerator, denominator)


def interval(raw: Any, name: str) -> Interval:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Interval(
        rational(raw.get("lower"), f"{name}.lower"),
        rational(raw.get("upper"), f"{name}.upper"),
    )


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def ij(value: Interval) -> dict[str, dict[str, int]]:
    return {"lower": fj(value.lower), "upper": fj(value.upper)}


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def validate_sha256(value: Any, name: str) -> str:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(ch not in string.hexdigits for ch in value)
    ):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def square_interval(value: Interval) -> Interval:
    upper = max(value.lower * value.lower, value.upper * value.upper)
    lower = Fraction(0) if value.lower <= 0 <= value.upper else min(
        value.lower * value.lower, value.upper * value.upper
    )
    return Interval(lower, upper)


def modulus_squared(real: Interval, imag: Interval) -> Interval:
    return square_interval(real).add(square_interval(imag))


def _atanh_log_interval(y: Fraction, terms: int) -> Interval:
    if not (Fraction(1) <= y <= Fraction(2)):
        raise CertificateError("internal logarithm range-reduction failure")
    if terms < 8:
        raise CertificateError("logarithm term count must be at least 8")
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return Interval(lower, lower + tail)


def log_positive_fraction(value: Fraction, terms: int) -> Interval:
    if value <= 0:
        raise CertificateError("logarithm input must be positive")
    numerator, denominator = value.numerator, value.denominator
    exponent = numerator.bit_length() - denominator.bit_length()

    def power_of_two(k: int) -> Fraction:
        return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))

    reduced = value / power_of_two(exponent)
    while reduced < 1:
        exponent -= 1
        reduced *= 2
    while reduced >= 2:
        exponent += 1
        reduced /= 2
    return _atanh_log_interval(reduced, terms).add(
        _atanh_log_interval(Fraction(2), terms).scale(Fraction(exponent))
    )


def log_positive_interval(value: Interval, terms: int) -> Interval:
    if value.lower <= 0:
        raise CertificateError("modulus-square interval must have positive lower endpoint")
    return Interval(
        log_positive_fraction(value.lower, terms).lower,
        log_positive_fraction(value.upper, terms).upper,
    )


def determinant_interval(matrix: list[list[Interval]]) -> Interval:
    size = len(matrix)
    if size < 1 or any(len(row) != size for row in matrix):
        raise CertificateError("determinant matrix must be nonempty and square")
    result = Interval(Fraction(0), Fraction(0))
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            1
            for i in range(size)
            for j in range(i + 1, size)
            if permutation[i] > permutation[j]
        )
        term = Interval(Fraction(1), Fraction(1))
        for row, column in enumerate(permutation):
            term = term.mul(matrix[row][column])
        result = result.add(term.scale(Fraction(-1 if inversions % 2 else 1)))
    return result


def row_status(value: Interval) -> str:
    if value.upper < 0:
        return "CERTIFIED_NEGATIVE"
    if value.lower >= 0:
        return "CERTIFIED_NONNEGATIVE"
    return "UNRESOLVED"


def parse_points(
    data: dict[str, Any], *, require_digests: bool
) -> dict[str, dict[str, Any]]:
    raw_points = data.get("points")
    if not isinstance(raw_points, list) or not raw_points:
        raise CertificateError("points must be a nonempty list")
    points: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(raw_points):
        if not isinstance(raw, dict):
            raise CertificateError(f"points[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in points:
            raise CertificateError(f"invalid or duplicate point id at points[{index}]")
        u = rational(raw.get("u"), f"points[{index}].u")
        if u <= 0:
            raise CertificateError("all squared horizontal nodes must be positive")
        rectangle = raw.get("xi_rectangle")
        if not isinstance(rectangle, dict):
            raise CertificateError(f"points[{index}].xi_rectangle must be an object")
        real = interval(rectangle.get("real"), f"points[{index}].xi_rectangle.real")
        imag = interval(rectangle.get("imag"), f"points[{index}].xi_rectangle.imag")
        canonical = {
            "id": identifier,
            "u": fj(u),
            "xi_rectangle": {"real": ij(real), "imag": ij(imag)},
        }
        digest = canonical_sha(canonical)
        declared = raw.get("point_sha256")
        if require_digests and declared is None:
            raise CertificateError(
                f"production point {identifier} must carry point_sha256"
            )
        if declared is not None and validate_sha256(declared, "point_sha256") != digest:
            raise CertificateError(f"point digest mismatch for {identifier}")
        points[identifier] = {
            "u": u,
            "h": modulus_squared(real, imag),
            "sha256": digest,
        }
    return points


def validate_production_source(data: dict[str, Any]) -> dict[str, str]:
    source = data.get("source")
    if not isinstance(source, dict):
        raise CertificateError("production certificate must bind source artifacts")
    if source.get("primitive_schema") != PRIMITIVE_SCHEMA:
        raise CertificateError("production primitive source schema mismatch")
    if source.get("total_count_schema") != COUNT_SCHEMA:
        raise CertificateError("production total-count source schema mismatch")
    if source.get("total_count_classification") != COUNT_CLASSIFICATION:
        raise CertificateError("production total-count source classification mismatch")
    return {
        "primitive_sha256": validate_sha256(
            source.get("primitive_sha256"), "source.primitive_sha256"
        ),
        "total_count_sha256": validate_sha256(
            source.get("total_count_sha256"), "source.total_count_sha256"
        ),
    }


def verify_source_artifacts(
    data: dict[str, Any],
    primitive_artifact: dict[str, Any],
    count_artifact: dict[str, Any],
) -> dict[str, str]:
    """Bind a production arithmetic replay to the two producer artifacts."""
    source = validate_production_source(data)
    if primitive_artifact.get("schema") != PRIMITIVE_SCHEMA:
        raise CertificateError("primitive artifact schema mismatch")
    if primitive_artifact.get("normalization_id") != NORMALIZATION:
        raise CertificateError("primitive artifact normalization mismatch")
    if count_artifact.get("schema") != COUNT_SCHEMA:
        raise CertificateError("total-count artifact schema mismatch")
    if count_artifact.get("classification") != COUNT_CLASSIFICATION:
        raise CertificateError("total-count artifact classification mismatch")
    primitive_sha = canonical_sha(primitive_artifact)
    count_sha = canonical_sha(count_artifact)
    if primitive_sha != source["primitive_sha256"]:
        raise CertificateError("primitive artifact digest does not match certificate")
    if count_sha != source["total_count_sha256"]:
        raise CertificateError("total-count artifact digest does not match certificate")
    return {
        "primitive_sha256": primitive_sha,
        "total_count_sha256": count_sha,
    }


def parse_count_windows(
    data: dict[str, Any], classification: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    raw_windows = data.get("count_windows")
    if not isinstance(raw_windows, list) or not raw_windows:
        raise CertificateError("count_windows must be a nonempty list")
    expected_gate = SYNTHETIC_GATE if classification == "SYNTHETIC_MODEL" else PRODUCTION_GATE
    windows: list[dict[str, Any]] = []
    ids: set[str] = set()
    previous_radius = Fraction(0)
    previous_count = 0
    shells: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_windows):
        if not isinstance(raw, dict):
            raise CertificateError(f"count_windows[{index}] must be an object")
        identifier = raw.get("id")
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise CertificateError("count-window IDs must be nonempty and unique")
        ids.add(identifier)
        radius = rational(raw.get("radius"), f"count_windows[{index}].radius")
        if radius <= previous_radius:
            raise CertificateError("count-window radii must be strictly increasing")
        count = exact_int(raw.get("count_lower"), f"count_windows[{index}].count_lower")
        if count < previous_count:
            raise CertificateError("nested total-zero lower counts must be nondecreasing")
        gate = raw.get("gate")
        if not isinstance(gate, dict) or gate.get("status") != expected_gate:
            raise CertificateError(f"count-window gate status must equal {expected_gate!r}")
        gate_sha = validate_sha256(gate.get("sha256"), "count-window gate sha256")
        increment = count - previous_count
        windows.append(
            {
                "id": identifier,
                "radius": radius,
                "count": count,
                "gate_sha256": gate_sha,
            }
        )
        if increment:
            shells.append(
                {
                    "source_window_id": identifier,
                    "count": increment,
                    "B": radius * radius,
                }
            )
        previous_radius = radius
        previous_count = count
    if previous_count <= 0:
        raise CertificateError("the final total-zero lower count must be positive")
    return windows, shells


def raw_log_value(point: dict[str, Any], terms: int) -> Interval:
    return log_positive_interval(point["h"], terms)


def deflated_log_value(
    point: dict[str, Any], shells: list[dict[str, Any]], terms: int
) -> Interval:
    result = raw_log_value(point, terms)
    u = point["u"]
    for shell in shells:
        result = result.sub(
            log_positive_fraction(u + shell["B"], terms).scale(Fraction(shell["count"]))
        )
    return result


def secant(left: dict[str, Any], right: dict[str, Any], lv: Interval, rv: Interval) -> Interval:
    denominator = left["u"] - right["u"]
    if denominator == 0:
        raise CertificateError("secant nodes must be distinct")
    return lv.sub(rv).scale(Fraction(1, 1) / denominator)


def monotonicity_product(
    left: dict[str, Any], right: dict[str, Any], shells: list[dict[str, Any]]
) -> Interval:
    if not left["u"] < right["u"]:
        raise CertificateError("monotonicity nodes must be increasing")
    left_factor = Fraction(1)
    right_factor = Fraction(1)
    for shell in shells:
        left_factor *= (left["u"] + shell["B"]) ** shell["count"]
        right_factor *= (right["u"] + shell["B"]) ** shell["count"]
    return right["h"].scale(left_factor).sub(left["h"].scale(right_factor))


def loewner_determinant(
    row_ids: list[str],
    column_ids: list[str],
    points: dict[str, dict[str, Any]],
    shells: list[dict[str, Any]],
    terms: int,
    deflated: bool,
) -> Interval:
    size = len(row_ids)
    if size < 1 or size != len(column_ids) or size > 4:
        raise CertificateError("Loewner determinant order must be between one and four")
    if len(set(row_ids)) != size or len(set(column_ids)) != size:
        raise CertificateError("Loewner row and column lists must not repeat nodes")
    if set(row_ids) & set(column_ids):
        raise CertificateError("Loewner row and column lists must be disjoint")
    if any(identifier not in points for identifier in row_ids + column_ids):
        raise CertificateError("Loewner row references an unknown point")
    row_nodes = [points[identifier]["u"] for identifier in row_ids]
    column_nodes = [points[identifier]["u"] for identifier in column_ids]
    if any(row_nodes[i] >= row_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner row nodes must be strictly increasing")
    if any(column_nodes[i] >= column_nodes[i + 1] for i in range(size - 1)):
        raise CertificateError("Loewner column nodes must be strictly increasing")
    values = {
        identifier: (
            deflated_log_value(points[identifier], shells, terms)
            if deflated
            else raw_log_value(points[identifier], terms)
        )
        for identifier in row_ids + column_ids
    }
    matrix = [
        [secant(points[r], points[c], values[r], values[c]) for c in column_ids]
        for r in row_ids
    ]
    return determinant_interval(matrix)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must equal {SCHEMA!r}")
    if data.get("normalization_id") != NORMALIZATION:
        raise CertificateError("completed-xi normalization mismatch")
    classification = data.get("classification")
    if classification not in ("SYNTHETIC_MODEL", "RIEMANN_XI_DIRECTED"):
        raise CertificateError("unsupported classification")
    ordinate = rational(data.get("ordinate"), "ordinate")
    terms = exact_int(data.get("log_terms", 256), "log_terms")
    if terms < 32 or terms > 4096:
        raise CertificateError("log_terms must be between 32 and 4096")

    claimed_certificate_sha = data.get("certificate_sha256")
    if classification == "RIEMANN_XI_DIRECTED" and claimed_certificate_sha is None:
        raise CertificateError("production certificate must carry certificate_sha256")
    if claimed_certificate_sha is not None:
        claimed_certificate_sha = validate_sha256(
            claimed_certificate_sha, "certificate_sha256"
        )
        body = dict(data)
        body.pop("certificate_sha256", None)
        if canonical_sha(body) != claimed_certificate_sha:
            raise CertificateError("certificate_sha256 mismatch")

    if classification == "RIEMANN_XI_DIRECTED":
        validate_production_source(data)
    points = parse_points(
        data, require_digests=classification == "RIEMANN_XI_DIRECTED"
    )
    windows, shells = parse_count_windows(data, classification)
    raw_rows = data.get("rows")
    if not isinstance(raw_rows, list) or not raw_rows:
        raise CertificateError("rows must be a nonempty list")

    outputs: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, dict):
            raise CertificateError(f"rows[{index}] must be an object")
        row_id = raw.get("id")
        kind = raw.get("kind")
        if not isinstance(row_id, str) or not row_id or row_id in seen:
            raise CertificateError("row id must be nonempty and unique")
        seen.add(row_id)
        if kind in ("raw-monotonicity", "deflated-monotonicity"):
            left_id, right_id = raw.get("left"), raw.get("right")
            if left_id not in points or right_id not in points:
                raise CertificateError(f"unknown monotonicity point in {row_id}")
            left, right = points[left_id], points[right_id]
            if kind == "raw-monotonicity":
                value = right["h"].sub(left["h"])
            else:
                value = monotonicity_product(left, right, shells)
            detail = {"left": left_id, "right": right_id}
        elif kind in ("raw-cross-loewner-determinant", "deflated-cross-loewner-determinant"):
            row_ids, column_ids = raw.get("rows"), raw.get("columns")
            if not isinstance(row_ids, list) or not isinstance(column_ids, list):
                raise CertificateError("Loewner rows and columns must be arrays")
            value = loewner_determinant(
                row_ids,
                column_ids,
                points,
                shells,
                terms,
                deflated=kind.startswith("deflated"),
            )
            detail = {"rows": row_ids, "columns": column_ids, "order": len(row_ids)}
        else:
            raise CertificateError(f"unsupported row kind {kind!r}")
        outputs.append(
            {
                "id": row_id,
                "kind": kind,
                **detail,
                "interval": ij(value),
                "status": row_status(value),
            }
        )

    negative = [row for row in outputs if row["status"] == "CERTIFIED_NEGATIVE"]
    unresolved = [row for row in outputs if row["status"] == "UNRESOLVED"]
    if classification == "RIEMANN_XI_DIRECTED" and negative:
        verdict = "NEGATIVE_TOTAL_COUNT_DEFLATED_XI_ARITHMETIC_REPLAY"
    elif classification == "SYNTHETIC_MODEL" and negative:
        verdict = "SYNTHETIC_TOTAL_COUNT_DEFLATION_SEPARATION"
    elif unresolved:
        verdict = "UNRESOLVED"
    else:
        verdict = "NO_NEGATIVE_IN_DECLARED_ROWS"

    result = {
        "schema": SCHEMA,
        "verified": True,
        "source_artifacts_verified": False,
        "classification": classification,
        "normalization_id": NORMALIZATION,
        "ordinate": fj(ordinate),
        "point_count": len(points),
        "count_windows": [
            {
                "id": item["id"],
                "radius": fj(item["radius"]),
                "count_lower": item["count"],
                "gate_sha256": item["gate_sha256"],
            }
            for item in windows
        ],
        "deflation_shells": [
            {
                "source_window_id": item["source_window_id"],
                "count_increment": item["count"],
                "distance_square_upper": fj(item["B"]),
            }
            for item in shells
        ],
        "point_fingerprints": {
            identifier: point["sha256"] for identifier, point in sorted(points.items())
        },
        "rows": outputs,
        "certified_negative_rows": len(negative),
        "unresolved_rows": len(unresolved),
        "verdict": verdict,
        "scope_warning": (
            "The checker proves exact rectangle contraction and nested total-count "
            "deflation algebra only. A production CLI replay additionally requires "
            "the primitive and total-count artifacts whose digests are bound by the "
            "certificate. Under RH, unconditional total-zero lower counts become "
            "critical-line lower counts. A negative still requires independent "
            "backend reproduction and analytic review."
        ),
    }
    if claimed_certificate_sha is not None:
        result["certificate_sha256"] = claimed_certificate_sha
    digest_body = dict(result)
    result["verification_sha256"] = canonical_sha(digest_body)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--primitive-artifact", type=Path)
    parser.add_argument("--count-artifact", type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
        if data.get("classification") == "RIEMANN_XI_DIRECTED":
            if args.primitive_artifact is None or args.count_artifact is None:
                raise CertificateError(
                    "production replay requires --primitive-artifact and "
                    "--count-artifact"
                )
            primitive_artifact = json.loads(
                args.primitive_artifact.read_text(encoding="utf-8")
            )
            count_artifact = json.loads(
                args.count_artifact.read_text(encoding="utf-8")
            )
            if not isinstance(primitive_artifact, dict) or not isinstance(
                count_artifact, dict
            ):
                raise CertificateError("source artifacts must contain JSON objects")
            result["source_artifacts"] = verify_source_artifacts(
                data, primitive_artifact, count_artifact
            )
            result["source_artifacts_verified"] = True
            if result["certified_negative_rows"]:
                result["verdict"] = (
                    "NEGATIVE_TOTAL_COUNT_DEFLATED_XI_WITNESS_PENDING_REVIEW"
                )
            result.pop("verification_sha256", None)
            result["verification_sha256"] = canonical_sha(result)
        code = 1 if result["unresolved_rows"] else 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        result = {"schema": SCHEMA, "verified": False, "error": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
