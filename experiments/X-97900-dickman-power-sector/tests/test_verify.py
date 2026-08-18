import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

P = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("verify", P)
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class TestDickmanPacket(unittest.TestCase):
    def test_dickman_positive(self):
        for u in (1, 1.5, 2, 2.5, 3, 4):
            self.assertGreater(float(verify.dickman(u)), 0.0)

    def test_exposure(self):
        r = Fraction(7, 11)
        a = Fraction(2, 11)
        f = Fraction(13, 17)
        self.assertEqual((r-a)*f+a*f, r*f)

    def test_algebra_fixture(self):
        data = verify.exact_algebra_checks()
        self.assertTrue(data["two_node_current_negative"])
        self.assertTrue(data["scalar_transport_fixture"])


if __name__ == "__main__":
    unittest.main()
