#!/usr/bin/env python3
"""Exact rational checker for the certified-frame / triangular-tail cofinal gate."""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence

SCHEMA = "riemann.x15305-zero-frame-tail-gates.v1"

class CertificateError(ValueError):
    pass

def rat(x: Any, name: str) -> Fraction:
    if isinstance(x, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(x, int):
        return Fraction(x)
    if not isinstance(x, dict):
        raise CertificateError(f"{name} must be an integer or rational object")
    n, d = x.get("numerator"), x.get("denominator")
    if isinstance(n, bool) or not isinstance(n, int) or isinstance(d, bool) or not isinstance(d, int) or d <= 0:
        raise CertificateError(f"bad rational at {name}")
    return Fraction(n, d)

def jout(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}

def digest(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()

def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError("wrong schema")
    sigma2 = rat(data.get("sigma2"), "sigma2")
    visible_loss = rat(data.get("visible_residual_lower_loss"), "visible_residual_lower_loss")
    cross2 = rat(data.get("visible_ambient_cross_squared"), "visible_ambient_cross_squared")
    h = rat(data.get("ambient_coercivity"), "ambient_coercivity")
    radical_loss = rat(data.get("radical_lower_loss"), "radical_lower_loss")
    radical_dual2 = rat(data.get("radical_row_dual_squared"), "radical_row_dual_squared")
    assembly = rat(data.get("assembly_radius"), "assembly_radius")
    for name, x in [
        ("sigma2", sigma2), ("visible_residual_lower_loss", visible_loss),
        ("visible_ambient_cross_squared", cross2), ("radical_lower_loss", radical_loss),
        ("radical_row_dual_squared", radical_dual2), ("assembly_radius", assembly)
    ]:
        if x < 0:
            raise CertificateError(f"{name} must be nonnegative")
    if h <= 0:
        raise CertificateError("ambient_coercivity must be positive")
    beta = sigma2 - visible_loss - cross2 / h
    if beta <= 0:
        raise CertificateError("certified visible Schur margin is not strictly positive")
    epsilon = radical_loss + radical_dual2 + assembly
    claimed_beta = data.get("claimed_beta")
    if claimed_beta is not None and rat(claimed_beta, "claimed_beta") != beta:
        raise CertificateError("claimed_beta mismatch")
    claimed_epsilon = data.get("claimed_epsilon")
    if claimed_epsilon is not None and rat(claimed_epsilon, "claimed_epsilon") != epsilon:
        raise CertificateError("claimed_epsilon mismatch")
    out = {
        "schema": "riemann.x15305-zero-frame-tail-gates.verification.v1",
        "verified": True,
        "status": "CERTIFIED_POSITIVE_VISIBLE_SCHUR_AND_GLOBAL_LOWER_FLOOR",
        "visible_schur_floor": jout(beta),
        "global_negative_floor_loss": jout(epsilon),
        "global_floor": jout(-epsilon),
        "components": {
            "sigma2": jout(sigma2),
            "visible_residual_lower_loss": jout(visible_loss),
            "visible_ambient_schur_loss": jout(cross2 / h),
            "radical_lower_loss": jout(radical_loss),
            "radical_row_dual_squared": jout(radical_dual2),
            "assembly_radius": jout(assembly),
        },
        "proof_object_sha256": digest(data),
        "proof_boundary": (
            "Exact scalar/Loewner consequence only. Production must source-bind the "
            "certified-zero frame, residual lower/cross bounds, ambient metric, "
            "radical-tail dual estimate, and assembly enclosure."
        ),
    }
    body = dict(out)
    out["verification_sha256"] = digest(body)
    return out

def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("certificate", type=Path)
    args = p.parse_args(argv)
    try:
        data = json.loads(args.certificate.read_text())
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError, ZeroDivisionError) as exc:
        print(json.dumps({"verified": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
