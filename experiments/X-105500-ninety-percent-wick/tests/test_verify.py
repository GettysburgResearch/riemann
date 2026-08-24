from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105500_verify", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class T105500ReplayTests(unittest.TestCase):
    def test_full_signature_regression(self) -> None:
        result = VERIFY.full_signature_checks()
        self.assertEqual(result["total_exact_cases"], 8925)

    def test_wick_degree_two_cancellation(self) -> None:
        result = VERIFY.wick_algebra_checks()
        self.assertTrue(result["degree_one_cancelled"])
        self.assertTrue(result["degree_two_cancelled"])

    def test_energy_bound(self) -> None:
        result = VERIFY.energy_bound_checks()
        self.assertEqual(result["rational_upper"], "9181/9504000")
        self.assertLess(F(9181, 9504000), F(1, 1000))

    def test_ninety_percent_fraction(self) -> None:
        result = VERIFY.record_checks()
        self.assertEqual(result["conditional_line_fraction"], "1563433/1703567")
        self.assertGreater(F(1563433, 1703567), F(9, 10))

    def test_fail_closed_flags(self) -> None:
        payload = VERIFY.build_payload()
        self.assertFalse(payload["pnt_limit_machine_proved"])
        self.assertFalse(payload["montgomery_vaughan_transfer_machine_proved"])
        self.assertFalse(payload["w2xfer105500_proved"])
        self.assertFalse(payload["ninety_percent_established"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
