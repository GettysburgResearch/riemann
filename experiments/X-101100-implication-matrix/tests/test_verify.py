import importlib.util
import pathlib
import unittest
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("t101100_verify", VERIFY)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TestT101100(unittest.TestCase):
    def test_full_result_is_fail_closed(self):
        result = mod.build_result()
        self.assertEqual(result["verdict"], mod.PASS)
        self.assertFalse(result["subcritical_arithmetic_matrix_proved"])
        self.assertFalse(result["rh_established"])

    def test_critical_matrix_does_not_absorb(self):
        a, b, c, d = F(3,4), F(1,2), F(1,2), F(0)
        self.assertEqual((1-a)*(1-d)-b*c, 0)

    def test_activation_atom_is_load_bearing(self):
        s = F(2)
        That = 4/(s-F(1,2)) - 3/s
        Qhat = 16/(s-1) - 24/(s-F(1,2)) + 9/s
        self.assertEqual((s-1)*Qhat, 1+3*That)
        self.assertNotEqual((s-1)*Qhat, 3*That)

    def test_wrong_coefficient_three_fails(self):
        s = F(3)
        That = 4/(s-F(1,2)) - 3/s
        Qhat = 16/(s-1) - 24/(s-F(1,2)) + 9/s
        self.assertNotEqual((s-1)*Qhat, 1+2*That)


if __name__ == "__main__":
    unittest.main()
