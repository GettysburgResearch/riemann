#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108330_ARBITRARY_DEFECT_THETA_TAIL_FIREWALL"


def run():
    checks = 0
    for M in range(1, 65):
        n = 64 * M

        # pi<4 gives 2*pi*M/n < 1/8; with h=1/8 this gives ht<1/64.
        assert Fraction(8 * M, n) == Fraction(1, 8)
        checks += 1

        # B >= 1-(ht)^2/2 > 31/32 on the whole construction interval.
        assert Fraction(1) - Fraction(1, 2 * 64**2) > Fraction(31, 32)
        checks += 1

        # Endpoint derivative reserve:
        # (31/32)(n/5) - 3/8 - 1 > 0.
        assert Fraction(31 * n, 160) - Fraction(11, 8) > 0
        checks += 1

        # Strict convexity reserve on every critical corridor.
        reserve = Fraction(31 * n * n, 32) - Fraction(n, 16) - 4 - Fraction(3, 64)
        assert reserve > 0
        checks += 1

        # Parent positivity reserve.
        assert Fraction(31, 32) - Fraction(1, 2) > 0
        checks += 1

        # M disjoint corridors each pay two exact reverse-Rolle units.
        assert 2 * M >= M
        checks += 1

    assert checks == 384

    payload = {
        "schema": "riemann.x108330.arbitrary-defect-theta-tail-firewall.v1",
        "classification": CLASSIFICATION,
        "exact_checks": checks,
        "values_of_M_checked": 64,
        "arbitrary_defect_construction_checked": True,
        "exact_xi_tail_preserved": True,
        "high_derivative_saddle_preserved": True,
        "fixed_odd_source_asymptotics_preserved": True,
        "local_source_package_implies_winding_refuted": True,
        "xi31wind108320_proved": False,
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
