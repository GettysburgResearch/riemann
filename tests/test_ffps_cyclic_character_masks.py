from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_cyclic_character_masks.py"
)
FIXTURE_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "ffps_cyclic_character_masks", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load cyclic-character mask producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CyclicCharacterMaskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_current(self) -> None:
        self.assertEqual(MODULE.build_fixture(), self.fixture)

    def test_payload_is_canonical(self) -> None:
        body = dict(self.fixture)
        payload = body.pop("payload_sha256")
        self.assertEqual(
            hashlib.sha256(MODULE._canonical_bytes(body)).hexdigest(), payload
        )

    def test_all_four_correlated_sources_are_locked(self) -> None:
        self.assertEqual(len(MODULE.SOURCE_LOCKS), 4)
        self.assertEqual(self.fixture["resource_contract"]["actual_source_files"], 4)
        for row in self.fixture["source_manifest"]:
            self.assertEqual(row["commit"], MODULE.CORRELATED_COMMIT)

    def test_legendre_case_reproduces_frozen_value(self) -> None:
        row = MODULE.cyclic_union_closed_form((5, 13), 2, 1)
        self.assertEqual(row["restricted_gram_denominator"], 258)
        self.assertEqual(row["sharp_restricted_leverage"], [24, 43])
        self.assertEqual(row["sharp_positive_uniform_weight"], [2, 1])
        self.assertTrue(row["strictly_improves_complete_tensor"])

    def test_ternary_kernel_is_sharp_but_worse_than_full(self) -> None:
        row = MODULE.direct_cyclic_grid_audit((7, 13), 3, (0,))
        closed = row["closed_form"]
        self.assertEqual(closed["support_size"], 6)
        self.assertEqual(closed["restricted_gram_denominator"], 420)
        self.assertEqual(closed["sharp_restricted_leverage"], [27, 35])
        self.assertEqual(closed["complete_tensor_leverage"], [9, 14])
        self.assertFalse(closed["strictly_improves_complete_tensor"])
        self.assertEqual(row["distinct_restricted_row_sums"], [70])

    def test_ternary_two_cosets_improve_and_are_uniform(self) -> None:
        row = MODULE.direct_cyclic_grid_audit((7, 13), 3, (0, 1))
        closed = row["closed_form"]
        self.assertEqual(closed["support_size"], 12)
        self.assertEqual(closed["restricted_gram_denominator"], 588)
        self.assertEqual(closed["sharp_restricted_leverage"], [27, 49])
        self.assertEqual(closed["sharp_positive_uniform_weight"], [3, 2])
        self.assertTrue(closed["strictly_improves_complete_tensor"])
        self.assertEqual(row["distinct_restricted_row_sums"], [49])

    def test_two_prime_cyclic_union_is_fixed_size_optimal(self) -> None:
        row = MODULE.direct_cyclic_grid_audit((7, 13), 3, (0, 1))
        control = row["two_prime_fixed_size_control"]
        self.assertEqual(control["row_degrees"], [4, 4, 4])
        self.assertEqual(control["column_degrees"], [2, 2, 2, 2, 2, 2])
        self.assertEqual(control["balanced_margin_maximum"], 588)
        self.assertTrue(control["attains_global_fixed_size_maximum"])

    def test_union_choice_only_uses_its_cardinality(self) -> None:
        left = MODULE.direct_cyclic_grid_audit((7, 13), 3, (0, 1))
        right = MODULE.direct_cyclic_grid_audit((7, 13), 3, (1, 2))
        self.assertEqual(left["direct_denominator"], right["direct_denominator"])
        self.assertEqual(
            left["closed_form"]["sharp_restricted_leverage"],
            right["closed_form"]["sharp_restricted_leverage"],
        )

    def test_composite_order_has_no_partial_constant_mode(self) -> None:
        row = MODULE.cyclic_union_closed_form((17, 41), 4, 2)
        self.assertEqual(row["nonzero_power_orders"], [4, 2, 4])
        self.assertTrue(row["every_nonzero_power_is_nontrivial_locally"])
        self.assertEqual(row["sharp_restricted_leverage"], [320, 443])
        self.assertEqual(row["sharp_positive_uniform_weight"], [2, 1])

    def test_same_density_has_same_energy_across_character_orders(self) -> None:
        quadratic = MODULE.cyclic_union_closed_form((17, 41), 2, 1)
        quartic = MODULE.cyclic_union_closed_form((17, 41), 4, 2)
        self.assertEqual(
            quadratic["restricted_gram_denominator"],
            quartic["restricted_gram_denominator"],
        )
        self.assertEqual(
            quadratic["sharp_restricted_leverage"],
            quartic["sharp_restricted_leverage"],
        )

    def test_full_improvement_criterion_is_exact(self) -> None:
        kernel = MODULE.cyclic_union_closed_form((7, 13), 3, 1)
        union = MODULE.cyclic_union_closed_form((7, 13), 3, 2)
        self.assertEqual(
            kernel["improvement_criterion"],
            {
                "formula": "P*t>Q*(k+t)",
                "left_P_times_t": 91,
                "right_Q_times_k_plus_t": 112,
            },
        )
        self.assertEqual(union["improvement_criterion"]["left_P_times_t"], 182)
        self.assertEqual(union["improvement_criterion"]["right_Q_times_k_plus_t"], 140)

    def test_fixed_d_construction_attains_continuous_limit(self) -> None:
        expected = {
            2: ([2, 3], [3, 4], 3, 2),
            3: ([4, 7], [7, 16], 7, 4),
            4: ([8, 15], [15, 64], 15, 8),
        }
        for dimension_count, values in expected.items():
            row = MODULE.fixed_d_limit(dimension_count)
            density, leverage, order, retained = values
            self.assertEqual(row["continuous_optimal_density"], density)
            self.assertEqual(row["continuous_optimal_leverage"], leverage)
            self.assertEqual(row["constructive_character_order"], order)
            self.assertEqual(row["constructive_retained_values"], retained)
            self.assertEqual(
                row["constructive_limiting_leverage"],
                row["continuous_optimal_leverage"],
            )

    def test_legendre_near_optimality_ratio(self) -> None:
        for dimension_count in range(2, 10):
            row = MODULE.fixed_d_limit(dimension_count)
            self.assertEqual(
                Fraction(*row["legendre_to_optimum_ratio"]),
                Fraction(4**dimension_count, 4**dimension_count - 1),
            )

    def test_kernel_order_increases_on_one_formal_panel(self) -> None:
        d = 5
        c = 2**d
        values = [Fraction(k * k, 1 + (k - 1) * c) for k in range(2, 12)]
        self.assertTrue(all(left < right for left, right in pairwise(values)))

    def test_rejects_order_not_supported_by_every_group(self) -> None:
        with self.assertRaisesRegex(ValueError, "divide every"):
            MODULE.cyclic_union_closed_form((5, 13), 3, 1)

    def test_rejects_bad_retained_value_count(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.cyclic_union_closed_form((7, 13), 3, 0)
        with self.assertRaises(ValueError):
            MODULE.cyclic_union_closed_form((7, 13), 3, 3)

    def test_rejects_nonprime_or_duplicate_control_panel(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.cyclic_union_closed_form((9, 13), 2, 1)
        with self.assertRaises(ValueError):
            MODULE.cyclic_union_closed_form((13, 13), 2, 1)

    def test_rejects_malformed_direct_residue_set(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.direct_cyclic_grid_audit((7, 13), 3, ())
        with self.assertRaises(ValueError):
            MODULE.direct_cyclic_grid_audit((7, 13), 3, (0, 0))
        with self.assertRaises(ValueError):
            MODULE.direct_cyclic_grid_audit((7, 13), 3, (3,))

    def test_direct_dimension_cap_fails_closed(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "dimension cap"):
            MODULE.direct_cyclic_grid_audit((17, 41), 4, (0,))

    def test_resource_caps_fail_closed(self) -> None:
        guard = MODULE.ResourceGuard()
        with self.assertRaisesRegex(RuntimeError, "operation cap"):
            guard.operation("overflow", MODULE.MAX_EXACT_OPERATIONS + 1)
        with self.assertRaisesRegex(RuntimeError, "matrix-cell cap"):
            guard.matrix(MODULE.MAX_MATRIX_CELLS + 1)
        with self.assertRaisesRegex(RuntimeError, "coordinate cap"):
            guard.coordinates(MODULE.MAX_ENUMERATED_COORDINATES + 1)

    def test_fixture_records_no_sweeps_or_global_claim(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["characters_enumerated"], 0)
        self.assertEqual(scope["conductors_enumerated"], 0)
        self.assertEqual(scope["l_functions_enumerated"], 0)
        firewalls = " ".join(self.fixture["firewalls"])
        self.assertIn("No principal member is individualized", firewalls)
        self.assertIn("grows with x, d, or M", firewalls)

    def test_exact_math_closes_before_source_reads(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(
            resources["actual_exact_operations"],
            resources["operations_before_sources"],
        )
        self.assertEqual(
            resources["actual_matrix_cells"],
            resources["matrix_cells_before_sources"],
        )
        self.assertEqual(
            resources["actual_enumerated_coordinates"],
            resources["coordinates_before_sources"],
        )


if __name__ == "__main__":
    unittest.main()
