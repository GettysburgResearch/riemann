"""Exact isotonic, activation-order and complete native-source support controls."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/riemann-structures/native-six-hour/native_occupation_support.py"
SPEC = importlib.util.spec_from_file_location("native_occupation_support", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build()
        cls.rows = {row["name"]: row for row in cls.payload["registered_panels"]}

    def test_exact_four_pins_precede_executable_import(self):
        self.assertEqual(len(self.payload["sources"]), 4)
        with (
            patch.object(M, "authenticate", side_effect=ValueError("changed source")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "changed source"):
                M.source()
            compiler.assert_not_called()

    def test_exact_eight_registered_regimes_retained(self):
        self.assertEqual(set(self.rows), {row[0] for row in M.PANELS})
        self.assertEqual(len(self.rows), 8)
        self.assertEqual(len(self.payload["complete_ordered_records"]), 63)

    def test_increasing_target_clips_both_endpoints(self):
        path, value, mode = M.planar_optimizer((1, -4, 1, 0, 0, 0), 0, 1, 0, 1)
        self.assertEqual(mode, "increasing_affine_clip")
        self.assertEqual(
            path, ((F(), F()), (F(1, 4), F()), (F(3, 4), F(1)), (F(1), F(1)))
        )
        self.assertEqual(value, F(-13, 24))

    def test_decreasing_target_requires_constant_isotonic_projection(self):
        path, value, mode = M.planar_optimizer((-3, 4, 1, 0, 0, 0), 0, 1, 0, 1)
        self.assertEqual(mode, "isotonic_constant")
        self.assertEqual(
            path, ((F(), F()), (F(), F(1, 2)), (F(1), F(1, 2)), (F(1), F(1)))
        )
        self.assertEqual(value, F(-1, 4))
        with self.assertRaisesRegex(ValueError, "monotone"):
            M.planar_integral(((F(), F(1)), (F(1), F())), -3, 4, 1)

    def test_endpoints_allow_vertical_completion_without_false_point_values(self):
        rows = self.rows["constant_target_endpoints"]["marked_controls"]
        self.assertEqual(
            [row["marked_s_t"] for row in rows], [["0", "1/4"], ["1", "3/4"]]
        )
        for row in rows:
            points = row["source"]["points"]
            self.assertEqual(points[0], ["0", "0", "0"])
            self.assertEqual(points[-1], ["1", "1", "1"])
            self.assertLessEqual(len(points), 7)

    def test_tied_activation_orders_are_distinct_actual_sources(self):
        first, second = self.payload["tied_vertical_orders"]
        self.assertEqual(first["source"]["literal_functional_value"], "1")
        self.assertEqual(second["source"]["literal_functional_value"], "0")
        self.assertNotEqual(
            first["source"]["all63_actual_source_records"],
            second["source"]["all63_actual_source_records"],
        )

    def test_both_signs_of_f_select_the_correct_global_support(self):
        self.assertEqual(self.rows["order_positive"]["global_support_value"], "0")
        self.assertEqual(self.rows["order_negative"]["global_support_value"], "-1")
        for name in ("order_positive", "order_negative"):
            self.assertEqual(
                {row["order"] for row in self.rows[name]["candidate_values"]},
                {"w_before_v", "v_before_w"},
            )

    def test_concave_interior_minimum_is_not_a_vertex_guess(self):
        row = self.rows["concave_interior"]
        self.assertEqual(row["global_support_value"], "-11/8")
        self.assertIn(
            {"value": "-11/8", "s": "1/2", "r": "1/4", "order": "v_before_w"},
            row["candidate_values"],
        )
        self.assertTrue(row["selected_source"]["all63_match_frozen_affine_readout"])

    def test_flat_quadratic_keeps_valid_boundary_candidates(self):
        row = self.rows["concave_flat"]
        self.assertEqual(row["global_support_value"], "0")
        self.assertTrue(all(F(item["value"]) == 0 for item in row["candidate_values"]))
        with self.assertRaisesRegex(ValueError, "requires c<=0"):
            M.triangle_candidates((1, -4, 1, 0, 0, 0), "w_before_v")

    def test_all_selected_paths_retain_the_literal63_record_identity(self):
        for row in self.rows.values():
            selected = [item["source"] for item in row.get("marked_controls", [])]
            if "selected_source" in row:
                selected.append(row["selected_source"])
            selected.append(row["signed_single_w_control"]["collapsed_source"])
            for item in selected:
                self.assertEqual(len(item["all63_actual_source_records"]), 63)
                self.assertTrue(item["all63_match_frozen_affine_readout"])
                self.assertLessEqual(len(item["points"]), 7)

    def test_signed_single_w_collapse_uses_original_path_and_never_raises_cost(self):
        for row in self.rows.values():
            control = row["signed_single_w_control"]
            self.assertLessEqual(
                F(control["collapsed_source"]["literal_functional_value"]),
                F(control["original_value"]),
            )
            self.assertTrue(all(0 <= F(x) <= 1 for x in control["marked_s_t"]))

    def test_positive_c_controls_do_not_claim_global_two_dimensional_solution(self):
        for name in (
            "increasing_target",
            "decreasing_target",
            "constant_target_endpoints",
        ):
            self.assertEqual(self.rows[name]["mode"], "exact_fixed_marked_problem_only")
            self.assertFalse(
                self.rows[name]["global_two_dimensional_support_value_claimed"]
            )
        self.assertFalse(
            self.payload["scope"]["positive_c_global_two_dimensional_solver_executed"]
        )
        self.assertFalse(self.payload["scope"]["original_physical_quadratic_optimized"])

    def test_zero_length_and_constant_planar_intervals(self):
        path, value, _ = M.planar_optimizer((1, -4, 1, 0, 0, 0), 0, 0, 0, 1)
        self.assertEqual(path, ((F(), F()), (F(), F(1))))
        self.assertEqual(value, 0)
        _, value, _ = M.planar_optimizer((1, 0, 1, 0, 0, 0), 0, 1, F(1, 2), F(1, 2))
        self.assertEqual(value, F(3, 4))

    def test_wrong_triangle_order_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "activation triangle"):
            M.activation_path(F(3, 4), F(1, 4), "w_before_v")
        with self.assertRaisesRegex(ValueError, "activation order"):
            M.triangle_candidates((0, 0, 0, 0, 0, 0), "merged_diagonal")

    def test_literal_types_and_caps_are_enforced(self):
        for bad in (True, 1.0, None):
            with self.assertRaises(ValueError):
                M.coefficient_tuple((bad, 0, 0, 0, 0, 0))
        for bad in ((9, 0, 0, 0, 0, 0), (F(1, 17), 0, 0, 0, 0, 0)):
            with self.assertRaises(ValueError):
                M.coefficient_tuple(bad)
        with self.assertRaises(ValueError):
            M.unit(F(5, 4))

    def test_complete_strict_json_and_hash_contract(self):
        for bad in (True, 1.0):
            with self.assertRaises(ValueError):
                M.equal({"rank": bad}, {"rank": 1})
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        changed = copy.deepcopy(self.payload)
        changed["registered_panels"].pop()
        with self.assertRaises(ValueError):
            M.equal(changed, self.payload)
        body = {
            key: value
            for key, value in self.payload.items()
            if key != "proof_object_sha256"
        }
        self.assertEqual(
            M.sha256(M.canonical(body).encode()).hexdigest(),
            self.payload["proof_object_sha256"],
        )


if __name__ == "__main__":
    unittest.main()
