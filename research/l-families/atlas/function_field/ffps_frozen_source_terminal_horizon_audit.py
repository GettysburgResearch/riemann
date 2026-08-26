#!/usr/bin/env python3
"""Bounded exact replay for the frozen-source terminal-horizon audit."""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

FROZEN_SOURCES = {
    "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc": {
        (
            "claims/lemmas/L-102735-four-octave-localization-of-the-radial-frontier.md"
        ): "cb0f305b4e26b3f8553c7f6fe4bab5097b1ab97e",
        (
            "claims/lemmas/"
            "L-102886-dyadic-frozen-vaughan-cutoff-removes-transfer-atoms.md"
        ): "26abf63b6a69c449f89313b151931b2dc71a42ad",
        (
            "claims/lemmas/"
            "L-102887-horizon-safe-pair-gauge-eliminates-the-largest-two-smooth-boundary.md"
        ): "383aa27fee269645e45c26c12fbd4a97a6b337a8",
        (
            "claims/lemmas/"
            "L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md"
        ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
        (
            "claims/lemmas/L-102959-incidence-masked-centered-phase-packing.md"
        ): "59f12fea22bc1871f160cf280baf62155225fdd2",
        (
            "claims/lemmas/"
            "L-102962-canonical-equal-pair-gauge-is-horizon-safe-on-the-boolean-balanced-source.md"
        ): "d8f4557df6dc37e6b605b1821c5b8ab028136398",
        (
            "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md"
        ): "b319572db9ecc89bc528b85368cbf49aa13206d0",
    },
    "98af0db6ec7f77d6333a77a3dac53c4698852f43": {
        (
            "claims/lemmas/"
            "L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md"
        ): "346cc52420ec65457c2a5accc045d4a85635cc24",
        (
            "claims/lemmas/L-106132-boolean-half-source-least-prime-calderon-row.md"
        ): "f393a1d8583c5680b98a4b3e26d9b5a61c8d2b7a",
        (
            "claims/lemmas/"
            "L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md"
        ): "b988b14eb982504a799158eed4c76e7f033c96f0",
        (
            "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md"
        ): "cf40354ff8810a2d4bea9459cf142c300ba36237",
        (
            "claims/theorems/T-106150-same-half-source-analytic-square-frontier.md"
        ): "ac15f0106a26303f06779feb484a521978fe3ecf",
    },
}


def check_source_blobs() -> None:
    """Authenticate every frozen claim used by the audit."""

    for commit, sources in FROZEN_SOURCES.items():
        for path, expected in sources.items():
            completed = subprocess.run(
                ["git", "rev-parse", f"{commit}:{path}"],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2,
            )
            if completed.stdout.strip() != expected:
                raise RuntimeError(f"frozen source blob mismatch: {commit}:{path}")


def integer_nth_root_floor(value: int, degree: int) -> int:
    """Return floor(value**(1/degree)) without floating-point arithmetic."""

    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("value must be a nonnegative integer")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
        raise ValueError("degree must be a positive integer")
    if value < 2:
        return value
    low, high = 0, 1
    while high**degree <= value:
        high *= 2
    while high - low > 1:
        middle = (low + high) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    return low


def subsets(support: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """All ordered-subset choices used in Boolean convolution."""

    result = []
    for mask in range(1 << len(support)):
        result.append(
            tuple(support[index] for index in range(len(support)) if mask >> index & 1)
        )
    return tuple(result)


def complement(support: tuple[int, ...], subset: tuple[int, ...]) -> tuple[int, ...]:
    chosen = set(subset)
    return tuple(prime for prime in support if prime not in chosen)


def mu_cutoff(support: tuple[int, ...], cutoff: int) -> Fraction:
    product = math.prod(support)
    if product > cutoff:
        return Fraction(0)
    return Fraction(-1 if len(support) % 2 else 1)


def a_coefficient(support: tuple[int, ...], cutoff: int) -> Fraction:
    """a_U=epsilon-mu_U star 1 on one squarefree support."""

    epsilon = Fraction(1 if not support else 0)
    return epsilon - sum(mu_cutoff(part, cutoff) for part in subsets(support))


def h_coefficient(support: tuple[int, ...]) -> Fraction:
    return Fraction((-1) ** len(support), 2 ** len(support))


def f_coefficient(support: tuple[int, ...], cutoff: int) -> Fraction:
    """f_U=a_U star h on one squarefree support."""

    return sum(
        a_coefficient(part, cutoff) * h_coefficient(complement(support, part))
        for part in subsets(support)
    )


def b_coefficient(support: tuple[int, ...], cutoff: int) -> Fraction:
    """b_U=f_U star f_U on one squarefree support."""

    return sum(
        f_coefficient(part, cutoff) * f_coefficient(complement(support, part), cutoff)
        for part in subsets(support)
    )


def projection_negative_mass_counterexample(magnitude: int) -> dict[str, int]:
    """A scalar witness that negative mass is not monotone under projection."""

    if isinstance(magnitude, bool) or not isinstance(magnitude, int) or magnitude <= 0:
        raise ValueError("magnitude must be a positive integer")
    selected = -magnitude
    complement_value = magnitude
    complete = selected + complement_value
    return {
        "selected": selected,
        "complement": complement_value,
        "complete": complete,
        "selected_negative_mass": magnitude,
        "complete_negative_mass": max(-complete, 0),
    }


def run() -> dict[str, object]:
    base_exponent = 24
    base_horizon = 2**base_exponent
    next_horizon = 2 * base_horizon
    base_cutoff = integer_nth_root_floor(base_horizon, 6)
    next_cutoff = integer_nth_root_floor(next_horizon, 6)
    if (base_cutoff, next_cutoff) != (16, 17):
        raise AssertionError("dyadic cutoff counterfixture changed")

    owner_pair = (2, 3)
    core = (17, 43)
    physical_product = math.prod(owner_pair) * math.prod(core) ** 2
    source_window = (base_horizon // 8, 2 * base_horizon)
    if not source_window[0] <= physical_product <= source_window[1]:
        raise AssertionError("counterfixture is not in the exact native source window")

    b_base = b_coefficient(core, base_cutoff)
    b_next = b_coefficient(core, next_cutoff)
    if (b_base, b_next) != (Fraction(2), Fraction(0)):
        raise AssertionError("Boolean cutoff-crossing coefficient changed")

    canonical_pair_count = math.comb(len(owner_pair) + len(core), 2)
    canonical_base_share = b_base / canonical_pair_count
    canonical_next_share = b_next / canonical_pair_count

    native_ratio_at_base = Fraction(base_horizon, physical_product)
    if not Fraction(9, 2) < native_ratio_at_base < 8:
        raise AssertionError(
            "the source atom is not genuinely active at the base point"
        )

    localized_source_support = (base_horizon // 8, 2 * base_horizon)
    native_current_support = (
        localized_source_support[0],
        8 * localized_source_support[1],
    )
    extra_current_support = (
        localized_source_support[0],
        16 * localized_source_support[1],
    )
    if extra_current_support != (base_horizon // 8, 32 * base_horizon):
        raise AssertionError("fixed-source terminal dilation changed")
    if native_current_support != (base_horizon // 8, 16 * base_horizon):
        raise AssertionError("fixed-source native support changed")

    terminal_value = 16 * physical_product
    if not 2 * base_horizon < terminal_value < 4 * base_horizon:
        raise AssertionError("counterfixture does not cross a future dyadic block")

    projection_firewall = projection_negative_mass_counterexample(7)
    if projection_firewall["complete_negative_mass"] != 0:
        raise AssertionError("projection firewall failed")

    return {
        "frozen_sources": FROZEN_SOURCES,
        "fixed_source_support_theorem": {
            "native_kernel_support_ratio": [1, 8],
            "extra_kernel_support_ratio": [1, 16],
            "native_block": ["Y", "2Y"],
            "exact_native_source_projection": ["Y/8", "2Y"],
            "projected_native_current_support": ["Y/8", "16Y"],
            "projected_extra_current_support": ["Y/8", "32Y"],
            "terminal_horizon_dilation": 32,
            "dyadic_shells_across_full_extra_support": 8,
            "maximum_future_inverse_depth_from_X_in_[Y,2Y]": 5,
            "conclusion": (
                "anti-causal inversion is constant-horizon for the exact "
                "physical-product projection of one frozen source"
            ),
        },
        "cutoff_crossing_counterfixture": {
            "base_exponent": base_exponent,
            "Y": base_horizon,
            "2Y": next_horizon,
            "U_Y": base_cutoff,
            "U_2Y": next_cutoff,
            "owners": list(owner_pair),
            "core_primes": list(core),
            "physical_product": physical_product,
            "native_source_window": list(source_window),
            "Y_over_physical_product": str(native_ratio_at_base),
            "b_UY(core)": str(b_base),
            "b_U2Y(core)": str(b_next),
            "canonical_owner_pair_count": canonical_pair_count,
            "canonical_base_share": str(canonical_base_share),
            "canonical_next_share": str(canonical_next_share),
            "extra_support_endpoint_for_atom": terminal_value,
            "conclusion": (
                "the same live labelled balanced coordinate at cutoff 16 is "
                "absent after the next-horizon cutoff is reset to 17"
            ),
        },
        "projection_firewall": projection_firewall,
        "typed_conclusion": {
            "proved": ("the shell-projected source has a fixed 32Y terminal horizon"),
            "not_implied_by_frozen_WKSFSC": (
                "negative mass of that same cutoff-and-shell-projected source "
                "on [Y/8,32Y]"
            ),
            "smallest_new_gate": (
                "uniform same-U Jordan negative-mass control for each exact "
                "physical source shell on its complete [Y/8,32Y] support"
            ),
            "type_I_repair_boundary": (
                "cutoff drift is algebraically a difference of Type-I rows; "
                "extra-notched absolute closure of that difference is not in "
                "the frozen claims"
            ),
        },
        "resource_caps": {
            "boolean_labels": 4,
            "maximum_boolean_subsets_per_support": 4,
            "dyadic_horizons": 2,
            "maximum_dyadic_depth": 5,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    if args.check:
        check_source_blobs()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
