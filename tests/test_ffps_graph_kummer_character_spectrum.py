from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_graph_kummer_character_spectrum.py"
)
NOTE = SCRIPT.with_name("FFPS_GRAPH_KUMMER_CHARACTER_SPECTRUM.md")


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "ffps_graph_kummer_character_spectrum", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load graph Kummer spectrum replay")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MODULE = _load_module()


def test_disconnected_admissibility_and_uniform_fibers() -> None:
    census = MODULE.exact_fiber_census(4, ((0, 1), (2, 3)))
    assert census["component_count"] == 2
    assert census["incidence_rank"] == 2
    assert census["cycle_dimension"] == 0
    assert census["admissible_boundary_patterns"] == 4
    assert census["fiber_size"] == 1
    assert census["nontrivial_invariant_modes"] == 0


def test_cycle_space_is_exact_invariant_kernel() -> None:
    triangle = ((0, 1), (1, 2), (0, 2))
    census = MODULE.exact_fiber_census(3, triangle)
    assert census["incidence_rank"] == 2
    assert census["cycle_dimension"] == 1
    assert census["fiber_size"] == 2
    assert census["invariant_modes"] == 2
    assert census["nontrivial_invariant_modes"] == 1
    assert census["top_invariant"]


def test_connected_branch_and_betti_spectrum_closes() -> None:
    spectrum = MODULE.connected_branch_betti_spectrum(3, 3, 2)
    assert [row["multiplicity"] for row in spectrum["rows"]] == [2, 6]
    assert [row["geometric_branch_points"] for row in spectrum["rows"]] == [0, 4]
    assert spectrum["closed_totals"] == {
        "all_modes": 8,
        "invariant_modes": 2,
        "nontrivial_invariant_modes": 1,
        "nonconstant_modes": 6,
        "geometric_branch_points_across_all_modes": 24,
        "minimal_h1_across_all_modes": 12,
        "minimal_h2_across_all_modes": 2,
        "common_open_h1_across_all_modes": 34,
        "nonconstant_removable_puncture_tax": 12,
    }


def test_tree_topology_only_relocates_distinguished_top_mode() -> None:
    path = ((0, 1), (1, 2), (2, 3), (3, 4))
    star = ((0, 1), (0, 2), (0, 3), (0, 4))
    path_profile = MODULE.graph_profile(5, path)
    star_profile = MODULE.graph_profile(5, star)
    assert path_profile["cycle_dimension"] == star_profile["cycle_dimension"] == 0
    assert path_profile["top_boundary_vertices"] == 2
    assert star_profile["top_boundary_vertices"] == 4
    path_census = MODULE.exact_fiber_census(5, path)
    star_census = MODULE.exact_fiber_census(5, star)
    assert (
        path_census["branch_vertex_histogram"]
        == star_census["branch_vertex_histogram"]
        == {0: 1, 2: 10, 4: 5}
    )


def test_mask_transversality_full_and_broken_cycle() -> None:
    cycle = ((0, 1), (1, 2), (2, 3), (3, 4), (0, 4))
    full = MODULE.mask_transversality_profile(
        5, cycle, tuple(1 << edge for edge in range(5))
    )
    broken = MODULE.mask_transversality_profile(
        5, cycle, tuple(1 << edge for edge in range(4))
    )
    cycle_only = MODULE.mask_transversality_profile(5, cycle, ((1 << 5) - 1,))
    assert full["mask_cycle_intersection_dimension"] == 1
    assert full["invariant_nontrivial_selected_modes"] == 1
    assert not full["boundary_restriction_injective"]
    assert broken["mask_cycle_intersection_dimension"] == 0
    assert broken["invariant_nontrivial_selected_modes"] == 0
    assert broken["boundary_restriction_injective"]
    assert cycle_only["mask_dimension"] == 1
    assert cycle_only["boundary_image_dimension"] == 0


def test_exhaustive_connected_graph_census() -> None:
    census = MODULE.connected_graph_census()
    assert census["connected_graphs"] == 771
    assert census["edge_subset_evaluations"] == 55_894
    assert census["rows"] == [
        {"vertex_count": 2, "connected_graphs": 1, "trees": 1, "paths": 1},
        {"vertex_count": 3, "connected_graphs": 4, "trees": 3, "paths": 3},
        {"vertex_count": 4, "connected_graphs": 38, "trees": 16, "paths": 12},
        {"vertex_count": 5, "connected_graphs": 728, "trees": 125, "paths": 60},
    ]


def test_report_firewalls_and_resource_caps() -> None:
    report = MODULE.run_checks()
    assert report["status"] == "EXACT_GRAPH_KUMMER_CHARACTER_SPECTRUM"
    assert report["resource_ledger"]["finite_fields_enumerated"] == 0
    assert (
        report["resource_ledger"]["edge_subset_evaluations"]
        < report["resource_ledger"]["edge_subset_evaluations_cap"]
    )
    assert any("formal edge Fourier modes" in row for row in report["firewalls"])


def test_input_validation() -> None:
    try:
        MODULE.graph_profile(3, ((0, 1),))
    except ValueError:
        pass
    else:
        raise AssertionError("isolated vertex was accepted")
    try:
        MODULE.mask_transversality_profile(2, ((0, 1),), (2,))
    except ValueError:
        pass
    else:
        raise AssertionError("out-of-range mask generator was accepted")


def test_optimized_cli() -> None:
    completed = subprocess.run(
        [sys.executable, "-O", str(SCRIPT), "--check"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=10.0,
    )
    assert "EXACT_GRAPH_KUMMER_CHARACTER_SPECTRUM" in completed.stdout
    assert "No external novelty or priority claim" in NOTE.read_text(encoding="utf-8")
