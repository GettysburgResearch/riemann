#!/usr/bin/env python3
"""Exact Gaussian-rational controls for L-8303 coherent corner packets."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x8301_core", ROOT / "verify.py")
CORE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = CORE
SPEC.loader.exec_module(CORE)

SCHEMA = "riemann.endpoint-green-packet.synthetic.v1"
CertificateError = CORE.CertificateError
GQ = CORE.GQ


def z_at(a0: GQ, a1: GQ, x: Fraction) -> GQ:
    return a0 - a1 * x


def secular(g: dict[str, Any], z: GQ) -> Fraction:
    r = (z.conj() * g["b"]).re
    return 1 - 2 * r - g["D"] * z.abs2()


def pressure_bounds(g: dict[str, Any], z: GQ) -> tuple[Fraction, Fraction]:
    r = (z.conj() * g["b"]).re
    rad = r * r + g["D"] * z.abs2()
    lo, hi = CORE.sqrt_bounds(rad, 160)
    return r + lo, r + hi


def verify_case(case: dict[str, Any]) -> dict[str, Any]:
    case_id = case.get("id")
    if not isinstance(case_id, str) or not case_id:
        raise CertificateError("packet case id must be nonempty")
    h = CORE.parse_matrix(case.get("H"), f"{case_id}.H")
    if not CORE.is_hermitian(h) or not CORE.psd_ldl(h, strict=True):
        raise CertificateError(f"{case_id}: H must be positive-definite Hermitian")
    endpoints = case.get("endpoints")
    if not isinstance(endpoints, list) or len(endpoints) != 2:
        raise CertificateError(f"{case_id}: endpoints must have length two")
    left, right = endpoints
    if any(isinstance(i, bool) or not isinstance(i, int) for i in endpoints):
        raise CertificateError(f"{case_id}: endpoints must be integers")
    phase = GQ(1)
    g = CORE.endpoint_green(h, left, right, phase)
    a0 = CORE.parse_gq(case.get("A0"), f"{case_id}.A0")
    a1 = CORE.parse_gq(case.get("A1"), f"{case_id}.A1")
    xs = case.get("x_interval")
    if not isinstance(xs, list) or len(xs) != 2:
        raise CertificateError(f"{case_id}: x_interval must have length two")
    x0 = CORE.parse_fraction(xs[0], f"{case_id}.x_interval[0]")
    x1 = CORE.parse_fraction(xs[1], f"{case_id}.x_interval[1]")
    if x0 > x1:
        raise CertificateError(f"{case_id}: x interval is reversed")

    z0, z1 = z_at(a0, a1, x0), z_at(a0, a1, x1)
    f0, f1 = secular(g, z0), secular(g, z1)
    p0, p0u = pressure_bounds(g, z0)
    p1, p1u = pressure_bounds(g, z1)
    pmax_lo, pmax_hi = max(p0, p1), max(p0u, p1u)

    if f0 < 0 or f1 < 0:
        status = "PACKET_CROSSING_AT_ENDPOINT"
    elif f0 > 0 and f1 > 0:
        status = "PACKET_POSITIVE_ON_MESH_CELL"
    else:
        status = "PACKET_UNRESOLVED_BOUNDARY"
    if case.get("expected_status") != status:
        raise CertificateError(
            f"{case_id}: expected {case.get('expected_status')!r}, reconstructed {status!r}"
        )

    components = case.get("components", [])
    if not isinstance(components, list):
        raise CertificateError(f"{case_id}: components must be an array")
    component_secants: list[Fraction] = []
    component_sum = GQ()
    for index, value in enumerate(components):
        zj = CORE.parse_gq(value, f"{case_id}.components[{index}]")
        component_sum += zj
        component_secants.append(secular(g, zj))
    if components and a1.is_zero() and component_sum != a0:
        raise CertificateError(f"{case_id}: constant packet components do not sum to A0")

    mid = (x0 + x1) / 2
    fmid = secular(g, z_at(a0, a1, mid))
    if fmid < min(f0, f1):
        raise AssertionError(f"{case_id}: concavity endpoint principle failed")

    claimed = case.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError(f"{case_id}: claimed must be an object")
    expected_f0 = CORE.parse_fraction(claimed.get("f_left"), f"{case_id}.claimed.f_left")
    expected_f1 = CORE.parse_fraction(claimed.get("f_right"), f"{case_id}.claimed.f_right")
    if (f0, f1) != (expected_f0, expected_f1):
        raise CertificateError(f"{case_id}: secular endpoint mismatch")

    return {
        "id": case_id,
        "status": status,
        "Z_left": z0.to_json(),
        "Z_right": z1.to_json(),
        "secular_left": CORE.fraction_json(f0),
        "secular_right": CORE.fraction_json(f1),
        "secular_midpoint": CORE.fraction_json(fmid),
        "pressure_endpoint_hull": {
            "lower_of_max": CORE.fraction_json(pmax_lo),
            "upper_of_max": CORE.fraction_json(pmax_hi),
        },
        "component_secular_values": [CORE.fraction_json(x) for x in component_secants],
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise CertificateError("packet cases must be a nonempty array")
    ids: set[str] = set()
    output = []
    for case in cases:
        if not isinstance(case, dict):
            raise CertificateError("each packet case must be an object")
        if case.get("id") in ids:
            raise CertificateError("duplicate packet case id")
        ids.add(case.get("id"))
        output.append(verify_case(case))
    return {
        "schema": SCHEMA,
        "status": "EXACT_COHERENT_PACKET_CERTIFICATES_RECONSTRUCTED",
        "cases": output,
        "proof_boundary": "finite synthetic corner packets only; no prime-power production sign",
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read packet certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("packet certificate root must be an object")
    return value


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        out = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(json.dumps({"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
