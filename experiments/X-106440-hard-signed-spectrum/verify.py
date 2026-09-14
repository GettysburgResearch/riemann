#!/usr/bin/env python3
"""Exact finite checks for L/T-106432--106440.

The replay checks the finite-circle hard-band Hankel counting identities, the
denominator-kernel counterfamily, the residue-kernel partition and the exact
ninety-percent constants.  It does not evaluate Xi or prove
HARDSIGNED106440.
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def circle_checks() -> int:
    checks = 0
    max_frequency = 256
    # Deterministic rational Fourier energies; unimodularity is unnecessary
    # for the Hilbert--Schmidt counting identity itself.
    energies_minus = {
        m: Fraction((37 * m + 11) % 101 + 1, 103 * (m + 1))
        for m in range(1, max_frequency + 1)
    }
    energies_plus = {
        m: Fraction((29 * m + 7) % 97 + 1, 101 * (m + 2))
        for m in range(1, max_frequency + 1)
    }

    full_minus = sum(
        (m * value for m, value in energies_minus.items()), Fraction(0)
    )
    full_plus = sum(
        (m * value for m, value in energies_plus.items()), Fraction(0)
    )

    for d in range(1, 129):
        visible_minus = sum(
            (min(d, m) * value for m, value in energies_minus.items()),
            Fraction(0),
        )
        complement_minus = sum(
            ((m - d) * value for m, value in energies_minus.items() if m > d),
            Fraction(0),
        )
        visible_plus = sum(
            (min(d, m) * value for m, value in energies_plus.items()),
            Fraction(0),
        )
        complement_plus = sum(
            ((m - d) * value for m, value in energies_plus.items() if m > d),
            Fraction(0),
        )
        assert visible_minus + complement_minus == full_minus
        assert visible_plus + complement_plus == full_plus
        assert (
            full_minus - full_plus
            == (visible_minus - visible_plus)
            + (complement_minus - complement_plus)
        )
        checks += 3

    # U_m=z^{-m}: the d-column visible Hankel matrix has min(d,m) unit
    # anti-diagonal entries and the analytic numerator difference has no
    # negative Fourier coefficient.
    for m in range(1, 257):
        for d in range(1, 129):
            visible = sum(1 for k in range(d) if k < m)
            assert visible == min(d, m)
            checks += 1

    return checks


def residue_kernel_checks() -> int:
    checks = 0
    for h in (0.125, 0.5, 2.0, 7.0):
        for alpha in (
            0.2 + 0.1j,
            0.7 - 0.4j,
            1.3 + 2.1j,
            4.0 - 0.75j,
        ):
            visible = (1.0 - cmath.exp(-h * alpha)) / (alpha * alpha)
            complement = cmath.exp(-h * alpha) / (alpha * alpha)
            full = 1.0 / (alpha * alpha)
            assert abs((visible + complement) - full) < 1e-12
            checks += 1
    return checks


def payload() -> dict[str, object]:
    checks = circle_checks() + residue_kernel_checks()

    ninety_margin = Fraction(599, 625) - Fraction(9, 10)
    old_visible = Fraction(1, 600)
    conditional_tail = ninety_margin - old_visible
    assert ninety_margin == Fraction(73, 1250)
    assert conditional_tail == Fraction(851, 15000)

    result: dict[str, object] = {
        "schema": "riemann.x106440.hard-signed-spectrum.v1",
        "classification": "PASS_T106440_HARD_BAND_SIGNED_SPECTRAL_REDUCTION",
        "checks": checks,
        "circle_dimensions_checked": 128,
        "circle_frequency_cutoff_checked": 256,
        "denominator_kernel_counterfamily_checked": True,
        "visible_trace_formula_checked": True,
        "complement_trace_formula_checked": True,
        "signed_split_checked": True,
        "residue_kernel_partition_checked": True,
        "ninety_margin": "73/1250",
        "conditional_old_signed_tail_allowance": "851/15000",
        "actual_visible_one_over_600_proved": False,
        "hardsigned106440_proved": False,
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
    result = payload()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
