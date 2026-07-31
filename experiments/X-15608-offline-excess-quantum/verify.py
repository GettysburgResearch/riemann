#!/usr/bin/env python3
"""Exact Fraction-only verifier for L-15622."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("booleans are not rational inputs")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"unsupported rational value: {value!r}")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    G = frac(data["G"])
    alpha = frac(data["alpha"])
    t = frac(data["t"])
    Gamma = frac(data["Gamma"])
    D = [frac(x) for x in data["D_diagonal"]]
    packet = list(data["packet_indices"])
    extra = list(data["extra_low_indices"])

    if not (0 <= alpha < t < Gamma <= G):
        raise ValueError("need 0 <= alpha < t < Gamma <= G")
    if any(x < 0 for x in D):
        raise ValueError("D must be positive")
    if len(set(packet + extra)) != len(packet) + len(extra):
        raise ValueError("packet and extra indices must be distinct")
    if any(not isinstance(i, int) or isinstance(i, bool) or i < 0 or i >= len(D) for i in packet + extra):
        raise ValueError("invalid index")

    d = len(packet)
    q = len(extra)
    if d == 0 or q == 0:
        raise ValueError("control requires nonzero packet and extra block")

    A = [G - x for x in D]
    if any(A[i] > alpha for i in packet):
        raise ValueError("packet is not below alpha")
    if any(A[i] >= t for i in packet + extra):
        raise ValueError("combined packet is not strictly below t")

    theta = G - Gamma
    eta = Gamma - t
    c = Gamma - alpha
    clipped = [max(x - theta, Fraction(0)) for x in D]
    clipped_trace = sum(clipped, Fraction(0))
    packet_requirement = d * c
    excess = clipped_trace - packet_requirement
    required_quantum = q * eta

    if excess <= required_quantum:
        raise ValueError("claimed extra-low block does not force the strict excess quantum")

    proof_payload = {
        "schema": "riemann.offline-excess-quantum.v1",
        "G": fstr(G),
        "alpha": fstr(alpha),
        "t": fstr(t),
        "Gamma": fstr(Gamma),
        "theta": fstr(theta),
        "eta": fstr(eta),
        "packet_dimension": d,
        "extra_low_dimension": q,
        "A_diagonal": [fstr(x) for x in A],
        "D_diagonal": [fstr(x) for x in D],
        "clipped_diagonal": [fstr(x) for x in clipped],
        "clipped_trace": fstr(clipped_trace),
        "packet_requirement": fstr(packet_requirement),
        "clipped_excess": fstr(excess),
        "required_quantum": fstr(required_quantum),
        "verdict": "PASS",
    }
    canonical = json.dumps(proof_payload, sort_keys=True, separators=(",", ":")).encode()
    proof_payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return proof_payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(json.loads(args.certificate.read_text()))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
