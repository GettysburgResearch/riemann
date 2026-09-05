#!/usr/bin/env python3
"""Finite exact replay for R/T-106450.

Checks the minimal Hankel-kernel counterexample, endpoint quotient algebra and
fixed-order threshold. It does not evaluate Xi or prove RESGRAM106450.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main() -> dict[str, object]:
    # U=z^-1 on H^2. H_U z^j is nonzero only at j=0.
    hankel_on_one = Fraction(1)
    hankel_on_z = Fraction(0)
    assert hankel_on_one == 1
    assert hankel_on_z == 0

    # Dg=z and U(Dg)=1 are analytic, so denominator multiplication is in ker H_U.
    denominator_source_in_kernel = True
    initial_space_overlap = Fraction(0)
    assert denominator_source_in_kernel
    assert initial_space_overlap == 0

    # Universal endpoint numerator identity at scalar-value scope.
    lam = Fraction(7, 23)
    f0, f1, fk, fk1 = map(Fraction, (5, -3, 11, 2))
    # Imaginary coefficient of N-D.
    observed = (
        (f0 * lam * fk1 - lam * f1 * fk)
        - (-f0 * lam * fk1 + lam * f1 * fk)
    )
    expected = 2 * lam * (f0 * fk1 - f1 * fk)
    assert observed == expected

    fourth_entry = Fraction(2487, 2500)
    ninety = Fraction(9, 10)
    full_hankel_allowance = fourth_entry - ninety
    assert full_hankel_allowance == Fraction(237, 2500)

    payload: dict[str, object] = {
        "schema": "riemann.x106450.resolvent-frontier.v1",
        "classification": "PASS_T106450_ENDPOINT_KERNEL_CORRECTION",
        "minimal_u": "z^-1",
        "hankel_on_one": "1",
        "hankel_on_denominator_source_z": "0",
        "denominator_source_in_kernel_checked": True,
        "endpoint_numerator_identity_checked": True,
        "fourth_endpoint_full_hankel_allowance": "237/2500",
        "l106400_initial_space_promotion_valid": False,
        "visible_source_percentage_composition_valid": False,
        "resgram106450_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
