#!/usr/bin/env python3
"""Exact finite controls for HC1--HC28; no native primitive replay.

The analytic theorem, complete product, count imports, harmonic measure and
the former native receipt remain separately qualified dependencies. Checking
their hashes and metadata does not authenticate their mathematical premises.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
WAVE = HERE.parents[1]


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "harmonic_column_constants.json")
    args = parser.parse_args()
    guards: list[str] = []

    def check(condition: bool, name: str) -> None:
        need(condition, name)
        guards.append(name)

    candidates = json.loads((HERE / "native_candidates.json").read_text())
    receipt = json.loads((HERE / "native_slab_certificate.json").read_text())
    check(candidates["status"] == "CANDIDATES_ONLY_NOT_A_ZERO_CENSUS", "candidate status remains qualified")
    check(receipt["status"] == "PASS_DIRECTED_NATIVE_COMPANION_SLAB", "named prior receipt status")
    check(receipt["actual_primitive_endpoints_replayed"] is True, "named prior replay metadata")
    check(receipt["complete_census_height"] == candidates["height"] == 8192, "prior census height")
    check(receipt["imported_complete_count"] == receipt["replayed_disjoint_sign_crossing_brackets"] == 8049,
          "prior receipt imported count and bracket metadata")
    check(receipt["historical_Gram_Rosser_verification_replayed"] is False,
          "historical finite verification remains imported")
    for relative, expected in receipt["source_sha256"].items():
        check(digest(WAVE / relative) == expected, f"prior receipt direct-source hash: {relative}")
    denominator = candidates["denominator"]
    brackets = candidates["interval_numerators"]
    check(type(denominator) is int and denominator == 2**24, "exact candidate denominator")
    check(len(brackets) == candidates["candidate_count"] == 8049, "exact candidate count")
    previous = 0
    for lo, hi in brackets:
        need(type(lo) is int and type(hi) is int, "integer bracket endpoints")
        need(previous < lo < hi < 8192 * denominator, "disjoint ordered finite brackets")
        need(lo > 14 * denominator, "every native candidate bracket above fourteen")
        previous = hi
    guards.append("all 8049 exact bracket ordering/height/lower guards")
    check(brackets[0][1] < 15 * denominator, "first accepted candidate bracket below fifteen")

    R, A, V, C, L = Q(8192), Q(1, 2), Q(8191), Q(16383, 2), Q(32697, 4)
    check(C == R - A and V == R - 2 * A, "complete-census protected widths")
    check(Q(8174) < L < V, "strict neighborhood of the claimed column")
    jensen = Q(21, 20480) + Q(4103, 4096) * Q(49, 40)
    check(jensen == Q(201215, 163840) < Q(4, 3), "uniform polynomial companion Jensen coefficient")
    check(2 * V + 1 < 2**14, "near companion zero radius")
    near_count = 2 * 2**14 * 14
    check(near_count == 458752, "near complete companion count")
    check(C - V == A and near_count / A == 917504, "near negative logarithmic derivative budget")
    check(Q(60, 2 * V) < 1, "complete far companion inverse-square tail")
    check(near_count / A + 8 * A < 2**20, "uniform full companion lower harmonic bound")
    check(2 * 8049 == 16098, "complete finite Cauchy--Schwarz factor")
    check(V > 3 * R / 4 and R - V == 1, "complete actual tail geometry")
    check(56 * V * R / (R**2 - V**2) < 2**18, "complete actual tail logarithmic derivative bound")
    check(2 * 16098 == 32196 < 2**15 and 100 < 2**7, "real-boundary denominator constants")
    check(V + 15 < 2**14, "first pair uniform real-boundary derivative lower bound")
    check(Q(1) + Q(1, 32) + 2**44 < 2**45, "uniform bottom value exceeds two to minus seventy-two")
    check(2**27 + 3219600 + 100 * 2**64 < 2**72,
          "independent reciprocal bottom-bound guard")
    check(Q(2**20) + Q(1, 2**72) < 2**21 and 6 * 2**21 < 2**24,
          "vertical harmonic measure multiplier")
    check(2 * 3 * (V - L) > 100 > 98, "strict full-column exponential domination")

    sources = [
        HERE / "HARMONIC_COLUMN_TRANSPORT.md", Path(__file__).resolve(),
        HERE / "THEOREM.md", HERE / "CENSUS_LOCALIZATION.md",
        HERE / "NATIVE_SLAB_CERTIFICATE.md", HERE / "native_candidates.json",
        HERE / "native_slab_certificate.json", WAVE / "heights/COARSE_ZERO_COUNT.md",
    ]
    result = {
        "status": "PASS_HARMONIC_COLUMN_EXACT_CONSTANTS",
        "scope": "finite rational controls for analytic HC1-HC28; premises separately qualified",
        "normalization": "Xi(z)=xi(1/2+i*z)",
        "derivative_order": 0, "lambda_interval": [1, 10],
        "claimed_real_part_bound": 8174, "lower_depth_unbounded": True,
        "rh_proved": False, "primitive_zeta_values_replayed_by_this_checker": False,
        "analytic_or_count_premises_authenticated_by_this_checker": False,
        "prior_native_receipt_imported_with_its_stated_count_scope": True,
        "historical_Gram_Rosser_verification_replayed": False,
        "guard_count": len(guards), "exact_guards": guards,
        "source_sha256": {str(p.relative_to(WAVE)): digest(p) for p in sources},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["status"], "GUARDS", len(guards))


if __name__ == "__main__":
    main()
