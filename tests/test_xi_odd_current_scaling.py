"""Independent identities and hostile controls; analytic proofs stay in notes."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/xi_odd_current_scaling.py"
SPEC = importlib.util.spec_from_file_location("xi_odd_scaling", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SCOUT_SPEC = importlib.util.spec_from_file_location(
    "xi_odd_scaling_scout", MODULE.SCOUT
)
SCOUT = importlib.util.module_from_spec(SCOUT_SPEC)
SCOUT_SPEC.loader.exec_module(SCOUT)


class XiOddCurrentScalingTests(unittest.TestCase):
    def test_primitive_authentication(self):
        data = MODULE.authenticate_sources()
        self.assertEqual(data["source_count"], 4)
        self.assertTrue(data["exact_git_blobs_and_lf_bytes"])
        self.assertFalse(data["ancestral_code_executed"])

    def test_first_current_polynomials(self):
        self.assertEqual(MODULE.current_polynomials(1), ((1,), (1,)))
        self.assertEqual(MODULE.current_polynomials(3), ((1, 3), (1, Fraction(1, 3))))
        self.assertEqual(
            MODULE.current_polynomials(5), ((1, 10, 5), (1, 2, Fraction(1, 5)))
        )

    def test_heldout_balanced_and_unbalanced_weights(self):
        for k in (17, 29, 47, 63):
            for xi in (Fraction(2, 3), Fraction(13, 7)):
                for d in (0, Fraction(3, 11), 5, -5):
                    direct = d * (((xi + d) / 2) ** k - ((xi - d) / 2) ** k)
                    self.assertEqual(MODULE.current_control(k, xi, d), direct)

    def test_likelihood_polynomials_explicit(self):
        self.assertEqual(MODULE.likelihood_derivative(1), (3,))
        self.assertEqual(MODULE.likelihood_derivative(3), (7, 10, 15))

    def test_likelihood_all_successors(self):
        for k in range(1, 63, 2):
            poly = MODULE.likelihood_derivative(k)
            self.assertTrue(all(c >= 0 for c in poly))
            self.assertGreater(poly[0], 0)
            for z in (Fraction(1, 11), Fraction(1), Fraction(9)):
                self.assertGreater(MODULE.value_at(poly, z), 0)

    def test_exact_two_atom_covariance(self):
        # The monotone weighting argument is independent of the Xi density.
        for k in (1, 7, 31, 61):
            p, _ = MODULE.current_polynomials(k)
            nxt, _ = MODULE.current_polynomials(k + 2)
            for low, high in (
                (Fraction(1, 7), Fraction(2)),
                (Fraction(3), Fraction(11)),
            ):
                ratio_low = MODULE.value_at(nxt, low) / MODULE.value_at(p, low)
                ratio_high = MODULE.value_at(nxt, high) / MODULE.value_at(p, high)
                self.assertGreater((high - low) * (ratio_high - ratio_low), 0)

    def test_gaussian_moments_low_orders(self):
        self.assertEqual(MODULE.gaussian_derivative_moment(0), (1,))
        self.assertEqual(
            MODULE.gaussian_derivative_moment(1), (Fraction(3, 2), Fraction(1, 4))
        )
        self.assertEqual(
            MODULE.gaussian_derivative_moment(2),
            (Fraction(15, 4), Fraction(5, 4), Fraction(1, 16)),
        )

    def test_independent_mgf_all_moments(self):
        for q in range(9):
            self.assertEqual(
                MODULE.gaussian_derivative_moment(q), MODULE.gaussian_mgf_moment(q)
            )

    def test_translation_kappa_zero(self):
        for q in range(9):
            self.assertEqual(
                MODULE.current_translation_coefficients(q)[0],
                Fraction(1, 4**q * MODULE.math.factorial(q)),
            )

    def test_translation_second_order(self):
        self.assertEqual(
            MODULE.current_translation_coefficients(1),
            (Fraction(1, 4), Fraction(1, 24)),
        )

    def test_boundary_window_rational_heldouts(self):
        for q in (Fraction(7, 3), Fraction(19, 2), Fraction(101, 7)):
            for delta in (Fraction(-17, 5), Fraction(0), Fraction(37, 11)):
                row = MODULE.boundary_control(q, delta)
                self.assertEqual(
                    row["window_coefficient"],
                    delta + Fraction(7, 2) * q + Fraction(3, 2) + 1 / (4 * q + 2),
                )

    def test_boundary_center_exact_zero(self):
        for q in (2, 4, 8, 10, 16):
            offset = -Fraction(7, 2) * q - Fraction(3, 2) - Fraction(1, 4 * q + 2)
            self.assertEqual(
                MODULE.boundary_control(q, offset)["window_coefficient"], 0
            )

    def test_plus_measure_not_current_measure(self):
        # At kappa=0 the plus law is ordinary Gaussian, whereas the current law is u^2-weighted.
        self.assertNotEqual(MODULE.gaussian_derivative_moment(1)[0], Fraction(1, 2))

    def test_carrier_zero_and_sign(self):
        for kappa in (Fraction(0), Fraction(1, 3), Fraction(7, 2)):
            center = (1 + kappa**2 / 2) / 4
            self.assertEqual(MODULE.carrier_boundary_control(kappa, center), 0)
            self.assertGreater(MODULE.carrier_boundary_control(kappa, center - 1), 0)
            self.assertLess(MODULE.carrier_boundary_control(kappa, center + 1), 0)

    def test_order_caps_and_types(self):
        for bad in (True, False, 0, 2, -1, 65, 10**30, 3.0, Fraction(3), "3"):
            with self.assertRaises(ValueError):
                MODULE.current_polynomials(bad)
        with self.assertRaises(ValueError):
            MODULE.likelihood_derivative(63)

    def test_moment_caps_and_types(self):
        for bad in (True, -1, 9, 1.0, Fraction(1), "1"):
            with self.assertRaises(ValueError):
                MODULE.gaussian_derivative_moment(bad)

    def test_exact_input_contract(self):
        for bad in (True, 1.0, float("inf"), float("nan"), "1", None):
            with self.assertRaises(TypeError):
                MODULE.exact(bad)
        for bad in (2**64, Fraction(1, 2**64)):
            with self.assertRaises(ValueError):
                MODULE.exact(bad)
        for q in (0, -1):
            with self.assertRaises(ValueError):
                MODULE.boundary_control(q, 0)
        with self.assertRaises(ValueError):
            MODULE.carrier_boundary_control(-1, 0)

    def test_manifest_scope_and_omission_rejected(self):
        for kind in ("omission", "normalization", "gauge"):
            manifest = MODULE.expected_manifest()
            if kind == "omission":
                manifest["sources"].pop()
            elif kind == "normalization":
                manifest["normalization"] = "PhiXi=phi0"
            else:
                manifest["parameter_firewall"] = "choose a new native physical lambda"
            with self.assertRaises(ValueError):
                MODULE.authenticate_sources(manifest)

    def test_source_bytes_must_replay(self):
        with (
            mock.patch.object(
                MODULE.subprocess, "check_output", return_value=b"wrong\n"
            ),
            self.assertRaises(ValueError),
        ):
            MODULE.authenticate_sources()

    def test_fixture_source_authenticated_rebuild(self):
        data = json.loads(MODULE.FIXTURE.read_text(encoding="utf-8"))
        MODULE.validate_report(data)
        self.assertEqual(data["complete_current_grid_rows"], 896)
        self.assertEqual(len(data["likelihood_successor_panel"]), 31)
        self.assertEqual(len(data["gaussian_moment_panel"]), 9)
        self.assertEqual(len(data["boundary_window_panel"]), 32)

    def test_report_scope_mutations_rejected(self):
        data = MODULE.build_report()
        for key in data["scopes"]:
            mutant = copy.deepcopy(data)
            mutant["scopes"][key] = True
            with self.assertRaises(ValueError):
                MODULE.validate_report(mutant)

    def test_report_coefficient_and_type_mutations_rejected(self):
        data = MODULE.build_report()
        mutants = []
        mutant = copy.deepcopy(data)
        mutant["likelihood_successor_panel"].pop()
        mutants.append(mutant)
        mutant = copy.deepcopy(data)
        mutant["likelihood_successor_panel"][0]["K"] = True
        mutants.append(mutant)
        mutant = copy.deepcopy(data)
        mutant["gaussian_moment_panel"][1]["moment_polynomial_in_kappa_squared"][0] = (
            "1/2"
        )
        mutants.append(mutant)
        mutant = copy.deepcopy(data)
        mutant["arithmetic_class"] = "DIRECTED_INTERVAL"
        mutants.append(mutant)
        for mutant in mutants:
            with self.assertRaises(ValueError):
                MODULE.validate_report(mutant)

    def test_scout_caps_without_running_quadrature(self):
        for args in ((True, "micro", "1"), (0, "micro", "1"), (21, "micro", "1")):
            with self.assertRaises(ValueError):
                SCOUT.run_case(*args)
        for mode, parameter in (
            ("micro", "-1"),
            ("macro", "0"),
            ("boundary", "-1"),
            ("intermediate", "5"),
            ("micro", "nan"),
            ("micro", "inf"),
            ("micro", None),
            ("fixed", "2"),
        ):
            with self.assertRaises(ValueError):
                SCOUT.current_order(SCOUT.mp.mpf(4), mode, parameter)

    def test_scout_declares_nondirected_arithmetic(self):
        source = MODULE.SCOUT.read_text(encoding="utf-8")
        self.assertIn('"NON_DIRECTED_HIGH_PRECISION"', source)
        self.assertIn('"certified": False', source)
        self.assertIn(
            '"bounded_quadrature_not_full_integral_certificate": True', source
        )


if __name__ == "__main__":
    unittest.main()
