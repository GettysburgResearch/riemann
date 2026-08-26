from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym12_marked_valuation_kernel.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "genus2_sym12_marked_valuation_kernel", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load marked Sym12 valuation replay")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_exact_highest_weight_space_and_independent_rank() -> None:
    module = _load_module()
    domain, codomain, matrix = module.raising_matrix()
    nullspace = module.integer_nullspace_rows(matrix)

    assert len(domain) == 752
    assert len(codomain) == 686
    assert len(nullspace) == 66
    assert module.matrix_rank_mod_prime(matrix, 1_000_003) == 686
    assert (
        module.primitive_row_digest(nullspace)
        == "6f09eb35f716efab67f717cf55adcde1dab3e9fc11ef73747d41668f95d95c1e"
    )


def test_chart_orientation_and_twice_canonical_symmetrization() -> None:
    module = _load_module()

    assert module.selected_high_terms(0, 0, 0, "phi_prime") == ()
    assert module.selected_high_terms(9, 9, 9, "phi") == ()
    assert (0, 0, 0, 27, 2) in module.selected_high_terms(0, 0, 0, "phi")
    assert (0, 0, 0, 27, 2) in module.selected_high_terms(9, 9, 9, "phi_prime")
    assert (0, 0, 0, 27, 6) in module.complementary_high_terms(0, 0, 0, "phi")
    assert (0, 0, 0, 27, 6) in module.complementary_high_terms(9, 9, 9, "phi_prime")


def test_first_coefficient_min_linearizes_exactly() -> None:
    module = _load_module()
    domain, _, matrix = module.raising_matrix()
    nullspace = module.integer_nullspace_rows(matrix)
    vectors = module.basis_vectors(domain, nullspace)
    phi = module.chart_rows(vectors, "phi")
    phi_prime = module.chart_rows(vectors, "phi_prime")

    assert module.rank_rows_mod_prime(phi.values(), 66, 1_000_003) == 66
    assert module.rank_rows_over_q(phi_prime.values(), 66) == 5
    assert (
        module.rank_rows_over_q(list(phi.values()) + list(phi_prime.values()), 66) == 66
    )


def test_committed_full_matrix_certificate() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    model = payload["highest_weight_model"]
    matrix = payload["representative_boundary_valuation"]["combined_matrix"]
    valuation = payload["representative_boundary_valuation"]
    containing = valuation["containing_mark_chart_containments"]
    avoiding = valuation["avoiding_mark_chart_containments"]

    assert model["nullity"] == 66
    assert matrix == {
        "columns": 66,
        "nullity": 0,
        "rowwise_primitive_rational_kernel_basis_sha256": (
            "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
        ),
        "rank_mod_1000003": 66,
        "rank_mod_1000033": 66,
        "rank_over_Q": 66,
        "rows": 9902,
    }
    assert all(
        row["rank_stacked_over_Q"]
        == max(row["rank_phi_over_Q"], row["rank_phi_prime_over_Q"])
        for row in containing + avoiding
    )
    assert containing[6]["rank_phi_over_Q"] == 51
    assert containing[6]["rank_phi_prime_over_Q"] == 51
    assert avoiding[6]["rank_phi_over_Q"] == 53
    assert avoiding[6]["rank_phi_prime_over_Q"] == 53


def _control(module, d: int, b: int) -> tuple[int, int, int]:
    module.configure_parameters(d, b)
    domain, _, matrix = module.raising_matrix()
    highest = module.integer_nullspace_rows(matrix)
    valuation = module.valuation_analysis(domain, highest)
    combined = valuation["combined_matrix"]
    return len(highest), combined["rank_over_Q"], combined["nullity"]


def test_small_controls_detect_the_missing_orientation() -> None:
    module = _load_module()
    assert _control(module, 4, 6) == (6, 6, 0)
    assert _control(module, 7, 4) == (18, 18, 0)


def test_weight_2_11_calibration_matches_the_primary_dimension() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    controls = {(row["d"], row["b"]): row for row in payload["calibration_controls"]}
    control = controls[(12, 2)]
    assert control["highest_weight_dimension"] == 38
    assert control["corrected_rank"] == 36
    assert control["corrected_nullity"] == 2
    assert (
        control["kernel_sha256"]
        == "ce4cbd1e53811943c87c7fad2ffefdf785e19eba084f4c382ef173ccbe809095"
    )


def test_resource_firewall() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    caps = payload["resource_caps"]
    assert caps["point_counts"] == 0
    assert caps["partitions_computed"] == 1
    assert caps["largest_weight_state_space"] == 752
    assert caps["wall_clock_target_enforced"] is False
    assert caps["oriented_blocks_per_partition"] == 2
    assert caps["wall_clock_target_seconds"] == 300
