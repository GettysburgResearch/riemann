"""Independent source-allocation, enclosure and typed acceptance controls."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_positive_tail_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_positive_tail_final_test", PATH)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class NativePositiveTailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calibration = C.decode(C.frozen("calibration"))
        cls.heldout = C.decode(C.frozen("heldout"))
        cls.rows = cls.calibration["complete_smooth_cost_records"]
        cls.panel = cls.calibration["panels"][0]

    @staticmethod
    def replace_interval(row, lo, hi):
        row["lower"], row["upper"] = str(lo), str(hi)

    def test_01_complete_two_phase_certificate(self):
        result = C.build()
        self.assertEqual([p["H"] for p in result["panels"]], [25, 30, 60, 900, 2**20])
        self.assertEqual(
            result["literal_tensor_allocation_controls"],
            {"1": "0", "2": "1", "4": "5/4", "6": "2", "8": "1"},
        )
        self.assertIs(result["original_measure_retained"], True)
        self.assertIs(result["all_monotone_paths_covered"], True)
        self.assertIs(result["optimizer_persistence_claimed"], False)

    def test_02_unchanged_executable_and_ownership(self):
        self.assertEqual(C.frozen("scout"), C.frozen("heldout_scout"))
        self.assertNotEqual(C.PINS["calibration"][0], C.PINS["heldout"][0])
        C.strict_equal(
            self.calibration["owned_sha256_lf"], self.heldout["owned_sha256_lf"]
        )

    def test_03_recurrence_endpoint_coefficients(self):
        half, alpha, derivative = C.source_tables()
        self.assertEqual(half[:4], (F(1), -F(1, 2), -F(1, 8), -F(1, 16)))
        self.assertEqual(alpha[2], F(1, 2))
        self.assertEqual(derivative[2], F(3, 8))
        changed = copy.deepcopy(self.calibration)
        changed["all_local_alpha_coefficients"][2] = "1/8"
        with self.assertRaisesRegex(ValueError, "typed complete"):
            C.validate_tables(changed)

    def test_04_all_derivative_sites_and_allocations(self):
        self.assertEqual(C.literal_tensor_coefficient((0, 0, 0)), 0)
        self.assertEqual(C.literal_tensor_coefficient((1, 0, 0)), 1)
        self.assertEqual(C.literal_tensor_coefficient((2, 0, 0)), F(5, 4))
        self.assertEqual(C.literal_tensor_coefficient((1, 1, 0)), 2)
        self.assertNotEqual(C.literal_tensor_coefficient((1, 1, 0)), 1)
        self.assertEqual(C.literal_tensor_coefficient((3, 0, 0)), 1)

    def test_05_type_checks_precede_tensor_cache(self):
        C.literal_tensor_coefficient((1, 1, 0))
        for powers in ((True, 1, 0), (1.0, 1, 0), (21, 0, 0), (20, 1, 0), [1, 1, 0]):
            with self.assertRaises(ValueError):
                C.literal_tensor_coefficient(powers)

    def test_06_independent_multiplicative_cost_census(self):
        values = C.smooth_costs(60)
        self.assertEqual(values, sorted(set(values)))
        self.assertEqual(values[-1], 60)
        self.assertNotIn(7, values)
        self.assertIn(2**20, C.smooth_costs(2**20))
        self.assertEqual(C.powers_of(900), (2, 2, 2))
        for value in (True, 60.0, 25, 2**20 + 1):
            with self.assertRaises(ValueError):
                C.smooth_costs(value)
        with self.assertRaises(ValueError):
            C.powers_of(7)

    def test_07_complete_costs_cannot_be_masked(self):
        changed = copy.deepcopy(self.calibration)
        changed["complete_smooth_cost_records"].pop()
        with self.assertRaisesRegex(ValueError, "complete smooth-cost census"):
            C.validate_records(changed, 60)
        changed = copy.deepcopy(self.calibration)
        changed["complete_smooth_cost_records"][1]["cost"] = True
        with self.assertRaisesRegex(ValueError, "literal smooth cost"):
            C.validate_records(changed, 60)

    def test_08_wrong_tensor_coefficient_is_rejected(self):
        changed = copy.deepcopy(self.calibration)
        row = next(r for r in changed["complete_smooth_cost_records"] if r["cost"] == 6)
        row["exact_majorant_coefficient"] = "1"
        with self.assertRaisesRegex(ValueError, "literal full tensor"):
            C.validate_records(changed, 60)

    def test_09_contribution_bounds_are_checked_by_exact_squares(self):
        changed = copy.deepcopy(self.calibration)
        row = next(r for r in changed["complete_smooth_cost_records"] if r["cost"] == 2)
        self.replace_interval(row["directed_contribution"], F(3, 4), F(4, 5))
        with self.assertRaisesRegex(ValueError, "square bracket"):
            C.validate_records(changed, 60)

    def test_10_independent_root_enclosures(self):
        self.assertEqual(C.independent_root((F(), F())), (F(), F()))
        self.assertEqual(C.independent_root((F(4), F(4))), (F(2), F(2)))
        bracket = C.independent_root((F(2), F(2)))
        C.root_enclosure(bracket, F(2))
        self.assertLess(bracket[0], bracket[1])
        with self.assertRaises(ValueError):
            C.root_enclosure((F(3, 2), F(2)), F(2))
        with self.assertRaises(ValueError):
            C.independent_root((F(-1), F(1)))

    def test_11_aggregate_bound_is_not_coefficientwise_bound(self):
        changed = copy.deepcopy(self.calibration)
        local = changed["local_closed_sums"][0]
        local["A_actual"] = copy.deepcopy(local["A_max"])
        with self.assertRaisesRegex(ValueError, "closed-value enclosure"):
            C.validate_constants(changed)

    def test_12_complete_prefix_and_digest_are_retained(self):
        changed = copy.deepcopy(self.panel)
        changed["complete_prefix_costs"].pop()
        with self.assertRaisesRegex(ValueError, "typed complete"):
            C.validate_panel(changed, self.rows, self.calibration)
        changed = copy.deepcopy(self.panel)
        changed["prefix_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "prefix digest"):
            C.validate_panel(changed, self.rows, self.calibration)

    def test_13_same_majorant_subtraction_and_endpoint_rate(self):
        changed = copy.deepcopy(self.panel)
        self.replace_interval(changed["raw_total_minus_prefix"], 0, 0)
        with self.assertRaisesRegex(ValueError, "same positive majorant"):
            C.validate_panel(changed, self.rows, self.calibration)
        changed = copy.deepcopy(self.panel)
        self.replace_interval(changed["independent_endpoint_rate"], 0, 0)
        with self.assertRaisesRegex(ValueError, "square bracket"):
            C.validate_panel(changed, self.rows, self.calibration)

    def test_14_minimum_selection_and_original_error_bounds(self):
        for key, message in (
            ("uniform_field_error_upper", "two certified"),
            ("uniform_Hilbert_error_upper", "Hilbert upper"),
            ("uniform_energy_and_minimum_error_upper", "energy and minimum"),
        ):
            changed = copy.deepcopy(self.panel)
            changed[key] = "0"
            with self.assertRaisesRegex(ValueError, message):
                C.validate_panel(changed, self.rows, self.calibration)

    def test_15_scope_and_proof_identity_cannot_be_promoted(self):
        changed = copy.deepcopy(self.calibration)
        changed["optimal_path_persistence_claimed"] = True
        with self.assertRaisesRegex(ValueError, "completion scope"):
            C.validate_capture(changed, "calibration")
        changed = copy.deepcopy(self.calibration)
        changed["proof_object_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "capture proof hash"):
            C.validate_capture(changed, "calibration")

    def test_16_typed_json_and_duplicate_keys(self):
        for left, right in (({"a": True}, {"a": 1}), ({"a": 1.0}, {"a": 1})):
            with self.assertRaises(ValueError):
                C.strict_equal(left, right)
        for raw in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.assertRaises(ValueError):
                C.decode(raw)

    def test_17_exact_rational_and_interval_caps(self):
        for value in (True, 1.0, "2/4", "0" * 3000):
            with self.assertRaises(ValueError):
                C.rational(value)
        with self.assertRaises(ValueError):
            C.bounded(2**8192)
        with self.assertRaises(ValueError):
            C.interval({"lower": "2", "upper": "1"})

    def test_18_second_closed_value_route_covers_both_phases(self):
        C.validate_constants(self.calibration)
        C.validate_constants(self.heldout)
        fresh = C.independent_closed_bounds()
        self.assertGreater(fresh[3][0], 0)
        self.assertLess(fresh[1][1], fresh[2][0])


if __name__ == "__main__":
    unittest.main()
