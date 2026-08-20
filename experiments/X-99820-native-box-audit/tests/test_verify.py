import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class TestT99820(unittest.TestCase):
    def test_native_dictionary(self):
        self.assertGreater(VERIFY.check_native_label_dictionary(), 0)

    def test_normalization_mutation(self):
        out = VERIFY.check_normalization_mutation()
        self.assertLess(out["native_identity_abs_error"], 1e-10)
        self.assertGreater(out["wrong_operator_abs_error"], 1e-4)

    def test_collar(self):
        self.assertGreater(VERIFY.check_collar_dictionary(), 0)

    def test_hardy(self):
        self.assertEqual(VERIFY.check_hardy_fixtures(), 2000)


if __name__ == "__main__":
    unittest.main()
