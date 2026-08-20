import importlib.util
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("t103100_verify", VERIFY)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class TestT103100(unittest.TestCase):
    def test_fail_closed(self):
        r = mod.build_result()
        self.assertEqual(r["verdict"], mod.PASS)
        self.assertTrue(r["diagonal_subpower_proved"])
        self.assertFalse(r["hcnc103100_proved"])
        self.assertFalse(r["rh_established"])

    def test_eta_square(self):
        count, digest = mod.source_checks(80, 11)
        self.assertEqual(count, 160)
        self.assertEqual(len(digest), 64)

    def test_autocorrelation_breakpoints(self):
        self.assertEqual(mod.autocorrelation_checks(), 6)

    def test_narrow_factorization(self):
        self.assertGreater(mod.narrow_factor_checks(), 0)


if __name__ == "__main__":
    unittest.main()
