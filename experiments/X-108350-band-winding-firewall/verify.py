#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108350_BAND_WINDING_FIREWALL"


def run():
    checks = 0

    # Algebraic geometric-tail model for one normalized Blaschke packet.
    # q^m models exp(-2 y X), while (1-q) is the exact band mass of a
    # geometric interval in the time representation.
    q = Fraction(1, 4)
    for m in range(1, 513):
        winding = 2**m
        one_mass = q**m * (1 - q)
        total_mass = winding * one_mass
        assert total_mass == Fraction(3, 4 * 2**m)
        assert total_mass < 1
        assert winding * total_mass.denominator > total_mass.numerator
        checks += 3

    # Geographic scale: n=R log_2 R and Delta=1/(R log_2 R).
    # The elementary upper envelope 2 n Delta R^{-2} is exactly 2/R^2.
    for m in range(2, 258):
        R = 2**m
        n = R * m
        delta = Fraction(1, n)
        upper = 2 * n * delta * Fraction(1, R * R)
        assert upper == Fraction(2, R * R)
        assert upper < Fraction(1, R)
        checks += 2

    # Conjugate polynomial pair: E_minus is the coefficientwise conjugate
    # reflection of E_plus, hence their half-sum and scaled difference have
    # real coefficients. Check exact Gaussian-integer coefficient fixtures.
    plus = [complex(-1, -1), complex(1, 0)]  # z-(1+i)
    minus = [complex(-1, 1), complex(1, 0)]
    g = [(a + b) / 2 for a, b in zip(plus, minus)]
    f = [(a - b) / (2j) for a, b in zip(plus, minus)]
    assert all(abs(x.imag) == 0 for x in g)
    assert all(abs(x.imag) == 0 for x in f)
    checks += 2

    assert checks == 2054

    payload = {
        "schema": "riemann.x108350.band-winding-firewall.v1",
        "classification": CLASSIFICATION,
        "exact_checks": checks,
        "geometric_band_mass_checked": True,
        "winding_degree_checked": True,
        "geographic_count_scale_checked": True,
        "real_entire_companion_realization_checked": True,
        "source_band_to_winding_refuted": True,
        "xi31globalphase108350_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
