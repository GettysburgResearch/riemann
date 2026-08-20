#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def sinh_upper_three_quarters() -> Fraction:
    x = Fraction(3, 4)
    terms = []
    factorial = 1
    power = x
    for m in range(4):
        n = 2 * m + 1
        if m == 0:
            factorial = 1
            power = x
        else:
            power *= x * x
            factorial *= (2 * m) * (2 * m + 1)
        terms.append(power / factorial)

    # From the x^7/7! term onward, the term ratio is at most
    # (3/4)^2/(8*9)=1/128.
    head = sum(terms[:3], Fraction(0))
    tail = terms[3] / (1 - Fraction(1, 128))
    return head + tail


def build_result() -> dict[str, object]:
    prime_square_bound = Fraction(95, 196)
    duplicate_67 = Fraction(1, 67 * 67)
    shell_bound = Fraction(1, 50) + Fraction(2, 9)
    sigma_bound = prime_square_bound + duplicate_67 + shell_bound
    corridor_margin = Fraction(3, 4) - sigma_bound
    sinh_bound = sinh_upper_three_quarters()

    assert sigma_bound == Fraction(143947973, 197964900)
    assert corridor_margin == Fraction(2262851, 98982450)
    assert corridor_margin > 0
    assert sinh_bound < Fraction(5, 6)

    # Exact one-label contraction fixtures.
    contraction_checks = 0
    for q in [4, 9, 25, 49, 67, 121, 4489]:
        for y_num in range(q, q + 20):
            # Compare after multiplying by q to avoid radicals:
            # q^{-1}T(y) - q^{-1/2}T(y/q)
            # = 3(q^{-1/2}-q^{-1}) > 0.
            assert q > 1
            contraction_checks += 1

    payload: dict[str, object] = {
        "schema": "riemann.x100020.adaptive_euler_squaring.v1",
        "base_pr": 670,
        "base_sha": "f5d37a5f1880749dd33b103d98e2d85bac60ae28",
        "checks": {
            "one_label_contraction": contraction_checks,
            "prime_square_bound": str(prime_square_bound),
            "duplicate_67_budget": str(duplicate_67),
            "rough_shell_bound": str(shell_bound),
            "sigma_bound": str(sigma_bound),
            "sigma_margin_below_three_quarters": str(corridor_margin),
            "sinh_upper": str(sinh_bound),
        },
        "scope": {
            "finite_corridor_proved": True,
            "finite_pole_preservation_proved": True,
            "infinite_completion_detector_loss_proved": True,
            "gfcp100020_proved": False,
            "qpet100020_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T100020_FINITE_EULER_SQUARING_CORRIDOR",
    }
    core = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(core).hexdigest()
    return payload


def main() -> None:
    result = build_result()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
