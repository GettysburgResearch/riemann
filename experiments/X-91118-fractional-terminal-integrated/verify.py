#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path


def main() -> None:
    q0 = 100

    # Full-breakpoint lower-bound cases for q >= 100.
    assert Fraction(2*q0, q0-1) < Fraction(9,4)
    assert Fraction(2*q0+1, q0-1) < Fraction(9,4)

    assert Fraction(3*q0, q0-1) < Fraction(49,16)
    assert Fraction(3*q0, 2*q0-1) < Fraction(25,16)
    assert Fraction(3*q0+1, q0-1) < Fraction(49,16)
    assert Fraction(3*q0+1, 2*q0-1) < Fraction(25,16)

    assert Fraction(4*q0, q0-1) < Fraction(441,100)  # (21/10)^2
    assert Fraction(4*q0, 2*q0-1) < Fraction(9,4)
    assert Fraction(4*q0, 3*q0-1) < Fraction(36,25)

    derivative_floor = Fraction(1,2)
    W = 200_000
    continuum_omission = derivative_floor * (W-2)

    # L-91324 ordinary fractional response bound 89*C*q^-3/2,
    # with top-collar adjacent-difference constant C=32 and q>X/4.
    top_collar = 89 * 32 * 8
    existing_terminal_error = 28_836
    net_omission = continuum_omission - top_collar
    assert net_omission > existing_terminal_error

    result = {
        "classification": "PASS_INTEGRATED_FRACTIONAL_TOP_OMISSION",
        "real_column_threshold_q": q0,
        "derivative_floor": str(derivative_floor),
        "omission_width": W,
        "continuum_omission_coefficient": str(continuum_omission),
        "fractional_top_collar_coefficient": top_collar,
        "net_omission_coefficient": str(net_omission),
        "existing_terminal_error_coefficient": existing_terminal_error,
        "strict_margin": str(net_omission-existing_terminal_error),
        "scope": (
            "Fraction-only verification of the rational case bounds and final "
            "coefficient ledger. The breakpoint derivative inequality and its "
            "integration are proved symbolically in L-91329."
        ),
    }
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(out)


if __name__ == "__main__":
    main()
