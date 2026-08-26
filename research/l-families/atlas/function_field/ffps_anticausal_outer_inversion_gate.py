#!/usr/bin/env python3
"""Exact bounded replay for anti-causal outer-kernel inversion."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

Quadratic = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FROZEN_SOURCES = {
    "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc": {
        (
            "claims/lemmas/"
            "L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md"
        ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
        (
            "claims/lemmas/"
            "L-102885-derivative-outer-kernel-is-a-stable-image-of-the-same-k1-wavelet.md"
        ): "045481b73474d67ded5bf9633808e8d8d39c4622",
        (
            "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md"
        ): "b319572db9ecc89bc528b85368cbf49aa13206d0",
    },
    "98af0db6ec7f77d6333a77a3dac53c4698852f43": {
        "claims/lemmas/L-102500-common-compact-mother-and-bezout.md": (
            "db4590fc23b53ed601e108a77e4d064b7d9d13f9"
        ),
        "claims/lemmas/L-102701-common-mother-ratiofour-two-field-form.md": (
            "70eb455a3b2bb0398f8bba22dee82c39ef803156"
        ),
        (
            "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md"
        ): "cf40354ff8810a2d4bea9459cf142c300ba36237",
        (
            "claims/lemmas/"
            "L-102740-outer-ray-current-factors-through-the-first-order-critical-scale-current.md"
        ): "ec2f3aafe1b590a11a9967e298f5dfb0e2d59f55",
        (
            "claims/theorems/T-106150-same-half-source-analytic-square-frontier.md"
        ): "ac15f0106a26303f06779feb484a521978fe3ecf",
    },
}


def check_source_blobs() -> None:
    """Authenticate the exact frozen files used in the multiplier audit."""

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


def qmul(left: Quadratic, right: Quadratic) -> Quadratic:
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qadd(left: Quadratic, right: Quadratic) -> Quadratic:
    return left[0] + right[0], left[1] + right[1]


def qscale(scale: Fraction, value: Quadratic) -> Quadratic:
    return scale * value[0], scale * value[1]


def geometric_partial_sum(depth: int) -> Quadratic:
    """sum_(j=1)^depth 2^(-j/2), exactly in Q(sqrt(2))."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    ratio: Quadratic = (Fraction(0), Fraction(1, 2))
    term: Quadratic = (Fraction(1), Fraction(0))
    total: Quadratic = (Fraction(0), Fraction(0))
    for _ in range(depth):
        term = qmul(term, ratio)
        total = qadd(total, term)
    return total


def qstr(value: Quadratic) -> str:
    a, b = value
    if b == 0:
        return str(a)
    sign = "+" if b > 0 else "-"
    magnitude = abs(b)
    radical = "sqrt(2)" if magnitude == 1 else f"{magnitude}*sqrt(2)"
    if a == 0:
        return radical if b > 0 else f"-{radical}"
    return f"{a}{sign}{radical}"


def multiplier_polynomial_check() -> bool:
    """Check 4(s-1)*(5s+3/2)/4=(s-1)(5s+3/2)."""

    native_numerator = [Fraction(-4), Fraction(4)]
    stable_factor = [Fraction(3, 8), Fraction(5, 4)]
    product = [Fraction(0)] * 3
    for left_index, left in enumerate(native_numerator):
        for right_index, right in enumerate(stable_factor):
            product[left_index + right_index] += left * right
    return product == [Fraction(-3, 2), Fraction(-7, 2), Fraction(5)]


def run() -> dict[str, object]:
    if not multiplier_polynomial_check():
        raise AssertionError("native/intermediate multiplier factorization changed")
    limit: Quadratic = (Fraction(1), Fraction(1))
    panels = []
    previous = (Fraction(0), Fraction(0))
    for depth in (0, 1, 2, 4, 8, 16, 32):
        partial = geometric_partial_sum(depth)
        # Monotonicity is numerical only for this bounded display; exact
        # convergence follows from the geometric identity in the note.
        numeric = float(partial[0]) + float(partial[1]) * 2**0.5
        previous_numeric = float(previous[0]) + float(previous[1]) * 2**0.5
        if numeric < previous_numeric or numeric > 1 + 2**0.5:
            raise AssertionError("anti-causal coefficient ledger failed")
        panels.append(
            {"depth": depth, "partial_sum": qstr(partial), "decimal": f"{numeric:.12f}"}
        )
        previous = partial
    stable_inverse_l1 = Fraction(4, 5) / Fraction(3, 10)
    if stable_inverse_l1 != Fraction(8, 3):
        raise AssertionError("stable inverse constant changed")
    combined = qscale(stable_inverse_l1, limit)
    return {
        "frozen_sources": FROZEN_SOURCES,
        "three_kernel_multipliers": {
            "explicit_native_K_L": "4*q*r^2*(s-1)/(s*(s-1/2))",
            "L102740_differentiated_outer": "q*r^2*(s-1)*(5s+3/2)/(s*(s-1/2))",
            "common_mother_self_convolution": "q^2*r^2*(s-1)*(5s+3/2)/(s*(s-1/2))",
            "factorization": "K_extra=Q*T*K_native, T=(5D+3/2)/4",
            "factorization_polynomial_coefficients": ["-3/2", "-7/2", "5"],
            "typing_caveat": (
                "the frozen L-102885 names the common-mother K_extra object K_L; "
                "it is not the explicit native K_L of L-102880"
            ),
        },
        "anti_causal_inverse": {
            "Q": "I-sqrt(2)*S_2",
            "formula": "h=-sum_(j>=1)2^(-j/2)*S_2^(-j)g, g=Qh",
            "coefficient_sum": "1+sqrt(2)",
            "zero_mass_one_sided_bound": "||h_-||_TV <= (1+sqrt(2))*||g_-||_TV",
            "partial_sums": panels,
        },
        "stable_inverse": {
            "T": "(5/4)*(D+3/10)",
            "formula": "f=(4/5)*(D+3/10)^(-1)h",
            "positive_kernel": "(4/5)*exp(-3(u-v)/10)*1_(v<=u)",
            "L1_norm": str(stable_inverse_l1),
        },
        "combined_global_bound": {
            "formula": "||K_native-source_-||_1 <= C_inv*||K_extra-source_-||_TV",
            "C_inv": qstr(combined),
            "requires": "same fixed source and zero total logarithmic mass",
        },
        "terminal_gate": {
            "name": "TERMFUT106150",
            "statement": (
                "for the source frozen at horizon Y and cutoff U(Y), the same "
                "live K_extra current has complete support in [1,CY] for fixed C "
                "and Jordan negative variation Y^o(1) there"
            ),
            "consequence": (
                "Jordan WKSFSC106150 AND TERMFUT106150 transfer to the explicit "
                "native K_L live negative-mass premise"
            ),
            "status": "exactly isolates moving-cutoff/terminal compatibility",
        },
        "conclusion_scope": {
            "kernel_level": (
                "Jordan WKSFSC106150 AND TERMFUT106150 imply the same-source "
                "explicit-native live premise"
            ),
            "parent_binding": (
                "NATBIND106150 must bind BCI102990 to that explicit native "
                "kernel and same live source before the BCI/RH arrow"
            ),
            "parent_binding_status": "open",
            "raw_complete_beta_status": (
                "refuted by the complete-beta atomic variation firewall: "
                "Jordan negative variation is Omega(sqrt(Y)); the kernel-level "
                "implication concerns the differently scoped frozen live source"
            ),
            "viable_complete_replacement": (
                "mollify before Jordan decomposition; the fixed-mollified "
                "negative-mass estimate is RH-equivalent and is not proved here"
            ),
        },
        "resource_caps": {
            "maximum_dyadic_depth": 32,
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
