from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105310_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class T105310Tests(unittest.TestCase):
    def test_pick_kernel(self) -> None:
        row = MODULE.pick_kernel_fixture()
        self.assertEqual(row["checks"], 9)

    def test_confluent_budget(self) -> None:
        row = MODULE.confluent_budget_checks()
        self.assertEqual(row["nuisance_density"], "821/10000")

    def test_rank_trace(self) -> None:
        row = MODULE.rank_trace_checks()
        self.assertEqual(len(row["fixtures"]), 4)

    def test_record_arithmetic(self) -> None:
        row = MODULE.model_and_record_checks()
        self.assertEqual(row["multiplicity_counted_line_target"], "3369/5000")
        self.assertEqual(row["record_eta_target"], "919/1000")

    def test_fail_closed(self) -> None:
        payload = MODULE.build_payload()
        self.assertFalse(payload["lprt105310_proved"])
        self.assertFalse(payload["new_zero_proportion_established"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
