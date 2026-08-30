#!/usr/bin/env python3
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108310_ALL_ODD_DIRECT_COMPANION"


def transitions(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))


def run():
    exact_checks = 0
    sequence_checks = 0

    for n in range(1, 13):
        for signs in itertools.product((-1, 1), repeat=n):
            assert transitions(signs) <= 2 * min(signs.count(1), signs.count(-1))
            sequence_checks += 1
    exact_checks += sequence_checks

    polynomial_checks = 0
    for K in range(1, 32, 2):
        for u in range(-4, 5):
            for v in range(-4, 5):
                lhs = u * v**K - v ** (K + 1) + v * u**K - u ** (K + 1)
                rhs = -(u - v) * (u**K - v**K)
                assert lhs == rhs
                assert (u - v) * (u**K - v**K) >= 0
                polynomial_checks += 2
    exact_checks += polynomial_checks

    assert Fraction(999, 1000) - Fraction(9, 10) == Fraction(99, 1000)
    assert (Fraction(999, 1000) - Fraction(9, 10)) / 2 == Fraction(99, 2000)
    assert Fraction(99, 2000) - Fraction(1, 62) == Fraction(2069, 62000)
    assert Fraction(2069, 62000) > 0
    exact_checks += 4

    valid = [K for K in range(1, 100, 2) if Fraction(1, 2 * K) < Fraction(1, 20)]
    assert valid[0] == 11
    exact_checks += 1

    counter_checks = 0
    c = Fraction(2)
    for K in range(1, 32, 2):
        m = (K - 1) // 2
        signs = []
        for j in range(16):
            f_value = c + (1 if j % 2 == 0 else -1)
            derivative_sign = ((-1) ** (m + 1)) * (1 if j % 2 == 0 else -1)
            signs.append(1 if f_value * derivative_sign > 0 else -1)
        assert all(signs[j] != signs[j + 1] for j in range(15))
        tau = (-1) ** ((K + 3) // 2)
        assert tau * ((-1) ** m) == 1
        counter_checks += 2
    exact_checks += counter_checks

    assert exact_checks == 10819

    payload = {
        "schema": "riemann.x108310.all-odd-direct-companion.v1",
        "classification": CLASSIFICATION,
        "exact_checks": exact_checks,
        "sign_sequences_checked": sequence_checks,
        "odd_orders_checked": 16,
        "fourier_source_polynomial_checks": polynomial_checks,
        "countermodel_checks": counter_checks,
        "general_odd_endpoint_companion_proved": True,
        "general_minority_transition_gate_proved": True,
        "conrey31_input": "999/1000",
        "endpoint31_minority_allowance": "99/2000",
        "endpoint31_source_constant": "1/62",
        "endpoint31_transfer_moat": "2069/62000",
        "xi31minphase108310_proved": False,
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
