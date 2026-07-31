#!/usr/bin/env python3
"""Fraction-only verifier for the L-18508/T-18503 frame-tail moat."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as Q
from pathlib import Path

SCHEMA = "riemann.x18503-frame-tail-moat.v1"
class Reject(ValueError): pass

def integer(x, name):
    if isinstance(x, bool) or not isinstance(x, int):
        raise Reject(f"{name} must be integer")
    return x

def rat(x, name):
    if not isinstance(x, dict):
        raise Reject(f"{name} must be rational object")
    a = integer(x.get("numerator"), name + ".numerator")
    b = integer(x.get("denominator"), name + ".denominator")
    if b <= 0:
        raise Reject(f"{name} denominator must be positive")
    return Q(a, b)

def outq(x):
    return {"numerator": x.numerator, "denominator": x.denominator}

def digest(x):
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def verify(d):
    if d.get("schema") != SCHEMA:
        raise Reject("schema mismatch")
    sigma = rat(d.get("frame_floor"), "frame_floor")
    B = rat(d.get("omitted_zero_budget"), "omitted_zero_budget")
    eps = rat(d.get("radical_endpoint"), "radical_endpoint")
    if sigma <= 0:
        raise Reject("frame floor must be positive")
    if B < 0 or eps < 0:
        raise Reject("budgets must be nonnegative")

    direct = sigma - B
    requested = max(B, eps) < sigma
    positive_counted = B + eps < sigma
    gaussian = B + 2 * eps < sigma

    result = {
        "schema": SCHEMA,
        "frame_floor": outq(sigma),
        "omitted_zero_budget": outq(B),
        "radical_endpoint": outq(eps),
        "direct_visible_floor": outq(direct),
        "requested_interval_feasible": requested,
        "positive_counted_interval_feasible": positive_counted,
        "gaussian_interval_feasible": gaussian,
    }

    if gaussian:
        beta = eps + (sigma - B) / 2
        threshold = B + beta
        if not (eps < threshold < sigma):
            raise Reject("internal threshold inequality failed")
        if not (2 * eps <= beta):
            raise Reject("internal gaussian beta inequality failed")
        result.update({
            "status": "CERTIFIED_GAUSSIAN_FRAME_TAIL_MOAT",
            "beta": outq(beta),
            "threshold": outq(threshold),
            "counted_visible_margin": outq(beta - eps),
        })
    elif direct > 0:
        result.update({
            "status": "CERTIFIED_DIRECT_VISIBLE_FLOOR_ONLY",
            "beta": None,
            "threshold": None,
            "counted_visible_margin": None,
        })
    else:
        result.update({
            "status": "NO_POSITIVE_DIRECT_VISIBLE_FLOOR",
            "beta": None,
            "threshold": None,
            "counted_visible_margin": None,
        })

    result["proof_object_sha256"] = digest(result)

    expected = d.get("expected")
    if not isinstance(expected, dict):
        raise Reject("expected missing")
    for key in (
        "status",
        "requested_interval_feasible",
        "positive_counted_interval_feasible",
        "gaussian_interval_feasible",
    ):
        if expected.get(key) != result[key]:
            raise Reject(f"expected {key} mismatch")
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("certificate", type=Path)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    try:
        out = verify(json.loads(a.certificate.read_text()))
        code = 0
    except Exception as exc:
        out = {"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if a.output:
        a.output.write_text(text)
    else:
        print(text, end="")
    return code

if __name__ == "__main__":
    raise SystemExit(main())
