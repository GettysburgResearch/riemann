import importlib.util
import unittest
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("verify105540", P)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class TestT105540(unittest.TestCase):
    def test_bezout(self):
        self.assertEqual(mod.bezout_polynomial_checks()["determinant"], "1")

    def test_operator_regression(self):
        x = mod.matrix_bank_checks(cases=80)
        self.assertEqual(x["exact_identities"], 240)

    def test_two_boundary(self):
        x = mod.two_boundary_checks()
        self.assertEqual(x["cancelled_total_degrees"], [1, 2])

    def test_threshold(self):
        self.assertEqual(mod.threshold_checks()["line_fraction_boundary"], "9/10")

    def test_fail_closed(self):
        x = mod.build_payload()
        self.assertTrue(x["bankreal105530_proved"])
        self.assertFalse(x["matrixlerc105541_proved"])
        self.assertFalse(x["ninety_percent_established"])
        self.assertFalse(x["public_record_beaten"])
        self.assertFalse(x["rh_established"])


if __name__ == "__main__":
    unittest.main()
