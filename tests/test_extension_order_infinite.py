"""Bounded source and falsification controls for infinite extension order."""

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/extension-order-defect/infinite_replay.py"
)
SPEC = importlib.util.spec_from_file_location("infinite_extension_order", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class SourceTests(unittest.TestCase):
    def test_triangular_extraction_low_grades(self):
        rows = R.source_rows(8)
        self.assertEqual(rows[1]["multiplicities"], [1, 0, 1])
        self.assertEqual(rows[3]["multiplicities"], [0, 1, 1])
        self.assertEqual(rows[7]["multiplicities"], [4, 6, 10])

    def test_independent_frozen_mobius_source(self):
        _, completion = R.dependencies()
        for row in R.source_rows(48):
            self.assertEqual(row, completion.source_row(row["grade"]))

    def test_anti_invariant_projection(self):
        _, completion = R.dependencies()
        for row in R.source_rows(48)[1::2]:
            self.assertEqual(
                sum(row["multiplicities"][1:]), completion.anti_dimension(row["grade"])
            )

    def test_generator_character_newton(self):
        for kind in ("e", "s", "c"):
            self.assertEqual(
                R.generators(kind, 24, 24), R.generators_newton(kind, 24, 24)
            )

    def test_source_and_generator_caps(self):
        for bad in (True, 0, 65, 1.0):
            with self.assertRaises(ValueError):
                R.source_rows(bad)
        for bad in (True, 3, 34):
            with self.assertRaises(ValueError):
                R.generators("e", bad, 8)
        with self.assertRaises(ValueError):
            R.generators("unknown", 4, 8)

    def test_actual_degree_four_generator(self):
        old = R.generators("s", 2, 8)
        new = R.generators("s", 4, 8)
        self.assertEqual(new[4] - old[4], -1)
        self.assertEqual(R.generators("e", 4, 8)[4] - R.generators("e", 2, 8)[4], 3)


class InvariantTests(unittest.TestCase):
    def test_literal_old_basis_matches_reynolds(self):
        for cap in (2, 4):
            series = R.local_series("old", cap, 8)
            for grade in range(9):
                row = R.monomial_control("old", grade, cap)
                self.assertEqual(
                    [row["before"], row["after"]],
                    [series["before"][grade], series["after"][grade]],
                )

    def test_literal_infinity_residual_sign(self):
        for cap in (2, 4):
            split = R.local_series("split", cap, 8)
            nonsplit = R.local_series("nonsplit", cap, 8)
            for grade in range(9):
                row = R.monomial_control("infinity", grade, cap)
                self.assertEqual(row["cokernel_dimension"], split["difference"][grade])
                self.assertEqual(
                    row["cokernel_residual_trace"], nonsplit["difference"][grade]
                )

    def test_new_T4_crossed_sector(self):
        old = R.monomial_control("old", 5, 2)
        new = R.monomial_control("old", 5, 4)
        self.assertEqual(new["cokernel_dimension"] - old["cokernel_dimension"], 6)
        self.assertEqual(R.monomial_control("old", 4, 2)["cokernel_dimension"], 9)

    def test_frozen_single_generator_comparison(self):
        finite, _ = R.dependencies()
        for sign in (-1, 1):
            self.assertEqual(
                R.local_series("old", 2, 8, sign)["ratio"],
                finite.rational_local("old", "ratio", 8, sign),
            )
        self.assertEqual(R.monomial_control("infinity", 4, 2)["cokernel_dimension"], 13)
        self.assertEqual(
            R.monomial_control("infinity", 4, 2)["cokernel_residual_trace"], 1
        )

    def test_whole_source_reduced_products(self):
        for kind in ("old", "split", "nonsplit"):
            for sign in (-1, 1):
                self.assertEqual(
                    R.local_series(kind, 24, 24, sign)["ratio"],
                    R.reduced_ratio(kind, 24, 24, sign),
                )

    def test_infinity_trace_is_not_its_dimension(self):
        row = R.monomial_control("infinity", 8, 4)
        self.assertNotEqual(row["cokernel_dimension"], row["cokernel_residual_trace"])

    def test_new_zero_defect_all_checked_grades(self):
        source = R.local_series("zero", 24, 24)
        self.assertEqual(source["difference"], [0] * 25)
        self.assertEqual(source["ratio"], [1] + [0] * 24)

    def test_boundary_ratio_is_not_additive_cokernel(self):
        source = R.local_series("old", 24, 12)
        self.assertEqual(source["ratio"][4], 0)
        self.assertEqual(source["difference"][4], 9)

    def test_new_generator_stabilization(self):
        for kind in ("old", "split", "nonsplit"):
            first, next_one = (R.reduced_ratio(kind, cap, 12) for cap in (4, 6))
            self.assertEqual(first[:7], next_one[:7])

    def test_literal_caps(self):
        for args in (("old", True, 2), ("old", 9, 2), ("old", 4, 6), ("other", 2, 2)):
            with self.assertRaises(ValueError):
                R.monomial_control(*args)


class AnalyticAndArithmeticTests(unittest.TestCase):
    def test_actual_branch_norm_and_base_change(self):
        data = R.actual_branches()
        self.assertEqual([x["chi"] for x in data["rational_old"]], [-1, 1])
        self.assertEqual(data["quadratic_old"]["chi"], 1)
        self.assertFalse(data["base_change_49"]["new_field_count_performed"])

    def test_naive_scalar_norm_fails(self):
        data = R.scalar_base_change_control()
        self.assertEqual(data["first_mismatch"], 4)
        self.assertNotEqual(data["Xi49_z_squared"], data["Xi7_squared"])
        self.assertFalse(data["sheaf_base_change_failure_claimed"])

    def test_missing_degree_two_branch_is_detected(self):
        cut = 12
        incomplete = R.multiply(
            R.multiply(
                R.reduced_ratio("old", 12, cut),
                R.reduced_ratio("old", 12, cut, -1),
                cut,
            ),
            R.reduced_ratio("split", 12, cut),
            cut,
        )
        actual = R.global_ratio(7, 12, cut)
        self.assertEqual(actual[:6], incomplete[:6])
        self.assertEqual(actual[6] - incomplete[6], 3)

    def test_finite_critical_weights(self):
        rows = R.finite_critical_control()
        self.assertEqual([x["harmonic_index"] for x in rows], [1, 2, 3, 4])
        self.assertTrue(
            all(x["Xi7_at_half"] > 0 and x["Xi49_at_half"] > 0 for x in rows)
        )

    def test_negative_branch_zero_changes_leading_term(self):
        value = R.finite_values(8, Fraction(1, 2))
        self.assertEqual(value["Rminus"], value["W"])
        self.assertNotEqual(value["Rminus"], value["Rplus"])

    def test_unit_log_intervals_and_tail(self):
        coarse, fine = R.unit_log_enclosures(12), R.unit_log_enclosures(24)
        for kind in ("V", "W", "X", "Y"):
            a, b = coarse["analytic_unit_logs"][kind], fine["analytic_unit_logs"][kind]
            self.assertLessEqual(max(a[0], b[0]), min(a[1], b[1]))
            self.assertLess(b[1] - b[0], Fraction(1, 10**6))
        self.assertFalse(fine["infinite_boundary_product_evaluated"])

    def test_log_reciprocity_and_refinement(self):
        x = Fraction(19, 18)
        coarse, fine = R.interval_log(x, 8), R.interval_log(x, 24)
        self.assertLessEqual(coarse[0], fine[0])
        self.assertGreaterEqual(coarse[1], fine[1])
        inverse = R.interval_log(1 / x, 24)
        self.assertEqual(inverse, (-fine[1], -fine[0]))

    def test_outward_rounding_is_signed(self):
        x = Fraction(-1, 3)
        lo, hi = R.outward((x, x), 32)
        self.assertLessEqual(lo, x)
        self.assertGreaterEqual(hi, x)

    def test_analytic_caps(self):
        for bad in (0.25, Fraction(-1), Fraction(3)):
            with self.assertRaises(ValueError):
                R.interval_log(bad)
        with self.assertRaises(ValueError):
            R.finite_values(10, Fraction(1, 2))
        with self.assertRaises(ValueError):
            R.unit_log_enclosures(33)


class IntegrityTests(unittest.TestCase):
    def test_authentication_precedes_dynamic_import(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("blocked")),
            patch.object(R.importlib.util, "spec_from_file_location") as importer,
        ):
            with self.assertRaises(ValueError):
                R.dependencies()
            importer.assert_not_called()

    def test_pending_source_rejected(self):
        with patch.dict(
            R.PINS,
            {
                "finite_proof": {
                    "freeze": "PENDING",
                    "path": "PENDING",
                    "blob": "PENDING",
                }
            },
            clear=True,
        ), self.assertRaises(ValueError):
            R.authenticate()

    def test_strict_json_types(self):
        self.assertFalse(R.typed_equal({"a": True}, {"a": 1}))
        self.assertFalse(R.typed_equal([1], [1.0]))
        self.assertFalse(R.typed_equal([1], [1, 2]))

    def test_complete_frozen_replay(self):
        data = json.loads(R.FIXTURE.read_text(encoding="utf-8"))
        self.assertTrue(R.typed_equal(data, R.build()))

    def test_artifact_source_field_tamper(self):
        data = json.loads(R.FIXTURE.read_text(encoding="utf-8"))
        altered = json.loads(json.dumps(data))
        altered["actual_branches"]["quadratic_old"]["chi"] = -1
        self.assertFalse(R.typed_equal(data, altered))


if __name__ == "__main__":
    unittest.main()
