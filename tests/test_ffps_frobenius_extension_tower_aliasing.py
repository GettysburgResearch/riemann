from __future__ import annotations

import importlib.util
import json
import math
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
    / "ffps_frobenius_extension_tower_aliasing.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ffps_frobenius_extension_tower_aliasing", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FrobeniusExtensionTowerAliasingTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_exact_frobenius_cycle_inventory(self) -> None:
        self.assertEqual(subject.frobenius_cycle_counts(2, 3), {1: 2, 3: 2})
        self.assertEqual(subject.frobenius_cycle_counts(2, 4), {1: 2, 2: 1, 4: 3})
        for extension_degree in range(1, 9):
            counts = subject.frobenius_cycle_counts(2, extension_degree)
            self.assertEqual(
                sum(degree * count for degree, count in counts.items()),
                2**extension_degree,
            )

    def test_scalar_trace_and_pointwise_levels_are_distinct(self) -> None:
        permutation = subject.frobenius_permutation(2, 3)
        kernel_one = subject.centered_graph_kernel(2, 3, 1)
        kernel_two = subject.centered_graph_kernel(2, 3, 2)
        kernel_four = subject.centered_graph_kernel(2, 3, 4)
        self.assertEqual(subject.entry_sum(permutation), 8)
        self.assertEqual(subject.entry_sum(kernel_one), 0)
        self.assertEqual(subject.matrix_trace(kernel_one), 1)
        self.assertEqual(subject.matrix_trace(kernel_two), 1)
        self.assertNotEqual(kernel_one, kernel_two)
        self.assertEqual(kernel_one, kernel_four)

    def test_centered_rank_and_cyclic_multiplication(self) -> None:
        for power in range(7):
            kernel = subject.centered_graph_kernel(2, 4, power)
            self.assertEqual(subject.matrix_rank(kernel), 15)
            self.assertEqual(
                subject.matrix_trace(kernel),
                Fraction(2 ** math.gcd(power, 4) - 1),
            )
        self.assertEqual(
            subject.matrix_multiply(
                subject.centered_graph_kernel(2, 4, 3),
                subject.centered_graph_kernel(2, 4, 6),
            ),
            subject.centered_graph_kernel(2, 4, 9),
        )

    def test_cyclic_algebra_has_exact_dimension(self) -> None:
        for extension_degree in range(1, 6):
            flattened = tuple(
                tuple(
                    value
                    for row in subject.centered_graph_kernel(2, extension_degree, power)
                    for value in row
                )
                for power in range(extension_degree)
            )
            self.assertEqual(subject.matrix_rank(flattened), extension_degree)

    def test_closed_point_mobius_orientation_and_aliases(self) -> None:
        self.assertEqual(
            subject.mobius_divisor_terms(12),
            ((12, 1), (6, -1), (4, -1), (2, 1)),
        )
        nonzero = subject.permutation_polynomial_action(2, 3, 5)
        invisible = subject.permutation_polynomial_action(2, 3, 7)
        self.assertFalse(subject.matrix_is_zero(nonzero))
        self.assertEqual(subject.matrix_rank(nonzero), 4)
        self.assertEqual(subject.matrix_trace(nonzero), 0)
        self.assertEqual(subject.entry_sum(nonzero), 0)
        self.assertTrue(subject.matrix_is_zero(invisible))

    def test_prime_mobius_rank_formula(self) -> None:
        for prime in (2, 3, 5, 7, 11):
            for extension_degree in range(1, 6):
                action = subject.permutation_polynomial_action(
                    2, extension_degree, prime
                )
                self.assertEqual(
                    subject.matrix_rank(action),
                    subject.prime_mobius_rank_formula(2, extension_degree, prime),
                )

    def test_tower_capacity_and_label_fidelity_are_different(self) -> None:
        first = subject.tower_certificate(30, (2, 3, 5))
        self.assertTrue(first["pointwise_labels_distinct"])
        self.assertEqual(first["centered_algebra_dimension"], 8)
        self.assertEqual(first["divisor_grid_size"], 8)
        self.assertEqual(first["linear_grid_rank"], 7)
        self.assertFalse(first["linear_grid_faithful"])
        self.assertTrue(first["action_visible"])

    def test_extra_level_can_restore_full_grid_fidelity(self) -> None:
        shallow = subject.tower_certificate(210, (2, 3, 5, 7))
        deeper = subject.tower_certificate(210, (2, 3, 5, 7, 11))
        self.assertEqual(shallow["linear_grid_rank"], 13)
        self.assertFalse(shallow["linear_grid_faithful"])
        self.assertEqual(deeper["linear_grid_rank"], 16)
        self.assertTrue(deeper["linear_grid_faithful"])
        self.assertEqual(deeper["centered_algebra_dimension"], 24)

    def test_literal_matrix_cost_is_only_a_full_grid_bound(self) -> None:
        panel = subject.fidelity_cost_panel(6)
        last = panel["rows"][-1]
        self.assertEqual(last["divisor_grid_size"], 64)
        self.assertEqual(last["single_level_degree_lower_bound"], 64)
        self.assertEqual(last["arbitrary_tower_max_level_lower_bound"], 11)
        self.assertEqual(
            last["arbitrary_tower_largest_matrix_dimension_lower_bound"], 2048
        )
        self.assertIn("one particular Mobius vector", panel["scope"])

    def test_full_fixture_and_categorical_firewall(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        self.assertFalse(result["categorical_scope"]["betti_lower_bound"])
        self.assertFalse(
            result["categorical_scope"]["correspondence_support_rank_lower_bound"]
        )
        self.assertEqual(
            result["categorical_scope"]["closed_point_adams_formula"],
            "NOT CONSTRUCTED",
        )
        self.assertEqual(result["resource_caps"]["largest_exact_matrix_dimension"], 32)


if __name__ == "__main__":
    unittest.main()
