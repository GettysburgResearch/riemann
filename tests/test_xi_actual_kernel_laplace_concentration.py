"""Hostile exact controls for the new actual-kernel analytic packet."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_actual_kernel_laplace_concentration.py"
SPEC = importlib.util.spec_from_file_location("xi_actual_laplace", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class XiActualLaplaceTests(unittest.TestCase):
    def test_source_authentication(self):
        self.assertEqual(MODULE.authenticate_sources()["source_count"], 6)

    def test_full_line_normalization(self):
        data = MODULE.kernel_operator()
        self.assertEqual(data["actual_kernel_over_historical_phi0"], 2)
        self.assertEqual(data["quadratic_density_multiplier"], 4)
        self.assertFalse(data["frequency_rescaling"])

    def test_k1_exact_edge(self):
        data = MODULE.asymptotic_constants(1)
        self.assertEqual(data["R_constant"], 1)
        self.assertEqual(data["R_x_squared_coefficient"], 0)
        self.assertEqual(data["adapted_p_limit"], Fraction(1, 2))
        self.assertEqual(data["p_correction_times_pi_E_xi_squared_limit"], 0)

    def test_fifth_endpoint_constants(self):
        data = MODULE.asymptotic_constants(5)
        self.assertEqual(data["adapted_p_limit"], Fraction(1, 10))
        self.assertEqual(
            data["p_correction_times_pi_E_xi_squared_limit"], Fraction(6, 5)
        )
        self.assertEqual(data["m2_times_pi_E_limit"], Fraction(3, 2))

    def test_current_weight_balanced_and_unbalanced(self):
        for order in range(1, 16, 2):
            for d in (0, Fraction(1, 7), -3, 9):
                value = MODULE.current_weight(order, Fraction(1, 2), d)
                self.assertGreaterEqual(value, 0)
                self.assertEqual(
                    value, MODULE.current_weight(order, Fraction(1, 2), -d)
                )

    def test_moments_include_weight_and_q0(self):
        self.assertEqual(MODULE.gaussian_moment_constant(0), 1)
        self.assertEqual(MODULE.gaussian_moment_constant(1), Fraction(3, 2))
        self.assertEqual(MODULE.gaussian_moment_constant(2), Fraction(15, 4))
        self.assertNotEqual(MODULE.gaussian_moment_constant(1), Fraction(1, 2))

    def test_universal_zero_boundary(self):
        for order in range(1, 16, 2):
            self.assertEqual(MODULE.boundary_limit(order, Fraction(1, 4)), 0)
            self.assertGreater(MODULE.boundary_limit(order, 0), 0)
            self.assertLess(MODULE.boundary_limit(order, Fraction(1, 2)), 0)

    def test_order_and_moment_caps(self):
        for value in (True, 0, 2, -1, 17, 10**20, 5.0, Fraction(5)):
            with self.assertRaises(ValueError):
                MODULE.polynomials(value)
        for value in (True, -1, 7, 1.0, Fraction(1), 10**20):
            with self.assertRaises(ValueError):
                MODULE.gaussian_moment_constant(value)

    def test_exact_scalar_and_domain_guards(self):
        for value in (True, 1.0, float("inf"), float("nan"), "1", None):
            with self.assertRaises(TypeError):
                MODULE.boundary_limit(5, value)
        with self.assertRaises(ValueError):
            MODULE.boundary_limit(5, 2**64)
        with self.assertRaises(ValueError):
            MODULE.boundary_limit(5, Fraction(1, 2**64))
        for xi in (0, -1):
            with self.assertRaises(ValueError):
                MODULE.current_weight(5, xi, 1)

    def test_manifest_rejects_omission_and_normalization_drift(self):
        manifest = MODULE.expected_manifest()
        manifest["sources"].pop()
        with self.assertRaises(ValueError):
            MODULE.authenticate_sources(manifest)
        manifest = MODULE.expected_manifest()
        manifest["normalization"] = "PhiXi=phi0"
        with self.assertRaises(ValueError):
            MODULE.authenticate_sources(manifest)

    def test_blob_mismatch_rejected(self):
        with (
            mock.patch.object(MODULE.subprocess, "check_output", return_value=b"bad\n"),
            self.assertRaises(ValueError),
        ):
            MODULE.authenticate_sources()

    def test_fixture_replays(self):
        report = json.loads(MODULE.FIXTURE.read_text(encoding="utf-8"))
        MODULE.validate_report(report)
        self.assertEqual(report["current_weight_identities_replayed"], 224)
        self.assertFalse(report["scope"]["analytic_proof_formally_machine_verified"])

    def test_mutated_coefficients_and_scopes_rejected(self):
        report = MODULE.build_report()
        for section, field, value in (
            ("normalization", "actual_kernel_over_historical_phi0", 1),
            ("normalization", "frequency_rescaling", True),
            ("tail_constants", "global_product_Gaussian_majorant_multiplier", 1),
            ("scope", "source_Pick_or_physical_scale_transfer", True),
            ("scope", "floating_point_Xi_samples", False),
        ):
            mutant = copy.deepcopy(report)
            mutant[section][field] = value
            with self.assertRaises(ValueError):
                MODULE.validate_report(mutant)

    def test_finite_panel_deletion_and_type_drift_rejected(self):
        report = MODULE.build_report()
        report["odd_order_constants"].pop()
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)
        report = MODULE.build_report()
        report["odd_order_constants"][0]["K"] = True
        with self.assertRaises(ValueError):
            MODULE.validate_report(report)


if __name__ == "__main__":
    unittest.main()
