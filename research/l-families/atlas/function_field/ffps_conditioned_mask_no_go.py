#!/usr/bin/env python3
"""Exact FFPS no-go theorem for pure local masking and reweighting.

The corrected FFPS phase packet has Gram matrix pI-J on m=(p-1)/2
sign-pair coordinates.  This producer solves the exact constrained dual-norm
problem after retaining only a coordinates while requiring the same response
on the constant (principal-member) packet.  It does not model conditioning
that changes the Gram matrix or creates coherent cross-coordinate terms.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Sequence
from fractions import Fraction
from pathlib import Path

import ffps_principal_leverage as phase_packet

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "ffps_conditioned_mask_no_go.json"
NOTE_PATH = HERE / "FFPS_CONDITIONED_MASK_NO_GO.md"
TEST_PATH = ROOT / "tests" / "test_ffps_conditioned_mask_no_go.py"
DEPENDENCY_PATH = HERE / "ffps_principal_leverage.json"

SOURCE_COMMIT_751 = phase_packet.SOURCE_COMMIT_751
SOURCE_BLOBS_751 = phase_packet.SOURCE_BLOBS_751
CONTROL_PRIMES = (3, 5, 7, 11, 13)
MAX_EXACT_ROWS = 64


def _sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    fraction = Fraction(value)
    return [fraction.numerator, fraction.denominator]


def _validate_support(prime: int, support_size: int) -> int:
    dimension = phase_packet.sign_pair_dimension(prime)
    if not 1 <= support_size <= dimension:
        raise ValueError("support size must lie between one and (p-1)/2")
    return dimension


def restricted_gram(prime: int, support_size: int) -> tuple[tuple[int, ...], ...]:
    """Principal submatrix pI_a-J_a of the complete phase Gram."""

    _validate_support(prime, support_size)
    return tuple(
        tuple(prime - 1 if row == column else -1 for column in range(support_size))
        for row in range(support_size)
    )


def restricted_dual_norm_squared(
    prime: int, weights: Sequence[Fraction | int]
) -> Fraction:
    """Return alpha^T(pI_a-J_a)^(-1)alpha exactly."""

    support_size = len(weights)
    _validate_support(prime, support_size)
    values = tuple(Fraction(value) for value in weights)
    total = sum(values, Fraction(0))
    return sum((value * value for value in values), Fraction(0)) / prime + (
        total * total / (prime * (prime - support_size))
    )


def uniform_weights_for_principal_amplitude(
    prime: int, support_size: int
) -> tuple[Fraction, ...]:
    """Weights whose constant-packet response equals the full response m."""

    dimension = _validate_support(prime, support_size)
    return (Fraction(dimension, support_size),) * support_size


def optimal_normalized_leverage_squared(prime: int, support_size: int) -> Fraction:
    """Sharp dual norm at fixed full principal amplitude sum(alpha)=m."""

    dimension = _validate_support(prime, support_size)
    return Fraction(dimension * dimension, support_size * (prime - support_size))


def fixed_amplitude_excess(prime: int, weights: Sequence[Fraction | int]) -> Fraction:
    """Gap above the optimum among weights with sum(alpha)=m."""

    support_size = len(weights)
    dimension = _validate_support(prime, support_size)
    values = tuple(Fraction(value) for value in weights)
    if sum(values, Fraction(0)) != dimension:
        raise ValueError("weights must preserve the full constant-packet amplitude m")
    mean = Fraction(dimension, support_size)
    excess = sum(((value - mean) ** 2 for value in values), Fraction(0)) / prime
    direct = restricted_dual_norm_squared(prime, values)
    optimum = optimal_normalized_leverage_squared(prime, support_size)
    if direct - optimum != excess:
        raise ArithmeticError("fixed-amplitude Pythagorean identity failed")
    return excess


def unnormalized_uniform_leverage_squared(prime: int, support_size: int) -> Fraction:
    """Raw leverage of an unweighted mask before signal normalization."""

    _validate_support(prime, support_size)
    return Fraction(support_size, prime - support_size)


def signal_fraction(prime: int, support_size: int) -> Fraction:
    dimension = _validate_support(prime, support_size)
    return Fraction(support_size, dimension)


def leverage_penalty_over_full(prime: int, support_size: int) -> Fraction:
    full = phase_packet.principal_leverage_squared(prime)
    return optimal_normalized_leverage_squared(prime, support_size) / full


def contraction_classification(prime: int, support_size: int) -> dict[str, object]:
    """Classify the normalized mask by the exact dropped-coordinate threshold."""

    dimension = _validate_support(prime, support_size)
    dropped = dimension - support_size
    leverage = optimal_normalized_leverage_squared(prime, support_size)
    threshold_defect = dimension - dropped * (dropped + 1)
    relation = (
        "contractive" if leverage < 1 else "critical" if leverage == 1 else "expansive"
    )
    expected = (
        "contractive"
        if threshold_defect > 0
        else "critical"
        if threshold_defect == 0
        else "expansive"
    )
    if relation != expected:
        raise ArithmeticError("drop-threshold classification drifted")
    return {
        "dropped_coordinates": dropped,
        "triangular_threshold_defect": threshold_defect,
        "classification": relation,
    }


def build_fixture() -> dict[str, object]:
    rows = []
    for prime in CONTROL_PRIMES:
        dimension = phase_packet.sign_pair_dimension(prime)
        previous: Fraction | None = None
        for support_size in range(1, dimension + 1):
            weights = uniform_weights_for_principal_amplitude(prime, support_size)
            leverage = restricted_dual_norm_squared(prime, weights)
            formula = optimal_normalized_leverage_squared(prime, support_size)
            if leverage != formula:
                raise ArithmeticError("uniform extremizer missed the closed formula")
            raw = unnormalized_uniform_leverage_squared(prime, support_size)
            fraction = signal_fraction(prime, support_size)
            if raw / (fraction * fraction) != leverage:
                raise ArithmeticError("raw-mask signal normalization identity failed")
            if previous is not None and leverage >= previous:
                raise ArithmeticError(
                    "normalized leverage did not improve with support"
                )
            previous = leverage
            classification = contraction_classification(prime, support_size)
            rows.append(
                {
                    "prime": prime,
                    "full_dimension": dimension,
                    "support_size": support_size,
                    "dropped_coordinates": classification["dropped_coordinates"],
                    "restricted_gram": [
                        list(row) for row in restricted_gram(prime, support_size)
                    ],
                    "uniform_principal_preserving_weight": _fraction_pair(weights[0]),
                    "raw_unweighted_mask_leverage_squared": _fraction_pair(raw),
                    "raw_principal_signal_fraction": _fraction_pair(fraction),
                    "normalized_optimal_leverage_squared": _fraction_pair(leverage),
                    "penalty_over_full_panel": _fraction_pair(
                        leverage_penalty_over_full(prime, support_size)
                    ),
                    "triangular_threshold_defect": classification[
                        "triangular_threshold_defect"
                    ],
                    "classification": classification["classification"],
                }
            )
    if len(rows) > MAX_EXACT_ROWS:
        raise ArithmeticError("exact control rows exceeded the declared cap")

    half_panel_examples = []
    for prime in (7, 11, 13):
        dimension = phase_packet.sign_pair_dimension(prime)
        support_size = max(1, dimension // 2)
        half_panel_examples.append(
            {
                "prime": prime,
                "support_size": support_size,
                "full_dimension": dimension,
                "normalized_leverage_squared": _fraction_pair(
                    optimal_normalized_leverage_squared(prime, support_size)
                ),
            }
        )

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_conditioned_mask_no_go.v1",
        "status": "EXACT_LOCAL_PRINCIPAL_AMPLITUDE_MASKING_NO_GO",
        "source_frontier": {
            "pr": 751,
            "commit": SOURCE_COMMIT_751,
            "live_target": "T-106121 / FFPS106121",
            "git_blob_ids": SOURCE_BLOBS_751,
            "dependency": "ffps_principal_leverage.json",
            "dependency_sha256_lf": _sha256_lf(DEPENDENCY_PATH),
        },
        "theorem": {
            "setup": (
                "G_p=pI-J on m=(p-1)/2 sign-pair coordinates; retain a coordinates "
                "and require sum(alpha)=m so the full constant/principal packet keeps "
                "its native amplitude"
            ),
            "restricted_inverse": "(pI_a-J_a)^(-1)=p^(-1)I+[p(p-a)]^(-1)J",
            "dual_norm": (
                "||O_alpha||^2=p^(-1)sum_i(alpha_i^2)+[p(p-a)]^(-1)(sum_i alpha_i)^2"
            ),
            "sharp_optimum": "min_(sum alpha=m)||O_alpha||^2=m^2/[a(p-a)]",
            "unique_real_extremizer": "alpha_1=...=alpha_a=m/a",
            "pythagorean_excess": (
                "||O_alpha||^2-m^2/[a(p-a)]=p^(-1)sum_i(alpha_i-m/a)^2"
            ),
            "full_panel_value": "m/(p-m)=(p-1)/(p+1)",
            "strict_no_go": (
                "a(p-a) is strictly increasing for 1<=a<=m, so every proper mask "
                "has strictly larger normalized leverage than the full panel; arbitrary "
                "real reweighting cannot improve the uniform mask"
            ),
            "drop_threshold": (
                "writing a=m-k, the normalized mask is contractive, critical, or "
                "expansive according as k(k+1) is <, =, or > m"
            ),
            "fixed_fraction_limit": (
                "if a/m tends to theta in (0,1), normalized leverage tends to "
                "1/[theta(2-theta)]>1"
            ),
            "tensor_corollary": (
                "pure masks worsen every local factor, hence cannot improve a coherent "
                "tensor contraction or a positive direct-sum leverage bound"
            ),
        },
        "exact_controls": rows,
        "balanced_mask_examples": half_panel_examples,
        "interpretation": {
            "ruled_out": (
                "Any local condition whose sole operator effect is deletion and real "
                "reweighting of existing sign-pair coordinates, after normalizing the "
                "principal member back to its native amplitude"
            ),
            "not_ruled_out": [
                "conditioning that changes the arithmetic Gram matrix",
                "signed or phase-coherent cross-coordinate terms introduced before squaring",
                "cross-prime Fourier structure",
                "an amplifier using new arithmetic information rather than a support mask",
            ],
            "warning": (
                "The smaller raw value a/(p-a) is not a principal-leverage gain: it "
                "has attenuated the constant signal by a/m and becomes m^2/[a(p-a)] "
                "after source-faithful normalization."
            ),
        },
        "scope": {
            "odd_prime_theorem": True,
            "finite_field_extension_claim": (
                "the matrix proof applies with p replaced by any odd residue-field "
                "cardinality for which the same complete square-phase Gram holds"
            ),
            "enumerated_control_primes": list(CONTROL_PRIMES),
            "exact_control_rows": len(rows),
            "exact_control_row_cap": MAX_EXACT_ROWS,
            "root_number_conditioning_in_general_proved": False,
            "varying_conductor_moment_proved": False,
            "rh_or_grh_proved": False,
        },
        "provenance": {
            "producer_sha256_lf": _sha256_lf(Path(__file__)),
            "note_sha256_lf": _sha256_lf(NOTE_PATH),
            "test_sha256_lf": _sha256_lf(TEST_PATH),
        },
    }
    return fixture


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = _canonical(build_fixture())
    if args.check:
        if (
            not OUTPUT_PATH.is_file()
            or OUTPUT_PATH.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("FFPS conditioned-mask fixture drifted")
        print("PASS_FFPS_CONDITIONED_MASK_NO_GO")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
