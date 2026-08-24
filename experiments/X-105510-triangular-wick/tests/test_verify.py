from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("t105510_verify", PATH)
assert SPEC is not None and SPEC.loader is not None
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class T105510Tests(unittest.TestCase):
    def test_nilpotent_identity(self) -> None:
        self.assertEqual(
            VERIFY.triangular_identity_checks()["exact_nilpotent_matrix_cases"], 1000
        )

    def test_coefficients(self) -> None:
        result = VERIFY.coefficient_checks()
        self.assertEqual(result["q1"], "0")
        self.assertEqual(result["q2"], "0")
        self.assertEqual(result["q_m_ge_4"], "9/64")

    def test_energy_and_record(self) -> None:
        result = VERIFY.energy_and_record_checks()
        self.assertEqual(result["one_sided_energy_upper"], "1669/11698176")
        self.assertGreater(F(3654811, 3968189), F(23, 25))

    def test_fail_closed(self) -> None:
        payload = VERIFY.build_payload()
        self.assertFalse(payload["pnt_limit_machine_proved"])
        self.assertFalse(payload["triwxfer105510_proved"])
        self.assertFalse(payload["ninety_percent_established"])
        self.assertFalse(payload["record_beaten"])
        self.assertFalse(payload["rh_established"])


if __name__ == "__main__":
    unittest.main()
