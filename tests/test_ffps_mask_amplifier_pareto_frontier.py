"""Focused exact tests for the FFPS mask/amplifier Pareto packet."""

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
    / "ffps_mask_amplifier_pareto_frontier.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_mask_amplifier_pareto_frontier", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load mask/amplifier Pareto module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSMaskAmplifierParetoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.build_report()

    def test_exact_ternary_control(self) -> None:
        panel = self.report["panels"]["7_13"]
        row = self.report["design_points"]["ternary_7_13"]
        self.assertEqual(panel["A"], [14, 9])
        self.assertEqual(panel["B"], [91, 18])
        self.assertEqual(panel["u_star"], [5, 13])
        self.assertEqual(panel["leverage_star"], [648, 1183])
        self.assertEqual(row["u_selected_fourier_mass"], [1, 2])
        self.assertEqual(row["leverage"], [27, 49])
        self.assertEqual(row["unit_principal_minimum_cancellation_energy"], [2, 1])
        self.assertEqual(row["prime_order_exact_nonconstant_mode_count"], 2)

    def test_quadratic_and_ternary_same_panel_tradeoff(self) -> None:
        quadratic = self.report["design_points"]["quadratic_13_37"]
        ternary = self.report["design_points"]["ternary_13_37"]
        self.assertLess(
            Fraction(*ternary["leverage"]), Fraction(*quadratic["leverage"])
        )
        self.assertLess(
            Fraction(*ternary["u_selected_fourier_mass"]),
            Fraction(*quadratic["u_selected_fourier_mass"]),
        )
        self.assertGreater(
            ternary["prime_order_exact_nonconstant_mode_count"],
            quadratic["prime_order_exact_nonconstant_mode_count"],
        )
        self.assertEqual(ternary["leverage"], [54, 83])
        self.assertEqual(quadratic["leverage"], [216, 307])

    def test_continuous_optimum_has_zero_derivative(self) -> None:
        for panel in self.report["panels"].values():
            a_value = Fraction(*panel["A"])
            b_value = Fraction(*panel["B"])
            u_star = Fraction(*panel["u_star"])
            derivative_numerator = 2 * a_value - b_value + b_value * u_star
            self.assertEqual(derivative_numerator, 0)
            leverage = (1 + u_star) ** 2 / (a_value + b_value * u_star)
            self.assertEqual(leverage, Fraction(*panel["leverage_star"]))

    def test_strict_improvement_interval_is_exact(self) -> None:
        panel = self.report["panels"]["13_37"]
        a_value = Fraction(*panel["A"])
        b_value = Fraction(*panel["B"])
        endpoint = Fraction(*panel["strict_improvement_u_endpoint"])
        self.assertEqual(endpoint, (b_value - 2 * a_value) / a_value)
        at_endpoint = (1 + endpoint) ** 2 / (a_value + b_value * endpoint)
        self.assertEqual(at_endpoint, Fraction(*panel["complete_leverage"]))

    def test_invalid_or_ineligible_panels_fail_closed(self) -> None:
        for args in (
            ((7, 13), 2, 1),
            ((13, 37), 4, 2),
            ((13, 13), 3, 2),
            ((13, 37), 3, 3),
        ):
            with self.assertRaises(ValueError):
                MODULE.cyclic_design_point(*args)

    def test_dependency_blobs_and_note_contract(self) -> None:
        MODULE._check_dependency_blobs()
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "exact leverage/mode/anomaly Pareto frontier",
            "selected Kummer burden",
            "finite linear algebra",
            "conductor-uniform `CYSEL`",
            "RH or GRH",
        ):
            self.assertIn(marker, note)

    def test_optimized_mode_runs_same_checks(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=8.0,
        )
        self.assertIn("EXACT_CYCLIC_PARETO", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
