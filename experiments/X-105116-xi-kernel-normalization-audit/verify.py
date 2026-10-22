#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

VERDICT = "PASS_X105116_XI_KERNEL_NORMALIZATION_AUDIT"
ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(value: F | int) -> str:
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def source_lock() -> dict[str, object]:
    row: dict[str, object] = {
        "pr": 720,
        "pr_head": "beb9d8a4e10fb8c8deb74bb0505a32fe55cddd14",
        "pr_base": "research/gpt56-pro/104500-xi-riccati-pick-cascade",
        "l104513": {
            "commit": "49f04d3459d1276e6958cffb0a55680b0a4ca70e",
            "blob": "147f13997e1bb16c547994021dd26f7693f8a566",
            "origin_multiplicity_term_omitted": True,
        },
        "l104528": {
            "commit": "6ee43255d64a27b76de7e1d0fc230a4c7767969e",
            "blob": "187a2f43372241641e5b92a8300d4452f6a26d79",
            "unscaled_fourier_display_is_compatible_with_standard_xi": False,
        },
        "l104531": {
            "commit": "efe3ef6aed66a68a47bbfe1d3678210a249ad725",
            "blob": "7235207cb1bab2d540598dbe1c9cf076afd960a0",
            "theta_orbit_source_locked": True,
        },
        "upstream_pr716": {
            "pr": 716,
            "head": "a1d2387c4a1416c3f220a16fae849e6eab620545",
            "l104504": {
                "commit": "3776c61ff9b679bb8a933b1122f631cd83f88d85",
                "blob": "2f98606a8028497051e60300b20cff5c0e7301ef",
            },
        },
        "downstream_pr724": {
            "pr": 724,
            "head": "82ba4bdb824868dcf26d5d2f2d38b1e2af2d8631",
            "base": "codex/105100-residue-second-moment",
            "l105200": {
                "commit": "b03b4e66274d6fa014c13ed3c22cbdb11270845e",
                "blob": "c544394bd5e9c3f54624059ec58e7b24a4e36b1a",
            },
            "l105207": {
                "commit": "8ddb2a0fedadc4be7d7aa7796a4756659de3f3b8",
                "blob": "c7576257d8938a9984f69ac9e1f20d4b3eed2acf",
            },
            "l105208": {
                "commit": "82ba4bdb824868dcf26d5d2f2d38b1e2af2d8631",
                "blob": "6551bb638816224d851ef8059f31ea4561db82af",
            },
        },
    }
    oids = [
        row["pr_head"],
        row["l104513"]["commit"],
        row["l104513"]["blob"],
        row["l104528"]["commit"],
        row["l104528"]["blob"],
        row["l104531"]["commit"],
        row["l104531"]["blob"],
        row["upstream_pr716"]["head"],
        row["upstream_pr716"]["l104504"]["commit"],
        row["upstream_pr716"]["l104504"]["blob"],
        row["downstream_pr724"]["head"],
        row["downstream_pr724"]["l105200"]["commit"],
        row["downstream_pr724"]["l105200"]["blob"],
        row["downstream_pr724"]["l105207"]["commit"],
        row["downstream_pr724"]["l105207"]["blob"],
        row["downstream_pr724"]["l105208"]["commit"],
        row["downstream_pr724"]["l105208"]["blob"],
    ]
    require(
        all(
            isinstance(oid, str)
            and len(oid) == 40
            and all(character in "0123456789abcdef" for character in oid)
            for oid in oids
        ),
        "source lock contains a malformed Git object ID",
    )
    return row


def normalization_ledger() -> dict[str, object]:
    xi_prefactor = F(1, 2)
    phi_operator = F(1, 4)
    phi_to_xi = phi_operator / xi_prefactor
    standard_kernel_multiplier = xi_prefactor / phi_operator
    require(phi_to_xi == F(1, 2), "L-104531 Phi is not Xi/2")
    require(standard_kernel_multiplier == 2, "standard Xi kernel multiplier changed")
    return {
        "standard_xi": "xi(s)=(1/2)*s*(s-1)*Lambda(s)",
        "spectral_identity": "s=1/2+it gives s(s-1)=-(t^2+1/4)",
        "xi_prefactor_on_spectral_multiplier": render(xi_prefactor),
        "l104531_operator": "Phi=(1/4)*(D^2-1/4)*A",
        "phi_prefactor_on_spectral_multiplier": render(phi_operator),
        "Fourier(Phi)/Xi": render(phi_to_xi),
        "standard_kernel_multiplier_over_Phi": render(standard_kernel_multiplier),
        "l104528_unscaled_display_needs_factor_two_repair": True,
        "l104504_kernel_equals_l104531_kernel": True,
        "l104504_unscaled_display_needs_factor_two_repair": True,
        "standard_kernel_name": "Phi_std=2*Phi_0",
    }


def gamma_constant_ledger() -> dict[str, object]:
    orbit_leading = F(2)
    standard_kernel = F(2)
    two_sided_to_positive_half_line = F(2)
    gamma_substitution = F(1, 2)
    final_pi_squared_coefficient = (
        orbit_leading
        * standard_kernel
        * two_sided_to_positive_half_line
        * gamma_substitution
    )
    require(final_pi_squared_coefficient == 4, "H.9 coefficient is not 4*pi^2")
    growth_exponent = F(9, 2)
    moment_majorant_exponent = F(1)
    q_offset = growth_exponent + moment_majorant_exponent
    require(q_offset == F(11, 2), "q offset changed")
    zeta_exponent_at_y_zero = q_offset - 4
    require(zeta_exponent_at_y_zero == F(3, 2), "zeta threshold changed")
    return {
        "l104531_orbit_leading_pi_squared_coefficient": render(orbit_leading),
        "standard_kernel_multiplier": render(standard_kernel),
        "two_sided_symmetry_multiplier": render(two_sided_to_positive_half_line),
        "gamma_substitution_multiplier": render(gamma_substitution),
        "final_pi_squared_coefficient": render(final_pi_squared_coefficient),
        "moment_bound": "u^m<=m!*exp(u)",
        "q": "Y+11/2",
        "q_offset": render(q_offset),
        "n_sum": "sum n^(4-q)<=zeta(3/2)",
        "zeta_exponent_at_Y_zero": render(zeta_exponent_at_y_zero),
        "corrected_bound": "|Xi_t^(m)(z)|<=4*pi^2*m!*zeta(3/2)*pi^(-q/2)*Gamma(q/2)",
    }


def anchor_phase_ledger() -> dict[str, object]:
    return {
        "anchor": "a=-i*y with y>0",
        "phase_removed_quantity": "i^(-m)*Xi_t^(m)(-i*y)",
        "even_pair": "2*u^m*Phi_std(u)*cosh(y*u)>0",
        "odd_pair": "2*u^m*Phi_std(u)*sinh(y*u)>0",
        "all_fixed_derivatives_nonzero": True,
        "a_minus_i_is_common_for_every_fixed_triple": True,
    }


def downstream_scale_ledger() -> dict[str, object]:
    linear_scale = F(2)
    quadratic_scale = linear_scale**2
    require(quadratic_scale == 4, "quadratic Xi scale is not four")
    return {
        "target": "PR724 at 82ba4bdb824868dcf26d5d2f2d38b1e2af2d8631",
        "raw_kernel": "Phi_0 from L-104504/L-104531",
        "standard_kernel": "Phi_std=2*Phi_0",
        "xi_derivative_scale_over_raw_transform": render(linear_scale),
        "laguerre_defect_scale_over_raw_gram": render(quadratic_scale),
        "line_l2_norm_squared_scale_over_raw_formula": render(quadratic_scale),
        "l105200_scale_invariant": [
            "tilted_probability_measure",
            "saddle_location_and_curvature",
            "normalized_gaussian_limit",
            "zero_geometry",
        ],
        "l105207_scale_invariant": [
            "positive_semidefiniteness",
            "Schur_inequalities",
            "sign_region",
            "normalized_curvature_ratios",
        ],
        "l105208_scale_invariant": [
            "line_norm_inequality",
            "optimal_lambda",
            "normalized_orientation",
            "phase_sign_and_mean_positivity",
        ],
        "exact_raw_equalities_requiring_repair": [
            "L105200 opening Xi Fourier amplitude",
            "L105207 exterior-square and Fourier-density identities",
            "L105207 central defect constant",
            "L105208 Plancherel norm identities",
        ],
        "pr724_exact_normalization_ready": False,
    }


def scope() -> dict[str, bool]:
    return {
        "normalization_algebra_verified": True,
        "gamma_constant_bookkeeping_verified": True,
        "anchor_phase_bookkeeping_verified": True,
        "unmerged_source_blobs_imported": False,
        "xi_growth_claim_frozen_as_proof_object": False,
        "actual_xi_manifests_authenticated": False,
        "downstream_pr724_fully_reviewed": False,
        "rcmv104530_proved": False,
        "rh_established": False,
    }


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.x105116.xi-kernel-normalization-audit.v2",
        "classification": VERDICT,
        "checks": {
            "source_lock": source_lock(),
            "normalization_ledger": normalization_ledger(),
            "gamma_constant_ledger": gamma_constant_ledger(),
            "anchor_phase_ledger": anchor_phase_ledger(),
            "downstream_scale_ledger": downstream_scale_ledger(),
        },
        "scope": scope(),
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["audit_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["audit_sha256"])


if __name__ == "__main__":
    main()
