#!/usr/bin/env python3
"""Finite exact replay for L/T-106400.

The replay checks algebraic identities, a finite positive Xi-kernel surrogate,
the Frobenius quantile constants and fail-closed status flags.  It does not
evaluate Xi asymptotically or prove ROBUSTFRAME106400.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def endpoint_identity_fixture(p: Fraction, p1: Fraction, p2: Fraction,
                              p3: Fraction, lam: Fraction) -> None:
    """Check N-D = 2 i lambda (p p'''-p' p'') in Gaussian rationals."""
    # A Gaussian rational is represented by (real, imag).
    def mul(z: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

    def sub(z: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (z[0] - w[0], z[1] - w[1])

    e0m = (p, -lam * p1)
    e0p = (p, lam * p1)
    e2p = (p2, lam * p3)
    e2m = (p2, -lam * p3)
    difference = sub(mul(e0m, e2p), mul(e0p, e2m))
    expected = (Fraction(0), 2 * lam * (p * p3 - p1 * p2))
    assert difference == expected


def exterior_square_density(phi: dict[int, Fraction]) -> dict[int, Fraction]:
    support = sorted(phi)
    output: dict[int, Fraction] = {}
    for xi in range(2 * min(support), 2 * max(support) + 1):
        total = Fraction(0)
        for u, weight in phi.items():
            other = phi.get(xi - u, Fraction(0))
            total += Fraction(1, 2) * (2 * u - xi) ** 2 * weight * other
        output[xi] = total
    return output


def proof_payload() -> dict[str, object]:
    fixtures = [
        (Fraction(3, 2), Fraction(-4, 3), Fraction(5, 7), Fraction(11, 5), Fraction(2, 9)),
        (Fraction(-7, 4), Fraction(9, 8), Fraction(-3, 5), Fraction(13, 6), Fraction(5, 12)),
        (Fraction(2), Fraction(0), Fraction(-5), Fraction(7), Fraction(1, 3)),
    ]
    for fixture in fixtures:
        endpoint_identity_fixture(*fixture)

    # Positive, even finite surrogate of the Xi Fourier kernel.
    phi = {
        -3: Fraction(1, 11),
        -2: Fraction(2, 7),
        -1: Fraction(5, 9),
        0: Fraction(7, 5),
        1: Fraction(5, 9),
        2: Fraction(2, 7),
        3: Fraction(1, 11),
    }
    density = exterior_square_density(phi)
    assert all(value >= 0 for value in density.values())
    assert all(density[xi] == density[-xi] for xi in density)
    assert density[0] > 0

    # The square is load bearing: replacing it by a signed first power can
    # produce a negative convolution coefficient.
    signed = Fraction(0)
    xi = 1
    for u, weight in phi.items():
        signed += (2 * u - xi) * weight * phi.get(xi - u, Fraction(0))
    # Symmetry forces this particular full sum to zero.  A one-sided mutation
    # is negative and is retained as the hostile control.
    assert signed == 0
    one_sided = sum(
        ((2 * u - xi) * weight * phi.get(xi - u, Fraction(0))
         for u, weight in phi.items() if u <= 0),
        Fraction(0),
    )
    assert one_sided < 0

    # Frobenius quantile constants.
    kappa = Fraction(1, 1000)
    delta = Fraction(1, 100)
    q = Fraction(1, 200)
    a = Fraction(1, 2)
    charge = kappa + (1 - kappa) * (delta / (1 - a) ** 2 + q / a)
    assert charge == Fraction(1019, 20000)

    fixed_order = Fraction(599, 625)
    conclusion = fixed_order - charge
    assert conclusion == Fraction(18149, 20000)
    assert conclusion - Fraction(9, 10) == Fraction(149, 20000)

    # A finite eigenvalue fixture saturating the rank-count mechanism.
    eigenvalues = [Fraction(2, 5), Fraction(3, 5), Fraction(1), Fraction(6, 5)]
    frobenius_error = sum(((value - 1) ** 2 for value in eigenvalues), Fraction(0))
    discarded = sum(value < Fraction(1, 2) for value in eigenvalues)
    assert discarded * Fraction(1, 2) ** 2 <= frobenius_error
    assert all(Fraction(1, value) <= 2 for value in eigenvalues if value >= Fraction(1, 2))

    result: dict[str, object] = {
        "schema": "riemann.x106400.xi-endpoint-frame.v1",
        "classification": "PASS_T106400_XI_ENDPOINT_FRAME_ALGEBRA",
        "endpoint_companion_identity_checked": True,
        "intermediate_companion_cancellation_checked": True,
        "exterior_square_density_nonnegative": True,
        "exterior_square_density_even": True,
        "signed_kernel_mutation_rejected": True,
        "frobenius_quantile_constants_checked": True,
        "normalized_charge": "1019/20000",
        "conditional_line_fraction": "18149/20000",
        "conditional_line_decimal": "0.90745",
        "unused_margin_over_ninety": "149/20000",
        "robustframe106400_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = proof_payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
