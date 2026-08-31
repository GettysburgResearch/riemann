"""Source-local and independently integrated gauge-connection regression checks."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "gauge_connection_source_transport.py"
)
SPEC = importlib.util.spec_from_file_location("gauge_connection_transport", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class GaugeConnectionTests(unittest.TestCase):
    def test_native_degree_two_gauge_is_not_constant_in_parameter(self):
        record = M.local_record()
        self.assertEqual(record["g_x_coefficients"][1], ["0"])
        self.assertEqual(record["g_x_coefficients"][2], ["0", "-1/4", "1/4"])
        self.assertEqual(record["g_quadratic_tau_derivative"], ["-1/4", "1/2"])

    def test_actual_missing_connection_is_observed_at_same_integer(self):
        record = M.connection_record(1)
        self.assertEqual(record["transported_Euler_integral"], "-1/24")
        self.assertEqual(record["connection_integral"], "1/24")
        self.assertEqual(
            record["observed_Gram_coefficient_times_N_over_Gamma0"], "1/576"
        )
        self.assertEqual(record["observed_Gram_sign_matrix"], [[1, -1], [-1, 1]])
        self.assertEqual(
            record["integrated_two_sector_diagonal_times_N_over_Gamma0"], "1/288"
        )

    def test_subcritical_owner_projection_changes_under_actual_gauge(self):
        record = M.connection_record(3)
        self.assertEqual(record["half_divisor_owner_integral"], "-229/1792")
        self.assertEqual(record["Euler_owner_integral"], "-1/10")
        self.assertNotEqual(
            record["half_divisor_owner_integral"], record["Euler_owner_integral"]
        )

    def test_gauge_site_recombination_has_nonzero_diagonal_correction(self):
        record = M.connection_record(1)
        self.assertEqual(record["primitive_diagonal_correction_times_N"], "1/15")
        self.assertEqual(
            Fraction(record["primitive_H_diagonal_times_N"])
            - Fraction(record["primitive_expanded_diagonal_times_N"]),
            Fraction(1, 15),
        )

    def test_scalar_beta_route_uses_exact_endpoint_integrals(self):
        self.assertEqual(M.beta(2, 4), Fraction(1, 20))
        self.assertEqual(M.beta(3, 4), Fraction(1, 60))
        self.assertEqual(M.beta(4, 4), Fraction(1, 140))
        self.assertEqual(M.beta(5, 4), Fraction(1, 280))
        self.assertEqual(
            2
            * (
                M.beta(2, 4)
                + Fraction(3, 4) * M.beta(3, 4)
                + Fraction(3, 16) * M.beta(4, 4)
                + Fraction(1, 64) * M.beta(5, 4)
            ),
            Fraction(229, 1792),
        )

    def test_higher_core_connection_is_not_a_finite_depth_accident(self):
        for k in (4, 8, 16):
            record = M.connection_record(k)
            self.assertGreater(Fraction(record["connection_integral"]), 0)
            self.assertEqual(
                Fraction(record["connection_integral"])
                + Fraction(record["transported_Euler_integral"]),
                0,
            )
        # These are finite controls; the limit itself is proved by dominated convergence.

    def test_work_caps_reject_bool_fractional_and_large_inputs(self):
        for k in (True, 1.0, 0, 17):
            with self.subTest(k=k), self.assertRaises(ValueError):
                M.connection_record(k)
        for args in ((True, 2), (2, 0), (41, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                M.beta(*args)

    def test_frozen_executable_is_authenticated_before_import(self):
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M, "_ALGEBRA", None),
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.load_algebra()

    def test_artifact_comparison_preserves_numeric_types(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()
