"""Complete finite source, original metric, global variation and curvature."""

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "global_native_geodesic_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_global_geodesic", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeGlobalGeodesicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = M.scout_module()
        cls.native = {p: cls.module.native_field(p) for p in (2, 3, 5)}
        cls.energy = {
            p: cls.module.energy_polynomial(data[1]) for p, data in cls.native.items()
        }
        cls.curvature = M.curvature_control(
            cls.module, {p: data[0] for p, data in cls.native.items()}
        )
        cls.decisions = M.monotonicity_certificate(cls.module, cls.energy)

    def test_all_63_pairs_and_45_ratios_use_the_same_schedule(self):
        for records, ratios, endpoints, _ in self.native.values():
            self.assertEqual(len(records), 63)
            self.assertEqual(len(ratios), 45)
            self.assertEqual(len(endpoints), 16)
            self.assertTrue(all(row["n"] * row["m"] <= 25 for row in records))

    def test_every_product_endpoint_and_root_free_left_are_preserved(self):
        for records, _, endpoints, _ in self.native.values():
            self.assertTrue(all(values[1:] == [0, 0] for values in endpoints.values()))
            self.assertTrue(
                all(
                    row["epsilon_coefficients_before_physical_weight"]
                    == ["0", "0", "0"]
                    for row in records
                    if row["n"] == 1
                )
            )
            self.assertTrue(
                any(
                    row["m"] == 1
                    and row["epsilon_coefficients_before_physical_weight"][0] != "0"
                    for row in records
                )
            )

    def test_curvature_stokes_comparison_is_recordwise(self):
        self.assertEqual(self.curvature["physical_record_count"], 63)
        self.assertEqual(len(self.curvature["records"]), 63)
        self.assertGreater(
            self.curvature["nonzero_first_and_second_variations"]["3"][0], 0
        )
        self.assertGreater(
            self.curvature["nonzero_first_and_second_variations"]["3"][1], 0
        )

    def test_common_parameter_augmentation_kills_exact_source_direction(self):
        self.assertTrue(self.curvature["pointwise_common_direction_zero"])
        for row in self.curvature["records"]:
            self.assertEqual(
                sum(
                    F(value[0])
                    for value in row["curvature_and_Stokes_coefficients"].values()
                ),
                0,
            )
        total = self.module.ex()
        for coefficients in self.energy.values():
            total = self.module.ea(total, coefficients[1])
        self.assertEqual(total, self.module.ex())

    def test_prime_five_field_is_affine_and_whole_axis_minimum_is_native_square_path(
        self,
    ):
        self.assertEqual(
            self.curvature["nonzero_first_and_second_variations"]["5"][1], 0
        )
        self.assertEqual(self.energy[5][3:], (self.module.ex(), self.module.ex()))
        decision = self.decisions["5"]
        self.assertEqual(decision["unique_axis_minimum"], "-1")
        self.assertEqual(decision["actual_global_schedule"], ["s", "s", "s^2"])
        self.assertGreater(F(decision["gain_interval"]["lower"]), F(341, 100))

    def test_prime_two_axis_is_monotone_and_preserves_original_measure(self):
        decision = self.decisions["2"]
        self.assertEqual(decision["unique_axis_minimum"], "1")
        self.assertLess(F(decision["derivative_uniform_interval"]["upper"]), -2)
        self.assertGreater(F(decision["gain_interval"]["lower"]), F(339, 100))

    def test_primary_prime_three_has_one_interior_axis_minimum(self):
        decision = self.decisions["3"]
        self.assertEqual(
            decision["unique_axis_minimum_interval"], ["-53/100", "-13/25"]
        )
        self.assertGreater(
            F(decision["second_derivative_uniform_interval"]["lower"]), F(165, 100)
        )
        self.assertGreater(F(decision["grid_gain_interval"]["lower"]), F(23, 100))

    def test_diagonal_resolutions_do_not_replace_full_observed_energy(self):
        diagonals = self.native[3][3]
        self.assertEqual(
            set(diagonals),
            {
                "primitive_2ds_site",
                "integrated_site",
                "integrated_pair",
                "ratio_coalesced",
            },
        )
        self.assertEqual(len({row[0] for row in diagonals.values()}), 4)
        pair_energy = self.module.es(
            self.module.gamma(F(1)), diagonals["integrated_pair"][0]
        )
        self.assertNotEqual(pair_energy, self.energy[3][0])

    def test_source_improvement_is_not_just_a_different_constant_baseline(self):
        self.assertEqual(self.energy[2][0], self.energy[3][0])
        self.assertEqual(self.energy[2][0], self.energy[5][0])
        interval = self.module.ei(self.energy[2][0])
        self.assertGreater(interval[0], F(16672, 100))
        self.assertLess(interval[1], F(16673, 100))

    def test_bad_source_parameter_and_typed_json_are_rejected(self):
        for bad in (True, F(3, 2), 0.25):
            with self.assertRaises(ValueError):
                M.polynomial_value(self.module, self.energy[3], bad)
        with self.assertRaises(ValueError):
            M.replay_equal({"count": 63}, {"count": 63.0})

    def test_source_authentication_happens_before_execution(self):
        with patch.object(M, "SCOUT_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.scout_module()


if __name__ == "__main__":
    unittest.main()
