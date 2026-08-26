"""Tests for the odd-notch logarithmic-depth zero firewall."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_logarithmic_depth_zero_firewall.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md")

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_logarithmic_depth_zero_firewall", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load logarithmic-depth replay")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def independent_irreducible_count(q_value: int, degree: int) -> int:
    counts = [0] * (degree + 1)
    for current in range(1, degree + 1):
        subtotal = q_value**current
        for proper in range(1, current):
            if current % proper == 0:
                subtotal -= proper * counts[proper]
        counts[current] = subtotal // current
    return counts[degree]


class QuadraticFamilyLogarithmicDepthZeroFirewallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_irreducible_counts_and_modulus_degree(self) -> None:
        for q_value in MODULE.REPLAY_Q_VALUES:
            running = 0
            for degree in range(1, 2 * MODULE.MAX_REPLAY_J + 2):
                expected = independent_irreducible_count(q_value, degree)
                self.assertEqual(MODULE.irreducible_count(q_value, degree), expected)
                running += degree * expected
                self.assertEqual(MODULE.modulus_degree(q_value, degree), running)

    def test_exact_modulus_bounds(self) -> None:
        for q_value in MODULE.REPLAY_Q_VALUES:
            for depth in range(1, MODULE.MAX_REPLAY_J + 1):
                top_degree = 2 * depth + 1
                ell = MODULE.modulus_degree(q_value, top_degree)
                self.assertGreaterEqual(3 * ell, 2 * q_value**top_degree)
                self.assertLess((q_value - 1) * ell, q_value ** (top_degree + 1))
                self.assertTrue(MODULE.modulus_bounds_hold(q_value, depth))

    def test_anti_concentration_chain_on_small_exact_panels(self) -> None:
        for q_value, depth in MODULE.CENTRAL_PANELS:
            top_degree = 2 * depth + 1
            count = MODULE.irreducible_count(q_value, top_degree)
            atom = MODULE.central_rademacher_atom(count)
            self.assertLessEqual(atom * atom, Fraction(1, count))
            self.assertLessEqual(
                Fraction(1, count),
                MODULE.beta_squared_majorant(q_value, depth),
            )

    def test_safe_window_is_an_initial_segment(self) -> None:
        for q_value, h_value in MODULE.WINDOW_INPUTS:
            maximum = MODULE.maximum_safe_depth(q_value, h_value)
            self.assertGreater(maximum, 0)
            for depth in range(1, maximum + 1):
                self.assertTrue(MODULE.safe_terminal_depth(q_value, h_value, depth))
            self.assertFalse(MODULE.safe_terminal_depth(q_value, h_value, maximum + 1))

    def test_safe_condition_controls_pnt_exponent(self) -> None:
        for q_value, h_value in MODULE.WINDOW_INPUTS:
            maximum = MODULE.maximum_safe_depth(q_value, h_value)
            for depth in range(1, maximum + 1):
                panel = MODULE.layer_parameters(q_value, h_value, depth)
                minimum_degree = panel["d"]
                ell = panel["ell_r"]
                self.assertLessEqual(4 * ell, minimum_degree)
                self.assertGreater(minimum_degree, panel["r"])
                self.assertLessEqual(panel["twice_pnt_exponent"], -minimum_degree // 2)
                self.assertEqual(
                    panel["rough_layer_weight"],
                    str(Fraction(1, minimum_degree**2)),
                )

    def test_fixed_epsilon_power_panels_are_eventually_safe(self) -> None:
        for q_value in MODULE.REPLAY_Q_VALUES:
            for exponent in range(12, 33, 4):
                depth = 3 * exponent // 8
                self.assertTrue(
                    MODULE.safe_terminal_depth(q_value, q_value**exponent, depth)
                )

    def test_marked_prime_multiplicity_and_exclusion_fence(self) -> None:
        for complement_multiplicity in range(4):
            signature = MODULE.marked_prime_signature(100, 3, complement_multiplicity)
            self.assertEqual(signature["a_d"], complement_multiplicity + 1)
            self.assertEqual(
                signature["top_sign_coefficient"], complement_multiplicity + 1
            )
            self.assertTrue(signature["marked_pair_overcounts_by_m_d"])
            self.assertTrue(
                signature["R_divides_C_is_dropped_only_to_enlarge_upper_bound"]
            )

    def test_report_source_locks_and_claim_fences(self) -> None:
        MODULE.check_source_blobs()
        self.assertIsNone(self.report["marked_prime_reduction"]["profile_remainder"])
        self.assertTrue(self.report["barrier"]["k_wise_marginal_is_insufficient"])
        self.assertFalse(self.report["barrier"]["beyond_logarithmic_window"])
        self.assertFalse(self.report["claim_boundary"]["individual_L_function_zero"])
        self.assertEqual(self.report["resource_caps"]["zeros_enumerated"], 0)
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "represented by exactly `m_d` marked pairs",
            "Dropping the exclusion",
            "{I_q(d)\\over\\varphi(A)}",
            "\\ell_{2J+1}\\le{h-J\\over4}",
            "O_q(h^{-2})=O_q(M^{-2})",
            "adaptively correlated target",
            "no profile-count or asymptotic remainder",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        for q_value in (True, 2, 4):
            with self.assertRaises(ValueError):
                MODULE.irreducible_count(q_value, 3)
            with self.assertRaises(ValueError):
                MODULE.modulus_degree(q_value, 3)
        for degree in (True, 0):
            with self.assertRaises(ValueError):
                MODULE.irreducible_count(3, degree)
        with self.assertRaises(ValueError):
            MODULE.modulus_bounds_hold(3, MODULE.MAX_REPLAY_J + 1)
        with self.assertRaises(ValueError):
            MODULE.central_rademacher_atom(MODULE.MAX_CENTRAL_COUNT + 1)
        with self.assertRaises(ValueError):
            MODULE.layer_parameters(3, 1, 1)
        with self.assertRaises(ValueError):
            MODULE.marked_prime_signature(100, 1, -1)

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("logarithmic_depth_zero_firewall.v1", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
