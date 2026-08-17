#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json

def det2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def mul2(A, B):
    return [
        [sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    H_swap = [[Fraction(0), Fraction(1)],
              [Fraction(1), Fraction(0)]]
    K_bad = [[Fraction(1), Fraction(2)],
             [Fraction(2), Fraction(1)]]
    I = [[Fraction(1), Fraction(0)],
         [Fraction(0), Fraction(1)]]

    assert det2(H_swap) == -1
    assert det2(K_bad) == -3
    assert det2(mul2(I, K_bad)) == -3

    H_good = [[Fraction(1), Fraction(0)],
              [Fraction(1), Fraction(1)]]
    K_good = [[Fraction(2), Fraction(1)],
              [Fraction(1), Fraction(1)]]
    assert det2(H_good) == 1
    assert det2(K_good) == 1
    assert det2(mul2(H_good, K_good)) == 1

    greedy = Fraction(3) + Fraction(1, 2) * Fraction(2)
    assert greedy == 4

    result = {
        "classification": "PASS_T97210_CHECKERBOARD_RECONCILIATION",
        "unique_owner_negative_minor": str(det2(H_swap)),
        "positive_leaf_negative_minor": str(det2(K_bad)),
        "cauchy_binet_negative_control": str(det2(mul2(I, K_bad))),
        "compatible_positive_fixture": str(det2(mul2(H_good, K_good))),
        "fractional_knapsack_fixture": str(greedy),
        "terminal_checkerboard_proved": False,
        "owner_incidence_TN_proved": False,
        "GPHT_star_proved": False,
        "RH_established": False,
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__ == "__main__":
    main()
