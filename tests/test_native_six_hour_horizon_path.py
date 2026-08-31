"""Independent source, cone, and acceptance controls for the horizon-path replay."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from itertools import product
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_horizon_path_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_horizon_path_final_test", PATH)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class NativeHorizonPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = C.frozen("scout", True)
        cls.calibration = json.loads(C.frozen("calibration"))
        cls.heldout = json.loads(C.frozen("heldout"))
        cls.panel25 = cls.calibration["panels"][0]
        cls.panel60 = cls.heldout["panels"][1]
        cls.attempt25 = cls.panel25["all16_declared_start_outcomes"][0]

    @staticmethod
    def constant_cone(lower, upper, status):
        return [
            {
                "family": family,
                "sigma": sigma,
                "tau": tau,
                "coefficient_intervals_constant_linear_quadratic": [
                    {"lower": str(lower), "upper": str(upper)},
                    {"lower": "0", "upper": "0"},
                    {"lower": "0", "upper": "0"},
                ],
                "lower_envelope_minimum": str(lower),
                "lower_minimizer": "0",
                "upper_envelope_minimum": str(upper),
                "upper_minimizer": "0",
                "status": status,
            }
            for sigma, tau in product((0, 1), repeat=2)
            for family in ("p", "q")
        ]

    def test_01_complete_two_phase_replay(self):
        result = C.build()
        self.assertEqual([row["horizon"] for row in result["panels"]], [25, 30, 60])
        self.assertEqual(result["panels"][0]["records"], 63)
        self.assertEqual(result["panels"][2]["records"], 140)
        self.assertEqual([row["ratios"] for row in result["panels"]], [45, 55, 89])
        self.assertTrue(
            all(
                row["all_global_certificate_attempts"] == list(range(16))
                for row in result["panels"]
            )
        )
        self.assertTrue(
            all(
                row["strict_unique_oriented_path_attempts"] == list(range(16))
                for row in result["panels"]
            )
        )
        self.assertEqual(
            [
                row["first_certified_clipping_regime"]["upper_clipped"]
                for row in result["panels"]
            ],
            [False, True, True],
        )
        self.assertEqual(result["independent_all_monomial_control"]["cases"], 1728)
        self.assertIs(result["all_height_optimum_claimed"], False)
        self.assertIs(result["full_gamma_identified"], False)

    def test_02_unchanged_heldout_executable(self):
        self.assertEqual(C.frozen("scout"), C.frozen("heldout_scout"))
        self.assertNotEqual(C.PINS["calibration"][0], C.PINS["heldout"][0])
        self.assertEqual(
            self.calibration["owned_sha256_lf"], self.heldout["owned_sha256_lf"]
        )

    def test_03_all_monomial_pairs_have_actual_factor_two(self):
        result = C.monomial_control(self.scout)
        self.assertEqual(result["literal_measure_factor"], 2)
        row = self.scout.monomial_decoder((1, 0, 0), (0, 1, 0))
        moments = [
            C.moment_on_power_path(i, powers, (1, 2, 3))
            for i, powers in self.scout.BASIS
        ]
        coefficient = row[0] + sum(a * b for a, b in zip(row[1:], moments, strict=True))
        self.assertEqual(coefficient, F(2, 3))
        self.assertNotEqual(coefficient, F(1, 3))

    def test_04_actual_higher_physical_aliases(self):
        control = C.source_alias_control(self.scout, self.panel60)
        self.assertEqual(control["M6"], "1/5")
        self.assertEqual(control["M13"], "1/2")
        self.assertEqual(control["all_gcd_aliases"], {2: [1, 2, 3, 4, 5], 5: [1, 2, 3]})
        self.assertEqual(
            F(control["sqrt2_times_ratio2_coefficient"]), -F(26831, 23040) - F(1, 200)
        )
        self.assertEqual(
            F(control["sqrt5_times_ratio5_coefficient"]), -F(53, 48) - F(5, 96)
        )

    def test_05_power_path_moments_and_input_caps(self):
        self.assertEqual(C.moment_on_power_path(0, (0, 1, 0), (1, 2, 3)), F(1, 3))
        self.assertEqual(C.moment_on_power_path(0, (0, 2, 0), (1, 2, 3)), F(1, 5))
        for args in (
            (True, (0, 1, 0), (1, 2, 3)),
            (0, (0, True, 0), (1, 2, 3)),
            (0, (0, 1, 0), (1, 2, 0)),
            (0, (0, 1, 0), (1, 2, 5)),
        ):
            with self.assertRaises(ValueError):
                C.moment_on_power_path(*args)

    def test_06_quadratic_interior_and_endpoint_controls(self):
        self.assertEqual(C.minimum_quadratic((F(1), F(-4), F(4))), (F(), F(1, 2)))
        self.assertEqual(C.minimum_quadratic((F(1), F(-5), F(5))), (-F(1, 4), F(1, 2)))
        self.assertEqual(C.minimum_quadratic((F(1), F(), F(-2))), (-F(1), F(1)))
        self.assertEqual(C.minimum_quadratic((F(), F(), F())), (F(), F()))

    def test_07_cone_pass_fail_and_unknown_stay_distinct(self):
        self.assertTrue(C.validate_cone(self.constant_cone(F(1), F(2), "PASS")))
        self.assertFalse(C.validate_cone(self.constant_cone(F(-2), F(-1), "FAIL")))
        self.assertFalse(C.validate_cone(self.constant_cone(F(-1), F(1), "UNKNOWN")))
        counterfeit = self.constant_cone(F(-1), F(1), "PASS")
        with self.assertRaisesRegex(ValueError, "actual exact cone status"):
            C.validate_cone(counterfeit)

    def test_08_global_claim_requires_full_cone(self):
        changed = copy.deepcopy(self.attempt25)
        changed["certificate"]["eight_source_quadratics"] = self.constant_cone(
            F(-1), F(1), "UNKNOWN"
        )
        changed["certificate"]["global_all_path_source_optimum_certified"] = True
        with self.assertRaisesRegex(ValueError, "full source cone"):
            C.validate_attempt(changed)
        changed["certificate"]["global_all_path_source_optimum_certified"] = False
        self.assertFalse(C.validate_attempt(changed))

    def test_09_root_box_and_contraction_counterfeits(self):
        changed = copy.deepcopy(self.attempt25)
        changed["certificate"]["root_box"][0]["lower"] = "-1"
        with self.assertRaisesRegex(ValueError, "entire declared root box"):
            C.validate_attempt(changed)
        changed = copy.deepcopy(self.attempt25)
        changed["certificate"]["contraction_upper"] = "1"
        with self.assertRaisesRegex(ValueError, "strict rational contraction"):
            C.validate_attempt(changed)
        changed = copy.deepcopy(self.attempt25)
        changed["certificate"]["clipping_regime"]["upper_clipped"] = True
        with self.assertRaisesRegex(ValueError, "endpoint clipping"):
            C.validate_attempt(changed)

    def test_10_refusal_cannot_become_global_success(self):
        row = {
            "certificate": {
                "root_exists_and_unique_in_box": False,
                "global_all_path_source_optimum_certified": False,
                "retained_guard_failure": "declared test refusal",
            }
        }
        self.assertFalse(C.validate_attempt(row))
        row["certificate"]["global_all_path_source_optimum_certified"] = True
        with self.assertRaisesRegex(ValueError, "retained root refusal"):
            C.validate_attempt(row)

    def test_11_omitted_record_and_wrong_physical_column(self):
        changed = copy.deepcopy(self.panel60)
        changed["all_ordered_records"].pop()
        with self.assertRaisesRegex(ValueError, "ordered-record census"):
            C.validate_panel(changed)
        changed = copy.deepcopy(self.panel60)
        changed["all21_physical_rational_columns"][0][0] = str(
            F(changed["all21_physical_rational_columns"][0][0]) + 1
        )
        with self.assertRaisesRegex(ValueError, "typed complete"):
            C.validate_panel(changed)

    def test_12_no_unmeasured_rank_or_gamma_promotion(self):
        for key in (
            "all20_physical_directions_claimed_independent",
            "full_gamma_identified",
        ):
            changed = copy.deepcopy(self.panel25)
            changed[key] = True
            with self.assertRaisesRegex(ValueError, "actual source scope"):
                C.validate_panel(changed)

    def test_13_numeric_alias_and_rational_counterfeits(self):
        for left, right in (({"n": True}, {"n": 1}), ({"n": 1.0}, {"n": 1})):
            with self.assertRaises(ValueError):
                C.strict_equal(left, right)
        for value in (True, 1.0, "2/4", "0" * 3000):
            with self.assertRaises(ValueError):
                C.rational(value)

    def test_14_fixed_horizon_and_local_exponent_caps(self):
        self.assertEqual(C.supported(25), sorted(set(C.supported(25))))
        self.assertNotIn(7, C.supported(60))
        for value in (True, 60.0, 50, 61):
            with self.assertRaises(ValueError):
                C.supported(value)
        for value in (True, 6, -1, 1.0):
            with self.assertRaises(ValueError):
                self.scout.square_root_coefficient(value)


if __name__ == "__main__":
    unittest.main()
