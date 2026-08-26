"""Tests for the telescoping checkerboard curve model."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_checkerboard_telescoping_curve_model.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_CHECKERBOARD_TELESCOPING_CURVE_MODEL.md")

SPEC = importlib.util.spec_from_file_location("ffps_telescoping_curve", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load telescoping curve module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CheckerboardTelescopingCurveModelTests(unittest.TestCase):
    def test_bounded_replay(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(report["status"], "EXACT_GRAPH_OPTIMIZED_TELESCOPING_MODEL")
        self.assertEqual(report["rows"], 512)
        self.assertEqual(report["labelled_tree_profiles"], 1441)

    def test_irreducible_count_controls(self) -> None:
        self.assertEqual(MODULE.irreducible_count(3, 1), 3)
        self.assertEqual(MODULE.irreducible_count(3, 2), 3)
        self.assertEqual(MODULE.irreducible_count(3, 3), 8)
        self.assertEqual(MODULE.irreducible_count(5, 2), 10)

    def test_path_rank_and_telescoping(self) -> None:
        for path_length in range(1, 40):
            row, _ = MODULE.path_model(5, path_length)
            self.assertEqual(row["geometric_deck_group_f2_rank"], path_length)
            self.assertEqual(row["top_character_rank"], 1)
            self.assertEqual(row["top_invariants"], 0)

    def test_graph_rank_parity_and_optimizer_controls(self) -> None:
        path = MODULE.graph_profile(
            6, tuple((vertex, vertex + 1) for vertex in range(5)), 3
        )
        star = MODULE.graph_profile(6, tuple((0, vertex) for vertex in range(1, 6)), 3)
        cycle = MODULE.graph_profile(
            6, tuple((vertex, (vertex + 1) % 6) for vertex in range(6)), 3
        )
        self.assertEqual(path["incidence_rank"], 5)
        self.assertTrue(path["full_edge_rank"])
        self.assertTrue(path["is_path"])
        self.assertEqual(path["odd_vertex_count"], 2)
        self.assertEqual(path["geometric_branch_points"], 6)
        self.assertEqual(path["removable_puncture_tax"], 12)
        self.assertEqual(star["incidence_rank"], 5)
        self.assertTrue(star["full_edge_rank"])
        self.assertFalse(star["is_path"])
        self.assertEqual(star["odd_vertex_count"], 6)
        self.assertEqual(star["removable_puncture_tax"], 0)
        self.assertEqual(cycle["incidence_rank"], 5)
        self.assertFalse(cycle["full_edge_rank"])
        self.assertTrue(cycle["top_invariant"])
        self.assertEqual(cycle["minimal_top_h2"], 1)
        self.assertEqual(cycle["common_open_h1"], 17)
        self.assertIsNone(cycle["removable_puncture_tax"])

    def test_all_small_labelled_trees_have_two_odds_exactly_for_paths(self) -> None:
        rows, profiles = MODULE.labelled_tree_census()
        self.assertEqual(profiles, 1441)
        self.assertEqual(
            [(row["labelled_trees"], row["path_labelings"]) for row in rows],
            [(1, 1), (3, 3), (16, 12), (125, 60), (1296, 360)],
        )

    def test_prufer_decoder_control(self) -> None:
        self.assertEqual(
            MODULE.prufer_tree((0, 0, 0)),
            ((0, 1), (0, 2), (0, 3), (0, 4)),
        )

    def test_exact_puncture_tax(self) -> None:
        for field_size in (3, 5, 7):
            for path_length in (1, 2, 5, 17, 64):
                row, _ = MODULE.path_model(field_size, path_length)
                self.assertEqual(
                    row["common_open_h1"] - row["minimal_open_h1"],
                    row["removable_puncture_tax"],
                )
                self.assertEqual(
                    row["removable_puncture_tax"],
                    (path_length - 1) * row["e_q_d"],
                )

    def test_boundary_tower_even_step_is_sign_independent(self) -> None:
        for signs in ((1, 1, 1), (1, -1, 1), (-1, -1, -1)):
            self.assertEqual(
                MODULE.boundary_trace_difference(5, 10, signs),
                5 * len(signs),
            )
            self.assertEqual(
                MODULE.boundary_trace_difference(5, 20, signs),
                5 * len(signs),
            )

    def test_boundary_tower_odd_step_retains_signs(self) -> None:
        signs = (1, -1, -1, 1, 1)
        self.assertEqual(MODULE.boundary_trace_difference(3, 3, signs), 3 * sum(signs))
        self.assertEqual(MODULE.boundary_trace_difference(3, 4, signs), 0)

    def test_rational_endpoint_row_has_zero_minimal_cohomology(self) -> None:
        row, _ = MODULE.path_model(5, 4)
        self.assertEqual(row["e_q_d"], 1)
        self.assertEqual(row["minimal_open_h1"], 0)
        self.assertEqual(row["common_open_h1"], 3)

    def test_fixed_q_degree_grows_slowly(self) -> None:
        rows = [
            MODULE.path_model(3, path_length)[0] for path_length in (4, 16, 64, 128)
        ]
        degrees = [row["e_q_d"] for row in rows]
        self.assertEqual(degrees, sorted(degrees))
        self.assertLessEqual(degrees[-1], 7)

    def test_invalid_inputs_fail_closed(self) -> None:
        for value in (0, True, -1):
            with self.assertRaises(ValueError):
                MODULE.divisors(value)
        with self.assertRaises(ValueError):
            MODULE.irreducible_count(True, 2)
        with self.assertRaises(ValueError):
            MODULE.irreducible_count(2, 2)
        with self.assertRaises(ValueError):
            MODULE.irreducible_count(15, 2)
        with self.assertRaises(ValueError):
            MODULE.irreducible_count(3, 0)
        with self.assertRaises(ValueError):
            MODULE.minimal_closed_place_degree(3, 0)
        with self.assertRaises(ValueError):
            MODULE.boundary_trace_difference(0, 2, (1,))
        with self.assertRaises(ValueError):
            MODULE.boundary_trace_difference(2, 0, (1,))
        with self.assertRaises(ValueError):
            MODULE.boundary_trace_difference(2, 2, (0,))
        with self.assertRaises(ValueError):
            MODULE.graph_profile(3, ((0, 1),))
        with self.assertRaises(ValueError):
            MODULE.graph_profile(3, ((0, 1), (1, 0), (1, 2)))
        with self.assertRaises(ValueError):
            MODULE.prufer_tree((4,))

    def test_optimized_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_GRAPH_OPTIMIZED_TELESCOPING_MODEL", completed.stdout)

    def test_note_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "imported, not reproved",
            "legal for the arithmetic source",
            "not place the Gram panel and the path torsor inside the same native",
            "Graph optimizer",
            "OPEN / CENTRAL GATE",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
