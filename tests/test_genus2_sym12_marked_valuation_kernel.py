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
    containments = payload["representative_boundary_valuation"][
        "chart_kernel_containment_for_j_0_through_6"
    ]

    assert model["nullity"] == 66
    assert matrix == {
        "columns": 66,
        "nullity": 15,
        "rowwise_primitive_rational_kernel_basis_sha256": (
            "1326459cad19fcf373b6d4364acfc5597acb9799d5fbb87ca4c8e905fd8ce95d"
        ),
        "rank_mod_1000003": 51,
        "rank_mod_1000033": 51,
        "rank_over_Q": 51,
        "rows": 3481,
    }
    assert all(
        row["rank_stacked_over_Q"] == row["rank_phi_over_Q"] for row in containments
    )
    assert containments[-1]["rank_phi_over_Q"] == 51
    assert containments[-1]["rank_phi_prime_over_Q"] == 51


def test_resource_firewall() -> None:
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    caps = payload["resource_caps"]
    assert caps["point_counts"] == 0
    assert caps["partitions_computed"] == 1
    assert caps["largest_weight_state_space"] == 752
    assert caps["wall_clock_target_enforced"] is False
    assert caps["wall_clock_target_seconds"] == 60
