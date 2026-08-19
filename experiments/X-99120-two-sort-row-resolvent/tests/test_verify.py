import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class TestResolvent(unittest.TestCase):
    def test_base(self):
        self.assertTrue(verify.verify_fixture()["passed"])

    def test_cycle(self):
        self.assertFalse(verify.verify_fixture("cycle")["passed"])

    def test_negative_current(self):
        self.assertFalse(verify.verify_fixture("negative_current")["passed"])

    def test_status(self):
        result = verify.build_result()
        self.assertFalse(result["rh_established"])
        self.assertEqual(result["abstract_theorem"], "PROVED_EXACT")


if __name__ == "__main__":
    unittest.main()
