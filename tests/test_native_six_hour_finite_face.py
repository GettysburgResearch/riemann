"""Literal prime controls, complete original-kernel KKT, and source face support."""

import importlib.util
import json
import unittest
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "native_finite_face_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_finite_face", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeFiniteFaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scout = M.scout_module()
        cls.kernel = cls.scout.load_module(
            cls.scout.KERNEL_COMMIT, cls.scout.KERNEL_PATH, cls.scout.KERNEL_BLOB
        )
        cls.discovery = json.loads(
            M.frozen_bytes(M.COMMIT, M.DISCOVERY, M.DISCOVERY_BLOB)
        )
        cls.primes = tuple(cls.discovery["models"][1]["primes"])
        cls.models = [
            cls.scout.panel(cls.kernel, cls.primes[:4]),
            cls.scout.panel(cls.kernel, cls.primes),
        ]

    def test_preregistered_actual_prime_windows_are_replayed_without_reselection(self):
        source = self.scout.load_module(
            self.scout.ACQUISITION_COMMIT, self.scout.PRIME_PATH, self.scout.PRIME_BLOB
        )
        acquisition = json.loads(
            self.scout.frozen_bytes(
                self.scout.ACQUISITION_COMMIT,
                self.scout.ACQUISITION_PATH,
                self.scout.ACQUISITION_BLOB,
            )
        )
        self.assertEqual(
            self.primes,
            (99999931, 101999927, 104039917, 106120717, 108243127, 110408003),
        )
        for i, row in enumerate(acquisition["windows"]):
            M.replay_equal(source.window(i), row)
            self.assertTrue(source.prime(row["first_prime"]))
            self.assertFalse(row["window_changed"])

    def test_every_original_factor_allocation_and_same_band_pair_is_retained(self):
        for model in self.models:
            r, K = model["arity"], model["K"]
            self.assertEqual(len(model["all_source_records"]), 2**r)
            self.assertEqual(
                model["same_cardinality_ordered_pairs_excluding_empty"],
                comb(2 * r, r) - 1,
            )
            self.assertTrue(
                all(row["n"] * row["m"] == K for row in model["all_source_records"])
            )
            self.assertEqual(
                len({F(row["n"], row["m"]) for row in model["all_source_records"]}),
                2**r,
            )

    def test_actual_kernel_all_coordinate_kkt_certifies_the_finite_face(self):
        for model in self.models:
            self.assertTrue(model["unique_full_source_simplex_minimizer_certified"])
            self.assertEqual(len(model["all_coordinate_KKT"]), model["arity"])
            for row in model["all_coordinate_KKT"]:
                if row["active"]:
                    self.assertTrue(row["exact_stationarity"])
                else:
                    self.assertTrue(row["strict_KKT_certified"])
                    self.assertFalse(row["opposite_sign_certified"])
            self.assertFalse(model["kernel_replaced_by_its_quadratic_approximation"])

    def test_original_two_ds_physical_factor_is_not_a_surrogate_metric(self):
        for model in self.models:
            r = model["arity"]
            self.assertEqual(
                F(model["physical_Gram_multiplier"]), F(4, 4**r * prod(model["primes"]))
            )
            self.assertFalse(model["literal_prime_product_aliases_assumed"])
        M.replay_equal(self.models, self.discovery["models"])

    def test_new_capped_gamma_agrees_with_frozen_original_overlap_at_small_inputs(self):
        primes = (71, 73, 79, 83)
        for ratio in (F(1), F(73, 71), F(83 * 73, 79 * 71)):
            actual = self.scout.original_gamma(self.kernel, ratio, primes)
            inherited = self.kernel.gamma_square_ratio(ratio)
            self.assertEqual(
                actual, self.scout.normalize_logs(self.kernel, inherited, primes)
            )

    def test_cubic_kernel_bound_and_independent_all_coordinate_second_moments(self):
        control = M.cusp_control(self.kernel)
        self.assertEqual(control["cubic_Taylor_remainder_bound"], 30)
        four, six = M.second_order_control(4), M.second_order_control(6)
        self.assertEqual(four["all_J_gradient_gaps"], [-8, 0, 0, -8])
        self.assertEqual(six["all_J_gradient_gaps"], [-168, -56, 0, 0, -56, -168])
        self.assertEqual(six["all_H_gradient_gaps"], [-16, 0, 0, 0, 0, -16])
        self.assertEqual(
            (
                four["reflection_fixed_X2_coefficient"],
                six["reflection_fixed_X2_coefficient"],
            ),
            ("-4", "-28"),
        )

    def test_face_activation_does_not_delete_inactive_prime_factor_allocations(self):
        for r in (4, 6):
            model = M.face_source_records(r)
            support = (0, r // 2 - 1)
            row = next(
                row for row in model["all_source_records"] if row["support"] == support
            )
            self.assertNotEqual(F(row["actual_two_ds_coefficient"]), 0)
            self.assertFalse(model["inactive_prime_factors_deleted"])
            self.assertEqual(len(model["all_source_records"]), 2**r)

    def test_actual_two_stage_power_paths_preserve_endpoint_product(self):
        for r in (4, 6):
            for powers in ((1, 1), (2, 3)):
                model = M.face_source_records(r, powers)
                self.assertEqual(
                    sum(
                        F(row["actual_two_ds_coefficient"])
                        for row in model["all_source_records"]
                    ),
                    1,
                )
                self.assertEqual(model["first_stage_full_monomial_coefficient"], "0")
                self.assertEqual(model["native_measure"], "2 ds")

    def test_explicit_256_bit_extension_does_not_silently_modify_old_guard(self):
        for bad in (True, 1.0, 0, -1, 1 << 256):
            with self.assertRaises(ValueError):
                self.scout.exact_ratio(bad)
        value = F(
            self.primes[0] * self.primes[1] * self.primes[2],
            self.primes[3] * self.primes[4] * self.primes[5],
        )
        self.assertEqual(self.scout.exact_ratio(value), value)
        with self.assertRaises(ValueError):
            self.kernel.gamma_square_ratio(value)
        for bad in (True, 5, 7):
            with self.assertRaises(ValueError):
                M.second_order_control(bad)

    def test_outward_serialization_preserves_exact_bounds_without_disabling_digit_limits(
        self,
    ):
        for interval in (
            (F(1, 3), F(2, 3)),
            (F(1, 10**5000), F(2, 10**5000)),
            (F(-2, 10**5000), F(-1, 10**5000)),
        ):
            serialized = self.scout.interval_json(interval)
            self.assertLessEqual(F(serialized["lower"]), interval[0])
            self.assertGreaterEqual(F(serialized["upper"]), interval[1])
            self.assertEqual(serialized["outward_dyadic_precision_bits"], 512)
            self.assertTrue(serialized["exact_interval_used_for_all_decisions"])
        with self.assertRaises(ValueError):
            self.scout.interval_json((F(1, 1 << 131073), F(1)))

    def test_typed_artifacts_and_executable_source_authentication_fail_closed(self):
        with self.assertRaises(ValueError):
            M.replay_equal({"arity": 4}, {"arity": 4.0})
        with patch.object(M, "SCOUT_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.scout_module()
        with self.assertRaises(ValueError):
            M.face_source_records(6, (True, 1))


if __name__ == "__main__":
    unittest.main()
