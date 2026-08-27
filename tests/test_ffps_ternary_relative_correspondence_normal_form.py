from __future__ import annotations

import importlib.util
import json
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
    / "ffps_ternary_relative_correspondence_normal_form.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ternary_relative_correspondence_normal_form", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class TernaryRelativeCorrespondenceNormalFormTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_balanced_clean_physical_occupancy(self) -> None:
        labels = subject.bilateral_labels(7, 13)
        self.assertEqual(len(labels), 18)
        self.assertEqual([labels.count(value) for value in range(3)], [6, 6, 6])
        with self.assertRaises(ValueError):
            subject.bilateral_labels(7, 13, alignment=0)
        with self.assertRaises(ValueError):
            subject.balanced_ternary_labels(11)
        with self.assertRaises(ValueError):
            subject.balanced_ternary_labels(55)
        self.assertEqual(subject.sign_pair_count(49), 24)

    def test_exact_pre_externalization_relative_kernel(self) -> None:
        labels = subject.bilateral_labels(7, 7)
        hard, selected, relative = subject.ternary_covariance_kernels(labels)
        self.assertEqual(subject.subtract(hard, selected), relative)
        self.assertEqual(
            {value for row in hard for value in row}, {Fraction(3, 2), Fraction(3, 4)}
        )
        self.assertEqual(
            {value for row in selected for value in row},
            {Fraction(1, 2), Fraction(-1, 4)},
        )
        self.assertEqual(subject.matrix_rank(hard), 3)
        self.assertEqual(subject.matrix_rank(selected), 2)
        self.assertEqual(subject.matrix_rank(relative), 1)

    def test_common_native_lift_preserves_full_rank(self) -> None:
        for left, right, expected in ((7, 7, 9), (7, 13, 18)):
            with self.subTest(left=left, right=right):
                panel = subject.ternary_relative_panel(left, right)
                self.assertEqual(panel["cell_count"], expected)
                self.assertEqual(
                    panel["native_coupled_ranks"],
                    {
                        "hard": expected,
                        "relative": expected,
                        "selected": expected,
                        "wick_relative": expected,
                    },
                )
                self.assertEqual(
                    panel["pair_support"]["hard"],
                    panel["pair_support"]["total_pairs"],
                )
                self.assertEqual(
                    panel["pair_support"]["selected"],
                    panel["pair_support"]["total_pairs"],
                )

    def test_each_hard_rotation_is_two_thirds_but_full_rank_on_its_support(
        self,
    ) -> None:
        panel = subject.ternary_relative_panel(7, 13)
        self.assertEqual(panel["hard_rotation_support_sizes"], [12, 12, 12])
        self.assertEqual(panel["hard_rotation_support_ranks"], [12, 12, 12])

    def test_literal_atomic_deletion_commutes_with_relative_difference(self) -> None:
        labels = subject.bilateral_labels(7, 13)
        hard, selected, _ = subject.ternary_covariance_kernels(labels)
        native = subject.kronecker(
            subject.centered_phase_gram(7), subject.centered_phase_gram(13)
        )
        hard_native = subject.hadamard(native, hard)
        selected_native = subject.hadamard(native, selected)
        relative = subject.subtract(
            subject.delete_atomic_diagonal(hard_native),
            subject.delete_atomic_diagonal(selected_native),
        )
        self.assertEqual(relative, subject.delete_atomic_diagonal(native))
        self.assertEqual(subject.matrix_rank(relative), 18)

    def test_source_image_rank_equals_distinct_occupancy_before_wick(self) -> None:
        row = subject.source_image_rank_certificate()
        self.assertEqual(row["atom_count"], 7)
        self.assertEqual(row["occupied_cell_count"], 5)
        self.assertEqual(
            row["pullback_ranks"], {"hard": 5, "relative": 5, "selected": 5}
        )

    def test_frobenius_graph_orbit_has_linear_dimension_growth(self) -> None:
        row = subject.correspondence_orbit(7, 5)
        self.assertEqual(row["centered_orbit_dimension"], 6)
        self.assertEqual(row["with_background_dimension"], 7)
        self.assertEqual(
            row["graph_signatures"],
            [(1, 1), (7, 1), (49, 1), (343, 1), (2401, 1), (16807, 1)],
        )
        with self.assertRaises(ValueError):
            subject.correspondence_orbit(7, -1)

    def test_formal_divisor_shift_ledger_is_sparse_and_fenced(self) -> None:
        row = subject.formal_divisor_shift_ledger(6, 10)
        self.assertEqual(row["left_nonzero_mobius_divisors"], 4)
        self.assertEqual(row["right_nonzero_mobius_divisors"], 4)
        self.assertEqual(row["top_graph_products"], 16)
        self.assertEqual(row["surviving_support_components"], 16)
        self.assertEqual(row["left_axis_coefficient_factor"], 0)
        self.assertEqual(row["right_axis_coefficient_factor"], 0)
        self.assertIn("not a closed-point Adams theorem", row["formal_warning"])

    def test_full_fixture_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        self.assertFalse(
            result["partial_frobenius_and_correspondences"][
                "commuting_partial_frobenius_created"
            ]
        )
        self.assertFalse(
            result["partial_frobenius_and_correspondences"][
                "finite_dimensional_graph_closure"
            ]
        )
        self.assertEqual(
            result["proof_ledger"]["native_closed_point_adams_formula"],
            "NOT CONSTRUCTED",
        )
        self.assertEqual(
            result["proof_ledger"]["live_source_occupancy_lower_bound"],
            "OPEN / NOT CLAIMED",
        )
        self.assertEqual(result["resource_caps"]["largest_exact_matrix_dimension"], 18)


if __name__ == "__main__":
    unittest.main()
