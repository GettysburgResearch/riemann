#!/usr/bin/env python3
"""Fail-closed verifier for one source-bound cofinal CCM production block.

This checker does not reprove the alias stationary-phase theorem. It imports
its frozen all-scale inequality from L-16231 and verifies that a block binds an
actual DIRECTED_INTERVAL_ODE source file, then reconstructs the complete alias
Gram, support-measure, scalarization, and target/gap ratio exactly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x16209-cofinal-production.v1"
RESULT_SCHEMA = "riemann.x16209-cofinal-production-result.v1"
SOURCE_SCHEMA = "riemann.x16206-directed-interval-ode-primitive.v1"
ALIAS_THEOREM_GIT_BLOB_SHA1 = "c64928b212915d9ae766118b621e6b235de41aa8"
MODE8_THEOREM_GIT_BLOB_SHA1 = "0f02c679b7d2415f29f3b75bbc065d2958e3f0f3"


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


def canonical_sha(obj: dict[str, Any], drop: str | None = None) -> str:
    x = dict(obj)
    if drop is not None:
        x.pop(drop, None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_hex(v: Any, n: int, name: str) -> str:
    if not isinstance(v, str) or len(v) != n:
        raise CertificateError(f"{name} must be a {n}-hex digest")
    try:
        int(v, 16)
    except ValueError as exc:
        raise CertificateError(f"{name} is not hexadecimal") from exc
    return v.lower()


def power_of_two_exponent(n: int) -> int:
    if n <= 0 or n & (n - 1):
        raise CertificateError("gamma must be a power of two")
    return n.bit_length() - 1


def cube_root_floor(n: int) -> int:
    q = round(n ** (1 / 3))
    while (q + 1) ** 3 <= n:
        q += 1
    while q ** 3 > n:
        q -= 1
    return q


def ceil_fraction(x: Fraction, denominator: int) -> Fraction:
    return Fraction((x.numerator * denominator + x.denominator - 1) // x.denominator, denominator)


def alias_upper(gamma: int) -> Fraction:
    return (
        Fraction(18, math.isqrt(gamma))
        + Fraction(2, cube_root_floor(gamma))
        + Fraction(1792, gamma)
    )


def mode_ratio_upper(gamma: int) -> Fraction:
    exponent = power_of_two_exponent(gamma)
    if exponent < 12 or (exponent - 12) % 3:
        raise CertificateError("gamma is not on the frozen 4096*8^j schedule")
    j = (exponent - 12) // 3
    return Fraction(1, 50_000 * 4096**j)


def verify_source(source: dict[str, Any], path: Path, binding: dict[str, Any]) -> tuple[int, Fraction, Fraction]:
    if source.get("schema") != SOURCE_SCHEMA or source.get("classification") != "DIRECTED_INTERVAL_ODE":
        raise CertificateError("source is not a DIRECTED_INTERVAL_ODE primitive")
    if file_sha(path) != check_hex(binding.get("source_file_sha256"), 64, "source_file_sha256"):
        raise CertificateError("source file SHA-256 mismatch")
    internal = source.get("primitive_sha256")
    check_hex(internal, 64, "source primitive_sha256")
    if canonical_sha(source, "primitive_sha256") != internal:
        raise CertificateError("source internal primitive digest mismatch")
    if internal != check_hex(binding.get("source_primitive_sha256"), 64, "source_primitive_sha256"):
        raise CertificateError("certificate/source primitive digest mismatch")
    source_sha = check_hex(source.get("source_sha256"), 64, "source source_sha256")
    if source_sha != check_hex(binding.get("source_definition_sha256"), 64, "source_definition_sha256"):
        raise CertificateError("source definition digest mismatch")
    producer = check_hex(source.get("producer_sha256"), 64, "source producer_sha256")
    if producer != check_hex(binding.get("source_producer_sha256"), 64, "source_producer_sha256"):
        raise CertificateError("source producer digest mismatch")

    src = source.get("source")
    if not isinstance(src, dict):
        raise CertificateError("source definition missing")
    gamma = integer(src.get("gamma"), "source.gamma")
    if src.get("modes") != [0, 4, 8, 12]:
        raise CertificateError("source modes mismatch")
    rows = source.get("separation_and_pole_data")
    if not isinstance(rows, list) or [r.get("mode") for r in rows] != [0, 4, 8, 12]:
        raise CertificateError("separation packet mismatch")
    sigma_hi = max(frac(r["sigma_sq_interval"][1], "sigma upper") for r in rows)
    if sigma_hi > Fraction(1, 128):
        raise CertificateError("source exits L-16231 sigma scope")

    tail = source.get("tail_energy")
    if not isinstance(tail, dict):
        raise CertificateError("source tail-energy ledger missing")
    radial_sq = frac(tail.get("normalized_radial_total_l2_sq"), "normalized radial energy")
    derivative_sq = frac(tail.get("frequency_derivative_tail_l2_sq_upper"), "derivative energy")
    if radial_sq != 1 or derivative_sq > 4:
        raise CertificateError("source unit-energy bounds are not the frozen production bounds")
    return gamma, radial_sq, derivative_sq


def verify(payload: dict[str, Any], source_path: Path) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    source = json.loads(source_path.read_text())
    binding = payload.get("source_binding")
    if not isinstance(binding, dict):
        raise CertificateError("source_binding missing")
    gamma, radial_sq, derivative_sq = verify_source(source, source_path, binding)
    if gamma != integer(payload.get("gamma"), "gamma"):
        raise CertificateError("certificate gamma does not match source")
    if binding.get("alias_theorem_git_blob_sha1") != ALIAS_THEOREM_GIT_BLOB_SHA1:
        raise CertificateError("L-16231 theorem binding mismatch")
    if binding.get("mode8_theorem_git_blob_sha1") != MODE8_THEOREM_GIT_BLOB_SHA1:
        raise CertificateError("T-15102 theorem binding mismatch")

    exponent = power_of_two_exponent(gamma)
    if exponent < 15 or (exponent - 12) % 3:
        raise CertificateError("this emitter starts at gamma=32768 on the dyadic-cubic schedule")
    j = (exponent - 12) // 3
    q2 = math.isqrt(gamma)
    q3 = cube_root_floor(gamma)
    if q3**3 != gamma:
        raise CertificateError("dyadic-cubic schedule requires an exact cube")

    alias = payload.get("alias")
    if not isinstance(alias, dict):
        raise CertificateError("alias block missing")
    cross_required = alias_upper(gamma)
    cross_claim = frac(alias.get("cross_error_upper"), "cross_error_upper")
    if cross_claim < cross_required:
        raise CertificateError("alias cross bound understates L-16231")
    first_cross = frac(alias.get("first_alias_cross_upper"), "first_alias_cross_upper")
    r_frame = mode_ratio_upper(gamma)
    frame_sq = Fraction(32) * r_frame * (2 - r_frame) ** 2 / (1 - r_frame) ** 2
    if first_cross * first_cross < frame_sq:
        raise CertificateError("first-alias repaired-frame cross bound understated")
    first_lo = frac(alias.get("first_alias_lower"), "first_alias_lower")
    first_hi = frac(alias.get("first_alias_upper"), "first_alias_upper")
    if first_lo > 1 - first_cross or first_hi < 1 + first_cross:
        raise CertificateError("first-alias Gram does not contain the repaired source frame")
    full_lo = first_lo - cross_claim
    self_upper = frac(alias.get("higher_self_upper"), "higher_self_upper")
    full_hi = frac(alias.get("full_upper"), "full_upper")
    if full_lo <= 0 or full_hi < first_hi + self_upper + cross_claim:
        raise CertificateError("complete profile-Gram interval invalid")

    endpoint = payload.get("endpoint")
    if not isinstance(endpoint, dict) or endpoint.get("method") != "RADIAL_OUTGOING_PHASE":
        raise CertificateError("normalized radial endpoint ledger missing")
    endpoint_scale = Fraction(128, gamma)
    point = frac(endpoint.get("point_upper"), "endpoint point")
    l2norm = frac(endpoint.get("l2_norm_upper"), "endpoint l2 norm")
    l2sq = frac(endpoint.get("l2_sq_upper"), "endpoint l2 sq")
    if point < endpoint_scale or l2norm < endpoint_scale or l2sq < l2norm * l2norm:
        raise CertificateError("endpoint ledger understates the all-scale radial bound")

    tails = payload.get("source_tails")
    if not isinstance(tails, dict):
        raise CertificateError("source_tails missing")
    radial = frac(tails.get("radial_l2_sum_upper"), "radial_l2_sum_upper")
    derivative = frac(tails.get("derivative_l2_sum_upper"), "derivative_l2_sum_upper")
    if radial * radial < radial_sq or derivative * derivative < derivative_sq:
        raise CertificateError("source-tail norm understates the source primitive")
    deterministic = radial + derivative + point + l2norm

    cofinal = payload.get("cofinal_block")
    if not isinstance(cofinal, dict):
        raise CertificateError("cofinal_block missing")
    measure = frac(cofinal.get("measure_lower"), "measure_lower")
    exceptional = frac(cofinal.get("exceptional_measure_upper"), "exceptional_measure_upper")
    families = cofinal.get("families")
    if measure <= 0 or exceptional < 0 or not isinstance(families, list) or len(families) != 2:
        raise CertificateError("cofinal support ledger malformed")
    bad = exceptional
    thresholds = Fraction(0)
    for i, family in enumerate(families):
        ms = frac(family.get("mean_square_upper"), f"family[{i}].mean_square_upper")
        th = frac(family.get("threshold"), f"family[{i}].threshold")
        if ms < Fraction(1, gamma) or th < Fraction(1, q3):
            raise CertificateError("cofinal family understates the frozen mean-square ledger")
        bad += ms / (th * th)
        thresholds += th
    if bad >= measure:
        raise CertificateError("cofinal good-support measure is nonpositive")

    scalar = payload.get("scalarization")
    if not isinstance(scalar, dict):
        raise CertificateError("scalarization block missing")
    log_lower = frac(scalar.get("log_R_lower"), "log_R_lower")
    if log_lower > Fraction(69 * exponent, 100):
        raise CertificateError("log_R_lower is not justified by ln(2)>69/100")
    bounded = frac(scalar.get("bounded_main_correction_upper"), "bounded correction")
    if bounded < 1:
        raise CertificateError("bounded main correction understated")
    eps = (bounded + deterministic + thresholds) / (full_lo * log_lower)
    eps_claim = frac(scalar.get("claimed_epsilon_upper"), "claimed_epsilon_upper")
    if eps_claim < eps or eps_claim >= 1:
        raise CertificateError("scalarization epsilon claim invalid")

    hierarchy = payload.get("tail_hierarchy")
    if not isinstance(hierarchy, dict):
        raise CertificateError("tail_hierarchy missing")
    ratio_bound = mode_ratio_upper(gamma)
    declared_ratio = frac(hierarchy.get("d4_over_d8_upper"), "d4_over_d8_upper")
    if declared_ratio < ratio_bound:
        raise CertificateError("mode-4/mode-8 ratio understates the frozen hierarchy")
    C4 = frac(hierarchy.get("target_constant_upper"), "target_constant_upper")
    c8 = frac(hierarchy.get("gap_constant_lower"), "gap_constant_lower")
    if C4 < 4 or c8 > Fraction(1, 20) or c8 <= 0:
        raise CertificateError("target/gap constants are not outward")
    target_scaled = (1 + eps_claim) * C4 * declared_ratio
    gap_scaled = (1 - eps_claim) * c8 - 2 * eps_claim * C4 * declared_ratio
    if gap_scaled <= 0:
        raise CertificateError("complete scaled gap is not positive")
    ground_ratio = target_scaled / gap_scaled
    ratio_claim = frac(hierarchy.get("claimed_ground_ratio_upper"), "claimed_ground_ratio_upper")
    if ratio_claim < ground_ratio:
        raise CertificateError("ground ratio claim understated")

    next_gamma = integer(payload.get("next_gamma"), "next_gamma")
    if next_gamma != gamma * 8:
        raise CertificateError("next gamma is not the frozen dyadic-cubic successor")
    if alias_upper(next_gamma) >= cross_claim:
        raise CertificateError("alias cross bound does not improve at next scale")
    if mode_ratio_upper(next_gamma) * 4096 != ratio_bound:
        raise CertificateError("mode hierarchy does not contract by 4096")

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "classification": "SOURCE_BOUND_COFINAL_WRAPPER_BLOCK",
        "gamma": gamma,
        "schedule_index": j,
        "source_bindings": {
            "source_file_sha256": file_sha(source_path),
            "source_primitive_sha256": source["primitive_sha256"],
            "source_definition_sha256": source["source_sha256"],
            "source_producer_sha256": source["producer_sha256"],
        },
        "complete_alias": {
            "sqrt_floor": q2,
            "cuberoot": q3,
            "cross_required": fstr(cross_required),
            "cross_upper": fstr(cross_claim),
            "profile_gram_lower": fstr(full_lo),
            "profile_gram_upper": fstr(full_hi),
        },
        "source_tail": {
            "radial_l2_upper": fstr(radial),
            "frequency_derivative_l2_upper": fstr(derivative),
            "endpoint_point_upper": fstr(point),
            "endpoint_l2_norm_upper": fstr(l2norm),
            "deterministic_error_upper": fstr(deterministic),
        },
        "cofinal_support": {
            "bad_measure_upper": fstr(bad),
            "good_measure_lower": fstr(measure - bad),
        },
        "scalarization": {
            "epsilon_reconstructed": fstr(eps),
            "epsilon_upper": fstr(eps_claim),
        },
        "positive_route": {
            "d4_over_d8_upper": fstr(declared_ratio),
            "target_over_d8_upper": fstr(target_scaled),
            "gap_over_d8_lower": fstr(gap_scaled),
            "ground_ratio": fstr(ground_ratio),
        },
        "next_scale": {
            "gamma": next_gamma,
            "alias_upper": fstr(alias_upper(next_gamma)),
            "d4_over_d8_upper": fstr(mode_ratio_upper(next_gamma)),
        },
        "proof_boundary": (
            "The block binds an actual DIRECTED_INTERVAL_ODE source file. The alias and mode-hierarchy "
            "inequalities are imported by exact Git-blob identifiers and instantiated without redoing their proofs. "
            "The radial and frequency terms use the source primitive's exact unit-energy ceilings; this is conservative "
            "but sufficient for the cofinal scalarization and target/gap ratio."
        ),
    }
    result["proof_object_sha256"] = canonical_sha(result)
    claimed = payload.get("claimed_result_sha256")
    if claimed is not None and claimed != result["proof_object_sha256"]:
        raise CertificateError("claimed result digest mismatch")
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificate", type=Path)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    try:
        payload = json.loads(args.certificate.read_text())
        result = verify(payload, args.source)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError, KeyError) as exc:
        result = {"schema": RESULT_SCHEMA, "classification": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
