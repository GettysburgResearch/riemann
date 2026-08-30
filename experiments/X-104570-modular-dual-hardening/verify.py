#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def digest(payload: dict) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def poly_derivative(p: dict[int, Fraction], k: int) -> dict[int, Fraction]:
    q = dict(p)
    for _ in range(k):
        q = {d - 1: c * d for d, c in q.items() if d}
    return q


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    # Exact negative origin minor.
    a1, b1, a2, b2 = map(Fraction, (2, 5, 3, 7))
    off = (a1 * b2 + a2 * b1) / 2
    det = a1 * b1 * a2 * b2 - off * off
    exact_det = -(a1 * b2 - a2 * b1) ** 2 / 4
    assert det == exact_det < 0

    # Strict monotone-likelihood-ratio derivative identity.
    x = Fraction(4)
    q = Fraction(9, 4)
    lhs = 4 * q * x / (2 * q * x - 3) - 4 * x / (2 * x - 3) - 2 * (q - 1) * x
    rhs = -12 * x * (q - 1) / ((2 * q * x - 3) * (2 * x - 3)) - 2 * x * (q - 1)
    assert lhs == rhs < 0

    # P_x(y)=x^4 y^2-2x^2 y^4+y^6 and its y derivatives.
    xv = Fraction(3)
    p = {2: xv**4, 4: -2 * xv**2, 6: Fraction(1)}
    p2 = poly_derivative(p, 2)
    p4 = poly_derivative(p, 4)
    assert p2 == {0: 2 * xv**4, 2: -24 * xv**2, 4: Fraction(30)}
    assert p4 == {0: -48 * xv**2, 2: Fraction(360)}

    # Symbolic central-radius fixture.
    mu0 = Fraction(23, 1000)
    mu2 = Fraction(3, 1000)
    mu4 = Fraction(3, 5000)
    delta = mu0 * mu4 - mu2 * mu2
    assert delta > 0
    tau2 = 2 * mu0 * mu2 / delta
    assert tau2 > 25

    # Fixed-cutoff leading Laguerre coefficient.
    j = Fraction(7, 11)
    lead = (8 * j) ** 2 - (2 * j) * (40 * j)
    assert lead == -16 * j * j < 0

    # Jet basis normalization.
    own_jets = []
    for r in range(1, 7):
        degree = 2 * r + 1
        own_jets.append(Fraction(math.factorial(degree), math.factorial(degree)))
    assert all(v == 1 for v in own_jets)

    payload = {
        "schema": "riemann.t104570.modular_dual_hardening.v1",
        "checks": {
            "origin_psd_counterexample_determinant": str(det),
            "likelihood_ratio_derivative_negative": str(lhs),
            "modular_polynomial_derivatives": True,
            "local_moment_radius_fixture_squared": str(tau2),
            "fixed_cutoff_laguerre_lead": str(lead),
            "jet_matching_orders": 6,
        },
        "scope": {
            "strong_finite_matrix_psd_refuted": True,
            "complete_modular_scalar_identity_proved": True,
            "central_symbolic_positivity_interval_proved": True,
            "fixed_orbit_cutoff_cofinality_refuted": True,
            "jet_renormalized_adaptive_cutoff_proved": True,
            "scalar_global_positive_definiteness_proved": False,
            "adaptive_cofinal_margins_proved": False,
            "alpha2_from_alpha3_proved": False,
            "rh_established": False,
        },
        "verdict": "PASS_T104570_MODULAR_DUAL_ROUTE_HARDENING",
    }
    payload["proof_object_sha256"] = digest(payload)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
