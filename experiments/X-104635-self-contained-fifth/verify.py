#!/usr/bin/env python3
"""Exact self-contained fifth-input and 90-percent ledger replay."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import argparse, hashlib, importlib.util, json

HERE = Path(__file__).resolve()
BASE = HERE.parents[1] / "X-104620-conrey-reconstruction" / "verify.py"


def load_base():
    spec = importlib.util.spec_from_file_location("x104620_verify", BASE)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", type=Path)
    args = ap.parse_args()

    mod = load_base()
    cert = mod.certificate(5, Q(0), Q(1, 50))
    assert cert["alpha_lower"] == "49/50"

    x = Q(13, 8)
    lower = sum(x**j / factorial(j) for j in range(6))
    assert lower == Q(19839493, 3932160)
    assert lower > 5

    current = Q(13, 500)
    metric = Q(1001, 1000)
    tail = Q(13, 4000)
    shallow = metric * current + tail
    assert shallow == Q(7319, 250000)
    assert shallow < Q(3, 100)

    deep = Q(1, 20)
    total = deep + shallow
    assert total == Q(19819, 250000)
    assert total < Q(2, 25)

    base = Q(49, 50) - total
    assert base == Q(225181, 250000)
    assert base > Q(9, 10)

    result = {
        "schema": "riemann.t104635.self_contained_fifth.v1",
        "verdict": "PASS_T104635_SELF_CONTAINED_FIFTH_LEDGER",
        "checks": {
            "alpha5_lower": "49/50",
            "deep_charge": "1/20",
            "fractional_current_gate": "13/500",
            "fractional_tail": "13/4000",
            "shallow_upper": str(shallow),
            "total_charge": str(total),
            "alpha0_lower": str(base),
            "margin_over_90": "181/250000",
            "conrey_certificate": cert,
        },
        "scope": {
            "alpha5_exact_certificate": True,
            "self_contained_90_ledger": True,
            "fractrans104635_proved": False,
            "ninety_percent_established": False,
            "rh_established": False,
        },
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
