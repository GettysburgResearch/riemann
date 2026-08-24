from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

VERIFY_PATH = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105200_verify", VERIFY_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class T105200Tests(unittest.TestCase):
    def test_centered_defect_zero_mean(self) -> None:
        row = MODULE.centered_defect_fixture([F(1), F(3)], [F(2), F(7)])
        self.assertEqual(row["coefficient_mean"], "0")

    def test_coherence_bound_exhaustion(self) -> None:
        self.assertGreater(MODULE.coherence_exhaustion()["checks"], 500)

    def test_harmonic_recurrence(self) -> None:
        self.assertGreater(MODULE.harmonic_recurrence_checks()["checks"], 100)

    def test_moment_log_convexity(self) -> None:
        self.assertEqual(MODULE.moment_log_convexity_checks()["checks"], 24)

    def test_product_tail(self) -> None:
        self.assertEqual(MODULE.product_tail_checks()["checks"], 9)

    def test_o1_firewall(self) -> None:
        result = MODULE.nonsummable_o1_firewall(250)
        self.assertEqual(result["strict_growth_checks"], 250)

    def test_fail_closed_status(self) -> None:
        result = MODULE.build_result()
        self.assertFalse(result["analytic_saddle_estimates_machine_proved"])
        self.assertFalse(result["finite_prefix_controlled"])
        self.assertFalse(result["rpch104501_proved"])
        self.assertFalse(result["rh_established"])

    def test_verdict(self) -> None:
        self.assertEqual(MODULE.build_result()["verdict"], MODULE.VERDICT)


if __name__ == "__main__":
    unittest.main()
