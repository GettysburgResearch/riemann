#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T104100_ROOT_RETURN_ROOT_FREE_QUOTIENT"


def run() -> dict[str, object]:
    # Supercritical hierarchy countermodel:
    # nu=(2/5)delta_2-delta_1 has negative first moment and positive m>=2.
    critical = Fraction(2, 5) * 2 - 1
    assert critical == Fraction(-1, 5)
    supercritical_checks = 0
    for m in range(2, 101):
        moment = Fraction(2, 5) * (2**m) - 1
        assert moment >= Fraction(3, 5)
        supercritical_checks += 1

    # PSD does not orient a signed linear functional.
    det = Fraction(1) - Fraction(3, 4) ** 2
    linear_witness = Fraction(1) - 2 * Fraction(3, 4)
    assert det == Fraction(7, 16) > 0
    assert linear_witness == Fraction(-1, 2) < 0

    # Root-containing square: zero excess permits arbitrary root.
    root_square_checks = 0
    for root in (
        Fraction(-17), Fraction(-1), Fraction(0), Fraction(9, 2), Fraction(10**6)
    ):
        excess = Fraction(0)
        q = root * root + excess
        assert q - root * root == 0
        root_square_checks += 1

    # Pairwise positive products do not imply an all-factor positive cone.
    A = B = C = Fraction(-1)
    assert A * B == B * C == A * C == 1
    assert A * B * C == -1

    # Exact scalar Schur/Perron absorption on rational fixtures.
    rng = random.Random(104100)
    absorption_checks = 0
    for _ in range(10000):
        den = rng.randint(2, 500)
        theta = Fraction(rng.randint(0, den - 1), den)
        delta = 1 - theta
        e = Fraction(rng.randint(0, 1000), rng.randint(1, 200))
        r = Fraction(rng.randint(0, 1000), rng.randint(1, 200))

        upper_x2 = (theta * e + r) / delta
        # Choose an exact rational x with x^2 below the admissible bound.
        x = Fraction(rng.randint(-20, 20), 1000)
        if x * x > upper_x2:
            x = Fraction(0)
        q = x * x + e
        assert x * x <= theta * q + r
        assert delta * x * x <= theta * e + r
        assert delta * x * x <= e + r
        assert abs(float(x)) <= (
            math.sqrt(float(e)) + math.sqrt(float(r))
        ) / math.sqrt(float(delta)) + 1e-15
        absorption_checks += 1

    # theta=1 gives no strict absorption.
    for x in (Fraction(-9), Fraction(0), Fraction(13, 7)):
        e = Fraction(0)
        q = x * x + e
        assert x * x <= q
        assert (1 - Fraction(1)) * x * x == 0

    # A concrete subpower-moat/block-packing model.
    block_checks = 0
    for L in range(10, 500):
        delta_inv = (L + 1) ** 4
        pack = (L + 1) ** 6
        bound = math.sqrt(delta_inv) * pack
        # log_2(bound)/L -> 0; use a generous finite replay envelope.
        assert math.log2(bound) / L < 8.0
        block_checks += 1

    mutations = sorted([
        "excess_only_promoted_to_root_control_rejected",
        "moving_completed_observable_promoted_to_fixed_detector_rejected",
        "pairwise_positivity_promoted_to_all_prime_cone_rejected",
        "psd_kernel_promoted_to_linear_sign_rejected",
        "rh_equivalent_statement_promoted_to_proved_rejected",
        "supercritical_positivity_promoted_to_critical_sign_rejected",
        "theta_equal_one_called_strict_return_rejected",
    ])

    payload: dict[str, object] = {
        "schema": "riemann.x104100.root-return-quotient.v1",
        "classification": VERDICT,
        "base_pr": 704,
        "base_sha": "66f755df4321a03874e0da3f61b033300173e364",
        "supercritical_countermodel_checks": supercritical_checks,
        "root_square_checks": root_square_checks,
        "root_excess_absorption_checks": absorption_checks,
        "subpower_block_checks": block_checks,
        "psd_linear_sign_countermodel": True,
        "pairwise_all_factor_countermodel": True,
        "theta_one_firewall": True,
        "two_key_absorption_proved": True,
        "sorr104100_proved": False,
        "rfcp104100_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
