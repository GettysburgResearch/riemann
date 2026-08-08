from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_script(name: str) -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(ROOT / name)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_exact_dyadic_carry_bridge() -> None:
    result = run_script("verify.py")
    assert (
        result["sha256_without_digest"]
        == "dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715"
    )
    assert result["checks"]["average_rank_one_collapse"]["cases"] == 12879
    assert (
        result["checks"]["pointwise_two_contact"]["pointwise_cases"]
        == 13038
    )
    assert all(
        row["energy"] == 5
        for row in result["checks"]["unprojected_green_two_charge"]["instances"]
    )


def test_exact_bottom_charge_and_flow_invisibility() -> None:
    result = run_script("verify_bottom_charge.py")
    assert (
        result["sha256_without_digest"]
        == "395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f"
    )
    assert (
        result["classification"]
        == "PASS_EXACT_DYADIC_BOTTOM_CHARGE_AND_FLOW_INVISIBILITY"
    )
    assert all(
        row["high_index_flow_delta"] == {"numerator": 0, "denominator": 1}
        for row in result["rows"]
    )


def test_exact_digital_half_scale_lift() -> None:
    result = run_script("verify_digital_lift.py")
    assert (
        result["sha256_without_digest"]
        == "17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23"
    )
    assert (
        result["classification"]
        == "PASS_EXACT_ODD_ROW_EVEN_COLUMN_CARRY_ISOMETRY"
    )
    assert result["pointwise_duplicate_cases"] == 3780
    assert result["average_cells"] == 1830
    assert result["hermitian_rows"] == 60
    assert result["even_row_mutation_rejected"] is True


def test_factor_five_pointwise_dipole() -> None:
    result = run_script("verify_factor_five.py")
    assert (
        result["sha256_without_digest"]
        == "b2ff53b948da65a81082fa9a14d7f990c227bb47a6bb592458655ccec7a03f95"
    )
    assert result["checks"]["scaled_b2_box_profile"]["cases"] == 386270
    assert result["checks"]["pointwise_omega2_wavelet"]["cases"] == 386270
    assert result["checks"]["factor_five_kummer_nonnegativity"]["cases"] == 2505
    assert result["checks"]["odd_pointwise_carry"]["cases"] == 13040
    assert result["checks"]["transition_negative_examples"]["count"] > 0


def test_uniform_carry_schur_structure() -> None:
    result = run_script("verify_schur_structure.py")
    assert (
        result["sha256_without_digest"]
        == "fe8287748e6c2e7320ca24e8db827044d77511dc2a72e401afb91a90e11365f0"
    )
    assert result["checks"]["rows"]["count"] == 113515
    assert result["checks"]["rows"]["n_min"] == 210
    assert result["checks"]["rows"]["n_max"] == 520
    assert result["checks"]["maximum_wavelet_breaks"]["count"] <= 6
    assert (
        result["checks"]["reserve_denominator"]["value"]
        >= result["checks"]["exact_required_denominator"]["value"]
    )


def test_positive_inverse_wavelet_synthesis() -> None:
    result = run_script("verify_positive_synthesis.py")
    assert (
        result["sha256_without_digest"]
        == "11e5e76a49b49ab2f838d7a829936b4e46bed5482c0d0a717fb4161f6b99eeda"
    )
    assert result["checks"]["positive_inverse_convolution"]["cases"] == 100
    assert (
        result["checks"]["generalized_von_mangoldt_convolution"]["cases"]
        == 100
    )
    assert result["checks"]["positive_wavelet_synthesis"]["cases"] == 5148
    assert result["checks"]["digital_prime_correction"]["cases"] == 5148


def test_selberg_carry_moment_tower() -> None:
    result = run_script("verify_moment_tower.py")
    assert (
        result["sha256_without_digest"]
        == "eaaed5595e09e6b7d0f9fd990f42bea3e99d4c4e180fd04d78b7d2fa8434c2af"
    )
    assert (
        result["classification"]
        == "PASS_EXACT_SELBERG_CARRY_MOMENT_TOWER_AND_BOUNDARY_FIREWALL"
    )
    assert result["checks"]["convolutions"]["rows"] == 72
    assert result["checks"]["moment_tower"]["pointwise_cells"] == 2698
    assert (
        result["checks"]["moment_tower"]["nonzero_unit_boundary_cells"]
        == 411
    )
    assert (
        result["checks"]["moment_tower"]["coefficient_mutation_rejected"]
        == 1
    )
