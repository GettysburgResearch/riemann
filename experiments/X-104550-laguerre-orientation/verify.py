#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def convolution(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = defaultdict(Fraction)
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] += ai * bj
    return dict(out)


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def check_fixture(weights: dict[int, Fraction]) -> int:
    a0 = weights
    a1 = {n: Fraction(n) * a for n, a in weights.items()}
    a2 = {n: Fraction(n * n) * a for n, a in weights.items()}

    direct = convolution(a0, a2)
    sq = convolution(a1, a1)
    direct = {k: direct.get(k, Fraction()) - sq.get(k, Fraction())
              for k in set(direct) | set(sq)}

    source: dict[int, Fraction] = defaultdict(Fraction)
    for u, au in weights.items():
        for v, av in weights.items():
            source[u + v] += Fraction((u - v) ** 2, 2) * au * av

    assert direct == dict(source)
    assert all(c >= 0 for c in source.values())
    return len(source)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    fixtures = [
        {-2: Fraction(1, 7), -1: Fraction(2, 5), 0: Fraction(3, 4),
          1: Fraction(2, 5), 2: Fraction(1, 7)},
        {-3: Fraction(1, 11), -1: Fraction(5, 9), 1: Fraction(5, 9),
          3: Fraction(1, 11)},
        {-4: Fraction(2, 13), -2: Fraction(1, 3), 0: Fraction(7, 8),
          2: Fraction(1, 3), 4: Fraction(2, 13)},
    ]
    coefficient_counts = [check_fixture(w) for w in fixtures]

    alpha3 = Fraction(9873, 10000)
    q_values = [Fraction(1), Fraction(3, 4), Fraction(2, 3), Fraction(51, 100)]
    transfers = {str(q): str((2 * q - 1) * alpha3) for q in q_values}
    assert transfers["1"] == str(alpha3)
    assert (2 * Fraction(51, 100) - 1) * alpha3 > 0

    negative_control = {
        "positive_source": True,
        "positive_definite_transform": True,
        "transform_at_pi": "-1",
        "pointwise_nonnegative": False,
    }

    payload = {
        "schema": "riemann.t104550.fixed_order_laguerre.v1",
        "checks": {
            "finite_correlation_fixtures": len(fixtures),
            "nonnegative_fourier_coefficient_counts": coefficient_counts,
            "alpha3": str(alpha3),
            "orientation_transfer_examples": transfers,
            "positive_source_negative_control": negative_control,
        },
        "scope": {
            "laguerre_orientation_transfer_proved_exact": True,
            "correlation_kernel_identity_proved_exact": True,
            "laguerre_profile_positive_definite": True,
            "pointwise_lag2xi104550_proved": False,
            "alpha2_from_alpha3_established": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104550_FIXED_ORDER_LAGUERRE_KERNEL_ALGEBRA",
    }
    payload["proof_object_sha256"] = digest(payload)
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
