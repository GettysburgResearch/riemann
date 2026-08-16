from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("x91880_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

class TestT91880(unittest.TestCase):
    def test_baseline(self) -> None:
        result = MODULE.validate(MODULE.base_packet())
        self.assertEqual(result["native_total"], 60988)
        self.assertEqual(result["terminal_margin"], 581)
        self.assertEqual(result["child_mass"], "3/40")

    def test_q2_regression(self) -> None:
        result = MODULE.q2_obstruction()
        self.assertEqual(result["sign"], "negative")

    def test_many_to_one_first_owner_is_allowed(self) -> None:
        packet = MODULE.base_packet()
        self.assertLess(len(set(packet["first_owner"].values())), len(packet["first_owner"]))
        MODULE.validate(packet)

    def test_all_hostile_mutations_fail(self) -> None:
        for mutation in MODULE.MUTATIONS:
            with self.subTest(mutation=mutation):
                with self.assertRaises(MODULE.ContractError):
                    MODULE.validate(MODULE.base_packet(), mutation)

    def test_full_run(self) -> None:
        payload = MODULE.run(mutations=True)
        self.assertEqual(payload["classification"], MODULE.VERDICT)
        self.assertEqual(payload["hostile_mutations_rejected"], len(MODULE.MUTATIONS))

if __name__ == "__main__":
    unittest.main()
