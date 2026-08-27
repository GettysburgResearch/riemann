from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_marked_place_bifrobenius_gluing_gate.py"
)
SPEC = importlib.util.spec_from_file_location("marked_place_bifrobenius", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class MarkedPlaceBifrobeniusGluingGateTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_mobius_and_irreducible_counts(self) -> None:
        self.assertEqual(
            [subject.mobius(value) for value in range(1, 11)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
        )
        self.assertEqual(
            [subject.irreducible_count(3, degree) for degree in range(1, 7)],
            [3, 3, 8, 18, 48, 116],
        )

    def test_internal_rank_is_not_marked_block_rank(self) -> None:
        control = subject.marked_block_correction_control()
        self.assertEqual(control["internal_left_matrix_rank"], 2)
        self.assertEqual(control["internal_right_matrix_rank"], 3)
        self.assertEqual(control["marked_place_block_separation_rank"], 1)

    def test_simultaneous_frobenius_uses_correct_axes(self) -> None:
        control = subject.simultaneous_frobenius_control(3)
        self.assertTrue(control["trace_invariant_under_simultaneous_block_frobenius"])
        self.assertTrue(control["simultaneous_reduced_support_preserved"])
        self.assertFalse(control["one_axis_reduced_support_preserved"])
        self.assertEqual(control["simultaneous_image"], "(h*Y)^q")

    def test_crossed_incidence_allocation_trilemma(self) -> None:
        control = subject.crossed_incidence_control(5)
        self.assertFalse(control["root_only_support_preserved"])
        self.assertFalse(control["coefficient_only_support_preserved"])
        self.assertEqual(len(control["allocation_trilemma"]), 3)
        crossed = {row["crossed_object"] for row in control["allocation_trilemma"]}
        self.assertTrue(any("ell divides c" in item for item in crossed))
        self.assertTrue(any("equality diagonal" in item for item in crossed))

    def test_frozen_source_cost_is_explicitly_conditional(self) -> None:
        panel = subject.frozen_source_cost_panel()
        self.assertEqual(panel["rows"][-1]["identity_incidence_submatrix_rank"], 116)
        self.assertIn("not an occupancy theorem", panel["conditional_scope"])
        self.assertIn("source-cardinality", panel["finite_horizon_escape"])

    def test_graph_shift_escape_keeps_the_firewall(self) -> None:
        control = subject.graph_shift_control()
        self.assertEqual(control["distinct_through_depth"], 5)
        self.assertEqual(control["left_nonzero_mobius_slots"], 8)
        self.assertEqual(control["right_nonzero_mobius_slots"], 8)
        self.assertEqual(control["double_nonzero_mobius_slots"], 64)
        self.assertIn("not a closed-point trace theorem", control["firewall"])

    def test_source_partition_places_local_constituents_correctly(self) -> None:
        partition = subject.source_factor_partition()
        self.assertIn("Y=Q*d^2 mod ell", partition["marked_place_blocks"]["ell"])
        self.assertIn("X=P*c^2 mod rho", partition["marked_place_blocks"]["rho"])
        self.assertTrue(
            any("ell=P^-(c)" in edge for edge in partition["crossed_edges"])
        )

    def test_fixture_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        frontier = result["conditional_signed_pushforward_frontier"]
        self.assertEqual(
            frontier["exotic_structure_after_complete_signed_pushforward"],
            "OPEN / NOT RULED OUT",
        )
        ledger = result["proof_ledger"]
        self.assertEqual(
            ledger["full_native_commuting_partial_frobenii"], "NOT CONSTRUCTED"
        )
        self.assertEqual(
            ledger["absolute_nonexistence_after_signed_pushforward"], "NOT PROVED"
        )
        self.assertEqual(result["resource_caps"]["finite_field_element_enumeration"], 0)

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            subject.centered_incidence(3, 4)
        with self.assertRaises(ValueError):
            subject.irreducible_count(1, 2)
        with self.assertRaises(ValueError):
            subject.simultaneous_frobenius_control(1)
        with self.assertRaises(ValueError):
            subject.mobius(0)


if __name__ == "__main__":
    unittest.main()
