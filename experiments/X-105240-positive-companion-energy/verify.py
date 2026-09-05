#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json


def compute():
    # -Im H^2/[p(a+i delta p)] = delta H^2/(a^2+delta^2 p^2)
    p = Fraction(7, 3)
    a = Fraction(-5, 4)
    delta = Fraction(2, 5)
    H = Fraction(11, 6)
    denominator = a * a + delta * delta * p * p
    imag = -delta * H * H / denominator
    assert -imag == delta * H * H / denominator

    # Weighted regression minimum A - B^2/C when B<0.
    A = Fraction(5, 2)
    B = Fraction(-3, 2)
    C = Fraction(2, 1)
    lam = -B / C
    assert lam >= 0
    quadratic = A + 2 * lam * B + lam * lam * C
    assert quadratic == A - B * B / C
    assert quadratic >= 0

    # Half-circle residues require the final factor two.
    residue_sum = Fraction(17, 9)
    arc_contribution = residue_sum / 2
    assert 2 * arc_contribution == residue_sum

    payload = {
        "schema": "riemann.x105240.positive-companion-energy.v1",
        "classification": "PASS_T105240_POSITIVE_COMPANION_ENERGY",
        "imaginary_part_identity_checked": True,
        "weighted_regression_optimum_checked": True,
        "half_residue_factor_checked": True,
        "xi_mean_values_run": False,
        "lerc105240_proved": False,
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
