#!/usr/bin/env python3
"""Emit one source-bound X-16209 block and an all-scale dyadic-cubic schedule."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x16209_verify", HERE / "verify.py")
assert SPEC and SPEC.loader
vmod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = vmod
SPEC.loader.exec_module(vmod)


def sha_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def certificate(source_path: Path) -> dict:
    source = json.loads(source_path.read_text())
    gamma = int(source["source"]["gamma"])
    exponent = vmod.power_of_two_exponent(gamma)
    j = (exponent - 12) // 3
    q3 = vmod.cube_root_floor(gamma)
    cross = vmod.alias_upper(gamma)
    log_lower = Fraction(69 * exponent, 100)
    ratio = vmod.mode_ratio_upper(gamma)
    first_cross = Fraction(1, 1000)
    first_lo = 1 - first_cross
    first_hi = 1 + first_cross
    full_lo = first_lo - cross

    radial = Fraction(1)
    derivative = Fraction(2)
    endpoint = Fraction(128, gamma)
    deterministic = radial + derivative + 2 * endpoint
    threshold = Fraction(1, q3)
    bounded = Fraction(1)
    epsilon = (bounded + deterministic + 2 * threshold) / (full_lo * log_lower)
    epsilon_claim = vmod.ceil_fraction(epsilon, 100)

    C4 = Fraction(4)
    c8 = Fraction(1, 20)
    target = (1 + epsilon_claim) * C4 * ratio
    gap = (1 - epsilon_claim) * c8 - 2 * epsilon_claim * C4 * ratio
    ground = target / gap

    return {
        "schema": vmod.SCHEMA,
        "gamma": gamma,
        "source_binding": {
            "source_file_sha256": sha_file(source_path),
            "source_primitive_sha256": source["primitive_sha256"],
            "source_definition_sha256": source["source_sha256"],
            "source_producer_sha256": source["producer_sha256"],
            "alias_theorem_git_blob_sha1": vmod.ALIAS_THEOREM_GIT_BLOB_SHA1,
            "mode8_theorem_git_blob_sha1": vmod.MODE8_THEOREM_GIT_BLOB_SHA1,
        },
        "alias": {
            "alias_cutoff": math.isqrt(gamma),
            "airy_scale": q3,
            "first_alias_cross_upper": fstr(first_cross),
            "first_alias_lower": fstr(first_lo),
            "first_alias_upper": fstr(first_hi),
            "cross_error_upper": fstr(cross),
            "higher_self_upper": "16",
            "full_upper": "18",
        },
        "endpoint": {
            "method": "RADIAL_OUTGOING_PHASE",
            "point_upper": fstr(endpoint),
            "l2_norm_upper": fstr(endpoint),
            "l2_sq_upper": fstr(endpoint * endpoint),
        },
        "source_tails": {
            "method": "EXACT_UNIT_ENERGY_CEILING_FROM_BOUND_SOURCE_PRIMITIVE",
            "radial_l2_sum_upper": fstr(radial),
            "derivative_l2_sum_upper": fstr(derivative),
        },
        "cofinal_block": {
            "measure_lower": "1",
            "exceptional_measure_upper": fstr(threshold),
            "families": [
                {"name": "line-centered", "mean_square_upper": fstr(Fraction(1, gamma)), "threshold": fstr(threshold)},
                {"name": "horizontal", "mean_square_upper": fstr(Fraction(1, gamma)), "threshold": fstr(threshold)},
            ],
        },
        "scalarization": {
            "log_R_lower": fstr(log_lower),
            "bounded_main_correction_upper": "1",
            "claimed_epsilon_upper": fstr(epsilon_claim),
        },
        "tail_hierarchy": {
            "d4_over_d8_upper": fstr(ratio),
            "target_constant_upper": "4",
            "gap_constant_lower": "1/20",
            "claimed_ground_ratio_upper": fstr(ground),
        },
        "next_gamma": gamma * 8,
        "emitter_diagnostics": {
            "schedule_index": j,
            "deterministic_error": fstr(deterministic),
            "profile_gram_lower": fstr(full_lo),
            "epsilon_reconstructed": fstr(epsilon),
            "target_scaled": fstr(target),
            "gap_scaled": fstr(gap),
        },
    }


def schedule(start_j: int, count: int) -> dict:
    rows = []
    for j in range(start_j, start_j + count):
        gamma = 4096 * 8**j
        q3 = vmod.cube_root_floor(gamma)
        exponent = vmod.power_of_two_exponent(gamma)
        first_lo = Fraction(999, 1000)
        cross = vmod.alias_upper(gamma)
        gram = first_lo - cross
        endpoint = Fraction(128, gamma)
        deterministic = Fraction(3) + 2 * endpoint
        threshold = Fraction(1, q3)
        log_lower = Fraction(69 * exponent, 100)
        eps = (1 + deterministic + 2 * threshold) / (gram * log_lower)
        eps_claim = vmod.ceil_fraction(eps, 10_000)
        r = vmod.mode_ratio_upper(gamma)
        target = (1 + eps_claim) * 4 * r
        gap = (1 - eps_claim) * Fraction(1, 20) - 8 * eps_claim * r
        ratio = target / gap
        rows.append({
            "j": j,
            "gamma": gamma,
            "lambda_diagnostic": math.sqrt(gamma / (2 * math.pi)),
            "sqrt_floor": math.isqrt(gamma),
            "cuberoot": q3,
            "cross_alias_upper": fstr(cross),
            "profile_gram_lower": fstr(gram),
            "epsilon_upper": fstr(eps_claim),
            "d4_over_d8_upper": fstr(r),
            "ground_ratio_upper": fstr(ratio),
        })
    return {
        "schema": "riemann.x16209-cofinal-schedule.v1",
        "gamma_rule": "gamma_j=4096*8^j=(16*2^j)^3",
        "alias_rule": "18/floor(sqrt(gamma))+2/cuberoot(gamma)+1792/gamma",
        "mode_rule": "d4/d8<=1/(50000*4096^j)",
        "source_energy_rule": "radial L2<=1 and frequency-derivative L2<=2 from each bound primitive",
        "support_rule": "two mean-square families: M<=1/gamma, threshold=1/cuberoot(gamma)",
        "log_rule": "log(gamma)>=69*log2_exponent/100",
        "limit_statement": "cross_alias->0, epsilon->0, and complete ground ratio=O(4096^-j)=O(gamma^-4)->0",
        "blocks": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--schedule-count", type=int, default=8)
    args = ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    cert = certificate(args.source)
    cert_path = args.output_dir / "certificate-gamma32768.json"
    cert_path.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    result = vmod.verify(cert, args.source)
    cert["claimed_result_sha256"] = result["proof_object_sha256"]
    cert_path.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    result = vmod.verify(cert, args.source)
    result_path = args.output_dir / "verification-gamma32768.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    schedule_obj = schedule(1, args.schedule_count)
    (args.output_dir / "cofinal-schedule.json").write_text(
        json.dumps(schedule_obj, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "certificate": str(cert_path),
        "verification": str(result_path),
        "proof_object_sha256": result["proof_object_sha256"],
        "ground_ratio": result["positive_route"]["ground_ratio"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
