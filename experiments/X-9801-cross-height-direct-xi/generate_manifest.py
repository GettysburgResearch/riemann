#!/usr/bin/env python3
"""Generate the exact small-integer symmetric-height X-9801 candidate manifest."""
from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x9801_verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


def fj(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def encoded_component(value: int) -> str:
    if value < 0:
        return f"m{-value}"
    return f"p{value}"


def main() -> int:
    origin = Fraction(20225875608341108140435, 2**32)
    half_step = Fraction(5, 16)
    center = (-2, 3, -1)
    candidates = []
    for k in (10, 12, 14, 16, 18, 20):
        side_vectors = [(-3, 0, 3), (-2, -1, 3)]
        if k >= 12:
            side_vectors.append((-1, -2, 3))
        for side in side_vectors:
            point_ids = [f"x-{k}", "x-6", "x-5"]
            heights = []
            for identifier, ordinate in (
                ("minus", origin - half_step),
                ("center", origin),
                ("plus", origin + half_step),
            ):
                heights.append(
                    {
                        "id": identifier,
                        "ordinate": fj(ordinate),
                        "common_xi_scale_power_of_two": 0,
                        "points": [
                            {
                                "id": point_id,
                                "u": fj(
                                    Fraction(
                                        1,
                                        2
                                        ** (
                                            2
                                            * int(point_id.split("-")[1])
                                        ),
                                    )
                                ),
                                "h_interval": {
                                    "lower": fj(Fraction(1)),
                                    "upper": fj(Fraction(1)),
                                },
                            }
                            for point_id in point_ids
                        ],
                    }
                )
            terms = []
            for identifier, exponents in (
                ("minus", side),
                ("center", center),
                ("plus", side),
            ):
                for point_id, exponent in zip(point_ids, exponents):
                    if exponent:
                        terms.append(
                            {
                                "height": identifier,
                                "point": point_id,
                                "exponent": exponent,
                            }
                        )
            certificate = {
                "schema": VERIFY.SCHEMA,
                "classification": VERIFY.SYNTHETIC,
                "normalization_id": VERIFY.NORMALIZATION,
                "origin": fj(origin),
                "heights": heights,
                "terms": terms,
                "polynomial_gate": {"status": VERIFY.POLYNOMIAL_GATE},
            }
            result = VERIFY.verify(certificate)
            if not result["polynomial"]["strictly_positive_on_real_line"]:
                raise RuntimeError("candidate failed its exact polynomial gate")
            candidate_id = (
                f"k{k}-s" + "".join(encoded_component(value) for value in side)
            )
            candidates.append(
                {
                    "id": candidate_id,
                    "description": (
                        f"symmetric heights T0+-5/16; nodes x=2^-{k},2^-6,2^-5; "
                        f"side exponents {list(side)}; center exponents {list(center)}"
                    ),
                    "point_ids": point_ids,
                    "side_exponents": list(side),
                    "center_exponents": list(center),
                    "response_degree": result["polynomial"]["degree"],
                    "distinct_real_roots": result["polynomial"][
                        "distinct_real_roots"
                    ],
                    "response_at_origin": result["polynomial"]["value_at_origin"],
                    "polynomial_proof_object_sha256": result["polynomial"][
                        "proof_object_sha256"
                    ],
                    "same_height_center_response_globally_valid": False,
                    "classification": (
                        "EXACT_POLYNOMIAL_CANDIDATE_UNEVALUATED_OR_EMPIRICAL"
                    ),
                }
            )
    manifest = {
        "schema": "riemann.x9801-symmetric-candidates.v1",
        "origin": fj(origin),
        "half_step": fj(half_step),
        "normalization_id": VERIFY.NORMALIZATION,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "proof_boundary": (
            "Every listed response polynomial was reconstructed with exact "
            "rational arithmetic and certified to have no real root and positive "
            "value at the origin. Direct Riemann-xi signs are separate and must "
            "be obtained from proof-grade primitive rectangles."
        ),
    }
    output = HERE / "candidates" / "symmetric-pr105.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"candidate_count": len(candidates), "path": str(output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
