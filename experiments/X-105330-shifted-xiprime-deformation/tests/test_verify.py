from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105330_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class T105330Tests(unittest.TestCase):
    def test_deformation(self) -> None:
        row = MODULE.deformation_fixture()
        self.assertEqual(row["critical_residues"], ["-7/12", "-1/12"])

    def test_coefficient_shift(self) -> None:
        row = MODULE.coefficient_shift_fixture()
        self.assertEqual(row["checks"], 18)

    def test_cauchy_transfer(self) -> None:
        row = MODULE.cauchy_transfer_fixture()
        self.assertEqual(row["analytic_majorant_checks"], 120)

    def test_reflection(self) -> None:
        row = MODULE.reflection_fixture()
        self.assertEqual(row["checks"], 3)

    def test_fail_closed(self) -> None:
        payload = MODULE.build_payload()
        self.assertFalse(payload["suef105330_proved"])
        self.assertFalse(payload["new_zero_proportion_established"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
