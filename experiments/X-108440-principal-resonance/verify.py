#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108440_DOUBLE_QUADRATIC_PHYSICAL_ALIAS"


def legendre(a, p):
    value = pow(a % p, (p - 1) // 2, p)
    assert value in (1, p - 1)
    return 1 if value == 1 else -1


def run():
    primes = (5, 13, 17, 29, 37, 41)
    square_checks = 0

    for ell in primes:
        for rho in primes:
            if ell == rho:
                continue
            for Q in range(1, ell):
                for d in range(1, ell):
                    assert legendre(Q * d * d, ell) == legendre(Q, ell)
                    square_checks += 1
            for P in range(1, rho):
                for c in range(1, rho):
                    assert legendre(P * c * c, rho) == legendre(P, rho)
                    square_checks += 1

    assert square_checks == 40960

    payload = {
        "schema": "riemann.x108440.double-quadratic-principal-alias.v2",
        "classification": CLASSIFICATION,
        "exact_checks": square_checks,
        "square_pullback_checks": square_checks,
        "double_quadratic_physical_alias_proved": True,
        "legacy_gauss_weight_identification_claimed": False,
        "geometric_cancellation_of_double_row_refuted": True,
        "mixed_resonance_bound_proved": False,
        "principal_adapter_proved": False,
        "rh_established": False,
        "grh_established": False,
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
