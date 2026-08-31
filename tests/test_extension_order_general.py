"""Actual-source controls for the general extension-order and base theorem."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/extension-order-defect/general_replay.py"
)
SPEC = importlib.util.spec_from_file_location("general_extension_order", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ArithmeticSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, cls.after, cls.artifact = R.source()

    def row(self, p, a, b):
        return self.after.raw_row(p, a, b)

    def test_complete_source_atlas_classification(self):
        totals = {"1/2": 0, "1/sqrt(2)": 0}
        changes = 0
        for panel in self.artifact["panels"]:
            for bound in panel["rows"]:
                row = {key: bound[key] for key in self.after.RAW_KEYS}
                result = R.classify_before(row)
                self.assertEqual(
                    result["after_radius"], bound["analytic"]["after_radius"]
                )
                totals[result["before_radius"]] += 1
                changes += result["extension_order_changes_radius"]
        self.assertEqual(totals, {"1/2": 2647, "1/sqrt(2)": 397})
        self.assertEqual(changes, 849)
        self.assertEqual(sum(totals.values()), 3044)

    def test_actual_f7_same_generic_source_changes_radius(self):
        result = R.classify_before(self.row(7, 1, 0))
        self.assertEqual(result["after_radius"], "1/sqrt(2)")
        self.assertEqual(result["before_radius"], "1/2")
        self.assertEqual(result["rho_plus"], [-1, 3])
        self.assertEqual(result["rho_minus"], [-1, 3])
        self.assertTrue(result["positive_sqrt_coefficient_present"])

    def test_f5_zero_split_fibre_is_not_a_good_chi_sign(self):
        row = self.row(5, 1, 0)
        self.assertEqual(row["splitZero"], 1)
        self.assertEqual(row["splitPlus"] + row["splitMinus"], 0)
        result = R.classify_before(row)
        self.assertEqual(result["before_radius"], "1/sqrt(2)")
        self.assertFalse(result["positive_sqrt_coefficient_present"])

    def test_full_source_zero_cancels_pure_multiplier_pole(self):
        result = R.classify_before(self.row(11, 1, 3))
        self.assertEqual(result["alpha"], [-1, 1])
        self.assertEqual(result["rho_plus"], [1, 1])
        self.assertEqual(result["rho_minus"], [1, 1])
        self.assertEqual(result["before_radius"], "1/sqrt(2)")

    def test_positive_multiplier_zero_is_not_an_obstruction(self):
        result = R.classify_before(self.row(11, 1, 4))
        self.assertEqual(result["alpha"], [1, 1])
        self.assertEqual(result["before_radius"], "1/sqrt(2)")

    def test_split_infinity_blocks_analytic_after_zero(self):
        result = R.classify_before(self.row(13, 1, 5))
        self.assertEqual(result["after_radius"], "1/sqrt(2)")
        self.assertEqual(result["before_radius"], "1/2")
        self.assertNotEqual(result["rho_plus"][1], 1)

    def test_actual_pole_is_not_removed_by_integer_test(self):
        result = R.classify_before(self.row(13, 4, 1))
        self.assertEqual(result["after_radius"], "1/2")
        self.assertEqual(result["before_radius"], "1/2")

    def test_rational_branch_square_root_obstruction_can_be_leading_integral(self):
        found = False
        for panel in self.artifact["panels"]:
            for bound in panel["rows"]:
                result = R.classify_before(bound)
                if (
                    result["positive_sqrt_coefficient_present"]
                    and result["rho_plus"][1] == 1
                ):
                    self.assertEqual(result["before_radius"], "1/2")
                    found = True
        self.assertTrue(found)

    def test_second_circle_lattice_controls_do_not_assign_branch_patterns(self):
        result = R.classify_before(self.row(5, 1, 0))
        controls = result["second_circle_quarter_sixth_controls"]
        self.assertEqual(len(controls), 5)
        for control in controls:
            self.assertNotEqual(control["exponent_mod_integer"][1], 1)
            self.assertFalse(control["actual_pattern_assigned"])

    def test_tampered_trace_and_infinity_are_rejected(self):
        for key in ("tZ", "aE", "split", "delta"):
            bad = self.row(7, 1, 0)
            bad[key] += 1
            with self.assertRaises(ValueError):
                R.classify_before(bad)

    def test_zero_sign_relabelling_is_rejected(self):
        bad = self.row(5, 1, 0)
        bad["splitPlus"] += 1
        with self.assertRaises(ValueError):
            R.classify_before(bad)

    def test_source_integer_fields_reject_boolean_float_and_new_prime(self):
        for value in (True, 7.0, 37):
            bad = self.row(7, 1, 0)
            bad["p"] = value
            with self.assertRaises(ValueError):
                R.classify_before(bad)


class InvariantGeneratorTests(unittest.TestCase):
    def test_actual_standard_matrices_satisfy_s3(self):
        source = R.standard_source()
        self.assertEqual(source["cycle"], [[-1, -1], [1, 0]])
        self.assertEqual(source["reflection"], [[0, 1], [1, 0]])
        self.assertEqual(source["quadratic_eigenbasis_determinant"], -2)

    def test_c2_new_quadratic_generator_is_missed_by_fixed_input(self):
        row = R.invariant_monomials("C2", 4)
        self.assertEqual(row["monomials"], [[0, 2], [2, 0]])
        self.assertEqual(row["dimension"], 2)
        self.assertEqual(row["fixed_input_dimension"], 1)

    def test_c2_fixed_base_quotient_has_unbounded_nonzero_grades(self):
        for grade in range(0, 33, 4):
            self.assertEqual(
                R.invariant_monomials("C2", grade)[
                    "quotient_by_positive_fixed_inputs_dimension"
                ],
                1,
            )
        self.assertEqual(
            R.invariant_monomials("C2", 2)[
                "quotient_by_positive_fixed_inputs_dimension"
            ],
            0,
        )

    def test_c3_cubic_generators_and_relation(self):
        row = R.invariant_monomials("C3", 6)
        self.assertEqual(row["monomials"], [[0, 3], [3, 0]])
        self.assertEqual(row["fixed_input_dimension"], 0)
        self.assertEqual(R.cubic_normal_product((0, 1, 0), (0, 0, 1)), (3, 0, 0))

    def test_c3_normal_products_match_original_monomials(self):
        forms = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 2, 0), (1, 0, 2)]

        def original(form):
            h, p, q = form
            return h + 3 * p, h + 3 * q

        for left in forms:
            for right in forms:
                product = R.cubic_normal_product(left, right)
                self.assertEqual(
                    original(product),
                    tuple(
                        a + b
                        for a, b in zip(original(left), original(right), strict=True)
                    ),
                )

    def test_c3_residual_reflection_keeps_only_diagonal_monomials(self):
        for grade in range(33):
            row = R.invariant_monomials("C3", grade)
            self.assertEqual(row["residual_trace"], int(grade % 4 == 0))
        self.assertEqual(R.invariant_monomials("C3", 12)["dimension"], 3)
        self.assertEqual(R.invariant_monomials("C3", 12)["residual_trace"], 1)

    def test_literal_segre_negative_coordinates_minimal_in_degree_one(self):
        row = R.anti_module_generators(1)
        self.assertEqual(row["dimension"], 3)
        self.assertEqual(
            row["negative_degree_one_coordinates"], [[0, 2], [1, 0], [1, 1]]
        )

    def test_all_bounded_negative_monomials_have_invariant_quotient(self):
        for grade in range(1, 7):
            row = R.anti_module_generators(grade)
            for item in row["coverage"]:
                v, w = item["v"], item["w"]
                i, j = item["chosen_negative_coordinate"]
                self.assertEqual(sum(v), grade)
                self.assertEqual(sum(w), grade)
                self.assertEqual((v[1] + w[2]) % 2, 1)
                self.assertGreater(v[i], 0)
                self.assertGreater(w[j], 0)

    def test_repaired_module_is_not_a_new_action_on_original_cokernel(self):
        controls = R.base_controls()
        self.assertEqual(controls["repaired_C_minimal_generators"], {"0": 1, "3": 3})
        self.assertEqual(controls["repaired_C_rank"], 2)
        self.assertFalse(controls["original_Q_becomes_module_over_larger_base"])
        self.assertFalse(controls["C2_obstruction"]["product_preserves_B"])
        self.assertTrue(controls["all_grade_finiteness_and_rank_proved_not_inferred"])

    def test_primitive_caps_and_normal_form_validation(self):
        for bad in (True, -1, 33, 4.0):
            with self.assertRaises(ValueError):
                R.invariant_monomials("C2", bad)
        with self.assertRaises(ValueError):
            R.invariant_monomials("C4", 4)
        with self.assertRaises(ValueError):
            R.cubic_normal_product((0, 1, 1), (0, 0, 0))
        with self.assertRaises(ValueError):
            R.anti_module_generators(7)


class AuthenticationAndFixtureTests(unittest.TestCase):
    def test_authentication_happens_before_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("blocked")),
            patch.object(R.importlib.util, "spec_from_file_location") as imported,
        ):
            with self.assertRaises(ValueError):
                R.source()
            imported.assert_not_called()

    def test_pending_or_corrupt_freeze_is_not_accepted(self):
        bad = {"bad": {"freeze": "PENDING", "path": "absent", "blob": "PENDING"}}
        with (
            patch.object(R, "PINS", bad),
            patch.object(R.subprocess, "check_output") as git,
        ):
            with self.assertRaises(ValueError):
                R.authenticate()
            git.assert_not_called()

    def test_canonical_json_distinguishes_numeric_counterfeits(self):
        for value in (True, 1.0, "1"):
            self.assertFalse(R.strict_equal({"x": 1}, {"x": value}))
        self.assertTrue(R.strict_equal({"a": 1, "b": [2]}, {"b": [2], "a": 1}))

    def test_nonfinite_and_non_json_containers_fail_closed(self):
        for value in (float("nan"), float("inf"), -float("inf")):
            self.assertFalse(R.strict_equal([value], [value]))
        self.assertFalse(R.strict_equal([1], (1,)))
        self.assertFalse(R.strict_equal({1: "a"}, {"1": "a"}))

    def test_checker_rejects_typed_fixture_mutations(self):
        payload = {"count": 1, "exact": [1, 3], "flag": True}
        for key, value in (
            ("count", True),
            ("count", 1.0),
            ("exact", [1.0, 3]),
            ("flag", 1),
        ):
            bad = copy.deepcopy(payload)
            bad[key] = value
            with (
                patch.object(R, "build_payload", return_value=payload),
                self.assertRaises(ValueError),
            ):
                R.check_payload(bad)

    def test_bound_fixture_complete_and_strict(self):
        data = json.loads(R.FIXTURE.read_bytes())
        R.check_payload(data)
        self.assertEqual(data["total"], 3044)
        self.assertEqual(data["extension_order_changes"], 849)
        self.assertEqual(data["before_radius_counts"], {"1/2": 2647, "1/sqrt(2)": 397})
        self.assertEqual(len(data["selected_actual_sources"]), 7)


if __name__ == "__main__":
    unittest.main()
