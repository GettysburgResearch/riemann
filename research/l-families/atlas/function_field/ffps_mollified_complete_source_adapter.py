#!/usr/bin/env python3
"""Bounded source-lock replay for the mollified complete-source adapter."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PARENT_COMMIT = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
HALF_SOURCE_COMMIT = "98af0db6ec7f77d6333a77a3dac53c4698852f43"

PARENT_BLOBS = {
    "claims/lemmas/L-102505-squared-core-physical-collapse-is-polylogarithmic.md": (
        "135b496421bbb0986946ae647e4e2b9058d8f22c"
    ),
    "claims/lemmas/L-102601-logarithmic-phase-connection-tail.md": (
        "ecc70bc470155a0b156f0f607ebd09504d9d4691"
    ),
    "claims/lemmas/L-102602-native-completion-defect-and-pole-audit.md": (
        "47966830014aaaaf0ff83f3659a2b04541f45486"
    ),
    "claims/lemmas/L-102603-duhamel-current-for-the-completion-defect.md": (
        "ee0e142dd5c4db246237167f64c410d1583e3d34"
    ),
    "claims/lemmas/L-102604-duhamel-equal-owner-disintegration.md": (
        "ab3135710439ff79a9ee634bfc291f2f5f34d0dd"
    ),
    "claims/lemmas/L-102702-diagonal-and-factor-pair-costs-are-subpower.md": (
        "5ce74d15cc7b41e990630f6749bfd3c2473cbbf4"
    ),
    "claims/lemmas/L-102705-same-owner-square-core-overlap-is-polylogarithmic.md": (
        "445306dd4a8f3f85134fcb5da3bfa83e7165ecc6"
    ),
    (
        "claims/lemmas/"
        "L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md"
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        "claims/lemmas/"
        "L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md"
    ): "6810bcece309b0c54ae6c8fc84b314990004549c",
    (
        "claims/lemmas/L-102708-uniform-geodesic-source-energy-is-polylogarithmic.md"
    ): "14ae4c9ff5e29f12cf8aa70ead5d4c4dd337d6d7",
    "claims/lemmas/L-102709-regionwise-gauge-selection-is-source-exact.md": (
        "6080f9c6d36f5654a69d2c8148d3aa4483f39dfb"
    ),
    "claims/lemmas/L-102747-pair-owner-collapse-costs-only-log-squared.md": (
        "3437a003426ed54cb690b891e81388b722ed3539"
    ),
    (
        "claims/lemmas/"
        "L-102883-balanced-vaughan-free-energy-and-equal-product-cost-are-subpower.md"
    ): "b8a6eed2c8dda7d0ed28a8dd18fc57387e4c2e7b",
    (
        "claims/lemmas/L-102886-dyadic-frozen-vaughan-cutoff-removes-transfer-atoms.md"
    ): "26abf63b6a69c449f89313b151931b2dc71a42ad",
    (
        "claims/lemmas/"
        "L-102887-very-large-common-square-cores-are-absolutely-summable.md"
    ): "22fe3cfa5bb47698fc2a5ad879fc0870543469b2",
    (
        "claims/lemmas/"
        "L-102904-endpoint-color-walsh-expansion-has-only-squared-activity-off-the-midpoint.md"
    ): "f0bdbf09e620027eafe9a198350f588edafdd269",
    (
        "claims/lemmas/"
        "L-102905-local-critical-hodge-decomposition-of-complementary-factors.md"
    ): "215d7bbb7a25c788eaa39cc4d3e717e911705886",
    "claims/lemmas/L-102906-global-primewise-hodge-normal-form.md": (
        "9e7728f51948b55a886e919d9d8a58cc5de07b6e"
    ),
    (
        "claims/lemmas/"
        "L-102951-harmonic-critical-class-is-the-squarefree-boolean-euler-class.md"
    ): "1a2f15e7b5fcb0a3fb17d20668c3735065d14224",
    (
        "claims/lemmas/"
        "L-102952-owner-excluded-boolean-vaughan-coefficients-are-universal.md"
    ): "8e0de55d193d6f9dafd025235dac8ab48e687081",
    (
        "claims/lemmas/"
        "L-102953-squarefree-type-I-is-an-l1-shift-transfer-of-the-parent-lattice.md"
    ): "9bfb57bdd6799c82fb274c441b14854fae322bcb",
    (
        "claims/lemmas/"
        "L-102954-hodge-boolean-reduction-leaves-one-owner-indexed-restriction.md"
    ): "65c63098dcea20bfe8a189355c86fe663908b00b",
    (
        "claims/lemmas/"
        "L-102955-boolean-balanced-equal-and-one-sided-core-sectors-are-subpower.md"
    ): "208f3752be4245a835c5a150c14945ca48365489",
    (
        "claims/lemmas/"
        "L-102962-canonical-equal-pair-gauge-is-horizon-safe-on-the-boolean-balanced-source.md"
    ): "d8f4557df6dc37e6b605b1821c5b8ab028136398",
    (
        "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md"
    ): "b319572db9ecc89bc528b85368cbf49aa13206d0",
}

HALF_SOURCE_BLOBS = {
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
    "claims/theorems/T-106150-same-half-source-analytic-square-frontier.md": (
        "ac15f0106a26303f06779feb484a521978fe3ecf"
    ),
}

Quadratic = tuple[Fraction, Fraction]


def _check_blob(commit: str, path: str, expected: str) -> None:
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


def check_source_blobs() -> None:
    for path, expected in PARENT_BLOBS.items():
        _check_blob(PARENT_COMMIT, path, expected)
    for path, expected in HALF_SOURCE_BLOBS.items():
        _check_blob(HALF_SOURCE_COMMIT, path, expected)


def duplicate_67_coefficients() -> dict[int, int]:
    """Collapse two distinct labelled factors over the physical prime 67."""
    first = (1, -1)
    second = (1, -1)
    result = [0, 0, 0]
    for left_degree, left_coefficient in enumerate(first):
        for right_degree, right_coefficient in enumerate(second):
            result[left_degree + right_degree] += left_coefficient * right_coefficient
    return dict(enumerate(result))


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qscale(scale: Fraction, value: Quadratic) -> Quadratic:
    return scale * value[0], scale * value[1]


def kernel_identity_sample(s: int) -> tuple[Quadratic, Quadratic]:
    if isinstance(s, bool) or not isinstance(s, int) or s <= 1:
        raise ValueError("sample must be an integer greater than one")
    sf = Fraction(s)
    q = (Fraction(1), -Fraction(1, 2**s))
    r = Fraction(1) - Fraction(1, 2**s)
    a_hat = qscale(r / (sf * (sf - Fraction(1, 2))), q)
    differential = (
        Fraction(1, 2) * sf * (sf - 1) * (5 * sf + Fraction(3, 2)) * (2 * sf - 1)
    )
    from_half_source = qscale(differential, qmul(a_hat, a_hat))
    target_scalar = (
        r**2 * (sf - 1) * (5 * sf + Fraction(3, 2)) / (sf * (sf - Fraction(1, 2)))
    )
    direct_extra = qscale(target_scalar, qmul(q, q))
    return from_half_source, direct_extra


def type_i_exponents() -> dict[str, Fraction]:
    unrestricted_lattice = Fraction(-1, 2)
    squarefree_count_tax = Fraction(1, 4)
    squarefree_lattice = unrestricted_lattice + squarefree_count_tax
    vaughan_weight_tax = Fraction(1, 6)
    final_row = squarefree_lattice + vaughan_weight_tax
    return {
        "unrestricted_lattice": unrestricted_lattice,
        "squarefree_count_tax": squarefree_count_tax,
        "squarefree_lattice": squarefree_lattice,
        "vaughan_weight_tax": vaughan_weight_tax,
        "final_boolean_type_i": final_row,
    }


def source_path_disposition() -> list[dict[str, str]]:
    return [
        {
            "step": "duplicate-67 labelled Euler source -> beta",
            "status": "proved exact",
        },
        {
            "step": "native Euler -> harmonic Hodge class at frozen scope",
            "status": "proved modulo frozen squared ideal",
        },
        {
            "step": "Boolean Vaughan and owner restriction",
            "status": "proved exact",
        },
        {
            "step": "native balanced observation -> completed x_p x_q y_C observation at k_epsilon",
            "status": "open: NATCOMP-MOLL106150",
        },
        {
            "step": "completed Boolean balanced source -> Beta half-source square",
            "status": "proved exact",
        },
        {
            "step": "completed half-source -> extra-notched Wick differential",
            "status": "proved exact",
        },
    ]


def run() -> dict[str, object]:
    samples = {}
    for s in (2, 3, 5):
        left, right = kernel_identity_sample(s)
        if left != right:
            raise AssertionError(f"kernel identity failed at s={s}")
        samples[str(s)] = {
            "rational": str(left[0]),
            "sqrt2": str(left[1]),
        }
    exponents = type_i_exponents()
    if exponents["final_boolean_type_i"] != Fraction(-1, 12):
        raise AssertionError("Type-I exponent ledger changed")

    beta_coefficients = duplicate_67_coefficients()
    if beta_coefficients != {0: 1, 1: -2, 2: 1}:
        raise AssertionError("duplicate-67 beta coefficients changed")

    closure_rows = {
        "boolean_type_i": {
            "sources": ["L-102953", "L-106080"],
            "transport": "proved generic fixed-BV zero-mass kernel estimate",
        },
        "diagonal_and_equal_product": {
            "sources": ["L-102702", "L-102883"],
            "transport": "fixed-L2 energy plus one-block Cauchy-Schwarz",
        },
        "same_owner_square_cores": {
            "sources": ["L-102705"],
            "transport": "fixed compact-kernel autocorrelation",
        },
        "pair_owner_collapse": {
            "sources": ["L-102747", "L-102962"],
            "transport": "exact allocation and logarithmic multiplicity only",
        },
        "very_large_common_square": {
            "sources": ["L-102887"],
            "transport": "absolute common-square summation",
        },
        "source_l1_squared_and_higher": {
            "sources": ["L-102601", "L-102904", "L-102905", "L-102906"],
            "transport": "Tonelli after exact source isolation",
        },
        "finite_and_terminal": {
            "sources": ["L-102886", "L-106080"],
            "transport": "fixed finite support",
        },
    }
    return {
        "frozen_sources": {
            "parent_commit": PARENT_COMMIT,
            "parent_blobs": PARENT_BLOBS,
            "half_source_commit": HALF_SOURCE_COMMIT,
            "half_source_blobs": HALF_SOURCE_BLOBS,
        },
        "source_path": source_path_disposition(),
        "duplicate_67": {
            "labelled_local_polynomial": "(1-x_67,1)(1-x_67,2)",
            "physical_coefficients_by_exponent": {
                str(key): value for key, value in beta_coefficients.items()
            },
        },
        "kernel": {
            "extra_multiplier": ("q(s)^2*r(s)^2*(s-1)*(5s+3/2)/(s*(s-1/2))"),
            "mollifier": "fixed positive log box eta_epsilon",
            "kernel_zero_order_at_s_zero": 1,
            "mollifier_mass": 1,
            "identity_samples": samples,
        },
        "type_i_exponents_in_Y": {key: str(value) for key, value in exponents.items()},
        "closure_rows": closure_rows,
        "adapter": {
            "name": "MEXTSRC106150",
            "status": "open: not proved by the frozen source chain",
            "missing_source_gate": "NATCOMP-MOLL106150",
            "missing_source_gate_reason": (
                "multiplicative polylog gauge equivalence does not imply an "
                "additive L1-subpower error at k_epsilon"
            ),
            "retained_live_object": "D_out J_U^diamond for the complete balanced source",
            "proposed_closed_remainder": "absolute Y^(o(1)) on each dyadic block",
            "mollified_one_sided_gate": "MWKSFSC106150 remains open",
            "conditional_conclusion": (
                "MEXTSRC106150 and MWKSFSC106150 plus the direct consumer imply RH"
            ),
        },
        "horizon": {
            "raw_piecewise_object": (
                "sum_j restriction of D_out J_(U_j)^diamond to [j log 2,(j+1) log 2)"
            ),
            "endpoint_atoms": "assigned exactly once by half-open restrictions",
            "frozen_wksfsc_binding": (
                "not established by the wording of T-106150 alone"
            ),
            "finite_horizon_contraction": (
                "(eta_epsilon*L_fr)^-([0,T]) <= L_fr^-([0,T])"
            ),
        },
        "scope": {
            "equal_and_one_sided_balanced_sectors_deleted": False,
            "ordinary_self_convolution_used": False,
            "anti_causal_future_used": False,
            "multiplicative_gauge_spent_as_additive_error": False,
            "mextsrc_proved": False,
            "raw_wksfsc_bound_to_piecewise_gate": False,
            "rh_proved": False,
            "grh_proved": False,
        },
        "resource_caps": {
            "mellin_samples": 3,
            "source_atoms_enumerated": 0,
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
