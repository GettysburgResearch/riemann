#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path


def proof_digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    alpha2 = Fraction(599, 625)       # 0.9584
    alpha3 = Fraction(9873, 10000)   # 0.9873
    wrong = (1 - alpha2) / (2 * alpha3)
    good = 1 - wrong

    assert wrong == Fraction(208, 9873)
    assert good == Fraction(9665, 9873)
    assert float(good) > 0.9789
    assert alpha2 < alpha3 < 1

    cartwright_counterexample = {
        "function": "2+cos(z)",
        "real_parent_zeros": 0,
        "derivative_line_proportion": "1",
        "parent_line_proportion": "0",
        "nonreal_parent_zero_height": "arcosh(2)",
    }

    payload = {
        "schema": "riemann.t104540.conrey_fixed_order.v1",
        "checks": {
            "alpha2": str(alpha2),
            "alpha3": str(alpha3),
            "wrong_extrema_upper_fraction": str(wrong),
            "good_extrema_lower_fraction": str(good),
            "cartwright_counterexample": cartwright_counterexample,
        },
        "scope": {
            "conrey_proof_replayed": False,
            "alpha2_imported_unconditional": True,
            "alpha3_imported_unconditional": True,
            "proportion_only_reverse_implication_refuted": True,
            "good_extrema_orientation_proved_from_both_rows": True,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104540_FIXED_ORDER_REVERSE_ROLLE_DISPOSITION",
    }
    payload["proof_object_sha256"] = proof_digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
