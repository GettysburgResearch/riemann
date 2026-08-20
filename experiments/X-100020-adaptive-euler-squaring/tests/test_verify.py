import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class TestT100020(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(
            verify.build_result()["verdict"],
            "PASS_T100020_FINITE_EULER_SQUARING_CORRIDOR",
        )

    def test_fail_closed(self):
        scope = verify.build_result()["scope"]
        self.assertTrue(scope["finite_corridor_proved"])
        self.assertFalse(scope["gfcp100020_proved"])
        self.assertFalse(scope["qpet100020_proved"])
        self.assertFalse(scope["rh_established"])

    def test_budget(self):
        checks = verify.build_result()["checks"]
        self.assertEqual(
            checks["sigma_margin_below_three_quarters"],
            "2262851/98982450",
        )


if __name__ == "__main__":
    unittest.main()
