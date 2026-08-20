import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class RecoveryReplayTests(unittest.TestCase):
    def test_replay(self):
        result = VERIFY.verify()
        core = result["core"]
        self.assertEqual(
            core["classification"],
            "PASS_T100400_TWO_SURVIVING_CLOSURE_ROUTES_RECOVERY",
        )
        self.assertFalse(core["rh_established"])
        self.assertTrue(core["open"]["QACG100400"])
        self.assertTrue(core["open"]["LPMW100410"])

    def test_negative_collar(self):
        self.assertGreater(VERIFY.shifted_square_checks(), 0)

    def test_largest_prime(self):
        self.assertGreater(VERIFY.largest_prime_checks(5000), 1000)

    def test_phase_identity(self):
        self.assertEqual(VERIFY.phase_hasse_checks(), 4)


if __name__ == "__main__":
    unittest.main()
