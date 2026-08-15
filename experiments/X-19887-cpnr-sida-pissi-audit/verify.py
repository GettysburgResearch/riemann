#!/usr/bin/env python3
"""Exact finite regression for the CPNR/SIDA/PSSI final audit.

The checker authenticates rational constants and finite algebra only. It does
not prove the analytic Chebyshev theorem, the frozen factor-67 stack, the
endpoint consumer, RH, or the measure-theoretic Stieltjes uniqueness theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x19887-cpnr-sida-pissi-audit.v1"
OUTPUT_SCHEMA = "riemann.x19887-cpnr-sida-pissi-verification.v1"

class CertificateError(ValueError):
    pass

def rat(v: Any, name: str) -> Fraction:
    if isinstance(v, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(v, int):
        return Fraction(v)
    if isinstance(v, str):
        try:
            return Fraction(v)
        except Exception as exc:
            raise CertificateError(f"{name} is not rational") from exc
    raise CertificateError(f"{name} is not an exact rational")

def fj(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def canonical_sha(v: Any) -> str:
    raw = json.dumps(v, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("unsupported schema")

    log2_lo = rat(data["log2_lower"], "log2_lower")
    log2_hi = rat(data["log2_upper"], "log2_upper")
    sqrt2_hi = rat(data["sqrt2_upper"], "sqrt2_upper")
    sqrt67_hi = rat(data["sqrt67_upper"], "sqrt67_upper")
    if not (log2_lo < log2_hi):
        raise CertificateError("bad log2 enclosure")
    if not (log2_lo == Fraction(2, 3) and log2_hi == Fraction(7, 10)):
        raise CertificateError("control expects the declared rational log2 enclosure")
    if sqrt2_hi * sqrt2_hi <= 2:
        raise CertificateError("sqrt2 upper bound is not strict")
    if sqrt67_hi * sqrt67_hi <= 67:
        raise CertificateError("sqrt67 upper bound is not strict")

    thinning_bound = 2080 * log2_hi * sqrt67_hi
    if thinning_bound != 12012:
        raise CertificateError("unexpected thinning constant")

    omega = [rat(x, f"omega[{i}]") for i, x in enumerate(data["omega"])]
    current = [rat(x, f"current[{i}]") for i, x in enumerate(data["current"])]
    child_caps = [[rat(x, f"child_caps[{j}][{i}]") for i, x in enumerate(row)] for j, row in enumerate(data["child_caps"])]
    alphas = [rat(x, f"alphas[{i}]") for i, x in enumerate(data["alphas"])]
    y4 = [rat(x, f"y4[{i}]") for i, x in enumerate(data["y4"])]
    if not (len(omega) == len(current) == len(y4)):
        raise CertificateError("vector dimension mismatch")
    if len(child_caps) != len(alphas) or any(len(row) != len(omega) for row in child_caps):
        raise CertificateError("child dimension mismatch")
    if any(x < 0 for x in omega + current + y4 + alphas):
        raise CertificateError("negative input")
    if sum(alphas) >= Fraction(1, 8):
        raise CertificateError("child mass is not strictly subcritical")

    used = current[:]
    for a, row in zip(alphas, child_caps):
        used = [u + a * c for u, c in zip(used, row)]
    residual = [o - u for o, u in zip(omega, used)]
    if any(r < 0 for r in residual):
        raise CertificateError("CPNR residual is negative")
    delta_local = sum(w * r for w, r in zip(y4, residual))

    child_slacks = [[rat(x, f"child_slacks[{j}][{i}]") for i, x in enumerate(row)] for j, row in enumerate(data["child_slacks"])]
    if len(child_slacks) != len(alphas) or any(len(row) != len(omega) for row in child_slacks):
        raise CertificateError("child slack dimension mismatch")
    parent_slack = residual[:]
    for a, row in zip(alphas, child_slacks):
        parent_slack = [u + a * c for u, c in zip(parent_slack, row)]
    delta_children = [sum(w * s for w, s in zip(y4, row)) for row in child_slacks]
    delta_parent = sum(w * s for w, s in zip(y4, parent_slack))
    if delta_parent != delta_local + sum(a * d for a, d in zip(alphas, delta_children)):
        raise CertificateError("native slack cocycle failed")

    kroot_plus = rat(data["sqrtK_plus_130"], "sqrtK_plus_130")
    if kroot_plus <= 0:
        raise CertificateError("sqrtK_plus_130 must be positive")
    strict_defect_lower = Fraction(8, 27) / kroot_plus
    if strict_defect_lower <= 0:
        raise CertificateError("strict defect lower bound vanished")

    lhs_type = data["pissi_lhs_measure_type"]
    branch_type = data["pissi_native_branch_measure_type"]
    branch_mass = rat(data["pissi_native_branch_mass"], "pissi_native_branch_mass")
    if lhs_type != "pure_point" or branch_type != "absolutely_continuous":
        raise CertificateError("control requires pure-point lhs and diffuse native branch")
    if branch_mass <= 0:
        raise CertificateError("native diffuse branch must be nonzero")
    pissi_verdict = "REJECT_POSITIVE_PARALLEL_PISSI_NONZERO_DIFFUSE_SUBMEASURE"

    interval_lengths = [rat(x, f"interval_lengths[{i}]") for i, x in enumerate(data["interval_lengths"])]
    sida_constant = rat(data["sida_lipschitz_constant"], "sida_lipschitz_constant")
    if any(x <= 0 for x in interval_lengths) or sida_constant <= 0:
        raise CertificateError("invalid SIDA controls")
    sida_bounds = [sida_constant * x for x in interval_lengths]
    if any(sida_bounds[i+1] >= sida_bounds[i] for i in range(len(sida_bounds)-1)):
        raise CertificateError("SIDA bounds must strictly decrease")

    proof = {
        "thinning_bound": fj(thinning_bound),
        "residual": [fj(x) for x in residual],
        "delta_local": fj(delta_local),
        "delta_parent": fj(delta_parent),
        "strict_defect_lower": fj(strict_defect_lower),
        "pissi_verdict": pissi_verdict,
        "sida_bounds": [fj(x) for x in sida_bounds],
    }
    return {
        "schema": OUTPUT_SCHEMA,
        "verdict": "PASS_CPNR_SIDA_AND_PISSI_SCOPE_AUDIT",
        **proof,
        "proof_object_sha256": canonical_sha(proof),
        "proof_boundary": (
            "Exact rational regression for the thinning constant, source-owned residual, "
            "native slack cocycle, shrinking SIDA bounds, and the spectral-type category "
            "conflict in positive parallel PSSI. It does not prove the frozen analytic stack or RH."
        ),
    }

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    try:
        data = json.loads(args.certificate.read_text())
        result = verify(data)
    except (OSError, json.JSONDecodeError, KeyError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
