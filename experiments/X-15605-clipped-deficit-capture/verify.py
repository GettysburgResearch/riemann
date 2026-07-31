#!/usr/bin/env python3
"""Exact verifier for L-15618/L-15620 synthetic clipped-deficit certificates."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "riemann.clipped-deficit-capture.v1"


def frac(value: Any, field: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{field}: booleans are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{field}: invalid rational") from exc
    raise ValueError(f"{field}: expected integer or rational string")


def canonical_digest(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    if certificate.get("schema") != SCHEMA:
        raise ValueError("unsupported schema")

    G = frac(certificate.get("G"), "G")
    alpha = frac(certificate.get("alpha"), "alpha")
    Gamma = frac(certificate.get("Gamma"), "Gamma")
    deficits_raw = certificate.get("deficit_eigenvalues")
    packet_raw = certificate.get("packet_indices")

    if not isinstance(deficits_raw, list) or not deficits_raw:
        raise ValueError("deficit_eigenvalues must be a nonempty list")
    deficits = [frac(v, f"deficit_eigenvalues[{i}]") for i, v in enumerate(deficits_raw)]
    if any(v < 0 for v in deficits):
        raise ValueError("deficit eigenvalues must be nonnegative")

    if not isinstance(packet_raw, list) or not packet_raw:
        raise ValueError("packet_indices must be a nonempty list")
    if any(isinstance(i, bool) or not isinstance(i, int) for i in packet_raw):
        raise ValueError("packet indices must be integers")
    if len(set(packet_raw)) != len(packet_raw):
        raise ValueError("packet indices must be distinct")
    if min(packet_raw) < 0 or max(packet_raw) >= len(deficits):
        raise ValueError("packet index out of range")

    if not (alpha < Gamma <= G):
        raise ValueError("require alpha < Gamma <= G")

    d = len(packet_raw)
    packet = set(packet_raw)
    A_diag = [G - x for x in deficits]

    if any(A_diag[i] > alpha for i in packet):
        raise ValueError("packet is not below alpha")

    theta = G - Gamma
    clipped = [max(x - theta, Fraction(0)) for x in deficits]
    clipped_trace = sum(clipped, Fraction(0))
    packet_clipped = sum((clipped[i] for i in packet), Fraction(0))
    forced_capture = d * (Gamma - alpha)

    # L-15618's Jensen lower bound is replayed directly in this diagonal model.
    if packet_clipped < forced_capture:
        raise ValueError("packet clipped capture is below the forced lower bound")
    if clipped_trace > forced_capture:
        raise ValueError("clipped scalar saturation gate fails")

    complement = [A_diag[i] for i in range(len(A_diag)) if i not in packet]
    if not complement:
        raise ValueError("synthetic certificate needs a nonempty complement")
    exact_complement_floor = min(complement)
    if exact_complement_floor < Gamma:
        raise ValueError("actual complement floor is below Gamma")

    full_trace_excess = sum(deficits, Fraction(0)) - d * (G - alpha)
    full_trace_rhs = G - Gamma

    result: dict[str, Any] = {
        "schema": SCHEMA,
        "G": str(G),
        "alpha": str(alpha),
        "Gamma": str(Gamma),
        "theta": str(theta),
        "dimension": len(deficits),
        "packet_dimension": d,
        "full_trace_excess": str(full_trace_excess),
        "full_trace_rhs": str(full_trace_rhs),
        "full_trace_gate": "PASS" if full_trace_excess <= full_trace_rhs else "FAIL",
        "clipped_trace": str(clipped_trace),
        "packet_clipped_capture": str(packet_clipped),
        "required_packet_capture": str(forced_capture),
        "clipped_gate": "PASS",
        "exact_complement_floor": str(exact_complement_floor),
        "verdict": "PASS",
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        certificate = json.loads(Path(sys.argv[1]).read_text())
        result = verify(certificate)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
