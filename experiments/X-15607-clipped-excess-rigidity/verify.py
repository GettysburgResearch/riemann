#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(value: Any, field: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{field}: booleans are not valid rationals")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"{field}: invalid rational {value!r}") from exc
    raise ValueError(f"{field}: expected integer or rational string")


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    schema = data.get("schema")
    if schema != "riemann.clipped-excess-rigidity.v1":
        raise ValueError("unsupported schema")

    G = parse_fraction(data["G"], "G")
    alpha = parse_fraction(data["alpha"], "alpha")
    theta = parse_fraction(data["theta"], "theta")
    eta = parse_fraction(data["eta"], "eta")
    D = [parse_fraction(x, f"D[{i}]") for i, x in enumerate(data["D"])]
    A = [parse_fraction(x, f"A[{i}]") for i, x in enumerate(data["A"])]
    packet = data["packet_indices"]

    if not isinstance(packet, list) or not packet:
        raise ValueError("packet_indices must be a nonempty list")
    if any(isinstance(i, bool) or not isinstance(i, int) for i in packet):
        raise ValueError("packet indices must be integers")
    if len(set(packet)) != len(packet):
        raise ValueError("duplicate packet index")
    if len(D) != len(A):
        raise ValueError("D/A dimension mismatch")
    if any(i < 0 or i >= len(D) for i in packet):
        raise ValueError("packet index out of range")
    if eta <= 0:
        raise ValueError("eta must be positive")

    kappa = G - alpha
    if not (theta < kappa):
        raise ValueError("theta must be below kappa=G-alpha")
    Gamma = G - theta
    c = kappa - theta

    for i, (a_i, d_i) in enumerate(zip(A, D)):
        if d_i < 0:
            raise ValueError(f"D[{i}] must be nonnegative")
        if a_i < G - d_i:
            raise ValueError(f"lower-symbol inequality fails at {i}")
    for i in packet:
        if A[i] > alpha:
            raise ValueError(f"packet is not low at index {i}")

    clipped = [max(x - theta, Fraction(0)) for x in D]
    total_clipped = sum(clipped, Fraction(0))
    baseline = len(packet) * c
    excess = total_clipped - baseline
    if excess < 0:
        raise ValueError("negative clipped excess contradicts the hypotheses")

    packet_set = set(packet)
    q_clipped = sum(
        (clipped[i] for i in range(len(D)) if i not in packet_set),
        Fraction(0),
    )
    compression_slack = sum((alpha - A[i] for i in packet), Fraction(0))
    majorant_slack = sum((A[i] + D[i] - G for i in packet), Fraction(0))
    below_clip_leakage = sum(
        (max(theta - D[i], Fraction(0)) for i in packet), Fraction(0)
    )
    decomposition = (
        q_clipped + compression_slack + majorant_slack + below_clip_leakage
    )

    if decomposition != excess:
        raise ValueError("positive-defect decomposition identity failed")
    if any(
        x < 0
        for x in (
            q_clipped,
            compression_slack,
            majorant_slack,
            below_clip_leakage,
        )
    ):
        raise ValueError("a supposedly positive defect is negative")

    threshold = theta + eta
    count = sum(1 for x in D if x > threshold)
    count_excess = max(0, count - len(packet))
    if Fraction(count_excess) * eta > excess:
        raise ValueError("one-mode exclusion inequality failed")

    complement = [i for i in range(len(D)) if i not in packet_set]
    if not complement:
        raise ValueError("synthetic control needs a nonempty complement")
    certified_floor = Gamma - excess
    actual_complement_floor = min(A[i] for i in complement)
    if actual_complement_floor < certified_floor:
        raise ValueError("certified complement floor exceeds actual diagonal floor")

    zero_excess = excess == 0
    flat_band = all(
        clipped[i] == (c if i in packet_set else 0)
        for i in range(len(D))
    )
    if zero_excess != flat_band:
        raise ValueError("zero-excess/flat-band equivalence failed")

    proof_payload = {
        "schema": schema,
        "G": fstr(G),
        "alpha": fstr(alpha),
        "theta": fstr(theta),
        "eta": fstr(eta),
        "D": [fstr(x) for x in D],
        "A": [fstr(x) for x in A],
        "packet_indices": packet,
        "excess": fstr(excess),
        "decomposition": {
            "uncaptured_clipped_trace": fstr(q_clipped),
            "compression_slack": fstr(compression_slack),
            "lower_symbol_slack": fstr(majorant_slack),
            "below_clip_packet_leakage": fstr(below_clip_leakage),
        },
        "count_above_theta_plus_eta": count,
        "certified_complement_floor": fstr(certified_floor),
        "actual_complement_floor": fstr(actual_complement_floor),
        "zero_excess": zero_excess,
        "flat_band": flat_band,
    }
    encoded = json.dumps(
        proof_payload, sort_keys=True, separators=(",", ":")
    ).encode()
    digest = hashlib.sha256(encoded).hexdigest()

    return {
        **proof_payload,
        "proof_object_sha256": digest,
        "verdict": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    data = json.loads(args.certificate.read_text())
    result = verify(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
