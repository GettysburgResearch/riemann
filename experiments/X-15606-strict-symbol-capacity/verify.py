#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def frac(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("booleans are not rational values")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise ValueError(f"unsupported rational value: {x!r}")


def matrix(raw: Any) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("matrix must be a nonempty list")
    out = [[frac(v) for v in row] for row in raw]
    n = len(out)
    if any(len(row) != n for row in out):
        raise ValueError("matrix must be square")
    if any(out[i][j] != out[j][i] for i in range(n) for j in range(n)):
        raise ValueError("matrix must be symmetric")
    return out


def diag_shift(a: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [
        [a[i][j] + (c if i == j else 0) for j in range(len(a))]
        for i in range(len(a))
    ]


def principal(a: list[list[Fraction]], idx: list[int]) -> list[list[Fraction]]:
    return [[a[i][j] for j in idx] for i in idx]


def ldl_pivots(a: list[list[Fraction]]) -> list[Fraction]:
    n = len(a)
    lower = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    pivots: list[Fraction] = []
    for i in range(n):
        lower[i][i] = Fraction(1)
        pivot = a[i][i] - sum(
            lower[i][k] * lower[i][k] * pivots[k] for k in range(i)
        )
        pivots.append(pivot)
        if pivot == 0:
            for j in range(i + 1, n):
                residual = a[j][i] - sum(
                    lower[j][k] * lower[i][k] * pivots[k]
                    for k in range(i)
                )
                if residual != 0:
                    raise ValueError("zero LDL pivot with nonzero residual column")
            continue
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                lower[j][k] * lower[i][k] * pivots[k]
                for k in range(i)
            )
            lower[j][i] = numerator / pivot
    return pivots


def require_psd(a: list[list[Fraction]], name: str) -> list[Fraction]:
    pivots = ldl_pivots(a)
    if any(p < 0 for p in pivots):
        raise ValueError(f"{name} is not PSD: pivots={pivots}")
    return pivots


def require_pd(a: list[list[Fraction]], name: str) -> list[Fraction]:
    pivots = ldl_pivots(a)
    if any(p <= 0 for p in pivots):
        raise ValueError(f"{name} is not positive definite: pivots={pivots}")
    return pivots


def fstr(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def verify(data: dict[str, Any]) -> dict[str, Any]:
    gamma = frac(data["Gamma"])
    alpha = frac(data["alpha"])
    if not alpha < gamma:
        raise ValueError("need alpha < Gamma")

    deficit = matrix(data["D"])
    operator = matrix(data["A"])
    if len(deficit) != len(operator):
        raise ValueError("A and D dimensions differ")
    dimension = len(deficit)

    raw_indices = data["packet_indices"]
    if not isinstance(raw_indices, list) or not raw_indices:
        raise ValueError("packet_indices must be nonempty")
    if any(isinstance(i, bool) or not isinstance(i, int) for i in raw_indices):
        raise ValueError("packet indices must be integers")
    if len(set(raw_indices)) != len(raw_indices):
        raise ValueError("duplicate packet index")
    if any(i < 0 or i >= dimension for i in raw_indices):
        raise ValueError("packet index out of range")
    complement = [i for i in range(dimension) if i not in raw_indices]
    if not complement:
        raise ValueError("packet must be a proper subspace")

    deficit_pivots = require_pd(deficit, "D")

    # A >= Gamma I-D iff A+D-Gamma I >= 0.
    lower_slack = diag_shift(
        [
            [operator[i][j] + deficit[i][j] for j in range(dimension)]
            for i in range(dimension)
        ],
        -gamma,
    )
    lower_pivots = require_psd(lower_slack, "lower-symbol slack")

    packet_operator = principal(operator, raw_indices)
    packet_low = diag_shift(
        [[-value for value in row] for row in packet_operator], alpha
    )
    packet_low_pivots = require_psd(packet_low, "alpha I-A_L")

    kappa = gamma - alpha
    packet_deficit = principal(deficit, raw_indices)
    capture = diag_shift(packet_deficit, -kappa)
    capture_pivots = require_psd(capture, "D_L-(Gamma-alpha)I")

    trace_deficit = sum(deficit[i][i] for i in range(dimension))
    packet_requirement = len(raw_indices) * kappa
    if not trace_deficit > packet_requirement:
        raise ValueError("strict reverse trace inequality failed")

    packet_trace = sum(deficit[i][i] for i in raw_indices)
    complement_trace = sum(deficit[i][i] for i in complement)
    if trace_deficit != packet_trace + complement_trace:
        raise ValueError("trace decomposition failed")
    if not complement_trace > 0:
        raise ValueError("strict complement trace must be positive")

    strict_slack = trace_deficit - packet_requirement
    complement_floor = gamma - strict_slack
    complement_operator = principal(operator, complement)
    floor_pivots = require_psd(
        diag_shift(complement_operator, -complement_floor),
        "complement floor",
    )

    claimed = {
        "trace_D": frac(data["claimed_trace_D"]),
        "packet_requirement": frac(data["claimed_packet_requirement"]),
        "strict_slack": frac(data["claimed_strict_slack"]),
        "complement_floor": frac(data["claimed_complement_floor"]),
    }
    actual = {
        "trace_D": trace_deficit,
        "packet_requirement": packet_requirement,
        "strict_slack": strict_slack,
        "complement_floor": complement_floor,
    }
    if claimed != actual:
        raise ValueError(f"claimed values mismatch: claimed={claimed}, actual={actual}")

    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    return {
        "schema": "riemann.strict-symbol-capacity-refutation.v1",
        "verdict": "PASS",
        "dimension": dimension,
        "packet_dimension": len(raw_indices),
        "trace_D": fstr(trace_deficit),
        "packet_requirement": fstr(packet_requirement),
        "strict_slack": fstr(strict_slack),
        "complement_trace": fstr(complement_trace),
        "certified_complement_floor": fstr(complement_floor),
        "D_ldl_pivots": [fstr(x) for x in deficit_pivots],
        "lower_symbol_ldl_pivots": [fstr(x) for x in lower_pivots],
        "packet_low_ldl_pivots": [fstr(x) for x in packet_low_pivots],
        "capture_ldl_pivots": [fstr(x) for x in capture_pivots],
        "floor_ldl_pivots": [fstr(x) for x in floor_pivots],
        "proof_object_sha256": digest,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
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
