"""Actual homotopy leakage, its carrier correction, and diagonal resolutions."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native_phase_leakage_connection_cancellation.py"
)
SPEC = importlib.util.spec_from_file_location("phase_leakage", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativePhaseLeakageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        key = (M.EA, M.EA_PATH)
        cls.algebra = M.load_primitive(key, M.source_bytes(key))

    def test_native_complete_connection_cancels_three_signed_groups(self):
        result = M.activation_column(self.algebra)
        u = Fraction(1, 166320)
        self.assertEqual(
            [Fraction(x) for x in result["integrated_three_terms"]],
            [-14 * u, 15 * u, -u],
        )
        self.assertEqual(result["integrated_total"], "0")
        self.assertEqual(
            result["integrated_three_terms"], result["beta_integral_route"]
        )

    def test_owner_projection_and_dropped_connection_have_explicit_residuals(self):
        result = M.activation_column(self.algebra)
        u = Fraction(1, 166320)
        self.assertEqual(Fraction(result["owner_plus_connection_residual"]), -15 * u)
        self.assertEqual(Fraction(result["transport_without_connection_residual"]), u)

    def test_integrated_diagonal_depends_on_declared_atom_resolution(self):
        result = M.activation_column(self.algebra)
        u2 = Fraction(1, 166320) ** 2
        self.assertEqual(Fraction(result["two_mechanism_diagonal"]), 2 * u2)
        self.assertEqual(Fraction(result["three_group_diagonal"]), 422 * u2)
        self.assertEqual(
            Fraction(result["individual_activation_site_diagonal"]),
            Fraction(175, 2) * u2,
        )
        self.assertNotEqual(
            result["two_mechanism_diagonal"],
            result["two_mechanism_continuous_tau_diagonal"],
        )

    def test_nonconstant_tau_density_requires_its_connection_correction(self):
        result = M.activation_column(self.algebra)
        self.assertEqual(Fraction(result["tau_density_residual"]), Fraction(1, 123552))
        self.assertNotEqual(result["tau_density_residual"], "0")

    def test_all_bounded_owner_core_depths_obey_literal_product_rule(self):
        for owners, cores, p in ((1, 1, 2), (2, 3, 5), (4, 6, 3), (8, 12, 11)):
            with self.subTest(owners=owners, cores=cores):
                result = M.activation_column(self.algebra, owners, cores, p)
                self.assertEqual(result["integrated_total"], "0")
                self.assertEqual(
                    result["integrated_three_terms"], result["beta_integral_route"]
                )

    def test_gauge_primitive_has_zero_endpoints_and_no_tau_phase_surrogate(self):
        result = M.activation_column(self.algebra)
        b = [Fraction(x) for x in result["gauge_polynomial"]]
        self.assertEqual(b[0], 0)
        self.assertEqual(sum(b), 0)
        self.assertEqual(
            sum(x * Fraction(1, 2) ** i for i, x in enumerate(b)), Fraction(-1, 48)
        )

    def test_parameter_types_and_degree_caps_fail_closed(self):
        for args in ((True, 6, 3), (4, 0, 3), (9, 6, 3), (4, 13, 3), (4, 6, True)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                M.activation_column(self.algebra, *args)
        with self.assertRaises(ValueError):
            M.beta(True, 2)
        with self.assertRaises(ValueError):
            M.beta(41, 2)

    def test_unverified_executable_bytes_and_source_mutation_rejected(self):
        with self.assertRaisesRegex(ValueError, "executable primitive Git blob"):
            M.load_primitive((M.EA, M.EA_PATH), b"raise RuntimeError('not executed')")
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))

    def test_json_numeric_type_substitution_is_not_accepted(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()
