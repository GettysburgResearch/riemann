#!/usr/bin/env python3
"""Directed counterexample to the atom-one odd-prefix shortcut at quotient 23."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json

from verify_quotient22 import (
    ODD_SOURCES,
    PREC,
    ROUND_HALF_EVEN,
    build_coefficients,
    invsqrt_interval,
    localcontext,
    q_interval,
)


def main() -> None:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_HALF_EVEN
        j = 44
        x = 1012
        c_values, d_values = build_coefficients(j)
        value = q_interval(x, 1, j, c_values, d_values)
        for divisor in ODD_SOURCES:
            value -= invsqrt_interval(divisor) * q_interval(
                x, divisor, j, c_values, d_values
            )
        assert value.hi < 0
        payload = {
            "arithmetic_class": "DIRECTED_DECIMAL_INTERVAL",
            "classification": "PASS_ATOM_ONE_QUOTIENT_TWENTY_THREE_FIREWALL",
            "endpoint": x,
            "interval_hi": str(value.hi),
            "interval_lo": str(value.lo),
            "odd_sources": list(ODD_SOURCES),
            "quotient": "23",
            "refuted_claim": (
                "atom d=1 alone dominates every active odd component row"
            ),
            "rh_established_by_replay": False,
            "row": j,
            "target_lorenz_refuted": False,
        }
        canonical = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
        payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
        out = (
            Path(__file__).resolve().parent
            / "results"
            / "quotient23_firewall.json"
        )
        out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        print(payload["classification"])
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
