import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)

class Tests(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(
            verify.build()["verdict"],
            "PASS_T99240_HOLOMORPHIC_DEFECT_FIXED_ROW_TRANSFER",
        )

    def test_fail_closed(self):
        r = verify.build()
        self.assertFalse(r["rh_established"])
        self.assertFalse(r["local_common_parent_inputs_replayed"])

    def test_mass(self):
        self.assertEqual(verify.build()["geometric_mass_bound"], "128/7")

    def test_nonzero_leading_term(self):
        self.assertEqual(verify.build()["noncancellation_fixture"], "-10/3")

if __name__ == "__main__":
    unittest.main()
