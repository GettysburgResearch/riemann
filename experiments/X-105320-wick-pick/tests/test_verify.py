from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105320_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class T105320Tests(unittest.TestCase):
    def test_coefficient_bridge(self) -> None:
        row = MODULE.coefficient_bridge_checks()
        self.assertGreater(row["coefficient_derivative_checks"], 500)

    def test_wick_algebra(self) -> None:
        row = MODULE.wick_algebra_checks()
        self.assertEqual(row["coefficients"][:5], ["1", "0", "1/2", "1/3", "3/8"])

    def test_diagonal_bound(self) -> None:
        row = MODULE.diagonal_bound_checks()
        self.assertEqual(row["target_upper"], "7/320")

    def test_record_bridge(self) -> None:
        row = MODULE.record_checks()
        self.assertEqual(row["conditional_line_output"], "5765136493/8517835000")

    def test_fail_closed(self) -> None:
        payload = MODULE.build_payload()
        self.assertFalse(payload["wxfer105320_proved"])
        self.assertFalse(payload["new_zero_proportion_established"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
