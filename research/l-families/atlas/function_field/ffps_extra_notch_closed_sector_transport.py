#!/usr/bin/env python3
"""Bounded exponent replay for the mollified extra-notch transport lemma."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

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
            "L-102953-squarefree-type-I-is-an-l1-shift-transfer-of-the-parent-lattice.md"
        ): "9bfb57bdd6799c82fb274c441b14854fae322bcb",
        (
            "claims/theorems/T-102970-hodge-boolean-incidence-restriction-frontier.md"
        ): "fdbaad2077c5905368595a9f358cf7ae77a1d4c0",
        (
            "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md"
        ): "b319572db9ecc89bc528b85368cbf49aa13206d0",
    },
    "98af0db6ec7f77d6333a77a3dac53c4698852f43": {
        "claims/lemmas/L-102701-common-mother-ratiofour-two-field-form.md": (
            "70eb455a3b2bb0398f8bba22dee82c39ef803156"
        ),
        (
            "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md"
        ): "cf40354ff8810a2d4bea9459cf142c300ba36237",
        (
            "claims/theorems/T-106150-same-half-source-analytic-square-frontier.md"
        ): "ac15f0106a26303f06779feb484a521978fe3ecf",
    },
}


def check_source_blobs() -> None:
    """Authenticate the exact extra-notch and parent-closure sources."""

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


def type_i_exponents(cutoff_exponent: Fraction = Fraction(1, 6)) -> dict[str, Fraction]:
    """Generic zero-mass lattice and squarefree-transfer exponents."""

    unrestricted = 2 * cutoff_exponent - Fraction(1, 2)
    squarefree_lattice = -Fraction(1, 4)
    squarefree_type_i = squarefree_lattice + cutoff_exponent
    return {
        "unrestricted_type_i": unrestricted,
        "squarefree_lattice": squarefree_lattice,
        "squarefree_type_i": squarefree_type_i,
    }


def negative_variation_contraction(
    negative_mass: Fraction, probability_mass: Fraction
) -> Fraction:
    if negative_mass < 0 or probability_mass < 0:
        raise ValueError("masses must be nonnegative")
    if probability_mass != 1:
        raise ValueError("the smoothing kernel must have probability mass one")
    return negative_mass


def run() -> dict[str, object]:
    exponents = type_i_exponents()
    expected = {
        "unrestricted_type_i": -Fraction(1, 6),
        "squarefree_lattice": -Fraction(1, 4),
        "squarefree_type_i": -Fraction(1, 12),
    }
    if exponents != expected:
        raise AssertionError("Type-I exponent ledger changed")
    contraction_panels = []
    for mass in (Fraction(0), Fraction(1, 7), Fraction(3, 2), Fraction(1001, 13)):
        contracted = negative_variation_contraction(mass, Fraction(1))
        contraction_panels.append(
            {
                "input_negative_variation": str(mass),
                "upper_bound_after_smoothing": str(contracted),
            }
        )
    return {
        "frozen_sources": FROZEN_SOURCES,
        "kernel_class": {
            "raw": "finite signed compact logarithmic measure K_ext with total mass zero",
            "raw_multiplier": "q^2*r^2*(s-1)*(5s+3/2)/(s*(s-1/2))",
            "zero_mass_reason": "r(s)^2/s vanishes at s=0",
            "mollifier": "eta_epsilon=epsilon^(-1)*1_[0,epsilon]",
            "mollifier_multiplier": "(1-exp(-epsilon*s))/(epsilon*s)",
            "epsilon_scope": "epsilon>0 is fixed independently of Y",
            "smoothed": "k_epsilon=eta_epsilon*K_ext is compact BV and has integral zero",
            "BV_bound": "Var(k_epsilon)<=2*||K_ext||_TV/epsilon",
            "L1_bound": "||k_epsilon||_1<=||K_ext||_TV",
            "negative_variation": "smoothing by eta_epsilon is contracting",
            "local_negative_variation": (
                "integral_I (eta_epsilon*H)_- <= H_-(I-[0,epsilon])"
            ),
        },
        "generic_lattice_lemma": {
            "lattice": "L_k(Z)=sum_(m>=1) m^(-1) k(log(Z/m^2))",
            "continuous_integral": "(1/2)*integral k = 0",
            "euler_variation": "Var[x^(-1)k(log(Z/x^2))]=O_k(Z^(-1/2))",
            "conclusion": "L_k(Z)=O_k(Z^(-1/2))",
            "scaled_BV_function": (
                "g_Z(x)=Z^(-1/2)*h(x/sqrt(Z)), h(u)=u^(-1)*k(-2log(u))"
            ),
        },
        "restricted_squarefree_transfer": {
            "inclusion_exclusion": "L_k^(R)(W)=sum_(d|rad(R)) mu(d)/d*L_k(W/d^2)",
            "restricted_bound": "O_k(2^omega(R)*W^(-1/2))",
            "parent_scope_hypothesis": "2^omega(R)=Y^o(1)",
            "squarefree_identity": (
                "L_(k,sf)^(R)(Z)=sum_((ell,R)=1) mu(ell)/ell^2*L_k^(R)(Z/ell^4)"
            ),
            "support_cutoff": "ell=O_k(Z^(1/4))",
            "squarefree_conclusion": "L_(k,sf)^(R)(Z)=Y^o(1)*Z^(-1/4)",
        },
        "type_i_exponents": {key: str(value) for key, value in exponents.items()},
        "absolute_sector_lemma": {
            "premise": "sum_alpha abs(c_alpha)=Y^o(1)",
            "observation": "sum_alpha c_alpha*k_epsilon(log X-log n_alpha)",
            "conclusion": "logarithmic L1 norm <= ||k_epsilon||_1*Y^o(1)=Y^o(1)",
        },
        "parent_t102990_taxonomy": [
            {
                "sector": "Boolean Type-I",
                "transport": "generic zero-mass lattice plus l1 square shifts",
            },
            {
                "sector": "finite and terminal rows",
                "transport": "fixed finite kernel norm",
            },
            {"sector": "equal reduced core", "transport": "absolute source bound"},
            {"sector": "one-sided reduced core", "transport": "absolute source bound"},
            {
                "sector": "very-large common square core",
                "transport": "absolute summability",
            },
            {
                "sector": "squared/higher-prime-power color",
                "transport": "polylog absolute ledger",
            },
            {
                "sector": "equal-pair owner multiplicity",
                "transport": "polylog absolute ledger",
            },
        ],
        "adapter_status": {
            "generic_kernel_transport": "proved",
            "taxonomy_match": (
                "summary-level candidate mechanisms transcribed from T-102990"
            ),
            "remaining_binding_audit": (
                "verify each inherited proof at exact source scope and bind the seven "
                "rows into the same complete-source/horizon recombination"
            ),
            "EXTSRC106150": "open pending that provenance and source-binding audit",
            "complete_current_implication": (
                "raw Jordan WKSFSC plus proved EXTSRC106150 controls the "
                "mollified complete current"
            ),
        },
        "contraction_panels": contraction_panels,
        "resource_caps": {
            "source_atoms_enumerated": 0,
            "conductors_enumerated": 0,
            "curves_enumerated": 0,
            "point_counts": 0,
            "scalar_panels": len(contraction_panels),
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
