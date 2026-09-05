#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext

getcontext().prec = 100


def compute() -> dict:
    H0_lo = Decimal("0.67250070367941164")
    H0_hi = Decimal("0.67250070367941166")

    m = Decimal(280)
    q = Decimal(19) * (m - Decimal(6)) / Decimal(5000)
    transition = m / (m - Decimal(1))
    assert q == Decimal(2603) / Decimal(2500)
    assert transition < q < Decimal(2)

    c = (
        Decimal(2)
        * (q * Decimal(279) / Decimal(280)).sqrt()
        - Decimal(1)
        + q / Decimal(280)
    )
    c_alt = (
        Decimal(2)
        * (Decimal(726237) / Decimal(700000)).sqrt()
        - Decimal(1)
        + Decimal(2603) / Decimal(700000)
    )
    assert c == c_alt
    assert Decimal(1) < c < q
    assert c < Decimal(2) * Decimal(2).sqrt() - Decimal(1)

    a = c / m
    span = Decimal(279) / Decimal(140000)
    new_lo = (H0_lo - span) / (Decimal(1) - a)
    new_hi = (H0_hi - span) / (Decimal(1) - a)

    old_lo = (
        Decimal(1345000) * H0_lo - Decimal(2680)
    ) / Decimal(1340003)
    old_hi = (
        Decimal(1345000) * H0_hi - Decimal(2680)
    ) / Decimal(1340003)

    assert new_lo > Decimal("0.67300965")
    assert new_lo > old_hi
    assert new_lo > Decimal(2) / Decimal(3)

    # Hostile controls.
    q_269 = Decimal(19) * (Decimal(269) - Decimal(6)) / Decimal(5000)
    assert q_269 == Decimal(4997) / Decimal(5000)
    assert q_269 < Decimal(1) < q

    wrong_unit_cap = Decimal(1)
    wrong_a = wrong_unit_cap / m
    wrong_bound = (H0_lo - span) / (Decimal(1) - wrong_a)
    assert wrong_bound < new_lo

    wrong_span = Decimal(280) / Decimal(140000)
    wrong_span_bound = (H0_lo - wrong_span) / (Decimal(1) - a)
    assert wrong_span_bound < new_lo

    payload = {
        "schema": "riemann.x106550.280-pressure.v1",
        "classification": "PASS_T106550_280_POINT_SPECTRAL_PRESSURE_LIFT",
        "H0_interval": [str(H0_lo), str(H0_hi)],
        "block_size": 280,
        "local_pressure": str(q),
        "spectral_transition": str(transition),
        "spectral_defect_c280": str(c),
        "global_span_coefficient": str(span),
        "new_record_interval": [str(new_lo), str(new_hi)],
        "old_record_interval": [str(old_lo), str(old_hi)],
        "strict_improvement": True,
        "record_exceeds_0_67300965": True,
        "external_arb_certificate_replayed": False,
        "ninety_percent_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    payload = compute()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
