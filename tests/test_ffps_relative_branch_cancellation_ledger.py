from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_relative_branch_cancellation_ledger.py"
)
SPEC = importlib.util.spec_from_file_location("relative_branch_ledger", MODULE_PATH)
assert SPEC and SPEC.loader
relative_branch_ledger = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(relative_branch_ledger)


class RelativeBranchCancellationLedgerTest(unittest.TestCase):
    def test_every_nonzero_inertia_vector_has_same_census(self) -> None:
        for blocks in range(1, 9):
            size = 2**blocks
            for inertia_vector in range(1, size):
                counts = relative_branch_ledger.character_counts(blocks, inertia_vector)
                self.assertEqual(counts["hard_trivial"], size // 2)
                self.assertEqual(counts["hard_sign"], size // 2)
                self.assertEqual(counts["selected_trivial"], size // 2 - 1)
                self.assertEqual(counts["selected_sign"], size // 2)

    def test_unnormalized_relative_is_exactly_principal(self) -> None:
        for blocks in range(1, 11):
            ledger = relative_branch_ledger.local_inertia_ledger(blocks)
            relative = ledger["objects"]["relative_C_minus_S"]
            self.assertEqual(relative["trivial_coefficient"], "1")
            self.assertEqual(relative["sign_coefficient"], "0")
            self.assertEqual(relative["virtual_rank"], "1")
            self.assertEqual(relative["signed_tame_artin_conductor"], "0")

    def test_normalized_variants_do_not_share_the_cancellation(self) -> None:
        for blocks in range(1, 11):
            size = 2**blocks
            ledger = relative_branch_ledger.local_inertia_ledger(blocks)
            objects = ledger["objects"]
            atom_free = objects["atom_free_Pi0_minus_normalized_selected_average"]
            self.assertEqual(
                Fraction(atom_free["sign_coefficient"]),
                Fraction(-size, 2 * (size - 1)),
            )
            self.assertEqual(atom_free["virtual_rank"], "0")

            hard_minus_average = objects["C_minus_normalized_selected_average"]
            expected = Fraction(size * (size - 2), 2 * (size - 1))
            self.assertEqual(Fraction(hard_minus_average["sign_coefficient"]), expected)

    def test_zero_extension_retains_one_degree_per_boundary_point(self) -> None:
        for blocks in range(1, 11):
            ledger = relative_branch_ledger.extension_ledger(blocks, 37)
            self.assertEqual(ledger["relative_zero_extension_conductor_degree"], 37)
            self.assertEqual(ledger["relative_middle_extension_conductor_degree"], 0)
            self.assertEqual(ledger["boundary_skyscraper_length"], 37)
            rows = ledger["rows"]
            self.assertEqual(
                rows["hard_C"]["middle_extension_conductor_coefficient"],
                rows["unnormalized_selected_S"][
                    "middle_extension_conductor_coefficient"
                ],
            )

    def test_boundary_trace_tower(self) -> None:
        degrees = (3, 5, 11)
        self.assertEqual(relative_branch_ledger.boundary_trace(degrees, 1), 0)
        self.assertEqual(relative_branch_ledger.boundary_trace(degrees, 15), 8)
        self.assertEqual(relative_branch_ledger.boundary_trace(degrees, 33), 14)
        self.assertEqual(relative_branch_ledger.boundary_trace(degrees, 55), 16)
        self.assertEqual(relative_branch_ledger.boundary_trace(degrees, 165), 19)

    def test_input_firewalls_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            relative_branch_ledger.local_inertia_ledger(0)
        with self.assertRaises(ValueError):
            relative_branch_ledger.local_inertia_ledger(2, 4)
        with self.assertRaises(ValueError):
            relative_branch_ledger.extension_ledger(2, 0)
        with self.assertRaises(ValueError):
            relative_branch_ledger.boundary_trace((), 1)
        caps = relative_branch_ledger.run()["resource_caps"]
        self.assertEqual(caps["finite_field_points"], 0)
        self.assertEqual(caps["curves_or_pushforwards_computed"], 0)


if __name__ == "__main__":
    unittest.main()
