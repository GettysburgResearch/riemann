"""Independent exact controls for the all-field AFTER radius theorem."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
FILE = (
    ROOT
    / "research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius_replay.py"
)
SPEC = importlib.util.spec_from_file_location("arithmetic_after_radius", FILE)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ArithmeticRadiusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = R.atlas()
        cls.rows = [row for panel in cls.source["panels"] for row in panel["rows"]]

    def test_complete_independent_atlas(self):
        self.assertEqual(len(self.rows), 3044)
        self.assertEqual(
            [panel["p"] for panel in self.source["panels"]], list(R.PRIMES)
        )
        R.check_discovery(json.loads(R.DISCOVERY.read_text()), self.source)

    def test_all_field_congruence_and_pairing(self):
        for row in self.rows:
            self.assertEqual(row["tZ"] % 6, 0)
            self.assertEqual((row["oldPlus"] + row["oldMinus"]) % 2, 0)
            if row["p"] % 4 == 3:
                self.assertEqual(row["splitPlus"], row["splitMinus"])
                self.assertEqual(row["oldPlus"], row["oldMinus"])

    def test_quadratic_zero_is_not_given_a_sign(self):
        row = R.raw_row(5, 1, 0)
        self.assertEqual(
            [row[k] for k in ("splitPlus", "splitMinus", "splitZero")], [0, 0, 1]
        )
        self.assertEqual(R.quadratic_character(0, 5), 0)
        self.assertEqual(R.classify_after(row)["nu_plus"], [0, 1])

    def test_selected_actual_curve_counts(self):
        row = R.raw_row(5, 1, 0)
        self.assertEqual(
            [row[k] for k in ("pointsE", "pointsD", "aE", "aD", "tZ")],
            [4, 10, 2, -4, 0],
        )
        self.assertEqual(R.raw_row(7, 1, 0)["aE"], 0)
        self.assertEqual(R.raw_row(7, 1, 0)["aD"], 0)

    def test_independent_galois_closure_points(self):
        for panel in R.SELECTED:
            result = R.closure_control(*panel)
            self.assertEqual(result["proper_count"], R.raw_row(*panel)["zPoints"])

    def test_negative_multiplier_is_not_full_source_pole(self):
        result = R.classify_after(R.raw_row(11, 1, 3))
        self.assertEqual(result["alpha"], [-1, 1])
        self.assertEqual(result["pure_multiplier_first_behavior"], "pole")
        self.assertEqual(result["nu_plus"], [1, 1])
        self.assertEqual(result["nu_minus"], [1, 1])
        self.assertEqual(result["after_radius"], "1/sqrt(2)")
        self.assertTrue(result["negative_multiplier_canceled_by_finite_source"])

    def test_actual_full_source_pole_survives(self):
        result = R.classify_after(R.raw_row(13, 4, 1))
        self.assertEqual(result["positive_first_behavior"], "pole")
        self.assertEqual(result["after_radius"], "1/2")

    def test_positive_integer_multiplier_source(self):
        result = R.classify_after(R.raw_row(11, 1, 4))
        self.assertEqual(result["alpha"], [1, 1])
        self.assertEqual(result["nu_plus"], [1, 1])
        self.assertEqual(result["nu_minus"], [1, 1])
        self.assertEqual(result["after_radius"], "1/sqrt(2)")

    def test_second_circle_obstruction_all_sources(self):
        for row in self.rows:
            result = R.classify_after(row)
            gamma = Fraction(*result["gamma"])
            self.assertEqual((4 * gamma).denominator, 1)
            self.assertTrue(
                result["second_nonintegral_real"]
                or result["second_nonintegral_imaginary"]
            )

    def test_preregistered_after_class_counts(self):
        counts = {"1/2": 0, "1/sqrt(2)": 0}
        for row in self.rows:
            counts[R.classify_after(row)["after_radius"]] += 1
        self.assertEqual(counts, {"1/2": 1798, "1/sqrt(2)": 1246})

    def test_misassigned_zero_point_is_rejected(self):
        row = R.raw_row(5, 1, 0)
        row["splitPlus"] = 1
        with self.assertRaises(ValueError):
            R.classify_after(row)

    def test_PBW_and_restricted_divisors(self):
        for n in range(2, 129, 2):
            self.assertEqual(R.source_characters(n), R.restricted_characters(n))

    def test_error_bounds_at_sharp_small_grade(self):
        row = next(item for item in R.character_controls() if item["grade"] == 6)
        self.assertEqual(row["characters"], [11, 1, -1])
        self.assertEqual(row["dimension_error"], [-1, 1])
        self.assertEqual(row["transposition_error"], [-1, 3])
        self.assertEqual(row["dimension_cycle_bound"], [1, 1])
        self.assertEqual(row["transposition_bound"], [1, 3])

    def test_actual_low_irreducible_source(self):
        self.assertEqual(R.multiplicities(2), (1, 0, 1))
        self.assertEqual(R.multiplicities(4), (0, 1, 1))
        self.assertEqual(R.multiplicities(8), (4, 6, 10))

    def test_first_proper_polynomial_factor(self):
        row = R.raw_row(5, 1, 0)
        product = R.finite_ladder(row, 4, 16)
        p, ae, ad = row["p"], row["aE"], row["aD"]
        self.assertEqual(
            [product[i] for i in (0, 4, 8, 12, 16)],
            [1, -(ae + ad), 2 * p + ae * ad, -p * (ae + ad), p * p],
        )
        self.assertTrue(all(x == 0 for i, x in enumerate(product) if i % 4))

    def test_polynomial_product_and_Newton(self):
        for params in R.SELECTED:
            row = R.raw_row(*params)
            for cap in (4, 8, 12):
                self.assertEqual(
                    R.finite_ladder(row, cap, 24), R.finite_ladder(row, cap, 24, True)
                )

    def test_first_new_degree_six_factor(self):
        row = R.raw_row(5, 1, 0)
        old, new = (R.finite_ladder(row, cap, 12) for cap in (4, 6))
        self.assertEqual(old[:6], new[:6])
        self.assertEqual(new[6] - old[6], -4)

    def test_frobenius_squared_trace(self):
        self.assertEqual(R.frobenius_traces(2, 5, 2), [2, 2, -6])
        self.assertEqual(R.frobenius_traces(-4, 5, 2), [2, -4, 6])

    def test_parameter_caps(self):
        for args in (
            (True, 1, 0),
            (37, 1, 0),
            (5, 0, 1),
            (5, 1.0, 0),
            (5, 1, 5),
            (31, 1, 1),
        ):
            with self.assertRaises(ValueError):
                R.raw_row(*args)

    def test_character_and_coefficient_caps(self):
        for n in (True, 0, 129, 4.0):
            with self.assertRaises(ValueError):
                R.source_characters(n)
        with self.assertRaises(ValueError):
            R.restricted_characters(3)
        with self.assertRaises(ValueError):
            R.finite_ladder(R.raw_row(5, 1, 0), 14, 24)
        with self.assertRaises(ValueError):
            R.frobenius_traces(2, "5", 2)

    def test_cached_source_cannot_be_mutated(self):
        row = R.raw_row(5, 1, 0)
        row["pointsE"] = 999
        self.assertEqual(R.raw_row(5, 1, 0)["pointsE"], 4)

    def test_frozen_theorem_blob_failure(self):
        with (
            patch.object(R.subprocess, "check_output", return_value="wrong-blob\n"),
            self.assertRaises(ValueError),
        ):
            R.authenticate()

    def test_discovery_arithmetic_tamper(self):
        altered = copy.deepcopy(self.source)
        altered["panels"][0]["rows"][0]["pointsE"] += 1
        with self.assertRaises(ValueError):
            R.check_discovery(altered, self.source)

    def test_discovery_numeric_type_counterfeits(self):
        for field, value in (("splitZero", True), ("p", 5.0)):
            altered = copy.deepcopy(self.source)
            altered["panels"][0]["rows"][0][field] = value
            with self.assertRaises(ValueError):
                R.check_discovery(altered, self.source)

    def test_canonical_json_rejects_nan_and_key_aliases(self):
        self.assertFalse(R.strict_equal({"x": float("nan")}, {"x": float("nan")}))
        self.assertFalse(R.strict_equal({True: 1}, {"true": 1}))
        self.assertFalse(R.strict_equal({"x": 1}, {"x": 1.0}))
        self.assertFalse(R.strict_equal({"x": 1}, {"x": True}))

    def test_complete_bound_artifact(self):
        R.check_payload(json.loads(R.FIXTURE.read_text()))

    def test_artifact_numeric_type_counterfeits(self):
        original = json.loads(R.FIXTURE.read_text())
        boolean = copy.deepcopy(original)
        boolean["discovery_reconstructed_exactly"] = 1
        self.assertFalse(R.strict_equal(boolean, original))
        floating = copy.deepcopy(original)
        floating["panels"][0]["rows"][0]["analytic"]["alpha"][0] = 0.0
        self.assertFalse(R.strict_equal(floating, original))

    def test_no_before_classification_in_after_packet(self):
        result = R.classify_after(R.raw_row(13, 1, 5))
        self.assertNotIn("before_radius", result)
        self.assertNotIn("ramification_exponent", result)


if __name__ == "__main__":
    unittest.main()
