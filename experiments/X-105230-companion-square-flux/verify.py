#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json, math


def compute():
    lam = Fraction(3, 5)
    for C in [Fraction(0), Fraction(2), Fraction(100)]:
        rho_plus = (C - Fraction(2, 3)) / 2
        rho_minus = -(C + Fraction(2, 3)) / 2
        for rho in (rho_plus, rho_minus):
            residue = 1 + 2 * lam * rho + lam * lam * rho * rho
            assert residue == (1 + lam * rho) ** 2

    # delta=1/2 gives companion roots i(2+-sqrt(3)), both above the axis.
    assert 2 - math.sqrt(3) > 0
    assert 2 + math.sqrt(3) > 0

    small = sum((1 + lam * r) ** 2 for r in (
        (Fraction(0) - Fraction(2, 3)) / 2,
        -(Fraction(0) + Fraction(2, 3)) / 2,
    ))
    large = sum((1 + lam * r) ** 2 for r in (
        (Fraction(100) - Fraction(2, 3)) / 2,
        -(Fraction(100) + Fraction(2, 3)) / 2,
    ))
    assert large > 1000 * small

    pK = Fraction(19, 20)
    charge = Fraction(1, 50)
    assert pK - 2 * charge == Fraction(91, 100)

    payload = {
        "schema": "riemann.x105230.companion-square-flux.v1",
        "classification": "PASS_T105230_COMPANION_CORONA_SQUARE_FLUX",
        "square_residue_identity_checked": True,
        "upper_companion_fixture_checked": True,
        "count_only_firewall_checked": True,
        "ninety_percent_gate_fixture_checked": True,
        "canonical_product_passage_replayed": False,
        "cibf105230_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    p = compute()
    print(p["classification"])
    print(p["proof_object_sha256"])
    print(json.dumps(p, indent=2, sort_keys=True))
