import importlib.util
from pathlib import Path
import unittest

VERIFY = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("t105250_verify", VERIFY)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class TestHierarchy(unittest.TestCase):
    def test_verdict(self):
        p = module.compute()
        self.assertEqual(p["classification"], "PASS_T105250_POLYNOMIAL_WICK_HIERARCHY")
        self.assertFalse(p["actual_xi_transfer_proved"])
        self.assertFalse(p["ninety_percent_established"])
        self.assertFalse(p["density_one_established"])
        self.assertFalse(p["rh_established"])

    def test_degree_two(self):
        p = module.compute()
        self.assertEqual(p["degree_two_99_101_lower_bound"], "4997295529/5425779287")
        self.assertGreater(p["degree_two_99_101_decimal"], 0.92)


if __name__ == "__main__":
    unittest.main()
