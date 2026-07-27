#!/usr/bin/env python3
"""Exact audit checker for saturated sign chains and candidate locality gates."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x13801-audit-kernels.v1"
LOCAL_KINDS = {"LOCAL_COUNT_PREDICATE", "PROVED_SLAB_LOCALIZER"}
GLOBAL_KINDS = {
    "GLOBAL_PICK_FUNCTIONAL",
    "GLOBAL_WEIL_FUNCTIONAL",
    "GLOBAL_CARRIER_FUNCTIONAL",
    "GLOBAL_SCREW_FUNCTIONAL",
    "GLOBAL_DIRECT_XI_FUNCTIONAL",
}


class AuditError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AuditError(f"{name} must be an integer, not Boolean")
    return value


def rational(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise AuditError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise AuditError(f"{name} is not rational") from exc
    if isinstance(value, list) and len(value) == 2:
        p = integer(value[0], name + "[0]")
        q = integer(value[1], name + "[1]")
        if q == 0:
            raise AuditError(f"{name} denominator is zero")
        return Fraction(p, q)
    raise AuditError(f"{name} must be an integer, fraction string, or [p,q]")


def verify_sign_chain(payload: dict[str, Any]) -> dict[str, Any]:
    total = integer(payload.get("total_multiplicity"), "total_multiplicity")
    if total < 0:
        raise AuditError("total_multiplicity must be nonnegative")
    if payload.get("left_endpoint_zero_free") is not True:
        raise AuditError("left endpoint zero-free gate is missing")
    if payload.get("right_endpoint_zero_free") is not True:
        raise AuditError("right endpoint zero-free gate is missing")
    lower = rational(payload.get("lower"), "lower")
    upper = rational(payload.get("upper"), "upper")
    if lower >= upper:
        raise AuditError("slab endpoints are not increasing")
    raw = payload.get("samples")
    if not isinstance(raw, list) or len(raw) != total + 1:
        raise AuditError("a saturated chain needs total_multiplicity+1 samples")
    points: list[Fraction] = []
    signs: list[int] = []
    for index, sample in enumerate(raw):
        if not isinstance(sample, dict):
            raise AuditError(f"samples[{index}] must be an object")
        point = rational(sample.get("t"), f"samples[{index}].t")
        sign = integer(sample.get("sign"), f"samples[{index}].sign")
        if sign not in (-1, 1):
            raise AuditError("every sign must be exactly -1 or +1")
        points.append(point)
        signs.append(sign)
    if not (lower < points[0] and points[-1] < upper):
        raise AuditError("sample chain is not strictly inside the slab")
    if any(points[i] >= points[i + 1] for i in range(len(points) - 1)):
        raise AuditError("sample points are not strictly increasing")
    if any(signs[i] == signs[i + 1] for i in range(len(signs) - 1)):
        raise AuditError("the sign chain is not fully alternating")
    return {
        "kind": "saturated-sign-chain",
        "status": "CERTIFIED_SATURATED_CHAIN_STRUCTURE",
        "total_multiplicity": total,
        "simple_line_zero_intervals": total,
        "off_line_multiplicity_remaining": 0,
        "endpoint_gates_closed": True,
        "interpretation": (
            "Finite exact structure only. Soundness of the total count and each "
            "directed Hardy-Z sign is an external proof gate."
        ),
    }


def verify_retirement(payload: dict[str, Any]) -> dict[str, Any]:
    kind = payload.get("candidate_kind")
    if kind not in LOCAL_KINDS | GLOBAL_KINDS:
        raise AuditError("unknown candidate_kind")
    locality = payload.get("locality_gate_proved")
    complement = payload.get("complete_complement_bound")
    if not isinstance(locality, bool) or not isinstance(complement, bool):
        raise AuditError("locality/complement gates must be Boolean")
    if kind in LOCAL_KINDS:
        permitted = True
        reason = "the candidate predicate is local by theorem"
    else:
        permitted = locality or complement
        reason = (
            "a global functional needs a proved locality implication or a "
            "complete complementary-zero bound"
        )
    return {
        "kind": "candidate-retirement",
        "candidate_kind": kind,
        "status": "RETIREMENT_PERMITTED" if permitted else "RETIREMENT_REJECTED",
        "locality_gate_proved": locality,
        "complete_complement_bound": complement,
        "reason": reason,
    }


def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise AuditError("schema mismatch")
    kind = payload.get("kind")
    if kind == "saturated-sign-chain":
        result = verify_sign_chain(payload)
    elif kind == "candidate-retirement":
        result = verify_retirement(payload)
    else:
        raise AuditError("unsupported audit kind")
    return {"schema": SCHEMA, **result}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, AuditError) as exc:
        result = {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
