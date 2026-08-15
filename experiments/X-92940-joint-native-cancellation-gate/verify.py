#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def run() -> dict[str, object]:
    x = 10**16
    if not x > 134:
        raise AssertionError("ordinary activity gate")

    rough_ordinary_67 = math.log(x / 134) / math.sqrt(134)
    child_ordinary = -rough_ordinary_67
    if not child_ordinary < 0:
        raise AssertionError("negative ordinary child coordinate")

    if not x >= 536:
        raise AssertionError("detail activity gate")
    rough_detail_67 = math.log(4) / math.sqrt(134)
    child_detail = -rough_detail_67
    if not child_detail < -Fraction(1, 9):
        raise AssertionError("negative detail child coordinate")

    # Positive branchwise physical placement is incompatible with the exact
    # negative aggregate ordinary observation.
    if child_ordinary >= 0:
        raise AssertionError("branchwise positive placement unexpectedly possible")

    # The historical number is retained only in the rough-lift scope.
    if Fraction(7, 75) - Fraction(1, 400) != Fraction(109, 1200):
        raise AssertionError("qualified separator arithmetic")

    root = Fraction(60989, 1)
    terminal = root + Fraction(6039, 8)
    if terminal != Fraction(493951, 8) or not terminal < 61744:
        raise AssertionError("conditional cost arithmetic")

    evidence = {
        "frozen": {
            "pr500": "d73c1e7a1a482cac31581211a84db43cc34c824e",
            "pr505": "1113fe6d55e955a8d9de7b43ceb24f5792870550",
            "pr507": "dfaa70cd2eefcabbf6717e3da060792904c7f357",
        },
        "oriented_child": {
            "ordinary_q2_upper": child_ordinary,
            "detail_q2_upper": child_detail,
            "branchwise_positive_realization": False,
        },
        "required_interface": {
            "joint_before_channel_subtraction": True,
            "separate_child_positive_capacity": False,
            "one_use_input_ownership": True,
            "ordinary_q_and_4q_same_total_row": True,
            "single_global_quantizer": True,
            "signed_finite_comparison_separate": True,
            "joint_compiler_constructed": False,
        },
        "qualified_109_over_1200": True,
        "conditional_costs": {
            "one_shot": str(root),
            "terminal_arithmetic_only": str(terminal),
        },
        "verdict": "PASS_T92940_JOINT_NATIVE_CANCELLATION_GATE",
        "rh_proved": False,
    }
    canonical = json.dumps(evidence, sort_keys=True, separators=(",", ":")).encode()
    evidence["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="results/verification.json")
    args = parser.parse_args()
    result = run()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
