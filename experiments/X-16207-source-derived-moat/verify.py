#!/usr/bin/env python3
"""Fail-closed checker for source-derived CCM radial/endpoint moat data.

The checker binds the radial, horizontal, endpoint and first-alias Gram fields
to one source certificate.  It deliberately refuses to manufacture a complete
arithmetic profile-Gram floor from the first Poisson sample alone.
"""
from __future__ import annotations

import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x16207-source-derived-moat.v1"
RESULT_SCHEMA = "riemann.x16207-source-derived-moat-result.v1"

class CertificateError(ValueError):
    pass

def integer(v: Any, name: str) -> int:
    if isinstance(v, bool) or not isinstance(v, int):
        raise CertificateError(f"{name} must be an integer")
    return v

def frac(v: Any, name: str) -> Fraction:
    if isinstance(v, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(v, int):
        return Fraction(v)
    if isinstance(v, str):
        try:
            return Fraction(v)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    raise CertificateError(f"{name} must be an integer or rational string")

def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def check_sha(v: Any, name: str) -> str:
    if not isinstance(v, str) or len(v) != 64:
        raise CertificateError(f"{name} must be a SHA-256 digest")
    try:
        int(v, 16)
    except ValueError as exc:
        raise CertificateError(f"{name} is not hexadecimal") from exc
    return v.lower()

def canonical_sha(obj: dict[str, Any]) -> str:
    x = dict(obj); x.pop("proof_object_sha256", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    source = payload.get("source")
    if not isinstance(source, dict):
        raise CertificateError("source manifest missing")
    gamma = integer(source.get("gamma"), "source.gamma")
    if gamma <= 0 or source.get("modes") != [0, 4, 8, 12]:
        raise CertificateError("unexpected source packet")
    for key in ("actual_primitive_sha256", "full_exact_result_sha256", "full_exact_proof_object_sha256", "producer_sha256"):
        check_sha(source.get(key), f"source.{key}")

    columns = payload.get("repaired_columns")
    if not isinstance(columns, list) or len(columns) != 2:
        raise CertificateError("exactly two repaired columns are required")
    radial_sum = Fraction(0); derivative_sum = Fraction(0); horizontal_sum = Fraction(0); f4_sq = Fraction(0)
    for i, col in enumerate(columns):
        if not isinstance(col, dict):
            raise CertificateError(f"column[{i}] must be an object")
        r = frac(col.get("radial_l2_error_upper"), f"column[{i}].radial")
        d = frac(col.get("frequency_derivative_l2_error_upper"), f"column[{i}].derivative")
        h = frac(col.get("horizontal_strip_l2_error_upper"), f"column[{i}].horizontal")
        f4 = frac(col.get("source_fourth_derivative_l1_upper"), f"column[{i}].f4")
        if min(r, d, h, f4) < 0:
            raise CertificateError("source bounds must be nonnegative")
        radial_sum += r; derivative_sum += d; horizontal_sum += h; f4_sq += f4*f4

    repl = payload.get("source_derived_replacements")
    if not isinstance(repl, dict):
        raise CertificateError("source_derived_replacements missing")
    tail_sq = frac(repl.get("tail_l2_sq_upper"), "tail_l2_sq_upper")
    deriv_sq = frac(repl.get("derivative_tail_l2_sq_upper"), "derivative_tail_l2_sq_upper")
    horiz_sq = frac(repl.get("horizontal_tail_l2_sq_upper"), "horizontal_tail_l2_sq_upper")
    f4 = frac(repl.get("source_fourth_derivative_l1_upper"), "source_fourth_derivative_l1_upper")
    if tail_sq < radial_sum*radial_sum:
        raise CertificateError("global radial tail is understated")
    if deriv_sq < derivative_sum*derivative_sum:
        raise CertificateError("global derivative tail is understated")
    if horiz_sq < horizontal_sum*horizontal_sum:
        raise CertificateError("global horizontal tail is understated")
    if f4*f4 < f4_sq:
        raise CertificateError("packet fourth-derivative bound is understated")

    lam = frac(repl.get("lambda_lower"), "lambda_lower")
    pi_lo = frac(repl.get("pi_lower"), "pi_lower")
    zeta4 = frac(repl.get("zeta4_minus_one_upper"), "zeta4_minus_one_upper")
    if lam <= 0 or pi_lo <= 0 or pi_lo > 3 or zeta4 < Fraction(9083, 108045):
        raise CertificateError("endpoint constants are not outward")
    endpoint_point = zeta4*f4/(2*pi_lo*lam)**4
    endpoint_l2_sq = (zeta4*f4)**2/((2*pi_lo)**8*7*lam**7)
    point_claim = frac(repl.get("poisson_endpoint_point_upper"), "poisson_endpoint_point_upper")
    l2_sq_claim = frac(repl.get("poisson_endpoint_l2_sq_upper"), "poisson_endpoint_l2_sq_upper")
    l2_norm_claim = frac(repl.get("poisson_endpoint_l2_norm_upper"), "poisson_endpoint_l2_norm_upper")
    if point_claim < endpoint_point or l2_sq_claim < endpoint_l2_sq or l2_norm_claim*l2_norm_claim < l2_sq_claim:
        raise CertificateError("endpoint charge is understated")

    deterministic = radial_sum + derivative_sum + point_claim + l2_norm_claim
    deterministic_claim = frac(repl.get("deterministic_error_upper"), "deterministic_error_upper")
    if deterministic_claim < deterministic:
        raise CertificateError("deterministic error is not derived from source fields")

    first = payload.get("first_alias_profile_gram")
    if not isinstance(first, dict):
        raise CertificateError("first_alias_profile_gram missing")
    corr = frac(first.get("normalized_cross_abs_upper"), "normalized_cross_abs_upper")
    first_lo = frac(first.get("lower"), "first_alias.lower")
    first_hi = frac(first.get("upper"), "first_alias.upper")
    if corr < 0 or first_lo > 1-corr or first_hi < 1+corr:
        raise CertificateError("first-alias Gram bounds are not outward")

    complete = payload.get("complete_arithmetic_alias")
    if not isinstance(complete, dict):
        raise CertificateError("complete arithmetic alias block missing")
    alias_raw = complete.get("cross_error_upper")
    if alias_raw is None:
        promotion = "SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN"
        complete_lo = None
    else:
        alias = frac(alias_raw, "complete_alias.cross_error_upper")
        if alias < 0:
            raise CertificateError("complete alias error must be nonnegative")
        complete_lo = first_lo - alias
        if complete_lo <= 0:
            raise CertificateError("complete arithmetic profile Gram has no positive moat")
        promotion = "PRODUCTION_PROFILE_GRAM_CLOSED"

    if radial_sum > Fraction(1, gamma*gamma):
        raise CertificateError("radial diagonal target gamma^-2 failed")
    if derivative_sum > Fraction(1, gamma):
        raise CertificateError("frequency diagonal target gamma^-1 failed")

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "classification": promotion,
        "gamma": gamma,
        "source_bindings": {k: source[k] for k in source if k.endswith("sha256")},
        "source_derived": {
            "radial_l2_sum_upper": fstr(radial_sum),
            "frequency_derivative_l2_sum_upper": fstr(derivative_sum),
            "horizontal_l2_sum_upper": fstr(horizontal_sum),
            "tail_l2_sq_upper": fstr(tail_sq),
            "derivative_tail_l2_sq_upper": fstr(deriv_sq),
            "horizontal_tail_l2_sq_upper": fstr(horiz_sq),
            "fourth_derivative_l1_upper": fstr(f4),
            "endpoint_point_upper": fstr(endpoint_point),
            "endpoint_l2_sq_upper": fstr(endpoint_l2_sq),
            "deterministic_error_reconstructed": fstr(deterministic),
            "deterministic_error_upper": fstr(deterministic_claim)
        },
        "profile_gram": {
            "first_alias_lower": fstr(first_lo),
            "first_alias_upper": fstr(first_hi),
            "complete_lower": None if complete_lo is None else fstr(complete_lo)
        },
        "cofinal_decay": {
            "radial_gate": "sum eps_rad <= gamma^-2",
            "derivative_gate": "sum eps_drad <= gamma^-1",
            "endpoint_gate": "p=4 source H4 charge is checked per block and must tend to zero",
            "complete_alias_gate": "cross_error_upper must tend to zero before production promotion"
        },
        "proof_boundary": (
            "The radial, derivative, horizontal and endpoint placeholders are source-derived and bound into the deterministic error. "
            "The first-alias Gram is exact. Promotion remains fail-closed until a directed complete Poisson cross-alias operator bound is supplied."
        )
    }
    result["proof_object_sha256"] = canonical_sha(result)
    return result

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificate", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    try:
        obj = json.loads(args.certificate.read_text())
        out = verify(obj); code = 0
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        out = {"schema": RESULT_SCHEMA, "classification": "REJECTED", "reason": str(exc)}; code = 2
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(text)
    else:
        print(text, end="")
    return code
if __name__ == "__main__":
    raise SystemExit(main())
